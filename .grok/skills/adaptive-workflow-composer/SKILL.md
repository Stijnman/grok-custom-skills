---
name: adaptive-workflow-composer
description: >
  Composes multi-step agent workflows from goals and available skills. Use whe
  ntasks need orchestration or user says compose workflow, plan steps, adaptiv
  epipeline. Triggers: compose workflow, plan steps.
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [compose workflow, plan steps, adaptive pipeline, orchestrate task]
    related_skills: [workflow-composer, multi-agent-orchestrator, tool-discovery-engine]
---

# Adaptive Workflow Composer

## When to Use

- User says **compose workflow** or task matches this capability
- User says **plan steps** or task matches this capability
- User says **adaptive pipeline** or task matches this capability
- User says **orchestrate task** or task matches this capability

## Workflow

1. Parse goal into subtasks with dependencies.
2. Map subtasks to installed skills via tool-discovery-engine.
3. Order steps; identify parallelizable segments.
4. Output workflow DAG with skill assignments and fallbacks.

## Integrations

- `workflow-composer`
- `multi-agent-orchestrator`
- `tool-discovery-engine`

## Error Handling

| Failure | Response |
|---------|----------|
| No matching skill | Suggest natural-language-to-skill or manual step. |

## Gotchas

- Prefer fewer steps; merge trivial subtasks.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
