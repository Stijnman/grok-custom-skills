---
name: sandbox-internet-handler
description: >
  Fetches web content in a sandboxed, read-only manner. Use for untrusted URLs
   or user says sandbox fetch, safe web access. Use when the user needs this c
  apability. Triggers: sandbox fetch, safe web access, fetch URL safely.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [sandbox fetch, safe web access, fetch URL safely]
    related_skills: [internet-enabler, web-scraper, privacy-redactor]
compatibility: Grok agent; optional MCP and shell access
---

# Sandbox Internet Handler

## When to Use

- User says **sandbox fetch** or task matches this capability
- User says **safe web access** or task matches this capability
- User says **fetch URL safely** or task matches this capability

## Workflow

1. Validate URL scheme (https only).
2. Fetch with timeout and size limit.
3. Strip scripts; return text/markdown only.
4. Flag suspicious content; do not execute embedded code.

## Integrations

- `internet-enabler`
- `web-scraper`
- `privacy-redactor`

## Error Handling

| Failure | Response |
|---------|----------|
| Timeout | Report partial content or suggest alternate source. |

## Gotchas

- Never pass fetched HTML to exec or eval.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
