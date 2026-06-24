---
name: telegram-traffic-reports
description: >
  Fetches and reports traffic conditions via Telegram bot format. Use for comm
  ute updates or user says telegram traffic, traffic report Telegram. Use when
   theuser needs this capability. Triggers: telegram traffic, traffic report T
  elegram, commute alert.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [telegram traffic, traffic report Telegram, commute alert]
    related_skills: [waze-live-reports, traffic-flight-controller, cron-scheduler, multi-platform-messenger-bridge]
compatibility: Grok agent; optional MCP and shell access
---

# Telegram Traffic Reports

## When to Use

- User says **telegram traffic** or task matches this capability
- User says **traffic report Telegram** or task matches this capability
- User says **commute alert** or task matches this capability

## Workflow

1. Get user location or route.
2. Fetch traffic via waze-live-reports or traffic-flight-controller.
3. Format concise Telegram message with delays and incidents.
4. Optionally schedule via cron-scheduler.

## Integrations

- `waze-live-reports`
- `traffic-flight-controller`
- `cron-scheduler`
- `multi-platform-messenger-bridge`

## Error Handling

| Failure | Response |
|---------|----------|
| Location missing | Ask for origin/destination. |

## Gotchas

- Rate limit Telegram sends to 1/min per chat.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
