# game_designist

*Source: `heterodyne/agents/game_designist.py`*

agents/game_designist.py — The Game Designist (Agent 20)

Converts existing episode assets into complete VTT-ready module packages.

Reads from:
  - world_ledger.db: character data, relationships, map tables
  - exports/vtt/{location_id}_*.json: existing VTT scene exports (Cartographer output)
  - audio/output/images/portrait/{char}.png: character portraits
  - data/worlds/{world_id}/seasons/.../S{S}E{E:02d}.json: episode JSON

Produces:
  exports/vtt_modules/S{S}E{E:02d}_module/
    ├── module.json              Module manifest
    ├── characters/              NPC stat blocks (ACES format JSON)
    ├── tokens/                  Circular character token PNGs
    ├── scenes/                  Enhanced VTT scene JSONs (with NPC positions)
    ├── encounter.json           Encounter table with positions + loot
    ├── product_metadata.json    DriveThruRPG / itch.io listing metadata
    └── {location_id}_bundle.zip  Original VTT bundle (re-included)

The stat blocks are derived deterministically from CharacterIdentity data —
no LLM call needed for stat generation. LLM is only used for encounter briefs
and loot table flavour text (optional; set stub=True to skip).

DriveThruRPG upload: requires publisher account setup + manual submission.
itch.io upload: use butler CLI: `butler push . user/game:vtt --userversion X.Y`

## Defined here

### `GameDesignistReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `season` | `int` |
| `episode` | `int` |
| `module_dir` | `Optional[Path]` |
| `characters_processed` | `int` |
| `tokens_generated` | `int` |
| `scenes_packaged` | `int` |
| `encounter_generated` | `bool` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `GameDesignist`

Produces VTT module packages from episode assets.

Parameters
----------
world_ledger_path:
    Path to the world_ledger.db for the target world.
data_dir:
    Path to data/worlds/ root.
images_dir:
    Path to audio/output/images/ (where character portraits live).
vtt_dir:
    Path to exports/vtt/ (Cartographer VTT bundle outputs).
modules_dir:
    Output root for VTT modules. Defaults to exports/vtt_modules/.
llm_router:
    Optional LLMRouter for encounter brief generation. If None,
    loot and briefs are generated from templates without LLM.
stub:
    If True, skip LLM calls and PIL image processing.

## Top-level functions

- **`main()`** — 
