---
name: voice-think-fast-handler
description: "Provides quick acknowledgment during voice latency gaps. Use for: quick ack, thinking aloud, fast think, voice ack."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [quick ack, thinking aloud, fast think, voice ack]
    related_skills: [real-time-voice-reasoner, voice-synthesis-handler]
compatibility: Grok agent; optional MCP and shell access
---
# Voice Think Fast Handler
## When to Use

- User says **quick ack** or task matches this capability
- User says **thinking aloud** or task matches this capability
- User says **fast think** or task matches this capability
- User says **voice ack** or task matches this capability

## Workflow

1. On voice input received, emit brief ack ('Got it, checking...').
2. Continue full reasoning in background.
3. Deliver complete response when ready.
4. Avoid over-use; max one ack per 10 seconds.

## Integrations

- `real-time-voice-reasoner`
- `voice-synthesis-handler`

## Error Handling

| Failure | Response |
|---------|----------|
| Double ack | Suppress duplicate acks in same turn. |

## Gotchas

- Acks must not promise outcomes prematurely.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
