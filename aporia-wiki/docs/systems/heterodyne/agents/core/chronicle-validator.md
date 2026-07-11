# chronicle_validator

*Source: `heterodyne/agents/chronicle_validator.py`*

agents/chronicle_validator.py

QA for world history chronicles produced by SedimentEngine.

Two deterministic validators always run; an optional LLM continuity
spot-check is controlled by CHRONICLE_LLM_QA_ENABLED (default off).

Validators:
1. TimelineValidator      — entries in order, no duplicates, no future dates
2. EntityCoverageValidator — ledger characters/locations appear in chronicle
3. NarrativeContinuityValidator (optional LLM) — adjacent entries consistent

## Defined here

### `ValidationResult`

| Field | Type |
|---|---|
| `validator` | `str` |
| `passed` | `bool` |
| `message` | `str` |
| `severity` | `str` |

### `ChronicleValidationReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `checks` | `list[ValidationResult]` |

### `TimelineValidator`

Check that chronicle entries are ordered and non-duplicated.

### `EntityCoverageValidator`

Verify that known characters and locations appear in the chronicle.

### `NarrativeContinuityValidator`

LLM spot-check: do adjacent chronicle entries contradict each other?

### `ChronicleValidator`

Compose all chronicle validators into one pipeline.
