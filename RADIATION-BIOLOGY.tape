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
# RADIATION-BIOLOGY.tape — architecture-current (editable per v1.2)
# Event history → RADIATION-BIOLOGY.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "radiation-biology" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · radiation biology substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "RADIATION-BIOLOGY.log.tape"

@D b_6_dsb_repair_pathways_molecular_0 :: radiation-biology [ok]
  text = "**6 DSB-repair pathways** — molecular-biology primitive."


@D b_6_radiation_interaction_mechanis_1 :: radiation-biology [ok]
  text = "**6 radiation interaction mechanisms** — radiation-physics primitive."


@D b_6_gy_ld50_empirical_radiobiology_2 :: radiation-biology [ok]
  text = "**6 Gy LD50** — empirical radiobiology constant."

# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 SOURCES ─────────────────────────────────────────



@D b_icrp_publication_60_ld50_0 :: radiation-biology [ok]
  text = "ICRP Publication 60 (LD50)."


@D b_friedberg_dna_repair_and_mutagen_1 :: radiation-biology [ok]
  text = "Friedberg, *DNA Repair and Mutagenesis* (repair pathway taxonomy)."


@D b_attix_introduction_to_radiologic_2 :: radiation-biology [ok]
  text = "Attix, *Introduction to Radiological Physics* (interaction mechanisms)."

# ── §5 STATUS ─────────────────────────────────────────



