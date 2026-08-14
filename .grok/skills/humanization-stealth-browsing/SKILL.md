---
name: humanization-stealth-browsing
description: "Apply respectful, rate-limited browsing practices for public websites while honoring site rules and access controls. Use for: responsible web research, rate limiting, CAPTCHA stop, robots.txt."
version: 1.2.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional browser and shell access
metadata:
  grok:
    tags: [responsible browsing, rate limiting, public web research, robots.txt, CAPTCHA stop]
    related_skills: [web-scraper, sandbox-internet-handler]
---

# Responsible Web Browsing

## When to Use

Use this skill when collecting information from public websites requires careful pacing, stable navigation, or respect for fragile endpoints. It supports responsible research, not bypassing protections.

> Do not use this skill to evade bot detection, bypass access controls, defeat CAPTCHAs, circumvent paywalls, or access content that the user is not authorized to view.

## Workflow

1. Confirm that the target is public and that the requested collection is legitimate.
2. Prefer official APIs, published feeds, or a site’s documented export options.
3. Review and respect applicable terms, `robots.txt`, rate limits, and access restrictions.
4. Make requests incrementally, cache results where appropriate, and avoid unnecessary retries.
5. If a login wall, CAPTCHA, paywall, or block appears, stop and explain the limitation to the user.

## Operating Principles

| Principle | Practice |
|---|---|
| Minimize load | Use measured request rates and avoid broad, repetitive crawling. |
| Preserve provenance | Record source URLs and retrieval dates for material findings. |
| Respect controls | Do not rotate identities, automate CAPTCHA solving, or bypass authentication. |
| Fail safely | Stop rather than escalating when a site signals restricted access. |

## Error Handling

| Situation | Response |
|---|---|
| Rate limit or temporary block | Pause activity and offer a slower or official-data-source alternative. |
| CAPTCHA or login wall | Stop the automated flow; ask the user to provide authorized access if appropriate. |
| `robots.txt` or terms restrict collection | Do not scrape the restricted path; propose permitted alternatives. |
| Source data is incomplete | State the limitation and avoid filling gaps with assumptions. |
