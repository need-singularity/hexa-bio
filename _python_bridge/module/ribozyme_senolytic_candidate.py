#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ribozyme_senolytic_candidate.py — C2 cell R·δ (RIBOZYME × δ=senolytic).
IN-SILICO numerical primitive verification ONLY.
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
    "target_disease_class_label": "delta_senolytic",
    "matrix_cell_label": "R_delta",
    "target_pre_mrna_or_rna": "SASP-associated cytokine mRNA reference (illustrative IL-6-class)",
    "target_reference": "public open-access aging / senescence research literature",
    "construct_class": "hammerhead-minimal trans-cleaving ribozyme",
    "construct_topology": "5'-arm(12nt)-CATALYTIC_CORE(12nt)-3'-arm(12nt)",
    "catalytic_core_12nt": rb.CATALYTIC_CORE_12NT,
    "substrate_cleavage_motif": "NUH↓ triplet (canonical hammerhead)",
    "substrate_recognition_arm_5p_12nt": "GCCAUACCUUGC",  # illustrative
    "substrate_recognition_arm_3p_12nt": "AGCAUUGCCAGU",  # illustrative
    "full_designed_ribozyme_36nt": (
        "GCCAUACCUUGC" + rb.CATALYTIC_CORE_12NT + "AGCAUUGCCAGU"
    ),
    "n6_invariant_role": "σ(6)=12 catalytic core preserved; τ(6)=4 reaction states.",
    "source_literature_anchors": [
        "SASP cytokine mRNA reference — public open-access aging research literature",
        "Hammerhead ribozyme: Symons 1981; Hertel & Uhlenbeck 1992",
    ],
    "downstream_layer_handoff": [
        "delivery (LNP/AAV/exosome) → NANOBOT or VIROCAPSID at next layer",
        "in-cell efficacy → wet-lab (out-of-repo, C3+)",
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
    return {"n6_check": n6_check, "kinetics": kinetics, "pass_eval": pass_eval}


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption", "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_eval"]
    kin = verify_result["kinetics"]
    overall_pass = bool(pe["overall_pass"])
    row = {
        "schema": "raw_77_c2_ribozyme_senolytic_v1",
        "ts": ts, "cycle": 25,
        "phase": "c2-r-delta-senolytic-ribozyme-candidate",
        "domain": "hexa-ribozyme", "matrix_cell": "R_delta",
        "disease_class_label": "delta_senolytic",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "ribozyme_kinetics_simulation.py (F-RB-4 PASS, cycle 24 C0b)",
            "kinetics_pass": overall_pass,
            "k_cat_per_min": kin.get("k_cat_per_min"),
            "K_M_uM": kin.get("K_M_uM"),
            "kcat_over_KM": kin.get("kcat_over_KM"),
            "diffusion_margin_log10": kin.get("diffusion_margin_log10"),
            "eigen_hammes_pass": (kin.get("kcat_over_KM") is not None
                                  and kin["kcat_over_KM"] <= 1.0e9),
            "pass_count": pe["pass_count"],
            "total_count": pe["total_count"],
        },
        "n6_invariant": verify_result["n6_check"],
        "in_silico_grade_disclose": "IN-SILICO numerical-primitive verification ONLY.",
        "raw_91_c3_disclose": [
            "Substrate-recognition arms are illustrative reverse-complements; NOT clinically validated.",
            "Kinetics PASS is sequence-INDEPENDENT in F-RB-4 model.",
            "Delivery → NANOBOT/VIROCAPSID at next layer.",
            "16-cell matrix R·δ at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": "Imports ribozyme_kinetics_simulation (R2 preserved).",
        "raw_9_hexa_only": "python stdlib only",
        "raw_138_sentinel": "__R_DELTA_SENOLYTIC_C2__ " + ("PASS" if overall_pass else "FAIL"),
        "raw_77_append_only": True,
    }
    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(description="HEXA-BIO C2 cell R·δ")
    ap.add_argument("--t-end", type=float, default=600.0)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    verify_result = verify_with_ribozyme_sim(t_end=args.t_end)
    pe = verify_result["pass_eval"]
    overall_pass = bool(pe["overall_pass"])

    if not args.no_emit:
        emit_c2_witness(verify_result)

    print("__R_DELTA_SENOLYTIC_C2__ " + ("PASS" if overall_pass else "FAIL"))
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
