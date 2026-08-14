---
name: internet-enabler
description: "Ensures web access is used effectively for live information. Use for: search web, need internet, look up online, current info."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [search web, need internet, look up online, current info]
    related_skills: [deep-search-enabler, web-scraper, sandbox-internet-handler]
compatibility: Grok agent; optional MCP and shell access
---
# Internet Enabler
## When to Use

- User says **search web** or task matches this capability
- User says **need internet** or task matches this capability
- User says **look up online** or task matches this capability
- User says **current info** or task matches this capability

## Workflow

1. Decide if web search is needed (current events, versions, prices).
2. Formulate specific query; search with citations.
3. Cross-check 2+ sources for critical facts.
4. Summarize with URLs and retrieval date.

## Integrations

- `deep-search-enabler`
- `web-scraper`
- `sandbox-internet-handler`

## Error Handling

| Failure | Response |
|---------|----------|
| Search blocked | Use sandbox-internet-handler fallback. |

## Gotchas

- Prefer WebSearch for facts not in training data.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
