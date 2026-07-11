# foley_taxonomy

*Source: `heterodyne/schemas/foley_taxonomy.py`*

schemas.foley_taxonomy — CLAP prompt vocabulary for zero-shot foley sorting.

The ingest agent classifies each wav by embedding it with CLAP and comparing
against the text embeddings of these prompts. CLAP responds far better to
descriptive natural-language sentences ("the sound of footsteps on stone")
than to bare labels ("footsteps"), so every family carries several phrasings
and the best-scoring family wins.

FAMILY_PROMPTS keys are the 21 FoleyFamily values from schemas.foley_catalog;
keeping them in lockstep is asserted by
tests/test_foley_ingest.py::test_family_prompts_cover_every_family.

TAG_VOCAB is a flat descriptor vocabulary scored independently — the top few
above a threshold become the entry's tags, which still feed the keyword
component of matching (semantic search via CLAP is primary, tags are backup).
