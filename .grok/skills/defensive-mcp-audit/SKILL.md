---
name: defensive-mcp-audit
description: "Runs a defensive, read-only security audit of the local machine for MCP and AIagent risks: risky bindings, MCP config issues, and confused-deputy exposu re. Use for: audit mcp, mcp security, localhost exposure, defensive-mcp-audit."
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [audit mcp, mcp security, localhost exposure, defensive-mcp-audit]
    related_skills: [exposed-service-triage, mcp-tool-scout, hitl-approver]
    publication_reviewed: '2026-06-24'
compatibility: Grok agent; optional MCP and shell access
---
# Defensive MCP Audit
## When to Use

- User says **audit mcp** or task matches this capability
- User says **mcp security** or task matches this capability
- User says **localhost exposure** or task matches this capability
- User says **defensive-mcp-audit** or task matches this capability

## Workflow

1. Confirm audit is read-only; no port scanning beyond localhost inventory.
2. Run: python3 -m defensive_mcp_audit (or pip install defensive-mcp-audit[cli]).
3. Parse risk_level, risk_score, and findings table.
4. Explain each finding in plain language with remediation (bind localhost, disable service).
5. Never suggest attack techniques, malware, or penetration tests.
6. Offer HTML/JSON export path; do not upload reports externally without user consent.

## Integrations

- `exposed-service-triage`
- `mcp-tool-scout`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Tool not installed | pip install defensive-mcp-audit[cli] or clone github.com/Stijnman/defensive-mcp-audit. |
| Permission denied on ss | Report limitation; suggest user-run with adequate permissions. |

## Gotchas

- Defensive only — inspection, not exploitation.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Read-only inspection; no network attacks or exploitation.
- Reports stay local unless user explicitly requests upload.
- Remediation advice is configuration-only (bind, disable, firewall).

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

### Attribution

- Wraps the MIT-licensed defensive-mcp-audit project by Stijnman.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
