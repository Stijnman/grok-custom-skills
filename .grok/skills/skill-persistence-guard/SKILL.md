---
name: skill-persistence-guard
description: Detects missing skill directories in a configured local library and restores them from local artifacts or configured remote sources. Use when skills disappear between turns, after environment cleanup, during startup health checks, or when another skill reports missing dependencies.
license: MIT
---

# Skill Persistence Guard

## Overview
Detects and repairs missing skill directories without assuming a specific username, machine, or filesystem layout. Resolve the skill library and artifact directories from runtime configuration or environment variables before operating.

## Core Rules
- Critical skills may include autonomous-skill-forge, beta-unlocker, skill-evolver, multi-agent-orchestrator, drive-persistence-bridge, natural-language-to-skill, and skill-researcher.
- Prefer configured local artifact archives first, then explicitly configured remote sources.
- Log every restore action and its source.
- Do not claim success until the restored `SKILL.md` exists and validates.
- Never embed account IDs, user-home paths, tokens, or machine-specific directories in the published skill.

## Instructions

1. **Resolve runtime locations**
   - Read the skill-library path from the host/runtime configuration (for example `GROK_SKILLS_DIR`).
   - Read the artifact-cache path from configuration (for example `GROK_ARTIFACTS_DIR`).
   - If either required location is unavailable, report the missing configuration instead of guessing a path.

2. **Detect**
   - Enumerate the configured skill library and compare it with the expected critical set.
   - Flag any missing critical skill.

3. **Restore priority**
   - Search the configured artifact cache for matching versioned archives and prefer the newest valid artifact.
   - If a configured Drive source is available, locate the latest package there without embedding account-specific folder identifiers in this skill.
   - If a configured GitHub source is available, restore from the expected repository/ref.
   - Never overwrite a valid newer local skill with an older artifact.

4. **Validate after restore**
   - Run the repository's configured skill validator on the restored skill.
   - Confirm the directory and `SKILL.md` exist and validation succeeds.

5. **Report**
   - List what was missing, what was restored, the source used, and any remaining gaps.

6. **Integration**
   - May run before workflows that depend on the critical skill set.
   - May be triggered by orchestrator health checks.
   - Re-run a dependent job only after the restored dependency validates.

## Autonomy
Automatic restoration is appropriate only from explicitly configured, trusted sources. Otherwise report the missing dependency and required source configuration.

## Version
1.2 — 2026-09-22
Made filesystem and remote-source handling portable and removed machine/account-specific assumptions.
