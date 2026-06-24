---
name: traffic-flight-controller
description: >
  Coordinates traffic and navigation data sources for optimal routing info. Us
  efor commute planning or user says traffic route, best route now. Use when t
  heuser needs this capability. Triggers: traffic route, best route now, commu
  te plan, drive time.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [traffic route, best route now, commute plan, drive time]
    related_skills: [waze-live-reports, waze-navigator, telegram-traffic-reports]
compatibility: Grok agent; optional MCP and shell access
---

# Traffic Flight Controller

## When to Use

- User says **traffic route** or task matches this capability
- User says **best route now** or task matches this capability
- User says **commute plan** or task matches this capability
- User says **drive time** or task matches this capability

## Workflow

1. Query waze-live-reports and waze-navigator.
2. Merge incidents, ETA, alternate routes.
3. Rank routes by time and reliability.
4. Present recommendation with confidence.

## Integrations

- `waze-live-reports`
- `waze-navigator`
- `telegram-traffic-reports`

## Error Handling

| Failure | Response |
|---------|----------|
| No route data | Fallback to straight-line estimate; note limitation. |

## Gotchas

- Traffic data may be stale; show retrieval time.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
