#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanobot_bayesian_n6_stratum_bias.py — F-NB-2-c source-class stratum bias.

Closes F-NB-2-c sub-clause (`.roadmap.nanobot` line 99 / 100;
schema `nanobot/spec/bayesian_audit_v2.schema.json`). Stratifies the
existing n=30 nano-machine corpus by reference year (proxy for
textbook-vs-experimental classes) and re-runs `log_bayes_factor`
within each stratum.

Stratum classifier (heuristic, reproducible):
  pre_2000  : reference year < 2000 (textbook/foundational)
  post_2000 : reference year >= 2000 (experimental/recent)

PASS gate: |log10_BF(stratum_a) − log10_BF(stratum_b)| ≤ 1.0
  PASS  → corpus is source-class-unbiased (stratum agreement within
          one Jeffreys band, acceptable curation hygiene).
  FAIL  → significant inter-stratum disagreement; corpus selection
          may be load-bearing → re-curate before promoting.

Per cross-cutting Require (R5) raw 9 hexa-only: **Python stdlib only.**

Usage:

    python3 nanobot_bayesian_n6_stratum_bias.py --summary
    python3 nanobot_bayesian_n6_stratum_bias.py --emit
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nanobot_bayesian_audit_n30 as nba  # noqa: E402

REGISTRY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "state",
    "discovery_absorption",
    "registry.jsonl",
)

YEAR_RE = re.compile(r"\b(19[5-9]\d|20[0-3]\d)\b")
PASS_DELTA = 1.0  # one Jeffreys band


def classify_entry(entry: dict) -> str:
    ref = entry.get("ref", "") or ""
    m = YEAR_RE.search(ref)
    if not m:
        return "unknown"
    year = int(m.group(1))
    return "pre_2000" if year < 2000 else "post_2000"


def stratum_audit(stratum_corpus: list[dict]) -> dict:
    if not stratum_corpus:
        return {
            "n": 0,
            "n_match": 0,
            "n_total": 0,
            "log10_bf": None,
            "log10_bf_sentinel": "empty_stratum",
        }
    bayes = nba.log_bayes_factor(stratum_corpus)
    n_match = sum(nba.n6_match_per_entry(e) for e in stratum_corpus)
    n_total = sum(nba._applicable_axes_per_entry(e) for e in stratum_corpus)
    lbf = bayes["log10_bayes_factor_h1_over_h0"]
    if lbf == float("inf"):
        return {"n": len(stratum_corpus), "n_match": n_match, "n_total": n_total,
                "log10_bf": None, "log10_bf_sentinel": "+inf"}
    if lbf == float("-inf"):
        return {"n": len(stratum_corpus), "n_match": n_match, "n_total": n_total,
                "log10_bf": None, "log10_bf_sentinel": "-inf"}
    return {"n": len(stratum_corpus), "n_match": n_match, "n_total": n_total,
            "log10_bf": lbf, "log10_bf_sentinel": None}


def compute_delta(a: dict, b: dict) -> tuple[float, str]:
    """Return (delta, method) where method describes the comparison."""
    a_lbf, b_lbf = a.get("log10_bf"), b.get("log10_bf")
    if a_lbf is None or b_lbf is None:
        # Fall back to match-fraction delta as a robust proxy.
        a_frac = (a["n_match"] / a["n_total"]) if a["n_total"] else 0.0
        b_frac = (b["n_match"] / b["n_total"]) if b["n_total"] else 0.0
        return abs(a_frac - b_frac) * 10.0, "match_fraction_proxy"  # roughly maps frac→bf scale
    return abs(a_lbf - b_lbf), "log10_bf_direct"


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="F-NB-2-c source-class stratum bias")
    p.add_argument("--emit", action="store_true")
    p.add_argument("--summary", action="store_true")
    args = p.parse_args(argv)

    nba.SIGMA_6, nba.TAU_6, nba.PHI_6, nba.J2 = 12, 4, 2, 24  # canonical
    corpus = nba.build_corpus_n30()
    strata = {"pre_2000": [], "post_2000": [], "unknown": []}
    for e in corpus:
        s = classify_entry(e)
        strata[s].append(e)

    audit_pre = stratum_audit(strata["pre_2000"])
    audit_post = stratum_audit(strata["post_2000"])
    audit_unknown = stratum_audit(strata["unknown"])

    delta, method = compute_delta(audit_pre, audit_post)
    verdict = "PASS" if delta <= PASS_DELTA else "FAIL"

    audited_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    witness = {
        "schema": "raw_77_nanobot_bayesian_audit_v2",
        "audited_at": audited_at,
        "audit_kind": "n6_source_class_stratum_bias",
        "stratum_classifier": "year_pre_post_2000",
        "stratum_results": {
            "pre_2000": audit_pre,
            "post_2000": audit_post,
            "unknown": audit_unknown,
        },
        "f_nb_2_subclauses": {
            "f_nb_2_c": {
                "verdict": verdict,
                "delta_log10_bf": delta,
                "delta_method": method,
                "pass_threshold": PASS_DELTA,
                "raw_91_c3_disclose": (
                    "Stratification by reference year (pre/post 2000) is a proxy "
                    "for textbook-vs-experimental source class — heuristic, "
                    "automatable. PASS = |delta log10_BF| <= 1.0 (one Jeffreys band) "
                    "between primary strata. Corpus n=30 may yield empty/small "
                    "strata; in that case match-fraction proxy is reported."
                ),
            },
        },
        "raw_91_c3_disclose": (
            "F-NB-2-c sub-clause closure runs alongside F-NB-2-n6-decorative "
            "(prior closure 2026-05-06). F-NB-2-b (n=60 ensemble drift) "
            "still pending corpus enlargement cycle 27."
        ),
        "raw_77_append_only": True,
        "witness_ref": "state/discovery_absorption/registry.jsonl#raw_77_nanobot_bayesian_audit_v2",
    }

    if args.emit:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(witness, ensure_ascii=False, sort_keys=True) + "\n")
        sys.stderr.write(f"emitted 1 witness row -> {REGISTRY_PATH}\n")

    if args.summary:
        print(json.dumps(witness, sort_keys=True, indent=2))
    else:
        sys.stderr.write(
            f"pre_2000 n={audit_pre['n']} log_bf={audit_pre.get('log10_bf')}  "
            f"post_2000 n={audit_post['n']} log_bf={audit_post.get('log10_bf')}  "
            f"delta={delta:.4f} ({method})  verdict={verdict}\n"
        )

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
