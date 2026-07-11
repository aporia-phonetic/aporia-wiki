#!/usr/bin/env python3
"""Generate wiki reference pages from source repos.

Reads module docstrings and top-level class/function signatures directly
out of the source .py files (via `ast`, never executed/imported) and data
files (world_config.json, character identity.json/appearances.json) and
renders one markdown page per entity. Re-running this script regenerates
these pages from whatever the source repos currently contain — it holds no
world/character/system-specific content of its own, only path lists passed
in via SOURCES below and the JSON/docstrings it reads at runtime.

This is the mechanical half of keeping the wiki current; the wiki-update
Routine re-runs this script and diffs the output. Hand-authored pages
(overviews, concepts, glossary) are not touched by this script.
"""
from __future__ import annotations

import ast
import json
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"

# Where the four source repos live in this environment. The update Routine
# will set these to fresh clones; nothing below is world/system-specific.
SOURCES = {
    "heterodyne": Path("/home/user/heterodyne"),
    "auralbouros": Path("/home/user/auralbouros"),
    "godot-pipeline": Path("/home/user/godot-pipeline"),
    "find": Path("/home/user/find"),
}


@dataclass
class ModuleDoc:
    module_path: Path
    docstring: str | None
    classes: list[tuple[str, str | None, list[str]]]  # name, docstring, field lines
    functions: list[tuple[str, str | None]]


def parse_module(path: Path) -> ModuleDoc:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    docstring = ast.get_docstring(tree)
    classes = []
    functions = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            cls_doc = ast.get_docstring(node)
            fields = []
            for item in node.body:
                if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                    try:
                        type_str = ast.unparse(item.annotation)
                    except Exception:
                        type_str = "?"
                    fields.append(f"{item.target.id}: {type_str}")
            classes.append((node.name, cls_doc, fields))
        elif isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            functions.append((node.name, ast.get_docstring(node)))
    return ModuleDoc(module_path=path, docstring=docstring, classes=classes, functions=functions)


def render_module_page(mod: ModuleDoc, repo_name: str, title: str) -> str:
    rel = mod.module_path
    lines = [f"# {title}", ""]
    lines.append(f"*Source: `{repo_name}/{rel}`*")
    lines.append("")
    if mod.docstring:
        lines.append(mod.docstring.strip())
        lines.append("")
    if mod.classes:
        lines.append("## Defined here")
        lines.append("")
        for name, doc, fields in mod.classes:
            lines.append(f"### `{name}`")
            if doc:
                lines.append("")
                lines.append(doc.strip())
            if fields:
                lines.append("")
                lines.append("| Field | Type |")
                lines.append("|---|---|")
                for f in fields:
                    fname, _, ftype = f.partition(": ")
                    lines.append(f"| `{fname}` | `{ftype}` |")
            lines.append("")
    if mod.functions:
        lines.append("## Top-level functions")
        lines.append("")
        for name, doc in mod.functions:
            first_line = (doc or "").strip().splitlines()[0] if doc else ""
            lines.append(f"- **`{name}()`** — {first_line}")
        lines.append("")
    return "\n".join(lines)


def slugify(stem: str) -> str:
    return stem.replace("_", "-")


def generate_module_group(
    src_dir: Path,
    repo_name: str,
    out_dir: Path,
    group_label: str,
    skip_names: set[str] = frozenset({"__init__"}),
) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for py_file in sorted(src_dir.glob("*.py")):
        if py_file.stem in skip_names:
            continue
        try:
            mod = parse_module(py_file)
        except SyntaxError:
            continue
        mod.module_path = py_file.relative_to(SOURCES[repo_name])
        title = py_file.stem
        page = render_module_page(mod, repo_name, title)
        out_file = out_dir / f"{slugify(py_file.stem)}.md"
        out_file.write_text(page, encoding="utf-8")
        written.append(out_file.name)
    write_index_page(out_dir, group_label, written)
    return written


def write_index_page(out_dir: Path, title: str, page_names: list[str]) -> None:
    lines = [f"# {title}", ""]
    for name in sorted(page_names):
        stem = name[:-3] if name.endswith(".md") else name
        lines.append(f"- [{stem}]({name})")
    (out_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_agent_pages() -> None:
    heterodyne = SOURCES["heterodyne"]
    base_out = DOCS / "systems/heterodyne/agents"
    generate_module_group(heterodyne / "agents", "heterodyne", base_out / "core", "Core Agents")
    generate_module_group(
        heterodyne / "agents/dramatist_local", "heterodyne", base_out / "dramatist-local", "Dramatist (Local LLM)"
    )
    generate_module_group(
        heterodyne / "agents/writers_room", "heterodyne", base_out / "writers-room", "Writers' Room"
    )


def generate_schema_pages() -> None:
    heterodyne = SOURCES["heterodyne"]
    generate_module_group(heterodyne / "schemas", "heterodyne", DOCS / "systems/heterodyne/schemas", "Schemas")


def generate_find_agent_pages() -> None:
    find_agents = SOURCES["find"] / "find" / "agents"
    if find_agents.exists():
        generate_module_group(
            find_agents, "find", DOCS / "systems/find/agents", "Ops Agents",
            skip_names={"__init__", "base", "stubs"},
        )


def generate_godot_pipeline_pages() -> None:
    compositor = SOURCES["godot-pipeline"] / "compositor"
    if compositor.exists():
        generate_module_group(compositor, "godot-pipeline", DOCS / "systems/godot-pipeline/compositor", "Compositor")


def generate_world_pages() -> None:
    worlds_dir = SOURCES["heterodyne"] / "data" / "worlds"
    out_dir = DOCS / "worlds"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for world_dir in sorted(worlds_dir.iterdir()):
        if not world_dir.is_dir():
            continue
        world_id = world_dir.name
        cfg_path = world_dir / "world_config.json"
        if not cfg_path.exists():
            continue
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        lines = [f"# {cfg.get('world_name', world_id)}", ""]
        lines.append(f"`world_id`: `{world_id}`")
        lines.append("")
        desc = cfg.get("description")
        if desc:
            lines.append(desc.strip())
            lines.append("")
        genre = cfg.get("genre_settings", {})
        if genre:
            lines.append("## Genre & tone")
            lines.append("")
            if genre.get("genre"):
                lines.append(f"- **Genre:** {genre['genre']}")
            for td in genre.get("tone_descriptors", []):
                lines.append(f"- {td}")
            lines.append("")

        seasons_dir = world_dir / "seasons"
        season_ids = sorted(p.name for p in seasons_dir.iterdir()) if seasons_dir.exists() else []
        has_sourcebook = (world_dir / "sourcebook.md").exists()

        lines.append("## Status")
        lines.append("")
        if season_ids:
            lines.append(f"- Seasons: {', '.join(f'[{s}](../seasons/{world_id}/{s}.md)' for s in season_ids)}")
        else:
            lines.append("- No seasons produced yet — config-only stub world.")
        if has_sourcebook:
            lines.append(f"- Full sourcebook: `heterodyne/data/worlds/{world_id}/sourcebook.md` (not mirrored here — see that file in the engine repo for the complete series bible)")
        lines.append("")

        chars_dir = SOURCES["heterodyne"] / "data" / "characters"
        appearing = []
        if chars_dir.exists():
            for char_dir in sorted(chars_dir.iterdir()):
                appearances_path = char_dir / "appearances.json"
                if not appearances_path.exists():
                    continue
                data = json.loads(appearances_path.read_text(encoding="utf-8"))
                for app in data.get("appearances", []):
                    if app.get("world_id") == world_id:
                        appearing.append(char_dir.name)
                        break
        if appearing:
            lines.append("## Characters")
            lines.append("")
            for c in appearing:
                lines.append(f"- [{c}](../characters/{c}.md)")
            lines.append("")

        (out_dir / f"{world_id}.md").write_text("\n".join(lines), encoding="utf-8")
        written.append(f"{world_id}.md")
    write_index_page(out_dir, "Worlds", written)


def generate_character_pages() -> None:
    chars_dir = SOURCES["heterodyne"] / "data" / "characters"
    out_dir = DOCS / "characters"
    out_dir.mkdir(parents=True, exist_ok=True)
    if not chars_dir.exists():
        return
    written = []
    for char_dir in sorted(chars_dir.iterdir()):
        identity_path = char_dir / "identity.json"
        if not identity_path.exists():
            continue
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
        appearances_path = char_dir / "appearances.json"
        appearances = []
        if appearances_path.exists():
            appearances = json.loads(appearances_path.read_text(encoding="utf-8")).get("appearances", [])

        lines = [f"# {identity.get('name', char_dir.name)}", ""]
        lines.append(f"`character_id`: `{char_dir.name}`")
        lines.append("")
        if identity.get("archetype"):
            lines.append(f"**Archetype:** {identity['archetype']}")
            lines.append("")
        if identity.get("species"):
            lines.append(f"**Species:** {identity['species']}")
        if identity.get("voice_description"):
            lines.append("")
            lines.append(f"> {identity['voice_description']}")
        if identity.get("flaw"):
            lines.append("")
            lines.append(f"**Flaw:** {identity['flaw']}")
        catchphrases = identity.get("catchphrases", [])
        if catchphrases:
            lines.append("")
            lines.append("**Catchphrases:**")
            for c in catchphrases:
                lines.append(f"- \"{c}\"")
        lines.append("")

        if appearances:
            lines.append("## Appearances")
            lines.append("")
            lines.append("| World | Season | Tier |")
            lines.append("|---|---|---|")
            for app in appearances:
                w = app.get("world_id", "?")
                s = app.get("season_number", "?")
                tier = app.get("tier", "?")
                lines.append(f"| [{w}](../worlds/{w}.md) | {s} | {tier} |")
            lines.append("")

        (out_dir / f"{char_dir.name}.md").write_text("\n".join(lines), encoding="utf-8")
        written.append(f"{char_dir.name}.md")
    write_index_page(out_dir, "Characters", written)


def generate_season_pages() -> None:
    worlds_dir = SOURCES["heterodyne"] / "data" / "worlds"
    out_dir = DOCS / "seasons"
    out_dir.mkdir(parents=True, exist_ok=True)
    world_links = []
    for world_dir in sorted(worlds_dir.iterdir()):
        world_id = world_dir.name
        seasons_dir = world_dir / "seasons"
        if not seasons_dir.exists():
            continue
        (out_dir / world_id).mkdir(parents=True, exist_ok=True)
        world_links.append(world_id)
        season_names = []
        for season_dir in sorted(seasons_dir.iterdir()):
            if not season_dir.is_dir():
                continue
            season_id = season_dir.name
            season_names.append(f"{season_id}.md")
            lines = [f"# {world_id} — {season_id}", ""]
            cfg_path = season_dir / "season_config.json"
            if cfg_path.exists():
                cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
                for k in ("logline", "theme", "episode_count"):
                    if cfg.get(k):
                        lines.append(f"**{k.replace('_', ' ').title()}:** {cfg[k]}")
                lines.append("")
            episodes_dir = season_dir / "episodes"
            if episodes_dir.exists():
                ep_ids = sorted({p.stem.split("_")[0] for p in episodes_dir.glob("*.json")})
                if ep_ids:
                    lines.append("## Episodes")
                    lines.append("")
                    for ep in ep_ids:
                        lines.append(f"- {ep}")
                    lines.append("")
            plot_gates_path = season_dir / "plot_gates.json"
            if plot_gates_path.exists():
                try:
                    gates = json.loads(plot_gates_path.read_text(encoding="utf-8"))
                    n = len(gates) if isinstance(gates, list) else len(gates.get("gates", []))
                    lines.append(f"Plot gates defined: {n}")
                    lines.append("")
                except Exception:
                    pass
            lines.append(f"Parent world: [{world_id}](../../worlds/{world_id}.md)")
            (out_dir / world_id / f"{season_id}.md").write_text("\n".join(lines), encoding="utf-8")
        write_index_page(out_dir / world_id, f"{world_id} — Seasons", season_names)
    (out_dir / "index.md").write_text(
        "# Seasons\n\n" + "\n".join(f"- [{w}]({w}/index.md)" for w in sorted(world_links)) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    generate_agent_pages()
    generate_schema_pages()
    generate_find_agent_pages()
    generate_godot_pipeline_pages()
    generate_world_pages()
    generate_character_pages()
    generate_season_pages()
    print("Reference pages generated.")


if __name__ == "__main__":
    main()
