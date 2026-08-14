---
name: hybrid-execution-bridge
description: "Coordinate authorized work across sandbox tools, a user-approved local desktop, connected services, and public-web research. Use for: hybrid execution, local plus sandbox, connected services, scoped desktop access."
version: 1.1.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional browser, shell, desktop bridge, and connected-service access
metadata:
  grok:
    tags: [hybrid execution, local plus sandbox, connected services, scoped desktop access]
    related_skills: [computer-use-bridge, desktop-subagent-connector, connected-services-bridge, sandbox-internet-handler]
---

# Hybrid Execution Bridge

## Purpose

Use this skill to plan work that may span sandbox processing, user-approved local resources, connected services, and public-web research. Select the least-privileged environment for each step and keep external actions explicit.

## Routing workflow

1. Decompose the task into local, sandbox, connected-service, and public-web steps.
2. Use sandbox tools for code, documents, data processing, and ordinary public research whenever sufficient.
3. Use a local desktop bridge only after the user authorizes the scope and the bridge health check succeeds.
4. Use connected services only for the accounts and operations the user has approved.
5. Use responsible browsing methods; stop at login walls, CAPTCHAs, paywalls, or other access restrictions.
6. Present planned external writes, uploads, messages, deployments, or publications for explicit approval before carrying them out.
7. Summarize which environments were used, what data moved between them, and any limitations.

## Environment selection

| Need | Preferred environment | Boundary |
|---|---|---|
| Code, files, reports, or data analysis | Sandbox | Keep data within the task workspace unless the user authorizes export. |
| Existing user session, local software, or local files | Authorized desktop bridge | Verify scope and connection health; never assume access. |
| Drive, GitHub, or other connected account | Connected-service integration | Read first; require approval for writes or publication. |
| Public web information | Browser or approved research tool | Respect access restrictions and site rules. |

## Local desktop safeguards

When a user-authorized desktop bridge is needed, ask for clear permission, run its documented health check, and limit operations to the agreed files or application. Do not request or expose raw tokens in summaries. Stop immediately if the connection fails or the user revokes permission.

## Error handling

| Situation | Response |
|---|---|
| Local bridge is unavailable | Continue with sandbox alternatives and state the limitation. |
| Connected service lacks authorization | Do not retry with another account; ask the user to authorize or choose a local alternative. |
| Website presents a restriction | Stop automated access and explain the permitted options. |
| External action is pending | Present scope, destination, and user-visible effect; wait for approval. |

## Output

Return the execution plan, selected environments, authorization boundaries, completed work, and pending external actions. Do not claim that local, cloud, or connected-service work occurred unless it was verified.
