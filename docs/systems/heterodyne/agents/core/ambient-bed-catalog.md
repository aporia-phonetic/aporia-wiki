# ambient_bed_catalog

*Source: `heterodyne/agents/ambient_bed_catalog.py`*

agents.ambient_bed_catalog — in-memory catalog + scorer for A9.

Phase A scope (pre-hardware, isolated from the main pipeline):
  - Pure in-memory catalog seeded from `SEED_ENTRIES` below.
  - Scorer used by AmbientBedMaster to pick a bed_id from an
    AmbientBedQuery when no explicit override is supplied.
  - Every seed entry ships with `file_path=None` and `source="stub"` so
    the StubAmbientBedBackend renders pink-noise placeholders without
    any asset dependency. Real catalog audio is added by swapping
    `file_path` and `source` under a stable `bed_id` — scene metadata
    never changes.

Phase B will add SQLite persistence parallel to `agents.foley_catalog`
if the catalog grows large enough to warrant it. Until then, the seed
list is the source of truth.

## Top-level functions

- **`build_seed_catalog()`** — Build a fresh in-memory catalog from `SEED_ENTRIES`.
- **`score_entry()`** — Return the score for `entry` against `query`.
- **`best_match()`** — Return the single highest-scoring entry, or None if catalog is empty.
- **`resolve_explicit()`** — Look up an explicit bed_id. Returns None if not found or not given.
