# trajectory

*Source: `heterodyne/agents/trajectory.py`*

agents/trajectory.py

Cross-agent call-trajectory recorder for the AEON pipeline.

Captures the sequence of top-level agent calls during a single run and
lets a caller assert that sequence against an expected canonical
trajectory. Three match modes:

  EXACT      — recorded events must equal expected, in order, no extras.
  IN_ORDER   — every expected event appears at least once, in the given
               relative order. Recorded events may contain extras between
               or around them. Use when intermediate calls are optional.
  ANY_ORDER  — recorded events must contain every expected event at least
               once, order irrelevant.

This module is freestanding — it does not import from main.py or any
agent module. Insertion of record() calls into the pipeline is deferred
to the post-hardware-transition wiring plan. The CANONICAL_PIPELINE_TRAJECTORY
constant below is the source-of-truth vocabulary that wiring will use,
and that the batch-RunState slot identifiers (item 4) reuse.

## Defined here

### `TrajectoryViolation`

Raised when a recorded trajectory fails an assertion.

Subclasses AssertionError so existing test infrastructure that catches
assertion failures handles it naturally; also subclasses Exception so
runtime callers can catch it without depending on AssertionError
semantics.

### `TrajectoryRecorder`

Records the sequence of named events emitted during a pipeline run.

Thread-safe NOT guaranteed — AEON's pipeline is single-threaded per
episode, and the recorder is constructed per-run, so simultaneous
writes from multiple threads are out of scope.

| Field | Type |
|---|---|
| `events` | `list[tuple[str, datetime]]` |
