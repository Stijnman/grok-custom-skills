---
name: tool-discovery-engine
description: "Discovers available tools, MCP servers, and skills for a task. Use for: what tools, discover capabilities, find tool for, available skills."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [what tools, discover capabilities, find tool for, available skills]
    related_skills: [adaptive-workflow-composer, control-overview, skill-researcher]
compatibility: Grok agent; optional MCP and shell access
---
# Tool Discovery Engine
## When to Use

- User says **what tools** or task matches this capability
- User says **discover capabilities** or task matches this capability
- User says **find tool for** or task matches this capability
- User says **available skills** or task matches this capability

## Workflow

1. Scan MCP tool descriptors and .grok/skills/.
2. Match task keywords to tools/skills.
3. Rank by relevance and availability.
4. Output recommended tool/skill list with paths.

## Integrations

- `adaptive-workflow-composer`
- `control-overview`
- `skill-researcher`

## Error Handling

| Failure | Response |
|---------|----------|
| MCP dir missing | List skills only; note MCP unavailable. |

## Gotchas

- Always read tool schema before calling MCP tools.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
