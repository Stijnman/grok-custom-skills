---
name: skill-persistence-guard
description: Check a configured skills library for missing packages and help restore them from verified local or user-approved sources. Use when skills disappear, after environment cleanup, or during a requested library health check. Obtain explicit approval before remote downloads or overwriting existing files.
license: MIT
metadata:
  version: "1.2"
---
# Skill Persistence Guard

## Purpose
Find missing skill packages and assist with a verified, user-approved recovery. A health check is read-only; a missing package does not authorize a remote download or overwrite.

## Workflow
1. Use the runtime-configured skills root or an explicit path supplied by the user. Never assume a host-specific home path or create a shadow library.
2. Compare the requested expected package list with the current root. Report missing items and any uncertainty.
3. Inspect user-approved local artifact locations first. Verify source provenance and archive member paths before extracting; compare candidate versions rather than trusting the newest timestamp alone.
4. If no verified local copy exists, identify a remote source and destination, then obtain explicit user approval before download or local write. Never replace an existing package without explicit approval for that specific replacement.
5. Validate any approved restore using the repository or package validator available in the current environment. Confirm the expected `SKILL.md` exists.
6. Report what was missing, what was restored, verified source, approvals received, validation performed, and remaining gaps.

## Boundaries
- Do not download, upload, or push files without explicit approval of the destination and contents.
- Do not restore from unverified archives or access unrelated private data.
- If the configured skills root is missing or ambiguous, report that and ask; do not guess another location.

## Version
1.2 — 2026-10-21. Replaced assumed paths and automatic remote restoration with configured roots, source checks, and explicit approval.
