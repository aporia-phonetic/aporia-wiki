# character_instance

*Source: `heterodyne/schemas/character_instance.py`*

schemas.character_instance — Per-(character x world) mutable state.

This is the world-relative half of the character split. While a
CharacterIdentity (schemas.character_identity) is the portable "soul" shared
across every world, a CharacterInstance holds everything that is specific to
one character in one world: what they know, who they trust, how they feel,
their arc/secret/goal *in this world*, and their world-rooted history.

Instances live at data/worlds/{world_id}/instances/{character_id}.json. They
are the persistent seed/snapshot that bootstrap_ledger reads to populate the
live World Ledger at season start; the running ledger remains authoritative
during generation and writes back here at season boundaries.

Default is a fresh, isolated instance per (character, world). A story seed may
opt a character into a **memory bridge** that imports knowledge/arc from that
character's instance in another world — see `import_memory_from`.

Engine core only — never imports from gui/.

## Defined here

### `InstanceRelationship`

| Field | Type |
|---|---|
| `target_character_id` | `str` |
| `target_name` | `str` |
| `description` | `str` |

### `CharacterInstance`

One character's mutable state within one world.

| Field | Type |
|---|---|
| `character_id` | `str` |
| `world_id` | `str` |
| `tier` | `str` |
| `public_role` | `str` |
| `known_history` | `str` |
| `master_secret` | `str` |
| `arc` | `str` |
| `goal` | `str` |
| `items` | `list[str]` |
| `hp` | `int` |
| `plot_armor` | `int` |
| `relationships` | `list[InstanceRelationship]` |
| `knowledge_state` | `dict` |
| `trust_map` | `dict` |
| `emotional_state` | `dict` |
| `narrative_state` | `dict` |
| `story_circle_state` | `dict` |
| `memory_bridged_from` | `Optional[str]` |
| `created_at` | `str` |
| `updated_at` | `str` |

### `WorldInstanceStore`

Filesystem-backed store for a single world's character instances.
