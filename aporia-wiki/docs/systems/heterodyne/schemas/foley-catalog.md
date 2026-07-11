# foley_catalog

*Source: `heterodyne/schemas/foley_catalog.py`*

Foley catalog — Pydantic models for the autonomous foley pipeline.

The catalog is the canonical library of atomic foley sounds. Each entry is
ONE sound (a single footstep, one drip, one lens-zoom click). Looping and
rhythmic placement are the Mixer's job, not the catalog's. Multi-event
recordings get trimmed via the existing FoleyManifest at mix time.

Lifecycle:
  1. Dramatist emits foley_intent on each block (category + context).
  2. Foley Master agent (Phase 3.7) maps intent → catalog_id.
  3. If the match is missing, Foley Sourcer agent (Phase 3.6) obtains it
     and registers in the catalog.
  4. Mixer (Phase 3.5) resolves catalog_id → file_path and renders.

Once an entry exists, it is reused indefinitely. The catalog is append-only
in normal operation; a manual delete is possible but not part of the
autonomous flow.

## Defined here

### `CatalogEntry`

One atomic foley sound in the library.

Stable across the whole show once registered. The Foley Master picks
these by family + tags + character affinity. The Mixer consumes them
by reading file_path.

Naming convention:
  catalog_id is `<family>_<descriptor>_<NNN>`, three-digit zero-padded
  sequence within the family. Examples:
    footsteps_stone_single_001
    atmosphere_atrium_long_001
    ticker_lens_zoom_001          (signature)
    resonance_pulse_low_001

| Field | Type |
|---|---|
| `catalog_id` | `str` |
| `family` | `FoleyFamily` |
| `description` | `str` |
| `duration_seconds` | `float` |
| `loopable` | `bool` |
| `rhythmic_default_interval_ms` | `int | None` |
| `rhythmic_default_jitter_ms` | `int` |
| `tags` | `list[str]` |
| `signature_for` | `list[str]` |
| `affinity_for` | `list[str]` |
| `source` | `CatalogSource` |
| `source_url` | `str | None` |
| `source_query` | `str | None` |
| `license` | `CatalogLicense` |
| `attribution` | `str | None` |
| `source_original_path` | `str | None` |
| `source_original_sha256` | `str | None` |
| `file_path` | `str` |
| `created_at` | `datetime` |
| `last_used_at` | `datetime | None` |
| `use_count` | `int` |
| `notes` | `str | None` |

### `CatalogQuery`

Foley Master's request to the catalog.

Built from a Dramatist block's foley_intent. The catalog returns
candidate entries ranked by how well they match.

| Field | Type |
|---|---|
| `family` | `FoleyFamily` |
| `context_keywords` | `list[str]` |
| `duration_target_seconds` | `float | None` |
| `active_character` | `str | None` |
| `exclude_signatures_for_others` | `bool` |

### `CatalogMatch`

One ranked candidate from the catalog.

| Field | Type |
|---|---|
| `entry` | `CatalogEntry` |
| `score` | `float` |
| `reason` | `str` |

### `CatalogStats`

Snapshot of catalog state. Used by tools and CLI status commands.

| Field | Type |
|---|---|
| `total_entries` | `int` |
| `entries_by_family` | `dict[str, int]` |
| `entries_by_source` | `dict[str, int]` |
| `entries_by_license` | `dict[str, int]` |
| `entries_by_status` | `dict[str, int]` |
| `signature_entries` | `int` |
| `most_used` | `list[tuple[str, int]]` |
