# Security Policy

## Scope

This repository contains agent skill instructions (`SKILL.md` files), not executable
services. Security focus: what agents are instructed to do on user machines.

## Reporting

Open a GitHub issue on [grok-custom-skills](https://github.com/Stijnman/grok-custom-skills)
with the `security` label, or contact the maintainer privately for sensitive reports.

## Design principles

| Principle | Requirement |
|-----------|-------------|
| Defensive default | Read-only inspection unless user explicitly requests changes |
| Human gates | Destructive actions require `hitl-approver` |
| No offense | No exploits, payloads, port scanning beyond localhost inventory, or bypass guidance |
| Privacy | `privacy-redactor` before external share; no PII in handoff docs |
| Consent | No installs, pushes, uploads, or marketplace installs without user approval |
| Transparency | No silent telemetry or auto-rating posts to third-party APIs |

## Skill review before publish

Every skill in `.grok/skills/` must pass:

```bash
python3 .grok/skills/skill-evolver/scripts/validate_skill.py .grok/skills/<name>/SKILL.md
```

Plus manual check for:

1. **Safety & Ethics** section present (session-derived / publishable skills)
2. No hardcoded secrets, tokens, or user-specific home paths
3. No instructions to disable security software or exfiltrate data
4. Accurate description (no capabilities not covered in workflow)
5. Third-party attribution where CLI/tools are referenced

## Supported versions

Skills are reviewed against Grok agent environments with MCP support. Report the
agent platform and skill name when filing issues.

## Out of scope

These skills do not provide:

- Penetration testing or vulnerability exploitation
- Malware, spam, or harassment automation
- Circumvention of authentication or paywalls
- Guaranteed security of third-party marketplace skills (use `skill-rubric-reviewer`)