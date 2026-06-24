---
name: self-refine-loop
description: >
  Runs a generator-critique-reviser loop to iteratively improve agent outputs.
  Use when the user asks to refine, critique, or improve a draft, or mentionss
  elf-refine, reflexion, or iterative revision. Stops at 5 iterations orconfid
  ence 8/10. Triggers: self refine, reflexion loop, critique and revise.
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [self refine, reflexion loop, critique and revise, improve output]
    related_skills: [goal-verifier, agentic-uncertainty-quantifier, dspy-prompt-optimizer]
---

# Self Refine Loop

## When to Use

- User says **self refine** or task matches this capability
- User says **reflexion loop** or task matches this capability
- User says **critique and revise** or task matches this capability
- User says **improve output** or task matches this capability

## Workflow

1. Capture the current output and the user's quality criteria.
2. Generate a critique listing specific weaknesses (max 5 bullets).
3. Revise the output addressing every critique point.
4. Score confidence 0-10 on whether criteria are met.
5. Repeat until confidence >= 8 or 5 iterations; return best version with changelog.

## Integrations

- `goal-verifier`
- `agentic-uncertainty-quantifier`
- `dspy-prompt-optimizer`

## Error Handling

| Failure | Response |
|---------|----------|
| No criteria given | Ask user for 1-3 success criteria before looping. |
| Confidence stuck below 5 | Stop early; report blocker and ask for guidance. |
| Output grows unbounded | Cap revisions to prior length + 20%. |

## Gotchas

- Do not loop on trivial typos; one-pass fix is enough.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
