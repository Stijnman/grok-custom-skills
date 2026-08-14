---
name: exposed-service-triage
description: "Triages exposed TCP listeners found by security audits. Use for: exposed port, what is listening, fix exposed service, open port."
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [exposed port, what is listening, fix exposed service, open port]
    related_skills: [defensive-mcp-audit, hitl-approver]
    publication_reviewed: '2026-06-24'
compatibility: Grok agent; optional MCP and shell access
---
# Exposed Service Triage
## When to Use

- User says **exposed port** or task matches this capability
- User says **what is listening** or task matches this capability
- User says **fix exposed service** or task matches this capability
- User says **open port** or task matches this capability

## Workflow

1. Run read-only listener inventory (ss -tln, fuser) on user machine.
2. Map ports to processes; classify MCP-related vs system vs unknown.
3. Present findings table with risk tier and plain-language explanation.
4. Recommend: bind 127.0.0.1, disable service, or firewall rule.
5. Before stopping/disabling any service: hitl-approver required.
6. Never run aggressive remote scans or attack exposed services.

## Integrations

- `defensive-mcp-audit`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Cannot identify process | Report port and binding; suggest sudo ss -tlnp with user consent. |
| User requests aggressive scan | Decline; offer defensive audit only. |

## Gotchas

- Common OS services on 0.0.0.0 may be intentional; explain before recommending disable.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Read-only discovery first; service changes only after HITL approval.
- No denial-of-service, exploitation, or unauthorized access attempts.
- Remediation is documented steps for the user or admin to apply.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
