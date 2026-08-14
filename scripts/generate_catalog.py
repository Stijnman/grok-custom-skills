#!/usr/bin/env python3
"""Generate SKILLS_INDEX.md from .grok/skills/*/SKILL.md metadata."""

from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO / ".grok" / "skills"
OUTPUT = REPO / "SKILLS_INDEX.md"

CATEGORY_RULES = [
    ("Safety, Privacy & Governance", ("security", "privacy", "compliance", "defensive", "sandbox", "hitl", "guardian", "redactor", "humanization")),
    ("Skill Development & Operations", ("skill", "evolver", "evolution", "rubric", "marketplace", "catalog")),
    ("Workflow & Agent Orchestration", ("workflow", "agent", "orchestrator", "composer", "refine", "healing", "bottleneck", "uncertainty", "parallel")),
    ("Research, Web & Integrations", ("search", "scraper", "internet", "github", "mcp", "connector", "bridge", "tool-discovery")),
    ("Memory, Context & Knowledge", ("memory", "context", "knowledge", "preference", "cache", "handoff")),
    ("Media, Voice & Visuals", ("image", "video", "voice", "suno", "tts", "audio")),
    ("Messaging & Communication", ("whatsapp", "telegram", "messenger", "share", "humanizer")),
    ("Traffic & Navigation", ("waze", "traffic", "navigation")),
    ("Quality, Code & Performance", ("tester", "reviewer", "verifier", "performance", "visualizer", "insight")),
]


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end >= 0 else ""


def field(block: str, key: str) -> str:
    for line in block.splitlines():
        match = re.match(rf"^{re.escape(key)}:\s*(.+)$", line)
        if match:
            value = match.group(1).strip()
            if value.startswith('"') and value.endswith('"'):
                return value[1:-1].replace('\\"', '"')
            return value.strip("'\"")
    return ""


def category_for(name: str) -> str:
    lower = name.lower()
    for category, terms in CATEGORY_RULES:
        if any(term in lower for term in terms):
            return category
    return "General Utilities"


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


records = []
for skill_file in sorted(SKILLS_ROOT.glob("*/SKILL.md"), key=lambda item: item.parent.name.lower()):
    block = frontmatter(skill_file.read_text(encoding="utf-8", errors="replace"))
    name = field(block, "name") or skill_file.parent.name
    description = field(block, "description") or "No description provided."
    records.append({"name": name, "description": description, "path": skill_file.relative_to(REPO), "category": category_for(name)})

categories = {}
for record in records:
    categories.setdefault(record["category"], []).append(record)

lines = [
    "# Skills Catalog",
    "",
    f"This catalog is generated from the metadata in **{len(records)} skill definitions**. Run `python3 scripts/generate_catalog.py` after adding or changing a skill.",
    "",
    "## Browse by category",
    "",
    "| Category | Skills |",
    "|---|---:|",
]
for category in sorted(categories):
    lines.append(f"| {category} | {len(categories[category])} |")

lines.extend(["", "## Complete catalog", ""])
for category in sorted(categories):
    lines.extend([f"### {category}", "", "| Skill | Description |", "|---|---|"])
    for record in categories[category]:
        lines.append(f"| [`{cell(record['name'])}`]({record['path'].as_posix()}) | {cell(record['description'])} |")
    lines.append("")

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"catalog_skills={len(records)}")
print(f"catalog={OUTPUT}")
