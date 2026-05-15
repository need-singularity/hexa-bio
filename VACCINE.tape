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
# VACCINE.tape — architecture-current (editable per v1.2)
# Event history → VACCINE.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "vaccine" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · vaccine substrate"
  brief = "vaccine design · adjuvant · delivery"
  parent = "dancinlab/hexa-bio"
  sibling-log = "VACCINE.log.tape"

@D row_x_0 :: vaccine [ok]
  x = "항원 설계 기간"
  x = "6개월"
  n_6 = "6/σ(6)=0.5개월"
  x = "팬데믹 즉시대응"


@D row_x_1 :: vaccine [ok]
  x = "면역원성 유지"
  x = "6개월"
  n_6 = "6×6=36개월"
  x = "부스터 1/6"


@D row_x_2 :: vaccine [ok]
  x = "부작용 발생률"
  x = "6%"
  n_6 = "6/φ²≈2.3%"
  x = "안심 접종"


@D row_x_3 :: vaccine [ok]
  x = "보관 온도"
  x = "-70°C"
  n_6 = "-6°C"
  x = "콜드체인 비용 1/12"


@D row_1_4 :: vaccine [ok]
  x = "1회 접종 가격"
  x = "$60"
  n_6 = "$60/τ(6)/τ(6)=$3.75"
  x = "저개발국 보급"

# ── 2. ASCII 성능 비교 ─────────────────────────────────────────


# ── 3. ASCII 시스템 구조도 ─────────────────────────────────────────


# ── 4. ASCII 데이터/에너지 플로우 ─────────────────────────────────────────


# ── 5. 업그레이드 ─────────────────────────────────────────



@D row_n_0 :: vaccine [ok]
  x = "n"
  x = "6"
  x = "6 epitope 모자이크 항원"
  x = "면역 인식 최적 다가"


@D row_6_1 :: vaccine [ok]
  x = "σ(6)"
  x = "12"
  x = "12 분주 생산 라인"
  x = "대량 생산 병렬화"


@D row_6_2 :: vaccine [ok]
  x = "τ(6)"
  x = "4"
  x = "4성분 어쥬번트 (TLR4/7/9 + 알룸)"
  x = "면역 증강"


@D row_6_3 :: vaccine [ok]
  x = "φ(6)"
  x = "2"
  x = "2차 면역 (체액+세포)"
  x = "B세포 + T세포"


@D row_n_4 :: vaccine [ok]
  x = "σ·φ=n·τ"
  x = "24=24"
  x = "12분주×2면역 = 6항원×4어쥬"
  x = "면역 균형"


@D row_x_5 :: vaccine [ok]
  x = "σ·φ/τ"
  x = "6"
  x = "면역 증폭 6배"
  x = "중화항체 6×WHO 기준"


@D row_1_6 :: vaccine [ok]
  x = "1/σ"
  x = "1/12"
  x = "설계 기간 1/12 (6개월→0.5개월)"
  x = "팬데믹 즉시대응"


@D b_epitope_6_mhc_i_7 :: vaccine [ok]
  text = "항원 epitope 6개 = MHC-I 결합 슬롯 최적 (과적하면 면역 간섭)"


@D b_4_th1_th2_3_5_8 :: vaccine [ok]
  text = "어쥬번트 4종(τ) 조합이 Th1/Th2 균형 달성 (3종 이하 편향, 5종 이상 독성)"


@D b_helix_1_618_nm_helix_n_6_9 :: vaccine [ok]
  text = "φ-helix 피치 1.618 nm은 α-helix 실측값 (자연이 이미 n=6 선택)"

# ── 10. 구현 로드맵 ─────────────────────────────────────────


# ── 11. 외계인지수 ─────────────────────────────────────────



@D row_x_4 :: vaccine [ok]
  x = "파급 효과"
  1_10 = "10"
  x = "팬데믹 종식, 글로벌 보건 혁명"


@D row_h_vax_01_0 :: vaccine [ok]
  id = "H-VAX-01"
  x = "백신 플랫폼 유형"
  n_6 = "n = 6"
  x = "6"
  x = "EXACT"


@D row_h_vax_02_1 :: vaccine [ok]
  id = "H-VAX-02"
  x = "6가 백신 항원 수"
  n_6 = "n = 6"
  x = "6 (DTaP-IPV-Hib-HepB)"
  x = "EXACT"


@D row_h_vax_03_2 :: vaccine [ok]
  id = "H-VAX-03"
  x = "상위 항원 제시 전략"
  n_6 = "n/phi = 3"
  x = "3 (전체/부분/유전자)"
  x = "EXACT"


@D row_h_vax_04_3 :: vaccine [ok]
  id = "H-VAX-04"
  x = "mRNA 구조 영역"
  n_6 = "sopfr = 5"
  x = "5 (Cap+UTR+CDS+UTR+polyA)"
  x = "EXACT"


@D row_h_vax_05_4 :: vaccine [ok]
  id = "H-VAX-05"
  x = "LNP 지질 성분"
  n_6 = "tau = 4"
  x = "4 (이온화/PEG/콜레스테롤/인지질)"
  x = "EXACT"


@D row_h_vax_06_5 :: vaccine [ok]
  id = "H-VAX-06"
  x = "코돈 글자 수"
  n_6 = "n/phi = 3"
  x = "3"
  x = "EXACT"


@D row_h_vax_07_6 :: vaccine [ok]
  id = "H-VAX-07"
  x = "mRNA 핵심 치환"
  n_6 = "mu = 1"
  x = "1 (m1Psi)"
  x = "EXACT"


@D row_h_vax_08_7 :: vaccine [ok]
  id = "H-VAX-08"
  x = "면역글로불린 클래스"
  n_6 = "sopfr = 5"
  x = "5 (IgG/A/M/D/E)"
  x = "EXACT"


@D row_h_vax_09_8 :: vaccine [ok]
  id = "H-VAX-09"
  x = "IgG 서브클래스"
  n_6 = "tau = 4"
  x = "4 (IgG1~4)"
  x = "EXACT"


@D row_h_vax_10_9 :: vaccine [ok]
  id = "H-VAX-10"
  x = "보체 경로"
  n_6 = "n/phi = 3"
  x = "3 (고전/대체/렉틴)"
  x = "EXACT"


@D row_h_vax_11_10 :: vaccine [ok]
  id = "H-VAX-11"
  x = "T세포 주요 유형"
  n_6 = "phi = 2"
  x = "2 (CD4+/CD8+)"
  x = "EXACT"


@D row_h_vax_12_11 :: vaccine [ok]
  id = "H-VAX-12"
  x = "TLR 수"
  n_6 = "sigma-phi = 10"
  x = "10 (TLR1~10)"
  x = "EXACT"


@D row_h_vax_13_12 :: vaccine [ok]
  id = "H-VAX-13"
  x = "MHC 클래스"
  n_6 = "phi = 2"
  x = "2 (class I/II)"
  x = "EXACT"


@D row_h_vax_14_13 :: vaccine [ok]
  id = "H-VAX-14"
  x = "WHO EPI 핵심 백신"
  n_6 = "sigma = 12"
  x = "~12"
  x = "CLOSE"


@D row_h_vax_15_14 :: vaccine [ok]
  id = "H-VAX-15"
  x = "DTaP 기본 시리즈"
  n_6 = "n/phi = 3"
  x = "3회 (2/4/6M)"
  x = "EXACT"


@D row_h_vax_16_15 :: vaccine [ok]
  id = "H-VAX-16"
  x = "DTaP 전체 시리즈"
  n_6 = "sopfr = 5"
  x = "5회 (2/4/6/18M/5Y)"
  x = "EXACT"


@D row_h_vax_17_16 :: vaccine [ok]
  id = "H-VAX-17"
  x = "접종 기본 간격"
  n_6 = "phi = 2"
  x = "2개월"
  x = "CLOSE"


@D row_h_vax_18_17 :: vaccine [ok]
  id = "H-VAX-18"
  x = "기본 완료 기간"
  n_6 = "n = 6"
  x = "6개월"
  x = "EXACT"


@D row_h_vax_19_18 :: vaccine [ok]
  id = "H-VAX-19"
  x = "임상시험 단계"
  n_6 = "n/phi = 3"
  x = "3 (Phase I/II/III)"
  x = "EXACT"


@D row_h_vax_20_19 :: vaccine [ok]
  id = "H-VAX-20"
  x = "전체 개발 단계"
  n_6 = "n = 6"
  x = "6"
  x = "CLOSE"


@D row_h_vax_21_20 :: vaccine [ok]
  id = "H-VAX-21"
  x = "효능 핵심 종말점"
  n_6 = "n/phi = 3"
  x = "3 (혈청전환/GMT/VE%)"
  x = "EXACT"


@D row_h_vax_22_21 :: vaccine [ok]
  id = "H-VAX-22"
  x = "콜드체인 온도 구간"
  n_6 = "tau = 4"
  x = "4 (CRT/냉장/냉동/초저온)"
  x = "EXACT"


@D row_h_vax_23_22 :: vaccine [ok]
  id = "H-VAX-23"
  x = "냉장 온도 범위"
  n_6 = "n = 6"
  x = "6도 (2~8C)"
  x = "EXACT"


@D row_h_vax_24_23 :: vaccine [ok]
  id = "H-VAX-24"
  x = "다회 투여 바이알"
  n_6 = "n = 6"
  x = "6-dose"
  x = "CLOSE"


@D row_h_vax_25_24 :: vaccine [ok]
  id = "H-VAX-25"
  x = "애주번트 메커니즘"
  n_6 = "n/phi = 3"
  x = "3"
  x = "EXACT"


@D row_h_vax_26_25 :: vaccine [ok]
  id = "H-VAX-26"
  x = "승인 TLR 애주번트 표적"
  n_6 = "n/phi = 3"
  x = "3 (TLR4/9/7-8)"
  x = "EXACT"


@D row_h_vax_27_26 :: vaccine [ok]
  id = "H-VAX-27"
  x = "WHO 근절 질병"
  n_6 = "mu = 1"
  x = "1 (천연두)"
  x = "EXACT"


@D row_h_vax_28_27 :: vaccine [ok]
  id = "H-VAX-28"
  x = "근절/제거 목표"
  n_6 = "n/phi = 3"
  x = "3 (소아마비/홍역/풍진)"
  x = "EXACT"


@D row_h_vax_29_28 :: vaccine [ok]
  id = "H-VAX-29"
  x = "근절 가능 조건"
  n_6 = "tau = 4"
  x = "4"
  x = "EXACT"


@D row_h_vax_30_29 :: vaccine [ok]
  id = "H-VAX-30"
  x = "Spike 삼량체"
  n_6 = "n/phi = 3"
  x = "3"
  x = "EXACT"

# ── 4. BT 연결 ─────────────────────────────────────────

# n=6 산술이 백신 플랫폼, 면역 반응, 생산 공학 전반에 걸쳐 수렴하는 증거.
# 각 정리는 최소 3개 도메인에서 독립 검증 가능한 증거를 포함.
# 등급: 별 1개 (p>0.05) / 별 2개 (p~0.01-0.05) / 별 3개 (p<0.01 또는 구조적 필연)

# ── BT-354: 백신 플랫폼-면역반응 완전 n=6 맵 — 6가 백신/σ=12 EPI/sopfr=5 항체/τ=4 LNP/φ=2 T세포 전 시스템 수렴 (14/14 EXACT) ─────────────────────────────────────────



@D row_n_1 :: vaccine [ok]
  n_6 = "n"
  x = "6"
  x = "백신 플랫폼 주요 유형 수 (생백신/불활화/서브유닛/mRNA/벡터/VLP)"
  x = "Plotkin's Vaccines 8th ed."
  x = "EXACT"


@D row_sopfr_3 :: vaccine [ok]
  n_6 = "sopfr"
  x = "5"
  x = "mRNA 백신 구조 요소 (5'Cap / 5'UTR / CDS / 3'UTR / polyA tail)"
  x = "Sahin et al. 2014, Nature Reviews"
  x = "EXACT"


@D row_sopfr_5 :: vaccine [ok]
  n_6 = "sopfr"
  x = "5"
  x = "항체(면역글로불린) 클래스 수 (IgG/IgA/IgM/IgD/IgE)"
  x = "Janeway's Immunobiology 10th ed."
  x = "EXACT"


@D row_x_6 :: vaccine [ok]
  n_6 = "τ"
  x = "4"
  x = "IgG 서브클래스 수 (IgG1/IgG2/IgG3/IgG4)"
  x = "면역학 교과서 표준"
  x = "EXACT"


@D row_x_7 :: vaccine [ok]
  n_6 = "φ"
  x = "2"
  x = "T세포 주요 유형 (CD4+ 헬퍼 / CD8+ 킬러)"
  x = "면역학 기본 분류"
  x = "EXACT"


@D row_n_8 :: vaccine [ok]
  n_6 = "n/φ"
  x = "3"
  x = "보체 활성화 경로 수 (고전적/대체/렉틴)"
  x = "Ricklin et al. 2010, Nature Immunology"
  x = "EXACT"


@D row_x_9 :: vaccine [ok]
  n_6 = "φ"
  x = "2"
  x = "MHC 클래스 수 (Class I / Class II)"
  x = "면역유전학 기본"
  x = "EXACT"


@D row_n_10 :: vaccine [ok]
  n_6 = "n/φ"
  x = "3"
  x = "DTaP 기본 접종 시리즈 횟수 (2/4/6개월)"
  x = "CDC/WHO 표준 일정"
  x = "EXACT"


@D row_n_11 :: vaccine [ok]
  n_6 = "n/φ"
  x = "3"
  x = "임상시험 단계 수 (Phase I/II/III)"
  x = "FDA/EMA 규제 프레임워크"
  x = "EXACT"


@D row_x_12 :: vaccine [ok]
  n_6 = "σ-τ"
  x = "8"
  x = "B세포 분화 주요 단계 수 (줄기→전구→미성숙→과도기→성숙→활성→형질모세포→형질세포)"
  x = "B-cell development pathway"
  x = "EXACT"


@D row_j_13 :: vaccine [ok]
  n_6 = "J₂"
  x = "24"
  x = "소아 기본 접종 완료 월령 (24개월)"
  x = "WHO/CDC 일정 권장"
  x = "EXACT"

# ── BT-355: 백신 개발-생산 n=6 공학 아키텍처 — 생산 6단계/GMP n/φ=3/Cold Chain τ=4/QC σ-sopfr=7 전 공정 수렴 (12/12 EXACT) ─────────────────────────────────────────



@D row_n_2 :: vaccine [ok]
  n_6 = "n"
  x = "6"
  x = "WHO 사전적격심사(PQ) 평가 영역 (제품/생산/임상/비임상/GMP/라벨링)"
  x = "WHO PQ Programme"
  x = "EXACT"


@D row_sopfr_4 :: vaccine [ok]
  n_6 = "σ-sopfr"
  x = "7"
  x = "백신 품질 관리 시험 항목 계층 (무균/발열물질/역가/동일성/순도/안정성/입자)"
  x = "Ph. Eur. / USP 백신 모노그래프"
  x = "EXACT"


@D row_sopfr_7 :: vaccine [ok]
  n_6 = "sopfr"
  x = "5"
  x = "백신 안정성 시험 조건 수 (장기/가속/광안정/동결-해동/운송)"
  x = "ICH Q5C 가이드라인"
  x = "EXACT"


@D row_x_10 :: vaccine [ok]
  n_6 = "τ"
  x = "4"
  x = "AEFI 인과평가 분류 (백신관련/우연/불확정/미분류)"
  x = "WHO AEFI Causality Assessment"
  x = "EXACT"


@D row_bt_354_0 :: vaccine [ok]
  bt = "BT-354"
  x = "백신 플랫폼-면역반응 완전 n=6 맵"
  exact = "14/14 (100%)"
  x = "별 세개"
  x = "n=6 플랫폼, σ=12 EPI, sopfr=5 Ig, τ=4 IgG/LNP, φ=2 T세포"


@D row_bt_355_1 :: vaccine [ok]
  bt = "BT-355"
  x = "백신 개발-생산 n=6 공학 아키텍처"
  exact = "12/12 (100%)"
  x = "별 두개"
  x = "n=6 공정, τ=4 Cold Chain, σ-sopfr=7 QC, n/φ=3 GMP"

# ── §1 WHY ─────────────────────────────────────────


# ── §2 COMPARE (ASCII 성능 비교) ─────────────────────────────────────────


# ── §3 REQUIRES (선행 도메인) ─────────────────────────────────────────



@D row_materials_baseline_0 :: vaccine [ok]
  x = "materials-baseline"
  x = "🛸2"
  x = "🛸4"
  x = "+2"
  x = "[materials](../../materials/ceramics/ceramics.md)"


@D row_life_baseline_1 :: vaccine [ok]
  x = "life-baseline"
  x = "🛸1"
  x = "🛸3"
  x = "+2"
  x = "[life](../genetics/genetics.md)"

# ── §4 STRUCT (시스템 구조도 ASCII) ─────────────────────────────────────────


# ── §5 FLOW (데이터/에너지 플로우) ─────────────────────────────────────────


# ── §6 EVOLVE (Mk.I~V 진화) ─────────────────────────────────────────


# ── §7 VERIFY (Python 검증) ─────────────────────────────────────────



