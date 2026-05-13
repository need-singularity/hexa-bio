# TAPE-AUDIT — hexa-bio

## A. Audit-class ledgers

- `state/markers/*.marker` — **992 markers** (actuation_simulation, aml_flt3_candidate, closure_*). Each is a one-shot run sentinel (no append-only event grain). Strong **Class-T** migration candidate — collapse 992 `.marker` files into one `state/runs.tape` with `@T <verb>` + `@R ok|err` per run.
- `state/discovery_absorption/registry.jsonl` — already JSONL, schema-tagged (`raw_77_virocapsid_calibration_v1`), cycle/phase/falsifier provenance. **Class-A + Class-D** in `.tape` terms (raw absorption events + datasets).
- `state/{hexa_bio_cli.log, qmirror_cli.log}` — CLI-loop trace.

## B. Identity surface

`AGENTS.md` defines repo agent role + `AXIS.md` declares the n=6 lattice axis position. No persistent agent-identity record. **Strong fit** for `hexa-bio/identity.tape` — `@I` declaration + axis pin + falsifier roster (F-VIROCAPSID-3, F-RB-4).

## C. Domain.md files

78 UPPERCASE.md domain files (AGRICULTURE, APICULTURE, AQUACULTURE, BAKING, BIO-PHARMA, BIOCHAR-DRYLAND-RESTORATION, BIOLOGY-MEDICAL, CANCER-THERAPY, CHEESE-DAIRY, COFFEE-SCIENCE, COSMETIC-SURGERY, ...). No `+`-meta-domains yet — gap. Each domain is a candidate for sibling `<DOMAIN>.tape` carrying `@P` promotions + `@T` per-run trace tied to the markdown narrative.

## D. Per-run/per-event history

`registry.jsonl` already streams ribozyme kinetics + virocapsid calibration. Markers stream actuation simulation. Both → **Class-T tape**:
- `@T phase=f-rb-4-mvp-kinetics <- @S model=hammerhead_minimal_12nt => @R ok`
- Append-only fits the ribozyme/virocapsid n=6 closure loop natively.

## E. Promotion candidates

- **n6 atoms** — Hückel aromaticity (`bt-1387`), photosynthesis equation (`bt-1391`) — verified n=6 laws ready to lift from `breakthroughs/*.md` to atom IDs.
- **hxc binaries** — ribozyme kinetic curves + virocapsid spectra are dataset-shaped; promote raw bytes via `tape_to_hxc`.
- **n12 cube cells** — verb-dir × scale-tier matrix (hexa-weave/nanobot/ribozyme/virocapsid × 6 scales) maps onto an n12 cube face cleanly.

## Verdict

**HEAVY** — 992 markers + structured JSONL absorption registry + 78 domains. Best ROI: collapse markers to `state/runs.tape`, then sibling `.tape` per top-N domain.
