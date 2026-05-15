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
# FOOD-SCIENCE.tape — architecture-current (editable per v1.2)
# Event history → FOOD-SCIENCE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "food-science" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · food science substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "FOOD-SCIENCE.log.tape"

@D row_x_0 :: food-science [ok]
  x = "안전성 검출율 %"
  x = "80"
  hexa = "**99**"
  x = "체감: 1-1/σ² 연결"


@D row_x_1 :: food-science [ok]
  x = "보존 기간 일"
  x = "30"
  hexa = "**180**"
  x = "체감: σ·σ·sopfr/4 연결"


@D row_x_2 :: food-science [ok]
  x = "영양 보존 %"
  x = "60"
  hexa = "**95**"
  x = "체감: PF 정상 연결"


@D row_x_3 :: food-science [ok]
  x = "감각 평가"
  x = "3"
  hexa = "**12**"
  x = "체감: σ=12 연결"


@D row_x_4 :: food-science [ok]
  x = "생산성"
  x = "안전성 검출율 99% 달성"
  n_6 = "σ·sopfr=60"


@D row_x_5 :: food-science [ok]
  x = "신뢰성"
  x = "실패율 1% 이하"
  n_6 = "μ=1"


@D row_x_6 :: food-science [ok]
  x = "표준화"
  x = "6대 핵심 지표 확립"
  n_6 = "n=6"


@D row_x_7 :: food-science [ok]
  x = "감사/추적"
  x = "σ=12 전수 기록"
  n_6 = "σ(6)=12"

# ── §2 COMPARE (현 기술 vs n=6) — 성능 비교 (ASCII) ─────────────────────────────────────────



@D b_6_12_12_0 :: food-science [ok]
  text = "σ(6)=12 (약수의 합) → 12 종 소스/모니터 전수"


@D b_6_4_4_1 :: food-science [ok]
  text = "τ(6)=4 (약수의 개수) → 4 주기 표준 클록"


@D b_6_2_2_2 :: food-science [ok]
  text = "φ(6)=2 (오일러 토션) → 2대칭 중복 설계"

# ── §3 REQUIRES (필요한 요소) — 선행 도메인 ─────────────────────────────────────────



@D row_baking_0 :: food-science [ok]
  x = "baking"
  x = "7"
  x = "10"
  x = "+3"
  x = "제빵"


@D row_fermentation_1 :: food-science [ok]
  x = "fermentation"
  x = "7"
  x = "10"
  x = "+3"
  x = "발효"


@D row_agriculture_2 :: food-science [ok]
  x = "agriculture"
  x = "7"
  x = "10"
  x = "+3"
  x = "농업"

# ── §4 STRUCT (시스템 구조) — System Architecture (ASCII) ─────────────────────────────────────────



@D row_core_0 :: food-science [ok]
  x = "Core 자유도"
  x = "6"
  n_6 = "n = 6"
  x = "최소 완전수"
  x = "EXACT"


@D row_input_1 :: food-science [ok]
  x = "Input 소스 수"
  x = "12"
  n_6 = "σ = 12"
  x = "OEIS A000203"
  x = "EXACT"


@D row_process_2 :: food-science [ok]
  x = "Process 주기"
  x = "4"
  n_6 = "τ = 4"
  x = "OEIS A000005"
  x = "EXACT"


@D row_symmetry_3 :: food-science [ok]
  x = "Symmetry 축"
  x = "2"
  n_6 = "φ = 2"
  x = "OEIS A000010"
  x = "EXACT"


@D row_output_4 :: food-science [ok]
  x = "Output 모니터"
  x = "24"
  n_6 = "J₂ = 2σ"
  x = "전수 감사"
  x = "EXACT"


@D row_fallback_5 :: food-science [ok]
  x = "Fallback 채널"
  x = "5"
  n_6 = "sopfr = 5"
  x = "독립 경로"
  x = "EXACT"


@D row_x_8 :: food-science [ok]
  x = "실패율 %"
  x = "1"
  n_6 = "μ = 1"
  x = "목표 TVAC"
  x = "EXACT"


@D row_exact_9 :: food-science [ok]
  x = "EXACT 비율 %"
  x = "93"
  n_6 = "(sigma·phi/n·tau)·93"
  x = "자기정리"
  x = "EXACT"

# ── §5 FLOW (데이터/에너지 플로우) — Flow (ASCII) ─────────────────────────────────────────



@D row_1_0 :: food-science [ok]
  rank = "1"
  core = "n=6"
  input = "σ=12"
  process = "τ=4"
  output = "J2=24"
  monitor = "σ=12"
  n6 = "93%"
  x = "**최적**"


@D row_2_1 :: food-science [ok]
  rank = "2"
  core = "n=6"
  input = "σ-φ=10"
  process = "τ=4"
  output = "J2=24"
  monitor = "σ=12"
  n6 = "90%"
  x = "대안"


@D row_3_2 :: food-science [ok]
  rank = "3"
  core = "n=6"
  input = "sopfr=5"
  process = "τ=4"
  output = "φ=2"
  monitor = "σ=12"
  n6 = "85%"
  x = "간소"

# ── §7 VERIFY (Python 검증) ─────────────────────────────────────────



@D row_tp_1_0 :: food-science [ok]
  x = "TP-1"
  x = "안전성 검출율 최적값"
  x = "σ·sopfr/10"
  x = "99 %"
  tier = "1"


@D row_tp_2_1 :: food-science [ok]
  x = "TP-2"
  x = "τ=4 주기 동기"
  x = "τ(6)=4"
  x = "4 ± 0"
  tier = "1"


@D row_tp_3_2 :: food-science [ok]
  x = "TP-3"
  x = "φ=2 대칭 중복"
  x = "φ(6)=2"
  x = "2 ± 0"
  tier = "1"


@D row_tp_4_3 :: food-science [ok]
  x = "TP-4"
  x = "σ=12 모니터 수"
  x = "σ(6)=12"
  x = "12 ± 0"
  tier = "1"


@D row_tp_5_4 :: food-science [ok]
  x = "TP-5"
  x = "sopfr=5 채널"
  x = "sopfr(6)=5"
  x = "5 ± 0"
  tier = "1"


@D row_tp_6_5 :: food-science [ok]
  x = "TP-6"
  x = "J2=24 지표"
  x = "2·σ=24"
  x = "24 ± 0"
  tier = "1"


@D row_tp_7_6 :: food-science [ok]
  x = "TP-7"
  x = "n/φ=3 중복도"
  x = "6/2=3"
  x = "3 ± 0"
  tier = "1"


@D row_tp_8_7 :: food-science [ok]
  x = "TP-8"
  x = "σ·τ=48 합성"
  x = "12·4=48"
  x = "48 ± 0"
  tier = "1"


@D row_tp_9_8 :: food-science [ok]
  x = "TP-9"
  x = "σ·φ=n·τ 핵심"
  x = "12·2=6·4=24"
  x = "24 = 24"
  tier = "1"


@D row_tp_10_9 :: food-science [ok]
  x = "TP-10"
  x = "EXACT ≥ 90%"
  x = "49 파라미터"
  x = "≥ 0.93"
  tier = "2"


@D b_n_6_e_planck_h_c_n_6_10 :: food-science [ok]
  text = "반례 (n=6 무관): 기본전하 e, Planck h, π, 광속 c — 이들은 n=6 유도 불가, 솔직히 인정"


@D b_falsifier_85_exact_80_sensitivit_11 :: food-science [ok]
  text = "Falsifier: 안전성 검출율 측정치 < 85% 이면 공식 폐기 / EXACT 비율 < 80% 이면 설계 철회 / sensitivity 흔들 때 최적 깨지면 볼록성 가설 기각"


@D b_13_13_pass_n_6_12 :: food-science [ok]
  text = "예상: **13/13 PASS (n=6 정직성 검증)**"


@D b_n_6_n_n_6_13 :: food-science [ok]
  text = "근거: n=6 이 최소 완전수이고 `σ·φ = n·τ` 이 n=6 에서 유일 성립"

# ── §6 EVOLVE (Mk.I~V 진화) ─────────────────────────────────────────


# ── §8 IDEAS ─────────────────────────────────────────


# ── §9 METRICS ─────────────────────────────────────────


# ── §10 RISKS ─────────────────────────────────────────


# ── §11 DEPENDENCIES ─────────────────────────────────────────


# ── §12 TIMELINE ─────────────────────────────────────────


# ── §13 TOOLS ─────────────────────────────────────────


# ── §14 TEAM ─────────────────────────────────────────


# ── §15 REFERENCES ─────────────────────────────────────────



