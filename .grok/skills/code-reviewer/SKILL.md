---
name: code-reviewer
description: >
  Reviews code changes for bugs, style, security, and maintainability. Use aft
  erwriting code or when user says review code, code review, check my PR. Trig
  gers: review code, code review, check my changes. Use when the user needs th
  is capability.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [review code, code review, check my PR, review my changes]
    related_skills: [auto-tester, goal-verifier, self-refine-loop]
compatibility: Grok agent; optional MCP and shell access
---

# Code Reviewer

## When to Use

- User says **review code** or task matches this capability
- User says **code review** or task matches this capability
- User says **check my PR** or task matches this capability
- User says **review my changes** or task matches this capability

## Workflow

1. Read diff or changed files; understand intent.
2. Check: correctness, edge cases, security, tests, style.
3. Categorize findings: critical / major / minor / nit.
4. Suggest concrete fixes with file:line references.

## Integrations

- `auto-tester`
- `goal-verifier`
- `self-refine-loop`

## Error Handling

| Failure | Response |
|---------|----------|
| No diff available | Ask user for files or git diff. |

## Gotchas

- Critical security issues block merge recommendation.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
