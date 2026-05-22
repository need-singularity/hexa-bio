# D116 docs-only attestation (2026-05-22)

All substrate code migrated to `hexa-lang/stdlib/bio/` (PRs #278 / #280 / #284 / #292 / #294 / #296 — all MERGED).

This repo now holds domain narrative only (markdown · physics derivation · spec · citation index · governance `.tape`).

Code home: `~/core/hexa-lang/stdlib/bio/` (D116 · `project.tape` @D d3).

## What was removed

The migrated substrate (verified byte-identical against `hexa-lang` `origin/main:stdlib/bio/` before deletion):

- 5 core axes — `quantum/` · `weave/` · `nanobot/` · `ribozyme/` · `virocapsid/`
- 19 expansion / sub-axes — `allosteric/` · `aptamer/` · `autac/` · `bifunctional/` · `capsid_assembly_modulator/` · `covalent/` · `covalent_degrader/` · `cryptic_pocket/` · `lytac/` · `macrocycle/` · `metallodrug/` · `molecular_glue/` · `oligonucleotide/` · `peptide/` · `ppi/` · `protac/` · `reversible_covalent/` · `ribotac/` · `rna_targeting_small_molecule/`
- bridges — `_hexa_bridge/` · `_python_bridge/` · `_qiskit_bridge/` · `_absorption_bridge/`
- harness + data — `selftest/` · `tests/` · `case_studies/` · `drylab/` · `LVAD/`
- entry points — `cli/` · `examples/`
- root substrate — `hexa_bio.hexa` (→ `bio.hexa`) · `install.hexa` · `crispr-gene-editing/verify_crispr-gene-editing.hexa`

## What stays (D116-compliant narrative)

- `docs/` · `proposals/` · `papers/` · `wetlab/` · `breakthroughs/` · `sessions/` · `incoming/`
- `AXIS/` (HIERARCHY governance + index narrative)
- domain landing pages — `bio-pharma/` · `biology/` · `biology-medical/` · `genetics/` · `medical-device/` · `synbio/` · `crispr-cas13-poc-diagnostic/`
- canon-extract dirs — `hexa-nanobot/` · `hexa-ribozyme/` · `hexa-virocapsid/` · `hexa-weave/`
- top-level narrative md + `.roadmap.*` dotfiles + governance `.tape`
- cross-domain narrative tapes (Q-1 unresolved) — `AGRICULTURE` · `APICULTURE` · `AQUACULTURE` · `BAKING` · `BIOCHAR-DRYLAND-RESTORATION` · `CHEESE-DAIRY` · `COFFEE` / `COFFEE-SCIENCE` · `ECOLOGY-AGRICULTURE-FOOD`
- `crispr-gene-editing/crispr-gene-editing.md` (narrative; sibling `.hexa` migrated)
