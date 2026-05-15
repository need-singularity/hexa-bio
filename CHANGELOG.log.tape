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
# CHANGELOG.log.tape — append-only event history (v1.2 split)
# Sibling: CHANGELOG.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A meta_tape_honesty_contract_pilot := "CHANGELOG.tape — META/changelog honesty-contract pilot (no meta exemption)" :: rewrite [ok d=2026-05-15]
  pilot = "FIRST application of user decision #1 (2026-05-15): META/doc tapes (changelog, plans) satisfy the SAME lattice-honesty contract as science tapes — NO exemption. CHANGELOG.tape is the pilot subject."
  starting-state = "Linter FAILed with 3 deriv_hits, ALL genuine repo history: L321 Ribozyme G26-RB-2 entry naming the shipped feature 'J₂=24 reaction-coordinate quotient'; L613 F-CL-FORMAL-1 entry recording a Lean4 proof that σ(6)=1+2+3+6=12; L766 the v1.0.0 entry that itself flagged the lattice as *speculative*. None were fabricated science claims — all are descriptive provenance of past engineering work."
  preamble-added = "§0 honesty preamble inserted after @I id001 (before all historical entries): (1) @F f_lattice_fit := 'lattice-fit-in-changelog-entries' :: governance [required deny:write] declaring lattice tokens in historical entries are DESCRIPTIVE PROVENANCE (artifact names / proof subject / prior honesty caveat), not derivation; (2) @N n6_honest_stance := 'changelog lattice mentions are provenance, not derivation' :: note [required] stating plainly the changelog asserts no science from the lattice; (3) @I id001 gained tape-class = 'meta/changelog — honesty contract applied per user decision 2026-05-15 (no meta exemption)'."
  history-preserved = "TRUE. Every existing `text =` historical line is byte-for-byte unchanged. No entry deleted, none invented, no `[1.0.0]/[1.1.0]/...` section altered. Only ADDITIVE annotation: a `provenance =` body line on each of the 3 flagged entries (each statement is TRUE of that line — artifact-name / proof-subject / prior-caveat) and a `|>` grounding edge on the F-CL-FORMAL-1 entry."
  grounding = "Honest, option (a) — NOT a fabrication, but it required a judgement call worth recording. The F-CL-FORMAL-1 entry (L613) documents a landed Lean4 kernel proof of σ(6)=1+2+3+6=12. σ is the standard number-theoretic sum-of-divisors function; that proven fact genuinely rests on elementary number theory, NOT on the n=6 lattice. Grounded by a NEW @X x_hardy_wright_sigma :: literature with the REAL ref = Hardy & Wright, An Introduction to the Theory of Numbers, 6th ed., §16.7, and a |> edge from the F-CL-FORMAL-1 entry to it. The LATTICE_POLICY and AGENTS.tape @X entries are deliberately classified :: governance (NOT literature) and do NOT satisfy the grounding clause — no miscategorization."
  judgement-call = "EXPLICIT: a pure release-history changelog has no intrinsic scientific literature anchor. Grounding was reachable ONLY because ONE historical entry happens to document a number-theory proof, whose real source (Hardy & Wright) is honestly citable. Had no such entry existed, this changelog would have been PASS-incapable-honestly without fabricating a literature reference."
  lint = "python3 selftest/tape_lattice_honesty_lint.py CHANGELOG.tape --json → __TAPE_LATTICE_HONESTY__ PASS (has_guard=true, has_stance=true, grounded=true; the 3 historical lattice lines downgraded to tolerated provenance WARNs, not FAIL)."
  verdict = "Meta-tape contract was honestly satisfiable FOR THIS PARTICULAR changelog — but only via a contingent number-theory anchor (one entry documented a σ(6) proof). It did NOT generalize cleanly: a changelog with zero literature-bearing entries would force either fabrication or honest-FAIL. Pilot finding: decision #1 is honest-compatible but fragile for meta tapes; recommend allowing a META-tape grounding mode (@X :: governance citing the enforcing policy + a methodological/spec ref) rather than requiring :: literature, OR formally accepting that some honest meta tapes will FAIL the literature clause by design. Flagged for the user to revisit decision #1's grounding clause as it applies to meta tapes."
