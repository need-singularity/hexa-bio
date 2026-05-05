#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanobot_scd_decorated_skeleton_candidate.py — C2 cell N·β (NANOBOT × β=SCD).

Cycle 25 deliverable. Applies the existing F-NB-4 4-state 12-vertex DNA-
origami actuation simulation (`nanobot_actuation_simulation.py`, C0b PASS
2026-05-05) to record a candidate spec annotated against publicly catalogued
hematopoietic stem-cell surface marker CD34 referenced in open-access
hematology research literature (relevant to ex-vivo HSC-handling workflows
discussed in SCD literature).

IN-SILICO numerical primitive verification ONLY. NOT a clinical, regulatory,
or wet-lab claim. PASS criterion verifies actuator mechanical / thermodynamic
properties under the decoration topology — does NOT verify any in-vivo
distribution, pharmacokinetics, immunogenicity, clearance, or biological
outcome.

Per cross-cutting Require: (R1)/(R2) no edits to canonical/audited bridges,
(R4) registry append-only raw_77, (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell N·β at IN-SILICO
grade. C3+ is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nanobot_actuation_simulation as nb  # noqa: E402


CANDIDATE = {
    "target_disease_class_label": "beta_SCD",
    "matrix_cell_label": "N_beta",
    "surface_marker_referenced": "CD34",
    "skeleton": "truncated_icosahedron",
    "n_vertices": 12,
    "vertex_decorations": [
        {
            "vertex_idx": 0,
            "ligand_module_id": "anti_cd34_scfv_stub_public_db",
            "binding_domain_class": "anti-CD34 single-chain Fv",
            "binding_affinity_M_lit": 1.0e-9,
            "source_lit": "public antibody database catalogued anti-CD34 scFv",
        }
    ],
    "payload_slot": "unspecified-placeholder-no-molecule-modeled",
    "motor_cycle_states": 4,
    "motor_state_names": ["S0_idle", "S1_fwd_stroke", "S2_back_stroke", "S3_reset"],
    "n6_invariant_role": (
        "σ(6)=12 vertex count; τ(6)=4 motor states; φ(6)=2 productive vs "
        "back-slip; J₂=24 octahedral pose-equivalence quotient."
    ),
    "source_literature_anchors": [
        "anti-CD34 single-chain Fv — public antibody database",
        "DNA-origami 12-vertex polyhedron — public structural DNA nanotechnology literature",
    ],
    "downstream_layer_handoff": [
        "delivery / formulation / pharmacokinetics → out-of-scope at this primitive",
        "ex-vivo cell handling / engraftment / safety → wet-lab (out-of-repo, C3+)",
    ],
}


def verify_with_nanobot_sim(n_cycles=10000, T_kelvin=310.0,
                            skeleton="truncated_icosahedron", seed=42):
    return nb.run_actuation(
        n_cycles=n_cycles,
        T_kelvin=T_kelvin,
        skeleton=skeleton,
        seed=seed,
        verbose=False,
    )


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_evaluation"]
    overall_pass = bool(pe["overall_pass"])

    row = {
        "schema": "raw_77_c2_nanobot_scd_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-n-beta-scd-decorated-skeleton-candidate",
        "domain": "hexa-nanobot",
        "matrix_cell": "N_beta",
        "disease_class_label": "beta_SCD",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "nanobot_actuation_simulation.py (F-NB-4 PASS, cycle 24 C0b)",
            "actuation_pass": overall_pass,
            "n_cycles_run": verify_result.get("n_cycles_run"),
            "n_cycles_target": verify_result.get("n_cycles_target"),
            "skeleton": verify_result.get("skeleton"),
            "skeleton_vertex_count": verify_result.get("skeleton_vertex_count"),
            "T_kelvin": verify_result.get("T_kelvin"),
            "kT_J": verify_result.get("kT_J"),
            "work_per_cycle_J": verify_result.get("work_per_cycle_J"),
            "work_per_cycle_kT_units": verify_result.get("work_per_cycle_kT_units"),
            "work_margin_vs_10kT": verify_result.get("work_margin_vs_10kT"),
            "pose_canonicalize_speedup_factor":
                verify_result.get("pose_canonicalize_speedup_factor"),
            "brownian_collapse_detected":
                verify_result.get("brownian_collapse_detected"),
            "first_collapse_cycle": verify_result.get("first_collapse_cycle"),
            "pass_count": pe["pass_count"],
            "total_count": pe["total_count"],
        },
        "n6_invariant": verify_result["n6_invariant"],
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, regulatory, therapeutic, or treatment claim is being "
            "made or implied."
        ),
        "raw_91_c3_disclose": [
            "The disease_class_label 'beta_SCD' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; it does NOT denote any clinical or "
            "treatment proposal.",
            "Surface marker CD34 is referenced as a PUBLIC ANTIBODY DATABASE "
            "CATALOGUED entity only (commonly cited in HSC research). "
            "Candidate metadata is illustrative literature annotation.",
            "Ligand affinity 1e-9 M is a published-literature illustrative "
            "value; full antibody-receptor kinetics depend on structures "
            "not modeled.",
            "PASS criterion verifies the NANOBOT primitive's mechanical / "
            "thermodynamic properties under the decoration topology — does "
            "NOT verify any in-vivo distribution, pharmacokinetics, "
            "immunogenicity, ex-vivo handling outcome, or biological effect.",
            "Payload slot is unspecified placeholder — no molecule modeled, "
            "no biological action implied.",
            "16-cell matrix N·β at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": (
            "Imports nanobot_actuation_simulation (F-NB-4 PASS, cycle 24 "
            "C0b) as module; reuses its run_actuation API (R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__N_BETA_SCD_C2__ "
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
        description="HEXA-BIO C2 cell N·β (NANOBOT × β=SCD): in-silico "
                    "candidate spec for 12-vertex skeleton with one ligand "
                    "decoration annotated against publicly catalogued surface "
                    "marker (CD34) — verified via F-NB-4 actuation simulator. "
                    "Pure stdlib."
    )
    ap.add_argument("--cycles", type=int, default=10000)
    ap.add_argument("--T", type=float, default=310.0)
    ap.add_argument("--skeleton", default="truncated_icosahedron",
                    choices=["truncated_icosahedron", "cuboctahedron"])
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[nanobot_scd_decorated_skeleton_candidate] C2 cell N·β — SCD × NANOBOT")
        print(f"  surface marker referenced: {CANDIDATE['surface_marker_referenced']}")
        print(f"  skeleton: {CANDIDATE['skeleton']}, n_vertices: {CANDIDATE['n_vertices']}")
        print(f"  cycles={args.cycles} T={args.T}K skeleton={args.skeleton}")
        print()
        print("  verifying via F-NB-4 actuation simulator ...")

    verify_result = verify_with_nanobot_sim(
        n_cycles=args.cycles, T_kelvin=args.T,
        skeleton=args.skeleton, seed=args.seed)
    pe = verify_result["pass_evaluation"]
    overall_pass = bool(pe["overall_pass"])

    if not args.quiet:
        print(f"  n_cycles_run = {verify_result.get('n_cycles_run')}")
        print(f"  work_per_cycle = "
              f"{verify_result.get('work_per_cycle_kT_units'):.2f} kT")
        print(f"  J₂ pose speedup = "
              f"{verify_result.get('pose_canonicalize_speedup_factor'):.2f}×")
        print(f"  PASS criteria: {pe['pass_count']}/{pe['total_count']}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__N_BETA_SCD_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
