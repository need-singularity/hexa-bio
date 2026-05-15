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
# USER_ACTION_REQUIRED.log.tape — append-only event history (v1.2 split)
# Sibling: USER_ACTION_REQUIRED.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A honesty_lint_rewrite_2026_05_16 := "USER_ACTION_REQUIRED.tape — honesty-lint compliance rewrite (meta-mode opt-in)" :: rewrite [ok d=2026-05-16]
  starting-state = "Skeleton tape: @I id001 with no tape-class, no @F guard, no @N stance, no @X citations, no index entries. Linter would FAIL (missing @F lattice-fit guard, @N honest n=6 stance, grounding citation)."
  action = "Full rewrite to honesty-lint compliance under meta-mode opt-in (tape-class = 'meta/index')."
  changes-made = [
    "@I id001 updated: tape-class='meta/index' + rewritten-from provenance + methodology-cite grounding body line",
    "@N scope_disclaimer added: scope and constraint of this index stated explicitly",
    "9 @N idx_* pointer entries added: one per deferred-action item from USER_ACTION_REQUIRED.md §1-4, each with phase/status/owner + ?> edge to x_user_action_required_md",
    "@F f_lattice_fit added: guard against lattice-derivation in index entries",
    "@N n6_honest_stance added: observation-not-derivation stance (trivially holds — lattice has no role in CRO/IP/regulatory estimates)",
    "@X x_lattice_policy :: governance added (grounding clause satisfied for meta-mode)",
    "@X x_agents_tape :: governance added (notes g9+g10 deferral policy explicitly)",
    "@X x_user_action_required_md :: doc added (long-form sibling reference)"
  ]
  history-preserved = "TRUE. No original content was deleted — the prior skeleton contained only a comment block and a minimal @I id001. All additions are new. Index entries faithfully mirror USER_ACTION_REQUIRED.md §1-4 section content."
  lint = "python3 selftest/tape_lattice_honesty_lint.py USER_ACTION_REQUIRED.tape --json → __TAPE_LATTICE_HONESTY__ PASS (has_guard=true, has_stance=true, grounded=true, is_meta=true, deriv_warnings=[])"
  verdict = "PASS. Meta-mode grounding satisfied via methodology-cite body line on @I id001 + two @X :: governance citations. No literature anchor required or fabricated — correct for a pure external-action index. Zero deriv_warnings: lattice tokens are absent from index entries (they have no role here)."
