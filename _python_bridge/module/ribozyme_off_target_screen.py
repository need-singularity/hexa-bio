#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ribozyme_off_target_screen.py — deterministic stdlib-only Hamming-distance
off-target screen for ribozyme substrate-recognition arms.

Closes the in-repo portion of AXIS_CLOSURE_PLAN.md §3 / G26-RB-3 component (3):
the "off-target screen" stub is replaced with a real Hamming sliding-window
scan against a representative reference-mRNA pool. The MFE-port portion of
G26-RB-3 (component (2)) was already closed by `ribozyme_mfe_nussinov.py`
on 2026-05-12 (R-R1).

Algorithm:
  For each substrate-recognition arm a (the 5' or 3' antisense arm of the
  ribozyme), scan every reference mRNA m in the pool with a sliding window
  of length len(a):
      hits[a] = #{ window w in m : Hamming(w, a)         ≤ seed_tolerance }
              + #{ window w in m : Hamming(w, rc(a))     ≤ seed_tolerance }
  where rc() is the reverse complement on RNA (A↔U, G↔C). Sum across the
  pool → off_target_count(a). Normalize by pool size in kb →
  off_target_per_kb(a). PASS gate: off_target_per_kb(a) ≤ MAX_PER_KB_GATE
  for each arm.

Pool (raw#10 honest C3): the in-repo reference pool is a small
deterministic representative seed (~5 canonical AML-relevant human mRNA
fragments, ~100 nt each) chosen to exercise the algorithm with both
housekeeping (ACTB, GAPDH) and oncogene (MYC, KRAS, TP53) strata, PLUS one
synthetic low-complexity (CUG)ₙ triplet-repeat decoy representing the
low-complexity off-target stratum (real ASO/ribozyme off-target concern —
DMPK-style CUG expansions, CAG repeats, etc.). This is NOT a full
host-transcriptome backing — production screens use an external GenCode /
RefSeq DB. The in-repo portion closes the *algorithm + protocol*; the
full-corpus run remains out-of-repo (R5 sunset).

Deterministic: stdlib only, no network/time/random/env. Re-running on the
same inputs produces byte-identical output → §11 deductive verification
contract.
"""

from __future__ import annotations
from typing import Dict, List, Tuple
import sys


# ── Reference pool: small canonical AML-relevant seeds (deterministic) ──
# These are ~100 nt fragments lifted from canonical mRNA references; the
# *exact* sequences are intentionally small to keep the in-repo pool
# minimal. Production pool replaces this with full GenCode/RefSeq.
_POOL: List[Tuple[str, str]] = [
    ("ACTB_seed_5prime_UTR",
     "AGACGCCATCGCCCCCAGCCCCAGCCCCAGCCCGGGGCCCAACAGCCCCGGCAUCGACUUCCAUGGCCACGGCUGCUUCCAGCUCCUCCCC"),
    ("GAPDH_seed_CDS",
     "AGGUCAUCCAUGACAACUUUGGUAUCGUGGAAGGACUCAUGACCACAGUCCAUGCCAUCACUGCCACCCAGAAGACUGUGGAUGGCCCCU"),
    ("MYC_seed_3prime_UTR",
     "AGGCUUGAAAGAGAGGGGGUGGGUAUUUACUUUAAACAGCAAGGGAGCGUGCAGCGGAAACUUAGGCAUUUAUUUGUUUUUUUUUGCUCC"),
    ("KRAS_seed_CDS_codons1_30",
     "AUGACUGAAUAUAAACUUGUGGUAGUUGGAGCUGGUGGCGUAGGCAAGAGUGCCUUGACGAUACAGCUAAUUCAGAAUCAUUUUGUGGAC"),
    ("TP53_seed_DBD_codons150_180",
     "GCCGCCUGAGGUUGGCUCUGACUGUACCACCAUCCACUACAACUACAUGUGUAACAGUUCCUGCAUGGGCGGCAUGAACCGGAGGCCCAU"),
    # Synthetic low-complexity (CUG)n triplet-repeat decoy — NOT a real
    # transcript fragment; represents the low-complexity off-target stratum
    # (DMPK-style CUG expansions are a textbook ASO/ribozyme off-target trap).
    ("synth_low_complexity_CUG_repeat", "CUG" * 33 + "C"),
]


def reverse_complement(rna: str) -> str:
    table = str.maketrans("ACGU", "UGCA")
    return rna.translate(table)[::-1]


def hamming(a: str, b: str) -> int:
    if len(a) != len(b):
        raise ValueError(f"hamming: length mismatch {len(a)} vs {len(b)}")
    return sum(1 for x, y in zip(a, b) if x != y)


def _sanitize(seq: str) -> str:
    s = seq.upper().replace("T", "U")
    if not all(c in "ACGU" for c in s):
        bad = sorted({c for c in s if c not in "ACGU"})
        raise ValueError(f"non-RNA characters: {bad}")
    return s


def count_off_targets(arm: str, pool: List[Tuple[str, str]],
                      seed_tolerance: int = 1) -> Tuple[int, Dict[str, int]]:
    """Sliding-window Hamming scan of `arm` (and its reverse complement)
    against every mRNA in `pool`. Returns (total_hits, per_mrna_hits)."""
    arm = _sanitize(arm)
    rc = reverse_complement(arm)
    L = len(arm)
    total = 0
    per_mrna: Dict[str, int] = {}
    for mid, seq in pool:
        seq = _sanitize(seq)
        if len(seq) < L:
            per_mrna[mid] = 0
            continue
        c = 0
        for i in range(0, len(seq) - L + 1):
            w = seq[i:i + L]
            if hamming(w, arm) <= seed_tolerance:
                c += 1
            if rc != arm and hamming(w, rc) <= seed_tolerance:
                c += 1
        per_mrna[mid] = c
        total += c
    return total, per_mrna


def pool_size_kb(pool: List[Tuple[str, str]]) -> float:
    return sum(len(s) for _, s in pool) / 1000.0


def screen(arms_5prime_3prime: Tuple[str, str],
           pool: List[Tuple[str, str]] = None,
           seed_tolerance: int = 1,
           max_per_kb_gate: float = 4.0) -> Dict[str, object]:
    """Full screen.  Returns dict with per-arm counts, normalized rate, PASS flag."""
    if pool is None:
        pool = _POOL
    arm5, arm3 = arms_5prime_3prime
    pool_kb = pool_size_kb(pool)
    n5, by5 = count_off_targets(arm5, pool, seed_tolerance)
    n3, by3 = count_off_targets(arm3, pool, seed_tolerance)
    rate5 = n5 / pool_kb if pool_kb > 0 else 0.0
    rate3 = n3 / pool_kb if pool_kb > 0 else 0.0
    arm5_pass = rate5 <= max_per_kb_gate
    arm3_pass = rate3 <= max_per_kb_gate
    return {
        "arm_5prime": arm5,
        "arm_3prime": arm3,
        "seed_tolerance": seed_tolerance,
        "pool_kb": pool_kb,
        "pool_size_n": len(pool),
        "max_per_kb_gate": max_per_kb_gate,
        "arm_5prime_hits": n5,
        "arm_3prime_hits": n3,
        "arm_5prime_per_kb": rate5,
        "arm_3prime_per_kb": rate3,
        "arm_5prime_pass": arm5_pass,
        "arm_3prime_pass": arm3_pass,
        "overall_pass": arm5_pass and arm3_pass,
        "per_mrna_5prime": by5,
        "per_mrna_3prime": by3,
    }


# ── self-check / demo ───────────────────────────────────────────────────

_DEMO_CASES = [
    # AML FLT3-ITD-targeting hammerhead — arms complementary to FLT3 mRNA
    # junction. Arms are deliberately distinct from any pool seed so off-target
    # count should be LOW (PASS).
    ("ribozyme.aml.flt3_itd.v1",       ("CGAAUUCC", "GAACUUCG")),
    # Pan-coronavirus N-protein-targeting — same logic, distinct from pool.
    ("ribozyme.pancov.n_protein.v1",   ("UCGAUUAG", "CGUACGAU")),
    # Synthetic low-complexity arm — both arms are (CUG)n-repeat octamers, i.e.
    # complementary to the synth_low_complexity_CUG_repeat pool entry at every
    # 3rd window. Expected to FAIL the gate decisively (per-kb hits ≫ gate) —
    # demonstrates the screen actually detects off-targets, and that designing
    # a ribozyme arm against a triplet repeat is correctly flagged.
    ("ribozyme.synthetic_offtarget.demo", ("CUGCUGCU", "GCUGCUGC")),
]


def _selfcheck() -> int:
    print("ribozyme_off_target_screen — Hamming-distance off-target screen (G26-RB-3 component 3)")
    print(f"  reference pool: {len(_POOL)} mRNAs, total {pool_size_kb(_POOL):.3f} kb "
          f"(housekeeping + oncogene strata)")
    print()

    # Algorithmic sanity (deductive):
    print("  [PASS] reverse_complement involution — rc(rc(s)) == s for canonical hammerhead core")
    s = "CUGAUGAGGCCG"
    assert reverse_complement(reverse_complement(s)) == s, "rc involution failed"
    print("  [PASS] hamming triangle inequality — H(a,c) ≤ H(a,b) + H(b,c) on a 3-seq probe")
    a, b, c = "AUCG", "AUGG", "GUGG"
    assert hamming(a, c) <= hamming(a, b) + hamming(b, c), "hamming triangle failed"
    print()

    fails = 0
    for label, (a5, a3) in _DEMO_CASES:
        r = screen((a5, a3))
        verdict = "PASS" if r["overall_pass"] else "FAIL"
        emoji = "✓" if r["overall_pass"] else "✗"
        # FAIL is the EXPECTED verdict for the synthetic_offtarget demo case —
        # we WANT the screen to flag a deliberately-designed off-targeter.
        expected_pass = label != "ribozyme.synthetic_offtarget.demo"
        algorithmic_ok = r["overall_pass"] == expected_pass
        if not algorithmic_ok:
            fails += 1
        mark = "PASS" if algorithmic_ok else "FAIL"
        print(f"  [{mark}] {label:<40} 5'={a5} 3'={a3}  "
              f"hits 5'/3' = {r['arm_5prime_hits']}/{r['arm_3prime_hits']}  "
              f"per-kb 5'/3' = {r['arm_5prime_per_kb']:.2f}/{r['arm_3prime_per_kb']:.2f}  "
              f"screen_verdict={verdict}  expected={'PASS' if expected_pass else 'FAIL'}")

    # Determinism check.
    r1 = screen(("CGAAUUCC", "GAACUUCG"))
    r2 = screen(("CGAAUUCC", "GAACUUCG"))
    if r1 == r2:
        print(f"  [PASS] determinism — byte-identical re-run")
    else:
        fails += 1
        print(f"  [FAIL] determinism — output drift")

    total = len(_DEMO_CASES) + 1  # 3 cases + determinism
    print()
    if fails == 0:
        print(f"  --- summary --- {total} / {total} PASS → verdict: PASS")
        print("  scope (raw#10 C3): algorithm + small representative pool only.")
        print("        Production full host-transcriptome screen is out-of-repo")
        print("        (GenCode / RefSeq backing → ~/core/nexus/sim_bridge/).")
        print("        In-repo G26-RB-3 component (3) is CLOSED.")
        print("__RIBOZYME_OFF_TARGET_SCREEN__ PASS")
        return 0
    print(f"  --- summary --- {fails} FAIL → verdict: FAIL")
    print("__RIBOZYME_OFF_TARGET_SCREEN__ FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(_selfcheck())
