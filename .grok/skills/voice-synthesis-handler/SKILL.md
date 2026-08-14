---
name: voice-synthesis-handler
description: "Converts agent responses to natural speech output. Use for: speak response, text to speech, voice output, read aloud."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [speak response, text to speech, voice output, read aloud]
    related_skills: [real-time-voice-reasoner, voice-think-fast-handler]
compatibility: Grok agent; optional MCP and shell access
---
# Voice Synthesis Handler
## When to Use

- User says **speak response** or task matches this capability
- User says **text to speech** or task matches this capability
- User says **voice output** or task matches this capability
- User says **read aloud** or task matches this capability

## Workflow

1. Format response for spoken delivery (short sentences).
2. Strip markdown and code blocks for TTS.
3. Invoke TTS; confirm audio output path or stream.
4. Offer shorter summary if text exceeds 30 seconds speech.

## Integrations

- `real-time-voice-reasoner`
- `voice-think-fast-handler`

## Error Handling

| Failure | Response |
|---------|----------|
| TTS unavailable | Return text with speakable formatting note. |

## Gotchas

- Never speak secrets or OTP codes aloud.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
