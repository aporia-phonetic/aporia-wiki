# music_prompts

*Source: `heterodyne/agents/music_prompts.py`*

Music stem registry — the canonical declaration of what stems must exist
in the audio drama engine's audio/stems/ library for the active world.

Per HETERODYNE/CLAUDE.md's world-agnostic architecture rule, this module
must not hardcode any specific world's character names, magic/power-system
names, or lore. World-specific stem entries (character leitmotifs, school/
power-system signatures, season themes) live in
data/worlds/{world_id}/stem_registry.json — see schemas.paths.world_stem_registry_path
and _load_world_entries below, which mirror the pattern already established
by agents/scene_context.py for the location gazetteer.

A small set of "emotional bed" fallback entries (tension_low, tension_high,
wonder) ship as engine-level defaults: they describe mood/instrumentation
only, no character or setting names, so they're safe to keep in code (the
same content would make sense under any genre/era) and act as the resolver
fallback for music_cue triggers that don't resolve to a world-specific
leitmotif. A world can override any of these by defining an entry with the
same stem_id in its own stem_registry.json.

get_registry(world_id) returns the world's entries merged with the universal
fallback beds (world entries win on stem_id collision); the generator
(scripts/generate_stems.py) walks this list in order.

## Top-level functions

- **`get_registry()`** — Return the stem registry for `world_id` (resolved via
- **`get_entry_by_stem_id()`** — Return a single registry entry by stem_id, or raise KeyError.
