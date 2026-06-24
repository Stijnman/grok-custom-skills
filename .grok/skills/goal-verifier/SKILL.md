---
name: goal-verifier
description: >
  Verifies task completion against stated goals before marking work done. Usew
  hen the user asks to verify success, confirm completion, or says 'did Iachie
  ve this'. Runs checks + optional self-refine pass. Triggers: verify goal,con
  firm success, did I achieve this.
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [verify goal, confirm success, did I achieve this, check if done]
    related_skills: [self-refine-loop, auto-tester]
---

# Goal Verifier

## When to Use

- User says **verify goal** or task matches this capability
- User says **confirm success** or task matches this capability
- User says **did I achieve this** or task matches this capability
- User says **check if done** or task matches this capability

## Workflow

1. Restate the original goal in one sentence.
2. List acceptance criteria (explicit or inferred from conversation).
3. Check each criterion: pass / fail / partial with evidence.
4. If any fail, invoke self-refine-loop or report gaps.
5. Only mark complete when all critical criteria pass.

## Integrations

- `self-refine-loop`
- `auto-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| Goal undefined | Ask user to confirm goal before verifying. |
| False positive risk | Require evidence (file path, command output, or test result). |

## Gotchas

- Verification is read-only; do not mutate artifacts during checks.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
