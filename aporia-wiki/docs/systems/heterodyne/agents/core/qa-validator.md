# qa_validator

*Source: `heterodyne/agents/qa_validator.py`*

agents/qa_validator.py -- Parallax QA validation layer.

Three-agent validation system per AEON_Parallax_System.docx and
AEON_Parallax_Execution_Document.docx. Runs after each Dramatist segment
when EpisodeConfig.parallax_qa_enabled is True.

System A -- Structural Validator: gate completion, continuity, world state.
Conflict Analyzer -- classifies disagreements between A and the segment.
Adversarial Agent -- stress-tests the segment for hidden inconsistencies.

The Dramatist's generated segment is passed through all three agents.
If System A finds a structural violation, the segment is flagged for
regeneration with the violation report fed back to the Dramatist.

SYSTEM LAW: Agreement is not success. Disagreement is signal.

Cost: approximately 3 additional Claude API calls per segment.
Disable at EpisodeConfig.parallax_qa_enabled = False (default).

## Defined here

### `ValidationResult`

Output from System A (Structural Validator).

| Field | Type |
|---|---|
| `passed` | `bool` |
| `violations` | `list[str]` |
| `confidence` | `float` |

### `ConflictReport`

Output from the Conflict Analyzer.

| Field | Type |
|---|---|
| `conflicts` | `list[dict[str, Any]]` |
| `recommendation` | `str` |

### `AdversarialReport`

Output from the Adversarial Agent.

| Field | Type |
|---|---|
| `failure_scenarios` | `list[str]` |
| `risk_areas` | `list[str]` |
| `passed` | `bool` |

### `A5CheckResult`

Results of A5 deterministic dialogue de-optimization checks.

Runs without LLM calls. Environmental Ingestion and Mannerism Exhaustion
are checked mechanically; Non-Answer Constraint is enforced at the System A
prompt level. This result is passed to the Archivist so it can update
mannerism cooldowns after episode commit.

| Field | Type |
|---|---|
| `total_dialogue_blocks` | `int` |
| `foley_engaged_dialogue_blocks` | `int` |
| `environmental_ingestion_ratio` | `float` |
| `environmental_ingestion_passed` | `bool` |
| `mannerisms_fired` | `Dict[str, List[str]]` |
| `suppressed_mannerisms_violated` | `Dict[str, List[str]]` |
| `violations` | `List[str]` |
| `passed` | `bool` |

### `ParallaxResult`

Aggregated result from the full three-agent run.

| Field | Type |
|---|---|
| `segment` | `int` |
| `validation` | `ValidationResult` |
| `conflicts` | `ConflictReport` |
| `adversarial` | `AdversarialReport` |
| `requires_regeneration` | `bool` |
| `regeneration_context` | `str` |
| `a5` | `Optional[A5CheckResult]` |

### `ParallaxValidator`

Runs the three-agent Parallax QA pipeline on a single segment.

Parameters
----------
llm_client:
    Any object with a `.complete(system, messages)` method returning
    an object with a `.content` str attribute. Accepts the same
    LLMClient protocol as the Dramatist.
gate:
    The current plot gate dict, used by System A to check gate completion.
