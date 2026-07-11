# pronunciation

*Source: `heterodyne/agents/pronunciation.py`*

Per-world pronunciation lexicon (#1).

Invented vocabulary (character names, places, magic terms) is the #1 audible
failure mode for fantasy audio drama — an English TTS will happily mangle
"Cael" or "Keth Saraal". This module applies a per-world lexicon of phonetic
*respellings* to the text right before synthesis.

Why respelling and not IPA: of our three render engines, only Kokoro accepts
phoneme input; Zonos phonemizes internally and Chatterbox is text-only. The
one method that works across all three is substituting the invented word with
an English-pronounceable respelling in the input text. The lexicon also stores
IPA per term for future Kokoro phoneme-mode precision.

Lexicon file: data/worlds/<world_id>/pronunciation.json
    {
      "world_id": "verdant_deep",
      "terms": {
        "Keth Saraal": {"respelling": "Keth Sarahl", "ipa": "...", "notes": "..."},
        "Cael":        {"respelling": "Kale", "ipa": "...", "notes": "..."}
      }
    }

Application is whole-word and case-insensitive; multi-word terms are matched
before their sub-words (so "Keth Saraal" wins over "Saraal").

## Top-level functions

- **`lexicon_path()`** — 
- **`apply_pronunciation()`** — Substitute lexicon terms in `text` with their respellings.
- **`reload_cache()`** — Drop the compiled-lexicon cache (call after editing a lexicon file).
