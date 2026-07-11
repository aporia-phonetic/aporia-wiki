# Lore feed integration

`WorldScreen` (the in-app "World archive") is a searchable/filterable
list backed by `fetchLore(loreUrl)`, falling back to a `STUB_LORE`
constant when no feed URL is configured. Data shapes are defined in
`src/services/lore.ts`: `CharacterBio`, `WorldBio`, `EpisodeSummary`,
`NarrativeState`, `LorePayload`.

Sections and their detail screens:

- **Characters** → `CharacterDetailScreen` — portrait, role,
  affinity/tags, bio, plus optional extended dossier fields
  (`threatLevel`, `lastTransmission`, `relationships`, `rumors`,
  `leitmotifFragmentUrl`) rendered only when present.
- **Worlds & Factions** → `WorldDetailScreen`.
- **Episode Index** → `EpisodeLoreScreen`.
- **Narrative Arc** → `NarrativeDetailScreen` (Story Circle step,
  protagonist focus, Ghost Signal status).

## Relationship to heterodyne's lore export

heterodyne's `scripts/export_lore.py` builds
`exports/lore/lore_export.json` — a cross-repo data feed described in
`heterodyne/LORE_EXPORT.md`, and confirmed (by `find`'s own roadmap
notes) to feed an `/api/lore` endpoint. This is very likely the same
feed shape `fetchLore()` expects, making auralbouros the presentation
layer for heterodyne's world/character/episode data — though this
hasn't been directly confirmed against a live `loreUrl` config, since
auralbouros ships with `STUB_LORE` as its default and the feed URL is
environment-configured rather than committed to the repo. Worth
verifying end-to-end (point a dev build's `loreUrl` at a real
`lore_export.json` and confirm the shapes line up) before treating this
as settled.
