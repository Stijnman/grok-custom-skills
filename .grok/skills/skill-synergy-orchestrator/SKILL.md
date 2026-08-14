---
name: skill-synergy-orchestrator
description: "Combines multiple skills into synergistic pipelines. Use for: combine skills, skill pipeline, chain skills, skill synergy."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [combine skills, skill pipeline, chain skills, skill synergy]
    related_skills: [adaptive-workflow-composer, multi-agent-orchestrator, tool-discovery-engine]
compatibility: Grok agent; optional MCP and shell access
---
# Skill Synergy Orchestrator
## When to Use

- User says **combine skills** or task matches this capability
- User says **skill pipeline** or task matches this capability
- User says **chain skills** or task matches this capability
- User says **skill synergy** or task matches this capability

## Workflow

1. Identify skill chain for goal (e.g. research -> synthesize -> verify).
2. Define handoff data between skills.
3. Run pipeline; catch failures at each stage.
4. Tune order based on bottleneck-resolver feedback.

## Integrations

- `adaptive-workflow-composer`
- `multi-agent-orchestrator`
- `tool-discovery-engine`

## Error Handling

| Failure | Response |
|---------|----------|
| Skill missing | Substitute or install via skill-creation-enabler. |

## Gotchas

- privacy-redactor should run before any external-facing skill.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
