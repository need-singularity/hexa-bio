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
# BIOCHAR-DRYLAND-RESTORATION.log.tape — append-only event history (v1.2 split)
# Sibling: BIOCHAR-DRYLAND-RESTORATION.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A rewrite_from_lattice_tautology := "BIOCHAR-DRYLAND-RESTORATION.tape rewritten from lattice-tautology stub into real biochar-soil-science SSOT" :: rewrite [ok d=2026-05-16]
  origin = "BIOCHAR-DRYLAND-RESTORATION.tape was a fabricated lattice-tautology stub from the hexa-bio mass-split (commit 153b5a2): hundreds of lines of `@D row_* / @D b_*` entries asserting biochar and dryland-restoration quantities as lattice-derived constants (char yield, CEC, permanence, yield uplift — all with `hexa_biochar_mk1_physical_limit` fields and zero real agronomy citations driving the claims). n=6 lattice presented as the derivation framework for soil science. Stub deleted in full."
  authored = "Hand-written with real biochar/soil/dryland-restoration science + landmark literature. Replaced the stub with: slow-pyrolysis thermochemistry and char-yield envelope (Antal & Grønli 2003 IECR 42:1619); Terra Preta origin and archaeological context with explicit temporal/geographic transfer-risk caveats (Glaser/Lehmann/Zech 2002 · Lehmann & Joseph 2009/2015 textbook); honest CEC, water-holding-capacity, microbiome, and nutrient-retention effects with per-mechanism heterogeneity acknowledgement; biochar yield-response meta-analysis with explicit high-heterogeneity framing (Jeffery et al. 2011 AgEE 144:175–187; Crane-Droesch et al. 2013 ERL 8:044049 — tropics >> temperate; soil-type and management dependence explicit); carbon sequestration potential with production-footprint and permanence-conditionality caveats (Woolf et al. 2010 NatComm 1:56; Singh et al. 2012 GCB 18:2659); dryland restoration landscape techniques (FMNR/Niger case, half-moon ridges, check dams, sand-dune stabilisation — Reij & Garrity 2016 era); South Africa invasive-biomass feedstock context with honest stacked-value-hypothesis caveat. Five @D :: real-limit anchors: yield heterogeneity not universal positive (lim_yield_heterogeneity); pyrolysis energy HARD cost (lim_pyrolysis_energy); permanence conditional on soil+climate (lim_permanence_conditional); biomass feedstock competition (lim_biomass_competition); transport costs limit deployment density (lim_transport_cost). Three falsifiable @D :: prediction entries with explicit falsifiers."
  hype-discipline = "Biochar is explicitly hype-prone (prominent in scope_disclaimer and dom_yield_response). Meta-analysis mean (~10–16%) reported WITH its high between-study variance and moderating factors explicitly named. Woolf 2010 1.8 Gt/yr upper-bound framed as theoretical maximum under sustainable-biomass assumptions, not a current trajectory. Terra Preta lessons qualified for soil/climate transfer risk. WfW+biochar stacking hypothesis labelled plausible but unconfirmed at commercial scale. No numbers fabricated — all ranges and qualitative comparisons are paraphrased from cited literature with author/era flagging where exact bibliographic details are not asserted."
  n6-stance = "Declined as a derivation tool. @F f_lattice_fit + @N n6_honest_stance state plainly: biochar science exposes NO natural n=6 invariant — char yield, yield responses, sequestration rates, Terra Preta properties, and dryland restoration techniques are empirically determined / archaeologically reconstructed / field-documented, not lattice-derived. This honesty is the corrective for the audited lattice-tautology stub."
  governance = "Complies with hexa-bio AGENTS.tape @D g1 (real-limits-first — every @D anchored to real @X citations), @D g2 (lattice-is-tool — declined here), @D g8 (in-silico-only-claim-scope — @N scope_disclaimer: knowledge SSOT, NOT soil-amendment protocol / carbon-credit promise / regulatory claim), @F f1 (no lattice-fit on external science). Three citations (Jeffery 2011, Crane-Droesch 2013, Woolf 2010) are high-confidence with full bibliographic detail. Three (Antal & Grønli 2003, Singh et al. 2012, Glaser/Lehmann/Zech 2002) are specific known papers. Two (Lehmann & Joseph textbook, Reij & Garrity 2016) are author/era flagged where textbook edition or full page range not asserted."
  lint = "python3 selftest/tape_lattice_honesty_lint.py BIOCHAR-DRYLAND-RESTORATION.tape --json → __TAPE_LATTICE_HONESTY__ PASS (has_guard=true, has_stance=true, grounded=true; deriv_warnings = guard/stance provenance lines only, no genuine lattice-derivation lines)."
