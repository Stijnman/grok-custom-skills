---
name: deep-search-enabler
description: >
  Enables thorough multi-source research beyond quick answers. Use for complex
   research or user says deep search, comprehensive research. Use when the use
  r needs this capability. Triggers: deep search, comprehensive research, rese
  arch thoroughly.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [deep search, comprehensive research, research thoroughly]
    related_skills: [internet-enabler, web-scraper, insight-synthesizer, agentic-uncertainty-quantifier]
compatibility: Grok agent; optional MCP and shell access
---

# Deep Search Enabler

## When to Use

- User says **deep search** or task matches this capability
- User says **comprehensive research** or task matches this capability
- User says **research thoroughly** or task matches this capability

## Workflow

1. Decompose question into sub-queries.
2. Search web, docs, and workspace in parallel.
3. Synthesize with citations; flag conflicting sources.
4. Score confidence via agentic-uncertainty-quantifier.

## Integrations

- `internet-enabler`
- `web-scraper`
- `insight-synthesizer`
- `agentic-uncertainty-quantifier`

## Error Handling

| Failure | Response |
|---------|----------|
| No sources found | Broaden query; suggest alternate terms. |

## Gotchas

- Cite URLs for factual claims.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
