# parallax_qa_runner

*Source: `heterodyne/agents/parallax_qa_runner.py`*

agents/parallax_qa_runner.py

Invoker for the Parallax QA pipeline (agents/qa_validator.py).

Builds a `ParallaxValidator` per segment with a *fresh* LLM client routed
through the A7 LLMRouter under call_type="parallax_validator". Fresh
context means: the validator never inherits the Dramatist's accumulated
message history. Each Parallax call is constructed from scratch — system
prompt + single user message containing only the artifact and rubric.

Wired into main.py's `_run_generate()` as a post-generation, per-segment
observability pass, gated behind `episode_config.parallax_qa_enabled`
(--parallax-qa / PARALLAX_QA=1). Results are persisted to
data/qa_results/ and a `requires_regeneration` verdict logs WARN, but the
episode still commits as-is — actual auto-regeneration would need to hook
into the Dramatist LangGraph topology (this module's invocation contract
is unchanged so that wiring can still happen without redesign).

Usage:
    from agents.llm_router import get_default_router
    from agents.parallax_qa_runner import ParallaxQARunner

    runner = ParallaxQARunner(router=get_default_router())
    result = runner.validate_segment(
        segment_json=seg_json_str,
        ledger_json=ledger_json_str,
        segment_number=1,
        gate=plot_gate_dict,
    )
    if result.requires_regeneration:
        # caller decides what to do with result.regeneration_context
        ...

## Defined here

### `_RouterBackedLLMClient`

Adapter that satisfies the LLMClient protocol by delegating every
`complete()` call to a router under a fixed call_type.

Stateless by design — no message history, no conversation accumulation.
Each `complete()` invocation is independent. This is the mechanism by
which the Parallax validator gets a fresh context regardless of what
the Dramatist's client is doing concurrently.

### `ParallaxQARunner`

Run Parallax QA on a segment with a fresh LLM context.

The runner is constructed once per process; `validate_segment` is
called per segment. A new `ParallaxValidator` is built on every call
so no state leaks between segments either.

Parameters
----------
router:
    The shared `LLMRouter`. The runner pins all validator calls to
    `call_type="parallax_validator"` so spend can be retargeted via
    `config/llm_routing.yaml` without code changes.
