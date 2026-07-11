# input_guardrail

*Source: `heterodyne/agents/input_guardrail.py`*

agents/input_guardrail.py

Pre-generation input guardrail for the Dramatist.

Screens the plot-gate dict and World Ledger payload BEFORE any expensive
Claude call. Two-stage check:

  Stage 1  — deterministic schema integrity (required gate keys, type checks).
             No LLM. Catches malformed input cheaply.

  Stage 2  — fast-SLM semantic screen, one call, three categories:
               injection         — prompt-injection strings in user-supplied text
               policy_violation  — explicit content / disallowed-topic seepage
               rating_drift      — payload pushes the episode outside its declared rating

Routed through LLMRouter under call_type="input_guardrail" so the spend
target is config-flippable to a local SLM (Qwen3-4B / Gemma E2B) once the
new GPU is online. On the current cloud-only rig the route lands on the
`guardrail` backend (a Haiku alias).

Not wired into the pipeline yet. The Dramatist call site at
`agents/dramatist.py:915` and the exception path at `main.py:683–692`
are added by the post-hardware-transition wiring plan.

The `DramatistInputRejected` exception is defined here for the wiring
plan to import; nothing raises it today.

## Defined here

### `GuardrailResult`

Verdict from the input guardrail.

`passed` is True only when both stages cleared. `failure_kind="ok"`
pairs with `passed=True`; any other value pairs with `passed=False`.

| Field | Type |
|---|---|
| `passed` | `bool` |
| `failure_kind` | `FailureKind` |
| `evidence` | `str` |

### `DramatistInputRejected`

Raised (by the future wiring plan) when the guardrail blocks a run.

Carries the `GuardrailResult` so callers can log the failure_kind and
evidence without re-running the guardrail.

### `InputGuardrail`

Fast pre-generation screen for plot gate + ledger payload.

Parameters
----------
router:
    Shared `LLMRouter`. Calls pin to `call_type="input_guardrail"` so
    the backend can be retargeted via `config/llm_routing.yaml` once a
    local SLM is available.
