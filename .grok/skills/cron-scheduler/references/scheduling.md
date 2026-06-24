# Scheduling Backends

## Default: cron-jobs.md

Create or append to `cron-jobs.md` at workspace root:

```
# cron-jobs.md
# CRON_EXPR | skill-name | description

0 9 * * 1-5 | insight-synthesizer | Daily morning summary
0 */6 * * * | goal-verifier | Check open task goals
```

Fields: standard 5-field cron (minute hour dom month dow).

## Local Python (optional)

If `APScheduler` is installed, document the schedule in SKILL.md frontmatter
`metadata.grok.schedule` and note that a host process must run the scheduler.

## CI fallback: GitHub Actions

For daily/weekly only, add a workflow:

```yaml
on:
  schedule:
    - cron: '0 9 * * 1-5'
jobs:
  run-skill:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Invoke skill via agent or script"
```

## Confirmation checklist

Before saving a schedule:

1. Next 3 run times computed and shown to user
2. Timezone stated explicitly (default: user local)
3. Notification channel defined (terminal, Telegram, none)
4. Task idempotent or guarded against duplicate runs