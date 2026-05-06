#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanobot_n_r2_boundary_audit.py — F-NB-5 sister-axis collision-overlap measurement.

Implements the hexa-bio side of the F-NB-5 (sister-axis collision audit)
boundary protocol declared in `.roadmap.nanobot` N-R2. Quantifies the
architectural-primitive overlap between hexa-bio NANOBOT (single-molecule
architectural primitive, L0-L6) and life/therapeutic-nanobot/ (clinical-
application system, L7-L9).

Procedure:

  1. Extract L0-L6 primitive enumeration from cycle-24 actuation MVP
     witness raw_77_nanobot_actuation_v1 (in-repo registry).
  2. Look for canonical handoff JSON at the path declared in N-R2:
       ~/core/n6-architecture/domains/life/therapeutic-nanobot/handoff/
       2026-05-28_hexa-nanobot-therapeutic-nanobot-boundary.json
  3. If absent → emit witness with status=CANONICAL_PENDING and
     collision_overlap_ratio=null. Hexa-bio side mitigation already
     declared in N-R2 (single-molecule scope, L0-L6); cross-repo
     canonical edits handled in separate n6-architecture session per
     memory/feedback_cross_repo_canonical.md.
  4. If present → parse canonical L7-L9 enumeration, compute Jaccard
       collision_overlap_ratio = |L0_L6 ∩ L7_L9| / |L0_L6 ∪ L7_L9|
     PASS if ratio < 0.5 per F-NB-1-c gate (.roadmap.nanobot:66).

Per cross-cutting Require (R5) raw 9 hexa-only: **Python stdlib only.**

Usage:

    python3 nanobot_n_r2_boundary_audit.py --emit
    python3 nanobot_n_r2_boundary_audit.py --summary
    python3 nanobot_n_r2_boundary_audit.py --canonical-path /custom/path.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

REGISTRY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "state",
    "discovery_absorption",
    "registry.jsonl",
)

DEFAULT_CANONICAL_HANDOFF_PATH = os.path.expanduser(
    "~/core/n6-architecture/domains/life/therapeutic-nanobot/handoff/"
    "2026-05-28_hexa-nanobot-therapeutic-nanobot-boundary.json"
)

THRESHOLD_OVERLAP_RATIO = 0.5  # F-NB-1-c gate per .roadmap.nanobot:66


def load_latest_witness(schema: str) -> dict | None:
    """Return latest registry row of given schema (by ts/audited_at)."""
    rows: list[dict] = []
    if not os.path.exists(REGISTRY_PATH):
        return None
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("schema") == schema:
                rows.append(obj)
    if not rows:
        return None
    return sorted(rows, key=lambda r: r.get("ts") or r.get("audited_at") or "")[-1]


def extract_l0_l6_primitives(actuation_witness: dict) -> list[str]:
    """Extract L0-L6 architectural primitives from actuation witness.

    L0..L6 single-machine-kinetics enumeration (atoms-level architectural
    primitive scope per N-R2 line 37):

      L0  atomic vertex topology (12-vertex truncated icosahedron)
      L1  n6 invariant lattice (sigma_6 / tau_6 / phi_6 / J2)
      L2  Brownian thermal floor (kT @ T_kelvin)
      L3  Stokes-drag Langevin dynamics
      L4  Markov 4-state motor cycle (S0..S3)
      L5  J2=24 octahedral pose canonicalization
      L6  per-cycle work output (single-machine kinetics)
    """
    primitives: list[str] = []

    # L0: vertex topology
    skeleton = actuation_witness.get("skeleton")
    n_vert = actuation_witness.get("skeleton_vertex_count")
    if skeleton and n_vert:
        primitives.append(f"L0_vertex_topology:{skeleton}:n={n_vert}")

    # L1: n6 invariant
    n6 = actuation_witness.get("n6_invariant") or {}
    if n6:
        primitives.append(
            "L1_n6_invariant:sigma_6={s}:tau_6={t}:phi_6={p}:J2={j}".format(
                s=n6.get("sigma_6"),
                t=n6.get("tau_6"),
                p=n6.get("phi_6"),
                j=n6.get("J2"),
            )
        )

    # L2: Brownian thermal floor
    T = actuation_witness.get("T_kelvin")
    kT = actuation_witness.get("kT_J")
    if T is not None:
        primitives.append(f"L2_brownian_floor:T_kelvin={T}:kT_J={kT}")

    # L3: Stokes-drag Langevin
    gamma = actuation_witness.get("gamma_Ns_per_m")
    if gamma is not None:
        primitives.append(f"L3_stokes_langevin:gamma_Ns_per_m={gamma}")

    # L4: Markov 4-state motor cycle
    state_visits = actuation_witness.get("state_visit_counts") or {}
    if state_visits:
        states = sorted(state_visits.keys())
        primitives.append(
            "L4_markov_motor_cycle:n_states={n}:states={s}".format(
                n=len(states), s=",".join(states)
            )
        )

    # L5: J2=24 pose canonicalization
    speedup = actuation_witness.get("pose_canonicalize_speedup_factor")
    if speedup is not None:
        primitives.append(f"L5_j2_pose_canonicalization:speedup={speedup}")

    # L6: per-cycle work (single-machine kinetics)
    work_kT = actuation_witness.get("work_per_cycle_kT_units")
    if work_kT is not None:
        primitives.append(
            "L6_single_machine_kinetics:work_per_cycle_kT={w}".format(w=work_kT)
        )

    return primitives


def parse_canonical_handoff(path: str) -> tuple[bool, list[str] | None, str | None]:
    """Try to load canonical L7-L9 enumeration from handoff JSON.

    Returns (present, primitives_or_None, error_message_or_None).

    Expected canonical handoff JSON shape (TBD by n6-architecture
    canonical session per memory/feedback_cross_repo_canonical.md):

        {
          "schema": "raw_77_therapeutic_nanobot_l7_acceptance_v1",
          "l7_l9_primitives": ["L7_drug_load:...", "L8_immune_evasion:...", "L9_biodistribution:..."],
          ...
        }

    The audit script accepts either `l7_l9_primitives` (canonical key) or
    falls back to `expected_consumer_layers` (the field name used in
    raw_77_nanobot_l6_handoff_v1) for graceful schema co-evolution.
    """
    if not os.path.exists(path):
        return False, None, None
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        return True, None, f"canonical handoff parse error: {exc}"

    primitives = data.get("l7_l9_primitives")
    if primitives is None:
        primitives = data.get("expected_consumer_layers")
    if not isinstance(primitives, list):
        return True, None, "canonical handoff missing l7_l9_primitives / expected_consumer_layers list"
    return True, [str(p) for p in primitives], None


def compute_overlap(
    a: list[str], b: list[str]
) -> tuple[float, list[str], list[str]]:
    """Jaccard overlap on string sets."""
    sa, sb = set(a), set(b)
    inter = sa & sb
    union = sa | sb
    if not union:
        return 0.0, [], []
    return len(inter) / len(union), sorted(inter), sorted(union)


def build_witness(
    l0_l6: list[str],
    canonical_path: str,
    canonical_present: bool,
    canonical_l7_l9: list[str] | None,
    canonical_error: str | None,
) -> dict:
    audited_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not canonical_present or canonical_l7_l9 is None:
        # CANONICAL_PENDING — graceful degradation
        status = "CANONICAL_PENDING"
        collision_ratio: float | None = None
        intersection: list[str] | None = None
        union: list[str] | None = None
        criterion_2_pass: bool | None = None
        overall_pass: bool | None = None
        c3_extra = (
            "Canonical handoff JSON absent at expected path "
            "(~/core/n6-architecture/domains/life/therapeutic-nanobot/handoff/"
            "2026-05-28_hexa-nanobot-therapeutic-nanobot-boundary.json). "
            "Hexa-bio side mitigation already declared in .roadmap.nanobot N-R2 "
            "(single-molecule architectural primitive scope L0-L6 vs "
            "clinical-application system L7-L9). Full F-NB-5 closure blocked on "
            "n6-architecture canonical session per "
            "memory/feedback_cross_repo_canonical.md. F-NB-1-c remains "
            "DEFERRED until canonical handoff JSON lands and ratio < 0.5 "
            "is verified."
        )
        if canonical_error:
            c3_extra += f" Parse error encountered: {canonical_error}."
    else:
        ratio, inter, uni = compute_overlap(l0_l6, canonical_l7_l9)
        collision_ratio = ratio
        intersection = inter
        union = uni
        criterion_2_pass = ratio < THRESHOLD_OVERLAP_RATIO
        overall_pass = bool(canonical_present and criterion_2_pass)
        status = "PASS" if overall_pass else "FAIL"
        c3_extra = (
            f"Canonical handoff JSON parsed; computed Jaccard "
            f"|L0-L6 ∩ L7-L9|/|L0-L6 ∪ L7-L9|={ratio:.4f} against threshold "
            f"{THRESHOLD_OVERLAP_RATIO}. F-NB-1-c PASS gate is ratio < threshold."
        )

    crit_1_pass = canonical_present
    pass_count = int(crit_1_pass) + (int(criterion_2_pass) if isinstance(criterion_2_pass, bool) else 0)
    total_count = 2

    witness = {
        "schema": "raw_77_nanobot_n_r2_boundary_audit_v1",
        "ts": audited_at,
        "audited_at": audited_at,
        "cycle": 25,
        "phase": "f-nb-5-boundary-audit",
        "domain": "hexa-nanobot",
        "falsifier": "F-NB-5",
        "status": status,
        "hexa_l0_l6_primitives": l0_l6,
        "canonical_l7_l9_primitives": canonical_l7_l9,
        "canonical_handoff_path": canonical_path,
        "canonical_handoff_present": canonical_present,
        "collision_overlap_ratio": collision_ratio,
        "intersection": intersection,
        "union": union,
        "threshold_overlap_ratio": THRESHOLD_OVERLAP_RATIO,
        "pass_evaluation": {
            "criteria": {
                "1_canonical_handoff_present": {
                    "pass": crit_1_pass,
                    "path": canonical_path,
                },
                "2_collision_overlap_ratio_lt_threshold": {
                    "pass": criterion_2_pass,
                    "ratio": collision_ratio,
                    "threshold": THRESHOLD_OVERLAP_RATIO,
                },
            },
            "pass_count": pass_count,
            "total_count": total_count,
            "overall_pass": overall_pass,
        },
        "deferred_to_cross_repo": not canonical_present,
        "raw_138_sentinel": f"__N_R2_BOUNDARY_AUDIT__ {status}",
        "raw_91_c3_disclose": (
            "(1) Hexa-bio L0-L6 primitives extracted by direct-read of "
            "cycle-24 raw_77_nanobot_actuation_v1 fields (skeleton, "
            "n6_invariant, T_kelvin/kT_J, gamma_Ns_per_m, state_visit_counts, "
            "pose_canonicalize_speedup_factor, work_per_cycle_kT_units). "
            "(2) Collision overlap is Jaccard on canonical-string set "
            "representation; semantic equivalence between L0-L6 and L7-L9 "
            "labels is intentionally string-strict — overlap should be ZERO "
            "for proper L-layer separation, not merely <0.5. (3) Threshold "
            "0.5 is the F-NB-1-c gate per .roadmap.nanobot:66; tighter audit "
            "may apply during cycle-26 canonical handshake. "
            + c3_extra
        ),
        "raw_47_cross_repo": (
            "Self-contained hexa-bio-side audit; READ-ONLY consumer of "
            "canonical handoff JSON published by n6-architecture canonical "
            "session. Schema raw_77_nanobot_n_r2_boundary_audit_v1 parallel "
            "to raw_77_nanobot_l6_handoff_v1 (emission contract) and "
            "raw_77_nanobot_subclause_direct_read_v* (sister-genus closures)."
        ),
        "raw_9_hexa_only": (
            "python stdlib only — no jsonschema / no requests / no yaml. "
            "Filesystem read via os.path.exists + open(); JSON via stdlib json."
        ),
        "raw_53_deterministic": (
            "deterministic given the cycle-24 actuation witness and (when "
            "present) canonical handoff JSON snapshot."
        ),
        "raw_77_append_only": True,
        "witness_ref": "state/discovery_absorption/registry.jsonl#raw_77_nanobot_n_r2_boundary_audit_v1",
    }
    return witness


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(
        description="F-NB-5 sister-axis collision-overlap measurement (hexa-bio side)"
    )
    p.add_argument("--emit", action="store_true", help="Append witness to registry.jsonl")
    p.add_argument("--summary", action="store_true", help="Print full witness JSON to stdout")
    p.add_argument(
        "--canonical-path",
        default=DEFAULT_CANONICAL_HANDOFF_PATH,
        help="Override canonical handoff JSON path (default: per .roadmap.nanobot N-R2)",
    )
    args = p.parse_args(argv)

    actuation = load_latest_witness("raw_77_nanobot_actuation_v1")
    if actuation is None:
        sys.stderr.write(
            "error: missing source witness raw_77_nanobot_actuation_v1 in registry\n"
        )
        return 2

    l0_l6 = extract_l0_l6_primitives(actuation)
    if not l0_l6:
        sys.stderr.write(
            "error: failed to extract L0-L6 primitives from actuation witness\n"
        )
        return 3

    canonical_present, canonical_l7_l9, canonical_error = parse_canonical_handoff(
        args.canonical_path
    )

    witness = build_witness(
        l0_l6=l0_l6,
        canonical_path=args.canonical_path,
        canonical_present=canonical_present,
        canonical_l7_l9=canonical_l7_l9,
        canonical_error=canonical_error,
    )

    if args.emit:
        with open(REGISTRY_PATH, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(witness, ensure_ascii=False, sort_keys=True) + "\n")
        sys.stderr.write(f"emitted witness -> {REGISTRY_PATH}\n")

    if args.summary:
        print(json.dumps(witness, sort_keys=True, indent=2))
    else:
        sys.stderr.write(f"F-NB-5 boundary audit: status={witness['status']}\n")
        sys.stderr.write(
            f"  canonical_handoff_present={witness['canonical_handoff_present']}\n"
        )
        sys.stderr.write(
            f"  collision_overlap_ratio={witness['collision_overlap_ratio']}\n"
        )
        sys.stderr.write(
            f"  hexa_l0_l6_primitives n={len(witness['hexa_l0_l6_primitives'])}\n"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
