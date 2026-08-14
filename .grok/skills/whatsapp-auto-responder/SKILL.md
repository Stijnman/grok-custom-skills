---
name: whatsapp-auto-responder
description: "Drafts and optionally sends WhatsApp replies with rater and HITL gates. Use for: auto reply WhatsApp, enable WhatsApp assistant, reply on WhatsApp, `whatsapp-message-rater`."
version: 1.2.0
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

1. Rate incoming message via whatsapp-message-rater.
2. If spam > 7: ignore. If urgency > 8: notify user immediately.
3. Draft reply; run privacy-redactor on draft.
4. If contact auto-mode off or risk medium+: hitl-approver before send.
5. Send and log; respect max 10 auto-replies/hour per contact.

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

- Never auto-reply to financial or legal content.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
