# reported_speech_qa

*Source: `heterodyne/agents/reported_speech_qa.py`*

agents/reported_speech_qa.py

Voice-distinctness check for OMNISCIENT narrator mode (item M).

In omniscient mode every character line becomes third-person reported narration
routed through VS-000, each block carrying `reported_speech_source` (the
originating character). The prompt asks the Narrator to preserve each
character's voice in the reported speech ("Brick's terseness surfaces in short
declarative reported clauses") — but the Writers'-Room blind-attribution test
only runs on `type="dialogue"`, of which omniscient mode has NONE. So the
show's most literary mode had ZERO voice-consistency enforcement.

This closes that gap: group reported-speech blocks by their source character
and run one blind attribution over them, judged only on language, using the
world-agnostic VoiceSpec attribution briefs. Low accuracy = the reported voices
have converged into one narratorial register. Observability only.

Only activates when a segment actually contains reported_speech_source blocks,
so it is inert on every non-omniscient episode.

## Defined here

### `ReportedSpeechReport`

| Field | Type |
|---|---|
| `applicable` | `bool` |
| `lines_checked` | `int` |
| `accuracy` | `float | None` |
| `converged` | `bool` |
| `threshold` | `float` |
| `note` | `str` |

## Top-level functions

- **`check_reported_speech()`** — Blind-attribute reported speech; low accuracy = converged voices.
