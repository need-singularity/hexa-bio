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
# NEUROPHARMACOLOGY.tape — architecture-current (editable per v1.2)
# Event history → NEUROPHARMACOLOGY.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "neuropharmacology" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · neuropharmacology substrate"
  brief = "per-domain substrate · n=6 mapping · biological/biochemical context"
  parent = "dancinlab/hexa-bio"
  sibling-log = "NEUROPHARMACOLOGY.log.tape"

@D row_x_0 :: neuropharmacology [ok]
  x = "우울증 치료"
  x = "SSRI 반응률 50~60%, 4~6주 대기"
  hexa_neuro = "n/φ=3 모노아민 동시 표적, σ·τ=48시간 항정상태 최적"
  n_6 = "n/φ=3, σ·τ=48"


@D row_x_1 :: neuropharmacology [ok]
  x = "불안장애"
  x = "벤조디아제핀 의존성 위험"
  hexa_neuro = "φ=2 수용체 유형 기반 이온성/대사성 이중 조절"
  n_6 = "φ=2"


@D row_x_2 :: neuropharmacology [ok]
  x = "파킨슨병"
  x = "레보도파 장기 사용 시 운동 합병증"
  hexa_neuro = "sopfr=5 도파민 D1~D5 아형 선택적 작용제 설계"
  n_6 = "sopfr=5"


@D row_x_3 :: neuropharmacology [ok]
  x = "알츠하이머"
  x = "아세틸콜린에스테라아제 억제제 제한적"
  hexa_neuro = "σ=12 신경전달물질 네트워크 다중 표적 전략"
  n_6 = "σ=12"


@D row_x_4 :: neuropharmacology [ok]
  x = "수면장애"
  x = "수면제 내성/반동 불면증"
  hexa_neuro = "J₂=24시간 일주기 리듬 정밀 동기화"
  n_6 = "J₂=24"


@D row_x_5 :: neuropharmacology [ok]
  x = "만성통증"
  x = "오피오이드 중독 위기 (미국 연간 8만명 사망)"
  hexa_neuro = "σ-φ=10 mg 기본 용량 + σ-τ=8시간 반감기 최적"
  n_6 = "σ-φ=10, σ-τ=8"


@D row_x_6 :: neuropharmacology [ok]
  x = "약물 부작용"
  x = "정신과 약물 60% 환자 부작용 호소"
  hexa_neuro = "τ=4 ADME 전단계 시뮬레이션으로 부작용 예측"
  n_6 = "τ=4"


@D row_x_7 :: neuropharmacology [ok]
  x = "약물 개발"
  x = "신약 1개 개발 10~15년, 20억 달러"
  hexa_neuro = "n=6 세로토닌 수용체 계열 표적 최적화로 기간 σ/φ=6배 단축"
  n_6 = "n=6"
# 핵심: 신경약리학의 구조적 상수들이 n=6 산술에 정밀 수렴한다. 주요 신경전달물질 12종=σ, 약물동태 4단계=τ, 수용체 이분법=φ, 도파민 아형 5종=sopfr, 일주기 24시간=J₂ -- 독립적으로 확립된 생물학 사실들이 모두 n=6 상수와 일치한다.
# "뇌를 이해하려면 σ=12 신경전달물질의 τ=4 동태를 φ=2 수용체에서 읽어야 한다."

# ── 핵심 상수 ─────────────────────────────────────────


# ── 신경약리학 n=6 매핑 (11건) ─────────────────────────────────────────


# ── ASCII 시스템 구조도 ─────────────────────────────────────────


# ── ASCII 성능 비교 그래프 ─────────────────────────────────────────


# ── ASCII 데이터/에너지 플로우 ─────────────────────────────────────────


# ── 가설 (H-NP-01~20) ─────────────────────────────────────────


# ── 10대 불가능성 정리 (신경약리학 물리적 한계) ─────────────────────────────────────────


# ── 검증 가능 예측 (12건) ─────────────────────────────────────────


# ── 교차 도메인 브릿지 ─────────────────────────────────────────


# ── 진화 체크포인트 (Mk.I~V) ─────────────────────────────────────────


# ── 파이썬 검증코드 ─────────────────────────────────────────


# ── 정직한 검증 요약 ─────────────────────────────────────────


# ── §1 WHY ─────────────────────────────────────────


# ── §2 COMPARE (ASCII 성능 비교) ─────────────────────────────────────────


# ── §3 REQUIRES (선행 도메인) ─────────────────────────────────────────



@D row_materials_baseline_0 :: neuropharmacology [ok]
  x = "materials-baseline"
  x = "🛸2"
  x = "🛸4"
  x = "+2"
  x = "[materials](../../materials/ceramics/ceramics.md)"


@D row_life_baseline_1 :: neuropharmacology [ok]
  x = "life-baseline"
  x = "🛸1"
  x = "🛸3"
  x = "+2"
  x = "[life](../genetics/genetics.md)"

# ── §4 STRUCT (시스템 구조도 ASCII) ─────────────────────────────────────────


# ── §5 FLOW (데이터/에너지 플로우) ─────────────────────────────────────────


# ── §6 EVOLVE (Mk.I~V 진화) ─────────────────────────────────────────


# ── §7 VERIFY (Python 검증) ─────────────────────────────────────────



