# 리포트 표 sample — pocket VQE iteration matrix

본 파일 = 사용자가 명시한 reporting style sample (2026-05-11). 향후 리포트 시 본 형식의
표를 포함한다 (own preference 등록).

---

## sample 1 — pocket VQE iteration matrix (cumulative 진행)

```
┌──────┬─────────┬───────────┬─────────────┬─────────┐
│ iter │ target  │ optimizer │ delta (µHa) │ sub-µHa │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 0    │ HDAC6   │ SLSQP     │ 15.0        │ ❌      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 1    │ SARM1   │ SLSQP     │ 192.6       │ ❌      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 2    │ ClC-1   │ SLSQP     │ 0.237       │ ⭐      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 3    │ MFN2    │ SLSQP     │ 11.3        │ ❌      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 4    │ Cx32    │ SLSQP     │ 0.587       │ ⭐      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 5    │ c9orf72 │ SLSQP     │ 1.376       │ ❌      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 6    │ TBK1    │ SLSQP     │ 0.615       │ ⭐      │
├──────┼─────────┼───────────┼─────────────┼─────────┤
│ 7    │ KIF5A   │ L_BFGS_B  │ 0.023       │ ⭐⭐    │
└──────┴─────────┴───────────┴─────────────┴─────────┘
```

또는 markdown 표 (rendered) :

| iter | target  | optimizer | delta (µHa) | sub-µHa |
|------|---------|-----------|-------------|---------|
| 0    | HDAC6   | SLSQP     | 15.0        | ❌      |
| 1    | SARM1   | SLSQP     | 192.6       | ❌      |
| 2    | ClC-1   | SLSQP     | 0.237       | ⭐      |
| 3    | MFN2    | SLSQP     | 11.3        | ❌      |
| 4    | Cx32    | SLSQP     | 0.587       | ⭐      |
| 5    | c9orf72 | SLSQP     | 1.376       | ❌      |
| 6    | TBK1    | SLSQP     | 0.615       | ⭐      |
| 7    | KIF5A   | L_BFGS_B  | 0.023       | ⭐⭐    |

---

## 표 형식 규칙 (own 등록 reference)

1. **컬럼 헤더** — `iter | target | optimizer | delta (µHa) | sub-µHa` 형식 또는 동등 axis
2. **숫자 alignment** — 숫자 정밀도 통일 (`.3f` 또는 `.6f`)
3. **상태 emoji** — `❌` (FAIL) / `⭐` (PASS sub-µHa) / `⭐⭐` (best 또는 record) / `✅` (chem-acc OK)
4. **ASCII box-drawing** OR **markdown pipe-table** 둘 다 사용 가능
5. **paradigm 발견** 또는 **결과 분포** 명시 시 본 형식 우선

향후 리포트 (CMT/ALS/기타 disease 또는 양자 chemistry 진행) 시 본 sample 형식 적용.
