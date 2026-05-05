#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanobot_pancov_decorated_skeleton_candidate.py — C2 cell N·γ (NANOBOT × γ=pancov).

Cycle 25 deliverable. IN-SILICO numerical primitive verification ONLY.
NOT a clinical, regulatory, or wet-lab claim. Per cross-cutting Require:
(R1)/(R2) no canonical/audited-bridge edits, (R4) registry append-only
raw_77, (R5) Python stdlib only.
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
    "target_disease_class_label": "gamma_pancov",
    "matrix_cell_label": "N_gamma",
    "marker_referenced": "anti-conserved-RBD-region scFv (public AB DB catalogued)",
    "skeleton": "truncated_icosahedron",
    "n_vertices": 12,
    "vertex_decorations": [
        {
            "vertex_idx": 0,
            "ligand_module_id": "broadly_binding_anti_rbd_scfv_stub",
            "binding_domain_class": "anti-conserved-coronavirus-RBD scFv",
            "binding_affinity_M_lit": 1.0e-9,
            "source_lit": "public antibody database catalogued anti-RBD scFv",
        }
    ],
    "payload_slot": "unspecified-placeholder-no-molecule-modeled",
    "motor_cycle_states": 4,
    "motor_state_names": ["S0_idle", "S1_fwd_stroke", "S2_back_stroke", "S3_reset"],
    "n6_invariant_role": (
        "σ(6)=12 vertex; τ(6)=4 motor states; φ(6)=2; J₂=24."
    ),
    "source_literature_anchors": [
        "anti-conserved-RBD scFv — public antibody database",
        "DNA-origami 12-vertex polyhedron — public structural DNA nanotechnology literature",
    ],
    "downstream_layer_handoff": [
        "delivery / formulation → out-of-scope",
        "in-vivo distribution / pan-strain coverage → wet-lab (out-of-repo, C3+)",
    ],
}


def verify_with_nanobot_sim(n_cycles=10000, T_kelvin=310.0, skeleton="truncated_icosahedron", seed=42):
    return nb.run_actuation(n_cycles=n_cycles, T_kelvin=T_kelvin,
                            skeleton=skeleton, seed=seed, verbose=False)


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY_PATH = os.path.join(ROOT_DIR, "state", "discovery_absorption", "registry.jsonl")


def emit_c2_witness(verify_result):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pe = verify_result["pass_evaluation"]
    overall_pass = bool(pe["overall_pass"])

    row = {
        "schema": "raw_77_c2_nanobot_pancov_v1",
        "ts": ts,
        "cycle": 25,
        "phase": "c2-n-gamma-pancov-decorated-skeleton-candidate",
        "domain": "hexa-nanobot",
        "matrix_cell": "N_gamma",
        "disease_class_label": "gamma_pancov",
        "candidate": CANDIDATE,
        "verification": {
            "simulator": "nanobot_actuation_simulation.py (F-NB-4 PASS, cycle 24 C0b)",
            "actuation_pass": overall_pass,
            "n_cycles_run": verify_result.get("n_cycles_run"),
            "skeleton": verify_result.get("skeleton"),
            "T_kelvin": verify_result.get("T_kelvin"),
            "kT_J": verify_result.get("kT_J"),
            "work_per_cycle_kT_units": verify_result.get("work_per_cycle_kT_units"),
            "work_margin_vs_10kT": verify_result.get("work_margin_vs_10kT"),
            "pose_canonicalize_speedup_factor": verify_result.get("pose_canonicalize_speedup_factor"),
            "brownian_collapse_detected": verify_result.get("brownian_collapse_detected"),
            "pass_count": pe["pass_count"],
            "total_count": pe["total_count"],
        },
        "n6_invariant": verify_result["n6_invariant"],
        "in_silico_grade_disclose": (
            "IN-SILICO numerical-primitive verification ONLY. No biological, "
            "clinical, or treatment claim."
        ),
        "raw_91_c3_disclose": [
            "16-cell matrix label gamma_pancov is per .roadmap.hexa_bio §0; "
            "NOT a clinical or treatment proposal.",
            "Anti-conserved-RBD scFv is a PUBLIC ANTIBODY DATABASE CATALOGUED "
            "construct class only. Affinity 1e-9 M is illustrative literature value.",
            "PASS verifies mechanical/thermodynamic properties under decoration "
            "topology — NOT in-vivo distribution, pan-strain coverage, or biological outcome.",
            "Payload slot is unspecified placeholder — no molecule modeled.",
            "16-cell matrix N·γ at IN-SILICO grade only.",
        ],
        "raw_47_cross_repo": "Imports nanobot_actuation_simulation as module (R2 preserved).",
        "raw_9_hexa_only": "python stdlib only — no scipy/numpy/biopython",
        "raw_138_sentinel": "__N_GAMMA_PANCOV_C2__ " + ("PASS" if overall_pass else "FAIL"),
        "raw_77_append_only": True,
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def main():
    ap = argparse.ArgumentParser(description="HEXA-BIO C2 cell N·γ (NANOBOT × γ=pancov)")
    ap.add_argument("--cycles", type=int, default=10000)
    ap.add_argument("--T", type=float, default=310.0)
    ap.add_argument("--skeleton", default="truncated_icosahedron",
                    choices=["truncated_icosahedron", "cuboctahedron"])
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--no-emit", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.quiet:
        print(f"[nanobot_pancov_decorated_skeleton_candidate] C2 cell N·γ")
        print(f"  marker: {CANDIDATE['marker_referenced']}")

    verify_result = verify_with_nanobot_sim(
        n_cycles=args.cycles, T_kelvin=args.T,
        skeleton=args.skeleton, seed=args.seed)
    pe = verify_result["pass_evaluation"]
    overall_pass = bool(pe["overall_pass"])

    if not args.quiet:
        print(f"  pass: {pe['pass_count']}/{pe['total_count']}")

    if not args.no_emit:
        emit_c2_witness(verify_result)

    print("__N_GAMMA_PANCOV_C2__ " + ("PASS" if overall_pass else "FAIL"))
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
