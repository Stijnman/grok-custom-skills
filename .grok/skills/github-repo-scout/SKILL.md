---
name: github-repo-scout
description: "Investigates a GitHub repository from a URL: README, file tree, local clones tatus, and recommended next steps. Use for: github.com, check this repo, scout repo, what is this project."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [github.com, check this repo, scout repo, what is this project]
    related_skills: [oss-repo-maintainer, defensive-mcp-audit, skill-rubric-reviewer]
    publication_reviewed: '2026-06-24'
---
# GitHub Repo Scout
## When to Use

- User says **github.com** or task matches this capability
- User says **check this repo** or task matches this capability
- User says **scout repo** or task matches this capability
- User says **what is this project** or task matches this capability

## Workflow

1. Parse owner/repo from URL; reject non-GitHub hosts unless user confirms.
2. Fetch README and top-level tree via public API or git clone (read-only).
3. Compare README claims vs actual committed files (note drift).
4. Check if repo exists locally in workspace or common clone paths.
5. Summarize: purpose, install steps, risks, suggested actions (clone, audit, review).
6. Do not access private repos without authenticated user context.

## Integrations

- `oss-repo-maintainer`
- `defensive-mcp-audit`
- `skill-rubric-reviewer`

## Error Handling

| Failure | Response |
|---------|----------|
| 404/private repo | State access limitation; ask user to clone locally. |
| Rate limited | Backoff; use local clone if available. |

## Gotchas

- Public repos only unless user has authenticated MCP/GitHub access.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Read-only repository inspection.
- No harvesting of tokens, secrets, or private issue content.
- Do not auto-clone into system directories without user approval.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
