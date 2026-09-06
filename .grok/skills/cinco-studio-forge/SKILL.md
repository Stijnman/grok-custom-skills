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
