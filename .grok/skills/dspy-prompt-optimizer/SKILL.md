---
name: dspy-prompt-optimizer
description: "Tunes prompts iteratively using reflection and success metrics. Use for: optimize this prompt, dspy tune, improve prompt with reflection, `self-refine-loop`."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [optimize this prompt, dspy tune, improve prompt with reflection]
    related_skills: [self-refine-loop, auto-tester, hyper-skill-tester]
compatibility: Grok agent; optional MCP and shell access
---
# DSPy Prompt Optimizer
## When to Use

- User says **optimize this prompt** or task matches this capability
- User says **dspy tune** or task matches this capability
- User says **improve prompt with reflection** or task matches this capability

## Workflow

1. Capture baseline prompt and 2-3 example inputs with desired outputs.
2. Run baseline; score outputs against criteria.
3. Generate 3 prompt variants addressing failures.
4. Test variants; pick best by score.
5. Return optimized prompt with before/after metrics.

## Integrations

- `self-refine-loop`
- `auto-tester`
- `hyper-skill-tester`

## Error Handling

| Failure | Response |
|---------|----------|
| No examples | Ask for 2 input/output pairs minimum. |
| Overfitting one example | Require 3+ diverse examples. |

## Gotchas

- Keep prompt under 2000 tokens unless user needs longer.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
