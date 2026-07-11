# character_identity

*Source: `heterodyne/schemas/character_identity.py`*

schemas.character_identity — Portable, world-agnostic character identity + registry.

This is the "soul" half of the character split introduced by the World /
Character / Story decoupling. A CharacterIdentity holds only the fields that
are invariant no matter which world the character appears in: voice, archetype,
ACES, flaw, suit, species, mannerisms, look. Anything that is world-relative
and mutable (knowledge, trust, emotional state, arc, secrets, relationships)
lives in a per-(character x world) *instance* under
data/worlds/{world_id}/instances/{character_id}.json — see
schemas.character_instance.

Identities live in a global registry at data/characters/{character_id}/identity.json
and are eligible to be cast into any world or channel.

Engine core only — never imports from gui/. The field set deliberately mirrors
the portable subset of gui.state.CharacterSheet so the two can round-trip.

## Defined here

### `AcesStats`

| Field | Type |
|---|---|
| `athletics` | `int` |
| `cunning` | `int` |
| `eloquence` | `int` |
| `strange` | `int` |

### `PhysicalDescription`

| Field | Type |
|---|---|
| `height` | `str` |
| `build` | `str` |
| `distinguishing_features` | `str` |
| `general_appearance` | `str` |

### `CharacterIdentity`

The portable identity of a character, independent of any world or story.

| Field | Type |
|---|---|
| `character_id` | `str` |
| `name` | `str` |
| `voice_seed_id` | `str` |
| `archetype` | `str` |
| `resonance_school` | `str` |
| `aces` | `AcesStats` |
| `flaw` | `str` |
| `suit` | `str` |
| `species` | `str` |
| `leitmotif_description` | `str` |
| `voice_description` | `str` |
| `linguistic_id` | `str` |
| `catchphrases` | `list[str]` |
| `physical_description` | `PhysicalDescription` |
| `visual_seed_id` | `str` |
| `behavioral_mask` | `dict` |
| `origin_world` | `str` |
| `created_at` | `str` |

### `Appearance`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season_number` | `int` |
| `tier` | `str` |
| `recorded_at` | `str` |

### `AppearanceIndex`

| Field | Type |
|---|---|
| `character_id` | `str` |
| `appearances` | `list[Appearance]` |

### `CharacterRegistry`

Filesystem-backed store for portable CharacterIdentity records.

## Top-level functions

- **`derive_character_id()`** — Stable, filesystem-safe id from a character's display name.
