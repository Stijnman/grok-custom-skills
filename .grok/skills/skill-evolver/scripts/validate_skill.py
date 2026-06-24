#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and required sections."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = (
    "## When to Use",
    "## Workflow",
    "## Error Handling",
    "## Gotchas",
)

REQUIRED_FRONTMATTER = ("name:", "description:")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        errors.append("Missing YAML frontmatter")
        return errors

    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("Malformed frontmatter fences")
        return errors

    frontmatter, body = parts[1], parts[2]
    for key in REQUIRED_FRONTMATTER:
        if key not in frontmatter:
            errors.append(f"Frontmatter missing {key}")

    name_match = re.search(r"^name:\s*(\S+)", frontmatter, re.M)
    if name_match and path.parent.name != name_match.group(1):
        errors.append(
            f"name '{name_match.group(1)}' does not match directory '{path.parent.name}'"
        )

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing section: {section}")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <path/to/SKILL.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Not found: {path}", file=sys.stderr)
        return 2

    errors = validate(path)
    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())