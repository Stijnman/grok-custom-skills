---
name: auto-skill-resolver
description: Automatically analyzes any user prompt, determines required capabilities, searches local library + external skill sources, downloads or creates the missing skill on the fly, then forces permanent persistence. Every new skill is version-controlled, saved to persistent memory, pushed to GitHub (Stijnman/grok-custom-skills), and uploaded to Google Drive (Grok Skills Library folder). Non-negotiable persistence layer. Triggered on capability gaps or explicit resolve requests.
---

# Auto Skill Resolver (v2.0 — Full Persistence Edition)

## Non-Negotiable Rules (Highest Priority)

1. **Every newly generated or downloaded skill MUST be persisted** in all three places:
   - Local filesystem (`/home/workdir/.grok/skills/`)
   - Persistent Memory (via persistent-memory-bridge)
   - Google Drive (folder "Grok Skills Library" — ID `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK`)
   - GitHub repository `Stijnman/grok-custom-skills` (main branch)

2. Original Grok/bundled skills are also tracked in the same persistence system so the full library (original + generated) stays unified.

3. **Version Control is mandatory**. Every skill has semantic versioning (MAJOR.MINOR.PATCH), a CHANGELOG.md, and full history on GitHub.

4. External skill download sources are first-class. Prefer high-quality public sources before creating from scratch.

## Core Workflow

### 1. Analyze Prompt
Extract required capabilities. Produce a clear "capability need" statement.

### 2. Search (Local + External)
- Local: full scan of `/home/workdir/.grok/skills/` + `/root/.grok/skills/`
- External sources (in order of preference):
  - GitHub: `Stijnman/grok-custom-skills` and other known skill repos
  - Public agent skill marketplaces / collections (via web_search + tool-discovery-engine)
  - Known high-quality open skill repositories
- Rank matches. Prefer existing over creating.

### 3. Acquire
- If strong local match → load it
- If external match found → download + adapt + register
- If none → create via natural-language-to-skill + skill-researcher + skill-creator

### 4. Version & Persist (Mandatory for every new/changed skill)
```
a. Assign or bump semantic version
b. Write/update CHANGELOG.md
c. Write to local skills directory
d. Record in persistent memory (persistent-memory-bridge)
e. Package as tar.gz / individual files
f. Upload package + SKILL.md to Google Drive folder "Grok Skills Library"
g. Push to GitHub repo Stijnman/grok-custom-skills (create or update files)
h. Log everything to evolution_log.md
```

### 5. Activate & Continue
Load the skill and continue solving the original prompt.

## External Download Capability

Supported sources:
- GitHub repositories (especially Stijnman/* and other agent-skill collections)
- Direct raw.githubusercontent.com links to SKILL.md files
- Public skill indexes discovered via tool-discovery-engine / web_search
- Future: any user-configured external skill registries

Download process:
1. Fetch SKILL.md + supporting files
2. Validate format against skill-creator rules
3. Adapt paths and integrations if needed
4. Run full persistence pipeline (version + memory + Drive + GitHub)

## Version Control System

- Every skill directory contains:
  - SKILL.md (with version in frontmatter or body)
  - CHANGELOG.md
  - versions/ folder (historical SKILL.vX.Y.Z.md snapshots)
- GitHub is the source of truth for history and collaboration
- Local versions/ folder keeps recent history for offline use
- On every change: bump version according to semantic versioning rules

## Integration Points

- persistent-memory-bridge → mandatory memory write
- connected-services-bridge / google_drive_upload_artifact → Drive
- GitHub tools (create_or_update_file / push_files) → Stijnman/grok-custom-skills
- natural-language-to-skill, skill-researcher, skill-creator → generation
- skill-creation-enabler → long-term health
- tool-discovery-engine → external source discovery

## Output Transparency

Always emit:

```
[auto-skill-resolver v2]
Capability need: ...
Search result: local / external / create
Action taken: ...
Persistence: Memory ✓ | Drive ✓ | GitHub ✓ | Version X.Y.Z
Skill active.
```

## Version
2.0 — 2026-08-12  
Major upgrade: enforced multi-destination persistence (Memory + Drive + GitHub), external download support, full skill version control system. Made non-negotiable by user directive.
