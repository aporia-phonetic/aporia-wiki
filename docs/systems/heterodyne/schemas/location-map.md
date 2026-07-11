# location_map

*Source: `heterodyne/schemas/location_map.py`*

Location Map Schema

Defines the structure for tactical location maps used in AEON engine:
- MapRoom: Individual rooms/chambers defined by rectangles
- MapConnection: Connections between rooms via doors
- SpecialCell: Tagged cells with special properties
- LocationMap: Complete location map with rooms, connections, and special cells

Maps are generated via Cartographer agent and persisted in WorldLedger.LocationEntry.location_map

## Defined here

### `MapRoom`

A single room or chamber in a location map.

Rooms are represented as rectangles on a grid.
Multiple rooms with the same id are merged (allows creating L-shapes, T-shapes, etc.)

| Field | Type |
|---|---|
| `id` | `str` |
| `rect` | `tuple[int, int, int, int]` |
| `edge_style` | `Literal['clean', 'rough', 'chamfered', 'mixed']` |
| `label` | `str` |

### `MapConnection`

A connection (door) between two rooms.

Doors are placed on specific wall positions and can be open, locked, or secret.

| Field | Type |
|---|---|
| `from_room` | `str` |
| `from_wall` | `Literal['north', 'south', 'east', 'west']` |
| `from_position` | `int` |
| `to_room` | `str` |
| `to_wall` | `Literal['north', 'south', 'east', 'west']` |
| `to_position` | `int` |
| `door_type` | `Literal['open', 'door', 'locked_door', 'secret_door']` |

### `SpecialCell`

A cell with special properties (rubble, water, elevation, etc.).

| Field | Type |
|---|---|
| `x` | `int` |
| `y` | `int` |
| `tag` | `Literal['rubble', 'difficult', 'hazard', 'elevation', 'water']` |

### `LocationMap`

Complete tactical map for a single location.

Contains rooms, connections between rooms, and special cell markers.
Generated via Cartographer agent and validated via Parallax validators.

| Field | Type |
|---|---|
| `location_id` | `str` |
| `season` | `int` |
| `episode_first_appearance` | `int` |
| `rooms` | `list[MapRoom]` |
| `connections` | `list[MapConnection]` |
| `special_cells` | `list[SpecialCell]` |
