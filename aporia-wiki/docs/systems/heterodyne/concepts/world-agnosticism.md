# World-agnostic engine code

heterodyne is built to run *any* world — genre, era, cast, setting — off
the same engine code. The rule, enforced in the repo's own `CLAUDE.md`:

> `agents/*.py`, `schemas/*.py`, `config/*`, and `main.py` must never
> encode assumptions — genre, era, setting, tone, character names, place
> names — from whichever world happens to be in active production
> (`caelum_reach` today; `verdant_deep` before it; something else next).
> That includes assumptions baked into comments/docstrings used to
> justify code behavior, not just literal strings.

World-specific content belongs in `data/worlds/{world_id}/*` or
`Worlds/*.md`, and reaches engine code only as data/parameters passed in
at runtime — never as hardcoded literals, `Literal`/enum values, or
"this is fine because our current world is X" comments.

The test the repo's own docs suggest: **would this line still make sense
if the active world were a completely different genre and era?**

## Bugs of this shape, fixed once already

These are the concrete violations the engine team caught and corrected —
worth knowing so the same shape doesn't get reintroduced:

- `schemas/foley_filename.py` classified sci-fi/UI sound keywords as
  generic "cruft that doesn't fit the setting," because the prototype
  world was 1930s-adjacent.
- `scripts/ingest_sfx.py` sent the ingest LLM a system prompt hardcoded
  to "pulp adventure radio drama."
- `agents/scene_context.py` had Caelum Reach's location gazetteer as a
  Python literal, with every other world's locations mislabeled "A
  location in Caelum Reach" by the fallback path.
- `main.py`/`agents/dramatist.py` defaulted the active world to
  `"verdant_deep"` in ~20 separate places instead of one shared helper —
  see [`resolve_world_id`](cli-and-routing.md#resolve_world_id).

## Why this matters for the wiki too

The same discipline applies to how this wiki is generated: the reference
generator (`scripts/generate_reference.py`) reads whatever docstrings and
data files the source repos currently contain — it holds no world's
content in the generator logic itself. See
[reference/update-agent.md](../../../reference/update-agent.md).
