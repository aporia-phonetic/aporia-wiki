# batch_dispatcher

*Source: `heterodyne/agents/batch_dispatcher.py`*

agents/batch_dispatcher.py

Routes all Dramatist API calls through either the synchronous Messages API
or the asynchronous Message Batches API, based on EpisodeConfig.batch_mode.

This is the single interface between all prompt-assembly logic and the
Anthropic API. Nothing calls anthropic.Anthropic().messages.create() directly
except through here.

Prompt caching is applied automatically when use_prompt_caching=True.
Cache headers are added to the system prompt blocks, split at the
[WORLD LEDGER STATE] marker defined in section 4.4 of the spec:
  - Block 1 (before marker): world rules, vocal personalities, production weights.
    Changes rarely. Cache hit rate ~95%+ across a season.
  - Block 2 (after marker): World Ledger state, active callbacks, character states.
    Changes per episode. Cache hit rate ~75%+ across the four segments of one episode.

Cost model (Sonnet 4.6, $3.00/$15.00 per MTok):
  - Standard API, no cache: ~$1.50–$2.50 per episode
  - Batch API only:          ~$0.75–$1.25 per episode (50% off)
  - Batch + cache:           ~$0.40–$0.80 per episode (stacked)

## Defined here

### `BatchDispatcher`

Routes Claude API calls through the synchronous Messages API (REALTIME)
or the asynchronous Message Batches API (BATCH).

All Dramatist, TranslationAgent, and Parallax QA calls go through here.

Args:
    api_key:    Anthropic API key. Must be set — never hardcoded.
    model:      Claude model string. Defaults to claude-sonnet-4-6.
