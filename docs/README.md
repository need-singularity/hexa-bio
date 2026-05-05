# hexa-bio docs

## n6-architecture sister-domain specs (canonical)

The 4 verb specifications (WEAVE / NANOBOT / RIBOZYME / VIROCAPSID) live in
the `n6-architecture` project under `domains/biology/`. The files in
[`n6/`](./n6/) are **symlinks** to those canonical sources — edits made on
either side propagate immediately, so this directory tracks live spec state.

| Verb        | Local link                                 | Canonical source                                                   |
|-------------|--------------------------------------------|--------------------------------------------------------------------|
| WEAVE       | [`n6/hexa-weave.md`](./n6/hexa-weave.md)           | `~/core/n6-architecture/domains/biology/hexa-weave/hexa-weave.md`         |
| NANOBOT     | [`n6/hexa-nanobot.md`](./n6/hexa-nanobot.md)       | `~/core/n6-architecture/domains/biology/hexa-nanobot/hexa-nanobot.md`     |
| RIBOZYME    | [`n6/hexa-ribozyme.md`](./n6/hexa-ribozyme.md)     | `~/core/n6-architecture/domains/biology/hexa-ribozyme/hexa-ribozyme.md`   |
| VIROCAPSID  | [`n6/hexa-virocapsid.md`](./n6/hexa-virocapsid.md) | `~/core/n6-architecture/domains/biology/hexa-virocapsid/hexa-virocapsid.md` |

`hexa-bio` is the empirical companion to `n6-architecture/domains/biology/`
— specs (theoretical, n=6 invariant projection, falsifier preregister)
stay in `n6-architecture`; numerical sandbox + CLI implementation lives
here. Both must agree at MVP gate 2026-07-28.
