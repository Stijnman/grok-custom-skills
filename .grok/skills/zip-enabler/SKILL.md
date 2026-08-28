---
name: zip-enabler
description: Enables first-class .zip create, list, extract, verify, and persist support in the sandbox. Triggered by enable zip, zip support, make a zip, unzip this, package as zip, or when a user wants .zip instead of tar.gz. Uses Info-ZIP plus Python zipfile. Integrates with drive-persistence-bridge uploads.
metadata:
  version: "1.0.0"
  date: "2026-08-28"
---

# Zip Enabler

## Status

Enabled. The sandbox already has `/usr/bin/zip`, `/usr/bin/unzip`, and Python `zipfile`. This skill makes `.zip` a first-class packaging format next to `tar.gz`.

## When to use

- User says "enable zip", "zip support", "make a .zip", "unzip", or "/zip".
- Sharing archives that Windows/macOS users open without extra tools.
- Packaging skills or project trees for Drive upload in `.zip` form.

## Commands (run via bash)

Create a zip from paths (store relative names):

```bash
zip -r /home/workdir/artifacts/<name>-$(date +%Y%m%d).zip <path1> <path2>
```

Create from a directory without the parent prefix:

```bash
cd /path/to/parent && zip -r /home/workdir/artifacts/<name>-$(date +%Y%m%d).zip <dirname>
```

List contents:

```bash
unzip -l /home/workdir/artifacts/<file>.zip
```

Extract to a target folder:

```bash
mkdir -p /home/workdir/artifacts/unzipped-<name>
unzip -o /home/workdir/artifacts/<file>.zip -d /home/workdir/artifacts/unzipped-<name>
```

Integrity check:

```bash
unzip -t /home/workdir/artifacts/<file>.zip
```

Python fallback (same paths):

```bash
python3 /home/workdir/.grok/skills/zip-enabler/scripts/zip_tool.py create OUT.zip SRC...
python3 /home/workdir/.grok/skills/zip-enabler/scripts/zip_tool.py list FILE.zip
python3 /home/workdir/.grok/skills/zip-enabler/scripts/zip_tool.py extract FILE.zip DEST
```

## Persistence

After creating a zip meant as a backup or skill pack:

1. Write it under `/home/workdir/artifacts/`.
2. Upload with `google_drive_upload_artifact` using a path relative to artifacts (example `/enablers-20260828.zip`).
3. Prefer Drive folder `1jEivRtcNo-x9sd--2l1qe1bVox-TSnYK` for skill packs.
4. Offer `render_file` so the user can download it.

`tar.gz` remains valid. Use `.zip` when the user asked for zip or when the consumer is a desktop OS.

## Rules

- Never zip secrets, tokens, or private keys.
- Prefer `-r` recursive for skill directories.
- Name files `name-YYYYMMDD.zip`.
- Report size, SHA256, and member count after create.
- Do not claim zip was unavailable; the binaries are present.

## Version

1.0.0 — 2026-08-28. First-class .zip enablement.
