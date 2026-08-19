---
name: skill-evolution-engine
description: "Manages skill version history and automated improvement cycles. Use for: evolve skills, version skills, skill maintenance, `skill-evolver`."
version: 1.2.1
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

1. Snapshot the current SKILL.md to a local versioned backup and run the hyper-skill-tester baseline.
2. Prepare the proposed evolution as a reviewable diff with expected benefits, risks, and rollback path.
3. Obtain explicit user approval before applying, committing, publishing, or otherwise persisting the proposed change.
4. After approval, apply the change and compare scores. Present any regression and its rollback option for approval rather than rolling back automatically.

## Integrations

- `skill-evolver`
- `evolution`
- `evolver`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| Score regression | Preserve the evidence, present the latest backup and rollback diff, and wait for user approval before restoring. |

## Gotchas

- Keep version backups locally; do not publish, delete, or restore them without explicit user approval.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
