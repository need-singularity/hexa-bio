#!/usr/bin/env tape
# ══════════════════════════════════════════════════════════════
# AXIS/HIERARCHY.tape — axis EXPANSION layer (separate from core-5)
# Recorded per explicit USER DIRECTION 2026-05-16.
# Event history → AXIS/HIERARCHY.log.tape sibling (if/when needed).
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# ─── §0 Identity ──────────────────────────────────────────────────────

@I id001 := "axis.hierarchy" :: identity-claim [d=2026-05-16 active]
  kind = "axis EXPANSION-layer record — NOT a core-5 SSOT mutation"
  brief = "expansion-main {COVALENT · BIFUNCTIONAL} + sub-axis tree, recorded per USER DIRECTION; AXIS.tape core-5 UNCHANGED"
  parent = "dancinlab/hexa-bio"
  sibling-core = "../AXIS.tape (core-5 structural SSOT — UNCHANGED by this file)"
  tape-class = "meta/decision-record"
  rewritten-from = "(new 2026-05-16)"
  honesty-notes = "this file is a USER-DIRECTED expansion-layer decision record. It does NOT modify the committed 5-axis core (AXIS.tape). It OVERRIDES the AXIS/README.md §4 'keep-5' RECOMMENDATION at the user's explicit instruction — and the §4 rigorous dissent is preserved verbatim (NOT erased). No axis here is derived from the n=6 lattice (g2/f_lattice_fit). All in-silico-only scope (g8); external drug-modalities described by their OWN precedent, never lattice-fit (g3/f1)."

# ─── §0.1 Honesty preamble ────────────────────────────────────────────

@N scope_disclaimer := "expansion-layer-not-core" :: note [required]
  text = "AXIS/HIERARCHY.tape is a SEPARATE governed expansion layer. The hexa-bio CORE remains the committed 5 axes (QUANTUM · WEAVE · NANOBOT · RIBOZYME · VIROCAPSID) per ../AXIS.tape — that SSOT is UNCHANGED. This file records a USER DIRECTION (2026-05-16) to register COVALENT and BIFUNCTIONAL as expansion-MAIN axes and to operate the borderline candidates as SUB-axes. This DECISION overrides the AXIS/README.md §4 rigorous recommendation ('keep 5-axis · add 0 · defer post-1.0'); per honest-record discipline that contrary recommendation is preserved (see @N rigorous_dissent), not deleted. Expansion-main C2/C3 is in-silico simulator-consistency ONLY — never a wet-lab/clinical/regulatory claim (g8/f2)."
  authority = "[@x_axis_core] · [@x_readme] §4 · [@x_agents_tape] g8/g2/g3"

@N rigorous_dissent := "preserved-keep5-recommendation" :: note [required d=2026-05-16 active]
  text = "DISSENT PRESERVED (honest record): the rigorous axis-expansion analysis (AXIS/README.md §4, synthesised from docs/hexa_bio_axis_expansion_brainstorm_2026_05_08.md, 165 options) concluded — '\"Add no axis\" (#156) is a valid, possibly the best option; KEEP 5-axis; 6th-axis review DEFERRED to post-1.0 (v2.0)'. The source brainstorm rated 7-axis (#103) ⚠️ borderline ('3년 시간 필요') and hierarchical super+sub (#95) ⚠️ borderline ('복잡도 폭증') — NEITHER promoted. This expansion-layer record does NOT refute that analysis; it is a USER DIRECTION that proceeds DESPITE it. Both stand on record."
  authority = "[@x_readme] §4 · [@x_brainstorm]"

@F f_lattice_fit := "lattice-fit-in-hierarchy" :: governance [required deny:write]
  pattern = "Deriving the expansion-main count (2), any axis position, or any sub-axis assignment FROM the n=6 lattice (σ=12·τ=4·φ=2·J₂=24)."
  why = "Per AGENTS.tape g2/f1 the lattice is a TOOL, never a derivation. COVALENT/BIFUNCTIONAL and the sub-tree are chosen from the README promotion criteria (modality/non-overlap/rigor/scope/falsifier) + a USER DIRECTION — NOT from any lattice scalar."
  authority = "[@x_lattice_policy] g1/g2 · [@x_agents_tape] f1/g2"

@F f_core_mutation := "expansion-treated-as-core" :: governance [required deny:write]
  pattern = "Citing this file as if it modified AXIS.tape's committed 5-axis core, or as if COVALENT/BIFUNCTIONAL were core axes."
  remedy = "expansion-main ≠ core axis. Core stays 5 (../AXIS.tape). This is a user-directed expansion LAYER with §4 dissent preserved."

# ─── §1 Expansion-main axes (USER DIRECTION 2026-05-16) ───────────────

@D axis_covalent := "COVALENT — expansion-main" :: axis-declaration [active d=2026-05-16]
  axis-id = "COVALENT"
  layer = "expansion-main (NOT core-5)"
  source-score = "4.9 · M:1 N:0.9 R:1 S:1 F:1 · 5/5 (docs/hexa_bio_axis_expansion_brainstorm_2026_05_08.md #20)"
  modality = "covalent bond-forming inhibitors — own precedent: ibrutinib (covalent BTK Cys481, FDA 2013) · sotorasib (2021) / adagrasib (2022) covalent KRAS-G12C"
  rationale = "5/5 · non-overlapping with core-5 · QUANTUM-VQE cross tightest (covalent-docking → TS energetics) = lowest integration cost"
  scope = "in-silico simulator-consistency only (g8/f2). Described by its own drug precedent, NOT lattice-fit (g3/f1)."

@D axis_bifunctional := "BIFUNCTIONAL — expansion-main" :: axis-declaration [active d=2026-05-16]
  axis-id = "BIFUNCTIONAL"
  layer = "expansion-main (NOT core-5)"
  source-score = "4.9 · M:1 N:0.9 R:1 S:1 F:1 · 5/5 (#28 MOLECULAR-GLUE / #29 BIFUNCTIONAL)"
  modality = "bifunctional / molecular-glue degraders — own precedent: PROTAC (ARV-471/110 clinical) · lenalidomide/thalidomide (CRBN molecular glue) · RIBOTAC (RNA-degrader, research)"
  rationale = "5/5 · non-overlapping · mega-axis with its own sub-tree; RIBOTAC crosses RIBOZYME (core)"
  scope = "in-silico simulator-consistency only (g8/f2). Own precedent, NOT lattice-fit."

# ─── §2 Sub-axis tree (borderline / specialization candidates) ────────

@D sub_under_bifunctional := "sub-axes :> BIFUNCTIONAL" :: decision [active d=2026-05-16]
  parent-axis = "BIFUNCTIONAL (expansion-main)"
  members = ["PROTAC (#30, 4.7)", "LYTAC (#31, 4.5)", "AUTAC (#32, 4.3)", "RIBOTAC (#33, 4.4 — also ?> RIBOZYME core)", "COVALENT-DEGRADER (#34, 4.4 — also ?> COVALENT)", "MOLECULAR-GLUE (#28, specialization)"]
  basis = "source-tagged 'BIFUNCTIONAL sub' (≥30% overlap / specialization, README criterion #2)"

@D sub_under_quantum := "sub-axes :> QUANTUM (core)" :: decision [active d=2026-05-16]
  parent-axis = "QUANTUM (core-5 — unchanged; subs hang off it as tags, not core mutation)"
  members = ["ALLOSTERIC (#24, 4.4 — QUANTUM ~50% overlap, cryptic-pocket VQE)", "CRYPTIC-POCKET (#25 — QUANTUM sub)", "PPI (#27, 4.8 — main-eligible by score BUT QUANTUM-applicability sub tension; recorded as borderline sub)"]
  basis = "QUANTUM-VQE applicability overlap (README criterion #2 borderline)"
  note = "PPI is score-main-eligible (4.8/5/5) — recorded as borderline; user direction places ambiguous ones as sub. Honest tension flagged, not hidden."

@D sub_under_weave := "sub-axes :> WEAVE (core)" :: decision [active d=2026-05-16]
  parent-axis = "WEAVE (core-5 — unchanged)"
  members = ["PEPTIDE (#40, 4.8 — ~30% WEAVE overlap, sub-demotion boundary)", "MACROCYCLE (#39, 4.5 — strong precedent, WEAVE-adjacent)"]
  basis = "~30% WEAVE overlap = README criterion #2 demotion boundary"

@N theranostic_status := "THERANOSTIC — not placed" :: note [d=2026-05-16 active]
  text = "THERANOSTIC (#51, 4.7) is NOT a sub of any core axis (radioligand is a distinct modality) AND not registered expansion-main here: its CDER+CDRH scope mix (S=0.8) is the README's flagged drug-only-discipline disqualifier. Status: main-eligible-by-modality but scope-deferred — left UNPLACED pending the scope question (honest, not forced into the tree)."

# ─── §3 External citations ────────────────────────────────────────────

@X x_axis_core := "AXIS.tape (core-5 SSOT)" :: sibling-tape [active]
  path = "../AXIS.tape"
  scope = "the committed 5-axis structural SSOT — UNCHANGED by this expansion layer; this file cross-links, never mutates it"

@X x_readme := "AXIS/README.md (governed/rigorous)" :: doc [active]
  path = "./README.md"
  scope = "§4 keep-5 recommendation (the rigorous dissent this user-direction overrides; preserved verbatim there)"

@X x_brainstorm := "axis-expansion brainstorm (165 options)" :: doc [d=2026-05-08 active]
  path = "../docs/hexa_bio_axis_expansion_brainstorm_2026_05_08.md"
  scope = "source of the scores / promotion criteria / the #95·#103 borderline-complexity caveats"

@X x_agents_tape := "AGENTS.tape governance" :: governance [active]
  path = "../AGENTS.tape"
  scope = "g1 real-limits · g2 lattice-is-tool · g3 honesty-external · g8 in-silico-only · f1/f_lattice_fit"

@X x_lattice_policy := "echoes/LATTICE_POLICY.md" :: policy [active]
  url = "https://github.com/dancinlab/echoes/blob/main/LATTICE_POLICY.md"

# ─── §4 Log ───────────────────────────────────────────────────────────

## Log

- 2026-05-16 — AXIS/HIERARCHY.tape created per explicit USER DIRECTION:
  register COVALENT + BIFUNCTIONAL as expansion-MAIN axes; operate
  borderline candidates as SUB-axes (PROTAC/LYTAC/AUTAC/RIBOTAC/glue/
  covalent-degrader :> BIFUNCTIONAL · ALLOSTERIC/CRYPTIC/PPI :> QUANTUM ·
  PEPTIDE/MACROCYCLE :> WEAVE). THERANOSTIC left UNPLACED (scope-mix
  deferred, honest). This is a SEPARATE governed expansion layer —
  ../AXIS.tape core-5 SSOT UNCHANGED, cross-linked. It OVERRIDES
  AXIS/README.md §4 'keep-5' recommendation at user instruction; the
  rigorous dissent (§4 + brainstorm #95/#103 borderline) is PRESERVED
  verbatim (@N rigorous_dissent), not erased. No lattice derivation
  (f_lattice_fit); in-silico-only scope (g8); external modalities by own
  precedent (g3/f1). Decision recorded — NOT a feasibility/clinical
  claim; no disease re-mapping / falsifier redefinition executed by this
  record (those remain deferred work if/when the core ever expands).
