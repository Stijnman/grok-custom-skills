---
name: whatsapp-message-rater
description: >
  Rates WhatsApp messages for sentiment, urgency, and spam likelihood. Use bef
  ore auto-reply decisions or when user says rate this WhatsApp, analyze chat 
  sentiment, score message urgency. Use when the user needs this capability. T
  riggers: rate this WhatsApp, analyze chat sentiment, score message urgency.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [rate this WhatsApp, analyze chat sentiment, score message urgency]
    related_skills: [whatsapp-auto-responder, privacy-redactor, multi-platform-messenger-bridge]
compatibility: Grok agent; optional MCP and shell access
---

# Whatsapp Message Rater

## When to Use

- User says **rate this WhatsApp** or task matches this capability
- User says **analyze chat sentiment** or task matches this capability
- User says **score message urgency** or task matches this capability

## Workflow

1. Parse message: sender, text, timestamp, attachments.
2. Score sentiment (-1 to 1), urgency (0-10), spam (0-10).
3. Output JSON summary plus one-line recommendation.
4. Update per-contact profile if memory available.

## Output Template

```
{"sentiment": 0.0, "urgency": 0, "spam": 0, "recommendation": ""}
```

## Integrations

- `whatsapp-auto-responder`
- `privacy-redactor`
- `multi-platform-messenger-bridge`

## Error Handling

| Failure | Response |
|---------|----------|
| Empty message | Return neutral scores; flag as no-content. |
| PII in message | Run privacy-redactor before storing profile. |

## Gotchas

- Spam score > 7: never auto-reply; flag for user.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
