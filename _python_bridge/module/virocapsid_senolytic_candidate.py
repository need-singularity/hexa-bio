#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
virocapsid_senolytic_candidate.py — C2 cell V·δ (VIROCAPSID × δ=senolytic).
IN-SILICO numerical primitive verification ONLY.
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
    "target_disease_class_label": "delta_senolytic",
    "matrix_cell_label": "V_delta",
    "marker_referenced": "senescence-associated marker + p16 context (public catalogued)",
    "cage_class": "T=1 60-subunit icosahedral polyhedron",
    "t_number": 1,
    "n_cp_per_cage": 60,
    "n_pent_per_cage": 12,
    "annotation_slots": [
        {
            "slot_type": "surface-loop tropism annotation",
            "annotation_seq_lit_ref": "anti-senescence-marker stub (public AB DB catalogued)",
            "modeled_by_simulator": False,
        },
        {
            "slot_type": "internal-cargo metadata",
            "annotation_seq_lit_ref": "senolytic payload placeholder (sequence-level only)",
            "modeled_by_simulator": False,
        },
    ],
    "n6_invariant_role": "σ(6)=12 vertex; τ(6)=4 assembly states; φ(6)=2; J₂=24.",
    "source_literature_anchors": [
        "p16-INK4a (CDKN2A) — public open-access aging research literature",
        "T=1 60-subunit cage — Caspar-Klug 1962 + Zlotnick 2003",
    ],
    "downstream_layer_handoff": [
        "tropism / formulation / route → out-of-scope",
        "regulatory / clinical → out-of-repo (C3+)",
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
        "schema": "raw_77_c2_virocapsid_senolytic_v1",
        "ts": ts, "cycle": 25,
        "phase": "c2-v-delta-senolytic-cage-annotation-candidate",
        "domain": "hexa-virocapsid", "matrix_cell": "V_delta",
        "disease_class_label": "delta_senolytic",
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
            "delta_senolytic is a 16-cell matrix label, NOT a clinical proposal.",
            "p16-INK4a / senescence markers are PUBLIC OPEN-ACCESS aging research literature catalogued.",
            "Annotation slots are sequence-level metadata; simulator does NOT model biology.",
            "PASS verifies cage assembly-kinetics stability — NOT biological property.",
            "16-cell matrix V·δ at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": "Imports virocapsid_calibration (R2 preserved).",
        "raw_9_hexa_only": "python stdlib only",
        "raw_138_sentinel": "__V_DELTA_SENOLYTIC_C2__ " + ("PASS" if overall_pass else "FAIL"),
        "raw_77_append_only": True,
    }
    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(description="HEXA-BIO C2 cell V·δ")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    verify_result = verify_with_virocapsid_calibration(seed=args.seed)
    overall_pass = bool(verify_result["pass"])

    if not args.no_emit:
        emit_c2_witness(verify_result)

    print("__V_DELTA_SENOLYTIC_C2__ " + ("PASS" if overall_pass else "FAIL"))
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
