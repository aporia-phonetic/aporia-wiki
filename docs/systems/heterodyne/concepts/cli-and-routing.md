# CLI & LLM routing

## `aeon.py` — unified CLI

Three decoupled entities (World / Character / Story), three command
groups:

```
aeon world create     <world_id> [--name ... --genre ... --description ...]
aeon world build      <world_id>           # re-run the build on an existing world
aeon world chronicle  <world_id>           # just the Sediment Engine step
aeon world sourcebook <world_id> [--season N]
aeon world ingest     <world_id> [--season N]  # capture human sourcebook edits
                                               # as canon overrides that survive
                                               # recompiles
aeon world list
aeon world show       <world_id>

aeon character ...    # Phase 2
aeon story ...        # Phase 3
```

`world create`/`build` run the full standalone world build — Sediment
Engine → present-day narrative + sourcebook → QA gate → cast-free ledger
— producing a complete world sourcebook before any story or character
exists.

## `resolve_world_id`

`schemas/paths.py::resolve_world_id` is the single source of truth for
"which world is active." Precedence: explicit argument > `WORLD_ID` env
var > `AEON_WORLD_ID` env var (legacy alias) > `"verdant_deep"` as a
last-resort historical fallback (the one world that predates the
`WorldConfig` schema — not a genre/era default, just a harmless bootstrap
value). Every call site that used to hardcode
`os.getenv("WORLD_ID", "verdant_deep")` now calls this instead. See
[World-agnostic engine code](world-agnosticism.md) for why this
consolidation mattered.

## LLM routing

`agents/llm_router.py` dispatches each LLM call to the right backend by
*call type*, not by hardcoding a model per feature:

| Call type | Typical backend |
|---|---|
| `dramatist_segment` | Cloud (Claude) — 16–24k output, structured generation |
| `ip_clearance_semantic` | Local — cheap, narrow semantic-similarity check |
| `cultural_integrity` | Local — full-pass tagging after translation |
| `voice_sentinel` | Local — dialogue-consistency spot-check |
| `default` | Cloud — anything not explicitly routed |

Swapping a call type's backend to `local` in `config/llm_routing.yaml`
redirects spend to a self-hosted model without a code change. The actual
client implementations (`AnthropicLLM`/`OllamaLLM`/`OpenAICompatLLM`/
`MockLLM`) live in `agents/llm_clients.py`; the router is the dispatcher
on top.
