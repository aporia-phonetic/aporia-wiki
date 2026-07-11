# translation_agent

*Source: `heterodyne/agents/translation_agent.py`*

agents/translation_agent.py

Multilingual pipeline stage — translates completed episode JSON from English
to target languages. Sits between the Dramatist output and the Voice Engine input.

Architecture:
  Dramatist → [TranslationAgent] → Voice Engine (per language)
                                 → Foley Master (once, shared)
                                 → Maestro     (once, shared)
                                 → Mixer       (per language, trivial FFmpeg)

What is translated:
  - `text` fields in dialogue and narration blocks
  - `segment_end_hook` field

What is never translated:
  - block_id, type, character, voice_seed_id    — schema identifiers
  - foley_cues                                  — catalog keys, not natural language
  - foley_events                                — structured foley metadata, not narrative
  - music_cue trigger keys                      — stem manifest keys
  - acoustic_intent                             — TTS prosody hints, not natural language
  - ssml_tags                                   — preserve exactly
  - world_ledger_updates                        — schema values
  - Character names, location names             — world-specific terminology
  - continuity_warnings, tone_signature         — pipeline metadata

Cost model (Batch API + cache, Sonnet 4.6):
  Single episode, single language: ~$0.30–$0.80
  Full season (12 ep), 6 languages: ~$22–$58 total in one batch run
  Submitted as one batch. Estimated completion: under 1 hour.

## Defined here

### `CulturalFlag`

A single cultural integrity issue found in a translated episode.

| Field | Type |
|---|---|
| `severity` | `Literal['INFO', 'WARN', 'BLOCK']` |
| `category` | `Literal['idiom', 'register', 'honorific', 'religious', 'political', 'unlucky_number', 'loaded_name', 'gender_form', 'other']` |
| `block_id` | `str` |
| `original_english` | `str` |
| `flagged_text` | `str` |
| `suggestion` | `str` |
| `cultural_note` | `str` |

### `CulturalIntegrityReport`

Full Cultural Integrity Pass result for one episode × one language.

| Field | Type |
|---|---|
| `language_code` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `passed` | `bool` |
| `flags` | `List[CulturalFlag]` |
| `checked_at` | `datetime` |
| `model_used` | `str` |
| `raw_response` | `str` |

### `TranslationAgent`

Translates completed episode JSON from English to target languages.

All translation calls go through the BatchDispatcher. Single-episode
calls route via submit_single. Season-batch calls submit all N×L requests
(episodes × languages) as one batch for maximum efficiency.

Args:
    dispatcher: Initialized BatchDispatcher instance (used for translation
                calls and as the default backend for the A2 Cultural
                Integrity Pass).
    llm_router: Optional A7 LLMRouter. When provided, the A2 Cultural
                Integrity Pass routes through it using the
                `cultural_integrity` call type. Backend choice then lives
                in config/llm_routing.yaml — point it at `anthropic` for a
                Sonnet full-pass, `anthropic_haiku` for the cheap default,
                or `local` once a local 70B is available.

                When llm_router is None, the cultural integrity pass falls
                back to the dispatcher (current behavior, Sonnet via
                BatchDispatcher.model).
