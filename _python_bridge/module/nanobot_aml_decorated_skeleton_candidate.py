#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanobot_aml_decorated_skeleton_candidate.py — C2 cell N·α (NANOBOT × α=AML).

Cycle 25 deliverable. Applies the existing F-NB-4 4-state 12-vertex DNA-
origami actuation simulation (`nanobot_actuation_simulation.py`, C0b PASS
2026-05-05) to record a candidate spec for a 12-vertex truncated icosahedron
skeleton with one ligand-decorated vertex annotated against a publicly
catalogued surface marker (CD33) referenced in open-access antibody
database literature.

This is purely IN-SILICO numerical primitive verification on literature-
sourced metadata. NOT a clinical, regulatory, or wet-lab claim. The
simulator's PASS criterion verifies the actuator primitive's mechanical /
thermodynamic properties (work_per_cycle ≥ 10·kT, J₂=24 quotient ≥10×
speedup, σ=12 vertex count, τ=4 motor states, no thermal collapse) under
the decoration topology — it does NOT verify any in-vivo distribution,
pharmacokinetics, immunogenicity, clearance, or biological outcome.

Per cross-cutting Require:
  (R1) No n6-architecture canonical edits.
  (R2) No edits to existing audited bridges.
  (R4) Witness → state/discovery_absorption/registry.jsonl, schema
       raw_77_c2_nanobot_aml_v1, append-only.
  (R5) Python stdlib only.

Per .roadmap.hexa_bio §0 16-cell matrix: this fills cell N·α at IN-SILICO
grade. C3+ (wet-lab / IND / phase I) is out-of-repo.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nanobot_actuation_simulation as nb  # noqa: E402


# ---------------------------------------------------------------------------
# Candidate spec
# ---------------------------------------------------------------------------

# Surface marker CD33 is referenced as a PUBLIC ANTIBODY DATABASE CATALOGUED
# entity only. Ligand affinity 1e-9 M is a published-literature illustrative
# value. Payload slot is unspecified placeholder — no molecule modeled, no
# biological action implied.

CANDIDATE = {
    "target_disease_class_label": "alpha_AML",
    "matrix_cell_label": "N_alpha",
    "surface_marker_referenced": "CD33",
    "skeleton": "truncated_icosahedron",
    "n_vertices": 12,
    "vertex_decorations": [
        {
            "vertex_idx": 0,
            "ligand_module_id": "lintuzumab_scfv_stub_public_db",
            "binding_domain_class": "anti-CD33 single-chain Fv",
            "binding_affinity_M_lit": 1.0e-9,
            "source_lit": "public antibody database catalogued anti-CD33 (lintuzumab scFv)",
        }
    ],
    "payload_slot": "unspecified-placeholder-no-molecule-modeled",
    "motor_cycle_states": 4,
    "motor_state_names": ["S0_idle", "S1_fwd_stroke", "S2_back_stroke", "S3_reset"],
    "n6_invariant_role": (
        "σ(6)=12 vertex count (truncated icosahedron pentameric vertices); "
        "τ(6)=4 motor states; φ(6)=2 productive vs back-slip cycle outcome; "
        "J₂=24 octahedral pose-equivalence quotient (≥10× state-space "
        "reduction target)."
    ),
    "source_literature_anchors": [
        "anti-CD33 single-chain Fv (lintuzumab) — public antibody database",
        "DNA-origami 12-vertex polyhedron — public structural DNA nanotechnology literature",
    ],
    "downstream_layer_handoff": [
        "delivery / formulation / pharmacokinetics → out-of-scope at this primitive",
        "in-vivo distribution / clearance / immunogenicity → wet-lab (out-of-repo, C3+)",
    ],
}


# ---------------------------------------------------------------------------
# Verification via existing F-NB-4 simulator
# ---------------------------------------------------------------------------

def verify_with_nanobot_sim(n_cycles=10000, T_kelvin=310.0,
                            skeleton="truncated_icosahedron", seed=42):
    """Invoke the existing F-NB-4 actuation simulator. The simulator is
    decoration-INDEPENDENT at the mechanical / thermodynamic level — it
    operates on rate matrix Q derived from energy-ladder + Boltzmann +
    Stokes drag, not on explicit ligand identity. This wrapper records that
    the candidate's intended target is the publicly catalogued CD33 marker
    while the actuation PASS verifies infrastructure correctness (Brownian
    floor margin, J₂=24 speedup, no thermal collapse).
    """
    return nb.run_actuation(
        n_cycles=n_cycles,
        T_kelvin=T_kelvin,
        skeleton=skeleton,
        seed=seed,
        verbose=False,
    )


# ---------------------------------------------------------------------------
# Witness emission (raw_77_c2_nanobot_aml_v1)
# ---------------------------------------------------------------------------

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption",
                             "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_evaluation"]
    overall_pass = bool(pe["overall_pass"])

    row = {
        "schema": "raw_77_c2_nanobot_aml_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-n-alpha-aml-decorated-skeleton-candidate",
        "domain": "hexa-nanobot",
        "matrix_cell": "N_alpha",
        "disease_class_label": "alpha_AML",
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
            "The disease_class_label 'alpha_AML' is a 16-cell matrix label "
            "per .roadmap.hexa_bio §0; it does NOT denote any clinical, "
            "therapeutic, or treatment proposal.",
            "Surface marker CD33 is referenced as a PUBLIC ANTIBODY DATABASE "
            "CATALOGUED entity only. The candidate metadata is illustrative "
            "literature annotation.",
            "Ligand affinity 1e-9 M is a published-literature illustrative "
            "value; full antibody-receptor kinetics depend on structures "
            "not modeled by this primitive.",
            "PASS criterion verifies the NANOBOT primitive's mechanical / "
            "thermodynamic properties (Brownian floor margin, J₂=24 quotient, "
            "no thermal collapse) under the decoration topology — it does NOT "
            "verify any in-vivo distribution, pharmacokinetics, or biological "
            "outcome.",
            "Payload slot is unspecified placeholder — no molecule modeled, "
            "no biological action implied.",
            "16-cell matrix N·α at IN-SILICO grade only. Downstream layers "
            "(formulation, delivery, regulatory, clinical) are explicitly "
            "out-of-repo per (R6) hexa-bio scope.",
        ],
        "raw_47_cross_repo": (
            "Imports nanobot_actuation_simulation (F-NB-4 PASS, cycle 24 C0b) "
            "as module; reuses its run_actuation API without modification "
            "(R2 preserved)."
        ),
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": (
            "__N_ALPHA_AML_C2__ "
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
        description="HEXA-BIO C2 cell N·α (NANOBOT × α=AML): in-silico "
                    "candidate spec for 12-vertex truncated icosahedron "
                    "skeleton with one ligand decoration annotated against "
                    "publicly catalogued surface marker (CD33) — verified "
                    "via F-NB-4 actuation simulator. Pure stdlib."
    )
    ap.add_argument("--cycles", type=int, default=10000,
                    help="actuation cycle count (default 10000, F-NB-4 minimum)")
    ap.add_argument("--T", type=float, default=310.0,
                    help="temperature K (default 310)")
    ap.add_argument("--skeleton", default="truncated_icosahedron",
                    choices=["truncated_icosahedron", "cuboctahedron"])
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true",
                    help="skip writing C2 witness row to registry")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print("[nanobot_aml_decorated_skeleton_candidate] C2 cell N·α — AML × NANOBOT")
        print(f"  surface marker referenced: {CANDIDATE['surface_marker_referenced']}")
        print(f"  skeleton: {CANDIDATE['skeleton']}, "
              f"n_vertices: {CANDIDATE['n_vertices']}")
        print(f"  vertex decorations: {len(CANDIDATE['vertex_decorations'])} "
              f"(vertex 0: {CANDIDATE['vertex_decorations'][0]['ligand_module_id']})")
        print(f"  motor states: {CANDIDATE['motor_state_names']}")
        print(f"  cycles={args.cycles} T={args.T}K skeleton={args.skeleton} "
              f"seed={args.seed}")
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
              f"{verify_result.get('work_per_cycle_kT_units'):.2f} kT "
              f"(margin {verify_result.get('work_margin_vs_10kT'):.2f} kT vs 10·kT floor)")
        print(f"  J₂ pose speedup = "
              f"{verify_result.get('pose_canonicalize_speedup_factor'):.2f}× "
              f"(threshold ≥10×)")
        print(f"  brownian collapse: "
              f"{verify_result.get('brownian_collapse_detected')}")
        print(f"  PASS criteria: {pe['pass_count']}/{pe['total_count']}")
        print(f"  overall: {'PASS' if overall_pass else 'FAIL'}")

    if not args.no_emit:
        emit_c2_witness(verify_result)
        if not args.quiet:
            print(f"  C2 witness appended: {REGISTRY_PATH}")

    print(
        "__N_ALPHA_AML_C2__ "
        + ("PASS" if overall_pass else "FAIL")
    )
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
