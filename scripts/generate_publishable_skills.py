#!/usr/bin/env python3
"""Generate publishable-safe session-derived skills."""

from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / ".grok" / "skills"

# publication_safe: explicit constraints for public release
SKILLS: dict[str, dict] = {
    "defensive-mcp-audit": {
        "description": (
            "Runs a defensive, read-only security audit of the local machine for MCP "
            "and AI agent risks: risky bindings, MCP config issues, and confused-deputy "
            "exposure. Use before enabling MCP servers or when the user says audit mcp, "
            "check localhost exposure, mcp security. Outputs text, JSON, SARIF, or HTML. "
            "Triggers: audit mcp, mcp security, defensive-mcp-audit."
        ),
        "workflow": [
            "Confirm audit is read-only; no port scanning beyond localhost inventory.",
            "Run: python3 -m defensive_mcp_audit (or pip install defensive-mcp-audit[cli]).",
            "Parse risk_level, risk_score, and findings table.",
            "Explain each finding in plain language with remediation (bind localhost, disable service).",
            "Never suggest attack techniques, malware, or penetration tests.",
            "Offer HTML/JSON export path; do not upload reports externally without user consent.",
        ],
        "triggers": ["audit mcp", "mcp security", "localhost exposure", "defensive-mcp-audit"],
        "integrations": ["exposed-service-triage", "mcp-tool-scout", "hitl-approver"],
        "errors": {
            "Tool not installed": "pip install defensive-mcp-audit[cli] or clone github.com/Stijnman/defensive-mcp-audit.",
            "Permission denied on ss": "Report limitation; suggest user-run with adequate permissions.",
        },
        "gotchas": ["Defensive only — inspection, not exploitation."],
        "publication_safe": [
            "Read-only inspection; no network attacks or exploitation.",
            "Reports stay local unless user explicitly requests upload.",
            "Remediation advice is configuration-only (bind, disable, firewall).",
        ],
        "license_note": "Wraps the MIT-licensed defensive-mcp-audit project by Stijnman.",
    },
    "github-repo-scout": {
        "description": (
            "Investigates a GitHub repository from a URL: README, file tree, local clone "
            "status, and recommended next steps. Use when the user pastes a github.com URL "
            "or says check this repo, what is this project. Read-only; no credential access. "
            "Triggers: github URL, check this repo, scout repo."
        ),
        "workflow": [
            "Parse owner/repo from URL; reject non-GitHub hosts unless user confirms.",
            "Fetch README and top-level tree via public API or git clone (read-only).",
            "Compare README claims vs actual committed files (note drift).",
            "Check if repo exists locally in workspace or common clone paths.",
            "Summarize: purpose, install steps, risks, suggested actions (clone, audit, review).",
            "Do not access private repos without authenticated user context.",
        ],
        "triggers": ["github.com", "check this repo", "scout repo", "what is this project"],
        "integrations": ["oss-repo-maintainer", "defensive-mcp-audit", "skill-rubric-reviewer"],
        "errors": {
            "404/private repo": "State access limitation; ask user to clone locally.",
            "Rate limited": "Backoff; use local clone if available.",
        },
        "gotchas": ["Public repos only unless user has authenticated MCP/GitHub access."],
        "publication_safe": [
            "Read-only repository inspection.",
            "No harvesting of tokens, secrets, or private issue content.",
            "Do not auto-clone into system directories without user approval.",
        ],
    },
    "skill-collection-bootstrapper": {
        "description": (
            "Audits a skills repository, fills gaps, validates SKILL.md files, and "
            "installs to the user skills directory. Use when completing a skill "
            "collection or user says bootstrap skills, install skill repo. "
            "Triggers: bootstrap skills, complete skill collection, install skill repo."
        ),
        "workflow": [
            "Inventory SKILL.md files vs README skill list; report missing names.",
            "Run skill-rubric-reviewer on stubs scoring below 30/50.",
            "Regenerate or patch weak skills; validate frontmatter and required sections.",
            "Show diff summary before install; require user approval to overwrite existing skills.",
            "Copy approved skills to ~/.grok/skills/ or workspace .grok/skills/.",
            "Update SKILLS_INDEX.md if maintaining a repo.",
        ],
        "triggers": ["bootstrap skills", "complete skill collection", "install skill repo"],
        "integrations": ["skill-rubric-reviewer", "skill-evolver", "hitl-approver", "goal-verifier"],
        "errors": {
            "Name collision": "List conflicts; default to skip unless user approves overwrite.",
            "Validation fail": "Block install for failed SKILL.md; report path and errors.",
        },
        "gotchas": ["Never overwrite bundled skills without explicit user approval."],
        "publication_safe": [
            "User must approve before overwriting installed skills.",
            "No execution of untrusted scripts from skill folders during bootstrap.",
            "Validate SKILL.md structure before install.",
        ],
    },
    "mcp-tool-scout": {
        "description": (
            "Discovers MCP servers and reads tool schemas before calling MCP tools. "
            "Use before MCP invocations or when user says what MCP tools, check MCP schema. "
            "Read-only filesystem inspection of MCP descriptors. "
            "Triggers: mcp tools, MCP schema, discover MCP."
        ),
        "workflow": [
            "List MCP server folders (e.g. mcps/<server>/tools/*.json).",
            "Match user task keywords to available tool names and descriptions.",
            "Read full inputSchema for chosen tool before any CallMcpTool.",
            "Report missing auth or server instructions; do not guess parameters.",
            "Prefer least-privilege tool selection.",
        ],
        "triggers": ["mcp tools", "MCP schema", "discover MCP", "which MCP tool"],
        "integrations": ["tool-discovery-engine", "defensive-mcp-audit", "hitl-approver"],
        "errors": {
            "Schema missing": "Stop; do not call tool without reading descriptor.",
            "Auth required": "Ask user to complete auth out-of-band; never embed secrets in skill.",
        },
        "gotchas": ["Mandatory schema read prevents parameter injection mistakes."],
        "publication_safe": [
            "Read-only discovery; no MCP calls without user task context.",
            "Never log or publish auth tokens from MCP configs.",
            "Tool paths use forward slashes; no Windows credential stores.",
        ],
    },
    "exposed-service-triage": {
        "description": (
            "Triages exposed TCP listeners found by security audits. Identifies processes "
            "on risky bindings and recommends safe remediation. Use after mcp audit or when "
            "user asks what is on port X, fix exposed service. "
            "Triggers: exposed port, what is listening, fix exposed service."
        ),
        "workflow": [
            "Run read-only listener inventory (ss -tln, fuser) on user machine.",
            "Map ports to processes; classify MCP-related vs system vs unknown.",
            "Present findings table with risk tier and plain-language explanation.",
            "Recommend: bind 127.0.0.1, disable service, or firewall rule.",
            "Before stopping/disabling any service: hitl-approver required.",
            "Never run aggressive remote scans or attack exposed services.",
        ],
        "triggers": ["exposed port", "what is listening", "fix exposed service", "open port"],
        "integrations": ["defensive-mcp-audit", "hitl-approver"],
        "errors": {
            "Cannot identify process": "Report port and binding; suggest sudo ss -tlnp with user consent.",
            "User requests aggressive scan": "Decline; offer defensive audit only.",
        },
        "gotchas": ["Common OS services on 0.0.0.0 may be intentional; explain before recommending disable."],
        "publication_safe": [
            "Read-only discovery first; service changes only after HITL approval.",
            "No denial-of-service, exploitation, or unauthorized access attempts.",
            "Remediation is documented steps for the user or admin to apply.",
        ],
    },
    "skill-rubric-reviewer": {
        "description": (
            "Reviews SKILL.md files against a 10-dimension quality rubric inspired by the "
            "Agent Skills specification. Use when auditing skills before publish or user "
            "says review skill, score SKILL.md, skill quality audit. "
            "Triggers: review skill, skill rubric, audit SKILL.md."
        ),
        "workflow": [
            "Read SKILL.md and any references/, scripts/, assets/.",
            "Score 10 dimensions (frontmatter, description, conciseness, structure, clarity, "
            "freedom, errors, disclosure, scripts, completeness) 1-5 each.",
            "List issues for dimensions scoring 3 or below.",
            "Provide before/after rewrite suggestions; apply only if user requests.",
            "Flag publication blockers: secrets, harmful instructions, undeclared telemetry, PII in logs.",
        ],
        "triggers": ["review skill", "skill rubric", "audit SKILL.md", "score skill quality"],
        "integrations": ["skill-evolver", "hyper-skill-tester", "privacy-redactor"],
        "errors": {
            "Missing SKILL.md": "Report path; do not score directory without file.",
        },
        "gotchas": ["Rubric inspired by Agent Skills spec; independent implementation."],
        "publication_safe": [
            "Reviews content for safety before publish; blocks skills with harmful instructions.",
            "No automatic submission of reviews to external services without user consent.",
            "Does not exfiltrate skill contents to third parties.",
        ],
        "license_note": "Rubric aligned with Agent Skills spec best practices; original skill text.",
    },
    "skill-marketplace-installer": {
        "description": (
            "Safely searches and installs agent skills from public marketplaces (e.g. "
            "agentskill.sh) with user consent and security checks. Use when user says "
            "find skill, install skill from marketplace, /learn. "
            "Triggers: find skill, install skill, skill marketplace, check skill safety."
        ),
        "workflow": [
            "Search marketplace via documented CLI (npx @agentskill.sh/cli search).",
            "Show skill name, owner, description, and ratings before install.",
            "Require explicit user approval before install.",
            "Run security scan if CLI supports it; warn on suspicious patterns.",
            "Install to user skills directory; list what was added.",
            "Never install skills requesting credentials in SKILL.md without user review.",
        ],
        "triggers": ["find skill", "install skill", "skill marketplace", "check skill safety"],
        "integrations": ["skill-rubric-reviewer", "hitl-approver", "privacy-redactor"],
        "errors": {
            "CLI unavailable": "Document manual install from source URL with rubric review first.",
            "Scan flags risk": "Block install; explain finding; offer alternatives.",
        },
        "gotchas": ["Third-party skills are untrusted until reviewed with skill-rubric-reviewer."],
        "publication_safe": [
            "User consent required before every install.",
            "Recommends security scan before install when available.",
            "Attributes agentskill.sh CLI; does not bundle proprietary marketplace code.",
            "No silent telemetry or auto-rating posts in this skill.",
        ],
        "license_note": "Compatible with agentskill.sh CLI; marketplace terms apply to installed skills.",
    },
    "session-handoff-packager": {
        "description": (
            "Packages session work into a local handoff document for continuity. "
            "Use when saving progress or user says session summary, handoff, what we did. "
            "Triggers: session summary, handoff, save what we did."
        ),
        "workflow": [
            "List: repos explored, commands run, files created/changed, key findings.",
            "Note open items and recommended next steps.",
            "Run privacy-redactor on content before any external share.",
            "Write session-handoff.md to workspace (local only by default).",
            "Do not include secrets, tokens, or raw PII in handoff.",
        ],
        "triggers": ["session summary", "handoff", "save what we did", "continue next time"],
        "integrations": ["privacy-redactor", "ai-share-extractor-v4", "goal-verifier"],
        "errors": {
            "Workspace not writable": "Output handoff in chat only.",
        },
        "gotchas": ["Default is local file only; upload requires separate user request."],
        "publication_safe": [
            "PII redaction before share; secrets never included.",
            "Handoff stays in user workspace unless explicitly shared.",
            "Read-only summary of past actions; no new destructive operations.",
        ],
    },
    "ollama-localhost-guardian": {
        "description": (
            "Verifies local LLM services (e.g. Ollama) are bound to localhost only. "
            "Use when checking Ollama security or user says is ollama exposed, secure local LLM. "
            "Read-only network and config checks. "
            "Triggers: ollama security, localhost LLM, secure ollama."
        ),
        "workflow": [
            "Check listener on default Ollama port (11434) via ss or netstat.",
            "Pass if bound to 127.0.0.1; warn if 0.0.0.0 or ::.",
            "Optionally check OLLAMA_HOST env and systemd override files (read-only).",
            "Recommend binding to 127.0.0.1; hitl-approver before config changes.",
            "Note installed AI packages (mcp, openai, etc.) for inventory only.",
        ],
        "triggers": ["ollama security", "is ollama exposed", "secure local LLM", "ollama localhost"],
        "integrations": ["defensive-mcp-audit", "exposed-service-triage", "hitl-approver"],
        "errors": {
            "Ollama not running": "Report not listening; no install assumed.",
        },
        "gotchas": ["Check-only; config edits require user approval."],
        "publication_safe": [
            "Read-only checks; no model pulling or inference API abuse.",
            "No exposure of API keys or model weights.",
        ],
    },
    "oss-repo-maintainer": {
        "description": (
            "Helps maintain open-source repos: README accuracy, version consistency, "
            "and pre-release checklists. Use when syncing docs with repo reality or user "
            "says fix README, prep release, repo maintenance. "
            "Triggers: fix README, prep release, repo maintenance, sync docs."
        ),
        "workflow": [
            "Diff README skill/file lists vs git tree.",
            "Flag stale counts, missing install paths, broken links.",
            "Propose README and CHANGELOG edits; show diff before commit.",
            "Run validators (tests, skill validate) if present in repo.",
            "Suggest conventional commit message; hitl-approver before git push.",
        ],
        "triggers": ["fix README", "prep release", "repo maintenance", "sync docs"],
        "integrations": ["github-repo-scout", "skill-collection-bootstrapper", "goal-verifier"],
        "errors": {
            "Not a git repo": "Limit to file review only.",
        },
        "gotchas": ["Never push or publish without explicit user approval."],
        "publication_safe": [
            "Documentation accuracy focus; no unauthorized releases.",
            "Git push and publish require hitl-approver.",
            "Generic OSS workflow; no hardcoded user or org paths in instructions.",
        ],
    },
}


def format_skill_md(name: str, spec: dict) -> str:
    desc = spec["description"]
    triggers = spec["triggers"]
    workflow = spec["workflow"]
    errors = spec.get("errors", {})
    integrations = spec.get("integrations", [])
    gotchas = spec.get("gotchas", [])
    pub_safe = spec.get("publication_safe", [])
    license_note = spec.get("license_note", "")

    trigger_str = ", ".join(triggers[:6])
    related = ", ".join(integrations[:8])

    lines = [
        "---",
        f"name: {name}",
        "description: >",
    ]
    for para_line in textwrap.wrap(desc, width=78):
        lines.append(f"  {para_line}")
    lines.extend([
        "version: 1.0.0",
        "author: Stijnman",
        "license: MIT",
        "metadata:",
        "  grok:",
        f"    tags: [{trigger_str}]",
        f"    related_skills: [{related}]",
        "    publication_reviewed: '2026-06-24'",
        "---",
        "",
        f"# {name.replace('-', ' ').title()}",
        "",
        "## When to Use",
        "",
    ])
    for t in triggers:
        lines.append(f"- User says **{t}** or task matches this capability")
    lines.extend(["", "## Workflow", ""])
    for i, step in enumerate(workflow, 1):
        lines.append(f"{i}. {step}")
    lines.extend(["", "## Integrations", ""])
    for skill in integrations:
        lines.append(f"- `{skill}`")
    lines.extend(["", "## Error Handling", "", "| Failure | Response |", "|---------|----------|"])
    for err, resp in errors.items():
        lines.append(f"| {err} | {resp} |")
    lines.extend(["", "## Gotchas", ""])
    for g in gotchas:
        lines.append(f"- {g}")
    lines.extend([
        "",
        "## Safety & Ethics (Publication-Ready)",
        "",
        "This skill is designed for public distribution. Constraints:",
        "",
    ])
    for rule in pub_safe:
        lines.append(f"- {rule}")
    lines.extend([
        "",
        "### Prohibited actions",
        "",
        "- No unauthorized access, malware, or harmful automation",
        "- No silent exfiltration of data, credentials, or telemetry",
        "- No destructive system changes without hitl-approver",
        "- No publication of user PII or environment secrets in outputs",
        "",
    ])
    if license_note:
        lines.extend(["### Attribution", "", f"- {license_note}", ""])
    lines.extend([
        "## Example",
        "",
        "**Input:** User request matching triggers above.",
        "**Output:** Structured result per workflow; local artifacts only unless user opts in.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, spec in sorted(SKILLS.items()):
        d = ROOT / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(format_skill_md(name, spec), encoding="utf-8")
        print(f"  wrote {name}")
    print(f"\nTotal: {len(SKILLS)} publishable skills")


if __name__ == "__main__":
    main()