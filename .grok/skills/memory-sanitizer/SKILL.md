---
name: memory-sanitizer
description: "Scores and filters retrieved memory against trust and poisoning risk. Use for: sanitize memory, trust score retrieval, clean knowledge graph, `semantic-memory-manager`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [sanitize memory, trust score retrieval, clean knowledge graph]
    related_skills: [semantic-memory-manager, knowledge-graph-builder, agentic-uncertainty-quantifier]
compatibility: Grok agent; optional MCP and shell access
---
# Memory Sanitizer
## When to Use

- User says **sanitize memory** or task matches this capability
- User says **trust score retrieval** or task matches this capability
- User says **clean knowledge graph** or task matches this capability

## Workflow

1. For each memory entry, score trust 0-10 (source, recency, user-confirmed).
2. Discard entries below 4 unless user explicitly references them.
3. Prefix 4-6 scores with [unverified memory] when citing.
4. Flag contradictions between entries; prefer user-confirmed.

## Integrations

- `semantic-memory-manager`
- `knowledge-graph-builder`
- `agentic-uncertainty-quantifier`

## Error Handling

| Failure | Response |
|---------|----------|
| All entries low trust | Ask user to confirm facts before proceeding. |
| Contradictory memories | Present both; ask user to resolve. |

## Gotchas

- Delegate retrieval to semantic-memory-manager when installed.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
