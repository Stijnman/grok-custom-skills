#!/usr/bin/env python3
"""Run full skill optimization and compliance pipeline (2026 tooling)."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".grok" / "skills"


def run(cmd: list[str], label: str) -> int:
    print(f"\n=== {label} ===")
    r = subprocess.run(cmd, cwd=ROOT)
    return r.returncode


def skills_ref_validate() -> int:
    from skills_ref import validate, ValidationError

    ok = fail = 0
    print("\n=== skills-ref validate (agentskills.io) ===")
    for d in sorted(SKILLS.iterdir()):
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            continue
        try:
            validate(d)
            ok += 1
        except ValidationError as e:
            fail += 1
            print(f"  FAIL {d.name}: {e}")
    print(f"  {ok} ok, {fail} fail")
    return 1 if fail else 0


def fix_descriptions() -> int:
    """Ensure descriptions include 'Use when' + Triggers per agentskills.io guide."""
    print("\n=== description optimizer ===")
    fixed = 0
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm, body = parts[1], parts[2]
        name = skill_md.parent.name

        # Extract triggers from body When to Use section
        triggers = re.findall(r"\*\*([^*]+)\*\*", body.split("## Workflow")[0] if "## Workflow" in body else body)
        triggers = [t.strip() for t in triggers if len(t.strip()) < 40][:4]
        if not triggers:
            m = re.search(r"tags:\s*\[([^\]]+)\]", fm)
            if m:
                triggers = [t.strip() for t in m.group(1).split(",")][:4]

        desc_block = re.search(r"(description:\s*>?\s*\n(?:  .+\n|  .+)+)", fm)
        if not desc_block:
            continue
        desc_lines = [l.strip() for l in desc_block.group(1).splitlines() if l.strip().startswith("description:") or l.startswith("  ")]
        # Join wrapped YAML lines without spaces (wrap breaks words mid-token)
        desc_text = "".join(
            l.replace("description: >", "").strip()
            for l in desc_lines
            if not l.strip().startswith("description:")
        )

        has_when = any(
            p in desc_text.lower()
            for p in ("use when", "use this skill when", "use before", "use for", "use after")
        )
        needs_fix = (not has_when) or "triggers:" not in desc_text.lower()

        if not needs_fix:
            continue

        if not has_when:
            desc_text = desc_text.rstrip(".") + ". Use when the user needs this capability."
        if triggers and "triggers:" not in desc_text.lower():
            desc_text += f" Triggers: {', '.join(triggers[:4])}."

        # Rebuild frontmatter description
        wrapped = []
        for i in range(0, len(desc_text), 78):
            wrapped.append("  " + desc_text[i : i + 78])
        new_fm = re.sub(
            r"description:\s*>?\s*\n(?:  .+\n)*",
            "description: >\n" + "\n".join(wrapped) + "\n",
            fm,
            count=1,
        )
        if "compatibility:" not in new_fm:
            new_fm = new_fm.rstrip() + "\ncompatibility: Grok agent; optional MCP and shell access\n"

        new_text = "---" + new_fm + "---" + body
        skill_md.write_text(new_text, encoding="utf-8")
        fixed += 1
        print(f"  fixed {name}")

    print(f"  {fixed} descriptions updated")
    return 0


def add_validation_checklists() -> int:
    """Add pre-publish checklist to skill-rubric-reviewer if missing."""
    path = SKILLS / "skill-rubric-reviewer" / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Pre-publish validation loop"
    if marker in text:
        return 0
    insert = """
## Pre-publish validation loop

Run before publishing any skill:

```bash
python3 scripts/check_no_private_data.py
python3 scripts/publish_safety_check.py
python3 scripts/optimize_all_skills.py --validate-only
```

- [ ] `skills-ref` validation passes
- [ ] Description includes *what*, *when*, and *Triggers*
- [ ] No private emails, paths, or LAN IPs
- [ ] `hitl-approver` referenced for destructive ops

"""
    text = text.replace("## Workflow", insert + "## Workflow", 1)
    path.write_text(text, encoding="utf-8")
    print("  added validation loop to skill-rubric-reviewer")
    return 0


def main() -> int:
    validate_only = "--validate-only" in sys.argv
    codes = []

    if not validate_only:
        codes.append(fix_descriptions())
        codes.append(add_validation_checklists())

    codes.append(run([sys.executable, "scripts/check_no_private_data.py"], "private data scan"))
    codes.append(run([sys.executable, "scripts/publish_safety_check.py"], "safety scan"))
    codes.append(skills_ref_validate())

    failed = sum(1 for c in codes if c != 0)
    print(f"\n=== pipeline complete: {failed} stage(s) failed ===")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())