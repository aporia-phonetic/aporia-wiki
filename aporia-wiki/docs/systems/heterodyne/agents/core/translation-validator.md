# translation_validator

*Source: `heterodyne/agents/translation_validator.py`*

agents/translation_validator.py

Structural QA for translated episode JSON.

Three deterministic validators run always; two optional LLM checks (voice
consistency and meaning fidelity) can be enabled via TRANSLATION_LLM_QA_ENABLED.
All failures are non-blocking by default (TRANSLATION_BLOCK_ON_FAILURE=false).

Validators:
1. SchemaValidator       — required fields present, array lengths match original
2. PreservedFieldsValidator — IDs, character names, foley/music cues unchanged
3. CoverageValidator     — every translatable text field was actually translated
4. VoiceConsistencyValidator (optional LLM) — character register preserved
5. FidelityValidator (optional LLM) — translated text preserves the source's
   meaning; the structural checks above catch format corruption but not
   mistranslation, so this is the only check that looks at semantic accuracy.

## Defined here

### `ValidationResult`

| Field | Type |
|---|---|
| `validator` | `str` |
| `passed` | `bool` |
| `message` | `str` |
| `severity` | `str` |

### `TranslationValidationReport`

| Field | Type |
|---|---|
| `episode_ref` | `str` |
| `language` | `str` |
| `checks` | `list[ValidationResult]` |

### `SchemaValidator`

Verify required fields are present and segment counts match.

### `PreservedFieldsValidator`

Check that non-translatable fields are unchanged.

### `CoverageValidator`

Verify every translatable text field was actually translated.

### `VoiceConsistencyValidator`

LLM-backed spot-check: do character voices read consistently in translation?

Samples up to TRANSLATION_VOICE_SAMPLE_BLOCKS blocks per character and
asks Claude whether the register/tone of each character is internally
consistent within the translated text.

### `FidelityValidator`

LLM-backed spot-check: does the translation preserve the source's meaning?

The structural validators above confirm shape (counts, preserved IDs,
every field translated) but say nothing about whether the translated
text actually means what the English source meant. This samples matched
original/translated text pairs and asks the LLM to judge equivalence —
catching mistranslation, dropped clauses, and meaning drift that
structural checks can't see.

### `TranslationStructureValidator`

Compose all translation validators into one pipeline.
