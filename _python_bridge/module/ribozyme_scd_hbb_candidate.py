#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ribozyme_scd_hbb_candidate.py — C2 cell R·β (RIBOZYME × β=SCD).

Cycle 25 deliverable. Applies the existing F-RB-4 hammerhead-minimal 12-nt
4-state kinetics simulator to record a candidate ribozyme spec annotated
against publicly catalogued HBB pre-mRNA context referenced in open-access
hematology research literature.

IN-SILICO numerical primitive verification ONLY. NOT a clinical, regulatory,
or wet-lab claim. PASS verifies kinetics-model output (k_cat/K_M ≤ Eigen-
Hammes ceiling, mass conservation, RK4-Euler agreement) — does NOT verify
HBB-specific cleavage activity, in-cell catalytic efficacy, off-target
profile, delivery, or any biological outcome.

Per cross-cutting Require: (R1)/(R2) no edits to canonical/audited bridges,
(R4) registry append-only raw_77, (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell R·β at IN-SILICO
grade. C3+ is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ribozyme_kinetics_simulation as rb  # noqa: E402


CANDIDATE = {
    "target_disease_class_label": "beta_SCD",
    "matrix_cell_label": "R_beta",
    "target_pre_mrna": "HBB pre-mRNA (β-globin precursor)",
    "target_pre_mrna_reference": "HBB RefSeq (public sequence database)",
    "construct_class": "hammerhead-minimal trans-cleaving ribozyme",
    "construct_topology": "5'-arm(12nt)-CATALYTIC_CORE(12nt)-3'-arm(12nt)",
    "catalytic_core_12nt": rb.CATALYTIC_CORE_12NT,
    "substrate_cleavage_motif": "NUH↓ triplet (canonical hammerhead)",
    # Illustrative substrate-recognition arms — public-literature-anchored
    # HBB pre-mRNA context. NOT clinically validated.
    "substrate_recognition_arm_5p_12nt": "GCAUACGUUACG",
    "substrate_recognition_arm_3p_12nt": "AGCCAUUGCCGA",
    "full_designed_ribozyme_36nt": (
        "GCAUACGUUACG" + rb.CATALYTIC_CORE_12NT + "AGCCAUUGCCGA"
    ),
    "n6_invariant_role": (
        "σ(6)=12 catalytic-core nucleotide count preserved; τ(6)=4 reaction "
        "states inherited from F-RB-4 baseline."
    ),
    "source_literature_anchors": [
        "HBB pre-mRNA — public open-access hematology / sequence database",
        "Hammerhead ribozyme design: Symons 1981; Hertel & Uhlenbeck 1992",
    ],
    "downstream_layer_handoff": [
        "ribozyme delivery (LNP / AAV / exosome) → NANOBOT or VIROCAPSID at next layer",
        "in-cell efficacy / off-target / pharmacokinetics → wet-lab (out-of-repo, C3+)",
    ],
}


def verify_with_ribozyme_sim(t_end=600.0, dt=0.01, S_eff=1.0):
    sample_times = [t for t in rb.SAMPLE_TIMES if t <= t_end]
    if not sample_times or sample_times[-1] != t_end:
        sample_times.append(t_end)

    n6_check = rb.n6_invariant_check()
    rk4_result = rb.integrate("rk4", t_end, dt, sample_times, S_eff=S_eff)
    euler_result = rb.integrate("euler", t_end, dt, sample_times, S_eff=S_eff)
    kinetics = rb.compute_kcat_KM(rk4_result, S_eff=S_eff)
    pass_eval = rb.evaluate_pass(rk4_result, euler_result, kinetics)
    return {
        "n6_check": n6_check,
        "kinetics": kinetics,
        "pass_eval": pass_eval,
        "rk4_final": list(rk4_result["final"]),
        "samples_count": len(rk4_result["samples"]),
    }


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_eval"]
    kin = verify_result["kinetics"]
    overall_pass = bool(pe["overall_pass"])

    row = {
        "schema": "raw_77_c2_ribozyme_scd_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-r-beta-scd-hbb-ribozyme-candidate",
        "domain": "hexa-ribozyme",
        "matrix_cell": "R_beta",
        "disease_class_label": "beta_SCD",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "ribozyme_kinetics_simulation.py (F-RB-4 PASS, cycle 24 C0b)",
            "kinetics_pass": overall_pass,
            "k_cat_per_min": kin.get("k_cat_per_min"),
            "K_M_uM": kin.get("K_M_uM"),
            "kcat_over_KM": kin.get("kcat_over_KM"),
            "eigen_hammes_ceiling": 1.0e9,
            "diffusion_margin_log10": kin.get("diffusion_margin_log10"),
            "eigen_hammes_pass": (kin.get("kcat_over_KM") is not None
                                  and kin["kcat_over_KM"] <= 1.0e9),
            "pass_count": pe["pass_count"],
            "total_count": pe["total_count"],
        },
        "n6_invariant": verify_result["n6_check"],
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, regulatory, or treatment claim is being made or implied."
        ),
        "raw_91_c3_disclose": [
            "Substrate-recognition arms are illustrative reverse-complements "
            "of public HBB pre-mRNA context — they demonstrate the design "
            "step's arm-length convention, not a clinically validated "
            "targeting sequence.",
            "Kinetics PASS is sequence-INDEPENDENT in the F-RB-4 model — rate "
            "constants come from Eyring TST + Turner NN, not from explicit "
            "substrate-arm pairing. PASS verifies internal model consistency, "
            "NOT HBB-specific in-cell cleavage.",
            "Ribozyme delivery (LNP / AAV / exosome) is out-of-scope at this "
            "primitive — handoff to NANOBOT or VIROCAPSID at next layer.",
            "16-cell matrix R·β at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports ribozyme_kinetics_simulation (F-RB-4 PASS, cycle 24 "
            "C0b) as module; reuses its API (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/ViennaRNA",
        "raw_138_sentinel": (
            "__R_BETA_SCD_C2__ "
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
        description="HEXA-BIO C2 cell R·β (RIBOZYME × β=SCD): in-silico "
                    "hammerhead candidate annotated against publicly "
                    "catalogued HBB pre-mRNA context — verified via F-RB-4."
    )
    ap.add_argument("--t-end", type=float, default=600.0)
    ap.add_argument("--dt", type=float, default=0.01)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[ribozyme_scd_hbb_candidate] C2 cell R·β — SCD × RIBOZYME")
        print(f"  target pre-mRNA: {CANDIDATE['target_pre_mrna']}")
        print(f"  designed 36-nt: 5'-{CANDIDATE['full_designed_ribozyme_36nt']}-3'")
        print(f"  catalytic core (σ=12): 5'-{CANDIDATE['catalytic_core_12nt']}-3'")
        print()
        print("  verifying via F-RB-4 simulator ...")

    verify_result = verify_with_ribozyme_sim(t_end=args.t_end, dt=args.dt)
    pe = verify_result["pass_eval"]
    kin = verify_result["kinetics"]
    overall_pass = bool(pe["overall_pass"])

    if not args.quiet:
        print(f"  k_cat = {kin.get('k_cat_per_min'):.4f} min^-1")
        print(f"  K_M   = {kin.get('K_M_uM'):.4f} uM")
        print(f"  k_cat/K_M = {kin.get('kcat_over_KM'):.3e} M^-1 s^-1")
        print(f"  Eigen-Hammes margin = {kin.get('diffusion_margin_log10'):.2f} orders")
        print(f"  PASS criteria: {pe['pass_count']}/{pe['total_count']}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__R_BETA_SCD_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
