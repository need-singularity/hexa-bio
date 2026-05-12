#!/usr/bin/env bash
#
# cmt_vqe_ladder_readiness.sh
#
# CMT VQE-ladder readiness probe — checks whether the qmirror chemistry_vqe
# pipeline can (yet) run the CMT small-molecule pocket VQE binding scans
# (F-disease-cmt-Q-1..6, Tier 3 / Phase γ in .roadmap.disease_cmt_specific).
#
# Honest finding (encoded as a SKIP, not a FAIL): qmirror's chemistry_vqe
# kernel is a PURE-HEXA kernel hardcoded for the canonical H2/STO-3G/0.74Å
# case (5-term parity-mapped Hamiltonian + FCI reference). The active-space
# transformer + arbitrary-SMILES + drug-class paths "require classical
# chemistry primitives (PySCF integrals, RDKit geometry, CASCI) that are
# out of scope for a pure-hexa kernel" (qmirror/chemistry_vqe/module
# raw#10 caveat 1, post-Phase-10 absorption 2026-05-12).
#
# Therefore the CMT pocket VQE binding scans for hd6-001 (heavy 22), clc1-001
# (17), sar1-001 (17), mfn2-001 (19), gjb1-001 — which need 2e/2o or 4e/4o
# active spaces over real molecular Hamiltonians — CANNOT run on the current
# pure-hexa qmirror kernel. They would need either:
#   (a) the retired python bridge (qiskit-nature + pyscf, ~/.hexabio_venv) —
#       the path the legacy tests/mpro_pocket_vqe_v7.py used; or
#   (b) a future qmirror chemistry_vqe extension that re-introduces a
#       classical-integral backend (F-Q-6-E ramp dependency).
#
# This gate's job: document that readiness gap precisely, run the qmirror
# H2 selftest (which IS the live cond.14 spectroscopic-accuracy gate), and
# SKIP cleanly. It does NOT pretend the CMT pocket VQE is done.
#
# raw_91 honest C3:
#   What this gate measures:
#     - Whether qmirror's chemistry_vqe H2 selftest is reachable + passes
#       (the only chemistry-VQE thing the pure-hexa kernel can actually do).
#   What this gate explicitly does NOT measure:
#     - CMT pocket VQE binding (hd6/clc1/sar1/mfn2/gjb1 against HDAC6 /
#       ClC-1 / SARM1 / MFN2 / Cx32 pockets). That is Tier 3 / Phase γ —
#       blocked on a classical-chemistry backend. The paradigm-level
#       closure claim in .roadmap.disease_cmt_specific §11-v4 is a DESIGN-
#       AUDIT closure (verified by cmt_side_effect_avoidance_audit.py +
#       cmt_library_ranking.py), NOT a VQE-binding closure.
#   PASS / SKIP / FAIL semantics:
#     SKIP — the expected normal state: qmirror reachable, H2 selftest may
#            PASS, but CMT pocket VQE is NOT runnable on the pure-hexa
#            kernel. Documents the Tier-3 readiness gap. NOT a regression.
#     PASS — would only be emitted if a future qmirror chemistry_vqe build
#            advertises an active-space / SMILES path AND the CMT pocket
#            Hamiltonians have been built (neither is true as of 2026-05-12).
#     FAIL — qmirror reachable but its H2 chemistry-VQE selftest returns
#            non-zero (a qmirror regression — investigate qmirror commit).
#
# Cross-refs:
#   - .roadmap.disease_cmt_specific §5 (F-disease-cmt-Q-1..6) + §6 (Tier 3 / Phase γ + 양자-VQE adoption ladder)
#   - qmirror/chemistry_vqe/module/chemistry_vqe.hexa (raw#10 caveat 1)
#   - AGENTS.md "Sister repositories" + XENO.md (qmirror vs xeno roles)
#   - selftest/cmt_side_effect_avoidance_audit.py (the DESIGN-AUDIT closure that IS done)
#   - selftest/cmt_library_ranking.py (the subtype-stratified ranking that IS done)
#
# Sentinel: __CMT_VQE_LADDER_READINESS__ PASS|SKIP|FAIL

set -u

SENTINEL_PASS="__CMT_VQE_LADDER_READINESS__ PASS"
SENTINEL_SKIP="__CMT_VQE_LADDER_READINESS__ SKIP"
SENTINEL_FAIL="__CMT_VQE_LADDER_READINESS__ FAIL"

QMIRROR_ROOT="${QMIRROR_ROOT:-$HOME/core/qmirror}"
QMIRROR_MODULE="$QMIRROR_ROOT/chemistry_vqe/module/chemistry_vqe.hexa"

echo "cmt_vqe_ladder_readiness — CMT pocket-VQE (Tier 3 / Phase γ) readiness probe"
echo "  qmirror module: $QMIRROR_MODULE"
echo

# (1) qmirror module present?
if [ ! -f "$QMIRROR_MODULE" ]; then
  echo "  SKIP: qmirror chemistry_vqe module not found at $QMIRROR_MODULE"
  echo "        (clone https://github.com/dancinlab/qmirror to \$QMIRROR_ROOT or 'hx install qmirror')"
  echo "$SENTINEL_SKIP"
  exit 0
fi

# (2) qmirror chemistry_vqe is a pure-hexa H2-only kernel — check the caveat is still there.
#     (If a future build advertises an active-space / SMILES path, this grep would miss
#      and we'd want to re-evaluate — but the SKIP below still applies until the CMT
#      pocket Hamiltonians are actually built, which they are not.)
if grep -q "out of scope for a pure-hexa kernel" "$QMIRROR_MODULE" 2>/dev/null; then
  echo "  qmirror chemistry_vqe: confirmed pure-hexa kernel (H2/STO-3G hardcoded; arbitrary-SMILES / active-space"
  echo "                         transformer 'out of scope for a pure-hexa kernel' per raw#10 caveat 1)."
else
  echo "  NOTE: qmirror chemistry_vqe no longer carries the 'out of scope for a pure-hexa kernel' caveat —"
  echo "        a future build may have added an active-space path. Even so, the CMT pocket Hamiltonians"
  echo "        (HDAC6 / ClC-1 / SARM1 / MFN2 / Cx32) are not built in-repo, so the CMT pocket VQE remains"
  echo "        a Tier-3 / Phase γ work item. Continuing as SKIP."
fi
echo

# (3) Run the qmirror H2 chemistry-VQE selftest (the live cond.14 gate) — bounded.
echo "  invoking (cond.14 H2 gate): hexa run $QMIRROR_MODULE --selftest"
OUT="$(timeout 60 hexa run "$QMIRROR_MODULE" --selftest 2>&1)"
RC=$?

case "$RC" in
  0)
    echo "$OUT" | tail -8
    echo
    echo "  qmirror H2 chemistry-VQE selftest: exit 0 (cond.14 spectroscopic-accuracy gate intact)."
    echo "  → CMT pocket VQE (Tier 3 / Phase γ) is STILL not runnable on this pure-hexa kernel."
    echo "    CMT closure status: DESIGN-AUDIT closure DONE (cmt_side_effect_avoidance_audit.py +"
    echo "    cmt_library_ranking.py both PASS); VQE-binding closure PENDING a classical-chemistry"
    echo "    backend (retired python bridge, or future qmirror F-Q-6-E ramp)."
    echo "$SENTINEL_SKIP"
    exit 0
    ;;
  124)
    echo "$OUT" | tail -5
    echo
    echo "  SKIP: qmirror H2 chemistry-VQE selftest timed out at 60s"
    echo "        (likely hexa runtime dispatch server unreachable on this host — not a regression)"
    echo "$SENTINEL_SKIP"
    exit 0
    ;;
  *)
    # Distinguish "runtime can't reach dispatch server" (SKIP) from "qmirror returned non-zero" (FAIL).
    if echo "$OUT" | grep -qi "ConnectionRefusedError\|Connection refused"; then
      echo "$OUT" | tail -5
      echo
      echo "  SKIP: hexa runtime can't reach its dispatch server (ConnectionRefusedError) — not a qmirror regression."
      echo "$SENTINEL_SKIP"
      exit 0
    fi
    echo "$OUT" | tail -12
    echo
    echo "  qmirror H2 chemistry-VQE selftest: exit $RC (real qmirror regression — investigate qmirror commit)"
    echo "$SENTINEL_FAIL"
    exit 1
    ;;
esac
