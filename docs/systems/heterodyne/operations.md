# Operations

Runbooks live in the heterodyne repo root; this page is a pointer/index
so they're discoverable from the wiki, not a copy (they change with the
hardware/setup, and duplicating them here would just drift).

| Runbook | Covers |
|---|---|
| `COLD_START.md` | Minimum steps from a bare Linux machine (dual RTX 3090s) to a working episode render — quick-reference card |
| `HARDWARE_MIGRATION_GUIDE.md` | Full move from cloud-only TTS to local large-model TTS + local-LLM routing + local image/music gen on new hardware |
| `SECRETS.md` | SOPS/age-based secrets management (replaces a plaintext `.env`) |
| `ZONOS2_SETUP.md` | Production voice-cloning engine setup — won the TTS engine bake-off on speaker similarity and word-error-rate |
| `ORPHEUS_SETUP.md` | Fallback/alternate TTS backend setup |
| `KNOWN_ISSUES.md` | Running bug/gap log, updated per session — not a design doc, just a record so findings aren't lost |
| `AGENTS_A1_A8_STATUS.md` | Status of the A1–A8 engine-update workstreams |

## TTS backend priority (as of v2.3)

**ZONOS2** is the production voice-cloning engine — it runs as a
standalone GPU server the engine talks to over HTTP. **Chatterbox** is
the secondary fallback, then **Kokoro**. The narrator falls back to
ZONOS2 (not Kokoro) for deliberate, pitch-preserving pacing; ultra-short
lines route to Kokoro to avoid cloning engines hallucinating on
one-/two-word inputs. Production cloning wants 2× 24 GB GPUs; without
one the engine still runs, falling back to Kokoro.

See `documents/USER MANUAL/AEON_PULP_DRAMA_ENGINE_USER_MANUAL.md` §18
for the full TTS backend writeup and §33 for the version-by-version
changelog this page's summary is drawn from.
