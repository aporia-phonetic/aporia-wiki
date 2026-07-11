# _common

*Source: `heterodyne/agents/writers_room/_common.py`*

agents/writers_room/_common.py

Shared plumbing for the writers'-room pipeline stages: the
retry-with-error-feedback call pattern (same discipline as the Dramatist's
segment loop, at stage granularity) and small helpers.

## Defined here

### `WritersRoomError`

Base class for writers'-room pipeline failures.

### `StageValidationError`

A stage's LLM output failed parsing/validation after all retries.

## Top-level functions

- **`call_with_retry()`** — Call the router and parse; on parse/validation failure, feed the error
- **`load_prompt()`** — Read a writers'-room prompt file (prompts/writers_room/<name>.txt).
- **`estimate_duration_seconds()`** — Words-per-minute duration heuristic — no LLM call needed.
