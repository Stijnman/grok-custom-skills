---
name: oss-repo-maintainer
description: "Helps maintain open-source repos: README accuracy, version consistency, andp re-release checklists. Use for: fix README, prep release, repo maintenance, sync docs."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [fix README, prep release, repo maintenance, sync docs]
    related_skills: [github-repo-scout, skill-collection-bootstrapper, goal-verifier]
    publication_reviewed: '2026-06-24'
---
# Oss Repo Maintainer
## When to Use

- User says **fix README** or task matches this capability
- User says **prep release** or task matches this capability
- User says **repo maintenance** or task matches this capability
- User says **sync docs** or task matches this capability

## Workflow

1. Diff README skill/file lists vs git tree.
2. Flag stale counts, missing install paths, broken links.
3. Propose README and CHANGELOG edits; show diff before commit.
4. Run validators (tests, skill validate) if present in repo.
5. Suggest conventional commit message; hitl-approver before git push.

## Integrations

- `github-repo-scout`
- `skill-collection-bootstrapper`
- `goal-verifier`

## Error Handling

| Failure | Response |
|---------|----------|
| Not a git repo | Limit to file review only. |

## Gotchas

- Never push or publish without explicit user approval.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Documentation accuracy focus; no unauthorized releases.
- Git push and publish require hitl-approver.
- Generic OSS workflow; no hardcoded user or org paths in instructions.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
