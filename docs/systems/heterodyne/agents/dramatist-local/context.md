# context

*Source: `heterodyne/agents/dramatist_local/context.py`*

agents.dramatist_local.context — runtime context assembly for the local pipeline.

Builds the world/season/cast context blocks that get appended to every
stage's system prompt. This is the world-fidelity guard: the plain-prose
system prompt is short, so these data-driven blocks dominate the writer's
context (world facts arrive as data, never as engine literals).

The world-config / sourcebook / roster / crossover injection mirrors
Dramatist.generate_episode (agents/dramatist.py) — duplicated here because
that logic is interleaved with instance state in a module we deliberately
do not modify. The episode-config directives (narrator mode/perspective,
POV, content controls) are NOT duplicated: we reuse Dramatist.__init__'s
own construction and slice off what it appended.

## Top-level functions

- **`build_craft_addendum()`** — Craft rules every writing stage needs, plus the AI-tell lexicon.
- **`load_local_prompts()`** — Load the local-pipeline prompt pack. Missing files fail loudly.
- **`episode_directives()`** — Reuse the cloud Dramatist's episode-config directive construction.
- **`build_crossover_context()`** — Prior crossover records, mirroring generate_episode's injection.
- **`build_world_context()`** — World identity + magic + tone from world_config.json (authoritative).
- **`build_sourcebook_context()`** — Season sourcebook (preferred) or whole-world chronicle digest.
- **`build_roster_context()`** — Cast roster block (status, species, appearance, catchphrases).
- **`build_voice_context()`** — Vocal-personality guidance for the whole active cast.
- **`build_orientation_context()`** — Which characters debut this episode, and whether it opens a series/season.
- **`orientation_opening_beat()`** — A synthetic first beat that forces the writer to open by orienting the
- **`build_full_context()`** — Assemble every context block for the writer/beat/judge system prompts.
