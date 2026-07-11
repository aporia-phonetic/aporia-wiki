# Glossary

heterodyne already has a thorough 50+ term glossary in
`documents/USER MANUAL/AEON_PULP_DRAMA_ENGINE_USER_MANUAL.md` §32
(Archivist, Dramatist, World Ledger, Plot Gate, Voice Seed, and the rest
of the engine's internal vocabulary) — that stays canonical, this page
doesn't duplicate it. Below are terms that either span multiple systems
or aren't in that list.

**A.C.E.S. (channel)** — heterodyne's ACES distribution channel *and*
auralbouros's `src/engine/aces.ts` card-resolution engine (Rev 3,
"Universal 21") are the same branded game system wearing two hats: one
as a content-structuring channel preset in the engine, one as a playable
card game in the app. See
[Game systems](../systems/auralbouros/game-systems.md).

**Aporia Phonetic Group** — the parent company/LLC. "The launch trio"
refers to heterodyne + find + auralbouros; godot-pipeline is a parked
fourth piece.

**Company Ledger** — find's single-writer, HMAC-audited SQLite store of
business state (finance, contracts, customers). Not to be confused with
heterodyne's **World Ledger** (narrative state) — same word, unrelated
systems.

**CYOA** — Choose-Your-Own-Adventure. Both an in-app auralbouros feature
([CYOA engine](../systems/auralbouros/cyoa-engine.md)) and a planned
godot-pipeline render target ("CYOA decision node animations").

**Decision Queue** — find's mechanism for surfacing agent proposals to
the founder for approval; agents never act directly. See
[Decision Queue](../systems/find/decision-queue.md).

**Launch trio** — heterodyne + find + auralbouros, the three systems
targeted to ship together; godot-pipeline is explicitly parked until
after they ship.

**Lore export** — `heterodyne/scripts/export_lore.py`'s
`exports/lore/lore_export.json`, the cross-repo feed that likely backs
auralbouros's in-app lore archive. See
[Lore feed integration](../systems/auralbouros/lore-feed-integration.md).

**Sideris Narrative Systems** — the public/in-fiction brand name for the
story universe heterodyne generates and auralbouros presents.

**Steward** — find's single writer to the Company Ledger; all agents
read via `LedgerSnapshot` instead of writing directly.

**World Ledger** — heterodyne's persistent per-world narrative state
(knowledge, trust, emotion, location, callbacks...). See
[World Ledger & Plot Gates](../systems/heterodyne/concepts/world-ledger-and-plot-gates.md).
Not to be confused with find's unrelated **Company Ledger**.
