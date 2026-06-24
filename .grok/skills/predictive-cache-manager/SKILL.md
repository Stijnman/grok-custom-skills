---
name: predictive-cache-manager
description: >
  Caches frequent tool results and prefetches likely next requests. Use for re
  peated workflows or user says cache results, prefetch. Use when the user nee
  ds this capability. Triggers: cache results, prefetch, reuse cache, avoid re
  peat fetch.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [cache results, prefetch, reuse cache, avoid repeat fetch]
    related_skills: [performance-optimizer, mega-context-manager]
compatibility: Grok agent; optional MCP and shell access
---

# Predictive Cache Manager

## When to Use

- User says **cache results** or task matches this capability
- User says **prefetch** or task matches this capability
- User says **reuse cache** or task matches this capability
- User says **avoid repeat fetch** or task matches this capability

## Workflow

1. Identify repeat queries from session history.
2. Cache with TTL based on data freshness needs.
3. Invalidate on write operations to same resource.
4. Prefetch only high-confidence next steps.

## Integrations

- `performance-optimizer`
- `mega-context-manager`

## Error Handling

| Failure | Response |
|---------|----------|
| Stale cache served | Shorten TTL; add freshness check. |

## Gotchas

- Never cache auth tokens or PII.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
