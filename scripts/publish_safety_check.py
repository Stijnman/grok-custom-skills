#!/usr/bin/env python3
"""Pre-publish safety audit for SKILL.md files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parent.parent / ".grok" / "skills"

# Patterns that block publication (unless negated: No/Never/not)
BLOCK_PATTERNS = [
    (r"\bsilent(ly)?\s+(POST|submit|upload|exfil)", "silent telemetry/exfil"),
    (r"\b(exploits?|payloads?|0day|bypass\s+auth)\b", "offensive language"),
    (r"/home/[a-zA-Z0-9_-]+/", "hardcoded user home path"),
    (r"(api[_-]?key|secret|password)\s*[:=]\s*['\"][^'\"]+['\"]", "embedded secret"),
    (r"\bauto[- ]?rate\b.*agentskill", "silent agentskill rating"),
]

NEGATION_PREFIXES = ("no ", "not ", "never ", "without ", "prohibited", "don't ", "do not ")

# Publishable session skills require Safety section
REQUIRE_SAFETY = {
    "defensive-mcp-audit",
    "github-repo-scout",
    "skill-collection-bootstrapper",
    "mcp-tool-scout",
    "exposed-service-triage",
    "skill-rubric-reviewer",
    "skill-marketplace-installer",
    "session-handoff-packager",
    "ollama-localhost-guardian",
    "oss-repo-maintainer",
}

REQUIRED_FRONTMATTER = ("name:", "description:", "license:")


def audit(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    name = path.parent.name

    if not text.startswith("---"):
        issues.append("missing frontmatter")
        return issues

    for key in REQUIRED_FRONTMATTER:
        if key not in text.split("---", 2)[1]:
            issues.append(f"missing frontmatter {key.strip(':')}")

    for pattern, label in BLOCK_PATTERNS:
        for match in re.finditer(pattern, text, re.I):
            window = text[max(0, match.start() - 48) : match.start()].lower()
            if any(window.endswith(p) or p in window for p in NEGATION_PREFIXES):
                continue
            issues.append(f"blocked pattern ({label})")
            break

    if name in REQUIRE_SAFETY and "## Safety & Ethics" not in text:
        issues.append("missing Safety & Ethics section")

    if "Prohibited actions" not in text and name in REQUIRE_SAFETY:
        issues.append("missing Prohibited actions list")

    return issues


def main() -> int:
    failed = 0
    checked = 0
    for skill_md in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        checked += 1
        issues = audit(skill_md)
        if issues:
            failed += 1
            print(f"FAIL {skill_md.parent.name}: {', '.join(issues)}")
        else:
            rel = skill_md.relative_to(SKILLS_ROOT.parent.parent)
            print(f"OK   {rel}")

    print(f"\nChecked {checked} skills, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())