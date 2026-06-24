---
name: session-handoff-packager
description: >
  Packages session work into a local handoff document for continuity. Use when
  saving progress or user says session summary, handoff, what we did. Triggers
  :session summary, handoff, save what we did.
version: 1.0.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [session summary, handoff, save what we did, continue next time]
    related_skills: [privacy-redactor, ai-share-extractor-v4, goal-verifier]
    publication_reviewed: '2026-06-24'
---

# Session Handoff Packager

## When to Use

- User says **session summary** or task matches this capability
- User says **handoff** or task matches this capability
- User says **save what we did** or task matches this capability
- User says **continue next time** or task matches this capability

## Workflow

1. List: repos explored, commands run, files created/changed, key findings.
2. Note open items and recommended next steps.
3. Run privacy-redactor on content before any external share.
4. Write session-handoff.md to workspace (local only by default).
5. Do not include secrets, tokens, or raw PII in handoff.

## Integrations

- `privacy-redactor`
- `ai-share-extractor-v4`
- `goal-verifier`

## Error Handling

| Failure | Response |
|---------|----------|
| Workspace not writable | Output handoff in chat only. |

## Gotchas

- Default is local file only; upload requires separate user request.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- PII redaction before share; secrets never included.
- Handoff stays in user workspace unless explicitly shared.
- Read-only summary of past actions; no new destructive operations.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
