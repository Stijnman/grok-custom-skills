---
name: skill-researcher
description: "Researches existing skills and best practices before creating new ones. Use for: research skills, find skill examples, skill best practices, `natural-language-to-skill`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [research skills, find skill examples, skill best practices]
    related_skills: [natural-language-to-skill, skill-creation-enabler, tool-discovery-engine]
compatibility: Grok agent; optional MCP and shell access
---
# Skill Researcher
## When to Use

- User says **research skills** or task matches this capability
- User says **find skill examples** or task matches this capability
- User says **skill best practices** or task matches this capability

## Workflow

1. Search agentskill.sh and local .grok/skills/.
2. Compare similar skills; note gaps.
3. Summarize best patterns to adopt.
4. Recommend install or custom authoring path.

## Integrations

- `natural-language-to-skill`
- `skill-creation-enabler`
- `tool-discovery-engine`

## Error Handling

| Failure | Response |
|---------|----------|
| No matches | Propose greenfield skill spec. |

## Gotchas

- Prefer extending existing skills over duplicates.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
