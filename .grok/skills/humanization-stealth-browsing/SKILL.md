---
name: humanization-stealth-browsing
description: >
  Browses web with human-like patterns to reduce bot detection. Use for scrapi
  ngfragile sites or user says stealth browse, human-like browsing. Use when t
  heuser needs this capability. Triggers: stealth browse, human-like browsing,
   avoid bot detection.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [stealth browse, human-like browsing, avoid bot detection]
    related_skills: [web-scraper, sandbox-internet-handler, humanization-stealth-browsing]
compatibility: Grok agent; optional MCP and shell access
---

# Humanization Stealth Browsing

## When to Use

- User says **stealth browse** or task matches this capability
- User says **human-like browsing** or task matches this capability
- User says **avoid bot detection** or task matches this capability

## Workflow

1. Set realistic delays and headers.
2. Navigate incrementally; avoid burst requests.
3. Rotate user-agent only when site blocks.
4. Respect robots.txt; stop on CAPTCHA and ask user.

## Integrations

- `web-scraper`
- `sandbox-internet-handler`
- `humanization-stealth-browsing`

## Error Handling

| Failure | Response |
|---------|----------|
| CAPTCHA encountered | Stop; ask user to solve manually. |

## Gotchas

- Never bypass paywalls or auth without permission.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
