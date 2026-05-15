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
# Urban Farming (HEXA-URBFARM) — n=6 Hoagland 6 macronutrients
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "urban-farming" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · urban-farming substrate"
  brief = "Hoagland 6 macronutrients · 6 vertical-farm tiers · 6-band grow-LED spectrum"
  parent = "dancinlab/hexa-bio"

# ── §1 WHY ─────────────────────────────────────────


# ── §2 n=6 CONNECTION ─────────────────────────────────────────


@D b_6_macronutrients_verified_bioche_0 :: urban-farming [ok]
  text = "**6 macronutrients** (verified biochemistry — plants *require* all six)."

@D b_6_vertical_farm_functional_tiers_1 :: urban-farming [ok]
  text = "**6 vertical-farm functional tiers** (industry-standard layout)."

@D b_6_band_grow_led_spectrum_2 :: urban-farming [ok]
  text = "**6-band grow-LED spectrum**."

# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 SOURCES ─────────────────────────────────────────


@D b_hoagland_arnon_1950_the_water_cu_0 :: urban-farming [ok]
  text = "Hoagland & Arnon 1950, *The Water-Culture Method*."

@D b_kozai_et_al_plant_factory_an_ind_1 :: urban-farming [ok]
  text = "Kozai et al., *Plant Factory: An Indoor Vertical Farming System*."

# ── §5 STATUS ─────────────────────────────────────────

