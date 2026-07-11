# auralbouros — Sideris Narrative Systems companion app

Internal slug `find-engine`, npm package `auralboros`. A React Native /
Expo (TypeScript) mobile app — the public-facing companion for the
*Sideris Narrative Systems* audio-fiction/TTRPG property, bundling:

- A **podcast player** loading episodes from a configurable RSS feed.
- A **lore archive** ("the World archive") loading characters,
  factions/worlds, an episode index, and a narrative-arc tracker from a
  configurable JSON feed — falls back to `STUB_LORE` stub data when
  unconfigured. This is very likely the presentation layer for the same
  story universe heterodyne generates, fed by
  [`heterodyne/scripts/export_lore.py`](../heterodyne/overview.md)'s
  `exports/lore/lore_export.json`.
- **Four original card-game systems** — A.C.E.S., E.C.H.O., H.E.R.O.,
  H.A.R.T. — with A.C.E.S. and E.C.H.O. fully playable in-app, the other
  two as in-app rules references.
- Tools: a procedural NPC & Scene generator, an A.C.E.S. character
  creator.
- An **interactive-fiction (CYOA) engine** with HP / Plot-Armor / damage
  mechanics tied to A.C.E.S. card draws.
- **Season voting**, recorded locally or POSTed to an "AOL" backend.
- **The Babyborous** — a hidden ambient creature that only appears after
  sustained multi-day engagement, then grows and occasionally surfaces
  gifts (a character's leitmotif, rare lore fragments).

**Tech stack:** Expo SDK ~54, React Native 0.81, React 19, TypeScript
(strict), zustand for state, `expo-av` for audio, `fast-xml-parser` for
RSS.

## Accuracy note worth knowing

The in-code A.C.E.S. engine (`src/engine/aces.ts`) is **Revision 3
("Universal 21")**, which differs from the older Revision 2 rules still
written in the repo's own `docs/AURALBOROS MANUAL.md`. Where they
conflict, the code (Rev 3) is authoritative.

## Existing docs (not mirrored here)

`docs/AURALBOROS MANUAL.md` (Rev 5, prose game-systems manual) and
`docs/AURALBOROS_UI_ELEMENT_REFERENCE.md` are the richest existing
reference material in this repo — this wiki links to them rather than
duplicating; see [ui-reference.md](ui-reference.md) and
[game-systems.md](game-systems.md) for the wiki-side summaries and
cross-links into worlds/characters.
