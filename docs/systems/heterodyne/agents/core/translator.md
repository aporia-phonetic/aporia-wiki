# translator

*Source: `heterodyne/agents/translator.py`*

agents/translator.py

Block-level SSML translator for the Axiom Synthetic Pipeline.

Translates SegmentScript scene blocks from English to a target language
while preserving SSML emotional tags and adapting prosody for the target
TTS voice. Translation occurs at the block level for maximum cache hit
rate and Batch API parallelism.

Architecture:
  - One API call per block containing text (narration + dialogue blocks)
  - Foley and music_cue blocks are pass-through (no text to translate)
  - SSML tags in square brackets (e.g. [gravelly]) are TTS prosody markers —
    returned unchanged. Inline emotion tags (e.g. <laugh>) are likewise
    returned in identical position in the translated text.
  - Batch API support: all blocks for an episode can be submitted as a
    single batch request (50% token discount, async processing).

Usage:
    from agents.translator import BlockTranslator

    translator = BlockTranslator()
    translated_seg = translator.translate_segment(segment, target_language="es")

    # Or for a full episode (4 segments) via Batch API:
    translated_segs = translator.translate_batch(segments, target_language="es")

## Defined here

### `BlockTranslator`

Translates individual SceneBlocks from English to a target language.

Parameters
----------
api_key:
    Anthropic API key. If None, uses ANTHROPIC_API_KEY from environment.
model:
    Claude model ID to use for translation.
    Default: claude-haiku-4-5-20251001 (fast + cost-effective for translation).
use_prompt_caching:
    Attach ephemeral cache_control to the static system prompt block.
    ~90% discount on cached input tokens. Keep True in production.
