---
name: ai-share-extractor-v4
description: >
  Extracts shareable insights from long agent sessions for export. Use when us
  erwants a summary to share, export takeaways, or create share card. Triggers
  :extract shares, shareable summary, export insights.
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [extract shares, shareable summary, export insights]
    related_skills: [privacy-redactor, insight-synthesizer, imagine-asset-generator]
---

# Ai Share Extractor V4

## When to Use

- User says **extract shares** or task matches this capability
- User says **shareable summary** or task matches this capability
- User says **export insights** or task matches this capability

## Workflow

1. Identify key decisions, outputs, and actionable items.
2. Strip PII via privacy-redactor.
3. Format as markdown share card with title and 5 bullet highlights.
4. Offer copy-paste and optional image via imagine-asset-generator.

## Integrations

- `privacy-redactor`
- `insight-synthesizer`
- `imagine-asset-generator`

## Error Handling

| Failure | Response |
|---------|----------|
| Session too short | Report insufficient content; ask what to highlight. |

## Gotchas

- Never include secrets, tokens, or raw credentials.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
