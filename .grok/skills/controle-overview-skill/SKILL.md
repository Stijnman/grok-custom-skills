---
name: controle-overview-skill
description: >
  Provides control-panel overview of active skills, workflows, and status. Use
   when user says overview, status dashboard, what skills are active. Triggers
  : overview, status dashboard, what skills, control panel.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [overview, status dashboard, what skills, control panel]
    related_skills: [tool-discovery-engine, cron-scheduler, insight-synthesizer]
compatibility: Grok agent; optional MCP and shell access
---

# Controle Overview Skill

## When to Use

- User says **overview** or task matches this capability
- User says **status dashboard** or task matches this capability
- User says **what skills** or task matches this capability
- User says **control panel** or task matches this capability

## Workflow

1. List installed skills from .grok/skills/.
2. Summarize recent workflows and scheduled jobs.
3. Highlight risks from defensive audits if available.
4. Output status table: skill, last used, health.

## Integrations

- `tool-discovery-engine`
- `cron-scheduler`
- `insight-synthesizer`

## Error Handling

| Failure | Response |
|---------|----------|
| Skills dir missing | Report path; suggest install steps. |

## Gotchas

- Read-only inventory; do not modify skills during overview.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
