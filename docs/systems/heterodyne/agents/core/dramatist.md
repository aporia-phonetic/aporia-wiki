# dramatist

*Source: `heterodyne/agents/dramatist.py`*

Dramatist — the script generation agent.

Runs a LangGraph state machine with four nodes, one per segment. Each node:

  1. Selects active vocal personalities (all five for segment 1; thereafter
     the set of characters who spoke in the prior segment plus the Narrator).
  2. Assembles a dynamic user message from the segment template + Ledger +
     gate + personality prompts.
  3. Calls the injected LLMClient and parses the structured response.
  4. Validates against SegmentScript (raw shape + our custom validators).
     Retries up to MAX_VALIDATION_ATTEMPTS with the error message fed back
     to Claude; raises DramatistError if it never lands.
  5. Tracks token usage and refuses the next call if projected cost would
     exceed the spending cap.

The Dramatist does not write to disk, does not commit the Ledger, does not
know SQLite exists. It takes a Ledger in, emits four SegmentScripts out,
and returns. main.py plays referee.

## Defined here

### `DramatistError`

Base class for all Dramatist failures.

Subclasses LLMClientError so `except LLMClientError` catches both
Dramatist-level failures and raw backend/transport failures.

### `SegmentValidationError`

The LLM's output failed SegmentScript validation after all retries.

### `SpendingCapExceededError`

Projected cost of the next call would exceed the spending cap.

### `DramatistState`

State carried between LangGraph nodes.

Fields marked *input* are set before the graph runs and never mutate.
Fields marked *accumulating* grow as nodes fire.

| Field | Type |
|---|---|
| `ledger` | `WorldLedger` |
| `gate` | `dict[str, Any]` |
| `season` | `int` |
| `episode` | `int` |
| `system_prompt` | `str` |
| `segment_template` | `str` |
| `personality_prompts` | `dict[str, str]` |
| `episode_config` | `EpisodeConfig | None` |
| `segments` | `list[SegmentScript]` |
| `previous_hook` | `str` |

### `Dramatist`

LangGraph-driven script generation agent.

Parameters
----------
llm:
    An object satisfying the LLMClient protocol. Pass MockLLM in tests,
    AnthropicLLM in production. Optional when `router` is given.
router:
    Optional agents.llm_router.LLMRouter. When set, every call goes
    through the router with a per-purpose call_type (dramatist_segment,
    episode_summary, catchphrase_extraction, character_description) so
    backends are flippable via config/llm_routing.yaml. Takes precedence
    over `llm`.
run_id:
    Cost-ledger grouping key passed to the router (e.g. "s01e03").
prompts_dir:
    Path to the prompts directory (contains dramatist_system.txt,
    segment_template.txt, and vocal_personalities/).
spending_cap_usd:
    Hard ceiling on cumulative cost for a single episode generation.
    Checked before every call. None disables the check.
input_price_per_mtok, output_price_per_mtok:
    Overridable pricing constants. Defaults track Claude Sonnet 4.6.

## Top-level functions

- **`generate_stub_episode()`** — Four minimal valid SegmentScripts without any API calls.
- **`make_llm()`** — Return the configured LLM client, reading LLM_BACKEND from env if not specified.
- **`make_dramatist()`** — Convenience constructor that reads LLM_BACKEND from env.
- **`run_episode()`** — Production entrypoint for the Dramatist pipeline.
