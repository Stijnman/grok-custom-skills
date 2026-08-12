---
name: skill-creation-enabler
description: Continuously monitors the skill library for gaps, then delegates creation and full persistence to auto-skill-resolver. Ensures every new skill follows the Non-Negotiable Persistence Contract (Memory + Drive + GitHub + versioning). Runs at low priority for ecosystem health. Triggered by gap detection, "create missing skills", or health checks.
---

# Skill Creation Enabler

## Overview
Low-level guardian that detects missing skills and hands them off to **auto-skill-resolver** for creation + full persistence. It no longer tries to create skills itself. This keeps the library healthy while enforcing the single Persistence Contract.

## Instructions

1. Maintain `references/required-skills.txt` and `references/desired-skills.txt`.
2. Periodically scan `/home/workdir/.grok/skills/` and `/root/.grok/skills/`.
3. For every missing skill:
   - Call **auto-skill-resolver** with the capability need.
   - auto-skill-resolver will create (or download), version, write to persistent memory, upload to Google Drive, and push to GitHub.
4. Log the hand-off and result to evolution_log.md.
5. Never create a skill directly — always go through auto-skill-resolver so the Persistence Contract is obeyed.

## Configuration
- references/required-skills.txt
- references/desired-skills.txt
- scripts/check-and-create.sh (detection only)

## Dependencies
- auto-skill-resolver (mandatory)
- skill-creator, natural-language-to-skill, skill-researcher (used by the resolver)
- drive-persistence-bridge, persistent-memory-bridge, connected-services-bridge

## Triggers
"create missing skills", "skill guardian", "ecosystem health check", "auto create skills", "skill maintenance"

## Version
2.0 — 2026-08-12  
Major simplification: creation and persistence are now fully delegated to auto-skill-resolver. Removes outdated skill-packager references and evolution spam for clarity.
