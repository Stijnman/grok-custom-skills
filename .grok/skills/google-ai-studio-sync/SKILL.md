---
name: google-ai-studio-sync
description: Use when a user wants to catalog, export, persist, or synchronize a Google AI Studio Build app with GitHub or Drive.
license: MIT
metadata:
  type: workflow
  version: "1.2"
  created: "2026-09-06"
  renamed_from: cinco-studio-forge
---

# Google AI Studio Sync

Bridge user-provided Google AI Studio Build projects to GitHub and Drive without pretending an unavailable Studio API exists.

## When to use

Use this skill when the user asks to sync, export, catalog, persist, or rebuild a Google AI Studio / Build-mode app.

## Capabilities

1. **Catalog** — record app name, slug, platform, Gemini features, repository/path, last sync and status.
2. **Export** — accept a pasted tree, archive, existing repository, or connected-drive file and stage it in the active workspace.
3. **GitHub sync** — create/update repository files through available GitHub tools and return the resulting commit/PR reference.
4. **Drive persistence** — package an app in the active artifact/workspace directory and upload it through an available Drive connector.
5. **Rebuild prompt** — produce a paste-ready Build prompt describing purpose, platform, required features, UI constraints and known defects.

## Runtime paths

Never assume a particular user's home directory. Resolve writable locations from the current runtime. Prefer, in order:

- an explicit workspace/artifact directory supplied by the host;
- `$WORKSPACE` or `$ARTIFACTS_DIR` when defined;
- a temporary directory supplied by the runtime.

Keep generated paths relative where connector APIs require relative artifact paths.

## Operating rules

- Discover currently available GitHub/Drive tools before invoking them.
- Do not claim direct access to Google AI Studio unless a connected tool actually provides it.
- Do not silently authenticate as the user.
- Do not claim an export, upload, or push succeeded without a returned file identifier, commit SHA, PR, or equivalent receipt.
- Do not rewrite exported application code unless the user requested changes.
- Use the repository/folder named by the user; otherwise choose a clear project slug rather than embedding account-specific IDs.
- Treat credentials and project secrets as runtime configuration, never repository content.

## Catalog

For each app record:

- display name and kebab-case slug;
- platform;
- Gemini capabilities used;
- GitHub repository/path when known;
- last synchronization date;
- state such as Studio-only, GitHub, Drive, or synchronized.

A repository may keep this catalog at `references/app-catalog.md` when appropriate.

## Export and persistence

Accept a user-provided archive, source tree, repository, or connected-drive object. Extract/stage it inside the runtime-approved workspace. When persistence is requested, package it there and upload or commit through the connected service. Preserve the source unless modification was requested.

## GitHub synchronization

Prefer an isolated branch/PR for substantive changes. Use concise commit messages such as `google-ai-studio-sync: sync <slug>`. If repository creation is unavailable, preserve the staged result and report the exact limitation rather than claiming success.

## Rebuild prompts

Include the app purpose, target platform, required Gemini capabilities, UI constraints, and concrete defects from the previous build. Keep the result directly pasteable into AI Studio Build.

## Related skills

- `drive-persistence-bridge`
- `connected-services-bridge`
- `parallel-tool-orchestrator`
- `deep-search-enabler`

## Integrity

This is a handoff/synchronization workflow, not a reverse-engineered Google AI Studio backend. Capabilities must match the tools actually available in the current runtime.
