---
name: connected-services-bridge
description: >
  Connects external services (GitHub, Notion, Drive) to agent workflows. Use w
  hen integrating APIs or user says connect service, bridge API. Triggers: con
  nectservice, bridge API, integrate GitHub, hook up Notion.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [connect service, bridge API, integrate GitHub, hook up Notion]
    related_skills: [drive-persistence-bridge, tool-discovery-engine, internet-enabler]
compatibility: Grok agent; optional MCP and shell access
---

# Connected Services Bridge

## When to Use

- User says **connect service** or task matches this capability
- User says **bridge API** or task matches this capability
- User says **integrate GitHub** or task matches this capability
- User says **hook up Notion** or task matches this capability

## Workflow

1. Identify service and required scopes.
2. Check MCP or OAuth availability.
3. Configure connection; test read-only call first.
4. Document usage pattern for workflow-composer.

## Integrations

- `drive-persistence-bridge`
- `tool-discovery-engine`
- `internet-enabler`

## Error Handling

| Failure | Response |
|---------|----------|
| Auth missing | Guide user through auth; never store tokens in skill files. |

## Gotchas

- Least-privilege scopes only.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
