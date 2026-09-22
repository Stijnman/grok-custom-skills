---
name: agent-red-team
description: "Defensive safety review for AI agents, tools, MCP servers, and skills. Use when an authorized owner asks to red-team their own agent, review prompt-injection resilience, assess tool-abuse risks, or harden an AI workflow before release."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
---

# Agent Red Team

Authorized defensive testing for AI systems the user owns or is explicitly permitted to assess.

## When to use

- Before publishing an agent, skill, or MCP integration.
- When reviewing prompt-injection resilience or excessive tool permissions.
- When checking whether untrusted content can influence privileged actions.
- When validating human-approval gates and sensitive-data handling.

## Boundaries

- Work only on owned or explicitly authorized systems.
- Prefer static review, synthetic probes, staging environments, and read-only checks.
- Do not target unrelated third-party systems.
- Do not collect credentials, personal data, or private content.
- Do not create malware or destructive payloads.
- Require human approval before consequential external actions.

## Workflow

1. Confirm target, authorization, environment, and in-scope components.
2. Map trust boundaries across prompts, retrieved content, memory, tools, and external services.
3. Review injection resistance, authorization checks, least privilege, sensitive-data handling, and human-approval gates.
4. Use synthetic, non-destructive test inputs where dynamic testing is appropriate.
5. Record reproducible evidence without retaining secrets or personal data.
6. Rate each finding by impact and likelihood.
7. Recommend concrete fixes such as allowlists, schema validation, isolation, reduced permissions, or approval gates.
8. Re-test the corrected behavior.

## Output

Return:
1. Scope and authorization.
2. Surface map.
3. Findings with severity, evidence, impact, and remediation.
4. Three highest-priority fixes.
5. Residual risk and untested areas.

If no findings are discovered, state exactly what was tested and what remains outside scope.
