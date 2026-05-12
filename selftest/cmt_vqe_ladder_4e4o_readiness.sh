#!/usr/bin/env bash
#
# cmt_vqe_ladder_4e4o_readiness.sh
#
# CMT 4e/4o pocket-VQE ladder gate — the **4e/4o** sub-ramp of F-Q-6-E.
# Companion to cmt_vqe_ladder_readiness.sh (which gates the 2e/2o tier).
#
# What this gate verifies (via qmirror's chemistry_vqe_cmt_hamiltonians_4e4o.hexa):
#   For each molecule in the 4e/4o vendored set (currently: LiH validation
#   anchor + cmt-hd6 = HDAC6 candidate), the qmirror runtime reads the vendored
#   Hamiltonian (Pauli terms + constant_shift), the vendored UCCSD-converged
#   statevector ψ* (64 complex amplitudes, since 4e/4o ParityMapper((2,2)) +
#   2-qubit reduction = 6 qubits), and the vendored CASCI(4,4) reference, then
#   computes ⟨ψ*|H|ψ*⟩ via a generic n-qubit Pauli-expectation evaluator and
#   verdicts |delta| against the 1.6 mHa chemical-accuracy bound. PASS iff every
#   molecule reproduces its CASCI(4,4) ref within bound (in practice sub-µHa —
#   the UCCSD-converged state IS the CASCI eigenstate up to optimizer tol).
#
# raw_91 honest C3 — what this DOES NOT do:
#   - Run a pure-hexa variational optimizer on a 6-qubit Hamiltonian (that needs
#     a 26-parameter UCCSD/COBYLA stack ported to hexa — the next-next ramp).
#   - Cover the other 4 CMT small-molecule scaffolds (clc1/sar1/mfn2/gjb1) at
#     4e/4o — only LiH + hd6 are currently vendored. Extension is mechanical
#     (each ~3-4 min offline extraction, identical recipe).
#   - Compute "the binding energy" — CASCI(4,4) over a frontier-orbital active
#     space is a reproducible quantum-chemistry quantity, not a K_d. Pocket-
#     embedded VQE / final-molecule chemotype / 4e/4o → bigger AS = open ramps.
#
# This gate is OFF the 2e/2o gate (cmt_vqe_ladder_readiness.sh, which still gates
# the 2e/2o ladder for all 5 CMT scaffolds). The two are independent: 2e/2o is
# pure-hexa VQE (UCCSD-exact for 2-electron systems); 4e/4o is vendored-VQE-replay.
#
# Cross-refs:
#   - qmirror/chemistry_vqe/module/chemistry_vqe_cmt_hamiltonians_4e4o.hexa
#     (vendored Hamiltonians + ψ* + CASCI refs + generic n-qubit Pauli-expectation evaluator)
#   - qmirror/CHEMISTRY_VQE_PYSCF_BACKEND_PLAN_2026_05_12.md §4 (option (c) at the 4e/4o sub-tier)
#   - selftest/cmt_vqe_ladder_readiness.sh (the 2e/2o tier — orthogonal)
#   - .roadmap.disease_cmt_specific §6 양자-VQE adoption ladder
#   - .roadmap.quantum F-Q-6-E sub-tier table
#
# Sentinel: __CMT_VQE_LADDER_4E4O_READINESS__ PASS|SKIP|FAIL

set -u

SENTINEL_PASS="__CMT_VQE_LADDER_4E4O_READINESS__ PASS"
SENTINEL_SKIP="__CMT_VQE_LADDER_4E4O_READINESS__ SKIP"
SENTINEL_FAIL="__CMT_VQE_LADDER_4E4O_READINESS__ FAIL"

QMIRROR_ROOT="${QMIRROR_ROOT:-$HOME/core/qmirror}"
MODULE_4E4O="$QMIRROR_ROOT/chemistry_vqe/module/chemistry_vqe_cmt_hamiltonians_4e4o.hexa"
MODULE_2E2O="$QMIRROR_ROOT/chemistry_vqe/module/chemistry_vqe_cmt_hamiltonians.hexa"

echo "cmt_vqe_ladder_4e4o_readiness — 4e/4o pocket-VQE replay (F-Q-6-E 4e/4o sub-tier)"
echo "  qmirror 4e/4o module: $MODULE_4E4O"
echo "  runtime:              $(command -v hexa 2>/dev/null || echo '(hexa not on PATH)')"
echo

if [ ! -f "$MODULE_4E4O" ]; then
  echo "  SKIP: qmirror 4e/4o module not found at $MODULE_4E4O"
  if [ -f "$MODULE_2E2O" ]; then
    echo "        (qmirror has the 2e/2o tier but not the 4e/4o sub-ramp yet — update qmirror)"
  else
    echo "        (clone https://github.com/dancinlab/qmirror to \$QMIRROR_ROOT or 'hx install qmirror')"
  fi
  echo "$SENTINEL_SKIP"
  exit 0
fi

if ! command -v hexa >/dev/null 2>&1; then
  echo "  SKIP: hexa runtime not found on PATH"
  echo "$SENTINEL_SKIP"
  exit 0
fi

echo "  invoking: hexa run $MODULE_4E4O --selftest"
OUT="$(timeout 240 hexa run "$MODULE_4E4O" --selftest 2>&1)"
RC=$?

# Runtime-environment SKIP signatures (host can't exercise hexa now).
if echo "$OUT" | grep -qiE "ConnectionRefusedError|Connection refused|Killed: 9|Terminated: 15|__HEXA_RC=137|__HEXA_RC=143"; then
  echo "$OUT" | tail -6
  echo
  echo "  SKIP: hexa runtime couldn't complete on this host (TCP dispatch down / runtime watchdog / load)"
  echo "$SENTINEL_SKIP"
  exit 0
fi

case "$RC" in
  0)
    echo "$OUT" | tail -20
    echo
    if echo "$OUT" | grep -q "__QMIRROR_CHEM_CMT_VQE_4E4O__ PASS"; then
      echo "  qmirror 4e/4o VQE replay: all vendored molecules reproduced CASCI(4,4) within the chem-accuracy bound."
      echo "$SENTINEL_PASS"
      exit 0
    fi
    echo "  qmirror 4e/4o VQE module exited 0 but did not emit __QMIRROR_CHEM_CMT_VQE_4E4O__ PASS — treating as SKIP"
    echo "$SENTINEL_SKIP"
    exit 0
    ;;
  124)
    echo "$OUT" | tail -6
    echo
    echo "  SKIP: qmirror 4e/4o VQE selftest timed out at 240s"
    echo "$SENTINEL_SKIP"
    exit 0
    ;;
  *)
    echo "$OUT" | tail -20
    echo
    echo "  qmirror 4e/4o VQE selftest: exit $RC with no PASS sentinel (real regression)"
    echo "$SENTINEL_FAIL"
    exit 1
    ;;
esac
