---
name: autonomous-skill-forge
description: Unified autonomous skill creation, gap detection, research, and unlocking system. Combines skill-creation-enabler, natural-language-to-skill, and skill-researcher into one aggressive, versatile forge. Use when user wants to create, unlock, extend, or auto-generate any missing capability with minimal prompting. Triggers on skill unlocker, autonomous skill, forge skill, make any skill, skill workaround, create missing skills, gap fill, or vague capability requests. Highly autonomous — detects gaps, researches, designs, implements, validates, and persists with reduced hand-holding.
---

# Autonomous Skill Forge

## Overview
Single aggressive entry point that turns the previous three-skill combination into a more versatile and autonomous system. Detects capability gaps, researches solutions, generates production skills from loose natural language, unlocks or extends existing ones, and enforces full persistence. Designed for "anything" requests with high autonomy and low friction.

## Core Autonomy Rules
- Prefer action over clarification when the intent is clear enough.
- On vague requests ("make something for X", "unlock Y", "workaround for Z") — research + propose + implement a minimal viable skill unless high risk is detected.
- Continuously maintain awareness of the current skill library state.
- Escalate only when the requested capability would clearly violate core system safety or Persistence Contract.
- After any creation or major update, complete the full Non-Negotiable Persistence Contract before declaring success.

## Instructions

1. **Parse Intent (Aggressive Mode)**
   - Extract desired capability even from loose, incomplete, or ambitious language.
   - Normalize to a kebab-case skill name.
   - Classify request type: new skill, extension of existing, unlock/hidden mode, gap fill, or full autonomous scan.

2. **Inventory + Gap Detection**
   - Run `ls -1 /home/workdir/.grok/skills/` and `/root/.grok/skills/`.
   - Read frontmatter of candidate matches.
   - If a strong existing match exists, report it and offer extension instead of duplication.
   - If gap exists or match is weak, proceed to research + create.

3. **Research Phase (Parallel Preferable)**
   - Use web_search, open_page, x_keyword_search / x_semantic_search as needed.
   - Pull best practices, patterns, edge cases, and implementation details for the capability.
   - Cross-check against existing skills to avoid pure duplication.
   - Synthesize into clear procedural knowledge.

4. **Design + Generate**
   - Produce complete SKILL.md following exact ecosystem format (frontmatter rules strict).
   - Include strong trigger phrases, autonomy level, integration points, and Persistence Contract reminder.
   - Generate any required scripts/ or references/ content.
   - Keep SKILL.md focused and under 500 lines where possible.

5. **Implement**
   - Use skill-creator init script if needed, or direct write_file / edit_file.
   - Place under `/home/workdir/.grok/skills/<name>/`.
   - Make scripts executable when present.

6. **Validate**
   - Run `/root/.grok/skills/skill-creator/scripts/validate-skill.sh` on the new skill.
   - Fix structural or format issues immediately.
   - Conceptually test against sample queries.
   - Optionally invoke auto-tester for deeper checks.

7. **Persist (Mandatory)**
   - Local confirmation.
   - Package dated tar.gz and upload via connected Drive tools to folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`.
   - Push SKILL.md to GitHub repo `Stijnman/grok-custom-skills` at `.grok/skills/<name>/SKILL.md`.
   - Log file_id, commit, timestamp to evolution_log.md.
   - Never claim success until Persistence Contract is complete.

8. **Report**
   - Clear summary: what was created/unlocked, why, key capabilities, autonomy decisions made, persistence status.
   - Offer immediate usage examples or further evolution.

## Autonomy Levels
- **Standard**: Confirm before major creation.
- **High (default for this skill)**: Research + implement + persist on clear-enough requests; report after.
- **Full Scan**: On "run autonomous scan" or "fill gaps" — proactively detect multiple missing high-value skills and propose a prioritized batch (respect honest batch limits).

## Integration
- Calls or mimics logic from skill-researcher, natural-language-to-skill, skill-creation-enabler.
- Coordinates with skill-evolver, auto-tester, drive-persistence-bridge, connected-services-bridge.
- Can be triggered by other meta-skills for continuous library health.

## Non-Negotiable Rules
- Full Persistence Contract on every new or significantly updated skill.
- No pure duplicates of existing high-quality skills.
- Honest reporting of what was actually done vs deferred.
- Respect skill-evolver batch limits when doing bulk work.
- Log all major decisions.

## Version
1.0 — 2026-08-26
Initial composite forge. High autonomy + versatility focus as requested.
