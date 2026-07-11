# dramatic_function_judge

*Source: `heterodyne/agents/dramatic_function_judge.py`*

agents/dramatic_function_judge.py

LLM-as-judge for the multi-turn dramatic-function success metric (Item 7).

Compares a generated episode (the list of four SegmentScript artifacts)
against its plot gate's stated narrative intent — the `dramatic_function`
and `closing_hook` fields — and returns a binary pass/fail with a short
evidence string and a numeric fulfillment score.

Distinct from Voice Sentinel (voice consistency, untouched) and Parallax
QA (structural / continuity / A5 rules). Voice Sentinel asks "does this
sound like Maren?" Parallax asks "did the gate advance and the dialogue
follow the rules?" The judge asks "did the EPISODE achieve the dramatic
function the gate promised?" — a higher-order narrative-quality gate
that nothing in the current pipeline performs.

Wired into main.py's `_run_generate()` right after `archivist.commit_episode`
returns, gated behind `DRAMATIC_FUNCTION_JUDGE_ENABLED=1` (default off).
The result is persisted to `data/qa_results/` and a failure logs WARN — this
is observability for showrunner review, NOT a regeneration gate.

## Defined here

### `DramaticFunctionResult`

Verdict from the dramatic-function judge.

- `passed`: binary — did the episode achieve the gate's stated intent?
- `evidence`: short rationale citing concrete episode events.
- `gate_fulfillment_score`: 0.0–1.0 confidence; thresholds left to
  the wiring plan to decide (e.g. <0.5 → block, 0.5–0.7 → warn).

| Field | Type |
|---|---|
| `passed` | `bool` |
| `evidence` | `str` |
| `gate_fulfillment_score` | `float` |

### `DramaticFunctionJudge`

Run one LLM-as-judge call per episode.

Parameters
----------
router:
    Shared `LLMRouter`. Pins all calls to
    `call_type="dramatic_function_judge"` so the backend is
    config-flippable via `config/llm_routing.yaml`.
