# Operations

## Health Check

```bash
curl -fsS http://127.0.0.1:8093/healthz
```

Expected response:

```text
ok
```

## Restart

```bash
docker compose up -d --build
docker compose logs -f --tail=100
```

The container uses `restart: unless-stopped`.

## OAuth State

OAuth clients and tokens are stored in:

```text
data/oauth-state.json
```

Back this file up before pruning clients or changing OAuth behavior. Do not
commit it.

## Add AI Client

1. Add the provider redirect hostname to `ALLOWED_OAUTH_REDIRECT_HOSTS`.
2. Rebuild/restart the container.
3. Register the MCP URL in the AI client.
4. Confirm `/mcp` rejects unauthenticated requests.
5. Confirm tool calls use OAuth and do not expose `INGEST_TOKEN`.

## Update Catalog

Edit `app/catalog.py`, rebuild, then test:

```bash
curl -fsS http://127.0.0.1:8093/healthz
```

Then use an authenticated MCP client to call:

```text
list_repos
list_skills
search
```

## Troubleshooting

- `invalid_client`: the OAuth state file does not contain that client ID.
- `invalid_redirect_uri`: the provider hostname is not allowed.
- ingest errors: verify `INGEST_BASE_URL`, `INGEST_TOKEN`, and the ingest
  service health check.
- catalog miss: update `app/catalog.py`, rebuild, then retest catalog tools.
