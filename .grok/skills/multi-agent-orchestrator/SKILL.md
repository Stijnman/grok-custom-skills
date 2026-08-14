---
name: multi-agent-orchestrator
description: "Orchestrates complex multi-agent pipelines with DAG execution. Use for: orchestrate agents, agent pipeline, multi step agents, `multi-agent-coordinator`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [orchestrate agents, agent pipeline, multi step agents]
    related_skills: [multi-agent-coordinator, parallel-tool-orchestrator, self-refine-loop]
compatibility: Grok agent; optional MCP and shell access
---
# Multi Agent Orchestrator
## When to Use

- User says **orchestrate agents** or task matches this capability
- User says **agent pipeline** or task matches this capability
- User says **multi step agents** or task matches this capability

## Workflow

1. Build task DAG via adaptive-workflow-composer.
2. Spawn agents per node with scoped context.
3. Execute topological order; parallelize independent nodes.
4. Aggregate; run self-refine-loop on final output.

## Integrations

- `multi-agent-coordinator`
- `parallel-tool-orchestrator`
- `self-refine-loop`

## Error Handling

| Failure | Response |
|---------|----------|
| DAG cycle | Break cycle; serialize conflicting nodes. |

## Gotchas

- Integrates self-refine-loop as skeptic reviewer agent.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
