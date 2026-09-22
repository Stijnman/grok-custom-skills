---
name: godlevel-secret-hunter
description: Repository capability discovery and audit skill. Use when reviewing an owned or authorized codebase for undocumented features, experimental flags, dormant integrations, unused scripts, configuration options, or latent architecture that should be documented, tested, or deliberately enabled.
license: MIT
---

# Godlevel Secret Hunter

## Purpose
Find overlooked capabilities in repositories and runtime configuration that the operator owns or is authorized to inspect, then turn useful discoveries into documented, testable improvements.

## Workflow

1. **Inventory**
   - Inspect skill bodies, scripts, configuration, workflows, feature flags, integrations, and architecture documentation.
   - Identify experimental or undocumented functionality and stale or unused components.

2. **Classify**
   - Documented but unused capability.
   - Experimental feature requiring an explicit opt-in.
   - Configuration or integration opportunity.
   - Platform limitation that cannot be changed from the repository.

3. **Verify**
   - Trace each discovery to concrete source files or configuration.
   - Prefer tests or reproducible commands over assumptions.
   - Do not claim a capability is active until it has been verified.

4. **Improve**
   - Add documentation, tests, safer defaults, or explicit configuration for useful discoveries.
   - Keep experimental behavior opt-in when it can change data, external systems, permissions, or security posture.
   - Record blockers precisely instead of bypassing platform controls.

5. **Report**
   - List discoveries, evidence, changes made, validation results, and unresolved blockers.

## Scope
Use only on repositories, services, devices, and accounts the operator owns or is authorized to inspect. Do not attempt to bypass access controls, extract credentials, or activate capabilities that require permissions the operator does not have.

## Version
1.2 — 2026-09-22
