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
# SLEEP-MEDICINE.tape — architecture-current (editable per v1.2)
# Event history → SLEEP-MEDICINE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "sleep-medicine" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · sleep medicine substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "SLEEP-MEDICINE.log.tape"

@D b_aasm_6_stage_staging_the_clinica_0 :: sleep-medicine [ok]
  text = "**AASM 6-stage staging** — the clinical diagnostic primitive."


@D b_6_sleep_cycles_per_full_night_90_1 :: sleep-medicine [ok]
  text = "**~6 sleep cycles per full night** (~90 min per cycle)."


@D b_psg_12_channel_eeg_6_12_2 :: sleep-medicine [ok]
  text = "**PSG 12-channel EEG** = σ(6) = 12."

# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 SOURCES ─────────────────────────────────────────



@D b_aasm_sleep_staging_manual_latest_0 :: sleep-medicine [ok]
  text = "AASM Sleep Staging Manual (latest revision)."


@D b_buysse_et_al_1989_pittsburgh_sle_1 :: sleep-medicine [ok]
  text = "Buysse et al. 1989, *Pittsburgh Sleep Quality Index*."


@D b_psg_eeg_10_20_montage_standard_2 :: sleep-medicine [ok]
  text = "PSG EEG 10-20 montage standard."

# ── §5 STATUS ─────────────────────────────────────────



