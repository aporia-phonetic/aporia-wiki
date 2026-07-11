# recap_narrator

*Source: `heterodyne/agents/recap_narrator.py`*

recap_narrator.py — Generates the "Previously on..." narrator block for episode headers.

Reads the four segment-end hooks stored in the WorldLedger from the prior
episode and produces a single narration SceneBlock suitable for prepending
to the episode_header list.

## Defined here

### `LLMClient`

### `RecapNarrator`

Generates a 'Previously on...' SceneBlock from prior episode hooks.
