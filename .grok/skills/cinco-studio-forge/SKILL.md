---
name: cinco-studio-forge
description: Bridges Google AI Studio Build mode with GitHub and Drive for apps you vibe-coded. Five Cinco tools — catalog Studio builds, export source, push to GitHub, persist to Drive, iterate rebuild prompts. Triggered by AI Studio, aistudio/build, Cinco tools, Studio Forge, sync my Studio apps, push Build app to GitHub.
metadata:
  type: workflow
  version: "1.0"
  created: "2026-09-06"
---

# Cinco Studio Forge

Connect Google AI Studio (https://aistudio.google.com / https://ai.studio/build) Build-mode apps to this ecosystem and to GitHub.

There is **no official AI Studio connector** in Grok connected services. Do not invent API calls to aistudio.google.com. Use browser + GitHub + Drive. Be honest when login or export is blocked.

## Cinco tools (the five)

1. **Catalog** — list Studio Build apps the user names or that live in GitHub.
2. **Export** — pull source the user provides (paste, zip, repo, Drive) into a clean project tree.
3. **GitHub push** — commit the app to the user's GitHub (default owner `Stijnman`).
4. **Drive persist** — dated tar.gz via `google_drive_upload_artifact`.
5. **Rebuild** — write a tighter Build-mode prompt so the user can re-vibe the app in Studio.

## When this skill fires

User talks about Google AI Studio, Build tab, vibe-coded Gemini apps, "Cinco tools", "EOS studios" (same product), or "apps I created with GitHub".

## Hard limits

- Connected services available here — Google Drive, GitHub, Gmail, Calendar, Notion. Not AI Studio itself.
- AI Studio sessions are Google-account locked. You cannot silently log in as the user.
- Never claim a Studio app was pulled live from Google unless the user actually exported it or a GitHub copy exists.
- Persistence contract after any real app package — local artifacts + Drive folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK` + GitHub.

## Workflow

### 0. Discover tools first

Call `search_connected_tools` before Drive or GitHub writes. Typical queries — `upload artifact`, `push files`, `create or update file`, `list repositories`.

Default GitHub owner — `Stijnman`.
Default skills repo — `Stijnman/grok-custom-skills`.
Default project pattern — `Stijnman/<app-slug>` or a folder under an existing project repo if the user names one.

### 1. Catalog

Ask or accept a list of Build apps. Record for each:

- display name
- slug (kebab-case)
- platform (web / Android)
- Gemini features used (Live API, Nano Banana, Maps, Search, Veo, etc.)
- GitHub repo or path if known
- last sync date
- status (studio-only / github / drive / both)

Keep the running catalog at `references/app-catalog.md` and, when updated, persist it.

Studio entry points to give the user:

- Build home — https://aistudio.google.com/apps or https://ai.studio/build
- New app — Build tab → prompt box → optional AI chips → Build
- Code view — after generate, switch Preview → Code
- Download / copy — use Studio download or "save to Drive" then hand the zip to this skill

### 2. Export

Accept any of:

- pasted file tree
- zip in artifacts
- existing GitHub repo
- Drive file id

Unpack into `/home/workdir/artifacts/<slug>/`. Do not rewrite their app unless they asked for a fix.

### 3. GitHub push

Use discovered GitHub tools (`github___push_files` or `github___create_or_update_file`).

Commit message pattern — `cinco-studio-forge: sync <slug> from AI Studio Build`.

If repo does not exist, try create via GitHub tools. If create is denied, give the user the exact create URL and keep the local tree.

### 4. Drive persist

Package with tar.gz under `/home/workdir/artifacts/<slug>-YYYYMMDD.tar.gz`.

Upload with `google_drive_upload_artifact` using a relative artifact path. Target folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK` unless the user names another folder.

Retry with exp backoff+jitter 10s / 30s / 60s ±25%. Report exact failure. Never claim success without a file id or commit SHA.

### 5. Rebuild prompt

When the user wants to iterate in Studio, write a single paste-ready Build prompt that includes:

- app purpose
- platform (web default, Android if they said so)
- must-have Gemini chips
- UI constraints
- what broke last time

Do not dump a fake connected Studio session. Give them the prompt + the Build URL.

## Naming

Skill name — Cinco Studio Forge.
App slugs — kebab-case, no spaces.
Repos — prefer `studio-<slug>` if creating new.

## Integration

- Persistence details — drive-persistence-bridge
- Tool discovery — connected-services-bridge
- Parallel Drive+GitHub — parallel-tool-orchestrator
- Research on new Studio features — deep-search-enabler + open_page on https://ai.google.dev/gemini-api/docs/aistudio-build-mode

## Honesty

Google AI Studio Build is vibe-coding in the browser. This skill is the handoff layer to GitHub and Drive, not a reverse-engineered Studio backend.
