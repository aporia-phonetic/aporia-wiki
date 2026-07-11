# story_service

*Source: `heterodyne/agents/story_service.py`*

agents/story_service.py — Story-seed assembly over a built world + portable cast.

The story layer of the World / Character / Story split. A story season is created
*against* an already-built world and a registry of portable characters. This
service turns a story spec into the season's artifacts:

    seasons/season_NN/story_seed.json      the StorySeed (cast roles, deltas, gates)
    seasons/season_NN/plot_gates.json       gui-compatible gate chain
    seasons/season_NN/world_deltas.json     season-scoped additions/changes
    seasons/season_NN/season_config.json    derived SeasonConfig (channel-shaped)
    instances/{character_id}.json           per-world instance per cast member

It does NOT generate the world or the characters' foundations — it references
them. New characters a story needs (CastRole.generate=True) get basic engine
generation and are registered globally before being cast.

## Defined here

### `StoryBuildError`

Raised when a story can't be built (e.g. world not built, missing cast).

## Top-level functions

- **`resolve_cast()`** — Ensure every cast member has a global identity and a per-world instance.
- **`create_story()`** — Build and persist a story season's artifacts over a built world.
