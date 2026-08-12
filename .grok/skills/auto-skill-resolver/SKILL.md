---
name: auto-skill-resolver
description: Central gatekeeper that analyzes any prompt, finds or creates the needed skill, then forces full persistence (Memory + Google Drive + GitHub) and continuous library improvement. Enforces version control, clarity upgrades, and external downloads. Triggered by capability gaps, research requests, or "improve the skills".
---

# Auto Skill Resolver v2.2

## Purpose
Make the skill library self-improving, always-persisted, and clear.

## Non-Negotiable Persistence Pipeline
When any skill is created or improved:

1. Write/update local SKILL.md + CHANGELOG.md + versions/ snapshot
2. Record in Persistent Memory
3. Package and upload to Google Drive folder `Grok Skills Library` (ID: 1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK)
4. Push to GitHub `Stijnman/grok-custom-skills` under `.grok/skills/`
5. Update master SKILLS_INDEX.md
6. Log to evolution_log.md

## Research & Improvement Mode (activated by this request)
When asked to research/improve existing skills:

1. Inventory all skills
2. Detect clarity problems (long descriptions, missing "When not to use", mechanical evolution spam, broken references)
3. Detect persistence gaps
4. Detect missing capabilities
5. Apply concrete upgrades (clean frontmatter, add missing sections, strengthen versioning)
6. Run the full persistence pipeline on every changed skill

## Clarity Standards (enforced)
- Frontmatter description: short, trigger-rich, no colon-space that breaks YAML
- Body starts with clear Purpose / Overview
- Explicit ## When to use / ## When NOT to use
- Instructions in imperative form
- Keep mechanical evolution notes in CHANGELOG only, not body

## External Sources
Prefer downloading proven skills from:
- Stijnman/grok-custom-skills
- Other public agent skill collections
- Then adapt + persist

## Version
2.2 — 2026-08-12  
Activated for full library research + improvement + persistence enforcement.
