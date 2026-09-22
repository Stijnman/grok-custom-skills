---
name: beta-unlocker
description: "Use for: authorized discovery and assessment of feature flags, experimental settings, undocumented capabilities, beta modes, or configuration-gated functionality without bypassing platform controls."
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
