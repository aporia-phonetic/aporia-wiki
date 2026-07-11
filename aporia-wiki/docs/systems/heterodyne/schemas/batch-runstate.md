# batch_runstate

*Source: `heterodyne/schemas/batch_runstate.py`*

schemas/batch_runstate.py

Serializable batch-level RunState for the Anthropic Message Batches API.

The Dramatist already persists per-segment checkpoints
(`agents/dramatist.py:1704–1727`). What was missing — and what this
module adds — is a *batch-job-level* record: the Anthropic batch ID, the
per-custom-id slot completion state, and atomic on-disk persistence so
that an interrupted batch can be re-attached to the in-flight Anthropic
job on the server side rather than resubmitted from scratch.

Used by `BatchDispatcher.submit_episode_batch_tracked` and
`BatchDispatcher.resume_batch` (agents/batch_dispatcher.py).

Not invoked by the current pipeline. Wiring is deferred to the
post-hardware-transition integration plan, which will switch callers
from `submit_episode_batch` to `submit_episode_batch_tracked` and add a
`--resume-batch <id>` CLI flag.

## Defined here

### `RequestState`

Per-slot state for one custom_id within a batch job.

| Field | Type |
|---|---|
| `status` | `RequestStatus` |
| `result_path` | `Optional[Path]` |
| `error` | `str` |

### `RunState`

Durable record of one Anthropic batch submission.

Persisted atomically to `data/batch_runstate/{batch_id}.json` by the
tracked dispatcher path. On process restart, `resume_batch` loads this
file and skips resubmission — the Anthropic batch keeps processing
server-side regardless of client connectivity.

| Field | Type |
|---|---|
| `batch_id` | `str` |
| `submitted_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |
| `requests` | `dict[str, RequestState]` |

## Top-level functions

- **`default_runstate_dir()`** — Standard location for RunState files under the AEON-ENGINE tree.
- **`runstate_path_for()`** — Per-batch file path: `<runstate_dir>/<batch_id>.json`.
