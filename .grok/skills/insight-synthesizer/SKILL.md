---
name: insight-synthesizer
description: "Synthesizes findings from multiple sources into actionable insights. Use for: synthesize, key takeaways, summarize findings, insight report."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [synthesize, key takeaways, summarize findings, insight report]
    related_skills: [deep-search-enabler, knowledge-graph-builder, ai-share-extractor-v4]
compatibility: Grok agent; optional MCP and shell access
---
# Insight Synthesizer
## When to Use

- User says **synthesize** or task matches this capability
- User says **key takeaways** or task matches this capability
- User says **summarize findings** or task matches this capability
- User says **insight report** or task matches this capability

## Workflow

1. Collect inputs: search results, logs, conversation.
2. Cluster themes; rank by impact and confidence.
3. Output: 3-5 insights, each with evidence and action.
4. Tag uncertainties for agentic-uncertainty-quantifier.

## Integrations

- `deep-search-enabler`
- `knowledge-graph-builder`
- `ai-share-extractor-v4`

## Error Handling

| Failure | Response |
|---------|----------|
| Contradictory sources | Present both sides; do not merge blindly. |

## Gotchas

- Insights must be actionable, not restatements.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
