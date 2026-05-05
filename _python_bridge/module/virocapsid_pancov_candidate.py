#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
virocapsid_pancov_candidate.py — C2 cell V·γ (VIROCAPSID × γ=pancov).

Cycle 25 deliverable. IN-SILICO numerical primitive verification ONLY.
NOT a clinical, regulatory, or wet-lab claim.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import virocapsid_calibration as vc  # noqa: E402


CANDIDATE = {
    "target_disease_class_label": "gamma_pancov",
    "matrix_cell_label": "V_gamma",
    "marker_referenced": "conserved coronavirus envelope-protein RBD region (multivalent display context)",
    "cage_class": "T=1 60-subunit icosahedral polyhedron",
    "t_number": 1,
    "n_cp_per_cage": 60,
    "n_pent_per_cage": 12,
    "annotation_slots": [
        {
            "slot_type": "surface-loop multivalent display annotation",
            "annotation_seq_lit_ref": (
                "conserved RBD-region short peptide stub "
                "(public open-access structural biology / coronavirus alignment literature)"
            ),
            "modeled_by_simulator": False,
            "multivalent_display_count_metadata": 60,
        }
    ],
    "n6_invariant_role": (
        "σ(6)=12 pentamer vertex count; τ(6)=4 assembly states; "
        "φ(6)=2 closed vs open shell; J₂=24."
    ),
    "source_literature_anchors": [
        "conserved coronavirus envelope-protein RBD region — public open-access literature",
        "T=1 60-subunit cage — Caspar-Klug 1962 + Zlotnick 2003",
    ],
    "downstream_layer_handoff": [
        "formulation / route / dose / adjuvant → out-of-scope at primitive",
        "immunological / regulatory / clinical → out-of-repo (C3+)",
        "peptide-MHC / B-cell / T-cell biology → out-of-scope (sequence-level only)",
    ],
}


def verify_with_virocapsid_calibration(seed=42):
    return vc.calibrate_one(ref_system="stnv", mode="verify",
                            seed=seed, verbose=False)


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption", "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    overall_pass = bool(verify_result["pass"])

    row = {
        "schema": "raw_77_c2_virocapsid_pancov_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-v-gamma-pancov-cage-annotation-candidate",
        "domain": "hexa-virocapsid",
        "matrix_cell": "V_gamma",
        "disease_class_label": "gamma_pancov",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "virocapsid_calibration.py (F-VIROCAPSID-3 PASS, cycle 24 C0b)",
            "calibration_pass": overall_pass,
            "reference_system": "stnv",
            "t_number": 1,
            "n_cp_per_cage": 60,
            "calibrated_params": verify_result.get("params"),
            "verify_yield_at_t10000": verify_result.get("verify_yield_at_t10000"),
            "verify_mass_drift_rel": verify_result.get("verify_mass_drift_rel"),
            "verify_finite_ok": verify_result.get("verify_finite_ok"),
            "target_yield": verify_result.get("target_yield"),
            "primary_integrator": "backward_euler",
        },
        "n6_invariant": {
            "sigma_6": vc.cas.SIGMA_6, "tau_6": vc.cas.TAU_6,
            "phi_6": vc.cas.PHI_6, "J2": vc.cas.J2,
            "master_identity_ok": (vc.cas.SIGMA_6 * vc.cas.PHI_6 == vc.cas.J2
                                   and 6 * vc.cas.TAU_6 == vc.cas.J2),
        },
        "in_silico_grade_disclose": "IN-SILICO numerical-primitive verification ONLY.",
        "raw_91_c3_disclose": [
            "16-cell matrix label gamma_pancov is per .roadmap.hexa_bio §0; "
            "NOT a clinical or treatment proposal.",
            "Conserved RBD-region peptide reference is from PUBLIC OPEN-ACCESS "
            "literature only.",
            "PASS verifies cage primitive's assembly-kinetics stability — "
            "does NOT verify any biological property of annotated peptide.",
            "Annotation slot is sequence-level metadata; simulator does NOT "
            "model peptide-MHC interaction, immune presentation, or any biological process.",
            "Multivalent display count (60) is structural metadata only — "
            "no immunogenicity / efficacy claim.",
            "16-cell matrix V·γ at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": "Imports virocapsid_calibration (R2 preserved).",
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": "__V_GAMMA_PANCOV_C2__ " + ("PASS" if overall_pass else "FAIL"),
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(description="HEXA-BIO C2 cell V·γ (VIROCAPSID × γ=pancov)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print(f"[virocapsid_pancov_candidate] C2 cell V·γ")

    verify_result = verify_with_virocapsid_calibration(seed=args.seed)
    overall_pass = bool(verify_result["pass"])

    if not args.quiet:
        print(f"  yield = {verify_result.get('verify_yield_at_t10000'):.4f}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)

    print("__V_GAMMA_PANCOV_C2__ " + ("PASS" if overall_pass else "FAIL"))
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
