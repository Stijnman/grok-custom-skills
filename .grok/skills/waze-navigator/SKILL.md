---
name: waze-navigator
description: >
  Provides navigation guidance using Waze-style routing context. Use for turn-
   by-turn help or user says navigate, waze navigate, directions. Use when the
   user needs this capability. Triggers: navigate, waze navigate, directions, 
  how doI get to.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [navigate, waze navigate, directions, how do I get to]
    related_skills: [waze-live-reports, traffic-flight-controller]
compatibility: Grok agent; optional MCP and shell access
---

# Waze Navigator

## When to Use

- User says **navigate** or task matches this capability
- User says **waze navigate** or task matches this capability
- User says **directions** or task matches this capability
- User says **how do I get to** or task matches this capability

## Workflow

1. Get origin and destination.
2. Fetch routes via waze-live-reports enrichment.
3. Present primary route + one alternate.
4. Update if user reports new incidents.

## Integrations

- `waze-live-reports`
- `traffic-flight-controller`

## Error Handling

| Failure | Response |
|---------|----------|
| Offline | Provide static route; note no live traffic. |

## Gotchas

- Do not distract driver; keep responses concise for voice.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
