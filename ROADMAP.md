# hexa-bio ROADMAP

> Live tracker for the **4-verb molecular toolkit** (WEAVE / NANOBOT /
> RIBOZYME / VIROCAPSID). Canonical verb specs live in
> `n6-architecture/domains/biology/` and are linked from
> [`docs/n6/`](./docs/n6/) — this roadmap is the empirical companion's
> rolling status.

**Last sync**: 2026-05-05 · **Current release**: v1.0.0 · **Branch**: `main`

---

## §A META — cross-cutting state

### A.1 Invariant lattice (n=6)

The 4 verbs share one master identity:

```
σ(6) · φ(6) = n · τ(6) = J₂ = 24
   12   ·   2  =  6  ·   4  = 24
```

| Symbol | Value | Role | Verb projection |
|--------|-------|------|-----------------|
| σ(6)   | 12    | sigma — cardinality bin | 12 vertices / 12 raw-strategies / 12-nt catalytic core / 12 pentameric vertices |
| τ(6)   | 4     | tau — state quartet | 4 axes / 4 motor states / 4 reaction states / 4 assembly states |
| φ(6)   | 2     | phi — verdict bit | hydrophobic/-philic, open/closed, cleaved/intact, free/assembled |
| J₂     | 24    | Mathieu / Leech symmetry | M₂₄ · O ⊂ I octahedral subgroup |

### A.2 Release cadence

| Version | Date         | Status     | Wired verbs    | Highlights |
|---------|--------------|------------|----------------|------------|
| v1.0.0  | 2026-05-04   | RELEASED   | 1 / 4 (WEAVE)  | Standalone Molecular Toolkit; T=1 cage MVP + Bayesian audit posterior 0.9668 RESOLVED |
| v1.1.0  | _planned 07-28_ | TARGET    | 4 / 4 stubs → numerical | post-MVP-gate consolidation (see A.4) |
| v2.0.0  | TBD          | ASPIRATIONAL | 4 / 4 empirical | Bayesian audits (A.5) closed across all 4 verbs |

### A.3 Tetrahedron closure (cycle 7 → 24)

```
                  ┌──────────────┐
                  │   WEAVE      │  composition  (Landauer × NP-search ceiling)
                  │  cycle 7→24  │
                  └──────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
   ┌──────▼─────┐ ┌──────▼─────┐ ┌─────▼──────┐
   │  NANOBOT   │ │ RIBOZYME   │ │ VIROCAPSID │
   │  cycle 13  │ │ cycle 15   │ │ cycle 19   │  σ=12 STRUCTURAL-EXACT
   │ actuation  │ │ catalysis  │ │  assembly  │
   │ Brownian   │ │ diffusion  │ │ Caspar-Klug│
   │   floor    │ │   ceiling  │ │  T-number  │
   └────────────┘ └────────────┘ └────────────┘
```

- **Tetrahedron closed** at cycle 22 (2026-05-01) — 4 orthogonal genus axes:
  composition (covalent) · actuation (mechanical) · catalysis (chemical) ·
  assembly (thermodynamic).
- **Alien-grade**: 4.78 (cycle 22 close).
- **Tri-axis Ω-saturation** (FORMAL Π¹₁-CA₀ · PHYSICAL Landauer ·
  COMPUTATIONAL Π^p_2): PASS at workload ceiling (7/8 raw-70 axes PASS,
  CHI2 DEFER).
- **σ(6)=12 STRUCTURAL-EXACT** confirmed only on **VIROCAPSID** (Caspar-Klug
  T=1 12 vertices, log Bayes factor 3.37 decisive on n=34 corpus); others
  are STRUCTURAL-APPROXIMATE.

### A.4 90-day MVP gates — `2026-07-28` (T-83 days as of 2026-05-05)

All 4 verbs must deliver a numerical MVP simulation by this date or revert
from APPROACH grade to PROPOSED.

| Verb        | Falsifier   | MVP deliverable                                                    | Status   |
|-------------|-------------|--------------------------------------------------------------------|----------|
| WEAVE       | F-TP5-b     | end-to-end run with P≥10, N≥50                                    | OPEN     |
| NANOBOT     | F-NB-4      | 4-state 12-vertex DNA-origami simulation                          | OPEN     |
| RIBOZYME    | F-RB-4      | hammerhead-minimal 12-nt-core 4-state chemical-kinetics simulation | OPEN     |
| VIROCAPSID  | F-VIROCAPSID-3 | T=1 minimal 60-subunit 4-state Zlotnick-class kinetic simulation | PARTIAL — cage MVP yield 0.68 plateau (cycle 22; calibration gap not refutation) |

### A.5 Sister-axis collision audit — `2026-05-28` (T-23 days)

| Verb        | Falsifier              | Collision target                                |
|-------------|------------------------|-------------------------------------------------|
| NANOBOT     | F-NB-5                 | `life/therapeutic-nanobot/`                     |
| RIBOZYME    | F-RB-5                 | `life/crispr-gene-editing/`, `life/synbio/`     |
| VIROCAPSID  | F-VIROCAPSID-COLLISION | `life/virology/`, `life/vaccine/`               |

### A.6 Bayesian audit deadlines — `2026-09-28` (T-146 days)

n=30 corpus Bayesian model comparison (log Bayes factor ≥ 3 to reject H0
random):

- F-NB-2 (NANOBOT n6 invariant calibration)
- F-RB-2 (RIBOZYME catalytic-core 12-nt calibration)
- F-VIROCAPSID-2 — **RESOLVED cycle 22** (posterior 0.9668 on n=34 corpus,
  log Bayes factor 3.37)

### A.7 Empirical SSOT

- WEAVE numerical sandbox (cage assembly + Caspar-Klug Bayesian audit) →
  `~/core/nexus/sim_bridge/weave/` (canonical cycle 24+).
- This repo (`hexa-bio`) hosts: CLI verbs, examples, selftest, tests,
  module Python bridges. Spec text → `docs/n6/` (symlink to
  n6-architecture canonical).

---

## §B DOMAIN — per-verb roadmap

### B.1 🧶 WEAVE — composition (1/4 wired)

**Tagline**: write-side multi-strand molecular design composition. AlphaFold
3 / IsoDDE read-side counterpart.

| Status (cycle 8 actual)            | 90-day MVP target (07-28)      | Stretch |
|------------------------------------|--------------------------------|---------|
| P=0 (no empirical run)             | P=10 proteome subset           | P=100   |
| 12 falsifiers (9 closure + 3 new)  | 12                             | 20      |
| Raw-70 axes PASS 8/9               | 9/9 with empirical anchor      | 9/9 n>1 |
| **lean4 sorry count = 0** (W5)     | 0                              | 0       |
| F-D-3 deadline-miss prob 50-58%    | < 40 % (W7-W9 burndown)        | < 25 %  |
| CHI2 sample size n=1 DEFER         | 5 PASS                         | 30      |

**Open work**:
- W7-W9 mechanical-layer burndown (sorry-free already; reduce F-D-3 risk).
- First end-to-end MVP run with P≥10, N≥50 → kills F-TP5-b by 2026-07-28.
- CHI2 axis lift from DEFER to PASS (need ≥1 published cellular heat-budget
  comparison sample).
- One Zenodo deposit gated on user approval (Option-E paper exists).

**Falsifier preregister** (9 across 3 measurable claims):
- F-TP5-b · F-TP5-c · F-TP5-d (90-day MVP gate)
- F-CL-FORMAL-* (formal-axis claims)
- F-W5-AX2-1 RESOLVED · F-MANUAL-LOGIN active · F-CL-FORMAL-4 PARTIAL

**Why it's ahead of the others**: only verb with mechanical layer (lean4),
empirical SSOT migration, and one external paper draft.

---

### B.2 🤖 NANOBOT — actuation (stub)

**Tagline**: single molecular nano-machine actuation architecture. DNA-origami
peer.

| Status (cycle 13 fan-out 2/5)      | 90-day MVP target (07-28)      | Stretch |
|------------------------------------|--------------------------------|---------|
| 5 falsifiers (F-NB-1..F-NB-5)      | 5                              | 12      |
| Raw-70 axes PASS 7/8 (CHI2 DEFER)  | 8/8                            | 8/8 n>1 |
| CHI2 sample size n=0               | 1 (PASS-MARGINAL)              | 30      |
| No simulation yet                  | 4-state 12-vertex DNA-origami  | —       |

**Open work**:
- Build 4-state 12-vertex DNA-origami simulation (truncated icosahedron /
  cuboctahedron skeleton) → kills F-NB-4 by 2026-07-28.
- Sister-axis collision audit vs `life/therapeutic-nanobot/` → kills F-NB-5
  by 2026-05-28.
- Bayesian model comparison on 30 published nano-machine architectures →
  kills F-NB-2 by 2026-09-28.

**Falsifier preregister** (15 across 5 measurable claims):
- Genus distinction: F-NB-1-genus / F-NB-1-b / F-NB-1-c
- n6 invariant binding: F-NB-2-n6-decorative / F-NB-2-b / F-NB-2-c
- 90-day MVP gate: F-NB-4-MVP-90day / F-NB-4-b / F-NB-4-c
- Sister-axis collision: F-NB-5-sister-axis-collision / F-NB-5-b / F-NB-5-c
- Brownian floor: F-NB-3-Brownian-floor / F-NB-3-b / F-NB-3-c

---

### B.3 ✂️ RIBOZYME — catalysis (stub)

**Tagline**: catalytic-RNA architecture. Hammerhead / HDV / hairpin /
ribosome PTC peer.

| Status (cycle 15 fan-out 3/3)      | 90-day MVP target (07-28)      | Stretch |
|------------------------------------|--------------------------------|---------|
| 5 falsifiers (F-RB-1..F-RB-5)      | 5                              | 12      |
| Raw-70 axes PASS 7/8 (CHI2 DEFER)  | 8/8                            | 8/8 n>1 |
| CHI2 sample size n=0               | 1 (PASS-MARGINAL)              | 30      |
| σ(6)=12 STRUCTURAL-APPROXIMATE     | hammerhead 12-nt simulation    | —       |

**Open work**:
- Build hammerhead-minimal 12-nt-core 4-state chemical-kinetics simulation
  (k_cat / K_M ≤ 10⁹ M⁻¹ s⁻¹ Eigen-Hammes ceiling) → kills F-RB-4 by
  2026-07-28.
- Sister-axis collision audit vs `life/crispr-gene-editing/` and
  `life/synbio/` → kills F-RB-5 by 2026-05-28.
- Bayesian audit on 30 published ribozyme architectures (catalytic-core size
  10–15 nt) → kills F-RB-2 by 2026-09-28.

**Falsifier preregister** (15 across 5 measurable claims):
- Genus distinction (vs WEAVE / NANOBOT): F-RB-1-genus / F-RB-1-b / F-RB-1-c
- n6 invariant binding: F-RB-2-n6-decorative / F-RB-2-b / F-RB-2-c
- 90-day MVP gate: F-RB-4-MVP-90day / F-RB-4-b / F-RB-4-c
- Sister-axis collision: F-RB-5-sister-axis-collision / F-RB-5-b / F-RB-5-c
- Diffusion limit: F-RB-3-diffusion-limit / F-RB-3-b / F-RB-3-c

---

### B.4 🦠 VIROCAPSID — assembly (stub, σ=12 STRUCTURAL-EXACT)

**Tagline**: icosahedral protein cage self-assembly. T=1 60-subunit cage,
vaccine VLP, drug capsule, nano-cage.

| Status (cycle 19 fan-out 4/4)      | 90-day MVP target (07-28)      | Stretch |
|------------------------------------|--------------------------------|---------|
| 16 falsifiers (5 measurable claims)| 16+                            | —       |
| Raw-70 axes PASS 7/8 (CHI2 DEFER)  | 8/8                            | 8/8 n>1 |
| CHI2 sample size n=0               | 1 (PASS-MARGINAL)              | 30      |
| F-VIROCAPSID-2 RESOLVED cycle 22   | (already closed)               | —       |
| Cage MVP yield 0.68 plateau        | aberrant-aggregate < closed-shell | quantitative margin |

**Open work**:
- Calibrate cage MVP nucleation-elongation rate constants to lift yield
  off 0.68 plateau → resolves F-VIROCAPSID-3 calibration gap by
  2026-07-28.
- Sister-axis collision audit vs `life/virology/` and `life/vaccine/` →
  kills F-VIROCAPSID-COLLISION by 2026-05-28.
- Multi-T-number corpus extension (T=1 / T=3 / T=4 / T=7 / T=13 / T=21)
  beyond the cycle-22 textbook n=34 — Bayesian audit further calibration
  by 2026-09-28.

**Falsifier preregister** (16 across 5 measurable claims):
- Genus distinction (vs three sisters): F-VIROCAPSID-1-genus / -1-b / -1-c / -1-d
- n6 invariant binding: F-VIROCAPSID-2-n6-decorative / -2-b / -2-c (RESOLVED cycle 22)
- 90-day MVP gate: F-VIROCAPSID-3-MVP-90day / -3-b / -3-c
- Sister-axis collision: F-VIROCAPSID-COLLISION + sub-clauses
- Kinetic trap: F-VIROCAPSID-4-kinetic-trap / -4-b / -4-c

**Why σ=12 STRUCTURAL-EXACT here**: Caspar-Klug 1962 + Euler V−E+F=2 forces
T=1 → 12 pentameric vertices exactly; Bayesian audit posterior 0.9668 ≥ 0.95
(log Bayes factor 3.37 decisive per Jeffreys 1961) on n=34 textbook corpus.

---

## §C SHORT-HORIZON CHECKLIST

| Date         | T-days | What                                              |
|--------------|--------|---------------------------------------------------|
| 2026-05-28   | 23     | F-NB-5 / F-RB-5 / F-VIROCAPSID-COLLISION audits   |
| 2026-07-28   | 83     | F-TP5-b / F-NB-4 / F-RB-4 / F-VIROCAPSID-3 MVPs   |
| 2026-09-28   | 146    | F-NB-2 / F-RB-2 Bayesian audits (n=30 corpora)    |

---

## §D POINTERS

- Canonical specs: [`docs/n6/`](./docs/n6/) (symlinks to n6-architecture)
- Empirical SSOT: `~/core/nexus/sim_bridge/weave/`
- Release notes: [`RELEASE_NOTES_v1.0.0.md`](./RELEASE_NOTES_v1.0.0.md)
- Changelog: [`CHANGELOG.md`](./CHANGELOG.md)
- Cross-axis applied bet (out of scope but tracked): SA #2
  `crispr-cas13-poc-diagnostic/` (2026-05-01, alien-grade 10
  PHYSICAL-LIMIT, F-CAS13-MVP-1..5)
