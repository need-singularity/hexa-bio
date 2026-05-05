#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ribozyme_aml_flt3_candidate.py — C2 cell R·α (RIBOZYME × α=AML).

Cycle 25 deliverable. Applies the existing F-RB-4 hammerhead-minimal 12-nt
4-state kinetics simulator (`ribozyme_kinetics_simulation.py`, C0b PASS
2026-05-05) to verify a candidate hammerhead ribozyme designed against
FLT3-ITD (FLT3 internal tandem duplication, exon 14 juxtamembrane region)
— a recurrent driver mutation in ~25-30% of AML cases.

This is purely IN-SILICO numerical primitive verification. NOT a clinical,
regulatory, or wet-lab claim. The simulator's PASS criterion verifies the
kinetics-model output (k_cat/K_M ≤ Eigen-Hammes diffusion ceiling, mass
conservation, RK4-Euler agreement) — it does NOT verify FLT3-ITD-specific
cleavage activity, in-cell catalytic efficacy, off-target profile,
delivery, or any biological outcome.

Per cross-cutting Require:
  (R1) No n6-architecture canonical edits.
  (R2) No edits to existing audited bridges.
  (R4) Witness → state/discovery_absorption/registry.jsonl, schema
       raw_77_c2_ribozyme_aml_v1, append-only.
  (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell R·α at IN-SILICO
grade. C3+ (wet-lab / IND / phase I) is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ribozyme_kinetics_simulation as rb  # noqa: E402


# ---------------------------------------------------------------------------
# Candidate spec
# ---------------------------------------------------------------------------

# FLT3-ITD targeting context (public AML genomics literature):
#   - FLT3 (Fms-related tyrosine kinase 3) is mutated in ~25-30% of AML cases
#   - ITD = internal tandem duplication, recurrent in exon 14 juxtamembrane (JM) domain
#   - Reference mRNA: NM_004119 (RefSeq); ITDs typically span codons 580-620
#   - Hammerhead ribozyme cleaves at NUH↓ triplet (where N=any, H=A/C/U)
#
# Substrate-recognition arms (helix I and helix III, 12-nt each) are
# illustrative reverse complements of published FLT3 JM-region context.
# They are NOT a clinically validated targeting sequence — they demonstrate
# that the design pipeline can ingest a real-target context and produce a
# dimer-arm + catalytic-core construct.
#
# Catalytic core: same 12-nt sequence as F-RB-4 baseline (5'-CUGAUGAGGCCG-3',
# Symons 1981 trimmed to σ(6)=12 exactly). Per (R2) the core sequence is
# unchanged — the only candidate-specific design is the substrate-recognition
# arms.

CANDIDATE = {
    "target_disease": "alpha_AML",
    "target_oncogene": "FLT3-ITD",
    "target_oncogene_full_name": "FLT3 internal tandem duplication, exon 14 juxtamembrane domain",
    "target_mrna_reference": "NM_004119 (FLT3 RefSeq)",
    "construct_class": "hammerhead-minimal trans-cleaving ribozyme",
    "construct_topology": "5'-arm(12nt)-CATALYTIC_CORE(12nt)-3'-arm(12nt)",
    "catalytic_core_12nt": rb.CATALYTIC_CORE_12NT,  # CUGAUGAGGCCG (unchanged from F-RB-4)
    "substrate_cleavage_motif": "NUH↓ triplet (canonical hammerhead, N=any, H=A/C/U)",
    # Illustrative substrate-recognition arms — public-literature-anchored
    # FLT3 JM-region context. These are reverse-complementary to a notional
    # NUH↓ context within the FLT3 ITD region. Specific 5' / 3' nucleotide
    # choices are demonstrative of the design step, not clinically validated.
    "substrate_recognition_arm_5p_12nt": "GCCAUACGGUUC",  # complementary to FLT3 JM 5'-context
    "substrate_recognition_arm_3p_12nt": "AGCAUUGCCAGA",  # complementary to FLT3 JM 3'-context
    "full_designed_ribozyme_36nt": (
        "GCCAUACGGUUC" + rb.CATALYTIC_CORE_12NT + "AGCAUUGCCAGA"
    ),
    "n6_invariant_role": (
        "σ(6)=12 catalytic-core nucleotide count preserved; τ(6)=4 reaction "
        "states (substrate-bound / TS / cleaved / product-released) inherited "
        "from F-RB-4 baseline."
    ),
    "source_literature_anchors": [
        "FLT3-ITD epidemiology: ~25-30% AML prevalence, recurrent driver",
        "Hammerhead ribozyme design: Symons 1981; Hertel & Uhlenbeck 1992",
        "RefSeq mRNA: NM_004119 (FLT3 transcript variant 1, public)",
        "k_cat range: 0.1-10 min^-1 canonical hammerhead under Mg2+ 10 mM",
    ],
    "downstream_layer_handoff": [
        "ribozyme delivery (lipid nanoparticle / AAV / exosome) → NANOBOT or VIROCAPSID at next layer",
        "in-cell efficacy / off-target profiling / pharmacokinetics → wet-lab (out-of-repo, C3+)",
    ],
}


# ---------------------------------------------------------------------------
# Verification via existing F-RB-4 simulator
# ---------------------------------------------------------------------------

def verify_with_ribozyme_sim(t_end=600.0, dt=0.01, S_eff=1.0):
    """Run the existing F-RB-4 simulator. The simulator is sequence-
    independent at the kinetics-model level — it operates on rate constants
    {k1, k_minus1, k2, k3, k4} derived from Eyring TST + Turner NN, not on
    explicit substrate sequence. This wrapper records that the candidate's
    intended target is FLT3-ITD while the kinetics PASS verifies physical
    plausibility of the rate-constant set.
    """
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


# ---------------------------------------------------------------------------
# Witness emission (raw_77_c2_ribozyme_aml_v1)
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_eval"]
    kin = verify_result["kinetics"]
    overall_pass = bool(pe["overall_pass"])

    row = {
        "schema": "raw_77_c2_ribozyme_aml_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-r-alpha-aml-flt3-itd-ribozyme-candidate",
        "domain": "hexa-ribozyme",
        "matrix_cell": "R_alpha",
        "disease_class": "alpha_AML",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "ribozyme_kinetics_simulation.py (F-RB-4 PASS, cycle 24 C0b)",
            "kinetics_pass": overall_pass,
            "kcat_per_s": kin.get("k_cat"),
            "kcat_per_min": kin.get("k_cat_per_min"),
            "K_M_uM": kin.get("K_M_uM"),
            "kcat_over_KM": kin.get("kcat_over_KM"),
            "eigen_hammes_ceiling_M_minus1_s_minus1": 1.0e9,
            "diffusion_margin_log10": kin.get("diffusion_margin_log10"),
            "eigen_hammes_pass": (kin.get("kcat_over_KM") is not None
                                  and kin["kcat_over_KM"] <= 1.0e9),
            "pass_count": pe["pass_count"],
            "total_count": pe["total_count"],
        },
        "n6_invariant": verify_result["n6_check"],
        "in_silico_grade_disclose": (
            "IN-SILICO stage only. Numerical-primitive verification of "
            "F-RB-4 simulator under candidate-spec metadata. No clinical, "
            "regulatory, immunological, or wet-lab claim."
        ),
        "raw_91_c3_disclose": [
            "Substrate-recognition arms (12-nt 5' and 12-nt 3') are illustrative "
            "reverse-complements of public FLT3 juxtamembrane region context — "
            "they demonstrate the design-step and arm-length convention, not a "
            "clinically validated targeting sequence.",
            "Kinetics PASS (k_cat/K_M ≤ Eigen-Hammes ceiling, mass conservation, "
            "RK4-Euler agreement) is sequence-INDEPENDENT in the F-RB-4 model — "
            "the rate constants {k1, k_minus1, k2, k3, k4} are derived from "
            "Eyring TST + Turner NN, not from explicit substrate-arm pairing.",
            "Therefore a PASS here verifies that the simulator + candidate "
            "metadata combination is internally consistent — it does NOT verify "
            "FLT3-ITD-specific in-cell cleavage activity, off-target profile, "
            "in-vivo pharmacokinetics, immunogenicity, or therapeutic efficacy.",
            "Ribozyme delivery (lipid nanoparticle / AAV / exosome) is out-of-scope "
            "at this primitive — handoff to NANOBOT (delivery actuator) or "
            "VIROCAPSID (gene cage) at next composition layer.",
            "16-cell matrix R·α at IN-SILICO grade only. Cure-grade requires "
            "C3+ external (CRO / wet-lab / regulatory / clinical).",
        ],
        "raw_47_cross_repo": (
            "Imports ribozyme_kinetics_simulation (F-RB-4 PASS, cycle 24 C0b) "
            "as module; reuses its integrate/compute_kcat_KM/evaluate_pass "
            "API without modification (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/ViennaRNA/biopython",
        "raw_138_sentinel": (
            "__R_ALPHA_AML_C2__ "
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
        description="HEXA-BIO C2 cell R·α (RIBOZYME × α=AML): in-silico "
                    "candidate spec for FLT3-ITD-targeting hammerhead ribozyme "
                    "verified against F-RB-4 kinetics simulator. Pure stdlib."
    )
    ap.add_argument("--t-end", type=float, default=600.0,
                    help="kinetics simulation end time (default 600s)")
    ap.add_argument("--dt", type=float, default=0.01)
    ap.add_argument("--no-emit", action="store_true",
                    help="skip writing witness row to registry")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[ribozyme_aml_flt3_candidate] C2 cell R·α — AML × RIBOZYME")
        print(f"  target: {CANDIDATE['target_oncogene']} "
              f"({CANDIDATE['target_oncogene_full_name']})")
        print(f"  construct: {CANDIDATE['construct_class']}")
        print(f"  designed 36-nt: 5'-{CANDIDATE['full_designed_ribozyme_36nt']}-3'")
        print(f"  catalytic core (12-nt, σ=12): "
              f"5'-{CANDIDATE['catalytic_core_12nt']}-3'")
        print(f"  recognition arms: 5p={CANDIDATE['substrate_recognition_arm_5p_12nt']}, "
              f"3p={CANDIDATE['substrate_recognition_arm_3p_12nt']}")
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
        print(f"  Eigen-Hammes margin = "
              f"{kin.get('diffusion_margin_log10'):.2f} orders below 1e9")
        print(f"  PASS criteria: {pe['pass_count']}/{pe['total_count']}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  witness appended: {REGISTRY_PATH}")

    print(
        "__R_ALPHA_AML_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
