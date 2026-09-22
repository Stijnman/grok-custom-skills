---
name: zip-toolkit
description: Use this skill when a user needs to inspect, create, test, convert, or safely extract ZIP, tar.gz, or tgz archives, including skill-pack archives.
license: MIT
metadata:
  version: "1.0"
  type: toolkit
  created: "2026-09-16"
---

# Zip Toolkit

Handle archive operations inside the current agent workspace. Resolve the workspace and skill directory from the runtime environment instead of assuming a specific user's home directory.

## When to use

- A user supplies a `.zip`, `.tar.gz`, or `.tgz` archive.
- A user asks to unzip, extract, pack, archive, inspect, test, or convert an archive.
- A skill pack needs to be previewed or installed without blindly overwriting existing skills.

## Safety and portability

- Reject zip-slip/path-traversal members: extracted paths must remain under the chosen destination.
- Never overwrite an installed skill unless the user explicitly requests it.
- Use a temporary or runtime-provided artifacts directory by default.
- Report destination, member count, top-level folders, and size after extraction.
- Do not brute-force encrypted archives.
- For large archives, inspect contents before extraction.

## Operations

Run `scripts/zip_tool.py` from this skill's directory:

```bash
python3 scripts/zip_tool.py <command> [args]
```

Supported operations include `info`, `list`, `test`, `extract`, `extract-file`, `create`, `add`, `remove`, `install-skills`, `preview-skills`, `to-targz`, `to-zip`, and `find-skills`.

Always run `info` before a large extraction.

## Skill-pack workflow

1. Inspect the archive and preview skills.
2. Extract into an isolated workspace directory.
3. Report detected skill folders and collisions.
4. Dry-run installation before copying into the active skills directory.
5. Require explicit overwrite intent for collisions.

A folder counts as a skill when it contains `SKILL.md` at its root, or one level below the archive root.

## Errors

- If platform archive binaries are missing, use the Python standard-library fallback implemented by the script.
- If integrity validation fails, stop before installation.
- If extraction is interrupted, do not treat the partial output as a valid installed skill pack.

## References

- `references/formats.md` — archive formats and traversal risks.
- `scripts/zip_tool.py` — implementation.
