---
name: whatsapp-auto-responder
description: "Drafts and optionally sends WhatsApp replies with rater and HITL gates. Use for: auto reply WhatsApp, enable WhatsApp assistant, reply on WhatsApp, `whatsapp-message-rater`."
version: 1.2.1
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [auto reply WhatsApp, enable WhatsApp assistant, reply on WhatsApp]
    related_skills: [whatsapp-message-rater, hitl-approver, privacy-redactor, cron-scheduler]
compatibility: Grok agent; optional MCP and shell access
---
# WhatsApp Auto Responder
## When to Use

- User says **auto reply WhatsApp** or task matches this capability
- User says **enable WhatsApp assistant** or task matches this capability
- User says **reply on WhatsApp** or task matches this capability

## Workflow

1. Keep the workflow in draft-only mode unless the user has explicitly enabled auto-mode for the named contact, message category, and time period.
2. Rate an incoming message via whatsapp-message-rater. If spam > 7, do not reply; if urgency > 8, notify the user immediately.
3. Draft a reply and run privacy-redactor on the draft.
4. Before activating, changing, or renewing auto-mode, present the contact scope, exclusions, rate limit, and expiration for explicit user approval.
5. Require hitl-approver before every send outside the approved auto-mode scope, for medium-or-higher risk content, and for financial, legal, sensitive, or ambiguous messages.
6. Send only within the active approved scope and log the outcome; respect a maximum of 10 auto-replies per hour per contact.

## Integrations

- `whatsapp-message-rater`
- `hitl-approver`
- `privacy-redactor`
- `cron-scheduler`

## Error Handling

| Failure | Response |
|---------|----------|
| Rate limit hit | Queue for user review; do not send. |
| Bridge unavailable | Draft only; tell user to send manually. |

## Gotchas

- Never auto-reply to financial, legal, sensitive, or ambiguous content.
- Do not infer contact consent, recipient identity, auto-mode scope, or authorization from prior messages.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
