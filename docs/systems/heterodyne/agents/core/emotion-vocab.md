# emotion_vocab

*Source: `heterodyne/agents/emotion_vocab.py`*

agents/emotion_vocab.py

Single source of truth for the engine's emotion vocabulary.

Before this module the emotion vocabulary was fragmented across three places
that silently disagreed:

  - AcousticIntent.emotion enum:  neutral/grief/fear/anger/joy/exhaustion/
                                  authority/conspiratorial/warm/cold
  - the Orpheus tag map:          keyed on the enum (mostly matched)
  - the Zonos 8-vector map:       keyed on happy/sad/angry/fearful/... — so
                                  the enum's `fear`, `anger`, `joy`,
                                  `exhaustion`, `authority`, `conspiratorial`,
                                  `cold` MISSED the map and produced no
                                  emotion vector at all.

And the Writers'-Room annotator emitted free-form `"emotion": "<one word>"`,
so anything outside the enum ("sad", "tender", "nervous", "bitter") fell
through every map and rendered flat.

This module fixes that: one canonical set, a permissive synonym normalizer
(any surface label → canonical), and per-canonical Orpheus tag + Zonos vector.
Nothing here is world-specific — it is a vocabulary of human emotion.

Consumers: agents/voice_engine.py (Orpheus + Zonos delivery), the annotator /
Dramatist prompts (constrained to CANONICAL_EMOTIONS), and the subtext blend.

## Top-level functions

- **`normalize_emotion()`** — Any surface label → a canonical emotion. Unknown/empty → 'neutral'.
- **`orpheus_tag()`** — `<tag>` string for Orpheus, or '' when the emotion has no inline tag.
- **`zonos_vector()`** — Zonos 8-vector for the emotion, or None for neutral/unknown.
- **`blend_zonos_vectors()`** — Blend surface + interior emotion vectors for subtext delivery.
- **`paralinguistic_tags()`** — Map a list of paralinguistic event names to Orpheus `<tag>` strings.
