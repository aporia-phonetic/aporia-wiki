# agent

*Source: `heterodyne/agents/dramatist_local/agent.py`*

agents.dramatist_local.agent — LocalDramatist orchestrator.

Same output contract as the cloud Dramatist (list[SegmentScript]); entirely
different generation internals: beat sheet -> plain-prose continuation loop
-> deterministic parse -> metadata annotation -> structured extraction.

Stage ordering minimizes Ollama model swaps: the writer model does the beat
sheet and every segment's prose first, then the annotator model handles all
annotation/extraction. This works because segment N+1 only needs segment
N's closing hook, which comes from the prose stage.

Orchestration is a plain Python loop (no LangGraph): dynamic segment count,
nested per-beat loops, metadata-mode branches, and (M5) judge-driven
regeneration are trivial as loops and awkward as a static graph; the cloud
path keeps its graph untouched.

## Defined here

### `LocalDramatist`

Multi-pass, fully-local episode script generator.
