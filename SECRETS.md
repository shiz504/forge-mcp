# Secrets

This repository intentionally omits live secrets.

Never commit:

- `.env`
- `INGEST_TOKEN`
- OAuth state files under `data/`
- reverse-proxy login files
- reverse-proxy password hashes
- tunnel credentials
- cloud provider API keys

Safe to commit:

- `.env.example`
- source code
- placeholder deployment snippets
- documentation using example hostnames or placeholders

If OAuth state or the ingest token is committed, revoke affected OAuth clients
or rotate the ingest token before continuing.
