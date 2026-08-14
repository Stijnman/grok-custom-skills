---
name: knowledge-graph-builder
description: "Builds structured knowledge graphs from text and sessions. Use for: knowledge graph, map entities, build graph, entity map."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [knowledge graph, map entities, build graph, entity map]
    related_skills: [semantic-memory-manager, insight-synthesizer, self-healing-error-recovery]
compatibility: Grok agent; optional MCP and shell access
---
# Knowledge Graph Builder
## When to Use

- User says **knowledge graph** or task matches this capability
- User says **map entities** or task matches this capability
- User says **build graph** or task matches this capability
- User says **entity map** or task matches this capability

## Workflow

1. Extract entities: people, tools, projects, concepts.
2. Define relations: uses, depends_on, blocks, produces.
3. Output JSON graph or mermaid diagram.
4. Store index in semantic-memory-manager.

## Integrations

- `semantic-memory-manager`
- `insight-synthesizer`
- `self-healing-error-recovery`

## Error Handling

| Failure | Response |
|---------|----------|
| Too many entities | Cluster; show top 20 with expand option. |

## Gotchas

- Graphs are hypotheses; mark unverified edges.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
