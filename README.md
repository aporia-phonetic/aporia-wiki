# aporia-wiki

Cross-referenced wiki for Aporia Phonetic Group: the four systems
(heterodyne, auralbouros, godot-pipeline, find) and the worlds,
characters, and seasons heterodyne produces. Built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and
deployed to GitHub Pages on push to `main`.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

## Regenerating reference pages

Pages under `docs/systems/*/agents/`, `docs/systems/*/schemas/`,
`docs/worlds/`, `docs/characters/`, and `docs/seasons/` are generated,
not hand-written — see
[`docs/reference/update-agent.md`](docs/reference/update-agent.md) for
how and why. To regenerate locally (requires the four source repos
cloned as siblings — see `SOURCES` in the script):

```bash
python3 scripts/generate_reference.py
```

## Structure

See [`docs/index.md`](docs/index.md) for the wiki's own landing page and
navigation overview.
