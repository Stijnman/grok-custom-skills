---
name: auto-skill-resolver
description: Central gatekeeper for the skill library. Analyzes any prompt or improvement request, finds or creates the needed skill, then forces the full non-negotiable persistence pipeline (Persistent Memory + Google Drive + GitHub) and continuous clarity upgrades. Enforces version control, external downloads, and library research. Triggered by capability gaps, "improve the skills", research requests, or any skill creation/evolution event.
---

# Auto Skill Resolver v2.3

## Purpose
Make the entire skill library self-improving, always-persisted, clear, and unified. This is the single entry point for skill acquisition and improvement.

## Non-Negotiable Persistence Contract
Every time a skill is created, improved, or downloaded, the following must happen in order:

1. Update local SKILL.md (clean, clear language)
2. Bump semantic version + write CHANGELOG.md + snapshot in versions/
3. Record the change in Persistent Memory (persistent-memory-bridge)
4. Package (tar.gz preferred)
5. Upload to Google Drive folder **Grok Skills Library** (ID: `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`)
6. Push to GitHub `Stijnman/grok-custom-skills` under `.grok/skills/<skill-name>/`
7. Update master index if present
8. Log to evolution_log.md with timestamp and summary

This applies to both newly generated skills and the original Grok/bundled skills when they are touched.

## Core Workflow

### Research & Analysis Mode (current request)
When asked to research existing skills:
- Scan the library for clarity problems, outdated references, missing persistence hooks, overlapping responsibilities
- Identify high-value improvements (especially around persistency and readability)
- Prioritize changes that reduce fragmentation

### Resolve Mode
1. Analyze the prompt or requested capability
2. Search local library first
3. Search external sources (GitHub skill repos, public collections)
4. Download + adapt or create via natural-language-to-skill + skill-researcher
5. Immediately run the full Persistence Contract above
6. Activate the skill and continue the original task

### Improvement Mode
- Prefer editing existing skills for clarity over creating new ones
- Strip accumulated evolution notes that bury the core instructions
- Make descriptions shorter and more precise
- Ensure every skill mentions the Persistence Contract or points to this skill

## Clarity Rules (enforced on every edit)
- Core instructions first, evolution history last (or moved to CHANGELOG)
- Frontmatter description must be a single clear paragraph
- Avoid referencing non-existent skills
- Prefer concrete paths, IDs, and tool names over vague "use the bridge"

## Integration
- Calls: natural-language-to-skill, skill-researcher, skill-creator, skill-evolver, drive-persistence-bridge, persistent-memory-bridge, connected-services-bridge
- Is called by: skill-creation-enabler, multi-agent-orchestrator, workflow-composer, any evolution cycle

## Version
2.3 — 2026-08-12  
Clarity + research focus. Strengthened Persistence Contract. Made the single gatekeeper for all skill changes.
