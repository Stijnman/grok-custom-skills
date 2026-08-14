#!/usr/bin/env python3
"""Validate basic quality standards for every skill package in the collection."""

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / ".grok" / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end >= 0 else ""


def field(block: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", block, flags=re.M)
    if not match:
        return ""
    value = match.group(1).strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value.strip("'\"")


errors = []
files = sorted(ROOT.glob("*/SKILL.md"))
if not files:
    errors.append("No skill definitions found.")

for skill_file in files:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    block = frontmatter(text)
    name = field(block, "name")
    description = field(block, "description")
    if not block:
        errors.append(f"{skill_file}: missing frontmatter")
    if not name:
        errors.append(f"{skill_file}: missing name")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_file}: name is not lowercase hyphenated")
    elif name != skill_file.parent.name:
        errors.append(f"{skill_file}: name does not match directory")
    if not description:
        errors.append(f"{skill_file}: missing description")
    elif "use for:" not in description.lower() and "use when" not in description.lower():
        errors.append(f"{skill_file}: description does not state when to use the skill")
    if not re.search(r"^#\s+\S+", text, flags=re.M):
        errors.append(f"{skill_file}: missing H1 title")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_file}: exceeds 500 lines")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"Validated {len(files)} skill definitions successfully.")
