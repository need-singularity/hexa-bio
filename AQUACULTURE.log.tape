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
# AQUACULTURE.log.tape — append-only event history (v1.2 split)
# Sibling: AQUACULTURE.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A rewrite_lattice_stub_to_real_science := "AQUACULTURE.tape full real-science rewrite from lattice-tautology stub" :: rewrite [ok d=2026-05-16]
  origin = "AQUACULTURE.tape was a ~380-line lattice-tautology stub (hexa-bio mass-split 153b5a2) containing rows of @D row_* with x=n_6 / hexa=σ·φ / n_6=σ=12 / EXACT values and Korean-language lattice-derivation prose. Zero real aquaculture science; zero citations."
  action = "Full rewrite 2026-05-16. All stub content deleted. Replaced with real-science SSOT grounded in published aquaculture/fisheries literature."
  content-added = "§1 global production (FAO SOFIA · finfish/shellfish landscape). §2 FCR definition and fishmeal/fish-oil dependency (Naylor et al 2000 framing · Tacon & Metian 2008). §3 disease pressure: sea lice (Lepeophtheirus salmonis; Torrissen et al 2013), ISA (ISAV; Chile 2007-2009 epizootic), EMS/AHPND (AHPND Vibrio parahaemolyticus PirAB toxin). §3 antibiotic use and Norwegian vaccination success (Lillehaug / Sommerset era). §4 system types: net-pen / pond / raceway / RAS / IMTA. §5 environmental footprint (Naylor 2000 canonical framing; nutrient loading; escapement genetics; bivalves as extractive). §6 five @D lim_* :: real-limit [ok required]: forage-fish ceiling (HARD), disease+escapement on open systems (HARD), nutrient loading benthic capacity (HARD), freshwater/land finitude (HARD), thermal tolerance climate sensitivity (HARD)."
  governance = "@F f_lattice_fit + @N n6_honest_stance — state plainly: aquaculture has no natural n=6 invariant. @N scope_disclaimer added: knowledge SSOT, not aquaculture-management advice (hexa-bio g8/f2). Three @D tp_* :: prediction with real falsifiers. Nine @X :: literature entries (mix of confident full-ref and primary-author/era-flagged where specific volume not asserted)."
  n6-stance = "Lattice declined as derivation tool. Aquaculture production species, FCR, disease categories, system types, and environmental metrics are EMPIRICAL — set by ecology, biology, and biogeochemistry, not σ/τ/φ/J₂. This honesty is the corrective for the audited lattice-tautology stub."
  lint = "python3 selftest/tape_lattice_honesty_lint.py AQUACULTURE.tape --json → __TAPE_LATTICE_HONESTY__ PASS (has_guard=true, has_stance=true, grounded=true; zero genuine derivation lines)"
