# envelope_builder

*Source: `heterodyne/agents/envelope_builder.py`*

envelope_builder.py — Assembles episode_header and episode_footer block lists.

No LLM calls — constructs SceneBlocks from world_config.json fields and
EpisodeConfig values. RecapNarrator is called separately in main.py and the
resulting block is passed in via build_header().

## Defined here

### `EnvelopeBuilder`

Builds episode header and footer block lists from authored config values.
