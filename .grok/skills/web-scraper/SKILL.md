---
name: web-scraper
description: "Extracts structured data from web pages. Use for: scrape page, extract from website, get page data, web extract."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [scrape page, extract from website, get page data, web extract]
    related_skills: [sandbox-internet-handler, humanization-stealth-browsing, internet-enabler]
compatibility: Grok agent; optional MCP and shell access
---
# Web Scraper
## When to Use

- User says **scrape page** or task matches this capability
- User says **extract from website** or task matches this capability
- User says **get page data** or task matches this capability
- User says **web extract** or task matches this capability

## Workflow

1. Fetch via sandbox-internet-handler or WebFetch.
2. Parse HTML to text, tables, or JSON per user spec.
3. Respect robots.txt and rate limits.
4. Return data with source URL and timestamp.

## Integrations

- `sandbox-internet-handler`
- `humanization-stealth-browsing`
- `internet-enabler`

## Error Handling

| Failure | Response |
|---------|----------|
| Blocked by site | Try stealth mode or ask user for export. |

## Gotchas

- Never scrape authenticated pages without user session.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
