---
name: multi-agent-orchestrator
description: Plan and coordinate work across multiple agents, delegate bounded tasks, and synthesize results with clear ownership and evidence. Use when the user asks for parallel research, multi-agent coordination, or a multi-step task that benefits from independent work. Confirm scope and obtain explicit approval before external writes or delegated state changes.
license: MIT
metadata:
  version: "1.51.0"
  type: workflow
---
# Multi-Agent Orchestrator

## Workflow
1. **Define the goal** — Restate deliverables, constraints, available tools, and the user-approved scope. Ask before delegating access to sensitive data or systems.
2. **Decompose** — Split work into independent, bounded subtasks with non-overlapping file ownership. Assign an owner and acceptance criteria for each.
3. **Delegate** — Give each worker only the information and access needed. State that workers must not exceed scope, modify files owned by another worker, or take external actions without explicit user approval.
4. **Track limits** — Respect tool, time, and batch limits. If the request exceeds capacity, complete the highest-priority tranche and list deferred work by name; never imply unfinished work was completed.
5. **Review** — Check outputs for evidence, consistency, safety, and overlap. Resolve conflicts by returning to source evidence rather than voting.
6. **Integrate** — Make only approved changes within the assigned ownership boundary. Preserve existing user changes and run relevant validation.
7. **Report** — Separate completed, deferred, and blocked work; identify files/actions and validation performed. Never invent agents, tools, dates, results, or approvals.

## Approval boundaries
- Delegation is not authorization for a worker to send messages, publish, upload, purchase, install, deploy, or alter production systems.
- Before any external write or destructive action, state the target and effect and obtain explicit user approval.
- Do not create a parallel/shadow skills library when the configured root is missing; report the missing location and ask how to proceed.

## Version
1.51.0 — Replaced stale host-specific directions with portable, approval-gated delegation and honest reporting.
