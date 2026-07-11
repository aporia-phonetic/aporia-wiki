# wrecker

*Source: `heterodyne/agents/wrecker.py`*

agents/wrecker.py — the Wrecker, an adversarial auditor.

Founding assumption: every plan, projection, system, and pipeline output is
WRONG until proven otherwise. The Wrecker does not balance — it prosecutes.
It receives a target and returns a WreckerReport: a structured prosecution
file identifying fragile assumptions, broken claims, load-bearing failures,
and the questions the target never asked.

Structural sibling of agents/qa_validator.py (the Parallax layer), but with the
evaluative posture inverted: where Parallax validates episode segments, the
Wrecker prosecutes plans, projections, schemas, and system output. Surface 2
(production) overlaps with the Parallax adversarial agent on purpose — for
episode QA, prefer Parallax; the Wrecker's distinct value is the financial /
strategy / schema surfaces, which nothing else audits.

LLM contract
------------
The agent is client-agnostic. It depends only on an `llm_client` exposing
`complete(system: str, messages: list[dict]) -> response`, where `response`
has `.content` (str) and, ideally, `.input_tokens` / `.output_tokens` (int)
for cost accounting. This is the same protocol the Dramatist and Parallax use,
so AnthropicLLM / MockLLM / OllamaLLM from agents.dramatist all work. The GUI
worker passes an AnthropicLLM (Claude Sonnet) — adversarial reasoning is the
canonical "edge case / high-reasoning" use the local-first policy reserves for
cloud. Post-hardware, an OllamaLLM (local 70B) can be passed instead with the
price constants set to 0.0.

Cost tracking
-------------
Mirrors the Dramatist: cumulative `total_input_tokens` / `total_output_tokens`
× list prices → `total_cost_usd()`. Each report also carries the cost of just
its own audit.

This file is additive. It modifies no existing agent.

## Defined here

### `WreckerError`

Raised when an audit cannot be completed (e.g., unparseable output).

### `WreckerAgent`

Adversarial auditor. Assumes everything is wrong.

Returns prosecution files (WreckerReport), not balanced reviews.

Parameters
----------
llm_client:
    Any object with a `complete(system, messages)` method returning an
    object with a `.content` str attribute (and ideally `.input_tokens` /
    `.output_tokens` ints). Same protocol as the Dramatist / Parallax.
ledger_db_path:
    Optional path to a world_ledger.db, for production/schema audits that
    want to cross-check against world state. Unused in the Phase-1 on-demand
    path; accepted for forward-compatibility.
state:
    Optional AppState (or any object), passed through for context. Not
    required for on-demand audits.
input_price_per_mtok, output_price_per_mtok:
    List prices used for cost accounting. Default to Claude Sonnet. Pass 0.0
    for a local (Ollama) backend.
