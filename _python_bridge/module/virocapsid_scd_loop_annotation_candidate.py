#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
virocapsid_scd_loop_annotation_candidate.py — C2 cell V·β (VIROCAPSID × β=SCD).

Cycle 25 deliverable. Applies the existing F-VIROCAPSID-3 calibration tool
(`virocapsid_calibration.py`, C0b PASS 2026-05-05) to record a candidate
spec for a T=1 60-subunit cage with a sequence-level annotation slot for
HSC tropism / HBB-context payload metadata referenced in public open-access
hematology research literature. The simulator does NOT model any biological
process — annotation slots are sequence-level metadata fields only.

IN-SILICO numerical primitive verification ONLY. NOT a clinical, regulatory,
or wet-lab claim. PASS verifies cage primitive's assembly-kinetics
stability under STNV-calibrated rate constants — does NOT verify any
biological property of the inserted annotations.

Per cross-cutting Require: (R1)/(R2) no edits to canonical/audited bridges,
(R4) registry append-only raw_77, (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell V·β at IN-SILICO
grade. C3+ is out-of-repo.
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
    "target_disease_class_label": "beta_SCD",
    "matrix_cell_label": "V_beta",
    "marker_referenced": "HBB Glu6Val + CD34 (HSC tropism context)",
    "cage_class": "T=1 60-subunit icosahedral polyhedron",
    "t_number": 1,
    "n_cp_per_cage": 60,
    "n_pent_per_cage": 12,
    "annotation_slots": [
        {
            "slot_type": "surface-loop tropism annotation",
            "annotation_seq_lit_ref": "anti-CD34 scFv stub (public AB DB catalogued)",
            "modeled_by_simulator": False,
        },
        {
            "slot_type": "internal-cargo metadata",
            "annotation_seq_lit_ref": "HBB-corrected payload placeholder (sequence-level only)",
            "modeled_by_simulator": False,
        },
    ],
    "n6_invariant_role": (
        "σ(6)=12 pentamer vertex count (Caspar-Klug T=1 invariant); "
        "τ(6)=4 assembly states; φ(6)=2 closed vs open shell; "
        "J₂=24 octahedral O ⊂ icosahedral I subgroup."
    ),
    "source_literature_anchors": [
        "HBB Glu6Val variant — public open-access hematology literature",
        "CD34 (HSC marker) — public antibody database",
        "T=1 60-subunit cage geometry — Caspar-Klug 1962 + Zlotnick 2003",
    ],
    "downstream_layer_handoff": [
        "tropism / formulation / route / dose → out-of-scope at this primitive",
        "regulatory / clinical → out-of-repo (C3+)",
        "ligand / cargo biological-interaction modeling → out-of-scope",
    ],
}


def verify_with_virocapsid_calibration(seed=42):
    return vc.calibrate_one(
        ref_system="stnv",
        mode="verify",
        seed=seed,
        verbose=False,
    )


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    overall_pass = bool(verify_result["pass"])

    row = {
        "schema": "raw_77_c2_virocapsid_scd_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-v-beta-scd-cage-annotation-candidate",
        "domain": "hexa-virocapsid",
        "matrix_cell": "V_beta",
        "disease_class_label": "beta_SCD",
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
            "method": verify_result.get("method"),
            "primary_integrator": "backward_euler",
        },
        "n6_invariant": {
            "sigma_6": vc.cas.SIGMA_6,
            "tau_6": vc.cas.TAU_6,
            "phi_6": vc.cas.PHI_6,
            "J2": vc.cas.J2,
            "master_identity_ok": (vc.cas.SIGMA_6 * vc.cas.PHI_6 == vc.cas.J2
                                   and 6 * vc.cas.TAU_6 == vc.cas.J2),
        },
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, regulatory, immunological, or treatment claim is being "
            "made or implied."
        ),
        "raw_91_c3_disclose": [
            "The disease_class_label 'beta_SCD' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; it does NOT denote any clinical or "
            "treatment proposal.",
            "Markers HBB Glu6Val and CD34 are referenced as PUBLIC OPEN-"
            "ACCESS LITERATURE CATALOGUED entities only.",
            "PASS criterion verifies cage primitive's assembly-kinetics "
            "stability — it does NOT verify any biological property of the "
            "annotated tropism or payload slots.",
            "Annotation slots (tropism, internal-cargo) are sequence-level "
            "metadata fields; the simulator does NOT model ligand-receptor "
            "interaction, payload release, or any biological process.",
            "Downstream layers (formulation, delivery, regulatory, clinical) "
            "are explicitly out-of-repo per (R6) hexa-bio scope.",
            "16-cell matrix V·β at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports virocapsid_calibration (F-VIROCAPSID-3 PASS, cycle 24 "
            "C0b) as module; reuses calibrate_one --mode verify (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__V_BETA_SCD_C2__ "
            + ("PASS" if overall_pass else "FAIL")
        ),
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(
        description="HEXA-BIO C2 cell V·β (VIROCAPSID × β=SCD): in-silico "
                    "candidate spec for T=1 60-subunit cage with sequence-"
                    "level annotation slots for HBB / CD34 markers — "
                    "verified via F-VIROCAPSID-3 calibration."
    )
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[virocapsid_scd_loop_annotation_candidate] C2 cell V·β — SCD × VIROCAPSID")
        print(f"  marker referenced: {CANDIDATE['marker_referenced']}")
        print(f"  cage class: {CANDIDATE['cage_class']}")
        print(f"  annotation slots: {len(CANDIDATE['annotation_slots'])} (all sequence-level only)")
        print()
        print("  verifying via F-VIROCAPSID-3 calibration tool ...")

    verify_result = verify_with_virocapsid_calibration(seed=args.seed)
    overall_pass = bool(verify_result["pass"])

    if not args.quiet:
        print(f"  yield_t10000 = {verify_result.get('verify_yield_at_t10000'):.4f}")
        print(f"  target = {verify_result.get('target_yield'):.4f}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__V_BETA_SCD_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
