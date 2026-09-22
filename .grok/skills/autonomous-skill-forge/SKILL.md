---
name: autonomous-skill-forge
description: "Use for: detecting a capability gap, researching a solution, creating or improving a reusable skill, validating it, and persisting the result."
license: MIT
---

# Autonomous Skill Forge

## Purpose
Build or improve reusable agent skills when an existing capability is missing or inadequate.

## Workflow
1. Inspect the available skill library and identify the closest existing capability.
2. Prefer extending a strong existing skill over creating a duplicate.
3. Research the required behavior, edge cases, and failure modes.
4. Design a focused skill with explicit triggers and actionable instructions.
5. Write it beneath `${GROK_SKILLS_DIR:-$HOME/.grok/skills}/<skill-name>/` or the runtime's configured skill directory.
6. Validate syntax, metadata, referenced scripts, and representative use cases.
7. Persist the validated result using only storage/connectors that are actually available in the current runtime.
8. Report what changed, what was tested, and any remaining blocker.

## Design rules
- Use lowercase kebab-case names.
- State clearly in frontmatter when the skill should be used.
- Keep runtime paths portable; derive them from environment/configuration rather than a specific user's home directory.
- Do not embed credentials, tokens, private identifiers, or machine-specific secrets.
- Avoid duplicate skills when an existing skill can be extended cleanly.
- Keep generated instructions concrete and testable.
- Do not claim persistence, tests, uploads, or commits that did not actually occur.

## Validation
Run the repository's skill validator after every significant edit. Fix validation failures before considering the skill complete. For scripts, also run syntax checks and focused tests where available.

## Persistence
Persist only through configured destinations. A typical installation can use a local skill directory plus version control; optional external backups may be used when their connectors are available. Record the resulting commit or artifact identifiers when the runtime provides them.

## Integration
This skill can coordinate with skill research, skill testing, persistence, version-control, and multi-agent tooling, but must degrade cleanly when those optional components are absent.
