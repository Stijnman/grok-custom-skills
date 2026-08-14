---
name: skill-collection-bootstrapper
description: "Audits a skills repository, fills gaps, validates SKILL.md files, and instal lsto the user skills directory. Use for: bootstrap skills, complete skill collection, install skill repo, `skill-rubric-reviewer`."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [bootstrap skills, complete skill collection, install skill repo]
    related_skills: [skill-rubric-reviewer, skill-evolver, hitl-approver, goal-verifier]
    publication_reviewed: '2026-06-24'
---
# Skill Collection Bootstrapper
## When to Use

- User says **bootstrap skills** or task matches this capability
- User says **complete skill collection** or task matches this capability
- User says **install skill repo** or task matches this capability

## Workflow

1. Inventory SKILL.md files vs README skill list; report missing names.
2. Run skill-rubric-reviewer on stubs scoring below 30/50.
3. Regenerate or patch weak skills; validate frontmatter and required sections.
4. Show diff summary before install; require user approval to overwrite existing skills.
5. Copy approved skills to ~/.grok/skills/ or workspace .grok/skills/.
6. Update SKILLS_INDEX.md if maintaining a repo.

## Integrations

- `skill-rubric-reviewer`
- `skill-evolver`
- `hitl-approver`
- `goal-verifier`

## Error Handling

| Failure | Response |
|---------|----------|
| Name collision | List conflicts; default to skip unless user approves overwrite. |
| Validation fail | Block install for failed SKILL.md; report path and errors. |

## Gotchas

- Never overwrite bundled skills without explicit user approval.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- User must approve before overwriting installed skills.
- No execution of untrusted scripts from skill folders during bootstrap.
- Validate SKILL.md structure before install.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
