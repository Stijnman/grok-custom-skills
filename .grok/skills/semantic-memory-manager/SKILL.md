---
name: semantic-memory-manager
description: >
  Stores and retrieves semantic memory with embeddings and tags. Use for long-
   term recall or user says semantic memory, search memory, recall. Use when t
  he user needs this capability. Triggers: semantic memory, search memory, rec
  all, store memory.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [semantic memory, search memory, recall, store memory]
    related_skills: [memory-sanitizer, persistent-memory-bridge, knowledge-graph-builder]
compatibility: Grok agent; optional MCP and shell access
---

# Semantic Memory Manager

## When to Use

- User says **semantic memory** or task matches this capability
- User says **search memory** or task matches this capability
- User says **recall** or task matches this capability
- User says **store memory** or task matches this capability

## Workflow

1. On store: chunk, tag, score initial trust 5.
2. On retrieve: query by semantic similarity + tags.
3. Run memory-sanitizer on all retrievals.
4. Prune entries older than 90d with trust < 3.

## Integrations

- `memory-sanitizer`
- `persistent-memory-bridge`
- `knowledge-graph-builder`

## Error Handling

| Failure | Response |
|---------|----------|
| No match | Broaden query; suggest manual tags. |

## Gotchas

- Central memory hub for messenger and healing skills.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
