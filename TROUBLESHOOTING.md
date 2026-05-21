# Troubleshooting

## Health Check Fails

```bash
docker compose ps
docker compose logs --tail=100 forge-mcp
curl -i http://127.0.0.1:8093/healthz
```

Check that `.env` exists and that `INGEST_BASE_URL` points at a healthy
`forge-ingest` service.

## OAuth Registration Rejected

If a client reports `invalid_redirect_uri`, add the provider hostname to:

```env
ALLOWED_OAUTH_REDIRECT_HOSTS=chatgpt.com,claude.ai
```

Restart after editing `.env`.

## Invalid Client

If a client reports `invalid_client`, the OAuth client ID is not present in
`data/oauth-state.json`.

Common causes:

- `data/` was deleted
- the container was moved without copying OAuth state
- the client registration was pruned

Reconnect the MCP client or restore the state file from backup.

## Ingest Errors

MCP tools call `forge-ingest` server-side. Check:

- `INGEST_BASE_URL`
- `INGEST_TOKEN`
- `forge-ingest` health
- target repository deploy-key access
- catalog mapping in `app/catalog.py`

## Tool Finds The Wrong Repo

The MCP server uses the static catalog in `app/catalog.py`.

Update the catalog entry, rebuild, and retest:

```bash
docker compose up -d --build
```

Then call:

```text
search
list_repos
list_skills
```

## Protecting Authorization

The `/authorize` route opens in a browser during OAuth setup. Protect it at the
reverse proxy layer with Basic Auth, SSO, or an access gateway.
