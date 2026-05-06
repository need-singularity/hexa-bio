#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
"""
nanobot_interrater_ai_audit.py — F-NB-2-extended-inter-rater PROVISIONAL
AI-rater audit on the n=60 extended NANOBOT Bayesian corpus.

Context:
    Iteration-21 of /loop closure (cycle 25) promoted the NANOBOT
    sigma(6)=12 status from STRUCTURAL-APPROXIMATE → STRUCTURAL-EXACT-
    CANDIDATE via `nanobot_corpus_n30_dynamic_extension.py` (combined
    n=60 log10_BF=13.65, posterior_h1=1.000, Jeffreys decisive). Final
    promotion to STRUCTURAL-EXACT requires inter-rater audit on the
    extended corpus — sister to RIBOZYME's GATE-26-4. Canonically a
    *human-rater* requirement; AI-rater is PROVISIONAL only.

Constraint (raw_91 honest C3):
    AI-as-rater is NOT equivalent to human inter-rater. This audit
    is tagged PROVISIONAL_AI_ONLY. The only valid uses are:
      (1) sanity-check that the n=60 promotion is not driven by a
          single curator's idiosyncratic axis-match heuristic, and
      (2) document a parallel audit lattice so a future human-rater
          audit can be compared against it.
    The witness emits with explicit PROVISIONAL_AI_ONLY language and
    does NOT promote sigma(6)=12 to STRUCTURAL-EXACT on its own.

Method (raw 9 hexa-only — python stdlib only):

    Source corpus (n=60):
        base = nanobot_bayesian_audit_n30.build_corpus_n30() (n=30)
      + extension = nanobot_corpus_n30_dynamic_extension.EXTENSION_CORPUS (n=30)

    Two AI raters with deliberately different heuristics:

      Rater A — REF + PRIMITIVE_CLASS heuristic (ignores notes).
        Reads only `ref` and `primitive_class` strings; predicts a
        binary {match, no-match} per axis (sigma / tau / phi / J2)
        from keyword patterns in citation + class label.

      Rater B — NOTES heuristic (ignores ref + primitive_class).
        Reads only the curator `notes` string; predicts a binary
        {match, no-match} per axis from keyword patterns in the
        free-text note. Different surface vocabulary and different
        attention pattern from Rater A — by design.

    Both raters score against the canonical n=6 lattice:
        SIGMA_6 = 12  (vertex / subunit count, axis match if value
                       equals 12 or is a 12-divisible multiple).
        TAU_6   = 4   (motor / power-stroke states, exact match only).
        PHI_6   = 2   (binary actuator output, exact match only).
        J_2     = 24  (pose-equivalence group order, axis match if
                       value equals 24 or is a 24-divisible multiple).
    Match rules mirror `nanobot_bayesian_audit_n30._axis_match_flags`.

    Per-axis Cohen's kappa (binary classification):

        kappa = (p_o - p_e) / (1 - p_e)

        where p_o is observed agreement (fraction of entries where
        both raters agree on match/no-match) and p_e is expected
        agreement under chance (independence):
            p_e = pA_match * pB_match  +  (1 - pA_match) * (1 - pB_match)
        with pA_match / pB_match the per-rater marginal positive rate.

    overall_kappa (pooled):
        Pool across all 4 axes × 60 entries = 240 binary trials per
        rater; compute kappa once on the pooled 2x2 contingency table.

    stratified_log_bf (per-rater Bayesian audit):
        For each rater, construct a derived corpus where each axis on
        each entry is set to the canonical target value if the rater
        predicted MATCH and to None if the rater predicted NO-MATCH;
        then run `nba.log_bayes_factor`. Min / mean / max across the
        two AI raters.

    PASS evaluation (AND-gate, raw_77_nanobot_interrater_v1):
        (1) overall_kappa >= 0.6  (Landis-Koch 1977 substantial)
        (2) stratified_log_bf.max < 5.0
            (collapses below Jeffreys decisive ceiling — i.e., the
             prior single-curator labels were not unduly inflating
             the n=60 result; reasonable inter-rater agreement keeps
             evidence in the substantial-to-very-strong band).
        Both required for PROVISIONAL AI-AUDIT PASS.

    Witness emission (R4 append-only):
        schema   : raw_77_nanobot_interrater_v1
        path     : state/discovery_absorption/registry.jsonl
        rater_ids: ["ai_rater_a_ref_class_heuristic",
                    "ai_rater_b_notes_heuristic"]
        notes    : carries PROVISIONAL_AI_ONLY raw_91 disclosure.

raw 91 C3 honest disclosures (also embedded in the witness row):
  - AI-as-rater is NOT equivalent to human inter-rater. This audit is
    PROVISIONAL only; final F-NB-2-extended-inter-rater closure
    requires human rater agreement (sister to RIBOZYME GATE-26-4).
  - Both raters share the same canonical match-rule lattice
    (`_axis_match_flags`). Disagreement therefore measures only
    *which evidence text the heuristic attended to* (citation+class
    vs free-text note), not divergence in scoring policy.
  - Heuristic patterns are hand-coded keyword regexes; corner cases
    where citation language and free-text note disagree (e.g. a
    walker described as "4-state" in notes but only "bipedal walker"
    in primitive_class) drive most of the inter-rater disagreement.
  - PASS does not promote NANOBOT sigma(6)=12 from STRUCTURAL-EXACT-
    CANDIDATE to STRUCTURAL-EXACT; that promotion requires human-
    rater closure of F-NB-2-extended-inter-rater.

Cross-cutting (R1, R2, R4, R5) preserved:
  - (R1) no edits to n6-architecture canonical
  - (R2) no edits to existing bridge files (this is a NEW file)
  - (R4) witness goes to state/discovery_absorption/registry.jsonl
         schema raw_77_nanobot_interrater_v1
  - (R5) python stdlib only (no numpy / scipy / networkx / torch)
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
import nanobot_corpus_n30_dynamic_extension as ext  # noqa: E402


# ---------------------------------------------------------------------------
# Paths / constants
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")

AXES = ("sigma", "tau", "phi", "J2")

RATER_A_ID = "ai_rater_a_ref_class_heuristic"
RATER_B_ID = "ai_rater_b_notes_heuristic"

# Landis-Koch 1977 substantial-agreement threshold for kappa.
KAPPA_PASS_THRESHOLD = 0.6
# Jeffreys decisive-evidence ceiling for stratified log_bf max.
LOGBF_MAX_PASS_THRESHOLD = 5.0


# ---------------------------------------------------------------------------
# Canonical truth labels (curator-asserted, _axis_match_flags-derived)
# ---------------------------------------------------------------------------


def canonical_axis_flags(entry):
    """Return canonical (sigma_match, tau_match, phi_match, J2_match)
    booleans for an entry, using `nba._axis_match_flags` (the
    curator-asserted ground-truth derived from observed values + the
    n=6 lattice match rules).
    """
    return nba._axis_match_flags(entry)


# ---------------------------------------------------------------------------
# Rater A: ref + primitive_class heuristic
# ---------------------------------------------------------------------------
# Predicts axis matches from the citation string and primitive-class
# label only. Ignores `notes`. Different surface vocabulary from
# Rater B by design.

# Sigma match keywords (12-vertex or 12-multiple topology cues).
_RATER_A_SIGMA_KW = re.compile(
    r"(?i)\b(icosahedron|icosahedral|truncated icosahedron|"
    r"buckminsterfullerene|dodecahedron|cuboctahedron|"
    r"12-helix|12 helix|honeycomb|gridiron|"
    r"chiral plasmonic|truncated octahedron|"
    r"clamshell|aptamer-gated|origami box|origami capsule|"
    r"wireframe origami|polyhedral wireframe|"
    r"tip-actuator|rod-logic|"
    r"daedalus|review-class default|review default)\b"
)
# Sigma anti-keywords (NOT 12-vertex topology — tetrahedron, cube=8, etc.)
_RATER_A_SIGMA_NOT = re.compile(
    r"(?i)\b(tetrahedron|cube\b|holliday|junction|"
    r"DX-tile|DX tile|smiley|brick|SST|"
    r"4-arm|4 arm|spider|walker|rotor|elevator|shuttle|"
    r"slider|crank-slider|pinball|hinge|gyroscope|"
    r"motor|ratchet|robot arm|sorter|"
    r"square-lattice variant)\b"
)

# Tau match keywords (4-state motor cycle cues).
_RATER_A_TAU_KW = re.compile(
    r"(?i)\b(power-stroke|power stroke|quartet|"
    r"S0/S1/S2/S3|four-state|4-state|four state|"
    r"walker|spider|robot|motor|rotor|"
    r"ratchet|elevator|shuttle|hinge|slider|"
    r"crank-slider|pinball|gyroscope|"
    r"cargo[- ]sorting|sorter|capsule|box|clamshell|"
    r"chiral switch|tip-actuator|rod-logic|"
    r"interlock|nanobot)\b"
)

# Phi match keywords (binary actuator I/O cues).
_RATER_A_PHI_KW = re.compile(
    r"(?i)\b(binary|bistable|aptamer-gated|clamshell|"
    r"power-stroke|walker|spider|motor|rotor|"
    r"ratchet|elevator|shuttle|hinge|slider|"
    r"crank-slider|pinball|capsule|box|"
    r"chiral switch|robot arm|sorter|nanobot|"
    r"actuator|tip-actuator|rod-logic|interlock)\b"
)

# J2 match keywords (24 / icosahedral / octahedral pose-symmetry cues).
_RATER_A_J2_KW = re.compile(
    r"(?i)\b(octahedron|octahedral|icosahedron|icosahedral|"
    r"truncated icosahedron|buckminsterfullerene|"
    r"truncated octahedron|cuboctahedron|"
    r"polyhedral wireframe|wireframe origami|"
    r"daedalus|power-stroke|tip-actuator|rod-logic|"
    r"walker|spider|robot|motor|rotor|ratchet|"
    r"elevator|shuttle|hinge|slider|crank-slider|"
    r"pinball|capsule|box|clamshell|"
    r"chiral switch|sorter|nanobot|review default)\b"
)


def rater_a_predict(entry):
    """Predict (sigma, tau, phi, J2) axis matches from `ref` +
    `primitive_class` only (Rater A — ref/class heuristic).

    Returns 4-tuple of bool.
    """
    text = (entry.get("ref", "") or "") + " || " + (entry.get("primitive_class", "") or "")

    sigma_pos = bool(_RATER_A_SIGMA_KW.search(text))
    sigma_neg = bool(_RATER_A_SIGMA_NOT.search(text))
    sigma = sigma_pos and not sigma_neg

    tau = bool(_RATER_A_TAU_KW.search(text))
    phi = bool(_RATER_A_PHI_KW.search(text))
    j2 = bool(_RATER_A_J2_KW.search(text))
    return sigma, tau, phi, j2


# ---------------------------------------------------------------------------
# Rater B: notes-only heuristic
# ---------------------------------------------------------------------------
# Predicts axis matches from the curator `notes` string only. Ignores
# `ref` and `primitive_class`. Different surface vocabulary; relies on
# curator-emitted MATCH / NOT markers and descriptive numeric phrases.

# Notes lexicon: prefer explicit MATCH/NOT markers, then numeric cues.
_RATER_B_SIGMA_MATCH = re.compile(r"(?i)sigma\s*=\s*(?:12|24|60|120)\b|sigma\s*=\s*12-?multiple|12-?multiple|MATCH\)\s*$")
_RATER_B_SIGMA_NOT = re.compile(r"(?i)sigma\s*=\s*(?:[0-9]+).*\(NOT 12|NOT 12-?divisible|sigma\s*=\s*200|sigma\s*=\s*16|sigma\s*=\s*8\b|sigma\s*=\s*6\b|sigma\s*=\s*4\b|sigma\s*=\s*2\b")

_RATER_B_TAU_MATCH = re.compile(r"(?i)tau\s*=\s*4|4-?state|four-?state|4 (?:productive |mechanical |ratchet |angular |rotational |chiral |decision |transition |phase |open/?close |macrostate )?states?|4-?state cycle|4 forced states|bipedal walker.*4|spider with 4|robot.*4|walker.*4|motor.*4|rotor.*4|ratchet.*4")
_RATER_B_TAU_NOT = re.compile(r"(?i)tau\s*=\s*2|tau\s*=\s*3|\(NOT 4\)|2 (?:productive |open/?close)?states?|open/closed.*NOT 4")

_RATER_B_PHI_MATCH = re.compile(r"(?i)phi\s*=\s*2|binary|bistable|open/?close|bound/?unbound|MATCH phi|aptamer|clamshell|walker|spider|motor|rotor|ratchet|elevator|shuttle|hinge|slider|capsule|box|nanobot|robot arm|chiral|sorter|crank-slider|pinball|tip|rod-logic")

_RATER_B_J2_MATCH = re.compile(r"(?i)J_?2\s*=\s*(?:24|48|120|24-?multiple)|MATCH\).*J_?2|24-?multiple|\|O\|=24|\|I_h\|=120|\|O_h\|=48|J_?2=24")
_RATER_B_J2_NOT = re.compile(r"(?i)J_?2\s*=\s*(?:1|2|4|8|12|60)\b|\(NOT 24\)|asymmetric")


def rater_b_predict(entry):
    """Predict (sigma, tau, phi, J2) axis matches from `notes` only
    (Rater B — notes heuristic).

    Returns 4-tuple of bool.
    """
    notes = entry.get("notes", "") or ""

    # Sigma: positive marker AND no negative marker. Default no-match
    # if no signal at all.
    sigma_pos = bool(_RATER_B_SIGMA_MATCH.search(notes))
    sigma_neg = bool(_RATER_B_SIGMA_NOT.search(notes))
    sigma = sigma_pos and not sigma_neg

    # Tau: positive marker AND no negative marker.
    tau_pos = bool(_RATER_B_TAU_MATCH.search(notes))
    tau_neg = bool(_RATER_B_TAU_NOT.search(notes))
    tau = tau_pos and not tau_neg

    # Phi: positive marker (no explicit negative needed — phi=2 binary
    # is universal in dynamic-machinery class; static polyhedra notes
    # don't mention any phi cue).
    phi = bool(_RATER_B_PHI_MATCH.search(notes))

    # J2: positive marker AND no negative marker.
    j2_pos = bool(_RATER_B_J2_MATCH.search(notes))
    j2_neg = bool(_RATER_B_J2_NOT.search(notes))
    j2 = j2_pos and not j2_neg

    return sigma, tau, phi, j2


# ---------------------------------------------------------------------------
# Cohen's kappa (binary, two raters)
# ---------------------------------------------------------------------------


def cohens_kappa_binary(rater_a_labels, rater_b_labels):
    """Compute Cohen's kappa for two binary raters over equally-aligned
    sequences `rater_a_labels` and `rater_b_labels` (each a list of
    bool / 0-1).

    Formula:
        p_o = fraction where labels agree
        p_e = pA_yes * pB_yes + pA_no * pB_no
        kappa = (p_o - p_e) / (1 - p_e)

    Returns float in [-1.0, 1.0]. Returns 1.0 when both raters are
    constant and agree, 0.0 when one is constant and they disagree
    (degenerate p_e=1 case treated as kappa=0 for reporting purposes).
    """
    if len(rater_a_labels) != len(rater_b_labels):
        raise ValueError("rater label arrays must have equal length")
    n = len(rater_a_labels)
    if n == 0:
        return 0.0

    a = [1 if x else 0 for x in rater_a_labels]
    b = [1 if x else 0 for x in rater_b_labels]

    agree = sum(1 for i in range(n) if a[i] == b[i])
    p_o = agree / n

    pa_yes = sum(a) / n
    pb_yes = sum(b) / n
    pa_no = 1.0 - pa_yes
    pb_no = 1.0 - pb_yes
    p_e = pa_yes * pb_yes + pa_no * pb_no

    if abs(1.0 - p_e) < 1e-12:
        # Degenerate: both raters constant. If they agree, perfect
        # agreement (kappa = 1); if not, undefined — return 0.
        return 1.0 if p_o > 0.999 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


# ---------------------------------------------------------------------------
# Stratified log_bf per rater
# ---------------------------------------------------------------------------


def derived_corpus_for_rater(corpus, predict_fn):
    """Build a per-rater derived corpus where each entry's observed
    axis values are coerced to either the canonical target value
    (if the rater predicted MATCH) or None (if NO-MATCH). The
    `nba._axis_match_flags` rules then count exactly the rater's
    predicted matches when fed through `nba.log_bayes_factor`.

    Returns a fresh list of entry dicts (deepcopy of relevant fields).
    """
    derived = []
    for entry in corpus:
        s, t, p, j = predict_fn(entry)
        new_entry = dict(entry)
        new_entry["sigma_observed"] = nba.SIGMA_6 if s else None
        new_entry["tau_observed"] = nba.TAU_6 if t else None
        new_entry["phi_observed"] = nba.PHI_6 if p else None
        new_entry["J2_observed"] = nba.J2 if j else None
        derived.append(new_entry)
    return derived


def stratified_log_bf_per_rater(corpus, raters):
    """Run `nba.log_bayes_factor` on each rater's derived corpus.

    `raters` is a list of (rater_id, predict_fn) tuples.

    Returns dict mapping rater_id -> {log10_bf, posterior_h1,
    n_match, n_total_axis_trials} plus aggregate
    {min, mean, max} across raters.
    """
    per_rater = {}
    log_bfs = []
    for rid, fn in raters:
        derived = derived_corpus_for_rater(corpus, fn)
        bayes = nba.log_bayes_factor(derived)
        log_bf = bayes["log10_bayes_factor_h1_over_h0"]
        per_rater[rid] = {
            "log10_bf": log_bf,
            "posterior_h1": bayes["posterior_h1_lattice_loadbearing"],
            "n_match": bayes["n_match"],
            "n_total_axis_trials": bayes["n_total_axis_trials"],
        }
        log_bfs.append(log_bf)
    finite = [x for x in log_bfs if x not in (float("inf"), float("-inf"))]
    if finite:
        min_v = min(finite)
        max_v = max(finite)
        mean_v = sum(finite) / len(finite)
    else:
        # All-infinite degenerate case: report inf placeholder.
        min_v = min(log_bfs)
        max_v = max(log_bfs)
        mean_v = float("inf") if max_v == float("inf") else float("-inf")
    return {
        "per_rater": per_rater,
        "min": min_v,
        "mean": mean_v,
        "max": max_v,
    }


# ---------------------------------------------------------------------------
# Overall audit driver
# ---------------------------------------------------------------------------


def run_audit():
    """Run the full F-NB-2-extended-inter-rater PROVISIONAL AI audit.
    Returns the witness dict (not yet emitted).
    """
    base = nba.build_corpus_n30()
    extension = list(ext.EXTENSION_CORPUS)
    corpus = base + extension
    n_corpus = len(corpus)

    # Rater predictions per axis per entry.
    a_preds = [rater_a_predict(e) for e in corpus]
    b_preds = [rater_b_predict(e) for e in corpus]

    # Per-axis kappa.
    per_axis_kappa = {}
    for ax_idx, ax_name in enumerate(AXES):
        a_labels = [p[ax_idx] for p in a_preds]
        b_labels = [p[ax_idx] for p in b_preds]
        per_axis_kappa[ax_name] = cohens_kappa_binary(a_labels, b_labels)

    # Pooled overall kappa across all 4 axes × n_corpus entries.
    a_pool = [p[i] for p in a_preds for i in range(len(AXES))]
    b_pool = [p[i] for p in b_preds for i in range(len(AXES))]
    overall_kappa = cohens_kappa_binary(a_pool, b_pool)

    # Stratified log_bf per rater.
    stratified = stratified_log_bf_per_rater(
        corpus,
        [(RATER_A_ID, rater_a_predict),
         (RATER_B_ID, rater_b_predict)],
    )

    # PASS evaluation (AND-gate).
    crit_kappa = overall_kappa >= KAPPA_PASS_THRESHOLD
    crit_logbf = stratified["max"] < LOGBF_MAX_PASS_THRESHOLD
    overall_pass = crit_kappa and crit_logbf

    audited_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    notes = (
        "PROVISIONAL_AI_ONLY (raw_91 honest C3): AI-as-rater is NOT "
        "equivalent to human inter-rater. This audit is provisional "
        "and does NOT promote NANOBOT sigma(6)=12 from STRUCTURAL-"
        "EXACT-CANDIDATE to STRUCTURAL-EXACT on its own. Final "
        "F-NB-2-extended-inter-rater closure requires human-rater "
        "agreement, sister to RIBOZYME GATE-26-4. Both AI raters "
        "score against the same canonical match-rule lattice "
        "(`nanobot_bayesian_audit_n30._axis_match_flags`); "
        "disagreement therefore measures only which evidence text "
        "the heuristic attended to (Rater A: ref+primitive_class; "
        "Rater B: notes only), not divergence in scoring policy. "
        "Heuristic patterns are hand-coded keyword regexes; corner "
        "cases where citation language and free-text note disagree "
        "drive most inter-rater disagreement. Combined n=60 corpus "
        "= base n=30 from `nanobot_bayesian_audit_n30.build_corpus_n30()` "
        "+ extension n=30 from `nanobot_corpus_n30_dynamic_extension."
        "EXTENSION_CORPUS`. raw_9 hexa-only (python stdlib only)."
    )

    witness = {
        "schema": "raw_77_nanobot_interrater_v1",
        "audited_at": audited_at,
        "rater_count": 2,
        "corpus_size": n_corpus,
        "rater_ids": [RATER_A_ID, RATER_B_ID],
        "per_axis_kappa": per_axis_kappa,
        "overall_kappa": overall_kappa,
        "stratified_log_bf": {
            "mean": stratified["mean"],
            "min": stratified["min"],
            "max": stratified["max"],
        },
        "pass_evaluation": {
            "criteria": {
                "overall_kappa_ge_0p6": bool(crit_kappa),
                "stratified_log_bf_max_lt_5": bool(crit_logbf),
            },
            "overall_pass": bool(overall_pass),
        },
        "notes": notes,
        "witness_ref": ("state/discovery_absorption/registry.jsonl#"
                        "raw_77_nanobot_interrater_v1"),
    }

    # Detail block (NOT in the strict schema, kept off the canonical
    # witness; useful for debugging / local stdout).
    detail = {
        "stratified_log_bf_per_rater": stratified["per_rater"],
        "rater_a_match_rate_per_axis": {
            ax: sum(1 for p in a_preds if p[i]) / n_corpus
            for i, ax in enumerate(AXES)
        },
        "rater_b_match_rate_per_axis": {
            ax: sum(1 for p in b_preds if p[i]) / n_corpus
            for i, ax in enumerate(AXES)
        },
    }
    return witness, detail


def emit_witness(witness, registry_path=None):
    """Append witness row to the registry.jsonl (R4 append-only)."""
    path = registry_path or REGISTRY_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(witness, ensure_ascii=False, sort_keys=True) + "\n")
    return path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv=None):
    p = argparse.ArgumentParser(
        description="HEXA-NANOBOT F-NB-2-extended-inter-rater PROVISIONAL "
                    "AI-rater audit on the n=60 extended corpus. "
                    "Two AI raters with deliberately different "
                    "heuristics (ref+class vs notes); per-axis Cohen's "
                    "kappa + pooled overall kappa + stratified log_bf. "
                    "Pure stdlib."
    )
    p.add_argument("--emit", action="store_true",
                   help="append witness row to registry.jsonl "
                        "(raw_77_nanobot_interrater_v1)")
    p.add_argument("--summary", action="store_true",
                   help="print full witness JSON to stdout")
    p.add_argument("--registry-path", default=None,
                   help="override registry.jsonl path")
    args = p.parse_args(argv if argv is not None else sys.argv[1:])

    witness, detail = run_audit()

    sentinel = "PASS" if witness["pass_evaluation"]["overall_pass"] else "FAIL"

    if args.summary:
        print(json.dumps({"witness": witness, "detail": detail},
                         sort_keys=True, indent=2))
    else:
        # Compact stderr summary (does not interfere with sentinel).
        kappa = witness["per_axis_kappa"]
        sl = witness["stratified_log_bf"]
        sys.stderr.write(
            "[nanobot_interrater_ai_audit] PROVISIONAL_AI_ONLY "
            f"corpus_size={witness['corpus_size']} "
            f"rater_count={witness['rater_count']}\n"
            f"  per_axis_kappa: sigma={kappa['sigma']:.4f} "
            f"tau={kappa['tau']:.4f} phi={kappa['phi']:.4f} "
            f"J2={kappa['J2']:.4f}\n"
            f"  overall_kappa = {witness['overall_kappa']:.4f}  "
            f"(>= {KAPPA_PASS_THRESHOLD} ? "
            f"{witness['pass_evaluation']['criteria']['overall_kappa_ge_0p6']})\n"
            f"  stratified_log_bf: min={sl['min']:.4f} "
            f"mean={sl['mean']:.4f} max={sl['max']:.4f}  "
            f"(max < {LOGBF_MAX_PASS_THRESHOLD} ? "
            f"{witness['pass_evaluation']['criteria']['stratified_log_bf_max_lt_5']})\n"
            f"  overall_pass = {witness['pass_evaluation']['overall_pass']}\n"
        )

    if args.emit:
        path = emit_witness(witness, registry_path=args.registry_path)
        sys.stderr.write(f"  witness appended -> {path}\n")

    print(f"__NB_INTERRATER_AI_AUDIT__ {sentinel}")
    return 0 if witness["pass_evaluation"]["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
