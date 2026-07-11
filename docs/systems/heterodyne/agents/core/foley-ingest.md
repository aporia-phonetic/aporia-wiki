# foley_ingest

*Source: `heterodyne/agents/foley_ingest.py`*

agents.foley_ingest — the master-sort agent for a personal foley library.

Takes a directory of raw wav files (the user's ~6,000-file library) and turns
it into clean, consistent, searchable catalog entries:

  1. QUALITY  — agents.foley_quality scores each file; rejects are skipped,
                flags are kept but recorded.
  2. CONSISTENCY — accepted clips are silence-trimmed, loudness-normalized to
                a single target (LUFS), peak-limited, and resampled to one
                rate, then written into audio/foley_catalog/<family>/.
  3. SORT     — CLAP zero-shot picks the best FoleyFamily and the top tags
                (schemas.foley_taxonomy prompts).
  4. SEARCH   — the CLAP audio embedding is stored in the sidecar
                EmbeddingStore so the Foley Master can find it semantically.
  5. REGISTER — a CatalogEntry row is written to the existing catalog DB.

Two modes:
  • dry_run=True  (default): analyze + classify, write a report, touch nothing.
  • dry_run=False (--commit): also process audio, write files, register rows.

This module imports torch/transformers lazily (via ClapEncoder), so importing
it is cheap and the rest of HETERODYNE is unaffected on machines without CLAP.

## Defined here

### `IngestConfig`

| Field | Type |
|---|---|
| `quality` | `QualityConfig` |
| `target_sr` | `int` |
| `target_lufs` | `float` |
| `peak_ceiling_dbfs` | `float` |
| `trim_silence` | `bool` |
| `max_tags` | `int` |
| `tag_min_score` | `float` |
| `family_floor` | `float` |
| `name_weight` | `float` |
| `license` | `str` |
| `source_label` | `str` |
| `keep_channels` | `bool` |

### `IngestResult`

| Field | Type |
|---|---|
| `src_path` | `str` |
| `accepted` | `bool` |
| `catalog_id` | `str | None` |
| `family` | `str | None` |
| `family_score` | `float` |
| `tags` | `list[str]` |
| `duration_s` | `float` |
| `verdict` | `str` |
| `reasons` | `list[str]` |
| `written_path` | `str | None` |
| `error` | `str | None` |
| `source_sha256` | `str | None` |
| `duplicate_of` | `str | None` |
| `format_duplicate_of` | `str | None` |

### `IngestReport`

| Field | Type |
|---|---|
| `results` | `list[IngestResult]` |

### `FoleyIngestor`

Sorts and registers a raw foley library into the catalog.
