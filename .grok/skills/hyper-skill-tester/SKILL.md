---
name: hyper-skill-tester
description: >
  Stress-tests skills with edge-case prompts and scoring rubric. Use before pu
  blishing skills or user says test skill, hyper test. Use when the user needs
   this capability. Triggers: test skill, hyper test, skill QA, audit skill qu
  ality.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [test skill, hyper test, skill QA, audit skill quality]
    related_skills: [auto-tester, skill-researcher, review-skill]
compatibility: Grok agent; optional MCP and shell access
---

# Hyper Skill Tester

## When to Use

- User says **test skill** or task matches this capability
- User says **hyper test** or task matches this capability
- User says **skill QA** or task matches this capability
- User says **audit skill quality** or task matches this capability

## Workflow

1. Load skill; generate 10 trigger and 5 anti-trigger prompts.
2. Simulate agent behavior against rubric.
3. Score 10 dimensions; flag scores below 3.
4. Output report with fix suggestions.

## Integrations

- `auto-tester`
- `skill-researcher`
- `review-skill`

## Error Handling

| Failure | Response |
|---------|----------|
| Skill not found | Verify path under .grok/skills/. |

## Gotchas

- Run after every skill-evolver change.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
