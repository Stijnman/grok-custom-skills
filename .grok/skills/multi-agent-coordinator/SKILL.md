---
name: multi-agent-coordinator
description: >
  Coordinates multiple agents with role assignment and handoffs. Use for paral
  lel work or user says coordinate agents, multi agent team. Use when the user
   needs this capability. Triggers: coordinate agents, multi agent team, agent
   roles, delegate agents.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [coordinate agents, multi agent team, agent roles, delegate agents]
    related_skills: [multi-agent-orchestrator, desktop-subagent-connector, goal-verifier]
compatibility: Grok agent; optional MCP and shell access
---

# Multi Agent Coordinator

## When to Use

- User says **coordinate agents** or task matches this capability
- User says **multi agent team** or task matches this capability
- User says **agent roles** or task matches this capability
- User says **delegate agents** or task matches this capability

## Workflow

1. Define roles: planner, executor, reviewer (minimum).
2. Assign subtasks per role.
3. Establish handoff format between agents.
4. Merge outputs; run goal-verifier on combined result.

## Integrations

- `multi-agent-orchestrator`
- `desktop-subagent-connector`
- `goal-verifier`

## Error Handling

| Failure | Response |
|---------|----------|
| Agent conflict | Reviewer role breaks tie. |

## Gotchas

- Max 5 parallel agents to avoid context sprawl.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
