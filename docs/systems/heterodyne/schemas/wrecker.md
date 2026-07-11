# wrecker

*Source: `heterodyne/schemas/wrecker.py`*

schemas/wrecker.py

Schema for the Wrecker Agent — the adversarial auditor.

The Wrecker's founding assumption is that every plan, projection, system, and
pipeline output is wrong until proven otherwise. It does not balance; it
prosecutes. A run produces a WreckerReport — a structured "prosecution file"
rather than a balanced review.

Verdict taxonomy
----------------
  FRAGILE       — May hold, but rests on unvalidated assumptions.
  BROKEN        — Contains an internal contradiction or a demonstrably false
                  assumption.
  LOAD_BEARING  — Structural dependency; flagged regardless of apparent
                  soundness, because failure here cascades.

Attack surfaces
---------------
  financial   — revenue projections, cost models, patron trajectories
  production  — pipeline output (episode JSON, agent notes, ledger state)
  strategy    — business-plan sections, marketing/competitive claims
  schema      — pydantic schemas, agent prompts, pipeline config

This schema is consumed by agents/wrecker.py (WreckerAgent) and rendered by
gui/panels/wrecker_panel.py. Reports are persisted to data/wrecker_reports/.

## Defined here

### `WreckerVerdict`

The verdict assigned to a single audited claim.

### `AttackSurface`

The audit surface a WreckerReport was generated against.

### `WreckerFinding`

A single prosecuted claim.

Every audited claim is decomposed into the assumption it hides, the worst
defensible alternative to that assumption, the evidence that already exists
for failure, and the full set of conditions that must simultaneously hold
for the claim to be correct.

| Field | Type |
|---|---|
| `claim` | `str` |
| `verdict` | `WreckerVerdict` |
| `embedded_assumption` | `str` |
| `worst_case_alternative` | `str` |
| `evidence_for_worst_case` | `str` |
| `what_must_be_true` | `list[str]` |
| `simultaneous_probability` | `str` |
| `is_structural_dependency` | `bool` |
| `cascade_targets` | `list[str]` |

### `UnaskedQuestion`

A question the target does not address but should.

| Field | Type |
|---|---|
| `question` | `str` |
| `why_it_matters` | `str` |
| `what_answering_it_changes` | `str` |

### `WreckerReport`

The prosecution file returned by a single audit.

`attack_surface` is stored as a plain string (not the enum) so reports
deserialized from older runs or hand-edited JSON never fail validation on
an unexpected surface value. `generated_at` and `total_cost_usd` are filled
in by the agent, not the model.

| Field | Type |
|---|---|
| `target_summary` | `str` |
| `attack_surface` | `str` |
| `findings` | `list[WreckerFinding]` |
| `unasked_questions` | `list[UnaskedQuestion]` |
| `load_bearing_map` | `list[str]` |
| `prosecution_summary` | `str` |
| `generated_at` | `datetime` |
| `total_cost_usd` | `float` |
