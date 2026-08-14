---
name: mcp-tool-scout
description: "Discovers MCP servers and reads tool schemas before calling MCP tools. Use for: mcp tools, MCP schema, discover MCP, which MCP tool."
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [mcp tools, MCP schema, discover MCP, which MCP tool]
    related_skills: [tool-discovery-engine, defensive-mcp-audit, hitl-approver]
    publication_reviewed: '2026-06-24'
compatibility: Grok agent; optional MCP and shell access
---
# MCP Tool Scout
## When to Use

- User says **mcp tools** or task matches this capability
- User says **MCP schema** or task matches this capability
- User says **discover MCP** or task matches this capability
- User says **which MCP tool** or task matches this capability

## Workflow

1. List MCP server folders (e.g. mcps/<server>/tools/*.json).
2. Match user task keywords to available tool names and descriptions.
3. Read full inputSchema for chosen tool before any CallMcpTool.
4. Report missing auth or server instructions; do not guess parameters.
5. Prefer least-privilege tool selection.

## Integrations

- `tool-discovery-engine`
- `defensive-mcp-audit`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Schema missing | Stop; do not call tool without reading descriptor. |
| Auth required | Ask user to complete auth out-of-band; never embed secrets in skill. |

## Gotchas

- Mandatory schema read prevents parameter injection mistakes.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Read-only discovery; no MCP calls without user task context.
- Never log or publish auth tokens from MCP configs.
- Tool paths use forward slashes; no Windows credential stores.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
