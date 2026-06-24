---
name: performance-optimizer
description: >
  Optimizes agent and code performance via profiling and tuning. Use when slow
   execution or user says optimize performance, make faster. Triggers: optimiz
  e performance, make faster, performance tune.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [optimize performance, make faster, performance tune]
    related_skills: [bottleneck-resolver, parallel-tool-orchestrator, predictive-cache-manager]
compatibility: Grok agent; optional MCP and shell access
---

# Performance Optimizer

## When to Use

- User says **optimize performance** or task matches this capability
- User says **make faster** or task matches this capability
- User says **performance tune** or task matches this capability

## Workflow

1. Profile hot paths: tools, loops, prompts.
2. Apply: caching, shorter prompts, parallel tools, lazy load.
3. Measure improvement.
4. Document tradeoffs for user.

## Integrations

- `bottleneck-resolver`
- `parallel-tool-orchestrator`
- `predictive-cache-manager`

## Error Handling

| Failure | Response |
|---------|----------|
| No baseline | Record timing before changes. |

## Gotchas

- Do not sacrifice correctness for speed.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
