# llm_clients

*Source: `heterodyne/agents/llm_clients.py`*

agents/llm_clients.py

Provider-agnostic LLM client infrastructure shared by every agent.

Extracted from agents/dramatist.py so the clients, the response envelope,
and the protocol live apart from any one agent's logic. `agents.dramatist`
re-exports every public name here for backward compatibility — existing
imports (`from agents.dramatist import AnthropicLLM`) keep working.

Backends:
    MockLLM         — test double driven by a response_fn
    AnthropicLLM    — Claude via the anthropic SDK (prompt caching on system)
    OllamaLLM       — local Ollama native REST endpoint
    OpenAICompatLLM — any server speaking the OpenAI /v1/chat/completions
                      shape: vLLM, LM Studio, llama.cpp server, TGI,
                      Ollama's OpenAI-compatible endpoint, hosted OSS
                      providers. One backend type covers "any new model"
                      without new Python.

Error contract: connection/transport/empty-response failures raise
LLMClientError. `agents.dramatist.DramatistError` subclasses it, so
`except LLMClientError` catches both infrastructure failures and
Dramatist-level failures.

## Defined here

### `LLMClientError`

A backend failed to produce a usable response (unreachable endpoint,
empty content, transport error). Base class for agent-level errors such
as DramatistError, so `except LLMClientError` catches everything.

### `LLMResponse`

Normalized response from any LLMClient implementation.

| Field | Type |
|---|---|
| `content` | `str` |
| `input_tokens` | `int` |
| `output_tokens` | `int` |
| `stop_reason` | `str | None` |

### `LLMClient`

Minimal LLM interface agents depend on.

Implementations: MockLLM (tests), AnthropicLLM, OllamaLLM,
OpenAICompatLLM. Swappable at construction time, or routed per
call type via agents.llm_router.LLMRouter.

### `MockLLM`

Test double. A callable provides the response per invocation.

`response_fn(system, messages) -> str` returns the raw text the model
would produce. Input/output token counts are estimated from char length
so cost-accounting paths still exercise.

### `AnthropicLLM`

Real Claude client via the anthropic SDK.

Uses the Messages API with prompt caching on the system prompt — long
system prompts that are stable across calls (the Dramatist's is stable
across all four segments of an episode) get ~90% input-cost savings on
cache hits.

Parameters
----------
api_key:
    Anthropic API key. If None, reads ANTHROPIC_API_KEY from the env.
model:
    Model string. Defaults to 'claude-sonnet-4-6' per project spec.
max_tokens:
    Output ceiling per call.
timeout:
    Per-request timeout in seconds. Default 600 (ten minutes) — long
    structured generations against a long cached system prompt can take
    4-9 minutes wall time.

### `OllamaLLM`

Local Ollama client (native /api/chat endpoint). Zero API cost.

Parameters
----------
model:
    Ollama model tag, e.g. 'llama3.1:8b'. Must be pulled first via
    ``ollama pull <model>``.
base_url:
    Ollama REST endpoint.
max_tokens:
    Maximum tokens to generate per call (Ollama ``num_predict``).
timeout:
    Per-request timeout in seconds.
options:
    Extra Ollama options passed through verbatim (temperature,
    num_ctx, top_p, ...). Lets llm_routing.yaml tune a model without
    code changes.

### `OpenAICompatLLM`

Generic client for any server speaking OpenAI's /v1/chat/completions.

Covers vLLM, LM Studio, llama.cpp server, TGI, Ollama's OpenAI
endpoint, and hosted OSS providers — trying a new model is a
llm_routing.yaml edit, never a Python change.

Parameters
----------
base_url:
    Server root, e.g. 'http://localhost:8000/v1' or
    'http://localhost:1234/v1'. '/chat/completions' is appended if
    the URL doesn't already end with it.
model:
    Model identifier as the server expects it.
api_key_env:
    Name of the environment variable holding the API key, if the
    server requires one. The key itself never appears in config.
max_tokens, timeout, temperature:
    Standard generation controls. temperature=None omits the field
    (server default applies).
