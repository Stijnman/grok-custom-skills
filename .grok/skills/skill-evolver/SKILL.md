---
name: skill-evolver
description: "Full skill rewrite and improvement with versioned backups and templates. Use for: evolve skill, upgrade SKILL.md, improve skill file, `skill-evolution-engine`."
version: 1.2.1
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [evolve skill, upgrade SKILL.md, improve skill file]
    related_skills: [skill-evolution-engine, hyper-skill-tester, natural-language-to-skill]
compatibility: Grok agent; optional MCP and shell access
---
# Skill Evolver
## When to Use

- User says **evolve skill** or task matches this capability
- User says **upgrade SKILL.md** or task matches this capability
- User says **improve skill file** or task matches this capability

## Workflow

1. Create a local versioned backup of the target SKILL.md and read references/evolution-guide.md for the rubric.
2. Prepare a reviewable rewrite diff that identifies the affected sections, expected benefits, and rollback path.
3. Obtain explicit user approval before applying, saving, committing, publishing, or otherwise persisting the rewrite.
4. After approval, apply the rewrite and validate it with hyper-skill-tester. Present any rollback option for approval rather than restoring automatically.

## References

Read `references/evolution-guide.md` when setup, backends, or rubric details are needed.

## Integrations

- `skill-evolution-engine`
- `hyper-skill-tester`
- `natural-language-to-skill`

## Error Handling

| Failure | Response |
|---------|----------|
| Broken frontmatter | Preserve the draft, show the local backup and rollback diff, and wait for user approval before restoring. |

## Gotchas

- Read references/evolution-guide.md before major rewrites.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
