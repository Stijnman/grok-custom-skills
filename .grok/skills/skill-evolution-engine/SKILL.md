---
name: skill-evolution-engine
description: "Manages skill version history and automated improvement cycles. Use for: evolve skills, version skills, skill maintenance, `skill-evolver`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [evolve skills, version skills, skill maintenance]
    related_skills: [skill-evolver, evolution, evolver, hyper-skill-tester]
compatibility: Grok agent; optional MCP and shell access
---
# Skill Evolution Engine
## When to Use

- User says **evolve skills** or task matches this capability
- User says **version skills** or task matches this capability
- User says **skill maintenance** or task matches this capability

## Workflow

1. Snapshot current SKILL.md to versions/.
2. Run hyper-skill-tester baseline.
3. Apply evolution proposal from evolution skill.
4. Compare scores; commit or rollback.

## Integrations

- `skill-evolver`
- `evolution`
- `evolver`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| Score regression | Auto-rollback to latest versions/ backup. |

## Gotchas

- Keeps last 10 version backups per skill.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
