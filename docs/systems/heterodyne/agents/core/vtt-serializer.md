# vtt_serializer

*Source: `heterodyne/agents/vtt_serializer.py`*

VTT serializers — translate persisted maps to external VTT platforms.

Foundry VTT is the primary target (Map §7.3); Roll20 and Owlbear Rodeo are also
supported. All three resolve doors from map_connections (walls themselves are
all 'solid'). render_svg() produces a preview/background image reusing the same
cell→pixel transform, and package_vtt_bundle() zips a shippable module
(scene JSON + SVG + optional rules card).

## Top-level functions

- **`wall_segment_to_pixel_line()`** — Map a (cell, edge) wall to a pair of pixel endpoints (Map §7.2).
- **`serialize_foundry()`** — Produce a Foundry VTT scene dict for one persisted map (Map §7.3).
- **`package_foundry_adventure()`** — Bundle multiple scenes into a ``.fvttadventure`` zip (Map §7.3).
- **`serialize_roll20()`** — Produce a Roll20 Dungeon Importer dict (Map §7.4).
- **`serialize_owlbear()`** — Owlbear Rodeo scene metadata + wall/door line geometry.
- **`render_svg()`** — Render a map to a standalone SVG string (floor cells, walls, doors).
- **`package_vtt_bundle()`** — Zip one map's VTT export with an SVG preview and optional rules card.
