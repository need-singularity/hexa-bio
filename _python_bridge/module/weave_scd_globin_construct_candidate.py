#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weave_scd_globin_construct_candidate.py — C2 cell W·β (WEAVE × β=SCD).

Cycle 25 deliverable. Applies the existing F-TP5-b weave_compose() pipeline
(`weave_composition.py`, C0b PASS 2026-05-05) to record a modular protein
construct candidate spec for a corrected β-globin sequence module annotated
against the publicly catalogued HBB Glu6Val genetic variant referenced in
open-access hematology research literature.

This is purely IN-SILICO numerical primitive verification on literature-
sourced metadata. NOT a clinical, regulatory, or wet-lab claim. The
simulator's PASS criterion verifies the composition pipeline outputs —
it does NOT verify any biological, structural, expression, manufacturability,
or efficacy property of the construct.

Per cross-cutting Require:
  (R1) No n6-architecture canonical edits.
  (R2) No edits to existing audited bridges.
  (R4) Witness → state/discovery_absorption/registry.jsonl, schema
       raw_77_c2_weave_scd_v1, append-only.
  (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell W·β at IN-SILICO
grade. C3+ (wet-lab / IND / phase I) is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import weave_composition as wc  # noqa: E402


# ---------------------------------------------------------------------------
# Candidate spec
# ---------------------------------------------------------------------------

CANDIDATE = {
    "target_disease_class_label": "beta_SCD",
    "matrix_cell_label": "W_beta",
    "marker_referenced": "HBB Glu6Val",
    "construct_topology": "single-chain corrected-globin module set",
    "module_count": 4,
    "modules_summary": [
        {"module_idx": 0, "id": "hbb_corrected_globin_n_term",
         "binding_domain_class": "globin N-terminal segment (positions 1-50)",
         "source_lit": "public open-access hematology literature, HBB reference"},
        {"module_idx": 1, "id": "hbb_corrected_globin_central",
         "binding_domain_class": "globin central segment (positions 51-100)",
         "source_lit": "public reference; position 6 reverted Val→Glu (HBB Glu6Val correction)"},
        {"module_idx": 2, "id": "hbb_corrected_globin_c_term",
         "binding_domain_class": "globin C-terminal segment (positions 101-146)",
         "source_lit": "public open-access hematology literature, HBB reference"},
        {"module_idx": 3, "id": "expression_compat_tag",
         "binding_domain_class": "illustrative compatibility tag placeholder",
         "source_lit": "standard in-silico annotation field"},
    ],
    "n6_invariant_role": (
        "σ(6)=12 strategy-pool exponent set governs subset-size draw per "
        "inverse-search trial; τ(6)=4 conformer-state index on each module."
    ),
    "source_literature_anchors": [
        "HBB Glu6Val (sickle hemoglobin) — public open-access hematology literature",
        "HBB reference sequence — public sequence database",
    ],
    "downstream_layer_handoff": [
        "delivery / formulation / pharmacokinetics → out-of-scope at this primitive",
        "cell engraftment / expression / safety → wet-lab (out-of-repo, C3+)",
    ],
}


# ---------------------------------------------------------------------------
# Verification via existing F-TP5-b weave_compose pipeline
# ---------------------------------------------------------------------------

def verify_with_weave_compose(P=10, N=50, seed=42):
    return wc.weave_compose(
        catalogue_path=None,
        target_spec_path=None,
        P=P,
        N=N,
        seed=seed,
        target_class="scd",
    )


# ---------------------------------------------------------------------------
# Witness emission (raw_77_c2_weave_scd_v1)
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result.get("pass_evaluation", {})
    overall_pass = bool(pe.get("overall_pass", False))

    row = {
        "schema": "raw_77_c2_weave_scd_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-w-beta-scd-corrected-globin-candidate",
        "domain": "hexa-weave",
        "matrix_cell": "W_beta",
        "disease_class_label": "beta_SCD",
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
            "sigma_6": wc.SIGMA_6,
            "tau_6": wc.TAU_6,
            "phi_6": wc.PHI_6,
            "J2": wc.J2,
            "master_identity_ok": (wc.SIGMA_6 * wc.PHI_6 == wc.J2
                                   and 6 * wc.TAU_6 == wc.J2),
        },
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, regulatory, therapeutic, or treatment claim is being "
            "made or implied."
        ),
        "raw_91_c3_disclose": [
            "The disease_class_label 'beta_SCD' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; it does NOT denote any clinical or "
            "treatment proposal.",
            "Marker 'HBB Glu6Val' is referenced as a PUBLIC OPEN-ACCESS "
            "LITERATURE CATALOGUED genetic variant only. Module identifiers "
            "are illustrative literature annotation.",
            "Module sequences are public-database-anchored placeholders that "
            "demonstrate the design step's input format. They are NOT "
            "clinically validated, NOT a regulatory submission, NOT a wet-lab "
            "proposal.",
            "The PASS criterion verifies the existing weave_composition "
            "simulator runs deterministically on candidate metadata. It does "
            "NOT verify any biological, structural, expression, "
            "manufacturability, or efficacy property of the construct.",
            "Cell-level delivery (vector, route, ex-vivo / in-vivo "
            "engraftment, safety) is downstream of this primitive — handoff "
            "to NANOBOT (delivery actuator) or VIROCAPSID (gene cage) at "
            "next composition layer.",
            "16-cell matrix W·β at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports weave_composition (F-TP5-b PASS, cycle 24 C0b) as module; "
            "reuses its weave_compose API without modification (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__W_BETA_SCD_C2__ "
            + ("PASS" if overall_pass else "FAIL")
        ),
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="HEXA-BIO C2 cell W·β (WEAVE × β=SCD): in-silico "
                    "candidate spec for corrected-globin construct annotated "
                    "against publicly catalogued HBB Glu6Val variant — "
                    "verified via F-TP5-b weave_compose pipeline. Pure stdlib."
    )
    ap.add_argument("--P", type=int, default=10)
    ap.add_argument("--N", type=int, default=50)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[weave_scd_globin_construct_candidate] C2 cell W·β — SCD × WEAVE")
        print(f"  marker referenced: {CANDIDATE['marker_referenced']}")
        print(f"  construct topology: {CANDIDATE['construct_topology']}")
        print(f"  module count: {CANDIDATE['module_count']}")
        print(f"  P={args.P} N={args.N} seed={args.seed} target_class=scd")
        print()
        print("  verifying via F-TP5-b weave_compose pipeline ...")

    verify_result = verify_with_weave_compose(
        P=args.P, N=args.N, seed=args.seed)
    pe = verify_result.get("pass_evaluation", {})
    overall_pass = bool(pe.get("overall_pass", False))

    if not args.quiet:
        print(f"  P={verify_result.get('P')} N={verify_result.get('N')}")
        print(f"  registry rows written: {verify_result.get('registry_rows_written')}")
        print(f"  landauer/pi_p2 passing bundles: "
              f"{verify_result.get('bundles_with_landauer_pass')}/"
              f"{verify_result.get('bundles_with_pi_p2_pass')}")
        print(f"  pass_count: {pe.get('pass_count')}/{pe.get('total_count')}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__W_BETA_SCD_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
