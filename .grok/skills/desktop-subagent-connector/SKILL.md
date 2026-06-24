---
name: desktop-subagent-connector
description: >
  Spawns desktop subagents for isolated GUI or local tasks. Use when delegatin
  gscreen work or user says desktop subagent, spawn local agent. Triggers: des
  ktop subagent, spawn local agent, delegate desktop.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [desktop subagent, spawn local agent, delegate desktop]
    related_skills: [computer-use-bridge, multi-agent-coordinator]
compatibility: Grok agent; optional MCP and shell access
---

# Desktop Subagent Connector

## When to Use

- User says **desktop subagent** or task matches this capability
- User says **spawn local agent** or task matches this capability
- User says **delegate desktop** or task matches this capability

## Workflow

1. Define subagent scope and timeout.
2. Launch with minimal tool set for task.
3. Monitor progress; collect result artifact.
4. Terminate subagent; merge results to parent context.

## Integrations

- `computer-use-bridge`
- `multi-agent-coordinator`

## Error Handling

| Failure | Response |
|---------|----------|
| Subagent timeout | Return partial result; report stuck step. |

## Gotchas

- Subagents inherit safety rules including hitl-approver.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
