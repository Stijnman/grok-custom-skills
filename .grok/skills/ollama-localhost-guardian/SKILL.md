---
name: ollama-localhost-guardian
description: >
  Verifies local LLM services (e.g. Ollama) are bound to localhost only. Usewh
  en checking Ollama security or user says is ollama exposed, secure localLLM.
   Read-only network and config checks. Triggers: ollama security, localhostLL
  M, secure ollama.
version: 1.0.0
author: Stijnman
license: MIT
compatibility: Grok agent; optional MCP and shell access
metadata:
  grok:
    tags: [ollama security, is ollama exposed, secure local LLM, ollama localhost]
    related_skills: [defensive-mcp-audit, exposed-service-triage, hitl-approver]
    publication_reviewed: '2026-06-24'
---

# Ollama Localhost Guardian

## When to Use

- User says **ollama security** or task matches this capability
- User says **is ollama exposed** or task matches this capability
- User says **secure local LLM** or task matches this capability
- User says **ollama localhost** or task matches this capability

## Workflow

1. Check listener on default Ollama port (11434) via ss or netstat.
2. Pass if bound to 127.0.0.1; warn if 0.0.0.0 or ::.
3. Optionally check OLLAMA_HOST env and systemd override files (read-only).
4. Recommend binding to 127.0.0.1; hitl-approver before config changes.
5. Note installed AI packages (mcp, openai, etc.) for inventory only.

## Integrations

- `defensive-mcp-audit`
- `exposed-service-triage`
- `hitl-approver`

## Error Handling

| Failure | Response |
|---------|----------|
| Ollama not running | Report not listening; no install assumed. |

## Gotchas

- Check-only; config edits require user approval.

## Safety & Ethics (Publication-Ready)

This skill is designed for public distribution. Constraints:

- Read-only checks; no model pulling or inference API abuse.
- No exposure of API keys or model weights.

### Prohibited actions

- No unauthorized access, malware, or harmful automation
- No silent exfiltration of data, credentials, or telemetry
- No destructive system changes without hitl-approver
- No publication of user PII or environment secrets in outputs

## Example

**Input:** User request matching triggers above.
**Output:** Structured result per workflow; local artifacts only unless user opts in.
