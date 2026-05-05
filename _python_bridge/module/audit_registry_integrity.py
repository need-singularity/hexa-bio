#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_registry_integrity.py — registry-integrity auditor for the HEXA-BIO
witness ledger at state/discovery_absorption/registry.jsonl.

This is a maintenance utility analogous to `git fsck`. It is READ-ONLY with
respect to existing registry rows: it never mutates, deletes, reorders, or
auto-fixes them. The only optional write is a single new audit-witness row
(schema raw_77_registry_audit_v1) appended to the same registry — append-only
under cross-cutting Require (R4). The audit row is meta-recursive but
well-defined: subsequent audit runs detect the prior audit row but exclude
themselves from the "subject" rows so the audit operates on the snapshot
present at invocation.

Seven integrity checks are performed:

  1. Every line is valid JSON (one row per line, no blanks, no garbage).
  2. Every row carries the required raw_77 schema fields:
        schema, ts, cycle, phase, raw_138_sentinel, raw_77_append_only=true.
  3. schema name follows pattern raw_77_<name>_v<n> (regex
     ^raw_77_[a-z0-9_]+_v[0-9]+$).
  4. ts is an ISO-8601 UTC parseable string ending Z (or +00:00).
  5. No duplicate (cycle, phase, ts) tuples exist (would indicate accidental
     double-emit of the same physical witness event).
  6. Per-schema row counts are reported (informational; gates only on
     non-empty result and recognized schema names).
  7. raw_138_sentinel content matches the expected per-schema pattern (e.g.
     a virocapsid_calibration row must carry "__VIROCAPSID_CALIBRATION__
     PASS" or " FAIL"). The audit-row schema itself uses the dedicated
     sentinel "__REGISTRY_AUDIT__ PASS|FAIL".

PASS criterion = all seven checks pass for the existing rows. The CLI exits
0 on PASS and 1 on FAIL.

Cross-cutting:
  - (R1) no n6-architecture/ canonical edits — N/A (none touched).
  - (R2) no edits to existing bridge files — N/A (this is a new file).
  - (R4) Witness → state/discovery_absorption/registry.jsonl raw_77 schema
    append-only. The audit-witness row uses raw_77_registry_audit_v1 and is
    appended at the tail; the script never seeks or rewrites earlier rows.
  - (R5) Python stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")

REQUIRED_FIELDS = ("schema", "ts", "cycle", "phase",
                   "raw_138_sentinel", "raw_77_append_only")

SCHEMA_NAME_PATTERN = re.compile(r"^raw_77_[a-z0-9_]+_v[0-9]+$")

# Per-schema sentinel-prefix expectations (raw_138_sentinel must start with
# the prefix and end with " PASS" or " FAIL"). The audit-row schema is added
# so that subsequent audit runs accept it as a recognized witness.
EXPECTED_SENTINEL_PREFIX = {
    "raw_77_virocapsid_calibration_v1": "__VIROCAPSID_CALIBRATION__",
    "raw_77_ribozyme_kinetics_v1":      "__RIBOZYME_MVP_RESULT__",
    "raw_77_nanobot_actuation_v1":      "__NANOBOT_MVP_RESULT__",
    "raw_77_c2_ribozyme_aml_v1":        "__R_ALPHA_AML_C2__",
    "raw_77_weave_pi_p2_v2_v1":         "__WEAVE_PI_P2_V2__",
    "raw_77_registry_audit_v1":         "__REGISTRY_AUDIT__",
}

# Schemas where the sentinel is row-kind dependent. weave_compose has both
# trial rows (__WEAVE_TRIAL__) and aggregate rows (__WEAVE_MVP_RESULT__).
WEAVE_TRIAL_PREFIX = "__WEAVE_TRIAL__"
WEAVE_AGG_PREFIX = "__WEAVE_MVP_RESULT__"

SENTINEL_TAIL_RE = re.compile(r" (PASS|FAIL)$")

AUDIT_SCHEMA = "raw_77_registry_audit_v1"
AUDIT_SENTINEL_PREFIX = "__REGISTRY_AUDIT__"


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_registry(path):
    """Read registry.jsonl line by line.

    Returns (rows, errors) where:
      rows   : list of dict, one per successfully parsed line, in file order.
      errors : list of (line_no, message) for lines that failed to parse.
    """
    rows = []
    errors = []
    if not os.path.exists(path):
        return rows, [(0, "registry file not found at " + path)]

    with open(path, "r", encoding="utf-8") as f:
        for i, raw in enumerate(f, start=1):
            stripped = raw.rstrip("\n")
            if not stripped.strip():
                # blank lines are flagged but do not abort
                errors.append((i, "blank line"))
                continue
            try:
                obj = json.loads(stripped)
            except json.JSONDecodeError as e:
                errors.append((i, "json decode error: " + str(e)))
                continue
            if not isinstance(obj, dict):
                errors.append((i, "row is not a JSON object"))
                continue
            rows.append(obj)
    return rows, errors


# ---------------------------------------------------------------------------
# Check 2: required fields
# ---------------------------------------------------------------------------

def check_required_fields(rows):
    """Per-row presence of required raw_77 schema fields.

    Returns dict with:
      per_row    : list of {field_name: bool, ...} aligned with rows[]
      missing    : list of (row_idx, [missing_fields])
      append_bad : list of row_idx where raw_77_append_only is not exactly True
      ok         : bool, True iff no missing and no bad append flag
    """
    per_row = []
    missing = []
    append_bad = []
    for idx, row in enumerate(rows):
        flags = {}
        miss = []
        for field in REQUIRED_FIELDS:
            present = field in row
            flags["has_" + field] = present
            if not present:
                miss.append(field)
        # raw_77_append_only must equal True (boolean), not just present.
        if row.get("raw_77_append_only") is not True:
            append_bad.append(idx)
            flags["has_append_only_flag"] = False
        else:
            flags["has_append_only_flag"] = True
        # convenience aliases for caller readability
        flags["has_sentinel"] = flags.get("has_raw_138_sentinel", False)
        per_row.append(flags)
        if miss:
            missing.append((idx, miss))
    return {
        "per_row": per_row,
        "missing": missing,
        "append_bad": append_bad,
        "ok": (len(missing) == 0 and len(append_bad) == 0),
    }


# ---------------------------------------------------------------------------
# Check 3: schema-name pattern
# ---------------------------------------------------------------------------

def check_schema_name_pattern(rows):
    """Return list of (row_idx, schema_value) that fail SCHEMA_NAME_PATTERN."""
    bad = []
    for idx, row in enumerate(rows):
        sch = row.get("schema")
        if not isinstance(sch, str) or not SCHEMA_NAME_PATTERN.match(sch):
            bad.append((idx, sch))
    return bad


# ---------------------------------------------------------------------------
# Check 4: ts ISO-8601 UTC parseable
# ---------------------------------------------------------------------------

def _parse_ts(ts):
    """Best-effort ISO-8601 parse. Accepts trailing Z or +00:00.

    Returns datetime or None on failure.
    """
    if not isinstance(ts, str):
        return None
    s = ts
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def check_ts_iso8601(rows):
    """Return list of (row_idx, ts_value) for rows with unparseable ts.

    A row passes if ts parses AND resolves to a UTC offset of zero
    (any +00:00 / Z form).
    """
    bad = []
    for idx, row in enumerate(rows):
        ts = row.get("ts")
        dt = _parse_ts(ts)
        if dt is None:
            bad.append((idx, ts))
            continue
        # require UTC (offset zero or naive-Z accepted via _parse_ts)
        if dt.utcoffset() is None or dt.utcoffset().total_seconds() != 0:
            bad.append((idx, ts))
    return bad


# ---------------------------------------------------------------------------
# Check 5: duplicate (cycle, phase, ts) tuples
# ---------------------------------------------------------------------------

def check_duplicates(rows):
    """Return list of duplicate (cycle, phase, ts) tuples that occur >1x.

    Each entry is (cycle, phase, ts, count, [row_idx,...]).
    weave_compose trial rows legitimately share (cycle, phase, ts) at the
    sub-second level for runs that emit the bundle in a tight loop —
    however those are still distinguished by the high-resolution ts
    (microsecond-precision Z suffix). Duplicates are therefore an actual
    integrity concern.
    """
    seen = {}
    for idx, row in enumerate(rows):
        key = (row.get("cycle"), row.get("phase"), row.get("ts"))
        seen.setdefault(key, []).append(idx)
    dups = []
    for key, idxs in seen.items():
        if len(idxs) > 1:
            dups.append((key[0], key[1], key[2], len(idxs), idxs))
    return dups


# ---------------------------------------------------------------------------
# Check 6: per-schema row counts
# ---------------------------------------------------------------------------

def per_schema_counts(rows):
    """Return Counter {schema: count}."""
    c = Counter()
    for row in rows:
        c[row.get("schema", "<missing>")] += 1
    return dict(c)


# ---------------------------------------------------------------------------
# Check 7: sentinel-line content matches schema's expected pattern
# ---------------------------------------------------------------------------

def check_sentinels(rows):
    """Return list of (row_idx, schema, sentinel) for rows whose sentinel
    does not match the expected per-schema pattern.

    Pattern rule:
      - Must be a string.
      - Must end with " PASS" or " FAIL".
      - For schemas in EXPECTED_SENTINEL_PREFIX, must start with the mapped
        prefix.
      - For raw_77_weave_compose_v1, prefix is __WEAVE_TRIAL__ when the
        row carries row_kind == "trial" and __WEAVE_MVP_RESULT__ when
        row_kind == "aggregate" (the only two row_kinds emitted by the
        weave bridge).
    """
    bad = []
    for idx, row in enumerate(rows):
        sch = row.get("schema")
        sent = row.get("raw_138_sentinel")
        if not isinstance(sent, str):
            bad.append((idx, sch, sent))
            continue
        if not SENTINEL_TAIL_RE.search(sent):
            bad.append((idx, sch, sent))
            continue
        if sch == "raw_77_weave_compose_v1":
            kind = row.get("row_kind")
            if kind == "trial":
                expected = WEAVE_TRIAL_PREFIX
            elif kind == "aggregate":
                expected = WEAVE_AGG_PREFIX
            else:
                bad.append((idx, sch, sent))
                continue
            if not sent.startswith(expected):
                bad.append((idx, sch, sent))
            continue
        expected = EXPECTED_SENTINEL_PREFIX.get(sch)
        if expected is None:
            # unrecognised schema — flag (will also fail schema-name check
            # if the name pattern itself is bad; here we just mark the
            # sentinel as unverified-against-known-pattern).
            bad.append((idx, sch, sent))
            continue
        if not sent.startswith(expected):
            bad.append((idx, sch, sent))
    return bad


# ---------------------------------------------------------------------------
# Aggregate audit
# ---------------------------------------------------------------------------

def run_audit(rows, parse_errors):
    """Run all seven checks and return a structured audit_result dict."""
    fields_result = check_required_fields(rows)
    schema_bad = check_schema_name_pattern(rows)
    ts_bad = check_ts_iso8601(rows)
    dups = check_duplicates(rows)
    counts = per_schema_counts(rows)
    sent_bad = check_sentinels(rows)

    # Check 6 passes if at least one row exists and every schema in counts
    # is recognised (matches the schema-name pattern). Empty registry is FAIL.
    counts_ok = (len(rows) > 0
                 and all(SCHEMA_NAME_PATTERN.match(s) for s in counts.keys()))

    checks = {
        "1_valid_json":      {"pass": (len(parse_errors) == 0),
                              "errors": parse_errors},
        "2_required_fields": {"pass": fields_result["ok"],
                              "missing": fields_result["missing"],
                              "append_bad": fields_result["append_bad"]},
        "3_schema_pattern":  {"pass": (len(schema_bad) == 0),
                              "violations": schema_bad},
        "4_ts_iso8601":      {"pass": (len(ts_bad) == 0),
                              "violations": ts_bad},
        "5_no_duplicates":   {"pass": (len(dups) == 0),
                              "duplicates": dups},
        "6_schema_counts":   {"pass": counts_ok, "counts": counts},
        "7_sentinel_match":  {"pass": (len(sent_bad) == 0),
                              "violations": sent_bad},
    }
    pass_count = sum(1 for c in checks.values() if c["pass"])
    overall_pass = (pass_count == len(checks))

    return {
        "n_rows_audited": len(rows),
        "n_parse_errors": len(parse_errors),
        "checks": checks,
        "pass_count": pass_count,
        "total_count": len(checks),
        "overall_pass": overall_pass,
    }


# ---------------------------------------------------------------------------
# Witness emission (raw_77_registry_audit_v1)
# ---------------------------------------------------------------------------

def emit_audit_witness(audit_result, registry_path=REGISTRY_PATH):
    """Append a single audit-witness row to the registry. Append-only."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pass_word = "PASS" if audit_result["overall_pass"] else "FAIL"

    counts = audit_result["checks"]["6_schema_counts"]["counts"]
    # JSON-serialisable summary of failures (truncate violation lists to
    # at most 8 entries each to keep the audit row bounded in size).
    def _trunc(seq, n=8):
        seq = list(seq)
        return seq[:n] + (["...(truncated)"] if len(seq) > n else [])

    summary = {}
    for k, v in audit_result["checks"].items():
        s = {"pass": v["pass"]}
        for sub in ("errors", "missing", "append_bad", "violations",
                    "duplicates"):
            if sub in v:
                s[sub + "_count"] = len(v[sub])
                s[sub + "_sample"] = _trunc(v[sub])
        if "counts" in v:
            s["counts"] = v["counts"]
        summary[k] = s

    row = {
        "schema": AUDIT_SCHEMA,
        "ts": ts,
        "cycle": 25,
        "phase": "registry-integrity-audit",
        "domain": "hexa-bio-meta",
        "falsifier": "F-REGISTRY-AUDIT",
        "tool": "audit_registry_integrity.py",
        "n_rows_audited": audit_result["n_rows_audited"],
        "n_parse_errors": audit_result["n_parse_errors"],
        "checks_summary": summary,
        "per_schema_counts": counts,
        "pass_evaluation": {
            "criteria": {k: v["pass"]
                         for k, v in audit_result["checks"].items()},
            "pass_count": audit_result["pass_count"],
            "total_count": audit_result["total_count"],
            "overall_pass": audit_result["overall_pass"],
        },
        "raw_138_sentinel": (AUDIT_SENTINEL_PREFIX + " " + pass_word),
        "raw_91_c3_disclose": (
            "Read-only integrity audit of registry.jsonl. The audit row "
            "itself is appended after the audit completes; subsequent "
            "audit runs treat prior audit rows as ordinary witness rows "
            "and validate them under the raw_77_registry_audit_v1 schema "
            "(prefix __REGISTRY_AUDIT__ + PASS|FAIL). The auditor never "
            "modifies, reorders, or deletes existing rows; on FAIL it "
            "reports diagnostics only — no auto-fix."
        ),
        "raw_47_cross_repo": (
            "Self-contained stdlib auditor; no shared state with sister "
            "bridge modules (cage_assembly_simulation, "
            "polyhedral_cage_bayesian_audit, virocapsid_calibration, "
            "ribozyme_kinetics_simulation, nanobot_actuation_simulation, "
            "weave_composition, ribozyme_aml_flt3_candidate)."
        ),
        "raw_9_hexa_only":
            "python stdlib only — no scipy / no numpy / no jsonschema",
        "raw_53_deterministic":
            "7 of 7 PASS criteria deterministic at fixed registry snapshot",
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(registry_path), exist_ok=True)
    with open(registry_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


# ---------------------------------------------------------------------------
# Reporter
# ---------------------------------------------------------------------------

def format_report(audit_result, quiet=False):
    """Build a human-readable per-check pass/fail report."""
    lines = []
    lines.append("=" * 72)
    lines.append("registry integrity audit — "
                 + REGISTRY_PATH)
    lines.append("=" * 72)
    lines.append("rows audited      : " + str(audit_result["n_rows_audited"]))
    lines.append("parse errors      : " + str(audit_result["n_parse_errors"]))
    lines.append("")

    checks = audit_result["checks"]
    label = {
        "1_valid_json":      "1. valid JSON / one row per line",
        "2_required_fields": "2. required raw_77 fields present",
        "3_schema_pattern":  "3. schema name pattern raw_77_*_v<n>",
        "4_ts_iso8601":      "4. ts ISO-8601 UTC parseable",
        "5_no_duplicates":   "5. no duplicate (cycle, phase, ts)",
        "6_schema_counts":   "6. per-schema row counts (recognised)",
        "7_sentinel_match":  "7. sentinel matches schema pattern",
    }
    for key in ("1_valid_json", "2_required_fields", "3_schema_pattern",
                "4_ts_iso8601", "5_no_duplicates", "6_schema_counts",
                "7_sentinel_match"):
        c = checks[key]
        mark = "PASS" if c["pass"] else "FAIL"
        lines.append("  [" + mark + "] " + label[key])
        if not c["pass"] and not quiet:
            for sub in ("errors", "missing", "append_bad", "violations",
                        "duplicates"):
                if sub in c and c[sub]:
                    lines.append("        " + sub + " (" + str(len(c[sub]))
                                 + "):")
                    for item in c[sub][:5]:
                        lines.append("          " + repr(item))
                    if len(c[sub]) > 5:
                        lines.append("          ...("
                                     + str(len(c[sub]) - 5) + " more)")
        if key == "6_schema_counts" and not quiet:
            for sch, n in sorted(c["counts"].items()):
                lines.append("        " + sch + ": " + str(n))

    lines.append("")
    lines.append("pass_count        : " + str(audit_result["pass_count"])
                 + " / " + str(audit_result["total_count"]))
    lines.append("overall           : "
                 + ("PASS" if audit_result["overall_pass"] else "FAIL"))
    lines.append("=" * 72)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="HEXA-BIO registry integrity auditor (raw_77 ledger). "
                    "Read-only; reports only; optional audit-witness emit."
    )
    ap.add_argument("--no-emit", action="store_true",
                    help="skip writing the audit-witness row to registry")
    ap.add_argument("--quiet", action="store_true",
                    help="suppress per-violation detail listings")
    ap.add_argument("--registry", default=REGISTRY_PATH,
                    help="override registry path (default: " + REGISTRY_PATH
                         + ")")
    args = ap.parse_args()

    rows, parse_errors = parse_registry(args.registry)
    audit_result = run_audit(rows, parse_errors)

    print(format_report(audit_result, quiet=args.quiet))

    if not args.no_emit:
        # Audit row is appended AFTER the audit completes — meta-recursive
        # but well-defined: this row is not in the snapshot just audited.
        emit_audit_witness(audit_result, registry_path=args.registry)
        if not args.quiet:
            print("audit witness appended to "
                  + os.path.relpath(args.registry, ROOT_DIR))

    # Sentinel echoed for grep-friendly downstream tooling.
    pass_word = "PASS" if audit_result["overall_pass"] else "FAIL"
    print(AUDIT_SENTINEL_PREFIX + " " + pass_word)

    sys.exit(0 if audit_result["overall_pass"] else 1)


if __name__ == "__main__":
    main()
