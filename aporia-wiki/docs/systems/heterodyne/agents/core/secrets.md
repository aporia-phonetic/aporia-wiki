# secrets

*Source: `heterodyne/agents/secrets.py`*

agents/secrets.py

A8 — SOPS Secrets loader.

Drop-in replacement for `from dotenv import load_dotenv; load_dotenv()`.
Loads secrets from a SOPS-encrypted YAML file (config/secrets.enc.yaml) and
populates os.environ for the rest of the engine. Falls back to .env in dev
or when sops isn't installed.

Why SOPS:
    .env files are unencrypted plaintext. SOPS encrypts at-rest with an age
    key on the host (not committed). The encrypted YAML lives in the repo
    safely; only a machine with the age key can decrypt it. Rotating a
    leaked key means re-encrypting the file, not rebuilding the deploy.

Lookup order (first non-empty wins):
    1. Already-set os.environ (e.g. CI, shell export)
    2. .env file (dev workflow — load_dotenv as before)
    3. SOPS-decrypted YAML (prod / new-rig workflow)

This order means .env always wins in dev, so existing developer flows
keep working with zero changes. SOPS only fills in keys that aren't
already provided.

Usage:
    from agents.secrets import load_secrets
    load_secrets()  # replaces load_dotenv() at top of main.py

If sops isn't installed or the encrypted file is missing, this falls back
silently to plain load_dotenv() behavior. That's intentional — dev work
shouldn't require sops.

The encrypted YAML structure mirrors .env keys verbatim:

    anthropic_api_key: sk-ant-...
    elevenlabs_api_key: ...
    freesound_api_key: ...
    openai_api_key: ...
    replicate_api_token: ...

Keys are uppercased before being written to os.environ to match .env
convention (e.g. `anthropic_api_key` -> ANTHROPIC_API_KEY).

See AEON-ENGINE/SECRETS.md for the full runbook (install, age key
generation, rotation).

## Defined here

### `SecretsError`

Raised when SOPS decryption fails in a way that should NOT be silent
(e.g. encrypted file exists but sops binary is missing in prod).

## Top-level functions

- **`load_secrets()`** — Populate os.environ from .env and (if available) the SOPS-encrypted YAML.
