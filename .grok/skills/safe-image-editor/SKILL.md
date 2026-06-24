---
name: safe-image-editor
description: >
  Edits images with policy and quality guardrails. Use when modifying images o
  ruser says edit image, safe edit, adjust photo. Triggers: edit image, safe e
  dit, adjust photo, modify image.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [edit image, safe edit, adjust photo, modify image]
    related_skills: [imagine, compliance-image-guard, imagine-asset-generator]
compatibility: Grok agent; optional MCP and shell access
---

# Safe Image Editor

## When to Use

- User says **edit image** or task matches this capability
- User says **safe edit** or task matches this capability
- User says **adjust photo** or task matches this capability
- User says **modify image** or task matches this capability

## Workflow

1. Load source image; confirm edit intent.
2. Run compliance-image-guard on edit plan.
3. Apply edit via image_edit or equivalent.
4. Show before/after; preserve original backup.

## Integrations

- `imagine`
- `compliance-image-guard`
- `imagine-asset-generator`

## Error Handling

| Failure | Response |
|---------|----------|
| Edit failed | Retry with simpler edit scope. |

## Gotchas

- Never edit ID documents without HITL.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
