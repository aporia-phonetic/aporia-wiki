# context

*Source: `heterodyne/agents/writers_room/context.py`*

agents/writers_room/context.py

Shared episode-context assembly, extracted from Dramatist.generate_episode
so both script pipelines (monolithic Dramatist and the writers' room) build
their prompts from the same sources: world_config.json, the season
sourcebook (with whole-world chronicle fallback), and the bridged cast
roster. All content is data-driven — nothing here assumes any particular
world, genre, or cast (see CLAUDE.md).

## Top-level functions

- **`world_context_block()`** — World identity + magic + tone from world_config.json, or '' if none.
- **`season_canon_block()`** — Season sourcebook block, falling back to the whole-world chronicle
- **`roster_block()`** — Character roster block (status, species, appearance, catchphrases)
- **`content_controls_block()`** — Compact violence/death/child constraint block from EpisodeConfig.
- **`narrator_constraints_block()`** — Narrator mode/perspective constraints for the scene writer.
- **`resolve_world()`** — World id from the ledger, falling back to the environment default.
