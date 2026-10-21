---
name: zip-toolkit
description: Inspect, create, test, and extract ZIP archives using the existing zip-enabler helper and verified standard utilities. Use when the user asks to inspect or extract an archive, package files, or review a skill pack. Obtain explicit approval before overwriting files, installing into a skills directory, or uploading externally; use configured paths, not fixed host paths.
license: MIT
metadata:
  version: "1.2"
  type: toolkit
  created: "2026-09-16"
---
# ZIP Toolkit

Use the existing `zip-enabler` helper only for operations it actually implements. Resolve the skills root and artifacts directory from runtime configuration or explicit user input; never assume fixed absolute paths.

## When to use

- The user provides a ZIP archive or asks to create, inspect, test, or extract one.
- The user asks to review an archive that may contain skills.

## Safety rules

- Keep extraction in a new, user-approved destination. Inspect archive member names before extraction; stop if any name is absolute, traverses upward, or cannot be evaluated safely.
- Do not overwrite existing files without explicit approval for the exact destination and files.
- Do not install skill packs automatically. The helper does not implement skill-pack installation.
- Do not upload or push an archive unless the user explicitly approves the destination and contents.
- Do not publish bulk copyrighted content from an archive; summarize relevant findings.

## Locate the helper

1. Resolve the configured skills root from runtime configuration or an explicit path.
2. Verify that `<skills-root>/zip-enabler/scripts/zip_tool.py` exists.
3. If it does not exist, stop and explain that this toolkit depends on the `zip-enabler` package. Do not invent or assume a `zip-toolkit` helper.
4. Invoke the verified file through Python. Its inspected interface supports only `create`, `list`, and `extract`:

```text
python3 "<skills-root>/zip-enabler/scripts/zip_tool.py" create <output.zip> <source> [<source> ...]
python3 "<skills-root>/zip-enabler/scripts/zip_tool.py" list <archive.zip>
python3 "<skills-root>/zip-enabler/scripts/zip_tool.py" extract <archive.zip> <new-destination>
```

Before using `extract`, run `list` and review every member path. This helper delegates extraction to Python's ZIP API and does not provide a dedicated archive-safety audit; if a path is suspicious or uncertain, do not extract it.

## Unsupported operations

The installed helper has no `info`, `test`, conversion, add/remove, archive preview, or skill-install commands. Do not advertise or invoke those verbs. For CRC testing, use a verified standard `unzip -t` utility if present; otherwise report the limitation. If the user asks to install an archive, explain that a separate reviewed installation workflow is required and obtain explicit approval before any write.

## Workflow for user-provided archives

1. Confirm the requested operation and destination.
2. Verify the helper exists before relying on it.
3. List and review member names before extraction; stop on unsafe or unclear paths.
4. Extract only to a new destination, then report the exact destination and available file/member count.
5. For skill packs, summarize contents. Do not install, overwrite, upload, or push without separate explicit approval.

## Version

1.2 — 2026-10-21. Removed nonexistent helper claims and fixed paths; documented real helper limits and approval boundaries.
