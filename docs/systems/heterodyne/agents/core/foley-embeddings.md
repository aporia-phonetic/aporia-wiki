# foley_embeddings

*Source: `heterodyne/agents/foley_embeddings.py`*

agents.foley_embeddings — CLAP semantic index for the foley catalog.

This is the piece that fixes "couldn't find sounds by searching." The old
Foley Master matched intent text against entry tags with substring overlap,
so `"icy exhale of a collapsing vault"` never found a clip tagged
`cold, whoosh`. CLAP (Contrastive Language-Audio Pretraining) embeds audio
and text into the same vector space, so semantically-similar text and audio
land near each other and cosine similarity just works.

Two responsibilities:

  1. ClapEncoder — a lazy singleton wrapping `laion/clap-htsat-unfused` via
     HuggingFace transformers (already a project dependency; no new package).
     embed_audio() for ingest, embed_text() for query time. All vectors are
     L2-normalized so dot product == cosine similarity.

  2. EmbeddingStore — a sidecar SQLite table (catalog_embeddings) keyed by
     catalog_id. Kept OUT of the CatalogEntry pydantic model on purpose: an
     embedding is an index artifact, not catalog semantics, and the existing
     63 entries must stay valid. load_matrix() returns a stacked matrix for
     fast batched cosine search.

Everything degrades gracefully: if torch/transformers can't load (or the
model can't be downloaded), is_clap_available() returns False and callers
fall back to keyword matching. The catalog never breaks because CLAP is
missing.

## Defined here

### `ClapEncoder`

Wraps a CLAP model for audio/text embedding. Load is deferred to
first use so importing this module is cheap and side-effect free.

| Field | Type |
|---|---|
| `_instance` | `'ClapEncoder | None'` |

### `EmbeddingStore`

SQLite-backed store of per-entry CLAP vectors.

Lives in the same database file as the catalog (default) so the index
travels with the catalog, but in its own table — the CatalogEntry model
is untouched.

## Top-level functions

- **`is_clap_available()`** — True if the CLAP stack can be imported (model download is separate).
- **`cosine_search()`** — Rank ids by cosine similarity to query_vec. Inputs are assumed
