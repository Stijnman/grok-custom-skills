---
name: compliance-image-guard
description: >
  Checks images for policy compliance before generation or publish. Use before
   sharing images or when user says compliance check, safe image. Use when the
   user needs this capability. Triggers: compliance check, safe image, image p
  olicy,can I publish this.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [compliance check, safe image, image policy, can I publish this]
    related_skills: [safe-image-editor, imagine-asset-generator, hitl-approver]
compatibility: Grok agent; optional MCP and shell access
---

# Compliance Image Guard

## When to Use

- User says **compliance check** or task matches this capability
- User says **safe image** or task matches this capability
- User says **image policy** or task matches this capability
- User says **can I publish this** or task matches this capability

## Workflow

1. Review image prompt or asset for policy risks.
2. Flag: real persons without consent, violence, IP infringement.
3. Block or revise prompt; route edge cases to hitl-approver.
4. Log decision rationale.

## Integrations

- `safe-image-editor`
- `imagine-asset-generator`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Ambiguous policy | Default deny; ask user to confirm. |

## Gotchas

- Real-person likeness requires explicit user confirmation.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
