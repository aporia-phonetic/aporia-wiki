# novelist_validator

*Source: `heterodyne/agents/novelist_validator.py`*

agents/novelist_validator.py

Three-agent QA for manuscript output from NovelistAgent.

Mirrors the Parallax QA pattern: three independent validators compose
a pipeline, each checking a different dimension of quality.

Validators:
1. NarrativeVoiceValidator    — character voices consistent with ledger signatures
2. WorldbuildingValidator     — manuscript consistent with world_ledger lore
3. PacingValidator            — structural arc coherence, chapter balance

All three are LLM-backed; the entire validator is optional and off by default
(NOVELIST_QA_ENABLED).  Fail-open: check failures return passed=True with
a warning log rather than blocking manuscript delivery.

## Defined here

### `ValidationResult`

| Field | Type |
|---|---|
| `validator` | `str` |
| `passed` | `bool` |
| `message` | `str` |
| `severity` | `str` |

### `NovelValidationReport`

| Field | Type |
|---|---|
| `source_ref` | `str` |
| `checks` | `list[ValidationResult]` |
| `requires_revision` | `bool` |

### `NarrativeVoiceValidator`

Check that character voices are consistent with world-ledger signatures.

Samples dialogue passages for each named character and asks Claude
whether the voice is internally consistent across the manuscript.

### `WorldbuildingValidator`

Check that the manuscript doesn't contradict established world lore.

Samples from the manuscript and cross-checks against world context
for named entity consistency and lore accuracy.

### `PacingValidator`

Check structural arc coherence and chapter balance.

Deterministic checks (no LLM): chapter length distribution, presence
of a discernible beginning/middle/end arc.  An optional LLM pass checks
narrative arc quality when NOVELIST_PACING_LLM_ENABLED is set.

### `NovelistValidator`

Compose all novel validators into one pipeline.
