# bloodkeeper

*Source: `heterodyne/agents/bloodkeeper.py`*

agents/bloodkeeper.py — The Bloodkeeper (Agent 24)

Genealogy visualization, bloodline sponsorship, and dynasty legacy documents.

Reads from:
  data/worlds/{world_id}/world_ledger.json   FamilyRelationship records
  data/sponsorships/registry.json            Sponsor registry (separate from narrative DB)

Outputs (caller passes output_dir=schemas.paths.output_type_dir("bloodkeeper", world_id) — whole-show, no season):
  {output_dir}/lineage.svg          Genealogy tree SVG
  {output_dir}/lineage.pdf          Printable tree PDF
  {output_dir}/dynasty_{char}.pdf   Patron dynasty legacy PDF
  {output_dir}/sponsors.json        Sponsor registry snapshot

Sponsorship note:
  Sponsors do NOT acquire IP rights. They fund a character lineage in the narrative.
  A sponsor agreement must be signed before activating a sponsorship product.
  See docs: BLOODKEEPER_SPONSOR_TOS.md (must be created before monetization launch).

Dependencies:
  networkx        pip install networkx
  fpdf2           pip install fpdf2
  (graphviz optional — falls back to pure networkx layout if not present)

## Defined here

### `SponsorRecord`

| Field | Type |
|---|---|
| `sponsor_id` | `str` |
| `patron_name` | `str` |
| `character_id` | `str` |
| `character_name` | `str` |
| `world_id` | `str` |
| `tier` | `str` |
| `active` | `bool` |
| `since_episode` | `int` |
| `notes` | `str` |
| `registered_at` | `str` |

### `BloodkeeperReport`

| Field | Type |
|---|---|
| `world_id` | `str` |
| `characters_mapped` | `int` |
| `relationships_mapped` | `int` |
| `sponsors_processed` | `int` |
| `output_paths` | `dict[str, str]` |
| `warnings` | `list[str]` |
| `error` | `str` |
| `started_at` | `datetime` |
| `completed_at` | `Optional[datetime]` |

### `Bloodkeeper`

Genealogy tracker and dynasty document generator.

Parameters
----------
data_dir:
    Path to data/worlds/ root.
sponsorship_dir:
    Directory holding the sponsor registry JSON. Defaults to data/sponsorships/.
output_dir:
    Base output directory. Bloodkeeper files go to {output_dir}/bloodkeeper/.
stub:
    If True, skip LLM calls (dynasty narrative text will be placeholder).
llm_router:
    Optional LLMRouter for dynasty narrative generation. None → build default.

## Top-level functions

- **`main()`** — 
