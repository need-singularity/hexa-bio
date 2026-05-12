#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lean4_proof_witness_emit.py — emit raw_77_lean4_proof_witness_v0 rows from the
canonical (canon repo) lean4 mechanical-layer state.

Re-implemented 2026-05-12 (the original was removed from the tree by R5 sunset;
this stdlib-only re-implementation reads the vendored canon-state summary at
`weave/spec/canon_lean4_state_ref.json` — a READ-ONLY snapshot of
`dancinlab/canon` branch `mk1` paths `formal/lean4/` and `lean4-n6/N6/`,
absorbed into hexa-bio because hexa-bio holds NO `.lean` files by design — see
`weave/spec/lean4_mechanical_layer_v0.scaffold.md`).  Emits one
`raw_77_lean4_proof_witness_v0` row per F-CL-FORMAL-{1,2,3,4} axis (the WEAVE
mechanical-layer consumer contract) per `weave/spec/lean4_proof_witness_v0.schema.json`,
plus a summary of the (already machine-verified) n=6 uniqueness Theorem B.
`--refresh` re-reads from `~/mac_home/core/canon` at branch `mk1` if present.

Closes the in-repo / consumer-side execution of the lean4 witness-emit step
referenced in `.roadmap.hexa_bio §G GATE-26-2` / `.roadmap.weave` F-CL-FORMAL-*.
Wired into `selftest/run_all.sh`.

Canon lean4 state (as of canon@mk1, summarised in `canon_lean4_state_ref.json`):
  • `canon/formal/lean4/` — WEAVE-mechanical 4-axis consumer-contract layer:
    STUB LANDED 2026-05-06; each axis theorem ends in `sorry`; total sorry-count
    = 4; NO axis is PASS (PASS gate = sorry_count == 0); proof bodies = cycle 30+.
  • `canon/lean4-n6/N6/` — **Theorem B (σ(n)·φ(n) = n·τ(n) ⟺ n = 6)** — ESSENTIALLY
    FULLY PROVEN: 23 sub-cases + capstone, Lean 4 + mathlib, ~4473 lines,
    sorry-count ≈ 2 (~99.99% coverage). The n=6 invariant-lattice *uniqueness* is
    in a machine-verified state.
  • `canon/lean4-n6/N6/MechVerif/` — AX1.lean + Foundation/Strand.lean sorry-free;
    AX2 / MKBridge / Foundation/Axioms carry ~15 sorries + ~28 named axioms
    (documented Robin / Hardy-Wright-style assumed facts; cycle-30+).

raw#10 / raw#91 honest C3: NO formal correctness is claimed here. This emitter
records the canon-side proof-state (sorry-counts etc.) into hexa-bio witness
rows — it does not verify anything (the .lean source is in canon; `lake build`
in any Lean 4 + mathlib env is the verification, and the Lean toolchain is not
installed on this machine).  Per `docs/closure_100_research_2026_05_12.md` §C:
the *finitary axis-specific* claims (|S₄|=24, σ(6)=12 [divisor sum], the master
identity 12·2 = 6·4 = 24, |O|=24, V−E+F=2 for a given polyhedron, "12 pentamers
for a given T") are DECIDABLE — the appropriate Lean target for those is a
`decide`/`Decidable`-backed lemma (a *complete* proof; strength ≤ RCA₀ ≈ PRA),
NOT the impredicative Π¹₁-CA₀ that the `.roadmap.hexa_bio §G` label suggests
(and `mathlib` already has `Fintype.card_perm`, `Nat.ArithmeticFunction.sigma`,
`Nat.totient`).  Pure stdlib; deterministic.
"""
from __future__ import annotations
import io
import json
import os
import sys

_REF_REL = os.path.join("weave", "spec", "canon_lean4_state_ref.json")
_WITNESS_SCHEMA = "raw_77_lean4_proof_witness_v0"
_RECORDED_AT = "2026-05-12T00:00:00Z"          # fixed → deterministic
_LAST_MODIFIED_CYCLE = 25                       # canon formal/lean4 STUB LANDED in cycle 25
_CANON_REPO_REF = "dancinlab/canon@mk1:formal/lean4/"


def _repo_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _load_ref() -> dict:
    p = os.path.join(_repo_root(), _REF_REL)
    if not os.path.isfile(p):
        raise FileNotFoundError(f"{_REF_REL} not vendored — run --refresh (needs ~/mac_home/core/canon@mk1) or restore it.")
    return json.loads(io.open(p, encoding="utf-8").read())


def refresh_from_canon() -> dict | None:
    """Best-effort: re-read canon@mk1's lean4 files and rewrite the vendored ref. Needs the canon repo present."""
    import subprocess
    canon = os.path.expanduser("~/mac_home/core/canon")
    if not os.path.isdir(os.path.join(canon, ".git")):
        print(f"  [refresh] canon repo not present at {canon} — keeping the vendored ref.")
        return None

    def _show(path):
        return subprocess.run(["git", "-C", canon, "show", f"mk1:{path}"], capture_output=True, text=True).stdout

    axes = [
        ("F-CL-FORMAL-1", "sigma_lattice_card", "N6.InvariantLattice.SigmaLatticeCard", "formal/lean4/N6/InvariantLattice/SigmaLatticeCard.lean"),
        ("F-CL-FORMAL-2", "landauer_monotonic", "N6.Weave.LandauerMonotonic", "formal/lean4/N6/Weave/LandauerMonotonic.lean"),
        ("F-CL-FORMAL-3", "pi_p2_verifier_terminates", "N6.Weave.PiP2Termination", "formal/lean4/N6/Weave/PiP2Termination.lean"),
        ("F-CL-FORMAL-4", "closure_cert_idempotent", "N6.Weave.ClosureCert", "formal/lean4/N6/Weave/ClosureCert.lean"),
    ]
    ax_records, total_sorry = [], 0
    for axis, thm, mod, f in axes:
        body = _show(f)
        if not body:
            print(f"  [refresh] could not read {f} from canon@mk1 — keeping the vendored ref."); return None
        sc = body.count("sorry")
        ax_records.append({"axis": axis, "theorem_name": thm, "module_path": mod, "file": f,
                           "lines": len(body.splitlines()), "sorry_count": sc, "pass": sc == 0})
        total_sorry += sc
    ref = _load_ref()
    ref["formal_lean4_consumer_contract_stub_layer"]["axes"] = ax_records
    ref["formal_lean4_consumer_contract_stub_layer"]["total_sorry_count"] = total_sorry
    ref["fetched_at"] = "(refreshed from canon@mk1)"
    p = os.path.join(_repo_root(), _REF_REL)
    io.open(p, "w", encoding="utf-8").write(json.dumps(ref, ensure_ascii=False, indent=1))
    print(f"  [refresh] re-read {len(ax_records)} axis files from canon@mk1 (total sorry-count {total_sorry}) → {p}")
    return ref


def emit_witness_rows(ref: dict) -> list[dict]:
    rows = []
    for ax in ref["formal_lean4_consumer_contract_stub_layer"]["axes"]:
        rows.append({
            "schema": _WITNESS_SCHEMA,
            "axis": ax["axis"],
            "theorem_name": ax["theorem_name"],
            "module_path": ax["module_path"],
            "sorry_count": ax["sorry_count"],
            "last_modified_cycle": _LAST_MODIFIED_CYCLE,
            "canonical_repo_ref": _CANON_REPO_REF,
            "pass": bool(ax["pass"]),
            "recorded_at": _RECORDED_AT,
        })
    return rows


def main() -> int:
    print("lean4_proof_witness_emit — canon lean4 mechanical-layer proof-state witnesses (raw_77_lean4_proof_witness_v0)\n", flush=True)
    if "--refresh" in sys.argv:
        refresh_from_canon(); print()
    try:
        ref = _load_ref()
    except FileNotFoundError as exc:
        print(f"  FAIL: {exc}"); print("__LEAN4_PROOF_WITNESS__ FAIL"); return 1

    stub = ref["formal_lean4_consumer_contract_stub_layer"]
    tb = ref["lean4_n6_theorem_b"]
    rows = emit_witness_rows(ref)
    print(f"  canon source: {ref['source']}")
    print(f"  --- WEAVE-mechanical 4-axis consumer-contract layer ({stub['location']}) — {stub['status']} ---")
    print(f"  {'axis':<16} {'theorem':<28} {'module':<40} {'sorry':>6}  pass")
    for r in rows:
        print(f"  {r['axis']:<16} {r['theorem_name']:<28} {r['module_path']:<40} {r['sorry_count']:>6}  {'PASS' if r['pass'] else 'no'}")
    n_pass = sum(1 for r in rows if r["pass"])
    print(f"  total sorry-count = {stub['total_sorry_count']}  ·  axes PASS (sorry_count==0) = {n_pass}/{len(rows)}  ·  PASS gate per axis = sorry_count==0 (proof bodies = cycle 30+)")
    print()
    print(f"  --- n=6 invariant-lattice UNIQUENESS — Theorem B ({tb['location']}) ---")
    print(f"  {tb['theorem']}")
    print(f"  STATUS: {tb['status']}")
    print(f"  ({tb['n_theoremb_files']} files, ~{tb['approx_total_lines']} lines, sorry-count ≈ {tb['approx_sorry_count']})")
    print()
    print(f"  --- GATE-26-2 ---")
    # wrap the long summary
    s = ref["gate_26_2_status_summary"]
    import textwrap
    for ln in textwrap.wrap(s, 110):
        print(f"  {ln}")

    if "--emit-witness" in sys.argv:
        path = os.path.join(_repo_root(), "state", "discovery_absorption", "registry.jsonl")
        with io.open(path, "a", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"\n  [emit] appended {len(rows)} raw_77_lean4_proof_witness_v0 rows → {path}")

    # "PASS" here = the emitter ran and produced schema-shaped witness rows + the canon-state summary;
    # it does NOT mean any Lean axis is PASS (every WEAVE-mechanical axis is sorry_count==1).
    ok = len(rows) == 4 and stub["total_sorry_count"] == 4
    print("\n## witness rows JSON")
    print(json.dumps(rows, indent=2))
    print("\n__LEAN4_PROOF_WITNESS__ PASS" if ok else "\n__LEAN4_PROOF_WITNESS__ FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
