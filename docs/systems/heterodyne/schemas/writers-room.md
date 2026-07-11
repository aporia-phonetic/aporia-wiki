# writers_room

*Source: `heterodyne/schemas/writers_room.py`*

schemas/writers_room.py

Intermediate artifacts for the writers'-room script pipeline
(agents/writers_room/). These are engine-only concepts — beat sheets,
per-character scene intentions, draft scenes, planted setups — and carry
no world-specific content. The pipeline's *final* output is the same
schemas.script_block.SegmentScript the monolithic Dramatist emits.

## Defined here

### `PlantedSetup`

One tracked narrative setup: planted, advanced, and eventually paid off.

The beat planner receives all open setups each episode and must advance
or pay off aging ones; the ledger extractor records what the finished
segment actually did. Reveals become *earned*: a twist is only allowed
to invert something previously planted.

| Field | Type |
|---|---|
| `setup_id` | `str` |
| `description` | `str` |
| `planted_episode` | `int` |
| `intended_payoff_hint` | `str` |
| `status` | `Literal['open', 'advanced', 'paid_off']` |
| `advanced_in_episodes` | `List[int]` |
| `paid_off_episode` | `Optional[int]` |

### `SceneBeat`

One planned scene inside a segment.

| Field | Type |
|---|---|
| `scene_id` | `str` |
| `location` | `str` |
| `characters` | `List[str]` |
| `objective` | `str` |
| `conflict` | `str` |
| `carries_crisis_peak` | `bool` |
| `setups_to_advance` | `List[str]` |
| `setups_to_plant` | `List[str]` |
| `tone` | `str` |

### `SegmentBeats`

The planned scene list for one of the four segments.

| Field | Type |
|---|---|
| `segment` | `int` |
| `scenes` | `List[SceneBeat]` |
| `segment_end_hook` | `str` |
| `dominant_tone` | `str` |

### `BeatSheet`

Whole-episode plan: 4 segments of scenes, planned in ONE call so the
episode's structure is globally coherent (setups early, payoff late).

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `segments` | `List[SegmentBeats]` |

### `SceneIntention`

One character's private stance entering a scene, scoped to what THEY
know. Feeds the scene writer as advisory material — actors advise,
the playwright writes.

| Field | Type |
|---|---|
| `character` | `str` |
| `wants` | `str` |
| `hides` | `str` |
| `would_do` | `str` |

### `DraftLine`

One spoken/narrated line in a draft scene. Deliberately minimal:
dialogue craft only — no foley, music, SSML, or IDs. Annotator stages
and the assembler add production metadata afterwards.

| Field | Type |
|---|---|
| `character` | `str` |
| `type` | `Literal['dialogue', 'narration']` |
| `text` | `str` |
| `scene_energy` | `str` |

### `DraftScene`

The scene writer's output for one SceneBeat, pre-annotation.

| Field | Type |
|---|---|
| `scene_id` | `str` |
| `lines` | `List[DraftLine]` |
| `new_locations_introduced` | `List[str]` |
