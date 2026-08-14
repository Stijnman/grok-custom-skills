---
name: self-healing-error-recovery
description: "Diagnoses failures and retries with alternate strategies. Use for: heal this error, self recover, fix failure automatically, retry smart."
version: 1.2.0
author: Stijnman
license: MIT
metadata:
  grok:
    tags: [heal this error, self recover, fix failure automatically, retry smart]
    related_skills: [knowledge-graph-builder, semantic-memory-manager, bottleneck-resolver]
compatibility: Grok agent; optional MCP and shell access
---
# Self Healing Error Recovery
## When to Use

- User says **heal this error** or task matches this capability
- User says **self recover** or task matches this capability
- User says **fix failure automatically** or task matches this capability
- User says **retry smart** or task matches this capability

## Workflow

1. Capture error message, command, and environment context.
2. Classify: transient / config / permission / logic / dependency.
3. Try up to 3 recovery strategies (retry, alternate path, dependency fix).
4. If recovered, summarize fix. If not, escalate with diagnosis.
5. Record lesson: error pattern -> successful fix.

## Integrations

- `knowledge-graph-builder`
- `semantic-memory-manager`
- `bottleneck-resolver`

## Error Handling

| Failure | Response |
|---------|----------|
| Destructive command failed | Do not auto-retry deletes; require HITL. |
| Same error 3x | Stop retrying; report root cause. |
| Permission denied | Never escalate privileges; ask user. |

## Gotchas

- Read-only diagnosis first; mutate only after classification.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
