---
name: persistent-memory-bridge
description: >
  Bridges session memory to persistent storage across conversations. Use when 
  continuity needed or user says remember this, persistent memory. Triggers: r
  emember this, persistent memory, save to memory, recall later.
version: 1.1.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [remember this, persistent memory, save to memory, recall later]
    related_skills: [semantic-memory-manager, memory-sanitizer, user-preference-profiler]
compatibility: Grok agent; optional MCP and shell access
---

# Persistent Memory Bridge

## When to Use

- User says **remember this** or task matches this capability
- User says **persistent memory** or task matches this capability
- User says **save to memory** or task matches this capability
- User says **recall later** or task matches this capability

## Workflow

1. Extract durable facts: preferences, project state, decisions.
2. Run memory-sanitizer before persist.
3. Write to semantic-memory-manager store.
4. Confirm what was saved; offer forget option.

## Integrations

- `semantic-memory-manager`
- `memory-sanitizer`
- `user-preference-profiler`

## Error Handling

| Failure | Response |
|---------|----------|
| Storage full | Prune lowest-trust entries first. |

## Gotchas

- Never persist secrets or credentials.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
