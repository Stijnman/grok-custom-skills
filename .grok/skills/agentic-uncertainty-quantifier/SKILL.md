---
name: agentic-uncertainty-quantifier
description: >
  Scores task uncertainty to calibrate memory depth and iteration count. Use w
  hen stakes are high, facts are sparse, or user says quantify uncertainty, fa
  st slow think, uncertainty score. Triggers: quantify uncertainty, fast slow 
  think,uncertainty score, how sure.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [quantify uncertainty, fast slow think, uncertainty score, how sure]
    related_skills: [self-refine-loop, semantic-memory-manager, deep-search-enabler]
compatibility: Grok agent; optional MCP and shell access
---

# Agentic Uncertainty Quantifier

## When to Use

- User says **quantify uncertainty** or task matches this capability
- User says **fast slow think** or task matches this capability
- User says **uncertainty score** or task matches this capability
- User says **how sure** or task matches this capability

## Workflow

1. Score epistemic uncertainty 0-10 (how much is unknown).
2. Score procedural uncertainty 0-10 (how clear are the steps).
3. High epistemic (>6): retrieve more context, run self-refine-loop.
4. Low procedural (<4): ask clarifying questions before acting.
5. Report scores and recommended depth to user.

## Integrations

- `self-refine-loop`
- `semantic-memory-manager`
- `deep-search-enabler`

## Error Handling

| Failure | Response |
|---------|----------|
| False confidence | Bias toward caution on destructive tasks. |

## Gotchas

- Uncertainty > 7 on financial/deploy actions triggers hitl-approver.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
