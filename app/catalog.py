from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CatalogItem:
    id: str
    owner: str
    repo: str
    title: str
    category: str
    description: str
    include: tuple[str, ...] = ()
    fetch_manifest: bool = False
    source_owner: str | None = None
    source_repo: str | None = None

    @property
    def ingest_owner(self) -> str:
        return self.source_owner or self.owner

    @property
    def ingest_repo(self) -> str:
        return self.source_repo or self.repo


CATALOG: tuple[CatalogItem, ...] = (
    # Skills are usually small repositories containing SKILL.md plus reference
    # material. These examples mirror a homelab / AI / operations workflow
    # without exposing any private repository names.
    CatalogItem(
        "skill:homelab-ops",
        "skills",
        "homelab-ops",
        "homelab-ops",
        "skill",
        "Network, Docker, DNS, monitoring, and recovery runbooks.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:ai-platform",
        "skills",
        "ai-platform",
        "ai-platform",
        "skill",
        "Local AI services, model runners, memory services, and automation reference.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:website-ops",
        "skills",
        "website-ops",
        "website-ops",
        "skill",
        "Website publishing, CMS operations, article workflow, and deployment notes.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:security-runbooks",
        "skills",
        "security-runbooks",
        "security-runbooks",
        "skill",
        "Firewall, hardening, incident response, and audit procedures.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:media-services",
        "skills",
        "media-services",
        "media-services",
        "skill",
        "Self-hosted media service operations and troubleshooting reference.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:pdf-tooling",
        "skills",
        "pdf-tooling",
        "pdf-tooling",
        "skill",
        "PDF extraction, OCR, conversion, merging, and API reference.",
        ("SKILL.md", "references/**"),
    ),
    CatalogItem(
        "skill:visual-tools",
        "skills",
        "visual-tools",
        "visual-tools",
        "skill",
        "Diagram, chart, and inline visual rendering guidance.",
        ("SKILL.md", "references/**"),
    ),
    # Repository entries can point directly at real forge repositories.
    CatalogItem("repo:infra/homelab", "infra", "homelab", "infra/homelab", "infra", "Home infrastructure reference repository."),
    CatalogItem("repo:infra/network", "infra", "network", "infra/network", "infra", "Router, DNS, VPN, and firewall configuration reference."),
    CatalogItem("repo:infra/monitoring", "infra", "monitoring", "infra/monitoring", "infra", "Metrics, logging, dashboards, and alerting repository."),
    CatalogItem("repo:apps/web", "apps", "web", "apps/web", "app", "Public website or web application repository."),
    CatalogItem("repo:apps/ai-platform", "apps", "ai-platform", "apps/ai-platform", "app", "Local AI platform source and service definitions."),
    CatalogItem("repo:tools/scripts", "tools", "scripts", "tools/scripts", "tool", "Bootstrap scripts, shell helpers, and workstation sync tooling.", fetch_manifest=True),
    CatalogItem("repo:tools/forge-ingest", "tools", "forge-ingest", "tools/forge-ingest", "tool", "Read-only Git forge ingest service."),
    CatalogItem("repo:tools/forge-mcp", "tools", "forge-mcp", "tools/forge-mcp", "tool", "OAuth-protected MCP wrapper for forge-ingest."),
    CatalogItem("repo:docs/runbooks", "docs", "runbooks", "docs/runbooks", "docs", "Operational runbooks and service documentation."),
    # Alias example: expose a friendly MCP-facing name while fetching from a
    # different underlying repository.
    CatalogItem(
        "repo:ai/context",
        "ai",
        "context",
        "ai/context",
        "ai",
        "Friendly alias for the main AI platform context repository.",
        source_owner="apps",
        source_repo="ai-platform",
    ),
)


def get_item(item_id: str) -> CatalogItem | None:
    return next((item for item in CATALOG if item.id == item_id), None)
