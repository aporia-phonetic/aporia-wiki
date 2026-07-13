# character_service

*Source: `heterodyne/agents/character_service.py`*

agents/character_service.py — Global, world-agnostic character generation + registry ops.

The character layer of the World / Character / Story split. A character is a
portable identity (schemas.character_identity.CharacterIdentity) in a global
registry under data/characters/, eligible to be cast into any world. This module:

  * generate_character()    — basic engine generation (one Claude call), the same
                              shape used by season bootstrap, but world-optional.
  * register_character()    — persist a generation/sheet dict as a global identity.
  * backfill_rep_company()  — seed registry identities from the immutable
                              VOICE_SEED_REGISTRY so existing voices are reusable
                              across worlds.

World-rooted fields (known_history, master_secret, arc, goal, public_role, items,
relationships) are *not* part of the portable identity — CharacterIdentity.from_sheet
drops them. They are seeded into a per-world CharacterInstance at story time.

## Top-level functions

- **`generate_character()`** — Generate one character dict. `brief` is optional world/genre context;
- **`register_character()`** — Persist a generation/sheet dict as a portable global identity.
- **`create_character()`** — Create + register a character identity from explicit fields (no Claude).
- **`generate_voice_seed_drafts()`** — Draft `count` new VOICE SEED field-sets via one Claude call.
- **`backfill_rep_company()`** — Seed global identities from the immutable VOICE_SEED_REGISTRY.
