# lean4_mechanical_layer_v0.scaffold

> **Scaffold spec — consumer's contract, NOT implementation.**
> Actual lean4 code lives in canonical upstream `~/core/n6-architecture/` per
> cross-repo memory rule
> (`memory/feedback_cross_repo_canonical.md`). This file describes what
> hexa-bio expects the canonical layer to expose so that when upstream work
> lands the consumer (hexa-bio) is ready to absorb it.
>
> No `.lean` files in hexa-bio. Spec + JSON Schema only.

**Status**: SCAFFOLD LANDED 2026-05-06 (cycle 25). Cross-repo canonical work
PENDING. Tracks `.roadmap.hexa_bio` §G GATE-26-2 / §B C0h and
`.roadmap.weave` §Falsifier preregister F-CL-FORMAL-1/2/3.

**Last sync**: 2026-05-06 · **Schema version**: v0 (scaffold; promotes to v1
on first canonical drop).

---

## §1 Purpose

GATE-26-2 (lean4-mechanical-extension) promotes sorry-free Foundation from
the WEAVE-only baseline (already PASS pre-cycle-24, see `.roadmap.weave`
status snapshot row "lean4 sorry count = 0") to the four cross-cutting
formal axes labelled F-CL-FORMAL-1/2/3/4. Axis 4 (closure-cert idempotence)
already has a lean4 theorem stub (PARTIAL); axes 1/2/3 are the scope of this
scaffold.

This spec lets hexa-bio:

  (a) lock the **theorem-name vocabulary** consumers should grep for once
      canonical lands;
  (b) define the **witness schema** (`raw_77_lean4_proof_witness_v0`) that
      hexa-bio will emit when canonical reports a proof state, so that
      `state/discovery_absorption/registry.jsonl` can record formal-axis
      progress without waiting on upstream file-system access;
  (c) preserve the **DEFERRED → SCAFFOLD LANDED** lift in
      `.roadmap.weave` and `.roadmap.hexa_bio` so cycle-26+ planning can
      reference a concrete artefact, not a placeholder.

## §2 Theorem signatures (expected)

Each signature is written in lean4 surface syntax with `sorry` as the
proof body — actual proof construction is the canonical-repo deliverable.
Names are normative for the consumer contract: hexa-bio's witness emitter
will look these up by exact name.

### §2.1 F-CL-FORMAL-1 — σ(6)=12 invariant

Axis claim (text): the proteome cardinality / 6-fold symmetry compatibility
constant σ(6) equals 12, matching the n=6 invariant lattice §A.1 entry
(σ(6)=12) of `.roadmap.hexa_bio`.

```lean4
theorem sigma_lattice_card : sigma 6 = 12 := sorry
```

  - **Module path (expected)**: `N6.InvariantLattice.SigmaLatticeCard`
  - **Imports**: `N6.InvariantLattice.Sigma` (canonical definition of σ).
  - **Discharges**: F-CL-FORMAL-1 PASS when `sorry`-count = 0 on this
    theorem (i.e. file compiles without `sorry`).
  - **Witness on PASS**: hexa-bio emits one
    `raw_77_lean4_proof_witness_v0` row with `theorem_name =
    "sigma_lattice_card"`, `sorry_count = 0`.

### §2.2 F-CL-FORMAL-2 — Landauer floor monotonicity

Axis claim (text): `heat_consumed_kT` is non-decreasing under sub-strategy
composition; i.e. composing two Landauer-pass strategies cannot lower the
heat consumed below the max of the two component costs (no free-energy
violation).

```lean4
theorem landauer_monotonic
    (s₁ s₂ : Strategy) (h₁ : LandauerPass s₁) (h₂ : LandauerPass s₂) :
    heatConsumed (compose s₁ s₂) ≥ max (heatConsumed s₁) (heatConsumed s₂)
  := sorry
```

  - **Module path (expected)**: `N6.Weave.LandauerMonotonic`
  - **Imports**: `N6.Weave.Strategy`, `N6.Weave.Landauer`.
  - **Discharges**: F-CL-FORMAL-2 PASS when `sorry`-count = 0.
  - **Pairing with hexa-bio code**: matches Landauer gate semantics in
    `_python_bridge/module/weave_composition.py` (heat_budget_kT field of
    `weave_composition_output_v1` schema).

### §2.3 F-CL-FORMAL-3 — Π^p_2 verifier termination

Axis claim (text): the Π^p_2 verifier is decidable and terminates in
bounded time on the canonical 12-strand catalogue. Pairs with the WEAVE
verifier upgrade GATE-26-3 (greedy v2 ↔ exhaustive v3 path).

```lean4
theorem pi_p2_verifier_terminates
    (cat : StrandCatalogue) (h : cat.size = 12) (q : Pi_p_2_Query cat) :
    ∃ (n : Nat), verifierSteps q ≤ n
  := sorry
```

  - **Module path (expected)**: `N6.Weave.PiP2Termination`
  - **Imports**: `N6.Weave.StrandCatalogue`, `N6.Weave.PiP2Verifier`.
  - **Discharges**: F-CL-FORMAL-3 PASS when `sorry`-count = 0.
  - **Pairing with hexa-bio code**: matches `weave_pi_p2_verifier_v3_exhaustive.py`
    (cycle-25 NP-solver upgrade) — termination bound `n` should be
    machine-extractable for cross-check against the v2/v3 50/50 agreement
    sweep recorded under GATE-26-3.

### §2.4 F-CL-FORMAL-4 — closure-cert idempotence (already PARTIAL)

Out of scope for v0 scaffold (theorem stub already present upstream per
`.roadmap.weave` F-CL-FORMAL-4 PARTIAL row). Listed here only for
completeness; promotes to scaffold v1 when canonical names lock in.

```lean4
-- existing PARTIAL stub, name TBD-canonical
theorem closure_cert_idempotent : ∀ c, discloseTwice c = discloseOnce c := sorry
```

## §3 Witness schema — raw_77_lean4_proof_witness_v0

Canonical JSON Schema co-located at
`weave/spec/lean4_proof_witness_v0.schema.json`. One row emitted per
(axis, theorem) pair when canonical reports a proof-state change.

Required fields (see schema for full constraints):

  - `schema`           — const `"raw_77_lean4_proof_witness_v0"`
  - `axis`             — enum `"F-CL-FORMAL-1" | "F-CL-FORMAL-2" | "F-CL-FORMAL-3" | "F-CL-FORMAL-4"`
  - `theorem_name`     — string, lean4 declaration name (e.g. `sigma_lattice_card`)
  - `module_path`      — string, lean4 module path (e.g. `N6.InvariantLattice.SigmaLatticeCard`)
  - `sorry_count`      — integer ≥ 0 (PASS = 0)
  - `last_modified_cycle` — integer ≥ 0 (cycle index of last canonical edit)
  - `canonical_repo_ref` — string, points into upstream
                          (e.g. `n6-architecture@<sha>:domains/biology/...`)
  - `pass`             — boolean, `true` iff `sorry_count == 0`
  - `recorded_at`      — RFC3339 timestamp on hexa-bio side

Emitted into `state/discovery_absorption/registry.jsonl` (R4 witness
protocol).

## §4 Cross-repo blockers (PENDING — outside hexa-bio)

Until the following land in `~/core/n6-architecture/` they are out of scope
for hexa-bio:

  1. Canonical `Strategy`, `LandauerPass`, `compose`, `heatConsumed`,
     `StrandCatalogue`, `Pi_p_2_Query`, `verifierSteps`, `sigma`
     definitions in lean4 (the scaffold's free symbols).
  2. Concrete proof bodies replacing each `sorry` in §2.1–§2.3.
  3. Module-path lock-in (this scaffold's `module_path` strings are
     proposals; canonical may rename, in which case hexa-bio updates the
     witness schema constant set in a v1 promotion).
  4. lake / Mathlib version pin recorded upstream (consumer can then pin
     by SHA in the witness `canonical_repo_ref`).

When (1)-(4) land, hexa-bio promotes:

  - `.roadmap.weave` F-CL-FORMAL-1/2/3 from `DEFERRED — canonical work
    pending; in-repo scaffold spec landed at
    weave/spec/lean4_mechanical_layer_v0.scaffold.md` to either PASS (if
    sorry-count==0) or REGRESSION-WATCH (if sorry-count>0, i.e. proof
    started but unfinished).
  - this scaffold v0 → v1 (lock canonical theorem names + module paths).

## §5 Non-goals

  - No lean4 source files (`.lean`) in this repo. Forbidden by R1 (canonical
    SSOT immutability) + cross-repo memory rule.
  - No proof obligation here. Hexa-bio is consumer; proof construction is
    canonical-repo session.
  - No CI hook in v0. Once canonical lands, a follow-up cycle wires
    `selftest/lean4_witness_audit.py` (TODO-cycle-26+) that ingests
    canonical-reported proof states and emits the `raw_77_lean4_proof_witness_v0`
    rows.

## §6 References

  - `.roadmap.weave` §Falsifier preregister F-CL-FORMAL-1..4
  - `.roadmap.hexa_bio` §G GATE-26-2 · §B C0h · §A.1 invariant lattice
  - `memory/feedback_cross_repo_canonical.md` — cross-repo edit rule
  - `weave/spec/lean4_proof_witness_v0.schema.json` — witness schema
  - `docs/n6/hexa-weave.md` (symlink → `n6-architecture` canonical)
