#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
virocapsid_kinetic_trap_remediation.py — F-VIROCAPSID-4 trap remediation.

Iteration 11 of the /loop closure session found F-VIROCAPSID-4-kinetic-trap
FAIL by 1.5 percentage points (y_aberrant_max = 0.1647 > 0.15 threshold)
at the cycle-24 stability-corner params {K12=1e-6, K21=1e-4, K_CLOSE=1e-7,
K_OPEN=1e-14}. This script attempts remediation via small parameter
perturbations seeking joint:

  PASS criterion:
    y_aberrant_max < 0.15  AND  y_closed_final >= 0.85

The cycle-24 baseline already satisfies y_closed_final >= 0.85; the
question is whether any nearby param point satisfies BOTH simultaneously.

Per cross-cutting Require (R5) raw 9 hexa-only: **Python stdlib only.**
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cage_assembly_simulation as cas  # noqa: E402

REGISTRY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "state",
    "discovery_absorption",
    "registry.jsonl",
)

BASELINE = {"K12": 1e-6, "K21": 1e-4, "K_CLOSE": 1e-7, "K_OPEN": 1e-14}
PASS_R_AGG = 0.15
PASS_YIELD = 0.85


def run_traj(K12, K21, K_CLOSE, K_OPEN, c0=60.0, t_end=10000.0, dt=0.01):
    cas.K12 = K12
    cas.K21 = K21
    cas.K_CLOSE = K_CLOSE
    cas.K_OPEN = K_OPEN
    sample_times = [t_end * (i / 100) for i in range(101)]
    result = cas.integrate("backward_euler", c0=c0, t_end=t_end, dt=dt,
                            sample_times=sample_times)
    samples = result["samples"]
    mass0 = result["mass0"]
    y_aberrant_max = 0.0
    y_closed_final = 0.0
    for t, state in samples:
        c0v, c1v, c2v, c3v = state
        y_pent = (5.0 * c1v) / mass0
        y_hex = (6.0 * c2v) / mass0
        y_aberrant = y_pent + y_hex
        if y_aberrant > y_aberrant_max:
            y_aberrant_max = y_aberrant
        y_closed_final = (cas.N_CP_PER_CAGE * c3v) / mass0
    return y_aberrant_max, y_closed_final


def main(argv):
    p = argparse.ArgumentParser(description="F-VIROCAPSID-4 trap remediation sweep")
    p.add_argument("--emit", action="store_true")
    p.add_argument("--summary", action="store_true")
    args = p.parse_args(argv)

    # K_CLOSE sweep: faster closure should drain intermediates earlier.
    # K12 sweep: slower nucleation should suppress intermediate burst.
    candidates = []
    K_CLOSE_grid = [1e-7, 3e-7, 1e-6, 3e-6, 1e-5]
    K12_grid     = [3e-7, 1e-6, 3e-6]
    for K_CLOSE in K_CLOSE_grid:
        for K12 in K12_grid:
            params = {"K12": K12, "K21": 1e-4, "K_CLOSE": K_CLOSE, "K_OPEN": 1e-14}
            y_aberrant_max, y_closed_final = run_traj(**params)
            r_agg_pass = y_aberrant_max < PASS_R_AGG
            yield_pass = y_closed_final >= PASS_YIELD
            joint_pass = r_agg_pass and yield_pass
            candidates.append({
                "params": params,
                "y_aberrant_max": y_aberrant_max,
                "y_closed_final": y_closed_final,
                "r_agg_pass": r_agg_pass,
                "yield_pass": yield_pass,
                "joint_pass": joint_pass,
            })
            sys.stderr.write(
                f"K12={K12:.1e} K_CLOSE={K_CLOSE:.1e}  "
                f"y_aberrant_max={y_aberrant_max:.4f}  "
                f"y_closed_final={y_closed_final:.4f}  "
                f"joint_pass={joint_pass}\n"
            )

    joint_passers = [c for c in candidates if c["joint_pass"]]
    audited_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    witness = {
        "schema": "raw_77_virocapsid_kinetic_trap_remediation_v1",
        "audited_at": audited_at,
        "audit_kind": "f_virocapsid_4_kinetic_trap_param_sweep",
        "baseline": BASELINE,
        "n_candidates_tested": len(candidates),
        "n_joint_passers": len(joint_passers),
        "joint_passers": joint_passers,
        "all_candidates": candidates,
        "f_virocapsid_4_kinetic_trap_remediation": {
            "verdict": "PASS" if joint_passers else "FAIL",
            "best_params": joint_passers[0]["params"] if joint_passers else None,
            "criteria": {
                "y_aberrant_max_lt_0p15": True,
                "y_closed_final_ge_0p85": True,
            },
            "raw_91_c3_disclose": (
                "Param sweep over K_CLOSE × K12 grid (5×3=15 candidates) "
                "seeking joint PASS (y_aberrant_max < 0.15 AND y_closed_final "
                ">= 0.85). PASS = at least one candidate satisfies both. "
                "Identifies remediation point for cycle-24 stability-corner "
                "params (which fail r_agg by 1.5pp)."
            ),
        },
        "raw_77_append_only": True,
        "witness_ref": "state/discovery_absorption/registry.jsonl#raw_77_virocapsid_kinetic_trap_remediation_v1",
    }

    if args.emit:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(witness, ensure_ascii=False, sort_keys=True) + "\n")
        sys.stderr.write(f"emitted 1 witness row -> {REGISTRY_PATH}\n")

    if args.summary:
        print(json.dumps(witness, sort_keys=True, indent=2))

    return 0 if joint_passers else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
