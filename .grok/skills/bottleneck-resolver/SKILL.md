---
name: bottleneck-resolver
description: "Identifies and resolves performance bottlenecks in agent workflows. Use for: find bottleneck, speed up, why so slow, optimize workflow."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [find bottleneck, speed up, why so slow, optimize workflow]
    related_skills: [performance-optimizer, parallel-tool-orchestrator, predictive-cache-manager]
compatibility: Grok agent; optional MCP and shell access
---
# Bottleneck Resolver
## When to Use

- User says **find bottleneck** or task matches this capability
- User says **speed up** or task matches this capability
- User says **why so slow** or task matches this capability
- User says **optimize workflow** or task matches this capability

## Workflow

1. Profile step durations (tool calls, waits, retries).
2. Rank bottlenecks by impact.
3. Propose fixes: parallelize, cache, simplify, batch.
4. Implement highest-impact fix; re-measure.

## Integrations

- `performance-optimizer`
- `parallel-tool-orchestrator`
- `predictive-cache-manager`

## Error Handling

| Failure | Response |
|---------|----------|
| Cannot measure | Add timing logs to next run. |

## Gotchas

- Measure before optimizing; avoid premature parallelization.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
