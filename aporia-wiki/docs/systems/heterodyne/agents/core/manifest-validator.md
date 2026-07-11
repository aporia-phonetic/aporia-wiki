# manifest_validator

*Source: `heterodyne/agents/manifest_validator.py`*

agents/manifest_validator.py

QA for A.C.E.S. outcome manifests produced by ManifestGenerator.

Two deterministic validators always run; an optional LLM coherence
spot-check is controlled by MANIFEST_LLM_QA_ENABLED (default off — manifests
are expensive to generate and the deterministic checks catch most issues).

Validators:
1. CoverageValidator    — all four domain files exist, outcome count per tier
2. SchemaValidator      — required keys present in each manifest file
3. NarrativeCoherenceValidator (optional LLM) — sampled outcome coherence

## Defined here

### `ValidationResult`

| Field | Type |
|---|---|
| `validator` | `str` |
| `passed` | `bool` |
| `message` | `str` |
| `severity` | `str` |

### `ManifestValidationReport`

| Field | Type |
|---|---|
| `character` | `str` |
| `checks` | `list[ValidationResult]` |

### `CoverageValidator`

Verify all four domain manifests exist with sufficient outcome counts.

### `SchemaValidator`

Check required keys are present in each manifest file.

### `NarrativeCoherenceValidator`

LLM spot-check: are sampled outcomes coherent and internally consistent?

### `ManifestStructureValidator`

Compose all manifest validators into one pipeline.
