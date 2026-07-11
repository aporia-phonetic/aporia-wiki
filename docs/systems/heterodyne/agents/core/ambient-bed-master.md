# ambient_bed_master

*Source: `heterodyne/agents/ambient_bed_master.py`*

agents.ambient_bed_master — A9 agent.

AmbientBedMaster resolves a sequence of `AmbientBedQuery` records into an
`AmbientBedPlan`, then renders the plan to a single bed-only WAV. The
plan also stands on its own — Phase B's mixer integration consumes the
plan directly without going through `render_plan`.

Phase A pipeline (standalone, isolated from main.py):

    catalog  = build_seed_catalog()
    backend  = StubAmbientBedBackend()
    agent    = AmbientBedMaster(catalog, backend)
    plan     = agent.resolve([(query_scene_1, 30.0), (query_scene_2, 45.0)])
    wav_path = agent.render_plan(plan, Path("/tmp/bed.wav"))

Phase B pipeline (post-hardware, wired into main.py):

    Dramatist → ... → Foley Master → AmbientBedMaster → Mixer

    The wire-in adapter builds an AmbientBedQuery per scene from
    ScriptBlock.ambient_bed_id, LocationEntry, and ChannelPreset, and
    `mixer.mix_episode` consumes the plan as a fourth bus (joined to
    the amix after the aecho reverb leg, before A3 transmission filter).

Selection chain per query (first hit wins):
    1. query.block_override_bed_id      — Dramatist per-block override
    2. query.location_override_bed_id   — world per-location override
    3. catalog scorer best match        — by school + tags + energy
    4. query.channel_default_bed_id     — channel-level fallback
    5. terminal fallback                — `universal_pink_minus50`

Segment coalescing: adjacent queries that resolve to the same bed_id
collapse into one BedSegment, so a long conversation in the same
location does not crossfade against itself. Crossfades happen only at
bed_id boundaries.

## Defined here

### `AmbientBedMaster`

A9 agent: resolves queries to a plan and renders the plan to WAV.

Standalone in Phase A — does not import WorldLedger, ChannelPreset,
ScriptBlock, or any pipeline module. The agent is constructed with a
catalog + backend(s) and tested in isolation.

Phase B preserves the public surface; only the call site changes
(main.py constructs queries from real schemas and `mixer.mix_episode`
consumes the plan instead of `render_plan`).
