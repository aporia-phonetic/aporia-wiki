# manifest_generator

*Source: `heterodyne/agents/manifest_generator.py`*

agents/manifest_generator.py

Pre-Generated Resolution Manifest for the A.C.E.S. card system.

Generates resolution outcome tables for all possible card draws against
all character × action-type combinations, storing them as JSON manifests
on disk. The ACES Resolver reads from these manifests at runtime without
making any API calls, keeping live sessions fast and deterministic.

A manifest covers one character × one resolution domain. Pre-generating
before a session means every possible draw already has a rich narrative
outcome ready.

Card deck model:
  Ranks: A 2 3 4 5 6 7 8 9 10 J Q K (per suit)
  Suits: Spades ♠ / Hearts ♥ / Diamonds ♦ / Clubs ♣
  Special: Joker (Red / Black)

Resolution domains (action types):
  ATHLETICS  — physical feats, combat, endurance
  CUNNING    — deception, investigation, stealth, survival
  ELOQUENCE  — persuasion, performance, intimidation, social
  STRANGE    — resonance/magic, perception, intuition, the weird

Outcome tiers (mapped from card rank vs. character stat):
  CRITICAL_SUCCESS  — Ace when stat ≥ 4, or suit matches character suit
  SUCCESS           — Card rank ≤ stat × 2.5 (roughly)
  PARTIAL           — Card rank within 2 of threshold
  FAILURE           — Card rank > threshold
  COMPLICATION      — Face cards (J Q K) always add a complication
  WILD              — Joker: narrative wildcard, showrunner chooses

Usage:
    from agents.manifest_generator import ManifestGenerator

    gen = ManifestGenerator(api_key=..., output_dir="data/aces_manifests/")
    gen.generate_character_manifest(character_sheet, world_id="verdant_deep")
    gen.generate_all_manifests(cast, world_id="verdant_deep")

## Defined here

### `OutcomeTier`

### `ResolutionDomain`

### `ManifestGenerator`

Generates and saves A.C.E.S. resolution manifests for a character.

Parameters
----------
output_dir:
    Directory where JSON manifest files are written.
    Files are named: {world_id}_{character_name_slug}_{domain}.json
api_key:
    Anthropic API key. None = use ANTHROPIC_API_KEY environment variable.
model:
    Claude model for narrative outcome text generation.
    Default: claude-haiku-4-5-20251001 (fast, cheap for tabular generation).
use_prompt_caching:
    Cache the static system prompt block.

## Top-level functions

- **`rank_value()`** — Numeric value of a rank for threshold comparison (Ace = 1 or 14).
- **`is_face_card()`** — 
- **`calculate_outcome_tier()`** — Determine the mechanical outcome tier for a draw.
- **`lookup_outcome()`** — Look up one entry from a loaded manifest dict.
