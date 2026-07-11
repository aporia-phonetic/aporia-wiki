# llm_router

*Source: `heterodyne/agents/llm_router.py`*

agents/llm_router.py

A7 — Local-LLM Routing.

Routes each LLM call to the right backend based on call type. The
`LLMClient` Protocol and the client implementations
(`AnthropicLLM`/`OllamaLLM`/`OpenAICompatLLM`/`MockLLM`) live in
agents/llm_clients.py — this module is the dispatcher on top of them.

Why route at all:
    Dramatist segments need Claude (16-24k output, structured generation).
    IP-clearance semantic checks, cultural-integrity tags, voice-sentinel
    spot-checks — these are all cheap, narrow calls that a local 70B
    handles fine. Today on the old rig everything goes to Claude; once
    the new GPU is online and a local model is running, swapping their
    backends to 'local' in config/llm_routing.yaml redirects spend without
    a code change.

Call-type taxonomy (extend as new callers wire in):
    dramatist_segment      — episode-segment generation (cloud, structured)
    ip_clearance_semantic  — IP conflict semantic similarity check
    cultural_integrity     — A2 full-pass tagging (post-translation)
    voice_sentinel         — dialogue consistency spot-check
    default                — anything not listed; falls through to cloud

Telemetry:
    Per-backend token counters, call counts, and dollar cost accumulate on
    the router instance. Reset by constructing a new router or calling
    `reset_telemetry()`. The GUI Compute tab can read `telemetry` to
    show live spend by backend.

    Every call is also written to data/cost_ledger.db (SQLite) so spend
    survives across runs. Pass run_id to complete() to group calls by
    episode or batch; query CostLedger.run_summary(run_id) afterwards.

Budget cap:
    Pass budget_usd to LLMRouter (or build_default_router) to hard-stop
    spending at a threshold. BudgetExceededError is raised before the
    next API call fires — no partial calls are billed.

Usage:
    from agents.llm_router import LLMRouter, build_default_router

    router = build_default_router()   # reads config/llm_routing.yaml
    response = router.complete(
        call_type="ip_clearance_semantic",
        system="...",
        messages=[{"role": "user", "content": "..."}],
        run_id="s01e03",
    )

When the new GPU lands and a local 70B model is running, edit
config/llm_routing.yaml — no Python changes needed.

See AEON-ENGINE/AGENTS_A1_A8_STATUS.md for context on what A7 unblocks.

## Defined here

### `BudgetExceededError`

Raised before an API call when cumulative spend has hit budget_usd.

### `LLMClient`

Same shape as agents.dramatist.LLMClient. Re-declared here so the
router doesn't pull in the full Dramatist module just for the type.

### `BackendUsage`

Per-backend running totals.

| Field | Type |
|---|---|
| `backend_name` | `str` |
| `calls` | `int` |
| `input_tokens` | `int` |
| `output_tokens` | `int` |
| `cost_usd` | `float` |
| `calls_by_type` | `dict[str, int]` |

### `LLMRouter`

Picks the right backend per call type, tracks usage, and enforces spend limits.

Construct via build_default_router() for the standard config, or
directly with explicit backends + routes for tests:

    router = LLMRouter(
        backends={"anthropic": MockLLM(...), "local": MockLLM(...)},
        routes={"ip_clearance_semantic": "local"},
        default_backend="anthropic",
    )

### `ConsensusEscalationUnavailableError`

Raised when the two GPU-local models split verdict and no escalation
client is configured to break the tie.

Callers should treat this as "no confident answer" — not silently trust
either GPU's response as if it were consensus. `ip_clearance_semantic`
callers already fall back to a conservative manual-review verdict on any
exception from the router, so raising here surfaces the ambiguity
instead of masking it.

### `ConsensusOllamaLLM`

Dual-GPU consensus backend for A7 (hardware day).

Fires the same prompt at two Ollama instances concurrently — one per RTX
3090. Extracts the first meaningful word from each response and compares
them. If both agree, returns the first response. On disagreement, makes
one escalation call to `escalation_client` (cloud Sonnet) and returns
that result with a warning log entry.

Used for `ip_clearance_semantic` where split verdicts are a signal of
genuine ambiguity that warrants the authoritative cloud call. If no
escalation client is configured, raises `ConsensusEscalationUnavailableError`
rather than silently returning one GPU's answer as though it were a
confident consensus.

### `_PendingConsensus`

Placeholder returned by _instantiate_backend for 'consensus' type.

build_default_router replaces it with a fully wired ConsensusOllamaLLM
once all backends (including the escalation target) are instantiated.

## Top-level functions

- **`build_default_router()`** — Construct an LLMRouter from config/llm_routing.yaml.
- **`get_default_router()`** — Lazy module-level router. First call builds from default config;
- **`reset_default_router()`** — For tests — force the next get_default_router() to rebuild.
