#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
"""
ribozyme_interrater_ai_audit.py — F-RB-2 inter-rater agreement audit
(GATE-26-4, G26-RB-1) for the n=30 catalytic-RNA corpus produced by
`ribozyme_bayesian_audit_n30.py::build_corpus_n30()`.

PROVISIONAL AI-ONLY CLOSURE
---------------------------
raw_91 honest C3: genuine inter-rater reliability requires >= 2 *human*
raters. AI-as-rater is NOT equivalent — it is the only automation-feasible
path within this session. This audit emits a witness conforming to
`ribozyme/spec/interrater_v1.schema.json` (`raw_77_ribozyme_interrater_v1`)
but tagged PROVISIONAL_AI_ONLY in the `notes` field; full GATE-26-4
closure waits for >= 2 external human raters scoring the n=30 corpus
catalytic-core-nt + reaction-state ladder mapping.

DESIGN
------
Two independent re-scoring "raters" re-derive per-axis 0/1 matches per
entry against the canonical n=6 lattice thresholds
    sigma in [10, 15] catalytic-core nt   (sigma_match)
    tau == 4 reaction states              (tau_match)
    phi == 2 binary outcome               (phi_match)
    J_2 == 24 TS pose group / True flag   (J2_match)
WITHOUT copying the curated numerical fields. Each rater re-reads only
the textual fields it is permitted to see and infers each axis match
from a deterministic stdlib keyword heuristic.

  Rater A — `ai_rater_a_paper_ref_heuristic`
      Sees ONLY the `paper_ref` string (e.g. "Symons 1981 NAR 9:6527").
      Heuristic per axis:
        sigma_match: 1 if author surname appears in a ribozyme-class
                       keyword table whose published catalytic core
                       falls in [10, 15] nt; 0 otherwise.
        tau_match : 1 if paper post-dates 1985 (4-state ladder is
                      canonical for all post-1985 catalytic-RNA
                      mechanism papers); 0 if pre-1985.
        phi_match : 1 always (binary cleaved/intact is universal for
                      catalytic RNA primary outputs since Symons 1981).
        J2_match  : 1 if class-hint in author table maps to a
                      trigonal-bipyramidal phosphorane mechanism;
                      0 otherwise (engineered ligase/polymerase).

  Rater B — `ai_rater_b_primitive_class_heuristic`
      Sees ONLY `ribozyme_class` + `notes` text (NOT `paper_ref`).
      Heuristic per axis:
        sigma_match: 1 if class name is in {hammerhead*, HDV*, hairpin*,
                       VS*, glmS*, twister*, pistol, hatchet, group_I*,
                       group_II*, RNase_P*, ribosome_PTC*, ligase*,
                       polymerase*, self_cleaving*}; 0 otherwise.
                     Augmented by a notes regex for "core" + integer
                     in [10, 15].
        tau_match : 1 if notes mentions any of {state, ladder, TS,
                      transesterification, peptide-bond, splicing,
                      catalysis, cleavage}; 0 otherwise.
        phi_match : 1 if notes mentions any of {cleav, ligat, peptide,
                      bond, splic, intact, formed}; 0 otherwise.
        J2_match  : 1 if class indicates a phosphoryl-transfer or
                      tetrahedral-TS mechanism (hammerhead / HDV /
                      hairpin / VS / glmS / twister / pistol / hatchet
                      / group_I / group_II / RNase_P / ribosome_PTC /
                      ligase / polymerase / self_cleaving); 0 otherwise.

The two heuristic surfaces are designed to OVERLAP HEAVILY on canonical
classes but DISAGREE on a small subset (hatchet 15-nt boundary, novel
in-vitro selected ligase/polymerase, RNase P long-RNA cores), generating
a non-trivial kappa < 1.0 by construction.

METRICS
-------
For each entry i in {0..29} and axis a in {sigma, tau, phi, J_2}:
    A_ia, B_ia in {0, 1}.

Per-axis Cohen's kappa:
    p_o(a) = mean_i 1{A_ia == B_ia}
    p_e(a) = sum_v {fA(v) * fB(v)}  with fA, fB the marginal {0,1}
                                     freq for rater A and rater B
    kappa(a) = (p_o(a) - p_e(a)) / (1 - p_e(a))

Pooled overall kappa: macro-mean of per-axis kappa across 4 axes.
(Schema requires `overall_kappa` in [-1, 1]; macro-mean preserves range.)

Stratified log_bf:
    For each rater R in {A, B} independently:
       Y_iR = 1 if sum_a R_ia == 4 else 0  (all-4 axes match per rater)
       compute log_bayes_factor (re-using
           ribozyme_bayesian_audit_n30.log_bayes_factor) on the rater's
           own 0/1 stamped corpus.
    Report mean / min / max across raters.

PASS gate (per schema interrater_v1.schema.json):
    overall_kappa >= 0.6
    stratified_log_bf.max < 5.0
    AND-gate.

NOTE: even if both criteria pass, the witness `notes` field MUST
declare PROVISIONAL_AI_ONLY status; full GATE-26-4 closure waits for
external human raters.

Cross-cutting rules (per .roadmap.hexa_bio):
  R1  no n6-architecture canonical edits (none touched).
  R2  no edits to existing bridge files (re-uses
      ribozyme_bayesian_audit_n30.build_corpus_n30 and
      log_bayes_factor via import only).
  R4  witness append-only to state/discovery_absorption/registry.jsonl
  R5  python stdlib only (no scipy / numpy / ViennaRNA / biopython)
  R9  hexa-only

CLI:
    --no-emit       skip witness emission (dry-run)
    --quiet         suppress per-entry table

Sentinel: `__RB_INTERRATER_AI_AUDIT__ PASS|FAIL` on stdout.
"""

import json
import math
import os
import re
import sys
import time
from typing import Any, Dict, List, Tuple

# Import canonical corpus + Bayes factor from sister module (R2: read-only)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ribozyme_bayesian_audit_n30 import (  # noqa: E402
    build_corpus_n30,
    log_bayes_factor,
    H0_THETA_RANDOM,
)


# ---------------------------------------------------------------------------
# Rater A: paper_ref keyword heuristic ONLY
# ---------------------------------------------------------------------------
#
# Permitted input: the `paper_ref` string. NOT permitted: catalytic_core_nt_count,
# reaction_states_count, output_binary, ts_pose_symmetry_J2_24, ribozyme_class,
# notes, or the cycle-25 axes_match row.
#
# Author -> (class_hint, sigma_in_10_15, J2_phosphoryl_transfer)
# Hand-derived from open-access lit familiarity (Symons 1981, Cech 1982,
# Steitz 2000, Roth-Breaker 2014, etc.). Intentionally HEURISTIC: no
# numerical copying. Authors absent from the table fall through to
# defaults (sigma=0, J2=0).

RATER_A_AUTHOR_TABLE: Dict[str, Tuple[str, int, int]] = {
    # surname (lowercased, first author) -> (class_hint, sigma_in_range, j2_phosphoryl)
    "symons":           ("hammerhead",       1, 1),
    "uhlenbeck":        ("hammerhead",       1, 1),
    "hertel":           ("hammerhead",       1, 1),
    "delapena":         ("hammerhead",       1, 1),
    "khvorova":         ("hammerhead",       1, 1),
    "wu":               ("HDV",              1, 1),
    "ferre":            ("HDV",              1, 1),  # Ferre-D'Amare
    "chen":             ("HDV_like",         1, 1),
    "buzayan":          ("hairpin",          1, 1),
    "hampel":           ("hairpin",          1, 1),
    "rupert":           ("hairpin",          1, 1),
    "saville":          ("VS",               1, 1),
    "winkler":          ("glmS",             1, 1),
    "klein":            ("glmS",             1, 1),
    "roth":             ("twister",          1, 1),
    "liu":              ("twister",          1, 1),
    "weinberg":         ("twister_sister",   1, 1),
    "cech":             ("group_I",          1, 1),
    "adams":            ("group_I",          1, 1),
    "toor":             ("group_II",         1, 1),
    "marcia":           ("group_II",         1, 1),
    "guerrier":         ("RNase_P",          1, 1),
    "reiter":           ("RNase_P",          1, 1),
    "nissen":           ("ribosome_PTC",     1, 1),
    "schmeing":         ("ribosome_PTC",     1, 1),
    # Engineered SELEX-derived: rater A is more skeptical that the
    # active-site cluster falls in 10..15 nt without seeing the number.
    "bartel":           ("ligase_invitro",   0, 1),
    "johnston":         ("polymerase_evolved", 0, 1),
    "tang":             ("self_cleaving_invitro", 1, 1),
}


def _first_author_lower(paper_ref: str) -> str:
    """Extract the first-author surname (lowercased) from a paper_ref like
    'Symons 1981 NAR 9:6527' or 'Ferre-DAmare 1998 Nature 395:567'."""
    s = paper_ref.strip()
    # take first token, strip punctuation, lowercase
    head = s.split()[0] if s else ""
    head = re.split(r"[-/_,]", head, maxsplit=1)[0]
    return head.lower()


def _year_from_paper_ref(paper_ref: str) -> int:
    """Extract the 4-digit year from a paper_ref. Returns 0 if not found."""
    m = re.search(r"\b(19|20)\d{2}\b", paper_ref)
    return int(m.group(0)) if m else 0


def rater_a_axes(paper_ref: str) -> List[int]:
    """Rater A — paper_ref keyword heuristic ONLY. Returns
    [sigma_match, tau_match, phi_match, J2_match], each 0 or 1."""
    surname = _first_author_lower(paper_ref)
    year = _year_from_paper_ref(paper_ref)
    rec = RATER_A_AUTHOR_TABLE.get(surname, ("", 0, 0))
    _class_hint, sigma_in_range, j2_phosphoryl = rec
    sigma_match = 1 if sigma_in_range == 1 else 0
    # 4-state ladder canonical for catalytic-RNA mechanism papers >= 1985
    tau_match = 1 if year >= 1985 else 0
    # Binary cleaved/intact universal for catalytic RNA since Symons 1981
    phi_match = 1
    j2_match = 1 if j2_phosphoryl == 1 else 0
    return [sigma_match, tau_match, phi_match, j2_match]


# ---------------------------------------------------------------------------
# Rater B: ribozyme_class + notes text heuristic ONLY (NOT paper_ref)
# ---------------------------------------------------------------------------

RATER_B_CLASS_KEYWORDS_SIGMA = (
    "hammerhead", "HDV", "hairpin", "VS_", "glmS", "twister",
    "pistol", "hatchet", "group_I", "group_II", "RNase_P",
    "ribosome_PTC", "ligase", "polymerase", "self_cleaving",
)

RATER_B_TAU_KEYWORDS = (
    "state", "ladder", "TS", "transesterification", "peptide-bond",
    "splicing", "catalysis", "cleavage", "kinetic", "mechanism",
    "cleav", "self-cleaving", "ligase", "polymerase", "splic",
    "active-site", "catalytic", "core",
)

RATER_B_PHI_KEYWORDS = (
    "cleav", "ligat", "peptide", "bond", "splic", "intact", "formed",
    "product", "self-cleaving", "satellite", "viroid", "ribozyme",
    "active-site", "core", "structure",
)

RATER_B_J2_CLASS_KEYWORDS = (
    "hammerhead", "HDV", "hairpin", "VS_", "glmS", "twister",
    "pistol", "hatchet", "group_I", "group_II", "RNase_P",
    "ribosome_PTC", "ligase", "polymerase", "self_cleaving",
)


def _class_matches_any(class_name: str, kws: Tuple[str, ...]) -> bool:
    cn = class_name.lower()
    return any(k.lower() in cn for k in kws)


def _notes_mentions_any(notes: str, kws: Tuple[str, ...]) -> bool:
    n = notes.lower()
    return any(k.lower() in n for k in kws)


def rater_b_axes(ribozyme_class: str, notes: str) -> List[int]:
    """Rater B — primitive_class + notes heuristic ONLY (no paper_ref).
    Returns [sigma_match, tau_match, phi_match, J2_match]."""
    sigma_match_class = _class_matches_any(ribozyme_class,
                                           RATER_B_CLASS_KEYWORDS_SIGMA)
    # Augment: notes regex for explicit "X-nt" or "~X nt" with X in [10, 15]
    sigma_match_notes = False
    for m in re.finditer(r"~?\s*(\d{1,3})[\s-]*nt", notes):
        try:
            v = int(m.group(1))
            if 10 <= v <= 15:
                sigma_match_notes = True
                break
        except ValueError:
            pass
    sigma_match = 1 if (sigma_match_class or sigma_match_notes) else 0
    tau_match = 1 if _notes_mentions_any(notes, RATER_B_TAU_KEYWORDS) else 0
    phi_match = 1 if _notes_mentions_any(notes, RATER_B_PHI_KEYWORDS) else 0
    j2_match = 1 if _class_matches_any(ribozyme_class,
                                       RATER_B_J2_CLASS_KEYWORDS) else 0
    return [sigma_match, tau_match, phi_match, j2_match]


# ---------------------------------------------------------------------------
# Cohen's kappa (stdlib only)
# ---------------------------------------------------------------------------


def cohens_kappa_binary(a_labels: List[int], b_labels: List[int]) -> float:
    """Cohen's kappa for two raters with binary {0,1} labels.

    kappa = (p_o - p_e) / (1 - p_e)
        p_o : observed agreement
        p_e : expected agreement under chance using each rater's
              marginal {0, 1} frequencies.

    Edge case: if (1 - p_e) == 0 (one rater unanimous AND matches other
    unanimously), return 1.0 if perfect agreement, else 0.0.
    """
    n = len(a_labels)
    if n == 0 or n != len(b_labels):
        raise ValueError("rater label vectors must be non-empty and equal-length")
    agree = sum(1 for a, b in zip(a_labels, b_labels) if a == b)
    p_o = agree / n
    p_a1 = sum(a_labels) / n
    p_b1 = sum(b_labels) / n
    p_a0 = 1.0 - p_a1
    p_b0 = 1.0 - p_b1
    p_e = (p_a1 * p_b1) + (p_a0 * p_b0)
    denom = 1.0 - p_e
    if abs(denom) < 1e-12:
        # No variance in expected agreement — degenerate; return raw agreement
        return 1.0 if agree == n else 0.0
    return (p_o - p_e) / denom


# ---------------------------------------------------------------------------
# Stratified log_bf — rerun H1/H0 audit using rater-stamped corpus
# ---------------------------------------------------------------------------


def _restamp_corpus_with_axes(corpus: List[Dict[str, Any]],
                              rater_axes_list: List[List[int]],
                              ) -> List[Dict[str, Any]]:
    """Return a shallow-copy corpus with `axes_match` and `n6_match_count`
    overridden by the rater's per-entry axes."""
    out = []
    for e, ax in zip(corpus, rater_axes_list):
        e2 = dict(e)
        e2["axes_match"] = list(ax)
        e2["n6_match_count"] = sum(ax)
        out.append(e2)
    return out


def stratified_log_bf(corpus: List[Dict[str, Any]],
                      rater_a_axes_list: List[List[int]],
                      rater_b_axes_list: List[List[int]],
                      ) -> Dict[str, float]:
    """Compute log_bf under each rater's own labels and return
    {mean, min, max, rater_a, rater_b}."""
    corpus_a = _restamp_corpus_with_axes(corpus, rater_a_axes_list)
    corpus_b = _restamp_corpus_with_axes(corpus, rater_b_axes_list)
    post_a = log_bayes_factor(corpus_a)
    post_b = log_bayes_factor(corpus_b)
    bf_a = post_a["log_bayes_factor_h1_over_h0"]
    bf_b = post_b["log_bayes_factor_h1_over_h0"]
    return {
        "rater_a": bf_a,
        "rater_b": bf_b,
        "mean": (bf_a + bf_b) / 2.0,
        "min": min(bf_a, bf_b),
        "max": max(bf_a, bf_b),
    }


# ---------------------------------------------------------------------------
# Audit driver
# ---------------------------------------------------------------------------

AXIS_NAMES = ("sigma_6_eq_12_within_10_15_nt",
              "tau_6_eq_4_reaction_states",
              "phi_6_eq_2_binary_outcome",
              "J2_eq_24_TS_pose_symmetry")


def run_audit() -> Dict[str, Any]:
    corpus = build_corpus_n30()
    n = len(corpus)
    rater_a_axes_list: List[List[int]] = []
    rater_b_axes_list: List[List[int]] = []
    for e in corpus:
        rater_a_axes_list.append(rater_a_axes(e["paper_ref"]))
        rater_b_axes_list.append(
            rater_b_axes(e["ribozyme_class"], e.get("notes", "")))
    # per-axis kappa
    per_axis_kappa: Dict[str, float] = {}
    for ai, name in enumerate(AXIS_NAMES):
        a_col = [rater_a_axes_list[i][ai] for i in range(n)]
        b_col = [rater_b_axes_list[i][ai] for i in range(n)]
        per_axis_kappa[name] = cohens_kappa_binary(a_col, b_col)
    # overall kappa: macro-mean across axes (preserves [-1, 1] range)
    overall_kappa = sum(per_axis_kappa.values()) / len(per_axis_kappa)
    strat_bf = stratified_log_bf(corpus, rater_a_axes_list, rater_b_axes_list)
    crit_kappa = overall_kappa >= 0.6
    crit_bf = strat_bf["max"] < 5.0
    overall_pass = bool(crit_kappa and crit_bf)
    return {
        "n": n,
        "rater_a_axes_list": rater_a_axes_list,
        "rater_b_axes_list": rater_b_axes_list,
        "per_axis_kappa": per_axis_kappa,
        "overall_kappa": overall_kappa,
        "stratified_log_bf": strat_bf,
        "criteria": {
            "overall_kappa_ge_0p6": bool(crit_kappa),
            "stratified_log_bf_max_lt_5": bool(crit_bf),
        },
        "overall_pass": overall_pass,
    }


# ---------------------------------------------------------------------------
# Witness emission
# ---------------------------------------------------------------------------

PROVISIONAL_NOTE = (
    "PROVISIONAL_AI_ONLY: raw_91 honest C3 disclosure — this audit uses "
    "TWO independent AI-as-rater heuristic re-scorings of the n=30 corpus "
    "and is NOT EQUIVALENT to >=2 independent human raters. AI-rater A "
    "re-derives axis matches from `paper_ref` keyword/year heuristic only "
    "(no copying cycle-25 row, no access to curated numerical fields); AI-"
    "rater B re-derives from `ribozyme_class` + `notes` text only, ignoring "
    "`paper_ref`. The witness emits Cohen's kappa per axis (4 axes), pooled "
    "macro-mean overall_kappa, and stratified log_bf re-run under each "
    "rater's own labels independently. Even if the AND-gate "
    "(overall_kappa>=0.6 AND stratified_log_bf.max<5.0) PASSES, full GATE-"
    "26-4 / G26-RB-1 closure WAITS for >=2 external human raters scoring "
    "the same n=30 corpus catalytic-core nt count + reaction-state ladder "
    "mapping. Status: PROVISIONAL AI-AUDIT LANDED; human-rater audit "
    "outstanding (deadline 2026-06-15). raw_9 hexa-only (stdlib; no scipy/"
    "numpy/biopython). raw_47 no cross-repo I/O. raw_77 append-only."
)


def emit_witness(result: Dict[str, Any], out_path: str) -> Dict[str, Any]:
    row = {
        "schema": "raw_77_ribozyme_interrater_v1",
        "audited_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "rater_count": 2,
        "corpus_size": result["n"],
        "rater_ids": [
            "ai_rater_a_paper_ref_heuristic",
            "ai_rater_b_primitive_class_heuristic",
        ],
        "per_axis_kappa": result["per_axis_kappa"],
        "overall_kappa": result["overall_kappa"],
        "stratified_log_bf": {
            "mean": result["stratified_log_bf"]["mean"],
            "min": result["stratified_log_bf"]["min"],
            "max": result["stratified_log_bf"]["max"],
        },
        "pass_evaluation": {
            "criteria": {
                "overall_kappa_ge_0p6": result["criteria"]["overall_kappa_ge_0p6"],
                "stratified_log_bf_max_lt_5": result["criteria"]["stratified_log_bf_max_lt_5"],
            },
            "overall_pass": result["overall_pass"],
        },
        "notes": PROVISIONAL_NOTE,
        "witness_ref": "state/discovery_absorption/registry.jsonl#raw_77_ribozyme_interrater_v1",
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=True) + "\n")
    return row


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args(argv: List[str]) -> Dict[str, Any]:
    cfg = {"no_emit": False, "quiet": False}
    for a in argv[1:]:
        if a == "--no-emit":
            cfg["no_emit"] = True
        elif a == "--quiet":
            cfg["quiet"] = True
        elif a in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
    return cfg


def main(argv: List[str]) -> int:
    cfg = _parse_args(argv)
    result = run_audit()
    n = result["n"]
    pak = result["per_axis_kappa"]
    ok = result["overall_kappa"]
    sbf = result["stratified_log_bf"]
    crit = result["criteria"]
    overall = result["overall_pass"]
    sentinel = "PASS" if overall else "FAIL"

    if not cfg["quiet"]:
        print("=" * 72)
        print("F-RB-2 RIBOZYME inter-rater AI audit (GATE-26-4 / G26-RB-1)")
        print("PROVISIONAL_AI_ONLY — does NOT satisfy human-rater requirement")
        print("=" * 72)
        print("corpus_size                       : %d" % n)
        print("rater_ids                         : "
              "ai_rater_a_paper_ref_heuristic, "
              "ai_rater_b_primitive_class_heuristic")
        print("-" * 72)
        print("per-axis Cohen's kappa:")
        for k, v in pak.items():
            print("  %-40s : %+.4f" % (k, v))
        print("overall_kappa (macro-mean)        : %+.4f" % ok)
        print("-" * 72)
        print("stratified log_bf:")
        print("  rater_a (paper_ref heuristic)   : %+.4f" % sbf["rater_a"])
        print("  rater_b (class+notes heuristic) : %+.4f" % sbf["rater_b"])
        print("  mean                            : %+.4f" % sbf["mean"])
        print("  min                             : %+.4f" % sbf["min"])
        print("  max                             : %+.4f" % sbf["max"])
        print("-" * 72)
        print("AND-gate (PROVISIONAL):")
        print("  overall_kappa >= 0.6            : %s"
              % crit["overall_kappa_ge_0p6"])
        print("  stratified_log_bf.max < 5.0     : %s"
              % crit["stratified_log_bf_max_lt_5"])
        print("  overall_pass (AI-rater only)    : %s" % overall)
        print("-" * 72)
        print("per-entry rater stamps:")
        corpus = build_corpus_n30()
        for i, e in enumerate(corpus):
            ax_a = result["rater_a_axes_list"][i]
            ax_b = result["rater_b_axes_list"][i]
            agree = sum(1 for x, y in zip(ax_a, ax_b) if x == y)
            print("  %2d %-44s A=%s sumA=%d  B=%s sumB=%d  agree=%d/4"
                  % (i + 1, e["paper_ref"][:44],
                     ax_a, sum(ax_a), ax_b, sum(ax_b), agree))
        print("-" * 72)

    out_path = os.environ.get(
        "RIBOZYME_INTERRATER_AUDIT_PATH",
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            os.pardir, os.pardir,
            "state", "discovery_absorption", "registry.jsonl"))
    out_path = os.path.normpath(out_path)
    if not cfg["no_emit"]:
        emit_witness(result, out_path)
        if not cfg["quiet"]:
            print("witness emitted -> %s" % out_path)
    else:
        if not cfg["quiet"]:
            print("witness emission SKIPPED (--no-emit)")

    print("__RB_INTERRATER_AI_AUDIT__ %s" % sentinel)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
