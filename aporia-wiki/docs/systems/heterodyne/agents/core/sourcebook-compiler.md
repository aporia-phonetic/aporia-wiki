# sourcebook_compiler

*Source: `heterodyne/agents/sourcebook_compiler.py`*

agents/sourcebook_compiler.py — World sourcebook (bible) compiler.

The final step of the standalone *world build*. Once the Sediment Engine has
laid down a world's deep history (deep_ledger.db), the Sourcebook Compiler turns
that history — plus the world's identity (world_config.json) and a present-day
narrative pass — into a first-class, human-readable world bible:

    data/worlds/{world_id}/sourcebook.json   structured bible
    data/worlds/{world_id}/sourcebook.md     readable bible

This is what makes a world stand on its own *before* any story or character
exists. It reuses the Sediment Engine's read side (chronicle_summary,
export_history_markdown) rather than re-querying the deep ledger.

The "narrative pass" (present-day factions / power map / open tensions) is a
light Claude call modelled on scripts/bootstrap_world._derive_chronicle_params:
single call, strict JSON, fully non-fatal — a world still compiles a sourcebook
if the call fails, just without the present-day section.

## Defined here

### `SourcebookCompiler`

Compiles a world's sourcebook from its config + deep ledger + narrative.

Pass ``season_number``/``temporal_position`` to scope the sourcebook to a
season's era instead of the world's present day — every current call site
(bootstrap_world.build_world, main.py --chronicle/--sourcebook, aeon.py
world create) omits both, so behavior there is unchanged.

## Top-level functions

- **`generate_world_narrative()`** — Run the present-day (or season-era) narrative pass. Returns {} on any
- **`load_season_sourcebook()`** — Load a previously-compiled season-scoped sourcebook, if one exists.
