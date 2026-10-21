#!/usr/bin/env python3
"""Validate basic quality standards for every skill package in the collection."""

from __future__ import annotations

import re
from pathlib import Path

from generate_catalog import field, frontmatter

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / ".grok" / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_collection(root: Path = ROOT) -> tuple[int, list[str]]:
    """Return package count and errors without printing, exiting, or changing files."""
    errors: list[str] = []
    files = sorted(root.glob("*/SKILL.md"))
    if not files:
        errors.append("No skill definitions found.")
    if root.is_dir():
        for directory in sorted(root.iterdir()):
            if directory.is_dir() and not directory.name.startswith("."):
                if not (directory / "SKILL.md").is_file():
                    errors.append(f"{directory}: missing SKILL.md")

    for skill_file in files:
        try:
            text = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{skill_file}: cannot read UTF-8 text ({error})")
            continue
        block = frontmatter(text)
        name = field(block, "name")
        description = field(block, "description")
        if not block:
            errors.append(f"{skill_file}: missing frontmatter")
        if not name:
            errors.append(f"{skill_file}: missing name")
        elif not NAME_PATTERN.fullmatch(name) or len(name) > 64:
            errors.append(f"{skill_file}: name must be lowercase hyphenated and at most 64 characters")
        elif name != skill_file.parent.name:
            errors.append(f"{skill_file}: name does not match directory")
        if not description:
            errors.append(f"{skill_file}: missing description")
        elif len(description) > 1024:
            errors.append(f"{skill_file}: description exceeds 1024 characters")
        elif "use for:" not in description.lower() and "use when" not in description.lower():
            errors.append(f"{skill_file}: description does not state when to use the skill")
        if not re.search(r"^#\s+\S+", text, flags=re.M):
            errors.append(f"{skill_file}: missing H1 title")
        if len(text.splitlines()) > 500:
            errors.append(f"{skill_file}: exceeds 500 lines")
    return len(files), errors


def main() -> int:
    count, errors = validate_collection()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {count} skill definitions successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
