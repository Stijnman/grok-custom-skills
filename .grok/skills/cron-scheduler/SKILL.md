---
name: cron-scheduler
description: "Schedules recurring or delayed agent tasks. Use for: schedule this, run daily, cron job, set timer."
version: 1.2.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [schedule this, run daily, cron job, set timer, every morning]
    related_skills: [insight-synthesizer, goal-verifier]
---
# Cron Scheduler
## When to Use

- User says **schedule this** or task matches this capability
- User says **run daily** or task matches this capability
- User says **cron job** or task matches this capability
- User says **set timer** or task matches this capability
- User says **every morning** or task matches this capability

## Workflow

1. Parse schedule expression (cron, interval, or natural language).
2. Write entry to workspace cron-jobs.md (default) or document GitHub Action.
3. Define task: skill to invoke, args, and notification channel.
4. Confirm next 3 run times with user.
5. On trigger, execute task and log via insight-synthesizer.

## References

Read `references/scheduling.md` when setup, backends, or rubric details are needed.

## Integrations

- `insight-synthesizer`
- `goal-verifier`

## Error Handling

| Failure | Response |
|---------|----------|
| Invalid cron | Show valid example: 0 9 * * 1-5 (weekdays 9am). |
| No workspace write access | Output schedule as copy-paste block only. |

## Gotchas

- Read references/scheduling.md for backend options.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow with integrations invoked as needed.
