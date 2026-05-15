#!/usr/bin/env tape
# ══════════════════════════════════════════════════════════════════════
# .tape v1.2 — grammar primer (cold-read by any LLM / agent / human)
# ══════════════════════════════════════════════════════════════════════
# Form: each entry is `@<type> <id> := "<subject>" :: <kind> [<grades>]`
#       optionally followed by body lines (2-space indent) — key=value,
#       edges (<- -> => …), or quoted prose.
#
# ENTRY TYPES (17):
#   Runtime (10): @S session  @U user  @A assistant  @T tool-call  @R result
#                 @H hook  @D decision  @K cost  @P provider  @? anomaly
#   Foundation:   @I identity-claim
#   Declarative:  @X external-citation  @F forbidden-pattern  @N note
#                 @C config  @L layout  @V spec-version
#
# EDGES (12, on body lines, 2-space indent):
#   Causal:     <- caused-by   -> triggers   == continues
#               ~> supersedes  !! aborts     |> verified-by
#   Effect:     => produces (followed by quoted natural-language)
#   Structural: <: specializes  :> generalizes  ?> soft-depends
#               !> conflicts-with  @> projects-to (e.g. @> AGENTS.md)
#
# GRADE TAGS (in [...] on entry header):
#   Delivery:   ok · err · denied · cancelled · partial · superseded
#   Governance: required · recommended · optional · draft · active · deprecated
#   Scoped:     allow:<x> · deny:<x>
#   Time/index: T<n> (turn)  N<n> (wall-sec)  d=<YYYY-MM-DD>
#
# PAYLOAD SYNTAX (body lines):
#   key = "value"           single-line string
#   key = [a, b, c]         array literal
#   key <<~EOF              heredoc (multi-line; ends with EOF on own line)
#     multi-line text
#   EOF
#   "see [@x1] §3"          inline citation by entry id
#   `cmd or path`           backtick code-span (inline only)
#
# Full spec: ~/core/tape/spec/tape.md (or github.com/dancinlab/tape)
# ══════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# XENO.log.tape — append-only event history (v1.2 split)
# Sibling: XENO.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A rewrite_real_science := "XENO.tape rewritten from lattice-tautology stub to real-science SSOT" :: rewrite [ok d=2026-05-16]
  origin = "XENO.tape was a lattice-tautology stub (hexa-bio mass-split 153b5a2): fragmented @D rows with truncated text, no citations, no real science, no @F lattice-fit guard, no @N honest-stance entry, no @X literature entries. It recorded substrate names (Akida/Loihi3/IonQ/etc.) but zero scientific grounding."
  action = "Full real-science rewrite 2026-05-16. Preserved: top grammar primer, banner, @V :: spec, @I id001 id/parent/sibling-log. Replaced everything from @I body onward."
  added = "NEW §0 @I id001 with honest brief + scope + rewritten-from provenance. NEW @N scope_disclaimer (required). NEW §1 neuromorphic foundations: Mead 1990 concept coining; SpiNNaker (Furber 2014); TrueNorth (Merolla/Science 2014); Loihi/Loihi2 (Davies/IEEE Micro 2018); BrainChip Akida (industry-era, author/era); event-driven sparsity mechanism. NEW §2 quantum hardware: NISQ paradigm (Preskill 2018); superconducting qubits (Arute/Nature 2019 — with explicit contested-quantum-supremacy flag); IonQ trapped-ion (industry-era); classical-quantum crossover honesty. NEW §3 QRNG: photon-based QRNG; device-independent certified randomness (Bierhorst/Nature 2018). NEW §4 organoid intelligence: OI concept (Smirnova et al./Front Sci 2023); DishBrain Pong (Kagan et al./Neuron 2022); ethics hard wall (sentience uncertainty); FinalSpark (industry-era). NEW §5 substrate trade-off matrix (5-dimension qualitative cross-substrate comparison). NEW §6 hexa-bio integration model (CLI gate pattern, no shadow, axes-map). NEW §7 real-limits: lim_decoherence (Preskill 2018 NISQ ceiling); lim_neuro_tooling (toolchain immaturity); lim_organoid_ethics (ethics/sentience hard wall, Smirnova 2023); lim_supply_access (hardware access constraints); lim_in_silico_boundary (epistemic in-silico ceiling). NEW §8 @F f_lattice_fit + @N n6_honest_stance (both required). NEW §9 3 @D tp_* :: prediction with falsifiers. NEW §10 cross-links (governance, compute-portfolio, qmirror, xeno, HEXA-NANOBOT, closure-backlog). NEW §11 9 @X :: literature entries: Mead 1990; Furber 2014 (Proc IEEE); Merolla 2014 (Science); Davies 2018 (IEEE Micro); Arute 2019 (Nature, contested flag); Preskill 2018 (Quantum); Bierhorst 2018 (Nature); Smirnova 2023 (Front Sci); Kagan 2022 (Neuron). Author/era-flagged: BrainChip Akida (industry-era); IonQ (industry-era); FinalSpark (industry-era)."
  n6-stance = "Declined as derivation tool. @F f_lattice_fit + @N n6_honest_stance state plainly: chip-architecture parameters (Loihi 128 cores, TrueNorth 4096 cores, IonQ chain length) are engineering/physics choices documented in the cited literature — not derivable from the n=6 lattice. Numerical coincidences are OBSERVATION ONLY, never derivation."
  honesty-caveats = "Google quantum-supremacy claim (Arute 2019) explicitly flagged as CONTESTED in @X x_arute_2019 and @D quant_superconducting — both the original result and classical-challenge papers are cited; no resolution claimed. Organoid intelligence (Smirnova 2023 / Kagan 2022) framed as early-stage with unresolved ethics (sentience uncertainty). BrainChip Akida, IonQ, FinalSpark cited at industry-era / author-era level — no precise datasheet specs asserted. No fabricated citations."
  lint = "python3 selftest/tape_lattice_honesty_lint.py XENO.tape --json → __TAPE_LATTICE_HONESTY__ PASS (has_guard=true, has_stance=true, grounded=true)"
  governance = "Complies with hexa-bio AGENTS.tape g1 real-limits-first · g2 lattice-is-tool · g5 sister-repo-CLI-not-wrap · g6 gates-not-reverifications · g7 SKIP-is-honest · g8 in-silico-only · f1 lattice-fit-forbidden · f3 no-shadow-impl. No shadow implementation of xeno/qmirror logic added."
