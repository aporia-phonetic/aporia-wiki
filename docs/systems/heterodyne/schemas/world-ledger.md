# world_ledger

*Source: `heterodyne/schemas/world_ledger.py`*

schemas/world_ledger.py

Canonical World Ledger schema for the Aeon Pulp Drama Engine.

Covers all base fields (Phase 1) plus the full Latent Extensions suite:
  - Narrative Codification  (ConflictType, NarrativeState)
  - Knowledge State         (P1 — highest continuity impact)
  - Trust Map               (P3 — directional, independent of bond_strength)
  - Emotional Baseline      (P5 — baseline_affect + current_affect)
  - Location Registry       (P4 — named locations with status flags)
  - Resource Inventory      (P8 — supplies beyond water)
  - Time / Fatigue          (P10 — elapsed hours, fatigue level)
  - Segment Closing Pos.    (P11 — per-character location at segment end)
  - Dead Variable Detector  (P7 — active flags + reactivation triggers)
  - Callback Registry       (P6 — SQLite-backed; model defined here)
  - World Clock             (Chronicle §2.2 — authoritative world time)
  - Temporal Position       (Chronicle §3.1 — present / historical / multi-era)
  - A2: Gender Presentation  — per-character grammatical-gender marker for multilingual TTS
  - A2: Cultural Markets     — world-level list of active translation market codes
  - A4: BehavioralMaskConfig — structured persona mask (strange_stat, absolute certainty,
                               elusive grace, mannerism exhaustion tracking). Feeds QA
                               checks at prompt level now; feeds logit processor after
                               local LLM is live. agency_level already present on
                               NarrativeState — no migration needed.

Write-lock is enforced at the Archivist layer — this schema is read-only during
all generation steps.

## Defined here

### `ConflictType`

The dominant conflict type active for a character this episode.

Derived by the Archivist's classify_conflict_type() at episode open.
Passed to the Dramatist as part of the dynamic context block.

### `KnowledgeConfidence`

Confidence level for a single fact in a character's knowledge_state dict.

unknown     — Character has no awareness of this fact.
rumored     — Character has heard something but has no reliable source.
suspected   — Character has indirect evidence; believes it likely.
observed    — Character witnessed or experienced something directly.
confirmed   — Character has verified the fact through a reliable source.
self_known  — Character knows this about themselves; has not disclosed it.

### `AffectState`

Emotional state of a character entering this episode.

Set by the Archivist from prior episode outcomes.
Consumed by the Dramatist to calibrate tone and interiority.

### `LocationStatus`

Status of a named location in the location registry.

unknown      — Exists in fiction; crew has no awareness.
known_exists — Crew knows it exists but has not reached it.
discovered   — Crew has found it; may not be accessible.
established  — Crew has visited; position in world confirmed.
destroyed    — Permanently removed from play.
sealed       — Passage blocked; requires unsealing event to reuse.

### `DepletionLevel`

Depletion model for non-numeric supplies.

### `FatigueLevel`

Crew fatigue level based on elapsed expedition time and sleep cycles.

Modifies Dramatist generation: exhausted crew makes worse decisions,
misreads situations, reacts slower. Feeds Perception Layer probability.

### `CallbackStatus`

Lifecycle state of a narrative callback.

### `CallbackPayoffType`

How the callback is meant to resolve.

### `AwarenessState`

Mutual awareness level of a relationship between two characters.

LATENT       — Relationship exists (by history or blood) but neither party
               is aware of its significance. The story hasn't surfaced it.
ONE_SIDED    — One character is aware of the relationship; the other is not.
               Asymmetric: always store which direction knows.
BOTH_AWARE   — Both parties know the relationship exists and what it means.
PUBLICLY_KNOWN — The relationship is common knowledge in the fiction.

### `GhostSignalStatus`

State of the ghost signal narrative device (S.S. Aporia transmission).

DORMANT      — Signal inactive; Ticker detects nothing.
ACTIVE       — Signal detectable by Ticker; crew unaware.
BROADCASTING — Signal actively transmitting narrative content.
FRAGMENTED   — Signal degraded; partial or corrupted transmissions.

### `RelationshipType`

Categorical type of a relationship edge in the Relational Graph.

### `RelationshipEdge`

A single directed relationship edge in the Relational Graph.

Edges are stored per-direction. Bond strength and awareness_state may
differ between source→target and target→source if asymmetric.

bond_strength is affective — the depth of the connection. It is distinct
from trust_level (TrustMap), which is epistemic — confidence in reliability.
A character can have high bond strength with someone they distrust,
and vice versa.

| Field | Type |
|---|---|
| `source` | `str` |
| `target` | `str` |
| `relationship_type` | `RelationshipType` |
| `bond_strength` | `float` |
| `awareness_state` | `AwarenessState` |
| `notes` | `Optional[str]` |
| `formative_period` | `Optional[str]` |
| `family_degree` | `Optional[int]` |
| `established_episode` | `Optional[int]` |

### `RelationalGraph`

Full directed graph of character relationships for the active season.

Edges are stored per-direction for query convenience. Bond strength
may differ between the two directions. The Archivist upserts edges
after disclosure events and bond-affecting story beats.

| Field | Type |
|---|---|
| `edges` | `List[RelationshipEdge]` |

### `AwarenessRecord`

One observer's awareness of a fixed-history relationship.

Distinct from the AwarenessState enum, which describes *mutual* awareness of
a live RelationalGraph edge. This record is *per-observer*: any character in
the ledger — plus the literal observer key ``"audience"`` — holds an
independent awareness state for a FamilyRelationship or FormativeRelationship.

Absence of an observer key from the relationship's awareness dict means that
observer is unaware (equivalent to ``knows=False``).

| Field | Type |
|---|---|
| `knows` | `bool` |
| `disclosure_episode` | `Optional[int]` |
| `source` | `Optional[str]` |

### `FamilyRelationship`

Biological or legal lineage between two entities.

Does not decay — a parent is a parent whether or not they have spoken in
thirty years. What makes it narratively active is *who knows about it*,
tracked per-observer in ``awareness``. Lives at the WorldLedger root, not on
a character entry: a relationship is an independent fact observed by multiple
parties, not a property of either party.

| Field | Type |
|---|---|
| `relationship_id` | `str` |
| `character_a_id` | `str` |
| `character_b_id` | `str` |
| `relationship_type` | `Literal['parent', 'child', 'sibling', 'half_sibling', 'adoptive_parent', 'adoptive_child', 'unknown_relative']` |
| `direction` | `Literal['a_to_b', 'b_to_a', 'mutual']` |
| `notes` | `Optional[str]` |
| `awareness` | `Dict[str, AwarenessRecord]` |

### `FormativeRelationship`

Historically fixed non-blood bond.

Permanent in history, variable in current affect. You can stop being
someone's ally; you do not stop having been their teacher. Affect and decay
live in the RelationalGraph; this record carries only the fixed historical
fact plus per-observer awareness of it.

| Field | Type |
|---|---|
| `relationship_id` | `str` |
| `character_a_id` | `str` |
| `character_b_id` | `str` |
| `relationship_type` | `Literal['mentor', 'student', 'ward', 'former_partner', 'estranged_colleague', 'rival_formative', 'surrogate_parent', 'surrogate_child']` |
| `direction` | `Literal['a_to_b', 'b_to_a', 'mutual']` |
| `notes` | `Optional[str]` |
| `awareness` | `Dict[str, AwarenessRecord]` |

### `StoryCircleState`

Dan Harmon's Story Circle position tracker for the protagonist arc.

Steps (Dan Harmon's formulation):
  1. You      — Status quo established. Character in their zone of comfort.
  2. Need     — Discontent or problem introduced.
  3. Go       — Enter the unfamiliar situation or world.
  4. Search   — Adapt and struggle in the unfamiliar.
  5. Find     — Discover what was wanted (the object of desire).
  6. Take     — Pay a heavy price for the discovery.
  7. Return   — Return to the familiar situation.
  8. Change   — Exhibit transformation (better or worse).

Archivist advances current_step at episode commit when it validates
that the expected narrative beat for the current step was delivered.
Step 8 (Change) is the season-level arc resolution — typically Episode 10+.

| Field | Type |
|---|---|
| `current_step` | `int` |
| `step_episode_map` | `Dict[int, int]` |
| `protagonist_id` | `str` |
| `change_record` | `Optional[str]` |
| `STEP_DESCRIPTIONS` | `Dict[int, str]` |

### `NarrativeState`

Narrative pressure variables for a single character in a single episode.

Calculated by the Archivist's classify_conflict_type() at episode open.
Consumed by the Dramatist to determine generation mode and escalation rules.

| Field | Type |
|---|---|
| `conflict_type` | `ConflictType` |
| `agency_level` | `float` |
| `narrative_pressure` | `int` |

### `FactRecord`

A single fact in a character's knowledge_state.

Carries enough metadata for the Archivist's between-episode decay pass:
confidence, when it was learned, when it was last referenced, and an
emotional_weight set by the Dramatist that protects high-impact memory
from being forgotten.

| Field | Type |
|---|---|
| `confidence` | `KnowledgeConfidence` |
| `year_learned` | `int` |
| `year_last_referenced` | `int` |
| `emotional_weight` | `float` |

### `KnowledgeState`

Per-character map of known facts → FactRecord (confidence + provenance).

Updated by the Archivist after each episode from World Ledger events.
Passed to the Dramatist as part of the character context block.
Constrains what each character may reference in dialogue.

Keys are snake_case fact identifiers (e.g. 'ondra_withheld_translation').

Legacy shape — Dict[str, KnowledgeConfidence] — is accepted on load and
promoted to FactRecord with year_learned=0 and default emotional_weight.

| Field | Type |
|---|---|
| `facts` | `Dict[str, FactRecord]` |

### `TrustEntry`

Directional trust level from one character toward another.

trust_level is independent of bond_strength. A character can have
high bond strength with someone they distrust (Maren → Cael) and
low bond strength with someone they fully trust (Maren → Ondra, professionally).

Decay is slow. A single betrayal event can collapse it to 0.
Verified promises and successful disclosures raise it incrementally.

| Field | Type |
|---|---|
| `trust_level` | `float` |
| `last_event` | `Optional[str]` |
| `last_event_episode` | `Optional[int]` |

### `TrustMap`

Full directional trust map for a single character.

Keys are target character names (lowercase). Values are TrustEntry models.
Asymmetric: maren.trust_toward['cael'] != cael.trust_toward['maren'].

| Field | Type |
|---|---|
| `trust_toward` | `Dict[str, TrustEntry]` |

### `EmotionalState`

Emotional register for a single character.

baseline_affect: default emotional register, stable across the season.
                 Set at character creation. Changes only at major arc beats.
current_affect:  emotional state entering this episode.
                 Updated by the Archivist from prior episode outcomes.

| Field | Type |
|---|---|
| `baseline_affect` | `AffectState` |
| `current_affect` | `AffectState` |
| `affect_note` | `Optional[str]` |

### `LocationEntry`

A single named location in the Keth-Saraal location registry.

The Dramatist cannot introduce a new named location without the Archivist
adding it here first. Sealed locations cannot appear in scenes without a
recorded unsealing event. Destroyed locations are permanently off-limits.

| Field | Type |
|---|---|
| `status` | `LocationStatus` |
| `accessible` | `bool` |
| `mapped` | `bool` |
| `first_appeared_episode` | `Optional[int]` |
| `sealed_by_event` | `Optional[str]` |
| `notes` | `Optional[str]` |
| `location_map` | `Optional[LocationMap]` |
| `map_status` | `Literal['none', 'generated', 'needs_update', 'manual']` |
| `grid_coordinates` | `Optional[Dict[str, Tuple[int, int]]]` |

### `LocationRegistry`

Full registry of named locations in the active season's setting.

Seeded at season open from the Series Bible. Updated by the Archivist
whenever the Dramatist introduces a new location (flagged via
new_locations_introduced in the JSON-Audio-Map output).

| Field | Type |
|---|---|
| `locations` | `Dict[str, LocationEntry]` |

### `Supplies`

Tracked resource inventory for the expedition.

The Dramatist is constrained by these values.
LOW light sources means unexplored areas require a scene-level solution.
CRITICAL food is a time pressure the Dramatist must acknowledge.
EXHAUSTED of any resource is a hard constraint — that resource cannot appear.

Enforces the action-dynamic 33% weighting through environmental scarcity
rather than only through conflict events.

| Field | Type |
|---|---|
| `water_hours` | `float` |
| `food_days` | `float` |
| `medical_basic` | `DepletionLevel` |
| `light_sources` | `DepletionLevel` |
| `rope_meters` | `float` |
| `auric_artifacts_attuned` | `int` |

### `TimeState`

Expedition time tracking.

expedition_elapsed_hours: total hours since descent began.
                          Incremented by Archivist from Dramatist's
                          estimated episode duration in World Ledger update.
estimated_surface_time:   approximate time of day on the surface.
                          Meaningless underground but relevant for crew
                          psychological state — they know what time it is above.
last_sleep_cycle_hours_ago: hours since the crew last slept.
crew_fatigue_level:       aggregate fatigue state.

Fatigue modifies Dramatist generation: exhausted crew makes worse decisions,
misreads situations, reacts slower. Feeds Perception Layer directly.

| Field | Type |
|---|---|
| `expedition_elapsed_hours` | `float` |
| `estimated_surface_time` | `str` |
| `last_sleep_cycle_hours_ago` | `float` |
| `crew_fatigue_level` | `FatigueLevel` |

### `EpisodeTimestamp`

Anchor for one episode in absolute world time.

Committed by the Archivist after every episode. The Chronicle aging pass
and Deep Ledger historical lookups both walk this list.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `year` | `int` |
| `day` | `int` |
| `elapsed_days_from_season_start` | `int` |

### `WorldClock`

Authoritative world time for the Chronicle and Deep Ledger.

Advanced by the Archivist after every episode commit using the per-segment
``time_elapsed_days`` produced by the Dramatist. ``TimeState`` continues to
track expedition-scale fatigue; ``WorldClock`` is the year/day source of
truth for character aging, era lookup, and timestamping.

| Field | Type |
|---|---|
| `current_year` | `int` |
| `current_era` | `str` |
| `era_year` | `int` |
| `season_started_year` | `int` |
| `elapsed_days_this_season` | `int` |
| `episode_timestamps` | `List[EpisodeTimestamp]` |

### `TemporalPosition`

Season-level placement on the timeline.

The Archivist uses this to decide whether to read the live WorldLedger
(present), build a historical snapshot from the Deep Ledger (historical),
or hot-swap snapshots per episode (multi_era / time-travel seasons).

| Field | Type |
|---|---|
| `position_type` | `Literal['present', 'historical', 'multi_era']` |
| `target_year` | `Optional[int]` |
| `target_era_id` | `Optional[str]` |
| `era_sequence` | `Optional[List[str]]` |

### `SegmentClosingPositions`

Per-character location at the close of the most recently committed segment.

Updated by the Archivist from the Dramatist's JSON-Audio-Map output.
Passed to the Dramatist as part of the dynamic context block for the
next segment, constraining where each character can begin the next scene
without requiring travel time.

Also feeds the Foley Master with precise location data for ambient
sound consistency without additional generation calls.

| Field | Type |
|---|---|
| `positions` | `Dict[str, str]` |
| `segment_number` | `int` |
| `episode` | `int` |

### `TrackedVariable`

A single World Ledger variable with an active/inactive flag.

Inactive variables are excluded from the Dramatist's dynamic context block
by the Archivist's context-prep logic. Nothing is deleted — only excluded.

reactivation_trigger: natural-language description of the condition under
                      which this variable re-enters the active context.
reactivation_episode_gate: earliest episode at which reactivation is possible.
                           Archivist checks this before evaluating the trigger.

| Field | Type |
|---|---|
| `value` | `Any` |
| `active` | `bool` |
| `reactivation_trigger` | `Optional[str]` |
| `reactivation_episode_gate` | `Optional[int]` |

### `Callback`

A single narrative callback: a detail planted in one episode meant to
pay off in a later episode.

Seeded by the Archivist from plot gate data at season open.
Passed to the Dramatist as active_callbacks when planted_episode has
passed but intended_payoff_episode has not yet arrived.
When a callback is triggered in generation, its status updates to TRIGGERED.

| Field | Type |
|---|---|
| `callback_id` | `str` |
| `planted_episode` | `int` |
| `planted_block_id` | `Optional[str]` |
| `description` | `str` |
| `intended_payoff_episode` | `int` |
| `payoff_type` | `CallbackPayoffType` |
| `status` | `CallbackStatus` |
| `payoff_description` | `str` |
| `triggered_episode` | `Optional[int]` |
| `triggered_block_id` | `Optional[str]` |

### `GenderPresentation`

Grammatical-gender presentation for a character.

Used by the Translation Agent's Cultural Integrity Pass to make correct
grammatical-gender choices in gendered languages (Spanish, Portuguese, French,
Hindi, etc.) and by the TTS Voice Engine to select gendered vocal references.

This field is NON-OPTIONAL on CharacterExtension. Without it, gendered-language
translations make arbitrary grammatical-gender assignments which undermine the
character-voice-consistency moat.

Values:
  MASCULINE   — character presents masculine; translations use masculine grammatical forms.
  FEMININE    — character presents feminine; translations use feminine grammatical forms.
  NEUTRAL     — character is gender-neutral or non-binary; translations use neutral
                forms where available (e.g. Swedish "hen", Spanish "-e" ending)
                or masculine as grammatical default where no neutral exists.
  AMBIGUOUS   — character's gender is deliberately withheld as a story element;
                translator uses a consistent unmarked form and notes the ambiguity.
                The Dramatist is instructed to preserve this ambiguity in English.

### `BehavioralMaskConfig`

Structured behavioral persona mask for a character.

The free-text ``voice_description`` (TTS/character config) feeds the Dramatist
prompt directly. This JSON structure is the machine-readable parallel:
  - At prompt level (now): Dramatist receives strange_stat, mannerism list,
    suppressed mannerisms, and absolute_certainty flag to shape generation.
  - At logit level (after local LLM is live, A4 activation):
    Strange-Tier vocabulary distortion, Absolute Certainty hard-suppress,
    Elusive Grace semantic-cluster amplification.

All logit-layer fields are safe to populate now — they are ignored until the
logit processor is wired. No migration needed at activation.

agency_level lives on NarrativeState (already present); no duplication needed.

| Field | Type |
|---|---|
| `strange_stat` | `int` |
| `absolute_certainty` | `bool` |
| `suppressed_modals` | `List[str]` |
| `elusive_grace` | `bool` |
| `semantic_clusters` | `List[str]` |
| `mannerisms` | `List[str]` |
| `mannerism_cooldown` | `Dict[str, int]` |
| `mannerism_cooldown_blocks` | `int` |

### `CharacterExtension`

All Latent Extension fields for a single character.

Kept separate from the core character dict in WorldLedger so that
the existing character schema is not broken during the upgrade.
The Archivist merges this into the character context block at episode open.

| Field | Type |
|---|---|
| `narrative_state` | `NarrativeState` |
| `knowledge_state` | `KnowledgeState` |
| `trust_map` | `TrustMap` |
| `emotional_state` | `EmotionalState` |
| `gender_presentation` | `GenderPresentation` |
| `behavioral_masks_json` | `Optional[BehavioralMaskConfig]` |

### `WorldLedger`

Canonical World Ledger for the Aeon Pulp Drama Engine.

Written only after generation completes (write-lock pattern enforced
by the Archivist). Read-only during all segment generation steps.

Base fields are unchanged from the original schema. All Latent Extension
fields are additive — no existing field names or types were modified.

| Field | Type |
|---|---|
| `season` | `int` |
| `episode` | `int` |
| `world_id` | `str` |
| `next_daily_gate` | `str` |
| `cultural_markets` | `List[str]` |
| `previous_episode_hooks` | `List[str]` |
| `debuted_voice_seed_ids` | `List[str]` |
| `location` | `str` |
| `characters` | `Dict[str, Any]` |
| `locations` | `Dict[str, Any]` |
| `artifacts` | `Dict[str, Any]` |
| `active_threats` | `List[str]` |
| `character_extensions` | `Dict[str, CharacterExtension]` |
| `location_registry` | `LocationRegistry` |
| `supplies` | `Supplies` |
| `time_state` | `TimeState` |
| `world_clock` | `WorldClock` |
| `segment_closing_positions` | `SegmentClosingPositions` |
| `callback_registry` | `List[Callback]` |
| `relational_graph` | `RelationalGraph` |
| `family_relationships` | `List[FamilyRelationship]` |
| `formative_relationships` | `List[FormativeRelationship]` |
| `ghost_signal_status` | `GhostSignalStatus` |
| `ghost_signal_episode_activated` | `Optional[int]` |
| `ghost_signal_notes` | `str` |
| `story_circle_state` | `StoryCircleState` |
| `crossover_records` | `List[Dict[str, Any]]` |
| `tracked_variables` | `Dict[str, TrackedVariable]` |
