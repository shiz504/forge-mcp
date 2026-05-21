# Configuration

`forge-mcp` exposes a remote OAuth-protected MCP server in front of
`forge-ingest`.

## Required Runtime Files

```text
.env
data/oauth-state.json
```

These are intentionally not committed.

## Environment

```env
MCP_PUBLIC_BASE_URL=https://mcp.example.net
INGEST_BASE_URL=http://host.docker.internal:8092
INGEST_TOKEN=copy-from-forge-ingest-env
INGEST_DEFAULT_REF=main
INGEST_REQUEST_TIMEOUT_SECONDS=90
ALLOWED_OAUTH_REDIRECT_HOSTS=chatgpt.com,claude.ai
```

`INGEST_TOKEN` remains server-side. MCP clients receive OAuth bearer tokens for
the MCP server, not the ingest capability token.

## OAuth

The server supports OAuth discovery and dynamic client registration for allowed
redirect hosts. Keep `ALLOWED_OAUTH_REDIRECT_HOSTS` tight and add new AI clients
one at a time.

Protect `/authorize` at the reverse proxy layer. Common options include Basic
Auth, SSO, or an access gateway.

## Catalog

The MCP-facing catalog lives in `app/catalog.py`. Catalog entries can point
directly at forge repositories or expose aliases through `source_owner` and
`source_repo`.
