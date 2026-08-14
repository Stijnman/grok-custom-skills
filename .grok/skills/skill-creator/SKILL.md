---
name: skill-creator
description: "Central skill for creating, updating, and registering new skills. Enforces the Non-Negotiable Persistence Contract on every creation or significant update: Local write + Google Drive upload (dated tar.gz via google_drive_upload_artifact into folder 1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK) + GitHub push (Stijnman/grok-custom-skills). Also triggers sync on major use/evolution events. Triggered by 'create skill', 'new skill', 'skill-creator', 'make a skill', or any skill creation request. Integrates with natural-language-to-skill and skill-creation-enabler."
---

# Skill Creator

## Purpose
This is the authoritative skill for creating and registering new skills in the ecosystem.  
Every successful creation or significant update MUST complete the full Persistence Contract before the task is considered finished.

## Non-Negotiable Persistence Contract (enforced on every create / update)

1. **Local**  
   Write the skill to `/home/workdir/.grok/skills/<skill-name>/SKILL.md` (and supporting files).

2. **Google Drive**  
   - Package: `tar -czf /home/workdir/artifacts/<skill-name>-YYYYMMDD.tar.gz -C /home/workdir/.grok/skills <skill-name>`
   - Upload with `google_drive_upload_artifact`  
     - `artifact_path`: relative path starting with `/` (e.g. `/skill-name-20260814.tar.gz`)
     - `folder_id`: `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`
   - Record the returned `file_id` and `web_view_link`.

3. **GitHub**  
   - Use `github___create_or_update_file`  
   - owner: `Stijnman`  
   - repo: `grok-custom-skills`  
   - path: `.grok/skills/<skill-name>/SKILL.md`  
   - Clear commit message including version and purpose  
   - Record the commit SHA.

4. **Logging**  
   Append to `/home/workdir/artifacts/evolution_log.md`:  
   timestamp + skill name + version + Drive file_id + GitHub commit SHA.

Only after all four steps succeed is the skill considered fully created/updated.

## Workflow

### On Creation Request
1. Parse natural language description (or accept structured input).
2. Design the skill (name, description, triggers, rules, modules).
3. Generate high-quality SKILL.md following ecosystem standards.
4. Create supporting directory structure if needed.
5. Write locally.
6. **Execute Persistence Contract** (mandatory).
7. Confirm success with links and IDs.
8. Optionally notify skill-creation-enabler / skill-evolver.

### On Significant Update / Evolution
Same Persistence Contract must be re-executed for the changed skill(s).

### On Major Use (optional but recommended)
When a skill is heavily used or produces important artifacts, a lightweight sync of the skill itself can be triggered to keep Drive/GitHub current.

## Integration
- Called by / works with: `natural-language-to-skill`, `skill-creation-enabler`, `skill-evolver`, `skill-researcher`.
- Uses: `connected-services-bridge` tools (`google_drive_upload_artifact`, `github___create_or_update_file`).
- Respects Honest Batch Limits from skill-evolver (max ~8 deep creations/edits per cycle).

## Triggers
- "create skill"
- "new skill"
- "skill-creator"
- "make a skill for ..."
- "build skill"
- Any request that results in a new or significantly changed skill definition

## Rules
- Never claim a skill is created until the full Persistence Contract has completed successfully.
- Always use current date (YYYYMMDD) in tar.gz filenames.
- Always use relative artifact_path for Drive uploads.
- Log every persistence action.
- On failure of any leg (Drive or GitHub), retry with exponential backoff (10/30/60s ±25% jitter) and report the exact status.

## Version
1.0 — 2026-08-14  
Introduced as the central enforcer of automatic Local + Drive + GitHub sync on every skill creation and significant update.
