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
# GASTROINTESTINAL-MEDICINE.tape — architecture-current (editable per v1.2)
# Event history → GASTROINTESTINAL-MEDICINE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "gastrointestinal-medicine" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · gastrointestinal medicine substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "GASTROINTESTINAL-MEDICINE.log.tape"

@D b_6_gi_segments_endoscopy_staging_0 :: gastrointestinal-medicine [ok]
  text = "**6 GI segments** — endoscopy staging primitive."


@D b_6_dominant_gut_microbiome_phyla_1 :: gastrointestinal-medicine [ok]
  text = "**6 dominant gut-microbiome phyla**."


@D b_6_fps_capsule_endoscopy_baseline_2 :: gastrointestinal-medicine [ok]
  text = "**6 fps** capsule-endoscopy baseline."

# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 SOURCES ─────────────────────────────────────────



@D b_sleisenger_fordtran_gastrointest_0 :: gastrointestinal-medicine [ok]
  text = "Sleisenger & Fordtran, *Gastrointestinal and Liver Disease*."


@D b_human_microbiome_project_reports_1 :: gastrointestinal-medicine [ok]
  text = "Human Microbiome Project reports (dominant phyla)."


@D b_fda_capsule_endoscopy_device_sta_2 :: gastrointestinal-medicine [ok]
  text = "FDA capsule-endoscopy device standards."

# ── §5 STATUS ─────────────────────────────────────────



