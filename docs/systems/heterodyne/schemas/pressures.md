# pressures

*Source: `heterodyne/schemas/pressures.py`*

schemas.pressures — Decaying internal-drive and moral-cost state.

A Pressure is a homeostatic drive (e.g. hunger, security, standing — the
vocabulary is entirely caller-defined) that decays every turn and can be
replenished by an action. A MoralityCost is a behavioral-cost value (e.g.
the psychological price of deceiving someone) that desensitizes with
repeated use, the same way real avoidance costs erode with practice.

Both are keyed by arbitrary string ids on PressureState rather than a
Literal/enum vocabulary, the same pattern KnowledgeState.facts and
TrustMap.trust_toward already use — so any world, any character, and any
archetype can define whichever drives and costs matter to them as data,
without this schema encoding a hierarchy of needs for one genre.

Orchestration across a whole PressureState (weighted deficit prioritization,
urgency-imperative text assembly) lives in agents/pressure_engine.py, mirroring
how agents/archivist.py orchestrates KnowledgeState.decay() rather than
folding that traversal into the schema itself.

## Defined here

### `Pressure`

A single decaying drive vector.

current trends toward 0 every tick (tick()) and is pushed back up by
replenish() when an action serves this drive. deficit() is how far
current has fallen below min_threshold — 0 while the drive is satisfied.
weight is the caller-assigned priority multiplier (omega) used to rank
this drive against a character's other drives; it belongs to the
character/world data that constructs the Pressure, not to this schema.

| Field | Type |
|---|---|
| `current` | `float` |
| `decay_rate_per_turn` | `float` |
| `min_threshold` | `float` |
| `weight` | `float` |
| `max_value` | `float` |

### `MoralityCost`

A behavioral cost that desensitizes with repeated use.

current_cost starts at base_cost and is multiplied by
desensitization_rate every time desensitize() is called — a character
who has told five lies pays less for the sixth. desensitization_rate of
1.0 means this cost never erodes; a value < 1.0 erodes it toward 0
(never below it, since desensitize() only ever multiplies by a
non-negative rate).

| Field | Type |
|---|---|
| `base_cost` | `float` |
| `current_cost` | `Optional[float]` |
| `desensitization_rate` | `float` |
| `times_executed` | `int` |

### `PressureState`

A character's full set of decaying drives and desensitizing costs.

Keys are arbitrary caller-defined ids (e.g. 'security', 'deception') —
this model imposes no vocabulary. None/absent is the inactive state:
a character with no PressureState simply isn't modeled by this system.

| Field | Type |
|---|---|
| `pressures` | `Dict[str, Pressure]` |
| `morality_costs` | `Dict[str, MoralityCost]` |
