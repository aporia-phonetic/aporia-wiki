# map_geometry

*Source: `heterodyne/agents/map_geometry.py`*

Map Geometry — Geometric operations for tactical map processing.

Core functions:
- Cell expansion: Convert room rectangles to occupied cells
- Wall extraction: Derive walls from cell boundaries
- Door placement: Convert connection records into door wall segments
- Tile assignment: Derive per-cell tile_type from edge_style
- Connectivity validation: Verify floor cells are all reachable
- Overlap detection: Ensure rooms don't overlap

## Top-level functions

- **`expand_rooms_to_cells()`** — Expand room rectangles into sets of occupied cells.
- **`get_room_walls()`** — Get wall boundaries for a room.
- **`get_wall_length()`** — Get the usable length of a wall.
- **`validate_door_position()`** — Validate that a door position is within wall bounds.
- **`check_room_overlap()`** — Check for overlapping room interiors.
- **`get_wall_cells()`** — Get all cells on a specific wall of a room.
- **`get_door_cell()`** — Get the cell coordinate for a door position on a wall.
- **`get_opposite_wall()`** — Get the opposite wall direction.
- **`extract_walls()`** — Derive wall segments from the set of floor cells.
- **`place_doors()`** — Replace solid wall segments with the appropriate door type per connection.
- **`assign_tile_types()`** — Derive per-cell tile_type for a room from its edge_style.
- **`validate_connectivity()`** — BFS flood fill from entrance. Reports unreachable cells.
- **`validate_map_geometry()`** — Comprehensive geometric validation of a location map.
