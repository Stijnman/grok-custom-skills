---
name: evolution
description: "Tracks incremental improvements to skills and workflows over time. Use for: evolve skill, track evolution, improve over time, `skill-evolver`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [evolve skill, track evolution, improve over time]
    related_skills: [skill-evolver, skill-evolution-engine, evolver]
compatibility: Grok agent; optional MCP and shell access
---
# Evolution
## When to Use

- User says **evolve skill** or task matches this capability
- User says **track evolution** or task matches this capability
- User says **improve over time** or task matches this capability

## Workflow

1. Capture baseline metrics (triggers, success rate, user feedback).
2. Propose one improvement per cycle.
3. Apply via skill-evolver; version backup.
4. Compare before/after; keep or rollback.

## Integrations

- `skill-evolver`
- `skill-evolution-engine`
- `evolver`

## Error Handling

| Failure | Response |
|---------|----------|
| Regression detected | Rollback from versions/ backup. |

## Gotchas

- One change per evolution cycle for clear attribution.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
