# parallax_map_validator

*Source: `heterodyne/agents/parallax_map_validator.py`*

Parallax Map Validator — Three-agent validation pipeline for tactical maps.

Validation agents:
1. Schema Validator     — Checks LocationMap schema compliance
2. Spatial Analyzer     — Checks room layout and connectivity
3. Quality Reviewer     — Checks gameplay viability and genre appropriateness

## Defined here

### `ValidationResult`

Result of a single validation check.

| Field | Type |
|---|---|
| `validator` | `str` |
| `passed` | `bool` |
| `message` | `str` |

### `ValidationReport`

Complete validation report for a map.

| Field | Type |
|---|---|
| `location_id` | `str` |
| `location_map` | `LocationMap` |
| `checks` | `list[ValidationResult]` |

### `SchemaValidator`

Validate LocationMap schema compliance.

### `SpatialAnalyzer`

Analyze spatial relationships and connectivity.

### `QualityReviewer`

Review map quality and gameplay viability.

### `ParallaxMapValidator`

Three-agent validation pipeline for location maps.
