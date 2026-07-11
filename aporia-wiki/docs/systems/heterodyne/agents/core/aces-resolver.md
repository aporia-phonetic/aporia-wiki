# aces_resolver

*Source: `heterodyne/agents/aces_resolver.py`*

agents/aces_resolver.py

A.C.E.S. Resolution Layer for the Aeon Pulp Drama Engine.

Replaces the prior D&D-skeleton resolution system with a playing-card-draw
mechanic that integrates with character sheets, the World Ledger, and the
Pre-Generated Resolution Manifest system.

Card draw → outcome lookup → narrative → optional World Ledger update.

Resolution model:
  - A deck is maintained per session (Deck instance, 52 + 2 Jokers = 54 cards)
  - On each resolution attempt, the top card is drawn
  - The drawn card + character stat + domain → outcome tier
  - The tier + suit + rank → manifest narrative lookup (no API call at runtime)
  - The Archivist can commit the resolution result to the World Ledger

Outcome tiers:
  CRITICAL_SUCCESS  — Ace in affinity domain, or Ace with stat ≥ 4
  SUCCESS           — Rank within comfortable threshold of stat
  PARTIAL           — Partial success: goal achieved, but with cost or limit
  FAILURE           — Goal not achieved; consequence applied
  COMPLICATION      — Face card modifier: adds a twist on top of tier
  WILD              — Joker: narrative wildcard

Integration:
    from agents.aces_resolver import AcesResolver, ResolutionContext
    from agents.manifest_generator import ManifestGenerator

    gen = ManifestGenerator(output_dir="data/aces_manifests/")
    resolver = AcesResolver(manifest_dir="data/aces_manifests/")

    ctx = ResolutionContext(
        character_name="Maren Voss",
        domain="cunning",
        action_description="Pick the lock on the vault door.",
        world_id="verdant_deep",
    )
    result = resolver.resolve(ctx)
    print(result.narrative)
    print(result.tier)

## Defined here

### `Deck`

A standard 54-card deck (52 + 2 Jokers) with draw and reshuffle.

Cards are represented as (rank, suit) tuples.
Jokers are ("joker_red", "—") and ("joker_black", "—").

### `ResolutionContext`

Input parameters for a single resolution attempt.

| Field | Type |
|---|---|
| `character_name` | `str` |
| `domain` | `str` |
| `action_description` | `str` |
| `world_id` | `str` |
| `stat_override` | `Optional[int]` |
| `force_draw` | `Optional[tuple[str, str]]` |

### `ResolutionResult`

Output of a single resolution attempt.

| Field | Type |
|---|---|
| `character_name` | `str` |
| `domain` | `str` |
| `action_description` | `str` |
| `rank` | `str` |
| `suit` | `str` |
| `tier` | `str` |
| `has_complication` | `bool` |
| `narrative` | `str` |
| `stat_value` | `int` |
| `from_manifest` | `bool` |
| `ledger_update_hint` | `str` |

### `AcesResolver`

Resolves A.C.E.S. card draws against character manifests.

Parameters
----------
manifest_dir:
    Directory containing pre-generated manifest JSON files.
    Files are named: {world_id}_{character_name_slug}_{domain}.json
deck:
    Deck instance to draw from. If None, creates a fresh shuffled deck.
