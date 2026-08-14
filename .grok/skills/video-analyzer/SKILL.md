---
name: video-analyzer
description: "Analyzes video content for scenes, text, and summaries. Use for: analyze video, what's in this video, video summary, review video."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [analyze video, what's in this video, video summary, review video]
    related_skills: [insight-synthesizer, compliance-image-guard]
compatibility: Grok agent; optional MCP and shell access
---
# Video Analyzer
## When to Use

- User says **analyze video** or task matches this capability
- User says **what's in this video** or task matches this capability
- User says **video summary** or task matches this capability
- User says **review video** or task matches this capability

## Workflow

1. Load video or URL; check size limits.
2. Extract key frames or use video review tools.
3. Summarize: scenes, spoken content, on-screen text.
4. Output timestamped highlights.

## Integrations

- `insight-synthesizer`
- `compliance-image-guard`

## Error Handling

| Failure | Response |
|---------|----------|
| File too large | Analyze first 5 minutes only; ask to trim. |

## Gotchas

- Run compliance check before publishing video-derived content.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
