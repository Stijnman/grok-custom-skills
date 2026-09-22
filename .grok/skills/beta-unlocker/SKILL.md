---
name: beta-unlocker
description: Use this skill when an authorized project needs discovery and assessment of hidden modes, feature flags, experimental features, undocumented capabilities, beta settings, or configuration-gated functionality. Scans codebases, configs, runtime, and skills, distinguishes configurable features from hard platform locks, and reports activation options without pretending unavailable controls exist.
license: MIT
---

# Beta Unlocker

## Overview
Discovery and assessment engine for features that are hidden, experimental, undocumented, or configuration-gated. It surfaces capabilities and distinguishes normal configuration switches from platform-level restrictions.

Use it only on systems and projects the operator is authorized to inspect or modify.

## Operating rules
- Inspect configuration, source, documented runtime flags, and skill metadata before proposing changes.
- Prefer reversible configuration changes over invasive modifications.
- Do not bypass access controls, licensing, authentication, or platform-enforced restrictions.
- Report hard platform locks accurately rather than representing them as configurable toggles.
- Keep a clear record of changed settings and how to revert them.
- Require explicit approval for destructive, account-wide, billing-related, or irreversible changes.
