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
# DOG-ROBOT-TEST.log.tape — append-only event history (v1.2 split)
# Sibling: DOG-ROBOT-TEST.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A a_honesty_rewrite_2026_05_16 := "honesty-lint compliance rewrite" :: rewrite [ok d=2026-05-16]
  action = "Rewrote DOG-ROBOT-TEST.tape into honesty-lint compliance via meta-mode opt-in."
  tape-class-added = "meta/test-fixture"
  guards-added = ["@F f_lattice_fit", "@N n6_honest_stance", "@N scope_disclaimer"]
  citations-added = ["@X x_lattice_policy :: governance", "@X x_agents_tape :: governance"]
  lattice-tokens-neutralised = "Row stubs τ³=64배·σ=12배·τ=4배·τ(6)=4 정합·σ(6)=12·4서브×3계층=12블록 replaced with TODO/실측 placeholders; none were real measurements"
  prior-state = "scaffold template with all-TODO performance rows and unguarded lattice magnitude strings"
  authority = "[@x_agents_tape] g_meta_mode_optin · selftest/tape_lattice_honesty_lint.py"
  => "DOG-ROBOT-TEST.tape passes tape_lattice_honesty_lint.py --json with is_meta=true"
