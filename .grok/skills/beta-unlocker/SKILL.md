---
name: beta-unlocker
description: Discover documented or user-authorized experimental features, feature flags, and configuration options; explain how they work and assess risks. Use when the user asks to find beta features, inspect feature flags, or understand a setting. Do not bypass access controls or change settings without explicit approval.
license: MIT
metadata:
  version: "2.1"
  type: workflow
---
# Beta Feature Explorer

## Purpose
Help users understand features and settings that are available to them, including documented preview programs and explicitly authorized test environments.

## Workflow
1. Confirm the application, account/environment, and requested scope. Ask before inspecting anything outside the named project or environment.
2. Review documentation and authorized configuration/code. Prefer read-only inspection and report the source of each finding.
3. Classify results as documented and available, experimental but authorized, unavailable due to platform/account constraints, or uncertain.
4. Explain prerequisites, risks, reversibility, and whether a setting affects other users or production data.
5. Before changing a flag, enrolling an account, installing software, modifying configuration, or performing any other state change, describe the exact change and obtain explicit user approval. Use a staging environment where appropriate.
6. Validate approved changes and report what was actually changed. If activation is blocked by provider policy or permissions, explain that rather than attempting a workaround.

## Boundaries
- Do not defeat authentication, permissions, license checks, safety controls, rate limits, or provider restrictions.
- Do not guess hidden endpoints, probe systems without authorization, or expose secrets while inspecting configuration.
- A request to explore or "unlock" is not approval to mutate settings, install software, or access another person's account.
- Do not publish or remotely persist findings without explicit approval of destination and contents.

## Version
2.1 — Replaced autonomous activation with authorized discovery and explicit approval for state changes.
