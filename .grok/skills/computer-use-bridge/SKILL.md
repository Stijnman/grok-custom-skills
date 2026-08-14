---
name: computer-use-bridge
description: "Bridges desktop automation to agent tool calls. Use for: computer use, desktop control, click on screen, GUI automation."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [computer use, desktop control, click on screen, GUI automation]
    related_skills: [desktop-subagent-connector, hitl-approver]
compatibility: Grok agent; optional MCP and shell access
---
# Computer Use Bridge
## When to Use

- User says **computer use** or task matches this capability
- User says **desktop control** or task matches this capability
- User says **click on screen** or task matches this capability
- User says **GUI automation** or task matches this capability

## Workflow

1. Confirm desktop environment and permissions.
2. Plan actions: click, type, navigate (minimal steps).
3. Execute via desktop-subagent-connector with screenshots.
4. Verify outcome visually; retry once on mismatch.

## Integrations

- `desktop-subagent-connector`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Permission denied | Ask user to grant accessibility permissions. |

## Gotchas

- Destructive GUI actions require hitl-approver.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
