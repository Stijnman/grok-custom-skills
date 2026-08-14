---
name: skill-evolver
description: "Full skill rewrite and improvement with versioned backups and templates. Use for: evolve skill, upgrade SKILL.md, improve skill file, `skill-evolution-engine`."
version: 1.2.0
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

1. Backup to versions/<timestamp>/SKILL.md.
2. Read references/evolution-guide.md for rubric.
3. Rewrite weak sections per 10-dimension review.
4. Validate; run hyper-skill-tester; save or rollback.

## References

Read `references/evolution-guide.md` when setup, backends, or rubric details are needed.

## Integrations

- `skill-evolution-engine`
- `hyper-skill-tester`
- `natural-language-to-skill`

## Error Handling

| Failure | Response |
|---------|----------|
| Broken frontmatter | Restore from versions/ immediately. |

## Gotchas

- Read references/evolution-guide.md before major rewrites.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
