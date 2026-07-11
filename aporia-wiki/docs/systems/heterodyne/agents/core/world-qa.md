# world_qa

*Source: `heterodyne/agents/world_qa.py`*

agents/world_qa.py — World-coherence quality gate.

The validation step of the standalone *world build*. After the Sediment Engine
and Sourcebook Compiler have run, the World QA gate checks that the world hangs
together before it is marked `built` and made available to story seeds.

Modelled on the deterministic half of agents/qa_validator.py (System A / A5):
no LLM calls — fast, mechanical structural checks over deep_ledger.db and the
compiled sourcebook. Emits a verdict (pass / warn / fail) with itemised issues
to data/worlds/{world_id}/world_qa.json.

A `warn` does not block a build (the world is usable but flagged); a `fail`
means the foundation is incoherent and should be regenerated.

## Defined here

### `WorldQAIssue`

| Field | Type |
|---|---|
| `severity` | `Severity` |
| `check` | `str` |
| `detail` | `str` |

### `WorldQAReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `verdict` | `Literal['pass', 'warn', 'fail']` |
| `era_count` | `int` |
| `figure_count` | `int` |
| `issues` | `list[WorldQAIssue]` |

### `WorldQA`

Deterministic world-coherence checks. No LLM calls.
