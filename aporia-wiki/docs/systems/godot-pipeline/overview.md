# godot-pipeline

Offline animation pipeline for Aporia Phonetic Group / The Heterodyne.
Renders 2D sprite-on-map scenes to MP4 using Godot 4's Movie Maker mode:

- Cliffhanger presentation clips (60–90s) at Patreon branching votes
- Resolution animations (30–60s) at episode opens
- TikTok/Reels social clips (9:16) from emotional peak moments
- CYOA decision node animations for the
  [auralbouros](../auralbouros/cyoa-engine.md) app

## Status: parked

**🟡 Back burner** — explicitly parked until after The Heterodyne + FIND +
Auralbouros "launch trio" ships. Per the repo's own `STATUS.md`: *"Do not
touch until launch trio ships. If you find yourself working on GODOT, ask
why — it's almost always avoidance of something harder on the critical
path."*

Progress so far: project scaffold, a full B1/B2/B3 implementation plan,
and B2 Track 0 (schema reconciliation) — the
[compositor](compositor/episode-to-scene.md) is reconciled to the live
heterodyne episode schema. Rendering plumbing (Track A) and sprite/art
assets (Track B) are not started.

## Structure

| Path | Purpose |
|---|---|
| `project/` | Godot 4 project files |
| `assets/sprites/` | Character sprite sheets (pose sets per character) |
| `assets/scene_templates/` | Godot scene templates per map type |
| `assets/loras/` | Channel-specific LoRA weights (not in repo) |
| [`compositor/`](compositor/index.md) | Python: heterodyne episode JSON → Godot scene file |
| `out/` | Rendered MP4 output (gitignored, regenerable) |
