---
name: workflow-composer
description: >
  Composes linear and branching workflows from goals and constraints. Use when
   planning multi-step work or user says compose workflow, build plan. Trigger
  s: compose workflow, build plan, workflow plan, step by step plan.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [compose workflow, build plan, workflow plan, step by step plan]
    related_skills: [adaptive-workflow-composer, goal-verifier, skill-synergy-orchestrator]
compatibility: Grok agent; optional MCP and shell access
---

# Workflow Composer

## When to Use

- User says **compose workflow** or task matches this capability
- User says **build plan** or task matches this capability
- User says **workflow plan** or task matches this capability
- User says **step by step plan** or task matches this capability

## Workflow

1. Define goal, constraints, and success criteria.
2. Break into steps with inputs/outputs per step.
3. Assign skills or tools per step.
4. Output markdown workflow doc with checklist.

## Integrations

- `adaptive-workflow-composer`
- `goal-verifier`
- `skill-synergy-orchestrator`

## Error Handling

| Failure | Response |
|---------|----------|
| Scope creep | Cap at 15 steps; split into phases if larger. |

## Gotchas

- workflow-composer is linear; use adaptive-workflow-composer for DAGs.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
