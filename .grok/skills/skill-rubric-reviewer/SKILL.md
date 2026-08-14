---
name: skill-rubric-reviewer
description: "Reviews SKILL.md files against a 10-dimension quality rubric inspired by the Agent Skills specification. Use for: review skill, skill rubric, audit SKILL.md, score skill quality."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [review skill, skill rubric, audit SKILL.md, score skill quality]
    related_skills: [skill-evolver, hyper-skill-tester, privacy-redactor]
    publication_reviewed: '2026-06-24'
---
# Skill Rubric Reviewer
## When to Use

- User says **review skill** or task matches this capability
- User says **skill rubric** or task matches this capability
- User says **audit SKILL.md** or task matches this capability
- User says **score skill quality** or task matches this capability


## Pre-publish validation loop

Run before publishing any skill:

```bash
python3 scripts/check_no_private_data.py
python3 scripts/publish_safety_check.py
python3 scripts/optimize_all_skills.py --validate-only
```

- [ ] `skills-ref` validation passes
- [ ] Description includes *what*, *when*, and *Triggers*
- [ ] No private emails, paths, or LAN IPs
- [ ] `hitl-approver` referenced for destructive ops

## Workflow

1. Read SKILL.md and any references/, scripts/, assets/.
2. Score 10 dimensions (frontmatter, description, conciseness, structure, clarity, freedom, errors, disclosure, scripts, completeness) 1-5 each.
3. List issues for dimensions scoring 3 or below.
4. Provide before/after rewrite suggestions; apply only if user requests.
5. Flag publication blockers: secrets, harmful instructions, undeclared telemetry, PII in logs.

## Integrations

- `skill-evolver`
- `hyper-skill-tester`
- `privacy-redactor`

## Error Handling

| Failure | Response |
|---------|----------|
| Missing SKILL.md | Report path; do not score directory without file. |

## Gotchas

- Rubric inspired by Agent Skills spec; independent implementation.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Reviews content for safety before publish; blocks skills with harmful instructions.
- No automatic submission of reviews to external services without user consent.
- Does not exfiltrate skill contents to third parties.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

### Attribution

- Rubric aligned with Agent Skills spec best practices; original skill text.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
