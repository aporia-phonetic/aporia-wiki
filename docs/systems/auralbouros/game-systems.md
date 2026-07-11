# Game systems — A.C.E.S., E.C.H.O., H.E.R.O., H.A.R.T.

Condensed from the app's own `docs/AURALBOUROS MANUAL.md` §3.3, cross-checked
against the shipping code — full detail lives there, this is the map.

## A.C.E.S. — Adaptive Card Engine System

`src/engine/aces.ts`, **Revision 3 "Universal 21."** The core
action-resolution engine — also powers the CYOA engine's skill checks.
Draw against a dealer's Tell (face up) + Truth (face down) sum; stat
(1–5) sets your max additional Hits; ceiling is a universal 21 for every
stat (no Floor rule, no PARTIAL tier in Rev 3). Outcomes: `CATASTROPHE`
(bust), `CRITICAL` (exact match or natural 21), `SUCCESS`, `FAILURE`.
Suits map to domains: ♠ athletics, ♣ cunning, ♦ eloquence, ♥ strange —
the same four domains used on [character ACES stat blocks](../../characters/index.md).

> **Doc/code divergence:** `docs/AURALBOUROS MANUAL.md` still documents
> Rev 2 (stat-scaled bust thresholds, a Floor rule, a PARTIAL outcome).
> The shipping engine is Rev 3. Trust the code over that doc.

## E.C.H.O. — solo horror card game

`src/engine/echo.ts`. Fully playable in-app. Deck-splits into
Narrative/Mind/Body decks plus an Entrance and two Stalker tokens;
players map corridors/rooms, then resolve Mind+Body draws against a
threshold each turn while Stalkers advance. Reaching the Exit wins;
being caught by a Stalker ends the run.

## H.E.R.O. and H.A.R.T.

Rules-reference only in-app (no interactive engine module — full rules
live in `docs/AURALBOUROS MANUAL.md`). H.E.R.O. is a "virtue pyramid"
over-arc system (Hope/Endure/Resolve/Oath, demand tiers, an Apex
Choice). H.A.R.T. is a two-player relational card game (Hold/Ask/
Reveal/Try, a Relationship Token).

## Tools

- **NPC & Scene generator** — genre-filtered procedural NPC/scene
  generation (genre affects the location pool only).
- **A.C.E.S. character creator** — full dossier builder; the first
  saved character becomes the CYOA player character.
