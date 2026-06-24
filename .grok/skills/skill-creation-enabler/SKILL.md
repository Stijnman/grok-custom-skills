---
name: skill-creation-enabler
description: >
  Scaffolds and installs new skills into .grok/skills/. Use when creating skil
  lsor user says enable skill creation, install skill, new skill. Triggers: en
  able skill creation, install skill, new skill, add skill.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [enable skill creation, install skill, new skill, add skill]
    related_skills: [natural-language-to-skill, hyper-skill-tester, create-skill]
compatibility: Grok agent; optional MCP and shell access
---

# Skill Creation Enabler

## When to Use

- User says **enable skill creation** or task matches this capability
- User says **install skill** or task matches this capability
- User says **new skill** or task matches this capability
- User says **add skill** or task matches this capability

## Workflow

1. Validate skill name (lowercase-hyphen, unique).
2. Create directory and SKILL.md from template.
3. Optionally add references/ and scripts/.
4. Confirm install path; list in controle-overview-skill.

## Integrations

- `natural-language-to-skill`
- `hyper-skill-tester`
- `create-skill`

## Error Handling

| Failure | Response |
|---------|----------|
| Name collision | Suggest versioned name or merge. |

## Gotchas

- Default install: ~/.grok/skills/ or workspace .grok/skills/.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
