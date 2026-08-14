---
name: auto-skill-resolver
description: Central gatekeeper for the skill library. Analyzes any prompt or improvement request, finds or creates the needed skill, then forces the full non-negotiable persistence pipeline (Persistent Memory + Google Drive + GitHub) and continuous clarity upgrades. Enforces version control, external downloads, and library research. Triggered by capability gaps, "improve the skills", research requests, or any skill creation/evolution event. Receives hand-offs from skill-creation-enabler. Optimized for accurate LLM routing.
---

# Auto Skill Resolver

## Purpose
Make the entire skill library self-improving, always-persisted, clear, and unified. This is the single entry point for skill acquisition and improvement. skill-creation-enabler detects gaps and hands them off here.

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

This applies to both newly generated skills and the original Grok/bundled skills when they are touched. No skill is considered "created" until Local + Drive + GitHub succeed (or blockers are explicitly documented with recovery steps).

## Core Workflow

### Research & Analysis Mode
When asked to research existing skills:
- Scan the library for clarity problems, outdated references, missing persistence hooks, overlapping responsibilities
- Identify high-value improvements (especially around persistency and readability)
- Prioritize changes that reduce fragmentation
- Report exact skills examined vs deferred (honest batch limits)

### Resolve Mode (primary for missing-skill hand-offs)
1. Analyze the prompt or requested capability
2. Search local library first (`/home/workdir/.grok/skills/` + `/root/.grok/skills/`)
3. Search external sources (GitHub skill repos, public collections, ClawHub) if needed
4. Download + adapt or create via natural-language-to-skill + skill-researcher + skill-creator
5. Immediately run the full Persistence Contract above
6. Activate the skill and continue the original task

### Improvement Mode
- Prefer editing existing skills for clarity over creating new ones
- Strip accumulated evolution notes that bury the core instructions
- Make descriptions shorter and more precise
- Ensure every skill mentions the Persistence Contract or points to this skill

## Implementation Steps (Resolve Mode detail)

### Normalize
- Convert free-form request to valid kebab-case name (2-64 chars, alphanumeric + hyphens)

### Deduplicate
- If full coverage exists → report and stop
- If partial → prefer extension unless clear differentiation needed

### Create
```bash
bash /root/.grok/skills/skill-creator/scripts/init-skill.sh <name> /home/workdir/.grok/skills --resources scripts,references,assets
```
- Populate SKILL.md (imperative, non-obvious knowledge only)
- Validate: `bash /root/.grok/skills/skill-creator/scripts/validate-skill.sh <path>`

### Persist
```bash
tar -czf /home/workdir/artifacts/<name>-YYYYMMDD.tar.gz -C /home/workdir/.grok/skills <name>
```
- Upload via `google_drive_upload_artifact` with relative artifact_path into folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`
- `github___create_or_update_file` on `Stijnman/grok-custom-skills` at `.grok/skills/<name>/SKILL.md` (provide SHA when updating)
- Log file_id + commit SHA to evolution_log.md

## Clarity Rules (enforced on every edit)
- Core instructions first, evolution history last (or moved to CHANGELOG)
- Frontmatter description must be a single clear paragraph (plain YAML scalar, no `: `, no `<>`)
- Avoid referencing non-existent skills
- Prefer concrete paths, IDs, and tool names over vague "use the bridge"
- Honest batch limits: deep work on ≤3-8 skills per cycle; explicit deferred list for bulk requests

## Error Handling
- Exp backoff + jitter (10s / 30s / 60s ±25%) on transient failures
- Sandbox awareness: if connected tools fail, complete Local + package tar.gz, report exact recovery commands, never claim full persistence

## Integration
- Calls: natural-language-to-skill, skill-researcher, skill-creator, skill-evolver, drive-persistence-bridge, persistent-memory-bridge, connected-services-bridge
- Is called by: skill-creation-enabler, multi-agent-orchestrator, workflow-composer, any evolution cycle

## Helper Script
`scripts/resolve-skill.sh <skill-name>` — packages existing local skill and emits persistence targets.

## Version
2.4.0 — 2026-08-14
Aligned local with GitHub v2.3 + reinforced concrete create/validate/package steps + helper script + honest limits. Fills the required dependency for skill-creation-enabler.
