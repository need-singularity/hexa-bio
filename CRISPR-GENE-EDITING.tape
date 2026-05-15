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
# CRISPR-GENE-EDITING.tape — architecture-current (editable per v1.2)
# Event history → CRISPR-GENE-EDITING.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "crispr-gene-editing" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · CRISPR gene editing substrate"
  brief = "Cas9/Cas12/Cas13 · gene editing protocols · n=6 mapping"
  parent = "dancinlab/hexa-bio"
  sibling-log = "CRISPR-GENE-EDITING.log.tape"

@D row_x_0 :: crispr-gene-editing [ok]
  x = "유전병 치료"
  x = "대증 요법, 근본 치료 불가"
  hexa_crispr = "유전자 직접 교정, 근본 치유"
  n_6 = "Cas6 + phi=2 이중 가이드"


@D row_x_1 :: crispr-gene-editing [ok]
  x = "항암 면역"
  x = "CAR-T 1세대, 고가/부작용"
  hexa_crispr = "n=6 다중 편집 CAR-T, 정밀 표적"
  n_6 = "n=6, sigma=12배 효율"


@D row_x_2 :: crispr-gene-editing [ok]
  x = "작물 개량"
  x = "10년 이상 품종 개발"
  hexa_crispr = "다중 유전자 동시 편집, tau=4세대 만에 완성"
  n_6 = "tau=4, 기간 n=6분의 1"


@D row_x_3 :: crispr-gene-editing [ok]
  x = "합성 생물학"
  x = "단일 유전자 조작 수준"
  hexa_crispr = "n=6 모듈 동시 조립, 바이오 연료/소재"
  n_6 = "n=6 모듈"


@D row_x_4 :: crispr-gene-editing [ok]
  x = "유전 진단"
  x = "양수 검사/침습적"
  hexa_crispr = "CRISPR 진단칩 (SHERLOCK/DETECTR)"
  n_6 = "비용 1/sigma, n/phi=3단계"


@D row_x_5 :: crispr-gene-editing [ok]
  x = "바이러스 치료"
  x = "백신 개발 수년"
  hexa_crispr = "바이러스 게놈 직접 절단"
  n_6 = "tau=4주 내 치료제"


@D row_x_6 :: crispr-gene-editing [ok]
  x = "희귀 질환"
  x = "치료제 개발 불가 (환자 수 부족)"
  hexa_crispr = "개인 맞춤 유전자 교정"
  n_6 = "7000+ 희귀질환 치료 가능"


@D row_x_7 :: crispr-gene-editing [ok]
  x = "오프타겟 정밀도"
  x = "5~20% 오프타겟 발생"
  hexa_crispr = "Cas6+dual guide -> <0.1%"
  n_6 = "sigma-phi=10bp 윈도우"


@D row_x_8 :: crispr-gene-editing [ok]
  x = "전달 효율"
  x = "바이러스 벡터 30~60%"
  hexa_crispr = "Egyptian 1/2+1/3+1/6=1 완전 최적화"
  n_6 = "Egyptian=1"


@D row_x_9 :: crispr-gene-editing [ok]
  x = "세포 생존율"
  x = "편집 후 50~70% 생존"
  hexa_crispr = "Carnot 1-phi/sigma=83.3% 최적"
  n_6 = "Carnot 천장"


@D row_x_10 :: crispr-gene-editing [ok]
  x = "비용"
  x = "편집당 $10K~50K"
  hexa_crispr = "n/sigma=0.5 비용 절감 (50% 감소)"
  n_6 = "n/sigma=0.5"

# ── 핵심 상수 (n=6 CRISPR 프레임워크) ─────────────────────────────────────────



@D row_1_0 :: crispr-gene-editing [ok]
  x = "1"
  x = "Cas 유형 수"
  n_6 = "n"
  x = "6"
  crispr = "CRISPR Type I~VI = n=6 유형"


@D row_2_1 :: crispr-gene-editing [ok]
  x = "2"
  x = "Cas9 도메인"
  n_6 = "n"
  x = "6"
  crispr = "REC1/REC2/REC3/RuvC/HNH/PAM"


@D row_3_2 :: crispr-gene-editing [ok]
  x = "3"
  x = "가이드 RNA"
  n_6 = "phi(6)"
  x = "2"
  crispr = "crRNA + tracrRNA 이중 가이드"


@D row_4_3 :: crispr-gene-editing [ok]
  x = "4"
  x = "PAM 길이"
  n_6 = "n/phi"
  x = "3"
  crispr = "NGG = 3nt PAM 서열"


@D row_5_4 :: crispr-gene-editing [ok]
  x = "5"
  x = "편집 유형"
  n_6 = "tau(6)"
  x = "4"
  crispr = "녹아웃/녹인/염기편집/프라임편집"


@D row_6_5 :: crispr-gene-editing [ok]
  x = "6"
  x = "전달 경로"
  n_6 = "sopfr(6)"
  x = "5"
  crispr = "바이러스/지질/전기천공/RNP/나노입자"


@D row_7_6 :: crispr-gene-editing [ok]
  x = "7"
  x = "R-loop 시드"
  n_6 = "sigma(6)"
  x = "12"
  crispr = "12nt 시드 서열"


@D row_8_7 :: crispr-gene-editing [ok]
  x = "8"
  x = "세포 주기"
  n_6 = "J2(6)"
  x = "24"
  crispr = "24시간 세포 분열 주기"


@D row_9_8 :: crispr-gene-editing [ok]
  x = "9"
  x = "B-DNA 나선"
  n_6 = "sigma-phi"
  x = "10"
  crispr = "10bp/회전"


@D row_10_9 :: crispr-gene-editing [ok]
  x = "10"
  x = "수복 경로"
  n_6 = "n"
  x = "6"
  crispr = "NHEJ/HDR/MMEJ/BER/NER/직접결합"

# ── ASCII 성능 비교 (시중 vs HEXA-CRISPR v1 vs v2 3단 비교) ─────────────────────────────────────────


# ── ASCII 시스템 구조도 ─────────────────────────────────────────


# ── ASCII 데이터/에너지 플로우 ─────────────────────────────────────────


# ── n=6 핵심 연결 (기존 증거) ─────────────────────────────────────────



@D row_cas9_0 :: crispr-gene-editing [ok]
  x = "Cas9 주요 도메인"
  x = "6 (REC1/REC2/REC3/RuvC/HNH/PAM)"
  n_6 = "n"
  x = "EXACT"


@D row_sgrna_1 :: crispr-gene-editing [ok]
  x = "sgRNA 스템루프"
  x = "4"
  n_6 = "tau"
  x = "EXACT"


@D row_pam_ngg_2 :: crispr-gene-editing [ok]
  x = "PAM 서열 NGG 위치"
  x = "3'-말단"
  n_6 = "n/phi"
  x = "EXACT"


@D row_r_loop_3 :: crispr-gene-editing [ok]
  x = "R-loop 형성 시드 길이"
  x = "12 nt"
  n_6 = "sigma"
  x = "EXACT"


@D row_rna_4 :: crispr-gene-editing [ok]
  x = "가이드 RNA 길이"
  x = "20 nt"
  n_6 = "J2-tau"
  x = "EXACT"


@D row_pam_5 :: crispr-gene-editing [ok]
  x = "PAM-근위 시드"
  x = "10 nt"
  n_6 = "sigma-phi"
  x = "EXACT"


@D row_cas9_6 :: crispr-gene-editing [ok]
  x = "Cas9 분자량"
  x = "~160 kDa"
  n_6 = "phi^tau * sigma-phi"
  x = "CLOSE"


@D row_cas12a_7 :: crispr-gene-editing [ok]
  x = "Cas12a 절단 오프셋"
  x = "18-24 nt"
  n_6 = "(sigma+n)~J2"
  x = "EXACT"


@D row_hdr_8 :: crispr-gene-editing [ok]
  x = "HDR 팔 길이 최적"
  x = "800 bp"
  n_6 = "(sigma-phi)^2 * sigma-tau"
  x = "CLOSE"


@D row_dna_9 :: crispr-gene-editing [ok]
  x = "DNA 이중나선 회전"
  x = "10 bp/turn"
  n_6 = "sigma-phi"
  x = "EXACT"


@D row_x_11 :: crispr-gene-editing [ok]
  x = "스페이서 길이"
  x = "26-72 bp 대표 36 bp"
  n_6 = "n^2"
  x = "EXACT"


@D row_cas_type_12 :: crispr-gene-editing [ok]
  x = "Cas 유형 (Type)"
  x = "6 (I~VI)"
  n_6 = "n"
  x = "EXACT"


@D row_type_ii_13 :: crispr-gene-editing [ok]
  x = "Type II 핵심 단백질"
  x = "1 (Cas9)"
  n_6 = "mu"
  x = "EXACT"


@D row_cas9_nls_14 :: crispr-gene-editing [ok]
  x = "Cas9 NLS 최소 서열"
  x = "7 aa"
  n_6 = "sigma-sopfr"
  x = "EXACT"


@D row_cas12a_ruvc_15 :: crispr-gene-editing [ok]
  x = "Cas12a RuvC 서브도메인"
  x = "3"
  n_6 = "n/phi"
  x = "EXACT"


@D row_cas13_hepn_16 :: crispr-gene-editing [ok]
  x = "Cas13 HEPN 도메인"
  x = "2"
  n_6 = "phi"
  x = "EXACT"


@D row_crispr_17 :: crispr-gene-editing [ok]
  x = "CRISPR 어레이 반복 단위"
  x = "2 (반복+스페이서)"
  n_6 = "phi"
  x = "EXACT"


@D row_pam_ngg_18 :: crispr-gene-editing [ok]
  x = "표준 PAM 길이 (NGG)"
  x = "3 nt"
  n_6 = "n/phi"
  x = "EXACT"


@D row_cas9_19 :: crispr-gene-editing [ok]
  x = "Cas9 활성 부위 금속 이온"
  x = "2 Mg2+"
  n_6 = "phi"
  x = "EXACT"


@D row_spcas9_pam_ngg_20 :: crispr-gene-editing [ok]
  x = "SpCas9 PAM (NGG)"
  x = "2 G"
  n_6 = "phi"
  x = "EXACT"


@D row_sacas9_pam_nngrrt_21 :: crispr-gene-editing [ok]
  x = "SaCas9 PAM (NNGRRT)"
  x = "6 nt"
  n_6 = "n"
  x = "EXACT"


@D row_dsb_22 :: crispr-gene-editing [ok]
  x = "DSB 생성"
  x = "2 절단 (센스+안티센스)"
  n_6 = "phi"
  x = "EXACT"


@D row_x_23 :: crispr-gene-editing [ok]
  x = "닉카제 절단"
  x = "1 가닥"
  n_6 = "mu"
  x = "EXACT"


@D row_hnh_24 :: crispr-gene-editing [ok]
  x = "HNH 도메인 절단 위치"
  x = "PAM 3' 기준 3 nt"
  n_6 = "n/phi"
  x = "EXACT"


@D row_ruvc_25 :: crispr-gene-editing [ok]
  x = "RuvC 도메인 절단 위치"
  x = "PAM 3' 기준 3 nt"
  n_6 = "n/phi"
  x = "EXACT"


@D row_x_26 :: crispr-gene-editing [ok]
  x = "프라임 편집 구성요소"
  x = "3 (Cas9닉+RT+pegRNA)"
  n_6 = "n/phi"
  x = "EXACT"


@D row_x_27 :: crispr-gene-editing [ok]
  x = "염기 편집 활성 윈도우"
  x = "4-8 nt"
  n_6 = "tau~sigma-tau"
  x = "EXACT"


@D row_pegrna_28 :: crispr-gene-editing [ok]
  x = "pegRNA 프라이머 최적"
  x = "10-16 nt"
  n_6 = "sigma-phi~phi^tau"
  x = "EXACT"


@D row_x_29 :: crispr-gene-editing [ok]
  x = "수복 경로 수"
  x = "6 (NHEJ/HDR/MMEJ/BER/NER/직접결합)"
  n_6 = "n"
  x = "EXACT"


@D row_hdr_30 :: crispr-gene-editing [ok]
  x = "HDR 효율 최적 세포주기"
  x = "S/G2 중 2 phase"
  n_6 = "phi"
  x = "EXACT"


@D row_nhej_hdr_31 :: crispr-gene-editing [ok]
  x = "NHEJ:HDR 비율 (기본)"
  x = "~10:1"
  n_6 = "sigma-phi:mu"
  x = "EXACT"


@D row_1_32 :: crispr-gene-editing [ok]
  x = "1"
  x = "Cas 시스템 구조"
  exact = "10"
  x = "12"
  exact = "83.3%"
  x = "**"


@D row_2_33 :: crispr-gene-editing [ok]
  x = "2"
  x = "Cas 변이체 계보"
  exact = "8"
  x = "8"
  exact = "100%"
  x = "***"


@D row_3_34 :: crispr-gene-editing [ok]
  x = "3"
  x = "PAM+절단+수복"
  exact = "12"
  x = "12"
  exact = "100%"
  x = "***"


@D row_x_35 :: crispr-gene-editing [ok]
  x = "**합계**"
  x = ""
  exact = "**30**"
  x = "**32**"
  exact = "**93.8%**"
  x = "*****"

# ── 증거 테이블 (신규 10항목) ─────────────────────────────────────────



@D row_11_10 :: crispr-gene-editing [ok]
  x = "11"
  x = "무잡음 시퀀싱 불가능"
  n_6 = "SNR=sigma/phi=6"
  x = "Phred 품질 한계"


@D row_12_11 :: crispr-gene-editing [ok]
  x = "12"
  x = "Amdahl 병렬 한계"
  n_6 = "s=1/sigma=1/12"
  x = "다중 편집 직렬 부분"


@D row_13_12 :: crispr-gene-editing [ok]
  x = "13"
  x = "Boltzmann 결합 엔트로피"
  n_6 = "S=k_B*ln(sigma^tau)"
  x = "열역학"


@D row_14_13 :: crispr-gene-editing [ok]
  x = "14"
  x = "돌연변이 역전 불가능"
  n_6 = "phi=2 방향 (편집/역편집) 비대칭"
  x = "비가역성"

# ── 교차 도메인 공명 맵 ─────────────────────────────────────────


# ── 진화 경로 (Mk.I~V) ─────────────────────────────────────────



@D row_i_0 :: crispr-gene-editing [ok]
  mk = "I"
  x = "산술 증명"
  x = "Cas6/코돈/PAM 불변법칙 도출, DNA 이중나선 n=6 증명"
  u_k = "0.9"
  x = "2026"


@D row_ii_1 :: crispr-gene-editing [ok]
  mk = "II"
  x = "다중 편집"
  x = "n=6-plex 동시 편집, sopfr=5 전달 최적화, Egyptian 배분"
  u_k = "0.99"
  x = "2029"


@D row_iii_2 :: crispr-gene-editing [ok]
  mk = "III"
  x = "정밀 치료"
  x = "sigma=12 스크리닝, tau=4 편집유형 통합, 오프타겟 <0.01%"
  u_k = "0.999"
  x = "2033"


@D row_iv_3 :: crispr-gene-editing [ok]
  mk = "IV"
  x = "게놈 설계"
  x = "n!=720 조합 설계, J2=24h 세포주기 동기, 합성생물학 통합"
  u_k = "0.9999"
  x = "2040"


@D row_v_4 :: crispr-gene-editing [ok]
  mk = "V"
  x = "완전 편집"
  x = "14 불가능성 정리 전체 활용, 물리한계 수렴"
  u_k = "1-epsilon"
  x = "2050+"

# ── Cross-DSE 교차 브릿지 ─────────────────────────────────────────



@D row_car_t_5 :: crispr-gene-editing [ok]
  x = "CAR-T 면역"
  crispr_2011 = "1세대 단일 편집"
  crispr_2025 = "다중 편집 CAR-T (UCART)"
  n_6 = "n=6 표적 동시 조작"

# ── 2. 기술 스펙 -- Cas9 단일 절단에서 Prime Editor까지 ─────────────────────────────────────────


# ── 3. ASCII 성능 비교 -- ZFN vs TALEN vs CRISPR-Cas9 vs HEXA-CRISPR ─────────────────────────────────────────


# ── 4. ASCII 시스템 구조도 ─────────────────────────────────────────


# ── 5. ASCII 데이터/에너지 플로우 ─────────────────────────────────────────


# ── 6. BT 연결 ─────────────────────────────────────────


# ── 7. n=6 EXACT 증거 종합 (Mk.I) ─────────────────────────────────────────



@D row_15_14 :: crispr-gene-editing [ok]
  x = "15"
  x = "DSB 절단 가닥 수"
  x = "2"
  n_6 = "phi"
  x = "2"
  x = "EXACT"


@D row_16_15 :: crispr-gene-editing [ok]
  x = "16"
  x = "SaCas9 PAM 길이"
  x = "6 nt"
  n_6 = "n"
  x = "6"
  x = "EXACT"


@D row_17_16 :: crispr-gene-editing [ok]
  x = "17"
  x = "Cas13 HEPN 도메인"
  x = "2"
  n_6 = "phi"
  x = "2"
  x = "EXACT"


@D row_18_17 :: crispr-gene-editing [ok]
  x = "18"
  x = "염기 편집 윈도우"
  x = "4~8 nt"
  n_6 = "tau~sigma-tau"
  x = "4~8"
  x = "EXACT"


@D row_19_18 :: crispr-gene-editing [ok]
  x = "19"
  x = "프라임 편집 구성요소"
  x = "3"
  n_6 = "n/phi"
  x = "3"
  x = "EXACT"


@D row_20_19 :: crispr-gene-editing [ok]
  x = "20"
  x = "Cas9 활성 부위 Mg2+"
  x = "2"
  n_6 = "phi"
  x = "2"
  x = "EXACT"

# ── 8. 한계 및 Mk.II 전환 동기 ─────────────────────────────────────────



@D b_2012_crispr_cas9_jinek_doudna_ch_0 :: crispr-gene-editing [ok]
  text = "2012: CRISPR-Cas9 최초 보고 (Jinek, Doudna, Charpentier)"


@D b_2013_cong_zhang_1 :: crispr-gene-editing [ok]
  text = "2013: 포유류 세포 편집 (Cong, Zhang)"


@D b_2016_base_editor_komor_liu_tau_4_2 :: crispr-gene-editing [ok]
  text = "2016: Base Editor (Komor, Liu) -- tau=4 편집 유형 중 3번째"


@D b_2019_prime_editor_anzalone_liu_n_3 :: crispr-gene-editing [ok]
  text = "2019: Prime Editor (Anzalone, Liu) -- n/phi=3 구성요소"


@D b_2020_doudna_charpentier_4 :: crispr-gene-editing [ok]
  text = "2020: 노벨 화학상 (Doudna, Charpentier)"


@D b_2023_casgevy_5 :: crispr-gene-editing [ok]
  text = "2023: Casgevy 최초 승인 (겸상적혈구/베타지중해빈혈)"


@D b_2025_6 :: crispr-gene-editing [ok]
  text = "2025: 다중 질환 임상 진입 (암, 유전병, 감염병)"


@D b_mk_ii_2025_2030_7 :: crispr-gene-editing [ok]
  text = "**--> Mk.II: 2025~2030 정밀 전달 시대**"

# ── 10. 검증 코드 (Python) ─────────────────────────────────────────


# ── 11. 요약 ─────────────────────────────────────────



@D row_exact_0 :: crispr-gene-editing [ok]
  x = "EXACT 일치"
  x = "20/20 (100%)"


@D row_bt_1 :: crispr-gene-editing [ok]
  x = "BT 연결"
  x = "BT-188, BT-193, BT-25"


@D row_carnot_2 :: crispr-gene-editing [ok]
  x = "Carnot 천장"
  x = "1-phi/sigma = 83.3%"


@D row_n_5_3 :: crispr-gene-editing [ok]
  x = "n=5 대조"
  x = "7개 중 6개 실패"


@D row_materials_baseline_0 :: crispr-gene-editing [ok]
  x = "materials-baseline"
  x = "🛸2"
  x = "🛸4"
  x = "+2"
  x = "[materials](../../materials/ceramics/ceramics.md)"


@D row_life_baseline_1 :: crispr-gene-editing [ok]
  x = "life-baseline"
  x = "🛸1"
  x = "🛸3"
  x = "+2"
  x = "[life](../genetics/genetics.md)"

# ── §4 STRUCT (시스템 구조도 ASCII) ─────────────────────────────────────────


# ── §5 FLOW (데이터/에너지 플로우) ─────────────────────────────────────────


# ── §6 EVOLVE (Mk.I~V 진화) ─────────────────────────────────────────


# ── §7 VERIFY (Python 검증) ─────────────────────────────────────────



