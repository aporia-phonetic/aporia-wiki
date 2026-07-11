# pipeline

*Source: `heterodyne/agents/writers_room/pipeline.py`*

agents/writers_room/pipeline.py

The writers'-room orchestrator — the opt-in alternative to the monolithic
Dramatist, selected by EpisodeConfig.script_pipeline == "writers_room"
(--pipeline writers-room / SCRIPT_PIPELINE=writers_room).

Per episode:
  1. Beat planner (one call) plans all four segments' scenes.
  2. Per scene, sequentially: actor intentions (parallel tiny calls) →
     scene writer (dialogue/narration only) → prose lint (free) →
     optional scene critic + one revision → optional blind voice
     attribution (regenerate once on convergence) → audio annotation.
  3. Per segment: ledger extraction over the finished text, then pure-code
     assembly into a validated SegmentScript.

Output contract: the same list of four SegmentScripts the Dramatist emits,
checkpointed in the same S{s}E{ee}/SEG{n}.json format — Archivist, Foley
Master, Voice Engine, Mixer, and all QA are untouched. Scene-level
intermediates live under S{s}E{ee}/wr/ for cheap resume.

Every LLM call routes through the shared LLMRouter with a wr_* call type,
so each stage is independently cloud or local via config/llm_routing.yaml.

## Top-level functions

- **`generate_episode()`** — Generate all four segments via the writers'-room pipeline.
