# foley_master

*Source: `heterodyne/agents/foley_master.py`*

agents.foley_master — bridge from Dramatist intent to catalog entries.

Phase 3.7. Sits between the Dramatist (which emits structured FoleyIntent
on every block) and the Mixer (which consumes resolved catalog IDs).

Responsibilities:
  1. Walk every block in a generated episode
  2. For each FoleyIntent, query the catalog for the best CatalogEntry
  3. Write the chosen catalog_id into the block's foley_cues list
  4. On catalog miss (no family-matching entry available), optionally
     trigger the Sourcer to create one — gated by the master toggle
     and the Sourcer's own policies (license, spending cap)
  5. Produce a FoleyResolveReport summarizing what was matched, what
     was sourced, and what was left unresolved

Important design decisions:
  • The Foley Master does NOT modify Dramatist text or structure. It only
    populates foley_cues from foley_intent. Episode JSON written to disk
    contains both fields — the intent for audit, the cues for the Mixer.
  • Resolution is deterministic given the catalog state. Same catalog +
    same intent = same catalog_id chosen. Re-running on a committed
    episode is a no-op if all intents already resolved.
  • Catalog miss is NOT an error. The block is left with empty foley_cues
    and the report flags the gap. The Mixer handles missing cues
    gracefully (warning + skip).
  • When Sourcer triggers and produces new audio, the new catalog_id is
    used for the current block AND becomes available for future blocks
    in the same run (caching mid-episode).

## Defined here

### `FoleyMasterError`

Base class for Foley Master failures.

### `IntentResolution`

One intent → resolution outcome.

| Field | Type |
|---|---|
| `block_id` | `str` |
| `segment` | `int` |
| `intent` | `FoleyIntent` |
| `catalog_id` | `str | None` |
| `score` | `float` |
| `reason` | `str` |
| `sourced_this_run` | `bool` |

### `FoleyResolveReport`

Summary of a resolve_episode call.

| Field | Type |
|---|---|
| `total_intents` | `int` |
| `resolved` | `int` |
| `unresolved` | `int` |
| `sourced_this_run` | `int` |
| `sourcing_failures` | `int` |
| `spent_usd` | `float` |
| `per_intent` | `list[IntentResolution]` |

### `FoleyMaster`

Resolves Dramatist intents to catalog IDs.

Parameters
----------
catalog
    The FoleyCatalog instance backing the show. Required.
sourcer
    Optional BestOfThree orchestrator. When present and the master
    toggle is on (sourcer.master_enabled), missing catalog matches
    trigger automatic sourcing. When None, misses leave the block's
    foley_cues empty and the report flags the gap for human follow-up.
min_acceptable_score
    Threshold below which a catalog match is rejected as "too weak"
    and treated as a miss. Default 0.0 — accept anything the catalog
    family-filter returned. Raise this to 0.2-0.3 once the catalog
    is dense enough that low-quality matches become a problem.
