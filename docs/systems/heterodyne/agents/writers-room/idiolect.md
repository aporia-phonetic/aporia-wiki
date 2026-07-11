# idiolect

*Source: `heterodyne/agents/writers_room/idiolect.py`*

agents/writers_room/idiolect.py

Idiolect cards + continuity retrieval, both built from the same corpus:
the committed episode JSONs (the shape run_episode writes).

Idiolect cards make voice distinctness data-driven: per-character cadence
stats, favorite openers, and catchphrase usage counts from accumulated past
dialogue. Mannerism exhaustion becomes measurable — "used 'partner' 9x in
the last 3 episodes; rest it."

Continuity retrieval surfaces the few most relevant past moments for the
scene being written, so callbacks are concrete quotable beats instead of a
summary digest. Scoring is lexical-overlap (dependency-free); it degrades
to nothing gracefully when no past episodes exist.

## Top-level functions

- **`load_episode_corpus()`** — Flatten recent episode JSONs into [{episode, character, type, text}].
- **`build_idiolect_card()`** — One character's measured style card, or '' when no history exists.
- **`build_idiolect_cards()`** — Joined cards for the scene writer / intention prompts. '' if none.
- **`retrieve_moments()`** — Top-k past lines most lexically relevant to the query (scene
- **`format_moments_for_prompt()`** — MOMENTS YOU MAY CALL BACK TO block; '' when nothing retrieved.
