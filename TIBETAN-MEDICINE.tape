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
# TIBETAN-MEDICINE.tape — architecture-current (editable per v1.2)
# Event history → TIBETAN-MEDICINE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "tibetan-medicine" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · tibetan medicine substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "TIBETAN-MEDICINE.log.tape"

@D row_1_0 :: tibetan-medicine [ok]
  x = "1"
  taste = "sweet"
  tibetan = "mngar"
  western_analogue = "sugars"


@D row_2_1 :: tibetan-medicine [ok]
  x = "2"
  taste = "sour"
  tibetan = "skyur"
  western_analogue = "acid / fermented"


@D row_3_2 :: tibetan-medicine [ok]
  x = "3"
  taste = "salty"
  tibetan = "lan tshwa"
  western_analogue = "minerals"


@D row_4_3 :: tibetan-medicine [ok]
  x = "4"
  taste = "bitter"
  tibetan = "kha"
  western_analogue = "alkaloids"


@D row_5_4 :: tibetan-medicine [ok]
  x = "5"
  taste = "hot (pungent)"
  tibetan = "tsha ba"
  western_analogue = "capsaicin family"


@D row_6_5 :: tibetan-medicine [ok]
  x = "6"
  taste = "astringent"
  tibetan = "bska ba"
  western_analogue = "tannins"


@D b_6_12_phi_6_2_tau_6_4_identity_un_6 :: tibetan-medicine [ok]
  text = "σ(6)=12 · phi(6)=2 · tau(6)=4 — identity uniquely at n=6."


@D b_6_tastes_is_the_main_classificat_7 :: tibetan-medicine [ok]
  text = "**6 tastes** is the main classification axis."


@D b_rlung_wind_disorders_6_types_8 :: tibetan-medicine [ok]
  text = "**Rlung (wind) disorders**: 6 types."


@D b_gy_shi_body_classification_axes_9 :: tibetan-medicine [ok]
  text = "**Gyüshi body-classification axes**: 6 (body, space, season, age,"

# ── §2 n=6 CONNECTION (depth > 2 — culturally independent, textually fixed) ─────────────────────────────────────────


# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 VERIFY (roadmap) ─────────────────────────────────────────



@D b_atlas_node_add_c_tibetan_medicin_0 :: tibetan-medicine [ok]
  text = "[ ] Atlas node: add `@C:tibetan-medicine` under life sector (cross-layer"


@D b_assert_gyushi_taste_count_6_in_v_1 :: tibetan-medicine [ok]
  text = "[ ] Assert `gyushi_taste_count == 6` in `verify_tibetan-medicine.hexa`"


@D b_cross_reference_gy_shi_primary_s_2 :: tibetan-medicine [ok]
  text = "[ ] Cross-reference Gyüshi primary source references."

# ── §5 SOURCES ─────────────────────────────────────────



@D b_rgyud_bzhi_four_tantras_root_tan_0 :: tibetan-medicine [ok]
  text = "*rGyud bzhi* (Four Tantras), root tantra, ca. 12th century."


@D b_desi_sangye_gyatso_blue_beryl_co_1 :: tibetan-medicine [ok]
  text = "Desi Sangye Gyatso, *Blue Beryl* commentary (1703)."


@D b_men_tsee_khang_tibetan_medical_a_2 :: tibetan-medicine [ok]
  text = "Men-Tsee-Khang Tibetan Medical & Astrological Institute curriculum."

# ── §6 STATUS ─────────────────────────────────────────



