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
# NUCLEAR-MEDICINE.tape — architecture-current (editable per v1.2)
# Event history → NUCLEAR-MEDICINE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "nuclear-medicine" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · nuclear medicine substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "NUCLEAR-MEDICINE.log.tape"

@D b_6_12_phi_6_2_tau_6_4_identity_un_0 :: nuclear-medicine [ok]
  text = "σ(6)=12 · phi(6)=2 · tau(6)=4 — identity uniquely at n=6."


@D b_tc_99m_t_6_01_h_measured_balance_1 :: nuclear-medicine [ok]
  text = "**Tc-99m t½ = 6.01 h** (measured): balances imaging statistics (slow enough"


@D b_pet_detector_rings_6_detector_bl_2 :: nuclear-medicine [ok]
  text = "**PET detector rings**: 6 detector blocks is the minimum angular sampling"

# ── §2 n=6 CONNECTION (depth > 2 — nuclear physics + clinical optimum) ─────────────────────────────────────────


# ── §3 DIFFERENTIATION ─────────────────────────────────────────


# ── §4 VERIFY (roadmap) ─────────────────────────────────────────



@D b_atlas_node_add_m_nuclear_medicin_0 :: nuclear-medicine [ok]
  text = "[ ] Atlas node: add `@M:nuclear-medicine` under life sector"


@D b_assert_tc99m_half_life_hours_6_1_1 :: nuclear-medicine [ok]
  text = "[ ] Assert `tc99m_half_life_hours == 6` (±1% tolerance) in"


@D b_cross_link_to_physics_medical_ph_2 :: nuclear-medicine [ok]
  text = "[ ] Cross-link to `physics/medical-physics` and `life/cancer-therapy`."

# ── §5 SOURCES ─────────────────────────────────────────



@D b_nndc_chart_of_nuclides_tc_99m_t_0 :: nuclear-medicine [ok]
  text = "NNDC Chart of Nuclides (Tc-99m t½ = 6.0067 h ± measurement)."


@D b_cherry_sorenson_phelps_physics_i_1 :: nuclear-medicine [ok]
  text = "Cherry, Sorenson & Phelps, *Physics in Nuclear Medicine*."

# ── §6 STATUS ─────────────────────────────────────────



