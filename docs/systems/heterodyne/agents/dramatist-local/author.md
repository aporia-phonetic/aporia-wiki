# author

*Source: `heterodyne/agents/dramatist_local/author.py`*

agents.dramatist_local.author — author metadata mode (the schema-tax A/B).

Same continuation structure as writer.py, but each batch call asks the
writer model for full SceneBlock JSON (creative writing + production
metadata in one token stream) — a direct test of the rewrite brief's
hypothesis that the schema burden, not model size, caps density and causes
JSON failures. A batch that stays invalid after retries degrades to
plain-prose for that batch (parsed like derive mode) instead of killing
the run, so the A/B still completes and the failure count is measurable.

## Defined here

### `AuthorResult`

Author-mode counterpart of writer.SegmentProse (adds .blocks).

| Field | Type |
|---|---|
| `segment` | `int` |
| `transcript` | `str` |
| `hook` | `str` |
| `batches` | `int` |
| `beats_completed` | `int` |
| `blocks` | `list[dict]` |
| `degraded_batches` | `int` |

## Top-level functions

- **`generate_segment_blocks()`** — Author-mode continuation loop for one segment.
- **`generate_episode_blocks()`** — Author-mode blocks for every segment, chaining hooks (writer.py parity).
