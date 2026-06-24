---
name: privacy-redactor
description: >
  Detects and redacts PII in inputs and outputs before external actions. Use w
  hen the user says redact PII, privacy check, or sanitize this. Scans emails,
   phones, names, addresses. Routes high-risk to hitl-approver. Triggers: reda
  ct PII, privacy check, sanitize this, remove personal data.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [redact PII, privacy check, sanitize this, remove personal data]
    related_skills: [hitl-approver, whatsapp-auto-responder, memory-sanitizer]
compatibility: Grok agent; optional MCP and shell access
---

# Privacy Redactor

## When to Use

- User says **redact PII** or task matches this capability
- User says **privacy check** or task matches this capability
- User says **sanitize this** or task matches this capability
- User says **remove personal data** or task matches this capability

## Workflow

1. Scan text for PII patterns: email, phone, SSN, address, full names.
2. Replace with tokens: [EMAIL], [PHONE], [NAME], [ADDRESS].
3. List redactions in summary for user review.
4. If external send requested, run hitl-approver after redaction.

## Integrations

- `hitl-approver`
- `whatsapp-auto-responder`
- `memory-sanitizer`

## Error Handling

| Failure | Response |
|---------|----------|
| Over-redaction | Preserve structure; only redact confirmed PII. |
| Missed PII | Run second pass on capitalized tokens and @ symbols. |

## Gotchas

- Never log raw PII to external services after redaction.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
