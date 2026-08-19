---
name: telegram-traffic-reports
description: "Fetches and reports traffic conditions via Telegram bot format. Use for: telegram traffic, traffic report Telegram, commute alert, `waze-live-reports`."
version: 1.2.1
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

1. Get the user-approved location or route and clarify whether the request is for a draft, a one-time send, or a recurring alert.
2. Fetch traffic via waze-live-reports or traffic-flight-controller.
3. Format a concise Telegram message with delays and incidents; keep it as a draft by default.
4. Obtain explicit approval before sending to a named chat or enabling any recurring alert. Route scheduling through cron-scheduler only after its separate approval gate is satisfied.

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

- Rate limit approved Telegram sends to 1/min per chat.
- Do not infer a recipient, enable a bot, or create a recurring alert from route data alone.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
