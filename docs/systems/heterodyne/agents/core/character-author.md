# character_author

*Source: `heterodyne/agents/character_author.py`*

agents/character_author.py — multi-pass character authoring (C3).

Closes the depth gap between the hand-authored vocal personality files
(VS-001..005) and the one-shot generated stubs every new-world character
used to get. Four passes, all routed through the `character_generation`
call type (cloud or local per config/llm_routing.yaml):

  1. sheet     — the existing single-call generation (character_service)
  2. idiolect  — an idiolect card in the Writers'-Room card spirit
                 (register, cadence, openers, tics, negative space),
                 folded into linguistic_id + catchphrases
  3. sample    — a short in-voice dialogue sample
  4. check     — blind attribution of the sample against the existing
                 cast (the Writers'-Room quality pattern); if the new
                 voice reads as someone else's, passes 2-3 retry once
                 with distinctness feedback

The enriched depth lands in the portable identity fields the pipelines
already consume (linguistic_id, catchphrases, voice_description →
VoiceSpec, idiolect cards, derived personality prompts). The sample
itself is authoring scaffolding, returned under sheet["authoring"] for
inspection but not persisted on the identity.

World-agnostic: everything world-specific arrives via `brief`,
`resonance_schools`, and the prior cast — never hardcoded here.

## Top-level functions

- **`author_character()`** — Multi-pass character generation. Same return shape as
