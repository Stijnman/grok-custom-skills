---
name: natural-language-to-skill
description: >
  Converts natural language descriptions into SKILL.md drafts. Use when user d
  escribes a new capability or says create skill from description. Triggers: c
  reate skill from description, NL to skill, skill from prompt.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [create skill from description, NL to skill, skill from prompt]
    related_skills: [skill-creation-enabler, hyper-skill-tester, skill-researcher]
compatibility: Grok agent; optional MCP and shell access
---

# Natural Language To Skill

## When to Use

- User says **create skill from description** or task matches this capability
- User says **NL to skill** or task matches this capability
- User says **skill from prompt** or task matches this capability

## Workflow

1. Parse intent: triggers, workflow, integrations, errors.
2. Generate SKILL.md following Agent Skills spec.
3. Run hyper-skill-tester on draft.
4. Save to .grok/skills/<name>/ via skill-creation-enabler.

## Integrations

- `skill-creation-enabler`
- `hyper-skill-tester`
- `skill-researcher`

## Error Handling

| Failure | Response |
|---------|----------|
| Vague request | Ask 3 clarifying questions before generating. |

## Gotchas

- Name must be lowercase-hyphen, max 64 chars.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
