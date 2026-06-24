---
name: beta-unlocker
description: >
  Guides enabling beta or experimental Grok features safely. Use when user ask
  sabout beta features, early access, or unlock experimental tools. Triggers: 
  beta feature, early access, unlock experimental, enable beta.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [beta feature, early access, unlock experimental, enable beta]
    related_skills: [hitl-approver, help]
compatibility: Grok agent; optional MCP and shell access
---

# Beta Unlocker

## When to Use

- User says **beta feature** or task matches this capability
- User says **early access** or task matches this capability
- User says **unlock experimental** or task matches this capability
- User says **enable beta** or task matches this capability

## Workflow

1. Identify requested feature and current environment.
2. Check prerequisites (account tier, settings path, risks).
3. Provide step-by-step enable instructions.
4. Warn about instability; suggest hitl-approver for risky betas.

## Integrations

- `hitl-approver`
- `help`

## Error Handling

| Failure | Response |
|---------|----------|
| Feature unavailable | State requirement; suggest alternatives. |

## Gotchas

- Beta features may change without notice; avoid production deps.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
