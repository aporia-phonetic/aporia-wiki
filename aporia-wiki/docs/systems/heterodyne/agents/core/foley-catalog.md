# foley_catalog

*Source: `heterodyne/agents/foley_catalog.py`*

agents.foley_catalog — SQLite persistence layer for the foley catalog.

Owns:
  • The schema for the catalog database (foley_catalog.db)
  • CRUD operations for CatalogEntry rows
  • Query / match logic that the Foley Master agent (Phase 3.7) consumes
  • Stats reporting for tools and CLI

Lifecycle:
  • init_db() creates the schema if missing
  • bootstrap_legacy_stubs() seeds the catalog from LEGACY_LEXICON_MIGRATION
    on first run so existing E1-E4 episodes don't break
  • register() inserts a new CatalogEntry (called by Foley Sourcer)
  • find_matches() returns ranked CatalogMatch candidates for a query
  • get_by_id() / get_stats() for tools and audit

The catalog is append-only in normal operation. Entries can be replaced
via update_file_path (when a stub gets sourced) but never deleted by
agents — only by manual operator action via the CLI.

Stub policy:
  When the Foley Sourcer is disabled (FOLEY_SOURCING_ENABLED=false in .env),
  unsourced entries remain as 'stub' rows pointing to a placeholder file.
  The Mixer can render against stubs (silence or distinct noise) for
  development. When sourcing turns on, stubs get replaced atomically:
  same catalog_id, new file_path, source updated from 'stub' to whatever
  backend provided the audio.

## Defined here

### `CatalogError`

Base class for catalog failures.

### `CatalogNotFoundError`

No entry with the requested catalog_id.

### `CatalogConflictError`

Insertion violates a uniqueness constraint.

### `FoleyCatalog`

SQLite-backed catalog of atomic foley sounds.

Single instance per process. Threadsafe via per-call connections; the
Foley Master and Sourcer agents do not share connection objects.

Parameters
----------
db_path : str | Path
    Path to the SQLite file. Created on first use.
catalog_root : str | Path
    Directory under which file_path values resolve. Convention is
    `<project_root>/audio/foley_catalog/`. Mixer joins
    catalog_root with entry.file_path to find the WAV.
