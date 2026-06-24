---
name: parallel-tool-orchestrator
description: >
  Runs independent tool calls in parallel for latency reduction. Use when mult
  iple reads/searches needed or user says parallel tools, run concurrently. Tr
  iggers: parallel tools, run concurrently, batch requests, parallelize.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [parallel tools, run concurrently, batch requests, parallelize]
    related_skills: [performance-optimizer, bottleneck-resolver, multi-agent-orchestrator]
compatibility: Grok agent; optional MCP and shell access
---

# Parallel Tool Orchestrator

## When to Use

- User says **parallel tools** or task matches this capability
- User says **run concurrently** or task matches this capability
- User says **batch requests** or task matches this capability
- User says **parallelize** or task matches this capability

## Workflow

1. Identify independent tool calls in plan.
2. Batch parallel execution (max 5 concurrent).
3. Collect results; handle partial failures.
4. Continue sequential steps that depend on results.

## Integrations

- `performance-optimizer`
- `bottleneck-resolver`
- `multi-agent-orchestrator`

## Error Handling

| Failure | Response |
|---------|----------|
| Rate limited | Backoff exponentially; reduce concurrency. |

## Gotchas

- Never parallelize dependent or destructive operations.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
