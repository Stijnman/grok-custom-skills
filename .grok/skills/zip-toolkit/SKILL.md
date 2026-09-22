---
name: zip-toolkit
description: Use when the user asks to inspect, create, test, convert, or safely extract ZIP, tar.gz, or tgz archives, including skill-pack archives.
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
