#!/usr/bin/env python3
"""Generate a deterministic, newline-terminated SKILLS_INDEX.md catalog."""

from __future__ import annotations

from pathlib import Path
import re
import sys

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
    """Return the YAML-like frontmatter body, or an empty string if absent."""
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end >= 0 else ""


def field(block: str, key: str) -> str:
    """Extract a single-line frontmatter field without requiring a YAML dependency."""
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
    """Make text safe for a single Markdown-table cell."""
    return value.replace("|", "\\|").replace("\n", " ").strip()


def collect_records(skills_root: Path = SKILLS_ROOT) -> list[dict[str, str | Path]]:
    """Collect catalog records in a stable order from direct skill directories."""
    records: list[dict[str, str | Path]] = []
    for skill_file in sorted(skills_root.glob("*/SKILL.md"), key=lambda item: item.parent.name.lower()):
        block = frontmatter(skill_file.read_text(encoding="utf-8", errors="replace"))
        name = field(block, "name") or skill_file.parent.name
        description = field(block, "description") or "No description provided."
        records.append(
            {
                "name": name,
                "description": description,
                "path": skill_file.relative_to(REPO),
                "category": category_for(name),
            }
        )
    return records


def render_catalog(records: list[dict[str, str | Path]]) -> str:
    """Render records as the canonical catalog text, always ending in one newline."""
    categories: dict[str, list[dict[str, str | Path]]] = {}
    for record in records:
        categories.setdefault(str(record["category"]), []).append(record)

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
            name = cell(str(record["name"]))
            description = cell(str(record["description"]))
            path = Path(record["path"]).as_posix()
            lines.append(f"| [`{name}`]({path}) | {description} |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    records = collect_records()
    if not records:
        print(f"No skill definitions found under {SKILLS_ROOT}.", file=sys.stderr)
        return 1

    OUTPUT.write_text(render_catalog(records), encoding="utf-8")
    print(f"catalog_skills={len(records)}")
    print(f"catalog={OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
