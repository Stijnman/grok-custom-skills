---
name: waze-live-reports
description: >
  Fetches live Waze traffic incidents and jams for a location. Use for real-ti
  metraffic or user says waze report, live traffic, road incidents. Use when t
  heuser needs this capability. Triggers: waze report, live traffic, road inci
  dents, traffic jams.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [waze report, live traffic, road incidents, traffic jams]
    related_skills: [waze-navigator, traffic-flight-controller, telegram-traffic-reports]
compatibility: Grok agent; optional MCP and shell access
---

# Waze Live Reports

## When to Use

- User says **waze report** or task matches this capability
- User says **live traffic** or task matches this capability
- User says **road incidents** or task matches this capability
- User says **traffic jams** or task matches this capability

## Workflow

1. Resolve location to coordinates or area name.
2. Fetch live incident data via web or API.
3. Summarize: jams, accidents, road closures.
4. Include severity and estimated delay.

## Integrations

- `waze-navigator`
- `traffic-flight-controller`
- `telegram-traffic-reports`

## Error Handling

| Failure | Response |
|---------|----------|
| Location not found | Ask user to clarify or share map link. |

## Gotchas

- Data is third-party; cite source and time.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
