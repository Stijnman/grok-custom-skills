---
name: hitl-approver
description: >
  Pauses high-risk actions for explicit human approval. Use before WhatsApp se
  nds, deployments, deletions, credential changes, or financial actions. Trigg
  ers:approve this, hitl check, human review needed. Use when the user needs t
  his capability.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [approve this, hitl check, human review needed, confirm before send]
    related_skills: [whatsapp-auto-responder, privacy-redactor, multi-platform-messenger-bridge]
compatibility: Grok agent; optional MCP and shell access
---

# Hitl Approver

## When to Use

- User says **approve this** or task matches this capability
- User says **hitl check** or task matches this capability
- User says **human review needed** or task matches this capability
- User says **confirm before send** or task matches this capability

## Workflow

1. Classify action: message / deploy / delete / financial / credential.
2. Present briefing: summary, risk (low/medium/high), rollback plan.
3. Wait for explicit approval (yes / approve / go ahead).
4. On approval, execute and confirm outcome. On denial, abort and suggest safer path.

## Output Template

```
HITL Required: {type}
Summary: {summary}
Risk: {level}
Rollback: {plan}
Approve? (yes/no)
```

## Integrations

- `whatsapp-auto-responder`
- `privacy-redactor`
- `multi-platform-messenger-bridge`

## Error Handling

| Failure | Response |
|---------|----------|
| Ambiguous approval | Re-ask; never infer consent from silence. |
| Timeout in session | Defer action; remind user once. |
| User says no | Abort; log reason; offer alternative. |

## Gotchas

- Medium+ risk always requires HITL even if user seems hurried.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
