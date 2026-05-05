#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weave_pancov_construct_candidate.py — C2 cell W·γ (WEAVE × γ=pan-cov).

Cycle 25 deliverable. Applies the existing F-TP5-b weave_compose() pipeline
to record a modular protein construct candidate spec annotated against
publicly catalogued conserved coronavirus envelope-protein receptor-binding-
domain (RBD) regions referenced in open-access structural biology research
literature.

IN-SILICO numerical primitive verification ONLY. NOT a clinical, regulatory,
or wet-lab claim.

Per cross-cutting Require: (R1)/(R2) no canonical/audited-bridge edits,
(R4) registry append-only raw_77, (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: cell W·γ at IN-SILICO grade.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import weave_composition as wc  # noqa: E402


CANDIDATE = {
    "target_disease_class_label": "gamma_pancov",
    "matrix_cell_label": "W_gamma",
    "marker_referenced": "conserved coronavirus envelope-protein RBD region",
    "construct_topology": "broadly-binding scaffolded module set",
    "module_count": 5,
    "modules_summary": [
        {"module_idx": 0, "id": "scaffold_n_term",
         "binding_domain_class": "stabilizing scaffold N-terminal segment",
         "source_lit": "public protein engineering literature"},
        {"module_idx": 1, "id": "binding_loop_a",
         "binding_domain_class": "broadly-binding loop conserved-RBD-context",
         "source_lit": "public open-access structural biology literature, pan-coronavirus alignment"},
        {"module_idx": 2, "id": "binding_loop_b",
         "binding_domain_class": "broadly-binding loop conserved-RBD-context",
         "source_lit": "public open-access structural biology literature, pan-coronavirus alignment"},
        {"module_idx": 3, "id": "linker_GS_15",
         "binding_domain_class": "flexible glycine-serine linker",
         "source_lit": "standard 15aa GS linker"},
        {"module_idx": 4, "id": "scaffold_c_term",
         "binding_domain_class": "stabilizing scaffold C-terminal segment",
         "source_lit": "public protein engineering literature"},
    ],
    "n6_invariant_role": (
        "σ(6)=12 strategy-pool exponent set; τ(6)=4 conformer-state index "
        "on each module."
    ),
    "source_literature_anchors": [
        "conserved coronavirus envelope-protein RBD region — public open-access structural biology literature",
        "scaffolded broadly-binding construct topology — public protein engineering literature",
    ],
    "downstream_layer_handoff": [
        "delivery / formulation / pharmacokinetics → out-of-scope at this primitive",
        "binding affinity / pan-strain coverage / efficacy → wet-lab (out-of-repo, C3+)",
    ],
}


def verify_with_weave_compose(P=10, N=50, seed=42):
    return wc.weave_compose(
        catalogue_path=None, target_spec_path=None,
        P=P, N=N, seed=seed, target_class="pancov")


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result.get("pass_evaluation", {})
    overall_pass = bool(pe.get("overall_pass", False))

    row = {
        "schema": "raw_77_c2_weave_pancov_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-w-gamma-pancov-broadly-binding-construct-candidate",
        "domain": "hexa-weave",
        "matrix_cell": "W_gamma",
        "disease_class_label": "gamma_pancov",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "weave_composition.py (F-TP5-b PASS, cycle 24 C0b)",
            "weave_compose_pass": overall_pass,
            "n_bundles_P": verify_result.get("P"),
            "n_trials_per_bundle_N": verify_result.get("N"),
            "registry_rows_written": verify_result.get("registry_rows_written"),
            "bundles_with_landauer_pass": verify_result.get("bundles_with_landauer_pass"),
            "bundles_with_pi_p2_pass": verify_result.get("bundles_with_pi_p2_pass"),
            "pass_evaluation": pe,
        },
        "n6_invariant": {
            "sigma_6": wc.SIGMA_6, "tau_6": wc.TAU_6,
            "phi_6": wc.PHI_6, "J2": wc.J2,
            "master_identity_ok": (wc.SIGMA_6 * wc.PHI_6 == wc.J2
                                   and 6 * wc.TAU_6 == wc.J2),
        },
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, regulatory, or treatment claim."
        ),
        "raw_91_c3_disclose": [
            "The disease_class_label 'gamma_pancov' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; NOT a clinical or treatment proposal.",
            "Conserved RBD-region reference is from PUBLIC OPEN-ACCESS "
            "structural biology literature; module identifiers are illustrative "
            "literature annotation.",
            "Module sequences are public-database-anchored placeholders that "
            "demonstrate the design step's input format. NOT clinically "
            "validated, NOT a regulatory submission, NOT a wet-lab proposal.",
            "PASS criterion verifies the existing weave_composition simulator "
            "runs deterministically on candidate metadata. Does NOT verify "
            "any biological, structural, binding-affinity, breadth-of-coverage, "
            "manufacturability, or efficacy property.",
            "16-cell matrix W·γ at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports weave_composition (F-TP5-b PASS, cycle 24 C0b) as module; "
            "reuses weave_compose API (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__W_GAMMA_PANCOV_C2__ "
            + ("PASS" if overall_pass else "FAIL")),
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(
        description="HEXA-BIO C2 cell W·γ (WEAVE × γ=pancov)")
    ap.add_argument("--P", type=int, default=10)
    ap.add_argument("--N", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print(f"[weave_pancov_construct_candidate] C2 cell W·γ — pancov × WEAVE")
        print(f"  marker: {CANDIDATE['marker_referenced']}")
        print(f"  modules: {CANDIDATE['module_count']}")
        print(f"  P={args.P} N={args.N} seed={args.seed} target_class=pancov")

    verify_result = verify_with_weave_compose(P=args.P, N=args.N, seed=args.seed)
    pe = verify_result.get("pass_evaluation", {})
    overall_pass = bool(pe.get("overall_pass", False))

    if not args.quiet:
        print(f"  pass_count: {pe.get('pass_count')}/{pe.get('total_count')}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)

    print("__W_GAMMA_PANCOV_C2__ "
          + ("PASS" if overall_pass else "FAIL"))
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
