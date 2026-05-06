#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weave_pi_p2_verifier_v3_exhaustive.py — GATE-26-3 NP-solver path closure.

Closes GATE-26-3 (`weave-pi-p2-np-solver`) PASS criterion per umbrella
.roadmap.hexa_bio C0f: "on canonical n=50 sweep, exact-vs-greedy
agreement on ≥48/50 instances OR documented ≤2 honest disagreements
with worked examples".

The v2 verifier (`weave_pi_p2_verifier_v2.py`) implements a GREEDY
HEURISTIC: forall top-k off-targets, exists refold-avoidance. v3 here
implements the EXHAUSTIVE NP-solver path: forall ALL off-targets in
catalogue \\ bundle, exists refold-avoidance. For the canonical
12-strand catalogue this is polynomial (|pool| ≤ 12 - bundle_size),
but the critical distinction is that v3 returns the EXACT Π^p_2
verdict, where v2 may have false-positives or false-negatives if the
top-k pool misses the actual weakest off-target.

This script then runs both v2 and v3 over an n=50 deterministic bundle
sweep (seeded enumeration over the 12-strand catalogue) and reports
exact-vs-greedy agreement.

Per cross-cutting Require (R5) raw 9 hexa-only: **Python stdlib only.**

PASS criterion (GATE-26-3):
  agree_count >= 48 / 50  OR
  disagreement_count <= 2 with documented worked examples.

Usage:

    python3 weave_pi_p2_verifier_v3_exhaustive.py --emit
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import weave_composition as wc  # noqa: E402
import weave_pi_p2_verifier_v2 as v2  # noqa: E402

REGISTRY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "state",
    "discovery_absorption",
    "registry.jsonl",
)


def pi_p2_verifier_v3_exhaustive(bundle: list, all_strands: list,
                                  edit_threshold: int = v2.DEFAULT_EDIT_THRESHOLD) -> dict:
    """Exact Π^p_2 verifier: forall ALL off-targets (catalogue\\bundle),
    exists refold-avoidance (edit_distance ≥ edit_threshold).

    For the 12-strand catalogue this is polynomial (|pool| ≤ 12). The
    distinction from v2 (greedy top-k) is that v3 cannot miss the
    weakest off-target, so the verdict is exact for the candidate pool.
    """
    bundle_ids = {s.get("id", "") for s in bundle}
    candidate_pool = [s for s in all_strands if s.get("id", "") not in bundle_ids]

    per_strand = []
    n_strand_pass = 0
    n_evals = 0
    weakest_link = None

    for target in bundle:
        n_avoided = 0
        min_d = None
        weakest_o = None
        for off in candidate_pool:
            n_evals += 1
            d = v2.edit_distance(target.get("sequence", ""),
                                  off.get("sequence", ""),
                                  cap=64)
            if min_d is None or d < min_d:
                min_d = d
                weakest_o = off.get("id", "")
            if d >= edit_threshold:
                n_avoided += 1
        strand_pass = (min_d is None) or (min_d >= edit_threshold)
        if strand_pass:
            n_strand_pass += 1
        per_strand.append({
            "target_id": target.get("id", ""),
            "n_offtargets_checked": len(candidate_pool),
            "n_offtargets_avoided": n_avoided,
            "min_edit_distance_observed": min_d,
            "pass": strand_pass,
            "weakest_offtarget_id": weakest_o if not strand_pass else None,
            "weakest_edit_distance": min_d if not strand_pass else None,
        })
        if not strand_pass and (weakest_link is None or
                                 (min_d is not None and min_d < weakest_link.get("edit_distance", 999))):
            weakest_link = {
                "target_id": target.get("id", ""),
                "offtarget_id": weakest_o,
                "edit_distance": min_d,
            }

    overall_pass = n_strand_pass == len(bundle)
    return {
        "pass": overall_pass,
        "verifier_version": "v3_exhaustive_np_solver",
        "edit_threshold": edit_threshold,
        "per_strand_results": per_strand,
        "weakest_link_details": weakest_link,
        "n_strand_pass": n_strand_pass,
        "n_strand_total": len(bundle),
        "n_offtarget_evaluations": n_evals,
    }


def enumerate_n50_bundles(catalogue: list, bundle_size: int = 5, n: int = 50) -> list:
    """Deterministic n=50 bundle enumeration. Combinations of `bundle_size`
    drawn from the 12-strand catalogue; take first 50 in lexicographic order."""
    bundles = []
    indices = list(range(len(catalogue)))
    for i, combo in enumerate(combinations(indices, bundle_size)):
        if i >= n:
            break
        bundles.append({"name": f"bundle_{i:02d}", "strands": [catalogue[j] for j in combo]})
    return bundles


def main(argv):
    p = argparse.ArgumentParser(description="GATE-26-3 NP-solver exhaustive path")
    p.add_argument("--n-bundles", type=int, default=50)
    p.add_argument("--bundle-size", type=int, default=5)
    p.add_argument("--k-offtargets", type=int, default=v2.DEFAULT_K_OFFTARGETS)
    p.add_argument("--edit-threshold", type=int, default=v2.DEFAULT_EDIT_THRESHOLD)
    p.add_argument("--emit", action="store_true")
    p.add_argument("--summary", action="store_true")
    args = p.parse_args(argv)

    catalogue = wc.load_catalogue(None)
    bundles = enumerate_n50_bundles(catalogue, bundle_size=args.bundle_size,
                                      n=args.n_bundles)

    per_bundle = []
    agree_count = 0
    disagree_count = 0
    disagreements = []
    for b in bundles:
        v2_res = v2.pi_p2_verifier_v2(b["strands"], catalogue,
                                       k_offtargets=args.k_offtargets,
                                       edit_threshold=args.edit_threshold)
        v3_res = pi_p2_verifier_v3_exhaustive(b["strands"], catalogue,
                                                edit_threshold=args.edit_threshold)
        agree = v2_res["pass"] == v3_res["pass"]
        if agree:
            agree_count += 1
        else:
            disagree_count += 1
            disagreements.append({
                "bundle_name": b["name"],
                "v2_pass": v2_res["pass"],
                "v3_pass": v3_res["pass"],
                "v2_n_offtarget_evals": v2_res.get("n_offtarget_evaluations"),
                "v3_n_offtarget_evals": v3_res.get("n_offtarget_evaluations"),
                "v2_weakest_link": v2_res.get("weakest_link_details"),
                "v3_weakest_link": v3_res.get("weakest_link_details"),
                "interpretation": "v2 missed weakest off-target via top-k pruning"
                                  if (v3_res["pass"] is False and v2_res["pass"] is True)
                                  else "v2 over-rejected via degenerate top-k"
                                  if (v3_res["pass"] is True and v2_res["pass"] is False)
                                  else "tie",
            })
        per_bundle.append({
            "bundle_name": b["name"],
            "v2_pass": v2_res["pass"],
            "v3_pass": v3_res["pass"],
            "agree": agree,
        })

    n_total = len(bundles)
    overall_pass = agree_count >= 48 or disagree_count <= 2
    audited_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    witness = {
        "schema": "raw_77_weave_pi_p2_v3_exhaustive_v1",
        "audited_at": audited_at,
        "audit_kind": "gate_26_3_np_solver_exact_vs_greedy",
        "n_bundles": n_total,
        "bundle_size": args.bundle_size,
        "k_offtargets_v2": args.k_offtargets,
        "edit_threshold": args.edit_threshold,
        "agree_count": agree_count,
        "disagree_count": disagree_count,
        "disagreements": disagreements,
        "per_bundle": per_bundle,
        "gate_26_3_evaluation": {
            "verdict": "PASS" if overall_pass else "FAIL",
            "criterion": "agree_count >= 48 OR disagree_count <= 2",
            "agree_count": agree_count,
            "disagree_count": disagree_count,
        },
        "raw_91_c3_disclose": (
            "v3 exhaustive verifier checks ALL off-targets in "
            "catalogue\\bundle (not greedy top-k like v2). For the "
            "12-strand catalogue this is polynomial. v2-vs-v3 agreement "
            "on n=50 deterministic bundles measures whether v2's top-k "
            "heuristic matches the exact NP-solver verdict on this "
            "small-scale problem. PASS criterion is GATE-26-3 from "
            ".roadmap.hexa_bio C0f."
        ),
        "raw_77_append_only": True,
        "witness_ref": "state/discovery_absorption/registry.jsonl#raw_77_weave_pi_p2_v3_exhaustive_v1",
    }

    if args.emit:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(witness, ensure_ascii=False, sort_keys=True) + "\n")
        sys.stderr.write(f"emitted 1 witness row -> {REGISTRY_PATH}\n")

    if args.summary:
        print(json.dumps(witness, sort_keys=True, indent=2))
    else:
        sys.stderr.write(
            f"n_bundles={n_total} agree={agree_count} disagree={disagree_count}  "
            f"verdict={witness['gate_26_3_evaluation']['verdict']}\n"
        )
        for d in disagreements[:5]:
            sys.stderr.write(f"  disagree {d['bundle_name']}: v2={d['v2_pass']} v3={d['v3_pass']} ({d['interpretation']})\n")

    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
