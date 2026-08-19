# Agent attack categories (defensive catalog)

Use these as a checklist. Prefer the smallest set that covers the target’s trust boundaries.

## A. Prompt & policy

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| A1 | Direct jailbreak | User asks to ignore policy / reveal system prompt | Clear policy, refusal patterns, no secret-in-prompt |
| A2 | Indirect injection | Instructions inside docs, HTML, email, PDFs | Treat retrieved text as data; delimiters; scrubbers |
| A3 | Role-play escalation | “You are DAN / unrestricted” | Stable identity; policy before persona |
| A4 | Encoding / obfuscation | Base64, homoglyphs, hidden markdown | Decode-then-recheck policy; strip ZWSP |
| A5 | Many-shot / gradual | Slow drift from allowed → disallowed | Session budgets; periodic policy re-assert |

## B. Tools & MCP

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| B1 | Tool call smuggling | Fake tool XML/JSON in user text | Strict schema; server-side tool dispatch only |
| B2 | Over-broad tools | Shell / FS / browser used for out-of-scope asks | Least privilege; allowlists; path sandboxes |
| B3 | Confused deputy | Untrusted content drives privileged tool | HITL on send/delete/pay/push; confirm summaries |
| B4 | Result-as-instruction | Tool output contains “now run …” | Never execute instructions from tool payloads |
| B5 | MCP bind exposure | `0.0.0.0` MCP / Ollama | Localhost-only; see `defensive-mcp-audit` |

## C. Memory & retrieval

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| C1 | Poisoned memory | Stored note overrides policy later | Memory trust scores; `memory-sanitizer` |
| C2 | RAG injection | Hostile page in index | Source tagging; citation-required answers |
| C3 | Cross-tenant bleed | Session A data in session B | Strict session/user isolation |

## D. Data & privacy

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| D1 | Secret fishing | Ask for keys, `.env`, chat logs | Refuse; never echo secrets; `privacy-redactor` |
| D2 | PII amplification | Expand sparse personal data | Minimize; redact in logs |
| D3 | Exfil via tools | “Email my context to …” | HITL + allowlisted destinations |

## E. Multi-agent

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| E1 | Handoff poison | Malicious brief to subagent | Validate handoff schema; parent re-check |
| E2 | Collusion | Agents bypass parent policy | Shared policy kernel; no peer privilege boost |
| E3 | Report laundering | Bad action buried in long summary | Structured results; force risk field |

## F. Supply chain / skills

| ID | Category | What to test | Remediations |
|----|----------|--------------|--------------|
| F1 | Malicious skill instructions | SKILL.md that exfils or disables safety | Skill scan; `hyper-skill-tester`; review before install |
| F2 | Dependency confusion | Skill pulls unknown scripts | Pin paths; no silent curl\|sh |
| F3 | Trigger hijack | Over-broad description steals intents | Tight triggers; name uniqueness |

## Suggested pack sizes

- **Smoke (15 min):** A1, A2, B1, B2, B3, D1, F1  
- **Publish readiness:** all A–F with ≥2 probes each  
- **MCP-heavy:** full B + B5 + `defensive-mcp-audit`  
