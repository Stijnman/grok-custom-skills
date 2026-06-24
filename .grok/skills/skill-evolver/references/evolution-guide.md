# Skill Evolution Guide

## 10-dimension rubric (target 40+/50)

| # | Dimension | Fix if below 4 |
|---|-----------|----------------|
| 1 | Frontmatter | Add name, rich description with triggers |
| 2 | Description Quality | Include what + when + trigger keywords |
| 3 | Conciseness | Remove agent-obvious explanations |
| 4 | Structure | Split long content to references/ |
| 5 | Instruction Clarity | Add numbered workflow + examples |
| 6 | Freedom Calibration | Exact steps for fragile ops; defaults elsewhere |
| 7 | Error Handling | Add error table |
| 8 | Progressive Disclosure | Link references/ with when-to-read |
| 9 | Scripts Quality | Add --help, structured output, no prompts |
| 10 | Completeness | Cover everything in description |

## Evolution cycle

1. Backup current file to `versions/<YYYYMMDD-HHMMSS>/SKILL.md`
2. Run hyper-skill-tester baseline; record scores
3. Rewrite dimensions scoring 3 or below only (one pass)
4. Re-test; if overall drops, rollback from versions/
5. Keep last 10 backups; prune older

## Rewrite priorities

1. Description and triggers (biggest impact on skill selection)
2. Workflow steps (biggest impact on execution)
3. Error handling table
4. Integrations (use skills that exist in this repo)

## Version backup naming

```
versions/20260624-120000/SKILL.md
```

Never delete the only backup before a successful re-test.