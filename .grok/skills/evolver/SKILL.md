---
name: evolver
description: "Lightweight skill mutation helper for quick iterations. Use for: quick evolve, mutate skill, tweak skill, `skill-evolver`."
version: 1.2.1
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

1. Load the target SKILL.md and identify one narrowly scoped proposed edit.
2. Present the proposed change and expected effect; obtain explicit user approval before changing or saving the file.
3. After approval, apply the edit and validate the frontmatter.
4. Keep the change local unless the user separately authorizes a commit, publication, backup upload, or other external persistence.

## Integrations

- `skill-evolver`
- `evolution`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| Invalid frontmatter | Preserve the broken draft, show the restore option from git or a local versioned backup, and wait for approval before restoring. |

## Gotchas

- Prefer skill-evolver for major rewrites.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
