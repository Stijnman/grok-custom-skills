---
name: mega-context-manager
description: "Manages large context windows via chunking, summarization, and retrieval. Use for: manage context, too much context, chunk document, context budget."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [manage context, too much context, chunk document, context budget]
    related_skills: [semantic-memory-manager, predictive-cache-manager, persistent-memory-bridge]
compatibility: Grok agent; optional MCP and shell access
---
# Mega Context Manager
## When to Use

- User says **manage context** or task matches this capability
- User says **too much context** or task matches this capability
- User says **chunk document** or task matches this capability
- User says **context budget** or task matches this capability

## Workflow

1. Measure token estimate of inputs.
2. If over budget: chunk, summarize chunks, index.
3. Retrieve relevant chunks per subtask only.
4. Drop stale chunks after task completion.

## Integrations

- `semantic-memory-manager`
- `predictive-cache-manager`
- `persistent-memory-bridge`

## Error Handling

| Failure | Response |
|---------|----------|
| Retrieval miss | Expand query; include adjacent chunks. |

## Gotchas

- Summaries lose detail; keep raw chunks for citation.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
