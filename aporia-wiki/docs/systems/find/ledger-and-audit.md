# Company Ledger & audit model

**Single-writer pattern:** only the `Steward` (`find/ledger/`) writes to
the Company Ledger. Every agent reads through a `LedgerSnapshot` —
prevents concurrent corruption from ten independently-scheduled agents.
Raw writes outside the Steward go through `write_cursor(conn)` in
`find/ledger/ledger_db.py` when unavoidable (e.g. Authorizer/Compliance).

Other structural principles:

- **Mock-first connectors** — every external API (Mercury, Stripe, ...)
  has Mock + Real implementations, selected by env-var toggle. Tests and
  dev run against mocks; production flips connectors one at a time as
  accounts open.
- **Encrypted-at-rest secrets** — subscription credentials and document
  files use AES-GCM with a scrypt KDF (`find/crypto.py`), unlocked by a
  single `FIND_VAULT_PASSPHRASE`.
- Schema changes are sequentially numbered SQL migrations in
  `find/ledger/migrations/`, applied in order by
  `scripts/bootstrap_ledger.py`.

See [Decision Queue](decision-queue.md) for how agent proposals and the
audit trail connect.
