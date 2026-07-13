# voice_spec

*Source: `heterodyne/agents/voice_spec.py`*

agents/voice_spec.py

World-agnostic voice specification — the single source of truth for how a
character sounds. Derived AT RUNTIME from data that already exists, never
from a hardcoded cast:

  - the hand-authored personality prompt (prompts/vocal_personalities/*.txt),
    which is world-specific DATA, correctly located outside engine code;
  - structured signals from the roster / behavioral mask that ship on the
    ledger (linguistic_id, catchphrases, absolute_certainty, suppressed_modals,
    strange_stat, flat_affect).

Nothing here hardcodes any world's characters. A character with no personality
data yields an *empty* spec, and callers skip it — exactly the prior behavior
for unknown characters, but now every world's cast is covered instead of only
the five that used to be baked into agents/voice_sentinel.py.

Consumers (single source of truth — keep these in sync via this module only):
  - agents/voice_sentinel.py     — replaces the hardcoded VOCAL_RULES dict.
  - agents/translation_agent.py  — replaces hardcoded per-character examples.
  - writers_room voice checks     — cast briefs for blind attribution / omniscient.

Would this file still make sense if the active world were a different genre and
era? Yes — it reads whatever character data is passed in and derives from it.

## Defined here

### `VoiceSpec`

One character's structured voice signature.

`name` is the in-story character name (UPPER by convention on lookup).
Every field is optional; `is_empty` is True when we have nothing to say
about this voice, and consumers should skip rather than invent rules.

| Field | Type |
|---|---|
| `name` | `str` |
| `voice_seed_id` | `str` |
| `description` | `str` |
| `linguistic_id` | `str` |
| `catchphrases` | `tuple[str, ...]` |
| `personality_prompt` | `str` |
| `absolute_certainty` | `bool` |
| `suppressed_modals` | `tuple[str, ...]` |
| `strange_stat` | `int` |
| `flat_affect` | `bool` |

## Top-level functions

- **`build_voice_specs()`** — NAME(upper) → VoiceSpec for every living roster member.
- **`voice_specs_as_rules()`** — NAME(upper) → rules_text, dropping empty specs (callers skip those).
- **`voice_specs_as_briefs()`** — NAME(upper) → one-line attribution brief (for blind-attribution casts).
