# emotion_judge

*Source: `heterodyne/agents/emotion_judge.py`*

agents/emotion_judge.py

Two emotion-quality gates that close a loop nothing else covers.

  1. EmotionJudge (LLM-as-judge, item i) — the Dramatic Function judge asks
     "did the gate land?"; the Voice Sentinel asks "does it sound like this
     character?"; NOTHING asked "does the intended emotion actually REGISTER,
     or is it merely labeled?" This judge reads a segment against its
     tone_signature and scores emotional legibility. Observability only:
     mirrors DramaticFunctionJudge exactly (persist + WARN, never blocks).

  2. emotional_cadence_report (pure code, item j) — gate_critic audits hook /
     function variety at SEASON scale; nothing checked whether a single episode
     BREATHES. A run of four segments all tagged the same dominant_tone with no
     low/ma valley is emotionally monotonous even when every gate passes. This
     is a free, deterministic within-episode audit of tonal variety and relief.

Both are world-agnostic: they read tone_signature + scene_energy, never a cast.

## Defined here

### `EmotionJudgeResult`

Per-segment verdict: did the intended emotion register?

| Field | Type |
|---|---|
| `segment` | `int` |
| `intended_tone` | `str` |
| `registers` | `bool` |
| `evidence` | `str` |
| `emotional_legibility_score` | `float` |

### `EmotionJudge`

One LLM-as-judge call per segment. Fails closed (registers=False).

### `EmotionalCadenceReport`

| Field | Type |
|---|---|
| `dominant_tones` | `list[str]` |
| `energy_histogram` | `dict[str, int]` |
| `has_valley` | `bool` |
| `tone_variety` | `int` |
| `warnings` | `list[str]` |

## Top-level functions

- **`emotional_cadence_report()`** — Does the episode breathe? Flags tonal monotony and missing relief.
