---
name: evolver
description: "Lightweight skill mutation helper for quick iterations. Use for: quick evolve, mutate skill, tweak skill, `skill-evolver`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [quick evolve, mutate skill, tweak skill]
    related_skills: [skill-evolver, evolution, hyper-skill-tester]
compatibility: Grok agent; optional MCP and shell access
---
# Evolver
## When to Use

- User says **quick evolve** or task matches this capability
- User says **mutate skill** or task matches this capability
- User says **tweak skill** or task matches this capability

## Workflow

1. Load target SKILL.md.
2. Apply single targeted edit (description, workflow step, error row).
3. Validate frontmatter; save.
4. Notify skill-evolution-engine of change.

## Integrations

- `skill-evolver`
- `evolution`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| Invalid frontmatter | Restore from git or versions/ backup. |

## Gotchas

- Prefer skill-evolver for major rewrites.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
