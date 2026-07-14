# pressure_engine

*Source: `heterodyne/agents/pressure_engine.py`*

agents/pressure_engine.py

Outer-loop orchestration for schemas.pressures.PressureState: the tick/decay
pass, drive resolution after an action, moral-cost desensitization, and the
Conflict Resolution Engine that ranks a character's simultaneous drive
deficits by weighted urgency.

This module is freestanding — it does not import from main.py or any other
agent module, does not know about episodes, segments, or any world's genre,
and does not assume which drive ids or morality-cost ids a character uses.
All of that is caller-supplied data (typically populated onto
CharacterExtension.pressure_state from a character's own config).

System Prompt Modulation (build_urgency_imperative) replaces literal
API-level logit_bias: rather than biasing token ids (which behaves like a
sledgehammer on abstract concepts), it produces a natural-language directive
describing which drive is most unmet right now. The caller may supply a
`descriptions` map (drive id -> flavor text, itself pulled from world/character
data) to make that directive specific; without one it falls back to a generic,
mechanism-only sentence that stays genre-agnostic.

Wiring these calls into the live Dramatist/Archivist pipeline (one tick() per
turn, one build_urgency_imperative() injected into the per-character segment
prompt, desensitize() called wherever a moral-violation event is detected) is
deferred to a follow-up pass, the same way agents/trajectory.py's record()
calls were built complete and left unwired pending a pipeline insertion plan.

## Defined here

### `DeficitScore`

One drive's ranked standing in the Conflict Resolution Engine.

| Field | Type |
|---|---|
| `pressure_id` | `str` |
| `deficit` | `float` |
| `urgency` | `float` |

## Top-level functions

- **`tick()`** — Advance every pressure by one turn of decay, in place.
- **`resolve_action()`** — Apply drive replenishment for an action that served one or more drives.
- **`apply_moral_violation()`** — Desensitize the named MoralityCost after it was paid.
- **`weighted_deficits()`** — Every drive currently in deficit, ranked by urgency (deficit * weight),
- **`dominant_and_secondary()`** — Split weighted_deficits() into the single dominant drive and the rest
- **`dominant_deficit_ratio()`** — How far the dominant drive has fallen below its threshold, as a
- **`build_urgency_imperative()`** — Assemble a natural-language directive for the dominant unmet drive,
