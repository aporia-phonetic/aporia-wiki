# ambient_bed_catalog

*Source: `heterodyne/schemas/ambient_bed_catalog.py`*

Ambient bed catalog — Pydantic models for the A9 ambient-bed layer.

The ambient bed is the *fourth* sonic category in AEON-ENGINE, distinct from
dialogue, music, and foley. It is continuous, non-event-driven background
texture that establishes the physical reality of a scene: stone-room silence,
distant wind, the low hum of a ritual chamber. Listeners do not consciously
hear a good bed; they feel its absence when it drops to digital zero.

This module defines the data shapes only. The agent
(`agents.ambient_bed_master`) consumes these, the catalog loader
(`agents.ambient_bed_catalog`) persists them, and the rendering backends
(`agents.ambient_bed_backend`) turn them into PCM.

Phase A scope (pre-hardware):
  - These schemas exist as standalone, self-contained types.
  - `AmbientBedQuery` carries everything the agent needs without importing
    `WorldLedger`, `ChannelPreset`, or `ScriptBlock`. Phase B will write a
    thin adapter that builds Queries from the real production schemas.
  - `AmbientBedSettings` is a local stand-in for the eventual extension of
    `MixerSettings`. When Phase B wires the bed into mixer.py, these fields
    fold into MixerSettings unchanged.

The bed catalog does NOT share storage with the foley catalog. Beds are
loopable, continuous textures; foley entries are atomic events. Mixing the
two categories into one catalog would defeat the family-narrowing logic on
both sides.

## Defined here

### `AmbientBedEntry`

One loopable ambient bed in the library.

Unlike foley catalog entries (which are atomic events), ambient bed
entries are continuous textures designed to loop seamlessly under
dialogue for the duration of a scene. The `intrinsic_db` field
records the level the bed sits at in a finished mix; the agent
modulates this by scene_energy and bed_id-specific intensity.

Naming convention: `<school_or_region>_<character>_<level>` where
school is the resonance school affinity if any (e.g.
`stone_atrium_low`, `veil_subaqueous`, `ash_wind_distant`).

| Field | Type |
|---|---|
| `bed_id` | `str` |
| `family` | `AmbientBedFamily` |
| `file_path` | `Optional[Path]` |
| `loop_safe` | `bool` |
| `intrinsic_db` | `float` |
| `intensity_range` | `tuple[float, float]` |
| `fade_in_ms` | `int` |
| `fade_out_ms` | `int` |
| `school_affinity` | `list[str]` |
| `energy_affinity` | `list[str]` |
| `location_tags` | `list[str]` |
| `source` | `AmbientBedSource` |
| `license` | `CatalogLicense` |
| `attribution` | `Optional[str]` |
| `notes` | `Optional[str]` |

### `AmbientBedCatalog`

In-memory catalog of ambient bed entries.

The Phase A loader (`agents.ambient_bed_catalog`) populates this from
a static seed list. Phase B may add SQLite persistence parallel to the
foley catalog, but Phase A keeps the catalog purely in-memory — the
seed list is the source of truth and `bed_id`s are stable.

| Field | Type |
|---|---|
| `entries` | `list[AmbientBedEntry]` |

### `AmbientBedQuery`

Self-contained input to AmbientBedMaster.

Carries every field the selection chain needs to resolve a bed_id
*without* importing WorldLedger, ChannelPreset, or ScriptBlock.
Phase B's wire-in adapter will build these from the real production
schemas; Phase A constructs them directly in tests.

Selection chain (first hit wins):
  1. block_override_bed_id        — Dramatist-side per-block override
  2. location_override_bed_id     — world-side per-location override
  3. catalog scorer over (location_tags ∪ acoustic_character,
                          resonance_school, scene_energy)
  4. channel_default_bed_id       — channel fallback only
  5. terminal fallback            — `universal_pink_minus50`

| Field | Type |
|---|---|
| `location_id` | `Optional[str]` |
| `location_tags` | `list[str]` |
| `acoustic_character` | `Optional[str]` |
| `resonance_school` | `Optional[str]` |
| `scene_energy` | `str` |
| `block_override_bed_id` | `Optional[str]` |
| `location_override_bed_id` | `Optional[str]` |
| `channel_default_bed_id` | `Optional[str]` |

### `BedSegment`

One contiguous stretch of a single ambient bed.

The agent coalesces adjacent scenes that resolve to the same bed_id
into one BedSegment, so a long conversation across two beats of the
same location does not crossfade against itself. Crossfades happen
only at bed_id boundaries.

| Field | Type |
|---|---|
| `start_s` | `float` |
| `end_s` | `float` |
| `bed_id` | `str` |
| `intensity` | `float` |
| `fade_in_ms` | `int` |
| `fade_out_ms` | `int` |
| `energy_bucket` | `str` |
| `reason` | `str` |

### `AmbientBedPlan`

The agent's output — a list of bed segments covering the episode.

Phase A: rendered by `AmbientBedMaster.render_plan` into a single
bed-only WAV for standalone testing. Phase B: consumed by `mixer.py`
as a fourth bus, joining the four-way amix after the per-location
aecho reverb leg (the bed bypasses reverb because the bed *is* the
room).

| Field | Type |
|---|---|
| `segments` | `list[BedSegment]` |
| `total_duration_s` | `float` |

### `AmbientBedSettings`

Tuning knobs for the ambient bed layer.

Phase A: stand-alone settings model passed to AmbientBedMaster.
Phase B: these fields fold into `schemas.mixer_settings.MixerSettings`
so the layer can be tuned from the same GUI as voice/foley/music.

| Field | Type |
|---|---|
| `ambient_bed_enabled` | `bool` |
| `ambient_bed_db` | `float` |
| `sidechain_ambient_ratio` | `float` |
| `ambient_bed_intensity_floor` | `float` |
| `ambient_bed_crossfade_ms` | `int` |
| `ambient_bed_ma_boost_db` | `float` |
