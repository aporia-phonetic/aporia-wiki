# sediment_engine

*Source: `heterodyne/agents/sediment_engine.py`*

Sediment Engine — autonomous world history generation.

Generates a sequence of causally linked eras from an origin condition to a
present condition, persisting eras, historical events, figures, artifacts,
geography, linguistic sediment, mythology, and chronicle seeds to the per-world
``deep_ledger.db``.

This is the Chronicle-system implementation specified in
``docs/CHRONICLE_SYSTEM.md`` (as-built spec; the original
``AEON_CHRONICLE_SYSTEM.md`` it cited — the ``§1.2–1.7`` markers below —
was never committed and is lost).

## Defined here

### `WorldSeed`

Inputs to the Sediment Engine (Chronicle §1.2).

| Field | Type |
|---|---|
| `world_id` | `str` |
| `world_name` | `str` |
| `genre` | `str` |
| `description` | `str` |
| `magic_rule` | `str` |
| `origin_condition` | `str` |
| `present_condition` | `str` |
| `fundamental_tension` | `str` |
| `time_span_years` | `int` |
| `era_count_target` | `int` |
| `significant_figures_per_era` | `int` |
| `geography_seed` | `str` |
| `available_species` | `List[str]` |

### `ParsedEra`

| Field | Type |
|---|---|
| `era_id` | `str` |
| `name` | `str` |
| `duration_years` | `int` |
| `start_year` | `int` |
| `end_year` | `int` |
| `dominant_forces` | `str` |
| `end_condition` | `str` |
| `legacy` | `str` |
| `raw_output` | `str` |
| `events` | `List[Dict[str, Any]]` |
| `figures` | `List[Dict[str, Any]]` |
| `artifacts` | `List[Dict[str, Any]]` |
| `geographic_changes` | `List[Dict[str, Any]]` |
| `linguistic_seeds` | `List[Dict[str, Any]]` |

### `SedimentEngine`

Orchestrates sequential era generation for a world.

Persists everything into ``deep_ledger.db`` under
``data/worlds/{world_id}/`` (or a caller-supplied root).

## Top-level functions

- **`chronicle_summary()`** — Render a compact, prompt-ready digest of a world's deep history.
- **`world_state_at_year()`** — Construct a historical world-state snapshot at a given year.
- **`chronicle_summary_at_year()`** — chronicle_summary(), windowed to eras/events at or before target_year.
