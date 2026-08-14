---
name: auto-tester
description: "Runs validation tests on code, skills, or outputs after changes. Use for: run tests, auto test, validate changes, check tests."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [run tests, auto test, validate changes, check tests]
    related_skills: [goal-verifier, self-healing-error-recovery, hyper-skill-tester]
compatibility: Grok agent; optional MCP and shell access
---
# Auto Tester
## When to Use

- User says **run tests** or task matches this capability
- User says **auto test** or task matches this capability
- User says **validate changes** or task matches this capability
- User says **check tests** or task matches this capability

## Workflow

1. Detect project type (Python, Node, skill-only).
2. Run appropriate test command (pytest, npm test, or skill checklist).
3. Parse results; classify pass/fail/flaky.
4. On fail: invoke self-healing-error-recovery or report with fix hints.

## Integrations

- `goal-verifier`
- `self-healing-error-recovery`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| No test suite | Run smoke checks: import, lint, dry-run. |

## Gotchas

- Never skip tests before marking goal-verifier complete.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
