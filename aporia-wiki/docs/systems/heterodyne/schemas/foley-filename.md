# foley_filename

*Source: `heterodyne/schemas/foley_filename.py`*

schemas.foley_filename — filename-aware classification for foley ingest.

The user's library uses richly descriptive, structured filenames
(`alarm_siren_loop_03`, `gun_machinegun_auto_heavy_shot_04`,
`troll_monster_growl_long_11`, `footstep_gravel_run_02`). That text is
author-supplied ground truth — far more reliable for sorting than what CLAP
can infer from audio alone. CLAP classification of these clips wandered and
scored low (identical sirens scattered across three families at 0.1-0.4), and
because `find_matches` HARD-filters on family, a misclassified clip becomes
unfindable. So we mine the filename.

`classify_filename(stem)` tokenizes the name and returns:
  - family_scores: {FoleyFamily: weight}  (empty if no keyword matched)
  - tags: descriptor tokens worth surfacing for keyword search

The ingestor blends family_scores with the CLAP per-family score, so the name
decides when it has a confident hit and CLAP carries ambiguous/empty names.

Two keyword tiers:
  STRONG (weight 3) — subject/action words that pin a family (footstep, gun,
    goblin, spell, door, water...).
  WEAK   (weight 1) — material/context words that only nudge a family AND also
    become tags (metal, wood, gravel...).

Everything maps to one of the FoleyFamily values. Combat content is
first-class as "weapon" — firearms, blades, explosives, melee, and energy
weapons alike, for any world with conflict. Interface/UI/notification sounds
(menu blips, beeps, confirmation chimes) are first-class as "interface", for
any world with diegetic tech or a game-like HUD. Tokens that don't cleanly fit
an established family (robot/droid vocals, generic electric/glitch, ambiguous
alarms) fall through to `special` — a genuine miscellaneous catch-all, not a
genre-exclusion bucket — tagged precisely so semantic + keyword search still
find them.

## Top-level functions

- **`tokenize()`** — Filename stem -> lowercase tokens, digits and 1-char fragments dropped.
- **`classify_filename()`** — Return (family_scores, tags) mined from a filename stem.
