---
name: multi-platform-messenger-bridge
description: "Unify WhatsApp, Telegram, and future channels with shared conversation context and message-quality assessment. Use for: bridge messengers, unified chat memory, cross-platform reply, WhatsApp responder."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [bridge messengers, unified chat memory, cross-platform reply]
    related_skills: [whatsapp-auto-responder, whatsapp-message-rater, semantic-memory-manager, hitl-approver]
compatibility: Grok agent; optional MCP and shell access
---
# Multi Platform Messenger Bridge
## When to Use

- User says **bridge messengers** or task matches this capability
- User says **unified chat memory** or task matches this capability
- User says **cross-platform reply** or task matches this capability

## Workflow

1. Normalize message format across platforms (sender, channel, body, meta).
2. Route through whatsapp-message-rater (or platform equivalent).
3. Apply shared contact profile from semantic-memory-manager.
4. Dispatch reply via platform adapter; same HITL rules everywhere.

## References

Read `references/messenger-setup.md` when setup, backends, or rubric details are needed.

## Integrations

- `whatsapp-auto-responder`
- `whatsapp-message-rater`
- `semantic-memory-manager`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Platform not configured | Read references/messenger-setup.md; guide setup. |
| Channel policy mismatch | Apply strictest policy across channels. |

## Gotchas

- Read references/messenger-setup.md before first use.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
