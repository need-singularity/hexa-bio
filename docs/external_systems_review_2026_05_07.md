# External systems review — AlphaFold 3 + scGPT 흡수 검토

조사일자: 2026-05-07
조사 트리거: 사용자 알림 (heisenberg.kr/scgpt + 알파폴드 노벨상 2024 + "토대가 된 시스템" + "흡수 할 수 있는 것 흡수")
대상: hexa-bio + .roadmap.quantum 와의 접점, 흡수 가능 idea/architecture

---

## 1. AlphaFold 3 (Google DeepMind)

### 1.1 핵심

- 2024 노벨화학상 (David Baker / Demis Hassabis / John Jumper)
- 단백질뿐 아니라 **단백질 + DNA + RNA + ligand + ion + modified residue** 통합 구조 예측
- Architecture: Evoformer (sequence/MSA feature processing) + diffusion-based structure generation + 분자 type 별 specialized modules
- Implementation: JAX + Haiku (Python 85% + C++ 14%)
- Input: JSON (sequences + seeds + molecule IDs), Output: 3D structure + confidence metrics
- Repo: `github.com/google-deepmind/alphafold3`

### 1.2 라이선스 / dependency

- **Code: CC BY-NC-SA 4.0** (Non-commercial)
- **Weights: AlphaFold 3 Model Parameters Terms of Use** — request form 필요, 재배포 금지
- Dependencies: JAX, Haiku, RDKit, HMMER, UniProt/BFD/PDB databases

### 1.3 hexa-bio 와 접점

**우리 시스템의 도메인 vs AlphaFold 3 의 도메인**:

| hexa-bio | AlphaFold 3 |
|----------|-------------|
| RIBOZYME (catalytic RNA) | RNA + ligand + 단백질 binding |
| VIROCAPSID (cage assembly) | 단백질 self-assembly (대형 capsid 까지 다룸) |
| NANOBOT (mechanical actuation) | (단백질 motor 일부 cover) |
| WEAVE (DNA folding) | DNA + structural motifs |
| QUANTUM (VQE molecular E) | (별도 axis — energy/electronic structure) |

**흡수 가능한 idea**:

1. **JSON-driven input contract** — 우리도 schema-validated input (e.g. `raw_77_*_v1`) 동등한 패턴. 차이는 우리 schema 가 **falsifier-attached** (registry row 형식). AlphaFold 3 의 input JSON 도 우리 schema 의 ribozyme/virocapsid input contract 와 형태 흡사. 흡수: 우리 input schema 가 직접 ML pipeline 의 input 으로 사용 가능 (cross-formal).
2. **Confidence metrics** — AlphaFold 의 pLDDT (per-residue) + PAE (pairwise alignment error) 같은 self-reported confidence. 우리 ribozyme/virocapsid 는 falsifier PASS/FAIL 만; **per-component confidence score** 추가 가능.
3. **Multi-modality** — AlphaFold 3 가 단백질 + RNA + DNA + ligand 통합. 우리 hexa-bio 는 RIBOZYME/WEAVE/VIROCAPSID 가 별도 axis. **cross-axis** 분자 (예: ribozyme-protein complex, capsid-RNA packaging) 를 다루려면 AlphaFold 3 출력을 input 으로 받는 wrapper 가 첫 발걸음.

**흡수 불가능한 부분 (라이선스/규모)**:

- code base + weight 직접 통합 = CC BY-NC-SA 4.0 (commercial 제약) + weight 재배포 금지. 우리는 외부 호출만.
- 학습 데이터 (UniProt/BFD/PDB) 규모 = 수백 GB. directly hosting 비효율.

**권장 접근**:

- **outbound consumer** 패턴 — hexa-bio 가 AlphaFold 3 output (structure + confidence) 을 input 으로 받는 wrapper. 사용자가 AlphaFold 3 별도 실행 → output JSON → hexa-bio 가 ribozyme/virocapsid contract 와 join.
- 우리는 **down-stream** (validation, kinetics, assembly) 계층에 집중.
- AlphaFold 3 자체 docker container 는 사용자 자체 설치 — 우리는 dep 추가 0.

---

## 2. scGPT (Bo Wang lab, U Toronto)

### 2.1 핵심

- single-cell transcriptomics foundation model (transformer-based)
- Pretrained on **33 million normal human cells** (whole-human flagship) + organ-specific (brain/blood/heart/lung/kidney) + pan-cancer checkpoint
- Tasks: cell annotation, cell embedding, integration, **perturbation prediction** (genome-wide CRISPR-style 유전자 KO 효과 예측), GRN inference
- 91.4% 첫-시도 정답 (제약사 신약 타겟 발굴 — heisenberg.kr 인용 출처는 paper benchmark)
- Repo: `github.com/bowang-lab/scGPT`

### 2.2 라이선스 / dependency

- **MIT License** — commercial OK
- Dependencies: scanpy + flash-attn (optional) + HuggingFace transformers
- Pretrained checkpoints 다운로드 가능 (HuggingFace / Drive)
- Python ≥3.7.13 + R ≥3.6.1

### 2.3 hexa-bio 와 접점

**우리 시스템의 도메인 vs scGPT 의 도메인**:

| hexa-bio | scGPT |
|----------|-------|
| RIBOZYME (catalytic RNA) — molecular design | mRNA expression at cell level |
| VIROCAPSID — capsid assembly | (cell-level virus host response 일부 cover) |
| NANOBOT — mechanical | (out of scope) |
| WEAVE — DNA folding | (out of scope) |
| QUANTUM — minimal-basis VQE | (out of scope) |

**흡수 가능한 idea**:

1. **Foundation model + fine-tune 패턴** — pretrained checkpoint 위에 task-specific fine-tune. 우리는 분자 design 마다 별도 audit/falsifier; scGPT 는 universal embedding + downstream head. **흡수 가능**: 우리 `_python_bridge/module/quantum_*` 의 wave function 도 universal representation, downstream head (energy / Pauli / VQE / scan 등) attach.
2. **Perturbation prediction → 신약 타겟 발굴** — 유전자 KO 효과 예측 = drug target identification. 우리 RIBOZYME C2 axis (FLT3-ITD AML 등) 는 정확히 같은 application 영역. **연계 가능**: scGPT 가 발굴한 target → 우리 ribozyme design (cleave that mRNA) → wet-lab synbio.
3. **Cell-level VQE** — 활성부위/단백질 fragment VQE (Phase C drug-target pocket) + scGPT 의 cell-context embedding 결합 = **context-aware quantum chemistry**. multi-scale (cell → protein → active-site VQE).

**구체 시너지 (drug discovery pipeline)**:

```
scGPT:                                 hexa-bio quantum:
  cell-level perturbation       →     drug target gene/protein
  → 91.4% top-1 target          →     active-site residue identification
                                →     QM/MM split
                                →     active-site VQE (Phase C)
                                →     ΔE_binding measurement
                                       (chem-acc 1.6 mHa OR spec-acc 1 µHa)
                                
hexa-bio ribozyme (R-axis):
                                →     ribozyme cleave target mRNA
                                       (C2 cells: AML / SCD / pan-cov / senolytic)
```

**흡수 불가능 부분**:

- 33M cell pretraining 자체는 hexa-bio 가 수행 안 함 (data + GPU 비현실).
- HuggingFace transformers + flash-attn dep = 큰 dep, raw#10 caveat 매우 큼.
- pretrained weight 다운로드 ≈ 수 GB.

**권장 접근**:

- **outbound consumer** + **read-only inference** — scGPT pretrained 를 사용자 별도 환경에서 실행, output (target gene/protein list + confidence) 을 hexa-bio ribozyme C2 input 으로 join.
- 우리 ribozyme R-axis 의 target mRNA 선택 시 **scGPT-recommended gene list** 를 evidence_paths 에 첨부.
- raw#10 caveat: scGPT 의 정확도 한계 (out-of-distribution gene combos 에서 traditional 통계 모델보다 못함) — 단일 source 의존 금지.

---

## 3. 통합 검토 — hexa-bio 진로 권장

### 3.1 즉시 가능한 흡수 (0-1 cycle)

1. **input contract 통일** — AlphaFold 3 output JSON / scGPT recommend gene list 를 우리 registry row schema 와 join. `raw_77_external_evidence_v1` 같은 boundary schema 신설.
2. **docs 추가** — 본 문서가 그 흡수 가능성 정리. cross-system reference 로 `.roadmap.quantum` / `.roadmap.ribozyme` 에 link.

### 3.2 medium 흡수 (1-3 cycle, 사용자 결정 영역)

3. **scGPT 1회 inference smoke** — 사용자 환경에 scGPT install + 하나의 cell type / perturbation 예측 실행 → 결과 paste 해서 우리 ribozyme C2 row 의 evidence_paths 에 첨부. raw#10: scGPT inference cost 비명시.
4. **AlphaFold 3 1회 prediction smoke** — 사용자 환경에 AlphaFold 3 docker 실행 + 우리 virocapsid T=1 STNV 같은 작은 capsid 1회 예측 → confidence + structure 출력 → registry row.

### 3.3 long-term (다 cycle, 큰 로드맵)

5. **drug-discovery pipeline integration** — scGPT (target discovery) + AlphaFold 3 (structure prediction) + hexa-bio quantum (active-site VQE) + hexa-bio ribozyme (silencing) — 4-stage pipeline, end-to-end drug candidate. 사용자 결정 + 다 cycle.
6. **Foundation model 의 quantum-substrate 활용** — scGPT 의 transformer 가 cell representation, hexa-bio 의 quantum 이 분자 representation. 두 representation 의 cross-attention 으로 cell-context-aware molecular VQE. 신규 연구 axis.

### 3.4 hexa-bio 의 차별화 (흡수보다 보강)

- **falsifier-driven** workflow — 우리 raw_77 schema 의 falsifier ID + threshold + action-on-fail 패턴은 AlphaFold/scGPT 와 분리. 우리 advantage.
- **cross-repo SSOT** + memory + cycle history = audit trail. ML model 의 bb로 단점 (output 만 있고 reproduction trail 없음) 을 보완.
- **stdlib-only Python** (raw#9) — ML 라이브러리 의존 최소화. 우리 quantum cycle 이 dep 0 / 작은 dep 으로 기능.

---

## 4. raw#10 honest C3

1. **scGPT 91.4%** 수치 출처 = heisenberg.kr 인용 (paper 직접 검증 미실시). bioRxiv 2023 paper benchmark dataset specifics 미파악. 후속 cycle 에서 paper 직접 검증 필요.
2. **AlphaFold 3 노벨상 2024** = AlphaFold 2 의 contribution 으로 (Hassabis/Jumper) — AlphaFold 3 자체가 노벨상 받은 게 아니라 그 lineage. 정확성 위해 명시.
3. **이 문서의 "흡수 가능" 분류** = 사용자 의도 해석 (코드 통합 vs idea 흡수). 본 review 는 idea + outbound consumer 패턴 위주. 코드 통합 (scGPT/AlphaFold 의 module 직접 import) 은 별도 cycle 의 사용자 결정.
4. **시너지 시나리오** (§3.3 drug-discovery pipeline) = 가능성 / 로드맵 layout 일 뿐. 실제 4-stage pipeline 작동 검증 = 별도 다 cycle 작업.

---

## 5. 다음 cycle 진입점

### 5.1 즉시 (사용자 결정 영역 외, 자동 가능)

- 본 review docs commit + push (이번 cycle).
- `.roadmap.quantum` + `.roadmap.ribozyme` 에 외부 시스템 reference 추가 (한 줄).

### 5.2 사용자 결정 영역

- scGPT install + 1회 inference smoke (drug target prediction)
- AlphaFold 3 install + 1회 structure prediction smoke (virocapsid T=1)
- Phase C drug-target pocket VQE (scGPT 의 target 사용 가능 시점부터)

cron `67cceec6` 자동 진행 — §5.1 완료 후 다음 cycle 자동 결정.
