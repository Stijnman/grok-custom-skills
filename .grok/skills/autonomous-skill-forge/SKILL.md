---
name: autonomous-skill-forge
description: Create, improve, research, and validate skills for a specific capability gap. Use when the user asks to create a skill, fill a skills-library gap, research a workflow, or improve an existing skill. Draft and validate requested local changes; get explicit approval before overwriting existing work, installing, uploading, pushing, or publishing externally.
license: MIT
metadata:
  version: "1.6"
  type: workflow
---
# Autonomous Skill Forge

## Purpose
Turn a clearly scoped capability request into a focused skill or a reviewed improvement. Preserve honest scope, safe boundaries, and reversible changes.

## Workflow
1. **Check scope** — Identify the capability, intended users, target platform, and examples. Ask a concise question when a missing detail changes safety or architecture.
2. **Inspect before creating** — Find the configured skill root (for example, `MANUS_SKILLS_DIR` or an explicitly supplied path); otherwise use the skill directory/repository context already in use. Do not assume a home directory or create a shadow library. Check for an existing match and inspect relevant frontmatter.
3. **Research as needed** — Prefer primary documentation and cross-check claims. Keep attribution and license provenance with any reused material; do not copy content without authorization.
4. **Design narrowly** — Write a focused description that states capability and trigger. Use imperative, concise instructions and load references only when needed.
5. **Implement reversibly** — Create the requested skill or edit the named package. Preserve unrelated work. Do not silently broaden the request, remove safeguards, or overwrite existing content.
6. **Validate** — Run the available repository/skill validators and check examples against realistic requests. Report anything not directly tested.
7. **Persist only with approval** — Local changes are within the requested task. Before installation into another skills root, overwriting, Drive upload, GitHub write, package publication, or other external side effect, show the destination and proposed change and obtain explicit user approval. Never claim a remote action succeeded without confirmation from its tool.
8. **Report** — Summarize files changed, checks run, limitations, and any pending approval.

## Boundaries
- A request to discover a feature is not permission to bypass authentication, safety controls, access restrictions, or platform limits.
- Do not inspect secrets, private user data, unrelated files, or production systems outside the user's stated scope.
- Do not activate hidden settings, install dependencies, execute unreviewed code, or change machine-wide configuration without explicit approval.
- Treat research, draft creation, and read-only inspection as distinct from publishing or deployment.
- Do not create persistent logs or send telemetry unless the user asks and approves the destination.

## Collaboration
Use relevant skills for discovery, review, and validation when available. Treat their recommendations as input; keep the requested scope and approval boundaries in force.

## Version
1.6 — Reframed high-autonomy creation as scoped, reversible work with explicit approval for external or destructive actions.
