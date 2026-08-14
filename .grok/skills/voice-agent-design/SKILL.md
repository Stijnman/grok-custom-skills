---
name: voice-agent-design
description: "Design a safe, vendor-neutral voice agent with conversation flows, consent notices, escalation paths, and approval-gated actions. Use for: voice agent design, phone assistant, call flow, conversational IVR."
license: MIT
metadata:
  version: 1.0.0
  author: Stijnman
  grok:
    tags: [voice agent design, phone assistant, call flow, conversational IVR]
---

# Voice Agent Design

## Purpose

Design a voice-agent specification that is concise, understandable, and safe for callers. The skill is vendor-neutral and does not assume a specific telephony or model provider.

## Workflow

1. Define the agent’s purpose, audience, supported tasks, and explicit exclusions.
2. Draft a short conversation flow: greeting, disclosure where appropriate, intent capture, information gathering, resolution, confirmation, and close.
3. Identify sensitive data, recording notices, retention rules, and a path to a human representative.
4. List every external action, such as booking, messaging, payment, or account change, and require explicit confirmation immediately before it occurs.
5. Define failure handling for uncertainty, silence, interruption, bad transfer, and urgent or sensitive topics.
6. Write a test plan covering normal, ambiguous, adversarial, and escalation calls.

## Safety boundaries

Obtain explicit consent before voice cloning a real person. Do not imitate a person without authorization, conceal an AI identity where disclosure is required, or make promises the system cannot verify. Keep recordings and transcripts to the minimum authorized scope.

## Error handling

| Situation | Response |
|---|---|
| Intent remains unclear | Ask one concise clarification, then offer human handoff. |
| Caller requests a consequential action | Restate scope and obtain confirmation before acting. |
| Sensitive or emergency topic arises | Follow the approved escalation path; do not improvise advice. |
| Tool or knowledge source fails | State the limitation, avoid guessing, and offer a safe alternative. |
