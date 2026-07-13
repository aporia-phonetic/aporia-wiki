# worldbuild_llm

*Source: `heterodyne/agents/worldbuild_llm.py`*

agents/worldbuild_llm.py — shared LLM entry for standalone world-building passes.

Character generation, the sourcebook narrative pass, and the Sediment
Engine's cheap re-runnable passes are one-shot system+user calls that were
written against the raw anthropic SDK, hardcoding the backend. This module
gives them a single routed entry point:

  * no injected client → LLMRouter call type (config/llm_routing.yaml decides
    the backend — cloud, local Ollama, openai-compat — with per-backend
    fallback, cost telemetry, and structured-output support)
  * injected anthropic-style client → used directly, unchanged legacy
    behavior (tests and explicit overrides stay authoritative)

Call types owned here (routes in config/llm_routing.yaml):
    character_generation    one character sheet as JSON
    sourcebook_narrative    present-day narrative / faction passes
    chronicle_gap_analysis  Sediment Engine gap check (cheap, re-runnable)

## Top-level functions

- **`complete_text()`** — One system+user completion, returning the raw text.
