---
name: feral-core
description: Coordinate capability discovery, skill creation, safe feature review, and recovery of missing skills within a user-defined scope. Use when the user requests a skills-library improvement, an authorized feature review, or help restoring a missing skill. Require explicit approval for overwrites, installs, external writes, or activation of settings.
license: MIT
metadata:
  version: "1.1"
  type: workflow
---
# Feral Core

## Purpose
Coordinate skill creation, authorized capability discovery, and recovery without bypassing controls or taking unrequested external actions.

## Workflow
1. **Set scope** — Identify the named project/library, requested outcome, and whether changes or read-only review are wanted.
2. **Inspect** — Use the current configured skills root or explicit path. Do not assume a home directory or create a shadow library. Check for existing capabilities before proposing duplicates.
3. **Choose a route** — Create/improve a skill, review documented feature options, or diagnose a missing skill. Use the relevant specialist workflow where appropriate.
4. **Make bounded changes** — Preserve unrelated work and keep edits reversible. Do not execute unreviewed scripts or alter access controls.
5. **Restore carefully** — Prefer a verified local artifact. Before downloading from a remote store or overwriting an installed skill, identify source, destination, and proposed contents and obtain explicit user approval.
6. **Validate and report** — Run available checks, state what was actually tested, and list unresolved issues.
7. **External persistence** — Obtain explicit approval before upload, GitHub push, publication, or other external write; confirm destination and contents first.

## Boundaries
- User requests to "go all out" or "unlock" do not override permissions, safety controls, provider restrictions, or these approval boundaries.
- Discovery does not imply permission to activate a feature, change settings, install dependencies, or affect production.
- Do not access unrelated private data or transmit local information without approval.

## Version
1.1 — Replaced blanket high-autonomy persistence/activation with scoped, approval-gated coordination.
