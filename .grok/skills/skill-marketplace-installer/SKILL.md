---
name: skill-marketplace-installer
description: >
  Safely searches and installs agent skills from public marketplaces (e.g.agen
  tskill.sh) with user consent and security checks. Use when user says findski
  ll, install skill from marketplace, /learn. Triggers: find skill, installski
  ll, skill marketplace, check skill safety.
version: 1.0.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [find skill, install skill, skill marketplace, check skill safety]
    related_skills: [skill-rubric-reviewer, hitl-approver, privacy-redactor]
    publication_reviewed: '2026-06-24'
---

# Skill Marketplace Installer

## When to Use

- User says **find skill** or task matches this capability
- User says **install skill** or task matches this capability
- User says **skill marketplace** or task matches this capability
- User says **check skill safety** or task matches this capability

## Workflow

1. Search marketplace via documented CLI (npx @agentskill.sh/cli search).
2. Show skill name, owner, description, and ratings before install.
3. Require explicit user approval before install.
4. Run security scan if CLI supports it; warn on suspicious patterns.
5. Install to user skills directory; list what was added.
6. Never install skills requesting credentials in SKILL.md without user review.

## Integrations

- `skill-rubric-reviewer`
- `hitl-approver`
- `privacy-redactor`

## Error Handling

| Failure | Response |
|---------|----------|
| CLI unavailable | Document manual install from source URL with rubric review first. |
| Scan flags risk | Block install; explain finding; offer alternatives. |

## Gotchas

- Third-party skills are untrusted until reviewed with skill-rubric-reviewer.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- User consent required before every install.
- Recommends security scan before install when available.
- Attributes agentskill.sh CLI; does not bundle proprietary marketplace code.
- No silent telemetry or auto-rating posts in this skill.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

### Attribution

- Compatible with agentskill.sh CLI; marketplace terms apply to installed skills.

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
