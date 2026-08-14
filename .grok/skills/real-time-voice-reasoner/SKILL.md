---
name: real-time-voice-reasoner
description: "Handles real-time voice input with low-latency reasoning. Use for: voice mode, speak and reason, voice assistant, listen."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [voice mode, speak and reason, voice assistant, listen]
    related_skills: [voice-think-fast-handler, voice-synthesis-handler]
compatibility: Grok agent; optional MCP and shell access
---
# Real Time Voice Reasoner
## When to Use

- User says **voice mode** or task matches this capability
- User says **speak and reason** or task matches this capability
- User says **voice assistant** or task matches this capability
- User says **listen** or task matches this capability

## Workflow

1. Transcribe or receive voice input stream.
2. Apply voice-think-fast-handler for quick ack.
3. Reason on full utterance; respond concisely for TTS.
4. Confirm ambiguous commands verbally.

## Integrations

- `voice-think-fast-handler`
- `voice-synthesis-handler`

## Error Handling

| Failure | Response |
|---------|----------|
| Poor transcription | Ask user to repeat once. |

## Gotchas

- Voice confirmations for destructive actions.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
