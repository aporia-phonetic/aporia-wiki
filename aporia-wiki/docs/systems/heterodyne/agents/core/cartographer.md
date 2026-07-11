# cartographer

*Source: `heterodyne/agents/cartographer.py`*

Cartographer Agent — Tactical map generation for locations.

Generates tactical location maps using Claude integration, parsing
structured map output into LocationMap schema objects. Also persists
parsed maps into the per-world ``world_ledger.db`` map_* tables for
SVG / VTT export.

## Defined here

### `CartographerAgent`

Generate tactical location maps using Claude.
