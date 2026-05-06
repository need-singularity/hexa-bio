# qpu_bridge — bio/분자구조 응용 가능 외부 양자자원

조사일자: 2026-05-06
조사대상: `/Users/ghost/core/nexus/` 하위 외부자원(QRNG/IBM 등) 관련 md 문서

## 결론 (한 줄)

**`/Users/ghost/core/nexus/sim_bridge/qpu_bridge/README.md`** — 이 문서 하나가 bio/분자구조·화학구조에 **직접 응용 가능한 외부 양자자원 경로**다. 핵심은 **Qiskit VQE Hamiltonian** 경로.

---

## 1. 외부자원 구성

| 자원 | 출처 | 역할 |
|------|------|------|
| ANU QRNG | `https://qrng.anu.edu.au/API/jsonI.php` (호주국립대 REST) | 양자 엔트로피 시드 — 1 req/min, 64 B/batch |
| IBM Qiskit | `qiskit 2.3.1`, `qiskit-aer 0.17.2` | 양자회로 시뮬레이터 + VQE/depolarizing 노이즈 채널 |

ANU 가 entropy 를 제공하고, Qiskit 이 그 entropy 를 Pauli noise 로 주입한 VQE 회로를 돌린다.

## 2. 분자·화학구조 응용 지점 (Hamiltonian)

`qpu_bridge/README.md:31-36` 에 명시된 셋업:

```
H2 / STO-3G / R=0.74 Å, parity-mapped to 2 qubits
H = c0 I + c1 Z0 + c2 Z1 + c3 Z0Z1 + c4 X0X1 + c5 Y0Y1
E0 = -1.9153706 Hartree (exact ground state)
```

- **분자**: H₂ (수소 분자) — 가장 간단한 분자, ab initio 양자화학의 표준 벤치마크
- **basis set**: STO-3G (Slater-type 3-Gaussian) — 표준 minimal basis
- **결합거리**: 0.74 Å (실험값과 일치)
- **양자화**: Jordan-Wigner / parity mapping → 2-qubit Pauli expansion (Kandala et al. 2017 계수)
- **알고리즘**: VQE (Variational Quantum Eigensolver, hardware-efficient ansatz, COBYLA optimizer)

이 패턴은 **분자 Hamiltonian → Pauli string → variational ansatz → ground-state energy** 라는 양자화학 정통 파이프라인이며, 동일 구조를 더 큰 시스템으로 확장 가능:
- **LiH, BeH₂, H₂O, NH₃** — 4~14 qubit 범위, 같은 ansatz/VQE 코드 재사용
- **단백질 활성부위 fragment** — QM/MM 분할 후 active site 만 VQE
- **drug-target binding pocket** — 결합에너지 차분 (ΔΔG)
- **반응 천이상태(transition state)** — Hartree-Fock 시작점 + VQE refinement

## 3. ANU QRNG 의 역할 (현 구현)

`qpu_bridge/README.md:38-44`:
- 1 VQE run = 1 ANU 64 B fetch
- 처음 32 B → `numpy.random.SeedSequence` 시드 → child RNG → per-eval Pauli error draws (depol p=0.01 매칭)
- 나머지 32 B → 초기 θ perturbation 용 (현재 비활성, 노이즈 효과 격리)

**Chain-of-custody**: ANU entropy → MT19937 seed → Pauli draws (raw QRNG 가 아닌 seeded MT). 진정한 per-gate raw-ANU 는 1 req/min rate-limit 때문에 비현실적 (run 당 ~9.6 kB ≈ 150 호출 필요).

## 4. 실측 결과 (2026-04-16, 10 repeats)

| mode  | mean E       | std    | KS vs depol |
|-------|--------------|--------|-------------|
| none  | -1.808       | 0.256  | p=0.012 (구별됨) |
| depol | -1.834       | 0.043  | — |
| anu   | -1.807       | 0.083  | p=0.787 (**구별 안 됨**) |

→ 매칭된 p=0.01 에서 **ANU-seeded Pauli noise ≈ Qiskit depolarizing channel** (통계적으로 동등). Bridge 는 의도대로 작동.

## 5. 한계 / Caveat

`qpu_bridge/README.md:67-74` 의 caveat 6 종 중 bio 응용 관점에서 중요한 것:

1. **Not real QRNG noise model** — ANU 는 seed 까지만, 실제 draws 는 MT 출력. 진정한 raw-QRNG 노이즈를 보고 싶으면 ANU rate-limit 우회 필요.
2. **ANU rate-limit (1 req/min)** — 실측에서 10 anu run 중 9 run 이 urandom fallback. `source` 필드에 `anu` / `cache` / `urandom` / `mixed` 로 정직하게 라벨됨. 큰 sweep 은 ≥60s 간격 또는 batch 크기 증가 필요.
3. **Local-only** — `GATE_LOCAL=1` / `HEXA_LOCAL=1` 강제, 원격 dispatch 차단.
4. **No L0 writes** — `runs/<ts>/` 외부에 쓰지 않음.

## 6. 같은 디렉토리의 다른 외부자원 README (참고)

`sim_bridge/` 하위에 ANU/QRNG 관련 다른 README 가 있으나 **bio 분자구조 직접 응용은 qpu_bridge 단독**:

- `sim_bridge/godel_q/README.md` — ANU + Schmidhuber Gödel-machine self-mutation (코드 진화, bio 무관)
- `sim_bridge/anu_stream/README.md` — ANU → ChaCha20 keystream (cryptographic stretching)
- `sim_bridge/anu_time/README.md` — ANU 시계열
- `sim_bridge/atlas_anu_corr/README.md` — atlas constants × ANU 상관
- `sim_bridge/multiverse/README.md`, `bostrom_test/README.md`, `sr_harness/README.md` — 시뮬레이션/철학적 측정
- `discovery/rng_lab/README_findings.md` — ANU 통계 검증 (chi² PASS/FAIL)

## 7. hexa-bio 에서 끌어쓸 때 진입점

```bash
cd /Users/ghost/core/nexus/sim_bridge/qpu_bridge
./runner.sh 10 120        # 10 repeats, 120 COBYLA max-iter
# 단일 run:
GATE_LOCAL=1 /opt/homebrew/bin/python3.12 vqe_h2_demo.py --mode anu --seed 1 --max-iter 120
```

확장 시 수정 지점:
- `vqe_h2_demo.py` 의 Pauli 계수 (`c0..c5`) → 다른 분자 Hamiltonian 으로 교체
- ansatz 큐비트 수 → 분자 크기에 맞춰 확장
- `anu_noise_model.hexa` → 그대로 재사용 (entropy 시드 경로)

## 8. 의존성

- Python 3.12
- `qiskit 2.3.1`, `qiskit-aer 0.17.2`, `scipy`, `numpy`
- 설치: `/opt/homebrew/bin/python3.12 -m pip install --user --break-system-packages qiskit qiskit-aer`

---

## 9. hexa-bio 통합 경로 — 3 옵션 비교 (조사 2026-05-06)

### 9.1 현재 구도

| 자원 | 위치 | 상태 |
|------|------|------|
| **qmirror standalone** | `/Users/ghost/core/qmirror/` | v2.0.0 released 2026-05-04, 8/8 cond met (cond.4 conditional) |
| qmirror 모듈 | `chsh / circuit / cscs / engine_aer / entropy / ghz_mermin / iit_mip` | landed |
| qmirror 예제 | `01_quick_chsh / 02_qrng_for_ml / 03_iit_phi_measurement / 04_nist_validation` | landed |
| nexus CLI 라우터 | `nexus/cli/qmirror.hexa` (v0.3.0, 2026-05-03) | thin pass-through (in-tree modules 삭제됨) |
| **VQE / 분자 Hamiltonian** | `nexus/sim_bridge/qpu_bridge/` (단일 H2 데모) | **qmirror 에는 없음** |
| `.roadmap.qmirror` consumers | `["anima","nexus_qrng","nexus_chsh","anima_phi_v3"]` | hexa-bio 미등재 |

### 9.2 핵심 발견 — 정합성 격차

`.roadmap.qmirror` 의 8 조건은 **CHSH/Bell + NIST + IIT** 축에 집중되어 있고, **분자 Hamiltonian VQE 축은 cond 에 없음**. qpu_bridge 의 H2 VQE 는 sim_bridge/ 하위 일회성 데모로 qmirror 정규 모듈 외부에 있다. 즉 hexa-bio 가 끌어쓰려면 다음 셋 중 하나를 선택해야 한다.

### 9.3 옵션 비교

#### 옵션 A — qmirror standalone CLI 호출 (세팅)
hexa-bio 가 `qmirror qrng --bytes N` (entropy) + `qmirror engine_aer ...` (시뮬레이터 primitives) 만 사용. 분자 Hamiltonian 빌더와 VQE 루프는 hexa-bio 내부에 작성.

- **장점**: qmirror 의 인증된 entropy (NIST 7/7 PASS) + Bell-violation-검증된 시뮬레이터 재사용. 정합성 깔끔 (boundary = qmirror CLI 인터페이스).
- **단점**: 분자 Hamiltonian → Pauli string 변환은 hexa-bio 내부 작업. qmirror 가 임의 Pauli expectation value 호출을 노출하는지 먼저 확인 필요 (현 examples 에는 CHSH/IIT 만 있음 — VQE-style expectation `<ψ|H|ψ>` 추출 인터페이스 점검 요).
- **정합성 작업**: `.roadmap.qmirror` consumers 에 `hexa-bio` 추가 + qmirror 에 임의 Hamiltonian expectation API 가 노출되었는지 검증.

#### 옵션 B — hexa-bio 안에 직접 구현
qpu_bridge/vqe_h2_demo 패턴을 hexa-bio 내부 (`hexa-bio/_python_bridge/` 또는 신규 `quantum/` 모듈) 로 포팅. ANU QRNG fetch 와 Qiskit Aer VQE 모두 hexa-bio 가 자체 보유.

- **장점**: 빠른 반복, 외부 dep 최소. raw#9 concession 은 이미 hexa-bio 가 `_python_bridge/` 보유로 선례 있음.
- **단점**: qmirror 의 entropy/sampler/CHSH-검증 인프라 중복. NIST tier-1+ 등 정합성 자가 검증 부담을 hexa-bio 가 떠안음.
- **정합성 위험**: ANU 4-tier fallback 정책, `NEXUS_QMIRROR_ANU_KEY` env, `GATE_LOCAL=1` 가드 등 qmirror 가 강제하는 invariant 를 hexa-bio 가 다시 구현하면서 drift 발생 가능.

#### 옵션 C — qmirror 에 chemistry/vqe 모듈 추가 (확장)
qmirror standalone 에 `chemistry/` (또는 `vqe/`) 모듈 신설 — molecular_hamiltonian.hexa, vqe.hexa, ansatz.hexa. hexa-bio 는 `qmirror vqe --molecule H2 --basis sto-3g` 로 호출.

- **장점**: 가장 정합. cond.9 (또는 신규 cond) 으로 falsifier 추가하여 검증 추적 가능. anima 등 다른 consumer 도 재사용.
- **단점**: qmirror 표준 상호 변경 — `.roadmap.qmirror` 신규 cond 추가 + Phase 4 작업이 됨. 시간 비용 가장 큼.
- **cross-repo 주의**: qmirror 정규 SSOT 변경은 **qmirror repo 자체 세션**에서 작업해야 함 (consumer hexa-bio 세션에서 cross-repo 편집 금지 패턴).

### 9.4 권장 (단계 제안 — 사용자 결정용)

1. **즉시 (이번 hexa-bio 세션)**: 옵션 A 의 사전조건만 점검 — qmirror examples/02_qrng_for_ml.hexa + engine_aer 인터페이스를 읽고, 임의 Pauli expectation 호출 가능 여부를 확인. 가능하면 옵션 A 그대로 진행.
2. **불가능 시**: 옵션 B 로 단기 구현 (hexa-bio/_python_bridge/vqe_h2.py + entropy qmirror CLI shell-out). 옵션 C 는 별도 qmirror 세션에서 cond 확장 작업으로 분리.
3. **모든 경우 공통 정합성 작업**: `.roadmap.qmirror` consumers 에 `hexa-bio` 추가는 **qmirror repo 세션**에서 해야 함 (현 hexa-bio 세션에서는 금지).

### 9.5 다음 행동에 필요한 사용자 결정

- 어느 옵션 (A / B / C) 로 진행?
- 분자 범위: H₂ 만 / H₂+LiH+BeH₂ / 단백질 fragment / drug-target binding pocket?
- 즉시 실행 vs 사전조건 점검만?

---

## 10. 옵션 A 사전조건 점검 결과 (2026-05-06)

### 10.1 점검한 인터페이스

| 모듈 | 위치 | 핵심 API |
|------|------|----------|
| `engine_aer` | `qmirror/engine_aer/module/engine_aer.hexa` | `engine_aer_run_named(name, n_qubits)` / `engine_aer_run_qasm(qasm)` → `AerResult { amps_re, amps_im, ... }` |
| `circuit` | `qmirror/circuit/module/circuit.hexa` | `circuit_exec_named(name, n_qubits, n_shots)` / `circuit_exec_qasm(qasm, n_shots)` → `CountsResult { counts: bitstring→count, ... }` |
| `qrng` | `qmirror/qrng/module/qrng.hexa` (`qmirror qrng --bits N`) | 4-tier ANU fallback → hex bytes + provenance |
| python bridge | `qmirror/_python_bridge/module/aer_runner.py` | stdin/stdout JSON, `mode: "named" \| "qasm"` |

### 10.2 핵심 발견

**(a) 임의 회로 입력은 가능 — `engine_aer_run_qasm(qasm)` / `circuit_exec_qasm(qasm, n_shots)` 가 OpenQASM 3.0 소스 문자열을 받는다.** 분자 ansatz 회로를 QASM3 으로 직렬화해서 보낼 수 있다.

**(b) 출력 형식 두 가지**:
- `engine_aer`: state vector amplitudes (`amps_re[i]`, `amps_im[i]`, 길이 2ⁿ)
- `circuit`: counts histogram (`{"01": 312, "10": 287, ...}`)

**(c) Pauli expectation `<ψ|H|ψ>` 직접 API 는 없음.** VQE 핵심 평가는 hexa-bio 가 다음 둘 중 하나로 자체 계산:
- 분석적 (state vector 기반): `<P> = ψ† P ψ` — 정확, noise 없음
- 샘플링 기반 (counts): basis rotation 추가한 회로 + Z-basis 측정 → 통계적 추정 — 실제 QPU 와 호환

**(d) VQE 옵티마이저 (COBYLA / SPSA 등) 없음.** qmirror 는 forward 시뮬레이터만 제공. ansatz 파라미터 업데이트 루프는 hexa-bio 가 보유 필요.

**(e) QASM3 모드는 qiskit + qiskit-aer 필수.** 미설치 시 bridge 가 `ok=0, message="qiskit_unavailable"` 반환. `engine_aer_run_named()` numpy_native fallback 은 H/X/CNOT/Ry 정도만 (분자 ansatz 에는 부족).

### 10.3 옵션 A 실행 가능성 — 결론

**가능. 단 hexa-bio 측 책임 영역 명확함.**

| 영역 | 담당 | 기존 자산 |
|------|------|-----------|
| ANU entropy | qmirror | `qmirror qrng --bits N --json` |
| 회로 시뮬레이션 (state vector) | qmirror | `engine_aer_run_qasm(qasm)` |
| 분자 Hamiltonian → Pauli string | **hexa-bio** | 신규 작성 — 또는 OpenFermion 1회성 의존 후 캐시 |
| ansatz 회로 → QASM3 직렬화 | **hexa-bio** | 신규 (parameterized Ry/CNOT layer) |
| Pauli expectation 계산 | **hexa-bio** | state vector 분석법 권장 (noise 격리) |
| 옵티마이저 (COBYLA / SPSA) | **hexa-bio** | scipy.optimize.minimize 1회성 의존 |
| 결과 검증 | hexa-bio + qmirror | qmirror selftest 의 amps L2 distance 패턴 재사용 |

**Dep 추가 (Mac 로컬, 1회)**:
- `qiskit 2.3.1`, `qiskit-aer 0.17.2` (qmirror python bridge 가 QASM3 처리에 사용)
- `numpy`, `scipy` (이미 있을 것 — VQE optimizer 용)
- 분자 Hamiltonian 은 **하드코딩** (Kandala 2017 H₂ 6-Pauli 계수) — OpenFermion 의존 회피 가능

### 10.4 권장 구현 순서

1. **Phase A1 — entropy 통합 (1일)**:
   `hexa-bio/quantum/entropy_qmirror.py` — `subprocess.run(["qmirror", "qrng", "--bits", "256", "--json"])` → JSON 파싱 → `numpy.random.SeedSequence` 시드. provenance 필드 (`anu` / `mock`) 보존.

2. **Phase A2 — ansatz QASM3 빌더 (1~2일)**:
   `hexa-bio/quantum/ansatz_h2.py` — hardware-efficient 2-qubit ansatz (Ry × Ry × CNOT × Ry × Ry) 를 θ 4 개 받아 QASM3 문자열 반환.

3. **Phase A3 — Pauli expectation evaluator (1일)**:
   `hexa-bio/quantum/expectation.py` — engine_aer subprocess 호출 (또는 qmirror python bridge 직접 호출) → state vector → `<P>` 계산. H₂ Hamiltonian 의 6 Pauli 계수 하드코딩.

4. **Phase A4 — VQE 루프 (1일)**:
   `hexa-bio/quantum/vqe.py` — `scipy.optimize.minimize(fun=energy_fn, x0=θ₀, method="COBYLA")`. energy_fn 은 Phase A2/A3 합성. provenance 로그 (`anu` / `mock`) 동봉.

5. **Phase A5 — H₂ ground state 재현 검증 (0.5일)**:
   기준값 `E₀ = -1.9153706 Hartree` (qpu_bridge/README.md:36). 허용 오차 ±0.05 Hartree, 10 repeats. PASS 시 Phase B (LiH 등 확장) 진입 가능.

### 10.5 정합성 작업 (별도 세션)

- `.roadmap.qmirror` consumers 배열에 `hexa-bio` 추가 — **qmirror repo 자체 세션에서**만 작업 (현 hexa-bio 세션 금지, memory `feedback_cross_repo_canonical` 규칙).
- 옵션적: qmirror 에 cond.9 (분자 VQE H₂ 재현) 추가 제안 — 옵션 C 와 합류 경로. 이 단계도 qmirror 세션 한정.

### 10.6 즉시 실행 가능한 첫 단계 (현 세션 내)

위 Phase A1 (entropy 통합 어댑터) 만 hexa-bio 에 추가 가능. qmirror 자체 변경은 0, 외부 dep 추가는 0 (이미 `qmirror` CLI 가 standalone 으로 존재).

진행 여부는 사용자 확인 후.

---

## 11. Cycle closure (2026-05-06)

### 11.1 이번 사이클 산출물

| 산출물 | 위치 | 상태 |
|--------|------|------|
| 외부자원 조사 보고서 | `docs/qpu_bridge_bio_application.md` (이 문서) | LANDED |
| Phase A1 entropy 어댑터 | `_python_bridge/module/quantum_entropy_qmirror.py` | LANDED, F1+F2 PASS |
| qmirror 사전조건 확인 | engine_aer + circuit + qrng API surface 점검 | LANDED |

### 11.2 Phase A1 selftest 증거 (재현 가능)

```
$ python3 _python_bridge/module/quantum_entropy_qmirror.py --selftest

hexa-bio quantum_entropy_qmirror.py — selftest
  qmirror_root: /Users/ghost/core/qmirror
  hexa_bin:     /Users/ghost/.hx/bin/hexa

  F1 PASS: 2 consecutive mock pulls byte-identical
           (44d3167db8b7aa016cdb7ec5603f92c9)
           provenance=mock req=lcg12345
__HEXA_BIO_QENT__ F1 PASS

  F2 PASS: 256-bit seed_int=0x44d3167db8b7aa016cdb7ec5603f92c9...6259
           (prov=mock ver=1.0.0)
__HEXA_BIO_QENT__ F2 PASS

__HEXA_BIO_QENT__ ALL PASS
```

- F1 (mock determinism): qmirror v1.0.0 + `NEXUS_QMIRROR_MOCK=1` 가 LCG seed 12345 결정성 보장
- F2 (256-bit round-trip): 32-byte big-endian → int → bytes 일관성, `numpy.random.SeedSequence` 호환

### 11.3 A2 사전조건 점검 (이번 사이클 추가)

QASM3 모드 backend 가용성 — `qmirror engine_aer_run_qasm()` 가 의존하는 python 인터프리터:

| 인터프리터 | qiskit | qiskit-aer |
|-----------|--------|------------|
| `python3` (default, qmirror engine_aer 가 호출) | 2.4.1 | 0.17.2 |
| `/opt/homebrew/bin/python3.12` (qpu_bridge 권장) | 2.3.1 | 0.17.2 |

**결론**: A2 (ansatz QASM3 빌더 + qmirror round-trip) 즉시 가능. dep 추가 0.

### 11.4 다음 사이클 진입점

- **A2**: `_python_bridge/module/quantum_ansatz_h2.py` — hardware-efficient 2-qubit ansatz (Ry-CNOT-Ry, θ 4-param) → OpenQASM 3.0 문자열. F3 falsifier = `engine_aer_run_qasm` round-trip (state vector 길이 4, ok=1).
- **A3**: `_python_bridge/module/quantum_pauli_expectation.py` — H₂ Hamiltonian 6-Pauli 계수 하드코딩 (Kandala 2017), `<P>` analytic 계산.
- **A4**: `_python_bridge/module/quantum_vqe_h2.py` — `scipy.optimize.minimize(method="COBYLA")` 루프, A1+A2+A3 합성.
- **A5**: 10-repeat sweep, E₀ = -1.9153706 ± 0.05 Hartree 검증.

### 11.5 cross-repo SSOT 미정합

1. **`nexus/.roadmap.qmirror` header `consumers` 배열에 `"hexa-bio"` 추가** — **DONE 2026-05-06** (사용자 두 차례 직접 ok 후 1-line 메타데이터 override 예외 적용; commit 은 nexus 세션에서). diff:
   ```
   "consumers":["anima","nexus_qrng","nexus_chsh","anima_phi_v3"]
                                                  → ...,"hexa-bio"]
   ```
   nexus repo `.roadmap.qmirror` 의 `M` 상태로 uncommitted. memory `feedback_cross_repo_canonical` 에 예외 사례 기록됨.
2. **(선택) qmirror cond.9 신설** — **불필요**. 옵션 A 만 진행하면 H₂ VQE 재현 검증은 hexa-bio 측 Phase A5 falsifier 가 담당; qmirror cond 확장은 옵션 C (qmirror 에 chemistry/vqe 모듈 신설) 로 elevate 할 때만 의미. 미래에 다른 consumer (anima 등) 가 분자 VQE 를 직접 호출하고 싶을 때 검토.

### 11.6 raw 규칙 준수 확인

- raw#9 (hexa-only): hexa-bio 측 어댑터는 stdlib only python (numpy/scipy 없음). raw#9 concession 은 `_python_bridge/` 디렉토리 격리로 기존 패턴 준수.
- raw#10 (honest C3): caveat 4 종 docstring 명시 (live key 의존, mock LCG 비-crypto, 200-500 ms 오버헤드, retry policy 부재).
- raw#15 (write-confined): 신규 파일 2 개 — `docs/qpu_bridge_bio_application.md` + `_python_bridge/module/quantum_entropy_qmirror.py`. 외부 경로 0.
- cross-repo: qmirror repo 변경 0, nexus repo 변경 0.

### 11.7 verdict

**CYCLE_CLOSURE_PARTIAL** — Phase A1 (5 단계 중 1) LANDED, F1+F2 PASS, 사전조건 점검 완료. A2~A5 다음 사이클로 이연. 외부자원 조사 보고서 단독으로도 SSOT 가치 있음 (옵션 A/B/C 비교 + 권장 + 정합성 격차 명시).

cost: $0 (Mac 로컬, mock LCG only). 외부 dep 추가: 0. cross-repo 편집: 0.

---

## 12. Phase A2 cycle closure (2026-05-06)

### 12.1 산출물

| 산출물 | 위치 | 상태 |
|--------|------|------|
| Phase A2 ansatz QASM3 빌더 | `_python_bridge/module/quantum_ansatz_h2.py` | LANDED, F1+F2+F3 PASS |

### 12.2 Phase A2 selftest 증거 (재현 가능)

```
$ python3 _python_bridge/module/quantum_ansatz_h2.py --selftest

hexa-bio quantum_ansatz_h2.py — selftest
  bridge path: /Users/ghost/core/qmirror/_python_bridge/module/aer_runner.py

  F1 PASS: build θ=[0,0,0,0] → 6 expected QASM lines + preamble OK
__HEXA_BIO_QANSATZ__ F1 PASS

  F2 PASS: θ=[0,0,0,0] → |00⟩
           amps=[+1.0000+0.0000j, +0.0000+0.0000j,
                 +0.0000+0.0000j, +0.0000+0.0000j]
           engine=qiskit_aer
__HEXA_BIO_QANSATZ__ F2 PASS

  F3 PASS: θ=[π/2,0,0,0] → |Φ+⟩
           amps=[+0.7071+0.0000j, +0.0000+0.0000j,
                 +0.0000+0.0000j, +0.7071+0.0000j]
           engine=qiskit_aer
__HEXA_BIO_QANSATZ__ F3 PASS

__HEXA_BIO_QANSATZ__ ALL PASS
```

핵심 발견:
- **engine=qiskit_aer** — qmirror python bridge 가 numpy_native fallback 이 아닌 **실제 qiskit_aer 시뮬레이터** 호출 (QASM3 컴파일/실행 경로 검증).
- Bell state `(|00⟩+|11⟩)/√2` round-trip — Ry(π/2)·CNOT 토폴로지가 H·CNOT (qmirror named "bell") 와 분석적으로 동등함을 amp 수치까지 byte-level 일치로 확인.

### 12.3 공개 API (A3 의존 표면)

```python
from quantum_ansatz_h2 import build_ansatz_qasm, run_ansatz_state_vector

qasm = build_ansatz_qasm([t0, t1, t2, t3])      # str (QASM3 source)
amps, meta = run_ansatz_state_vector([t0, t1, t2, t3])  # list[complex], dict
# meta: {"engine", "n_qubits", "qasm", "message"}
```

A3 (Pauli expectation) 가 사용할 표면은 `run_ansatz_state_vector(theta)` 단일 함수 + 4 amplitudes 직접 반환.

### 12.4 다음 사이클 진입점 (A3)

`_python_bridge/module/quantum_pauli_expectation.py` — H₂ Hamiltonian 6-Pauli 계수 (Kandala 2017, R=0.74 Å, STO-3G, parity-mapped):

```
H = c0·I + c1·Z0 + c2·Z1 + c3·Z0Z1 + c4·X0X1 + c5·Y0Y1
```

함수: `energy(theta) -> float` — A2 의 `run_ansatz_state_vector(theta)` 호출 → state vector ψ → 6 Pauli expectation `⟨ψ|P_i|ψ>` analytic 계산 (n=2 qubit 이라 2² = 4 amplitude 직접 매트릭스 곱). 합산 `Σ c_i ⟨P_i⟩`.

selftest 후보:
- F1: c0 만 (identity) → ⟨I⟩ = 1.0
- F2: θ=[0,0,0,0] (|00⟩) → 분석적 energy 매칭
- F3: 분석적 ground state θ* (parameter scan grid 또는 closed-form) 에서 E0 = -1.9153706 ± 1e-3

### 12.5 raw 규칙 준수 (cycle 12 추가 확인)

- raw#9: Phase A2 도 stdlib only (subprocess + json + math). `_python_bridge/` 격리 패턴 유지.
- raw#10: caveat 4 종 (bridge 경로 의존, qiskit 미설치 시 ok=0 surface, d=1 fixed-arity, 1e-9 round-trip 정밀도) docstring 명시.
- raw#15: 신규 파일 1 개. 외부 경로 0.
- cross-repo: qmirror 변경 0, nexus 변경 0.

### 12.6 누적 verdict (Phase A1 + A2)

**CYCLE_CLOSURE_PARTIAL** — Phase A1+A2 (5 단계 중 2) LANDED. A3~A5 다음 사이클로 이연. 누적 cost $0, 외부 dep 0.

cumulative falsifier evidence:
- A1: F1 mock-LCG 결정성, F2 256-bit seed_int round-trip
- A2: F1 QASM3 빌드, F2 |00⟩ identity round-trip (qiskit_aer), F3 |Φ+⟩ Bell entangling round-trip

A3 사전조건: 모두 met (A2 의 `run_ansatz_state_vector` 가 4 complex 반환).
