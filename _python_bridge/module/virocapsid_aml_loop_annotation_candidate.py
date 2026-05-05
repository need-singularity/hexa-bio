#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
virocapsid_aml_loop_annotation_candidate.py — C2 cell V·α (VIROCAPSID × α=AML).

Cycle 25 deliverable. Applies the existing F-VIROCAPSID-3 calibration tool
(`virocapsid_calibration.py`, C0b PASS 2026-05-05) plus the underlying
4-state Zlotnick assembly-kinetics ODE (`cage_assembly_simulation.py`,
READ-ONLY per R2) to record a candidate spec for a T=1 60-subunit
icosahedral protein cage with a surface-loop peptide annotation derived
from public open-access oncology research literature for the marker WT1.

This is purely IN-SILICO numerical primitive verification on literature-
sourced metadata. NOT a clinical, regulatory, or wet-lab claim. The
simulator's PASS criterion verifies the cage primitive's assembly-kinetics
stability under STNV-calibrated rate constants (existing C0b deliverable)
— it does NOT verify any biological property of the inserted peptide
annotation.

Per cross-cutting Require:
  (R1) No n6-architecture canonical edits.
  (R2) No edits to existing audited bridges (cage_assembly_simulation.py,
       polyhedral_cage_bayesian_audit.py, virocapsid_calibration.py itself,
       ribozyme_kinetics_simulation.py, weave_composition.py,
       nanobot_actuation_simulation.py).
  (R4) Witness → state/discovery_absorption/registry.jsonl, schema
       raw_77_c2_virocapsid_aml_v1, append-only.
  (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell V·α at IN-SILICO
grade. C3+ (wet-lab / IND / phase I) is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import virocapsid_calibration as vc  # noqa: E402


# ---------------------------------------------------------------------------
# Candidate spec
# ---------------------------------------------------------------------------

# Marker WT1 is referenced as a PUBLIC OPEN-ACCESS LITERATURE CATALOGUED
# entity only. The peptide sequence annotation is illustrative literature
# reference. The simulator does NOT model peptide-MHC interaction,
# conformational rearrangement, immune presentation, or any biological
# process — surface-loop peptide annotation is a sequence-level metadata
# field only.

CANDIDATE = {
    "target_disease_class_label": "alpha_AML",
    "matrix_cell_label": "V_alpha",
    "peptide_marker_referenced": "WT1",
    "cage_class": "T=1 60-subunit icosahedral polyhedron",
    "t_number": 1,
    "n_cp_per_cage": 60,
    "n_pent_per_cage": 12,
    "surface_loop_peptide_annotation": {
        "annotation_type": "sequence-level metadata field",
        "peptide_seq_lit_ref": "RMFPNAPYL (WT1 short peptide, public open-access literature reference)",
        "loop_insertion_topology": "surface-exposed loop (illustrative, not modeled)",
        "modeled_by_simulator": False,
        "biological_process_modeled": "none",
    },
    "n6_invariant_role": (
        "σ(6)=12 pentamer vertex count (Caspar-Klug T=1 invariant); "
        "τ(6)=4 assembly states (free CP / pentamer / hexamer / closed cage); "
        "φ(6)=2 closed vs open shell; "
        "J₂=24 octahedral O ⊂ icosahedral I subgroup."
    ),
    "source_literature_anchors": [
        "WT1 marker — public open-access oncology research literature",
        "T=1 60-subunit icosahedral cage geometry — Caspar-Klug 1962",
        "4-state assembly kinetics — Zlotnick 2003 nucleation-elongation ODE",
    ],
    "downstream_layer_handoff": [
        "formulation / delivery / route / dose / adjuvant → out-of-scope at this primitive",
        "immunological / regulatory / clinical → out-of-repo (C3+)",
        "peptide-MHC interaction modeling → out-of-scope (sequence-level annotation only)",
    ],
}


# ---------------------------------------------------------------------------
# Verification via existing F-VIROCAPSID-3 calibration tool
# ---------------------------------------------------------------------------

def verify_with_virocapsid_calibration(seed=42):
    """Invoke virocapsid_calibration.calibrate_one() in --mode verify with
    the default STNV (T=1) reference. The simulator is annotation-INDEPENDENT
    at the assembly-kinetics level — it operates on rate constants
    {K12, K21, K_CLOSE, K_OPEN} derived from Zlotnick 2003, not on explicit
    peptide-loop content. This wrapper records that the candidate's
    intended marker is the publicly catalogued WT1 reference while the
    calibration PASS verifies infrastructure correctness (yield ≥ 0.85 at
    t=10000s, mass conservation, finite_ok).
    """
    return vc.calibrate_one(
        ref_system="stnv",
        mode="verify",
        seed=seed,
        verbose=False,
    )


# ---------------------------------------------------------------------------
# Witness emission (raw_77_c2_virocapsid_aml_v1)
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    overall_pass = bool(verify_result["pass"])

    row = {
        "schema": "raw_77_c2_virocapsid_aml_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-v-alpha-aml-loop-annotation-candidate",
        "domain": "hexa-virocapsid",
        "matrix_cell": "V_alpha",
        "disease_class_label": "alpha_AML",
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
            "clinical, regulatory, immunological, therapeutic, or treatment "
            "claim is being made or implied."
        ),
        "raw_91_c3_disclose": [
            "The disease_class_label 'alpha_AML' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; it does NOT denote any clinical, "
            "therapeutic, or treatment proposal.",
            "Marker WT1 is referenced as a PUBLIC OPEN-ACCESS LITERATURE "
            "CATALOGUED entity only. The peptide sequence annotation is "
            "illustrative literature reference.",
            "PASS criterion verifies the cage primitive's assembly-kinetics "
            "stability under STNV-calibrated rate constants (existing C0b "
            "deliverable) — it does NOT verify any biological property of "
            "the inserted peptide annotation.",
            "Surface-loop peptide annotation is a sequence-level metadata "
            "field; the simulator does NOT model peptide-MHC interaction, "
            "conformational rearrangement, immune presentation, or any "
            "biological process.",
            "Downstream layers (formulation, delivery, regulatory, clinical) "
            "are explicitly out-of-repo per (R6) hexa-bio scope.",
            "16-cell matrix V·α at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports virocapsid_calibration (F-VIROCAPSID-3 PASS, cycle 24 "
            "C0b) as module; reuses its calibrate_one API in --mode verify "
            "without modification (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__V_ALPHA_AML_C2__ "
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
        description="HEXA-BIO C2 cell V·α (VIROCAPSID × α=AML): in-silico "
                    "candidate spec for T=1 60-subunit cage with a surface-loop "
                    "peptide annotation derived from public open-access "
                    "literature for the marker WT1 — verified via "
                    "F-VIROCAPSID-3 calibration tool. Pure stdlib."
    )
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true",
                    help="skip writing C2 witness row to registry")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[virocapsid_aml_loop_annotation_candidate] C2 cell V·α — AML × VIROCAPSID")
        print(f"  peptide marker referenced: {CANDIDATE['peptide_marker_referenced']}")
        print(f"  cage class: {CANDIDATE['cage_class']}")
        print(f"  surface-loop annotation: "
              f"{CANDIDATE['surface_loop_peptide_annotation']['peptide_seq_lit_ref']}")
        print(f"  modeled_by_simulator: "
              f"{CANDIDATE['surface_loop_peptide_annotation']['modeled_by_simulator']}")
        print()
        print("  verifying via F-VIROCAPSID-3 calibration tool (--mode verify) ...")

    verify_result = verify_with_virocapsid_calibration(seed=args.seed)
    overall_pass = bool(verify_result["pass"])

    if not args.quiet:
        print(f"  yield_t10000 = {verify_result.get('verify_yield_at_t10000'):.4f}")
        print(f"  target = {verify_result.get('target_yield'):.4f}")
        print(f"  mass_drift_rel = {verify_result.get('verify_mass_drift_rel'):.2e}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__V_ALPHA_AML_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
