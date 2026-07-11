# CYOA engine

`src/engine/cyoa.ts` + `CYOAScreen`. A `CYOATree` is a graph of
`CYOANode`s with `CYOAChoice`s; choices can fire an `acesCheck` that
routes to a success/fail node using the player character's
[A.C.E.S.](game-systems.md#aces-adaptive-card-engine-system) stat in the
named domain.

Runtime save state (`CYOASave`, persisted to AsyncStorage) tracks:

- `currentNodeId`, `history`
- `hp` (default 3), `plotArmor` (default/max 2)
- `strangeSurgeFired`, `spentItems`

Mechanics: `applyDamage` (armor absorbs first, then HP; HP floors at 0 →
incapacitated node), `spendArmorForEcho` (spend a Plot Armor pip to
"ECHO" a catastrophe result), `applyStrangeSurge`.

Ships a built-in `STUB_TREE` ("A Signal from the Deep," S1E1) with a
Strange-gated hidden branch — this is placeholder content pending real
per-episode CYOA trees generated from heterodyne's episode output (see
[godot-pipeline](../godot-pipeline/overview.md), which already
references "CYOA decision node animations for the Auralbouros app" as a
downstream consumer of the same episode data).

## Season voting

`VoteScreen` + `src/services/votes.ts`. If `voteApiUrl` is configured,
ballots POST to `/api/votes/{season}/{episode}`; otherwise votes are
recorded locally. Results release one week after the season finale.
