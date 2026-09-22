---
name: zip-enabler
description: Portable ZIP archive creation, inspection, extraction, and integrity verification. Use when a user asks to create a ZIP, inspect ZIP contents, extract an archive, verify a ZIP, or package files for desktop-compatible transfer.
license: MIT
metadata:
  version: "1.0.1"
  date: "2026-09-23"
---

# Zip Enabler

## When to use

- A user asks to create, inspect, verify, or extract a `.zip` archive.
- Packaging a project or directory in a format commonly supported by desktop operating systems.
- A ZIP is explicitly preferred over `tar.gz`.

## Portable paths

Do not assume a particular username, home directory, workspace root, cloud folder, or installed binary location. Set paths for the current runtime:

```bash
export WORKSPACE="${WORKSPACE:-$PWD}"
export ARTIFACTS_DIR="${ARTIFACTS_DIR:-$WORKSPACE/artifacts}"
export SKILL_DIR="${SKILL_DIR:-$WORKSPACE/.grok/skills/zip-enabler}"
mkdir -p "$ARTIFACTS_DIR"
```

If `zip`/`unzip` are available, they can be used directly. Otherwise use the bundled Python helper.

## Commands

Create an archive:

```bash
zip -r "$ARTIFACTS_DIR/archive.zip" <path1> <path2>
```

List contents:

```bash
unzip -l "$ARTIFACTS_DIR/archive.zip"
```

Extract safely to a dedicated destination:

```bash
mkdir -p "$ARTIFACTS_DIR/unpacked"
unzip "$ARTIFACTS_DIR/archive.zip" -d "$ARTIFACTS_DIR/unpacked"
```

Verify integrity:

```bash
unzip -t "$ARTIFACTS_DIR/archive.zip"
```

Python fallback:

```bash
python3 "$SKILL_DIR/scripts/zip_tool.py" create "$ARTIFACTS_DIR/archive.zip" <path1> <path2>
python3 "$SKILL_DIR/scripts/zip_tool.py" list "$ARTIFACTS_DIR/archive.zip"
python3 "$SKILL_DIR/scripts/zip_tool.py" extract "$ARTIFACTS_DIR/archive.zip" "$ARTIFACTS_DIR/unpacked"
```

## Persistence

Persistence is optional and environment-specific. If the runtime provides an authorized storage integration, upload the resulting archive only when requested. Never embed account-specific folder IDs or assume a particular cloud provider.

## Rules

- Never archive secrets, tokens, private keys, or credentials unless the user explicitly intends to back them up and the destination is appropriate.
- Treat archive member paths as untrusted when extracting; prefer the bundled helper when safe extraction checks are required.
- Preserve relative paths rather than machine-specific absolute paths.
- After creation, report archive size, SHA256, and member count when useful.
- Do not claim a binary or integration exists until the runtime confirms it.

## Version

1.0.1 — portable paths, explicit trigger metadata, and environment-neutral persistence guidance.
