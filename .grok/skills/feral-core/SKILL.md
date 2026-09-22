---
name: feral-core
description: Unified high-autonomy skill orchestration engine. Use when the user asks to create or improve skills, discover configurable features, restore missing skills, run a focused improvement round, or coordinate multiple skill-maintenance capabilities in one workflow.
license: MIT
---

# Feral Core

## Overview
Coordinates skill creation, feature discovery, validation, restoration, and iterative improvement through one entry point.

## Workflow

1. **Verify the skill set**
   - Check that required skills are available through configured runtime paths.
   - Restore missing components only from configured and authorized persistence backends.

2. **Parse intent**
   - Determine whether the task is creation, improvement, feature discovery, restoration, validation, or orchestration.
   - Prefer an existing capable skill over creating a duplicate.

3. **Execute**
   - Missing capability: research, design, implement, validate, and persist a focused skill.
   - Configurable feature: identify the documented/configured switch and make reversible changes when authorized.
   - Missing skill: restore the newest validated version from an available trusted backend.
   - Improvement request: make one focused change, evaluate it, and keep it only when validation improves.

4. **Validate**
   - Run repository validators and focused tests after edits.
   - Do not report success when validation is red.

5. **Persist**
   - Persist through destinations actually configured in the runtime, such as version control or an approved artifact store.
   - Record resulting commit or artifact identifiers when available.

6. **Report**
   - State what changed, what passed, and any remaining blocker.

## Operating rules
- Keep paths portable and configuration-driven.
- Do not embed credentials, private identifiers, or machine-specific paths.
- Prefer reversible changes.
- Do not bypass authentication, access controls, licensing, or platform-enforced restrictions.
- Do not claim tests, persistence, commits, uploads, or feature activation that did not occur.

## Version
1.1 — 2026-09-22
Portable metadata and validation-safe operating contract.
