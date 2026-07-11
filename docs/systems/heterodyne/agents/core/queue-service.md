# queue_service

*Source: `heterodyne/agents/queue_service.py`*

agents/queue_service.py

SQLite-backed per-agent work queue.

Each agent type gets its own logical queue, all stored in the same
agent_work_queue table in world_ledger.db.  Physical delivery uses a
filesystem inbox folder; this service tracks status so crashes are
recoverable and incomplete items can be retried.

Status lifecycle:
    pending → processing → completed
                        ↘ failed

## Defined here

### `QueueItem`

| Field | Type |
|---|---|
| `item_id` | `str` |
| `agent_type` | `str` |
| `input_path` | `Path` |
| `status` | `str` |
| `queued_at` | `str` |
| `started_at` | `Optional[str]` |
| `completed_at` | `Optional[str]` |
| `output_path` | `Optional[Path]` |
| `error` | `Optional[str]` |

### `AgentQueueService`

SQLite-backed work queue for a single agent type.

Args:
    db_path:    Path to world_ledger.db (or any SQLite file with the
                agent_work_queue table).
    agent_type: Identifier for the consuming agent (e.g. "novelist").
    inbox_dir:  Directory to scan for new work items.
