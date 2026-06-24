#!/usr/bin/env python3
"""Regenerate SKILLS_INDEX.md from all SKILL.md files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / ".grok" / "skills"


def main() -> None:
    entries: list[tuple[str, str]] = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        name = skill_md.parent.name
        desc = ""
        m = re.search(r"description:\s*>\s*\n((?:  .+\n)+)", text)
        if m:
            desc = "".join(line.strip() for line in m.group(1).splitlines())
        else:
            m2 = re.search(r'description:\s*"(.+)"', text, re.S)
            if m2:
                desc = m2.group(1).replace("\n", " ")
        short = desc.split(". ")[0].strip()
        if short and not short.endswith("."):
            short += "."
        entries.append((name, short))

    lines = [
        "# Skills Index",
        "",
        f"**Total:** {len(entries)} skills",
        "",
        "| Skill | Summary |",
        "|-------|---------|",
    ]
    for name, short in entries:
        lines.append(f"| [{name}](.grok/skills/{name}/SKILL.md) | {short} |")

    out = ROOT / "SKILLS_INDEX.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} skills)")


if __name__ == "__main__":
    main()