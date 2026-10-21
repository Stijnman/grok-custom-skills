---
name: zip-enabler
description: Create, list, extract, and verify ZIP archives using available archive tools or Python zipfile. Use when the user asks to make or inspect a ZIP, extract an archive, or package files as ZIP. Confirm before overwriting files, installing a skill pack, or uploading an archive. Resolve paths from the current task or configured artifacts directory rather than a fixed home path.
metadata:
  version: "1.1.0"
  date: "2026-08-28"
license: MIT
---

# Zip Enabler

## Status

Enabled. The sandbox already has `/usr/bin/zip`, `/usr/bin/unzip`, and Python `zipfile`. This skill makes `.zip` a first-class packaging format next to `tar.gz`.

## When to use

- User says "enable zip", "zip support", "make a .zip", "unzip", or "/zip".
- Sharing archives that Windows/macOS users open without extra tools.
- Packaging skills or project trees for Drive upload in `.zip` form.

## Commands (run via bash)

Set `ARTIFACTS_DIR` and `SKILLS_ROOT` to directories configured for the current runtime or explicitly chosen by the user. Quote paths; these examples use Unix shell syntax.

Create a zip from paths (store relative names):

```bash
zip -r "$ARTIFACTS_DIR/name-YYYYMMDD.zip" "$SRC1" "$SRC2"
```

Create from a directory without the parent prefix:

```bash
(cd "$PARENT_DIR" && zip -r "$ARTIFACTS_DIR/name-YYYYMMDD.zip" "$DIRNAME")
```

List contents:

```bash
unzip -l "$ARTIFACTS_DIR/file.zip"
```

Extract to a new target folder without replacing existing files:

```bash
mkdir -p "$ARTIFACTS_DIR/unzipped-name"
unzip -n "$ARTIFACTS_DIR/file.zip" -d "$ARTIFACTS_DIR/unzipped-name"
```

Integrity check:

```bash
unzip -t "$ARTIFACTS_DIR/file.zip"
```

Python helper (verify the file exists under the configured skills root before use; it supports create/list/extract only):

```bash
python3 "$SKILLS_ROOT/zip-enabler/scripts/zip_tool.py" create "$ARTIFACTS_DIR/output.zip" "$SRC"
python3 "$SKILLS_ROOT/zip-enabler/scripts/zip_tool.py" list "$ARTIFACTS_DIR/file.zip"
python3 "$SKILLS_ROOT/zip-enabler/scripts/zip_tool.py" extract "$ARTIFACTS_DIR/file.zip" "$ARTIFACTS_DIR/destination"
```

## Persistence

After creating a zip meant as a backup or skill pack:

1. Write it under `<artifacts-dir>/`.
2. Before uploading, show archive contents and target account/folder, then obtain explicit user approval. Use the connector’s configured relative artifact path.
3. Use only a Drive folder the user explicitly names or approves; do not infer a stored folder ID.
4. Offer `render_file` so the user can download it.

`tar.gz` remains valid. Use `.zip` when the user asked for zip or when the consumer is a desktop OS.

## Rules

- Inspect archive member paths before extraction. If any path is absolute, traverses upward, or cannot be checked, stop; do not extract it.
- Never replace existing files without explicit approval.
- Never zip secrets, tokens, or private keys.
- Prefer `-r` recursive for skill directories.
- Name files `name-YYYYMMDD.zip`.
- Report size, SHA256, and member count after create.
- Do not claim zip was unavailable; the binaries are present.

## Version

1.1.0 — 2026-10-21. Replaced fixed paths and overwrite extraction; gated uploads on explicit destination approval.
