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
# V1_1_0_HANDOFF.log.tape — append-only event history (v1.2 split)
# Sibling: V1_1_0_HANDOFF.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A meta_tape_honesty_rewrite := "V1_1_0_HANDOFF.tape — meta-mode honesty-lint compliance rewrite" :: rewrite [ok d=2026-05-16]
  starting-state = "Plain log scaffold (64 lines): @I id001 with no tape-class, no @F guard, no @N honest-stance, no @X citations. Linter would FAIL on all three clauses (guard, stance, grounding)."
  action = "Full rewrite to honesty-lint meta-mode compliance per AGENTS.tape g_meta_mode_optin (d=2026-05-16). tape-class = 'meta/handoff' added to @I id001 triggering meta-mode in the linter."
  preamble-added = "§0 honesty preamble inserted after @I id001: (1) @F f_lattice_fit := 'lattice-fit-in-handoff-entries' :: governance [required deny:write] — declares checklist lattice tokens as descriptive provenance (artifact names), not derivation; (2) @N n6_honest_stance := 'handoff lattice mentions are provenance, not derivation' :: note [required] — plain honest statement that handoff asserts no science from the lattice; (3) @N scope_disclaimer — in-silico-only reminder preserved from sibling-md."
  content-preserved = "TRUE. All genuine v1.1.0 handoff checklist entries reproduced from V1_1_0_HANDOFF.md: C0b 4-verb PASS, C0a collision audits, Bayesian audits, cycle-25 follow-ons, pending user decisions (approve release notes, version bump, git tag/push), out-of-repo items (F-NB-5, canon kicks, C3+ wet-lab). No entry invented, none deleted."
  citations-added = "@X x_lattice_policy :: governance · @X x_agents_tape :: governance · @X x_handoff_md :: doc · @X x_release_notes :: doc. The two governance @X entries satisfy meta-mode clause 3 (grounding) per linter logic (is_meta=true branch)."
  log-created = "V1_1_0_HANDOFF.log.tape created (this file) as the append-only event history sibling per AGENTS.tape g_arch_vs_log_split."
  lint = "python3 selftest/tape_lattice_honesty_lint.py V1_1_0_HANDOFF.tape --json → {verdict: PASS, has_guard: true, has_stance: true, grounded: true, is_meta: true, deriv_warnings: []}"
  verdict = "PASS. Clean — zero deriv_warnings, zero deriv_hits. All three clauses satisfied in meta-mode: guard (@F f_lattice_fit), stance (@N n6_honest_stance), grounding (@X x_lattice_policy and @X x_agents_tape :: governance)."
