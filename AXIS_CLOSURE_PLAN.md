# AXIS_CLOSURE_PLAN — 5축 100% closure 로드맵

> hexa-bio 의 **5-axis** (QUANTUM / WEAVE / NANOBOT / RIBOZYME / VIROCAPSID;
> count locked — `.roadmap.axis_expansion_decision_2026_05_08`) 중 현재
> **weave 만 v1.x 스코프에서 100% closure** 닫혀 있다. 나머지 4축의 잔여
> gate / deadline / owner / 시퀀싱을 정리한다.
>
> **작성**: 2026-05-12 · **SSOT**: per-axis `.roadmap.*` sister files +
> `.roadmap.hexa_bio` (cross-cutting) + `CHANGELOG.md` `[Unreleased]`
> · **MVP gate**: 2026-07-28 (`.roadmap.hexa_bio §A.4`)
>
> **honest C3 (raw#10)**: 본 문서의 "100% closure" 는 *in-silico /
> formalism / infrastructure* 스코프 한정 — σ(6)=12 STRUCTURAL-EXACT +
> Bayesian audit decisive + output schema lock + C2 4/4 + falsifier
> preregister 전부 PASS. **therapeutic / clinical / regulatory / efficacy
> 와는 무관** (C3+ = out-of-repo, cross-cutting Require R6). full
> lean4-backed Π¹₁-CA₀ cert 는 v1.x 전체에서 MVP-caveat disclosure
> surrogate 로 처리되고 GATE-26-2 → v2.0.0 으로 track된다.

---

## §0 "axis 100% closure" 정의 (weave 가 만족한 기준 = 다른 4축의 목표)

| # | 기준 | weave 가 닫은 방식 |
|---|------|---------------------|
| 1 | **σ(6)=12 STRUCTURAL-EXACT** (CANDIDATE 아님) | T=1 cage vertex-count Bayesian audit posterior 0.9668 (n=34 corpus) |
| 2 | **핵심 numerical sandbox PASS 6/6** | F-TP5-b — `weave_compose()` end-to-end MVP, P=10×N=50=500 trial rows |
| 3 | **lean4 mechanical layer sorry-free** | sorry count = 0 (W5 milestone) |
| 4 | **output schema lock + row conformance** | `weave/spec/composition_output_v1.schema.json` + draft-07 validator (W-R1 / C0e) |
| 5 | **C2 4/4** (4 disease class × in-silico 후보 1개 + verification) | `raw_77_c2_weave_{aml,scd,pancov,senolytic}_v1` |
| 6 | **falsifier preregister 전부 PASS** (v1.x 스코프) | 12/12 (9 closure + 3 cycle 7-9 additions; C0c/C0d = user-discretion PASS) |
| 7 | (해당 시) **external inter-rater / corpus 충분조건** | weave 는 해당 없음 (CHI2 n=1 은 external-lit dep → DEFERRED, closure 차단 아님) |

> weave 잔여 (closure 비차단): GATE-26-2 full lean4 cert → v2.0.0; CHI2 sample
> n 1→5 (external 출판물 dep); Zenodo deposit (user-gated). 즉 **weave 는
> v1.x closure-grade 완료**, 위 항목은 v2.0.0 stretch.

---

## §1 현재 상태 스냅샷 (2026-05-12)

| Axis | Role | σ(6)=12 | Bayesian audit | output schema | C2 | 종합 |
|------|------|---------|----------------|---------------|----|----|
| **weave** | composition | ✅ STRUCTURAL-EXACT (T=1, post 0.9668) | F-VIROCAPSID-2 n=34 RESOLVED (cycle 22) | ✅ `composition_output_v1` lock | 4/4 | **✅ 100% closure (v1.x)** |
| **virocapsid** | assembly | ✅ STRUCTURAL-EXACT (T=1 corpus n=10 post 1.0 / log10_BF 16.63 · multi-T T=3/T=4 yield ≥0.85) | ✅ decisive (PDB corpus + calibration) | ⚠️ `cage_output_v1` LANDED, **lock 미완** (GATE-26-V-R1 / C5) | 4/4 | **🟡 ~90% — schema lock + full-corpus 잔여** |
| **nanobot** | actuation | 🟡 STRUCTURAL-EXACT-**CANDIDATE** (12-vertex) | 🟡 n=60 curated log10_BF 13.65 decisive, 단 canonical n=30 은 51% match (STRUCTURAL-APPROXIMATE); **inter-rater 미완** | ⚠️ `actuator_output_v1` v2 emission 미완 + L6 handoff schema v0 (lock 미완) | 4/4 | **🟡 ~70% — inter-rater + schema 잔여** |
| **ribozyme** | catalysis | 🟡 STRUCTURAL-EXACT-**CANDIDATE** (12-nt) | 🟡 F-RB-2 n=30 log_bf 79.74 PASS, 단 **PENDING INTER-RATER** | ⚠️ `ribozyme_output_v1` structure_2d **stub allowance** (MFE solver inline port 미완) | 4/4 | **🟡 ~75% — inter-rater + MFE port 잔여 (가장 가까움)** |
| **quantum** | computation | 🟡 VERIFIED (H₂ 6-Pauli / LiH path) — pocket-scale 미확장 | F-Q-1…5 PASS · F-Q-EXT-1…6 PASS | (n/a — `raw_77_quantum_*_v1` witness 스키마들) | (n/a — 4 bio axis 만 C2) | **🔴 ~55% — F-Q-6 pocket VQE OPEN (USER-GATED) + L3/L4 ladder** |

---

## §2 시퀀싱 — 닫는 순서 (가까운 것부터)

1. **RIBOZYME** — inter-rater 1건 (κ ≥ 0.6, ≥2 human raters) 만 닫으면 CANDIDATE → EXACT. + MFE solver inline port.
2. **NANOBOT** — ribozyme 와 sister 인 extended-corpus inter-rater 를 preregister + 실행, + cuboctahedron dual-skeleton (07-28) + schema v2 / L6 handoff lock.
3. **VIROCAPSID** — σ(6) 는 이미 STRUCTURAL-EXACT (closure-grade). 잔여 = C5 schema lock (07-28, 단기) + C3b 전체 corpus n≥100 + posterior ≥0.95 (long pole, cycle 28+) + F-VIROCAPSID-1-c/-d 독립축.
4. **QUANTUM** — long pole. **F-Q-6 (drug-target pocket VQE) 가 USER-GATED** — target system + pocket residue + ligand library 선정이 선행 필요. 그 다음 Phase C → Phase D (`.roadmap.novel_drugs`) → L3/L4 ladder.

> 병렬화 가능: 1·2 의 inter-rater 는 같은 인적 자원으로 한 번에; 3 의 C5
> schema lock 은 코드 작업이라 1·2 와 독립; 4 의 target 선정은 user
> decision 대기 (그 동안 Phase 2 hexa-native port + F-Q-EXT-7b alt-path 진행 가능).

---

## §3 RIBOZYME — catalysis (🟡 ~75%, 가장 가까움)

**Gate to close (CANDIDATE → EXACT)**:

| Gate | 내용 | Deadline | Owner | Status |
|------|------|----------|-------|--------|
| **G26-RB-1** | F-RB-2 inter-rater — n=30 corpus 의 per-axis match 판정을 ≥2 human rater 가 독립 채점, Cohen's κ ≥ 0.6 | **2026-06-15** | human raters (user 또는 위임) | ⬜ schema landed, rater 대기 |
| C0c | F-RB-2 n=30 Bayesian corpus 공식 closure (log_bf 79.74 이미 PASS, inter-rater 가 마지막 조건) | 2026-09-28 | — | 🟡 PASS PENDING INTER-RATER |
| G26-RB-2 | J₂=24 reaction-coordinate quotient decision — branch-lock 후 exec | branch-lock 06-15 / exec 09-28 | hexa-bio session | ⬜ |
| G26-RB-3 | C2 DoD uplift — component (2) structure prediction 을 stub→inline MFE (Nussinov/Zuker) + component (3) off-target screen 를 stub→실 host-transcriptome Hamming pool | 2026-09-28 | hexa-bio session | ⬜ partial-stub |
| R-R1 | `ribozyme/spec/ribozyme_output_v1.schema.json` — `structure_2d.dot_bracket` stub allowance 를 MFE solver inline port 로 제거 | cycle-26 stretch | hexa-bio session | 🟡 stub-allowed |

**잔여 작업 요약**:
- [ ] **inter-rater 실행** (G26-RB-1) — 가장 중요. 이거 하나로 σ(6)=12 STRUCTURAL-EXACT-CANDIDATE → STRUCTURAL-EXACT.
- [ ] `ribozyme_kinetics_simulation.py` 또는 신규 `ribozyme_mfe.py` 에 Nussinov-Zuker MFE 인라인 포트 → `structure_2d` stub 제거 (R-R1 / G26-RB-3).
- [ ] off-target screen 실 구현 (WEAVE Π^p_2 verifier v2 패턴 차용).
- [ ] J₂=24 quotient 결정 (G26-RB-2) — 현재 "deferred to stretch"; branch-lock 으로 in-scope/out-of-scope 확정.
- 비차단: falsifier count 5 → 12 (stretch); CHI2 n 30 (이미 PASS-MARGINAL 초과).

**닫힘 조건**: G26-RB-1 inter-rater κ ≥ 0.6 PASS + R-R1 stub 제거 + C2 4/4 (이미) → ribozyme v1.x closure-grade.

---

## §4 NANOBOT — actuation (🟡 ~70%)

**Gate to close (APPROXIMATE/CANDIDATE → EXACT)**:

| Gate | 내용 | Deadline | Owner | Status |
|------|------|----------|-------|--------|
| **G26-NB-EXT** | F-NB-2 extended-corpus inter-rater — n=60 curated dynamic-nano-machine corpus 의 axis-match 채점을 ≥2 external rater 가 독립 검증 (ribozyme G26-RB-1 의 sister) | **미preregister — 신규 gate 필요** | human raters | ⬜ not yet preregistered |
| C0c (ext) | F-NB-2-b ensemble drift — n=60 log10_BF ≥ 3.0 | 2026-09-28 (cycle 27) | — | ✅ **DECISIVE PASS** (log_bf 13.65, posterior 1.0) |
| F-NB-2-c | textbook-vs-experimental stratum bias ≤ 1 Jeffreys band | 2026-09-28 | hexa-bio session | ⬜ pending |
| F-NB-2-n6-decorative | n6-strip ablation \|Δlog_bf\| ≥ 0.5 | — | ✅ **PASS decisive** (Δ ≫ 0.5) |
| **C0d** | F-NB-4-cuboctahedron dual-skeleton PASS — `nanobot_actuation_simulation.py --skeleton cuboctahedron` (12-vertex, σ=12/τ=4/J₂=24 보존, work ≥10 kT, n_cycles ≥2500 no-collapse) | **2026-07-28** | hexa-bio session | ⬜ |
| N-R1 | `actuator_output_v1.schema.json` v2 emission — `nanobot_actuation_simulation.py` 를 확장해 `vertex_decorations`(12) + `pose_canonical_form`(rep pose 0..23, orbit 24) + `state_cycle`(4×4 rate matrix) + `binding_affinity` emit (v1 은 speedup factor 만) | cycle 26 | hexa-bio session | ⬜ v1 only |
| N-R2 | `handoff_l6_emission_v0.schema.json` lock — `emission_blocked_until_schema_lock=true` 해제 (v0 → v1) | cycle 26+ | hexa-bio session | 🟡 v0, blocked |

**잔여 작업 요약**:
- [ ] **G26-NB-EXT inter-rater gate 를 preregister + 실행** — `nanobot/spec/bayesian_audit_v2.schema.json` 에 inter-rater sub-clause 추가, ribozyme 와 같은 rater 풀로 일괄. 이게 STRUCTURAL-EXACT-CANDIDATE → STRUCTURAL-EXACT 의 마지막 조건.
- [ ] F-NB-2-c stratum-bias sub-clause 실행 (textbook vs experimental ≤ 1 Jeffreys band).
- [ ] cuboctahedron dual-skeleton 재실행 (C0d, 07-28).
- [ ] `actuator_output_v1` v2 emit-path + L6 handoff schema v0 → v1 lock (N-R1 / N-R2).
- 비차단: falsifier count 5 → 12 (stretch); wet-lab integration + IP/contract → cycle 30+.

**닫힘 조건**: G26-NB-EXT inter-rater PASS + C0d cuboctahedron PASS + N-R1 v2 emit + N-R2 schema lock + C2 4/4 (이미) → nanobot v1.x closure-grade. (단, parent F-NB-2 의 canonical n=30 이 51% match 라 "curated-corpus 조건부 STRUCTURAL-EXACT" 라는 honest disclosure 가 영구히 붙음.)

---

## §5 VIROCAPSID — assembly (🟡 ~90%, σ(6) 는 이미 EXACT)

**Gate to close**:

| Gate | 내용 | Deadline | Owner | Status |
|------|------|----------|-------|--------|
| **GATE-26-V-R1 (C5)** | cage output schema lock — `virocapsid/spec/cage_output_v1.schema.json` (LANDED) + 4 cells 가 conformance witness emit | **2026-07-28** | hexa-bio session | ⚠️ schema landed, lock+conformance 미완 |
| GATE-26-V-1b (C3b) | F-VIROCAPSID-1 full corpus — n≥100 PDB entries + posterior ≥ 0.95 (현재 n=10 post 1.0) | 2027-04-28 (deferred cycle 28+) | hexa-bio session | ⬜ infra ready (C3a), 확장 대기 |
| F-VIROCAPSID-1-c | source bias 독립축 — textbook vs experimental vs designed stratum (현재 5:4:1) | cycle 28+ | hexa-bio session | 🟡 partial |
| F-VIROCAPSID-1-d | annotation completeness 독립축 (현재 1.0 on n=10) | cycle 28+ | hexa-bio session | 🟡 |
| V-R2 stretch | multi-T 일반화 T=7 / T=13 / T=21 (현재 T=1/T=3/T=4 PASS) — per-system rate-constant re-derivation | cycle 30+ | hexa-bio session | ⬜ deferred |
| (sandbox 평준화) | weave 급 empirical sandbox — 현재 cage assembly 는 `~/core/nexus/sim_bridge/weave/` 의 ODE 를 공유 + `virocapsid_calibration.py` / `virocapsid_multi_t_calibration.py`; 독립 Zlotnick ODE 를 CLI 에 wiring | cycle 28+ | hexa-bio session | 🟡 shared bridge |

**잔여 작업 요약**:
- [ ] **C5 schema lock + 4-cell conformance witness** (07-28, 단기 — 코드 작업).
- [ ] C3b full corpus 확장: RCSB PDB API 로 n≥100 (T strata ≥3, source class ≥2 유지) + Bayesian re-audit posterior ≥ 0.95 (long pole).
- [ ] F-VIROCAPSID-1-c / -1-d 독립축 정량화.
- 비차단: T=7/T=13/T=21 (cycle 30+); 독립 ODE wiring.

**닫힘 조건**: σ(6)=12 STRUCTURAL-EXACT 는 이미 만족 (T=1 post 1.0, multi-T PASS). C5 schema lock 완료 시 **v1.x closure-grade 도달**; C3b n≥100 + posterior ≥0.95 는 robustness upgrade (v1.x 비차단, cycle 28+ stretch). 즉 virocapsid 는 사실상 단기(07-28)에 closure-grade 가능.

---

## §6 QUANTUM — computation (🔴 ~55%, long pole, USER-GATED)

**Gate to close**:

| Gate | 내용 | Deadline | Owner | Status |
|------|------|----------|-------|--------|
| F-Q-1 / -1-spec | H₂ chemical/spectroscopic accuracy | — | — | ✅ PASS (0.4 µHa / 0.14 µHa) |
| F-Q-2 | LiH chemical accuracy | — | — | ✅ PASS (1.408 mHa) — L1 부분 |
| F-Q-3 | H₂ bond-length scan | — | — | ✅ PASS (11/11 sub-µHa) — L2 |
| F-Q-4 / -5 | ANU live end-to-end / long-lived bridge ≥5× | — | — | ✅ PASS (anu_legacy / 31.4×) |
| F-Q-EXT-1…6 | external systems review (22 systems / 5 axes) + 3 axes pilot smoke + chain pilot | — | — | ✅ PASS |
| **F-Q-6** | **drug-target pocket VQE — Phase C** | OPEN | **USER** (target system + pocket residue + ligand library 선정 필요) | 🔴 **OPEN — USER-GATED** |
| F-Q-EXT-7b | caDNAno smoke — numpy ABI + PyQt5 forced load 로 BLOCKED | OPEN | hexa-bio session | 🔴 BLOCKED → alt-path (scadnano / oxDNA direct) 필요 |
| L1 (확장) | small-molecule generalize — BeH₂ 6-qubit (LiH 는 F-Q-2 로 완료) | — | hexa-bio session | 🟡 LiH done, BeH₂ pending |
| L3 | drug-target pocket fragment — single active-site QM/MM split, single-restart VQE (= F-Q-6) | gated on user | hexa-bio session | 🔴 = F-Q-6 |
| L4 | protein-relevant subsystem — single-residue active site | gated on L3 | hexa-bio session | ⬜ |
| Phase C / D (`.roadmap.novel_drugs`) | Phase C pocket supersystem VQE (F-Q-6-D, e.g. Cys145+His41+ligand reactive 부분, nirmatrelvir target) → Phase D library ranking (F-Q-6-F, target 마다 5-10 candidate library) | gated on user | hexa-bio session | 🔴 Phase C IN-PROGRESS, attempt 9 (D3 dispersion bottleneck) |
| Phase 2 port | `_python_bridge/module/quantum_*.py` adapters → hexa-native (별도 hexa-lang session, user directive 2026-05-07) | — | hexa-lang session | ⬜ out-of-scope here |
| σ(6) 확장 | n=6 binding 을 H₂/LiH 6-Pauli 너머 pocket-scale Hamiltonian 으로 일반화 | gated on Phase C | hexa-bio session | 🟡 H₂/LiH only |

**잔여 작업 요약**:
- [ ] **USER DECISION 필요** — F-Q-6 / Phase C 의 입력: (a) target protein + 활성부위 residue 집합, (b) ligand reactive 부분, (c) 5-10 candidate ligand library. 이게 정해지기 전까지 quantum closure 는 진행 불가. (`.roadmap.novel_drugs` 의 Phase C 가 nirmatrelvir / Cys145+His41 를 후보로 잡고 attempt 9 까지 진행 중 — user 가 이걸 confirm 하거나 다른 target 지정.)
- [ ] F-Q-EXT-7b caDNAno alt-path: caDNAno 가 numpy ABI + PyQt5 강제로드로 BLOCKED → scadnano (브라우저/CLI) 또는 oxDNA 직접 호출로 대체.
- [ ] L1 BeH₂ 6-qubit (LiH 패턴 재사용).
- [ ] Phase C 완료 후 L4 (single-residue active site) → Phase D library ranking.
- 비차단: Phase 2 hexa-native port (별도 session); fault-tolerant HW (Aer + ANU QRNG only — `.roadmap.quantum_hw_adoption_ladder`).

**닫힘 조건**: F-Q-6 (pocket VQE, target 1개 published reference error band 내) PASS + F-Q-EXT-7b 해소(또는 alt-path PASS) + L1 BeH₂ + L4 single-residue → quantum v1.x closure-grade. **선행조건 = user 의 target-system 결정.**

---

## §7 통합 타임라인 (제안)

| 시점 | 마일스톤 |
|------|----------|
| ~now → 2026-06-15 | **G26-RB-1 + G26-NB-EXT inter-rater 일괄 실행** (≥2 human raters, ribozyme κ≥0.6 + nanobot extended-corpus) → ribozyme & nanobot σ(6) CANDIDATE→EXACT 의 마지막 조건 충족. ribozyme G26-RB-2 branch-lock. |
| → 2026-07-28 (MVP gate) | virocapsid **C5 schema lock + 4-cell conformance** · nanobot **C0d cuboctahedron** · nanobot **N-R1 v2 emit** · ribozyme **R-R1 MFE port** (stub 제거) → ribozyme + nanobot + virocapsid v1.x closure-grade 도달 목표 |
| → 2026-09-28 | ribozyme G26-RB-2 exec + G26-RB-3 C2 uplift · nanobot F-NB-2-c stratum bias · nanobot N-R2 L6 handoff lock |
| 2026-08~ (user 결정 후) | **quantum Phase C — F-Q-6 pocket VQE** (target 확정 시 시작) → L3 → L4 → Phase D library ranking |
| cycle 28+ | virocapsid C3b full corpus n≥100 + posterior ≥0.95 · F-VIROCAPSID-1-c/-d 독립축 |
| cycle 30+ | virocapsid V-R2 T=7/13/21 · nanobot/ribozyme wet-lab handoff · quantum HW adoption ladder |
| v2.0.0 | GATE-26-2 full lean4-backed Π¹₁-CA₀ cert (전 5축) · Bayesian audits 5/5 empirical · weave CHI2 n≥5 |

---

## §8 user 입력이 필요한 항목 (지금 결정하면 빨라지는 것)

1. **quantum F-Q-6 target system** — Phase C 가 막혀 있는 유일한 이유. `.roadmap.novel_drugs` Phase C 후보(nirmatrelvir / SARS-CoV-2 Mpro Cys145+His41)를 confirm 할지, 다른 target 을 지정할지. → **이것 없이는 quantum 5/5 closure 불가.**
2. **inter-rater 인력** — G26-RB-1 (ribozyme, κ≥0.6) + G26-NB-EXT (nanobot extended corpus). user 가 직접 채점 vs ≥2명 위임. → ribozyme + nanobot σ(6) STRUCTURAL-EXACT 의 게이트.
3. **G26-RB-2 J₂=24 quotient** — ribozyme 의 reaction-coordinate J₂ quotient 을 v1.x in-scope 로 할지 stretch 로 둘지 (branch-lock 2026-06-15).
4. **virocapsid C3b deadline** — n≥100 corpus 를 v1.x 안으로 당길지(코드 작업, 1-2 cycle), cycle 28+ 로 둘지. (σ(6) EXACT 는 이미라 closure 비차단이지만 robustness 차원.)

---

## §9 cross-links

- cross-cutting tracker: [`.roadmap.hexa_bio`](.roadmap.hexa_bio) (§A.1 lattice / §A.2 cadence / §A.4 MVP gate / §F STALLED audit / §G cycle-26 gates)
- per-axis: [`.roadmap.weave`](.roadmap.weave) · [`.roadmap.virocapsid`](.roadmap.virocapsid) · [`.roadmap.nanobot`](.roadmap.nanobot) · [`.roadmap.ribozyme`](.roadmap.ribozyme) · [`.roadmap.quantum`](.roadmap.quantum)
- quantum drug-target: [`.roadmap.novel_drugs`](.roadmap.novel_drugs) (Phase B/C/D) · [`.roadmap.quantum_hw_adoption_ladder`](.roadmap.quantum_hw_adoption_ladder)
- axis lock: [`.roadmap.axis_expansion_decision_2026_05_08`](.roadmap.axis_expansion_decision_2026_05_08) · platform manifest: [`.roadmap.platform_index`](.roadmap.platform_index)
- changelog: [`CHANGELOG.md`](CHANGELOG.md) `[Unreleased]` · release notes: [`RELEASE_NOTES_v1.1.0.md`](RELEASE_NOTES_v1.1.0.md) · [`V1_1_0_HANDOFF.md`](V1_1_0_HANDOFF.md)
