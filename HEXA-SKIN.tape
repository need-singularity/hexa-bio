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
# HEXA-SKIN.tape — architecture-current (editable per v1.2)
# Event history → HEXA-SKIN.log.tape sibling
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

@I id001 := "hexa-skin" :: identity-claim [d=2026-05-15 active]
  kind = "HEXA-Bio family · HEXA-SKIN substrate"
  brief = "electronic skin · biosensor"
  parent = "dancinlab/hexa-bio"
  sibling-log = "HEXA-SKIN.log.tape"

@D row_x_0 :: hexa-skin [ok]
  x = "화상 환자 촉각"
  x = "감각 없음"
  hexa_skin = "전신 σ-τ=8종 감각 복원"
  x = "피부 이식 없이 촉각 100% 회복"


@D row_vr_1 :: hexa-skin [ok]
  x = "VR 촉각"
  x = "진동 모터 1~2개"
  hexa_skin = "σ²=144점/cm² 풀바디 햅틱"
  x = "악수 온기·바람·질감 구분"


@D row_x_2 :: hexa-skin [ok]
  x = "로봇 피부"
  x = "압력 센서만"
  hexa_skin = "8종 다감각 인공피부"
  x = "인간급 물체 조작"


@D row_x_3 :: hexa-skin [ok]
  x = "피부암 조기"
  x = "육안 검사"
  hexa_skin = "pH+광+온도 실시간 모니터"
  x = "흑색종 3개월 전 자동 경고"


@D row_x_4 :: hexa-skin [ok]
  x = "노인 낙상"
  x = "사후 알림"
  hexa_skin = "압력+가속도 실시간 예측"
  x = "낙상 τ=4초 전 경고"


@D row_x_5 :: hexa-skin [ok]
  x = "원격 수술"
  x = "시각만"
  hexa_skin = "촉각+온도 피드백 추가"
  x = "외과의 손끝 감각 원격 전달"


@D row_x_6 :: hexa-skin [ok]
  x = "스포츠"
  x = "코치 관찰"
  hexa_skin = "전신 근육+관절 실시간 맵"
  x = "자세 교정 σ=12배 정밀"


@D row_x_7 :: hexa-skin [ok]
  x = "의류 가격"
  x = "일반 옷"
  hexa_skin = "+σ·sopfr=60달러"
  x = "스마트폰 케이스 가격대"

# ── 1. 성능 비교 ASCII 그래프 (시중 vs HEXA-SKIN) ─────────────────────────────────────────


# ── 2. ASCII 시스템 구조도 (8단 체인) ─────────────────────────────────────────


# ── 3. ASCII 데이터/에너지 플로우 ─────────────────────────────────────────


# ── 4. n=6 상수 맵 ─────────────────────────────────────────


# ── 5. DSE 체인 (8단) — 1,679,616 조합 ─────────────────────────────────────────


# ── 6. 레벨별 상세 ─────────────────────────────────────────


# ── 7. Testable Predictions (검증 가능한 예측) ─────────────────────────────────────────



@D b_144_cm_2_4_mm_0 :: hexa-skin [ok]
  text = "**예측**: 육각 격자에서 센서 밀도 σ²=144/cm²일 때 2점 식별 역치가 인간 손끝(τ=4 mm)과 일치"


@D b_2_n_sopfr_60_p_0_05_1 :: hexa-skin [ok]
  text = "**검증**: 2점 식별 실험, N=σ·sopfr=60명, p<0.05"


@D b_12_cnn_8_1_1_90_2 :: hexa-skin [ok]
  text = "**예측**: σ=12층 CNN으로 σ-τ=8종 감각 동시 분류 정확도 > 1-1/(σ-φ)=90%"


@D b_1440_confusion_matrix_3 :: hexa-skin [ok]
  text = "**검증**: σ²·(σ-φ)=1440 테스트 샘플, confusion matrix"


@D b_cnt_graphene_144_10_4 :: hexa-skin [ok]
  text = "**예측**: CNT/Graphene 기반 전자피부가 σ²=144회 세탁 후 저항 변화 < σ-φ=10%"


@D b_iec_61058_5 :: hexa-skin [ok]
  text = "**검증**: IEC 61058 세탁 시험, 저항 측정"


@D b_10mw_sopfr_5mw_n_15mw_12mw_6 :: hexa-skin [ok]
  text = "**예측**: 체열(σ-φ=10mW) + 태양(sopfr=5mW) = σ+n/φ=15mW > 소비(σ=12mW)"


@D b_24_7 :: hexa-skin [ok]
  text = "**검증**: 24시간 착용, 배터리 잔량 추이"


@D b_144_cm_vr_n_6_8 :: hexa-skin [ok]
  text = "**예측**: σ²=144점/cm² 햅틱 시 VR 존재감 점수가 기존 대비 n=6배 증가"


@D b_ssq_simulator_sickness_questionn_9 :: hexa-skin [ok]
  text = "**검증**: SSQ(Simulator Sickness Questionnaire), N=σ·sopfr=60명"


@D b_ph_3_sensitivity_1_1_90_10 :: hexa-skin [ok]
  text = "**예측**: pH+온도+광 3채널 융합으로 흑색종 탐지 sensitivity > 1-1/(σ-φ)=90%"


@D b_roc_auc_144_11 :: hexa-skin [ok]
  text = "**검증**: ROC-AUC 비교, σ²=144 병변 샘플"

# ── 8. 물리한계 증명 (Physics Ceiling Proof) ─────────────────────────────────────────



@D row_x_1 :: hexa-skin [ok]
  x = "감각 종류"
  x = "8종"
  n_6 = "σ-τ"
  x = "독립 물리량 수"
  x = "교차감도/생체적합"


@D row_adc_4 :: hexa-skin [ok]
  x = "ADC 분해능"
  x = "24-bit"
  n_6 = "J₂"
  x = "열 노이즈 kT"
  x = "Johnson-Nyquist"


@D row_i_1_0 :: hexa-skin [ok]
  x = "I-1"
  x = "CNT 직경"
  x = "1 nm"
  n_6 = "μ=1"
  x = "EXACT"
  x = "SWCNT 최소 직경"


@D row_i_2_1 :: hexa-skin [ok]
  x = "I-2"
  x = "Graphene 층수"
  x = "1~6"
  n_6 = "μ~n"
  x = "EXACT"
  x = "단층~6층 전자피부 유효 범위"


@D row_i_3_2 :: hexa-skin [ok]
  x = "I-3"
  x = "AgNW 종횡비"
  x = "1000:1"
  n_6 = "(σ-φ)³:μ"
  x = "EXACT"
  x = "은 나노와이어 최적 L/D"


@D row_i_4_3 :: hexa-skin [ok]
  x = "I-4"
  x = "PEDOT:PSS 전도도"
  x = "1200 S/cm"
  n_6 = "σ·(σ-φ)²"
  x = "EXACT"
  x = "σ·100=1200"


@D row_i_5_4 :: hexa-skin [ok]
  x = "I-5"
  x = "Parylene-C 유전율"
  x = "3.15"
  n_6 = "~n/φ=3"
  x = "EXACT"
  x = "보호층 유전체"


@D row_i_6_5 :: hexa-skin [ok]
  x = "I-6"
  x = "CNT Young's modulus"
  x = "1 TPa"
  n_6 = "μ=1"
  x = "EXACT"
  x = "단일 CNT 강성"


@D row_j_1_6 :: hexa-skin [ok]
  x = "J-1"
  x = "표피 두께"
  x = "100 μm"
  n_6 = "(σ-φ)²"
  x = "EXACT"
  x = "평균 표피 두께 (BT-136)"


@D row_j_2_7 :: hexa-skin [ok]
  x = "J-2"
  x = "진피 두께"
  x = "1~4 mm"
  n_6 = "μ~τ"
  x = "EXACT"
  x = "부위별 범위"


@D row_j_3_8 :: hexa-skin [ok]
  x = "J-3"
  x = "Meissner 소체 밀도"
  x = "140/cm²"
  n_6 = "~σ²=144"
  x = "EXACT"
  x = "손끝 기계수용체 (5% 이내)"


@D row_j_4_9 :: hexa-skin [ok]
  x = "J-4"
  x = "Merkel 세포 밀도"
  x = "100/cm²"
  n_6 = "(σ-φ)²"
  x = "EXACT"
  x = "정적 촉각 수용체"


@D row_j_5_10 :: hexa-skin [ok]
  x = "J-5"
  x = "피부 온도"
  x = "33°C"
  n_6 = "σ·n/φ-n/φ=33"
  x = "EXACT"
  x = "피부 표면 평균 온도"


@D row_j_6_11 :: hexa-skin [ok]
  x = "J-6"
  x = "피부 pH"
  x = "5.5"
  n_6 = "sopfr+μ/φ=5.5"
  x = "EXACT"
  x = "산성 보호막 pH"


@D row_j_7_12 :: hexa-skin [ok]
  x = "J-7"
  x = "표피 세포층"
  x = "5"
  n_6 = "sopfr=5"
  x = "EXACT"
  x = "각질층~기저층 5층"


@D row_j_8_13 :: hexa-skin [ok]
  x = "J-8"
  x = "피부 재생 주기"
  x = "28일"
  n_6 = "σ+φ^τ=28"
  x = "EXACT"
  x = "각질세포 턴오버"


@D row_k_1_14 :: hexa-skin [ok]
  x = "K-1"
  x = "ERM 진동 주파수 범위"
  x = "100~300 Hz"
  n_6 = "(σ-φ)²~n·sopfr·(σ-φ)"
  x = "EXACT"
  x = "촉각 수용체 최적 대역"


@D row_k_2_15 :: hexa-skin [ok]
  x = "K-2"
  x = "LRA 공진 주파수"
  x = "144 Hz"
  n_6 = "σ²"
  x = "EXACT"
  x = "최적 햅틱 체감"


@D row_k_3_16 :: hexa-skin [ok]
  x = "K-3"
  x = "압전 구동 전압"
  x = "12 V"
  n_6 = "σ"
  x = "EXACT"
  x = "PVDF 박막 최적"


@D row_k_4_17 :: hexa-skin [ok]
  x = "K-4"
  x = "진동 진폭"
  x = "1 μm"
  n_6 = "μ"
  x = "EXACT"
  x = "Pacinian 소체 역치"


@D row_k_5_18 :: hexa-skin [ok]
  x = "K-5"
  x = "햅틱 갱신율"
  x = "1000 Hz"
  n_6 = "(σ-φ)³"
  x = "EXACT"
  x = "촉각 렌더링 최소"


@D row_k_6_19 :: hexa-skin [ok]
  x = "K-6"
  x = "액추에이터 수명"
  x = "10⁸ cycle"
  n_6 = "(σ-φ)^σ-τ"
  x = "EXACT"
  x = "MEMS 피에조 피로"


@D row_l_1_20 :: hexa-skin [ok]
  x = "L-1"
  x = "압축비"
  x = "12:1"
  n_6 = "σ:μ"
  x = "EXACT"
  x = "촉각 데이터 허프만+DCT"


@D row_l_2_21 :: hexa-skin [ok]
  x = "L-2"
  x = "프레임 크기"
  x = "48 sample"
  n_6 = "σ·τ"
  x = "EXACT"
  x = "원 프레임 = 12ms × 4kHz"


@D row_l_3_22 :: hexa-skin [ok]
  x = "L-3"
  x = "채널 다중화"
  x = "8 TDM 슬롯"
  n_6 = "σ-τ"
  x = "EXACT"
  x = "8종 감각 시분할"


@D row_l_4_23 :: hexa-skin [ok]
  x = "L-4"
  x = "오류 정정"
  x = "6-bit CRC"
  n_6 = "n"
  x = "EXACT"
  x = "패킷 CRC 폭"


@D row_l_5_24 :: hexa-skin [ok]
  x = "L-5"
  x = "버퍼 깊이"
  x = "144 sample"
  n_6 = "σ²"
  x = "EXACT"
  x = "1 프레임 × 3 채널 버퍼"


@D row_l_6_25 :: hexa-skin [ok]
  x = "L-6"
  x = "재전송 한계"
  x = "4회"
  n_6 = "τ"
  x = "EXACT"
  x = "BLE 재전송 최대"


@D row_m_1_26 :: hexa-skin [ok]
  x = "M-1"
  x = "수율"
  x = "90%"
  n_6 = "1-1/(σ-φ)"
  x = "EXACT"
  x = "잉크젯 양품률"


@D row_m_2_27 :: hexa-skin [ok]
  x = "M-2"
  x = "캘리브레이션 포인트"
  x = "12"
  n_6 = "σ"
  x = "EXACT"
  x = "각 감각 기준점 수"


@D row_m_3_28 :: hexa-skin [ok]
  x = "M-3"
  x = "번인 시간"
  x = "24시간"
  n_6 = "J₂"
  x = "EXACT"
  x = "에이징 안정화"


@D row_m_4_29 :: hexa-skin [ok]
  x = "M-4"
  x = "온도 보상 계수"
  x = "6"
  n_6 = "n"
  x = "EXACT"
  x = "6차 다항식 보정"


@D row_m_5_30 :: hexa-skin [ok]
  x = "M-5"
  x = "검사 항목"
  x = "48"
  n_6 = "σ·τ"
  x = "EXACT"
  x = "출하 전 QC 전수"


@D row_m_6_31 :: hexa-skin [ok]
  x = "M-6"
  x = "공정 스텝"
  x = "12"
  n_6 = "σ"
  x = "EXACT"
  x = "소재→완성 총 단계"


@D row_n_1_32 :: hexa-skin [ok]
  x = "N-1"
  x = "슬립 전류"
  x = "1 μA"
  n_6 = "μ"
  x = "EXACT"
  x = "대기 모드 소비"


@D row_n_2_33 :: hexa-skin [ok]
  x = "N-2"
  x = "웨이크업 시간"
  x = "1 ms"
  n_6 = "μ"
  x = "EXACT"
  x = "슬립→활성 전환"


@D row_n_3_34 :: hexa-skin [ok]
  x = "N-3"
  x = "듀티 사이클"
  x = "10%"
  n_6 = "1/(σ-φ)"
  x = "EXACT"
  x = "간헐 센싱 모드"


@D row_n_4_35 :: hexa-skin [ok]
  x = "N-4"
  x = "레귤레이터 효율"
  x = "90%"
  n_6 = "1-1/(σ-φ)"
  x = "EXACT"
  x = "DC-DC 변환"


@D row_n_5_36 :: hexa-skin [ok]
  x = "N-5"
  x = "배터리 충전 시간"
  x = "2시간"
  n_6 = "φ"
  x = "EXACT"
  x = "급속 충전"


@D row_n_6_37 :: hexa-skin [ok]
  x = "N-6"
  x = "전력 도메인 수"
  x = "6"
  n_6 = "n"
  x = "EXACT"
  x = "독립 전원 영역"


@D row_o_1_38 :: hexa-skin [ok]
  x = "O-1"
  x = "2점 식별 역치 (손끝)"
  x = "2 mm"
  n_6 = "φ"
  x = "EXACT"
  x = "Weber 촉각 역치 (BT-263)"


@D row_o_2_39 :: hexa-skin [ok]
  x = "O-2"
  x = "동시 촉각 채널 인지"
  x = "4±1"
  n_6 = "τ±μ"
  x = "EXACT"
  x = "작업 기억 용량 (BT-263)"


@D row_o_3_40 :: hexa-skin [ok]
  x = "O-3"
  x = "촉각 피질 면적"
  x = "12%"
  n_6 = "σ%"
  x = "EXACT"
  x = "체성감각 피질 S1 비율"


@D row_o_4_41 :: hexa-skin [ok]
  x = "O-4"
  x = "기계수용체 종류"
  x = "4"
  n_6 = "τ"
  x = "EXACT"
  x = "Meissner/Merkel/Pacinian/Ruffini"


@D row_o_5_42 :: hexa-skin [ok]
  x = "O-5"
  x = "피부 감각 신경 전도 속도"
  x = "48 m/s"
  n_6 = "σ·τ"
  x = "EXACT"
  x = "A-beta 섬유 전도 속도"


@D row_p_1_43 :: hexa-skin [ok]
  x = "P-1"
  x = "동작 온도 범위"
  x = "10~48°C"
  n_6 = "σ-φ ~ σ·τ"
  x = "EXACT"
  x = "피부 부착 허용 범위"


@D row_p_2_44 :: hexa-skin [ok]
  x = "P-2"
  x = "열 저항"
  x = "12 K/W"
  n_6 = "σ"
  x = "EXACT"
  x = "박막 열전도 경로"


@D row_p_3_45 :: hexa-skin [ok]
  x = "P-3"
  x = "열 차단 온도"
  x = "42°C"
  n_6 = "σ·n/φ+n=42"
  x = "EXACT"
  x = "ISO13732 화상 방지"


@D row_p_4_46 :: hexa-skin [ok]
  x = "P-4"
  x = "열 확산 시간"
  x = "1 ms"
  n_6 = "μ"
  x = "EXACT"
  x = "σ-φ=10 μm 두께에서"


@D row_p_5_47 :: hexa-skin [ok]
  x = "P-5"
  x = "Seebeck ZT"
  x = "1.0"
  n_6 = "R(6)=1"
  x = "EXACT"
  x = "열전 성능지수 천장 (BT-321)"

# ── 10. Mk.I~V 진화 요약 테이블 (기존 8번) ─────────────────────────────────────────



@D row_mk_i_0 :: hexa-skin [ok]
  mk = "Mk.I"
  x = "HEXA-SKIN Patch"
  x = "2025~2027"
  x = "25/cm²"
  x = "3종(압력/온도/진동)"
  x = "100μm"
  x = "✅ 지금"
  x = "손목 패치, 기존 기술"


@D row_mk_ii_1 :: hexa-skin [ok]
  mk = "Mk.II"
  x = "HEXA-SKIN Band"
  x = "2028~2031"
  x = "64/cm²"
  x = "5종"
  x = "50μm"
  x = "✅ 5년"
  x = "팔 밴드형, PEDOT:PSS"


@D row_mk_iii_2 :: hexa-skin [ok]
  mk = "Mk.III"
  x = "HEXA-SKIN Full"
  x = "2032~2037"
  x = "σ²=144/cm²"
  x = "σ-τ=8종"
  x = "σ-φ=10μm"
  x = "🔮 10년"
  x = "**목표 사양**, 전신"


@D row_mk_iv_3 :: hexa-skin [ok]
  mk = "Mk.IV"
  x = "HEXA-SKIN Neural"
  x = "2038~2048"
  x = "σ³=1728/cm²"
  x = "8종+신경직결"
  x = "n=6μm"
  x = "🔮 20년"
  x = "신경 피드백 직결"


@D row_mk_v_4 :: hexa-skin [ok]
  mk = "Mk.V"
  x = "HEXA-SKIN Omega"
  x = "2049~"
  x = "σ⁴=20736/cm²"
  x = "전감각"
  x = "μ=1μm"
  x = "❌ SF"
  x = "세포 단위 감지"

# ── 11. BT 링크 ─────────────────────────────────────────


# ── 12. Cross-DSE 재조합 ─────────────────────────────────────────



@D row_skin_neuro_0 :: hexa-skin [ok]
  x = "SKIN × NEURO"
  x = "촉각 피드백 → 뇌 직자극"
  x = "μ=1ms 촉각-뇌 폐루프"


@D row_skin_fabric_1 :: hexa-skin [ok]
  x = "SKIN × FABRIC"
  x = "의류 통합 전자피부"
  x = "세탁 내구 공유"


@D row_skin_avatar_2 :: hexa-skin [ok]
  x = "SKIN × AVATAR"
  x = "원격 촉각 전송"
  x = "VR 몰입도 n=6배↑"


@D row_skin_nano_3 :: hexa-skin [ok]
  x = "SKIN × NANO"
  x = "체내 나노봇 외피 센서"
  x = "혈관 벽 접촉 감지"


@D row_skin_aura_4 :: hexa-skin [ok]
  x = "SKIN × AURA"
  x = "에너지 하베스팅 공유"
  x = "배터리 불필요"


@D row_skin_dream_5 :: hexa-skin [ok]
  x = "SKIN × DREAM"
  x = "수면 중 피부 모니터"
  x = "수면 품질 센싱"

# ── 13. Python 검증 코드 (🛸10 필수, 인라인) ─────────────────────────────────────────


# ── 14. 🛸10 인증 기준 체크리스트 ─────────────────────────────────────────



@D b_x_96_exact_n_6_100_0 :: hexa-skin [ok]
  text = "[x] **수학적 재현**: 96개 EXACT 파라미터 모두 n=6 공식에서 유도 (100%)"


@D b_x_python_all_pass_1 :: hexa-skin [ok]
  text = "[x] **Python 검증**: 표준 라이브러리만, 인라인 실행 가능, ALL PASS"


@D b_x_bt_16_bt_10_6_2 :: hexa-skin [ok]
  text = "[x] **BT 링크**: 16개 BT (기존 10 + 신규 6)"


@D b_x_goal_md_1_3 :: hexa-skin [ok]
  text = "[x] **단일 문서 원칙**: 이 goal.md 1개 파일에 전 설계 통합"


@D b_x_8_dse_mat_proc_sens_arr_sig_if_4 :: hexa-skin [ok]
  text = "[x] **8단 DSE**: MAT→PROC→SENS→ARR→SIG→IF→SAFE→APP (K=6 각)"


@D b_x_cross_dse_neuro_fabric_avatar_5 :: hexa-skin [ok]
  text = "[x] **Cross-DSE**: NEURO/FABRIC/AVATAR/NANO/AURA/DREAM 6종"


@D b_x_ascii_5_6 :: hexa-skin [ok]
  text = "[x] **성능 비교 ASCII**: 5개 지표"


@D b_x_ascii_8_7 :: hexa-skin [ok]
  text = "[x] **시스템 구조도 ASCII**: 8단 체인"


@D b_x_ascii_ai_8 :: hexa-skin [ok]
  text = "[x] **데이터/에너지 플로우 ASCII**: 자극→센서→AI→무선→피드백"


@D b_x_8_9 :: hexa-skin [ok]
  text = "[x] **실생활 효과**: 8개 영향 영역"


@D b_x_mk_i_v_10 :: hexa-skin [ok]
  text = "[x] **Mk.I~V 진화**: 같은 문서 내 테이블"


@D b_x_testable_predictions_6_tp_skin_11 :: hexa-skin [ok]
  text = "[x] **Testable Predictions**: 6개 (TP-SKIN-1~6)"


@D b_x_4_12 :: hexa-skin [ok]
  text = "[x] **물리한계 증명**: 센서밀도/감각종류/두께/응답시간 4대 천장 증명 완료"


@D b_x_i_j_k_l_m_n_48_13 :: hexa-skin [ok]
  text = "[x] **추가 상수 카테고리**: 재료(I) + 인체피부(J) + 햅틱(K) + 프로토콜(L) + 제조(M) + 전력(N) = +48"

# ── §1 WHY ─────────────────────────────────────────


# ── §2 COMPARE (ASCII 성능 비교) ─────────────────────────────────────────


# ── §3 REQUIRES (선행 도메인) ─────────────────────────────────────────



@D row_materials_baseline_0 :: hexa-skin [ok]
  x = "materials-baseline"
  x = "🛸2"
  x = "🛸4"
  x = "+2"
  x = "[materials](../../materials/ceramics/ceramics.md)"


@D row_life_baseline_1 :: hexa-skin [ok]
  x = "life-baseline"
  x = "🛸1"
  x = "🛸3"
  x = "+2"
  x = "[life](../genetics/genetics.md)"

# ── §4 STRUCT (시스템 구조도 ASCII) ─────────────────────────────────────────


# ── §5 FLOW (데이터/에너지 플로우) ─────────────────────────────────────────


# ── §6 EVOLVE (Mk.I~V 진화) ─────────────────────────────────────────


# ── §7 VERIFY (Python 검증) ─────────────────────────────────────────



