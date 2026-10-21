#!/usr/bin/env python3
"""Generate a deterministic, newline-terminated SKILLS_INDEX.md catalog.

The catalog generator intentionally has no third-party dependencies. It reads the
Agent Skills frontmatter subset used here: top-level scalar fields (plain,
single-quoted, or JSON-compatible double-quoted) and folded/literal block
scalars. It is not a general YAML validator; use skills-ref for full spec
validation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

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

_FRONTMATTER_BOUNDARY = re.compile(r"^---\s*$")
_TOP_LEVEL_KEY = re.compile(r"^([A-Za-z0-9_-]+):(?:[ \t]*(.*))?$")


def frontmatter(text: str) -> str:
    """Return frontmatter body if delimited at the start of the file, else empty."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for index in range(1, len(lines)):
        if _FRONTMATTER_BOUNDARY.fullmatch(lines[index]):
            return "\n".join(lines[1:index])
    return ""


def _plain_scalar(value: str) -> str:
    """Read the supported YAML plain-scalar subset, including trailing comments."""
    # In YAML a comment marker starts a comment only when separated by whitespace.
    value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
    if value in ("", "~", "null", "Null", "NULL"):
        return ""
    return value


def _quoted_scalar(value: str) -> str:
    """Decode YAML single quotes and JSON-compatible YAML double quotes."""
    if value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            return value
        return value[1:-1].replace("''", "'")
    if value.startswith('"'):
        try:
            decoded = json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value[1:-1] if value.endswith('"') else value
        return decoded if isinstance(decoded, str) else str(decoded)
    return _plain_scalar(value)


def _fold_block(lines: list[str], parent_indent: int, style: str) -> str:
    """Fold/retain a YAML block scalar's supported ordinary text lines."""
    nonblank_indents = [len(line) - len(line.lstrip(" ")) for line in lines if line.strip()]
    content_indent = min(nonblank_indents) if nonblank_indents else parent_indent + 1
    content = [line[content_indent:] if line.strip() else "" for line in lines]
    trailing_blank_lines = 0
    for line in reversed(content):
        if line:
            break
        trailing_blank_lines += 1

    # Ordinary YAML folded scalars turn a single line break into a space while
    # preserving blank-line paragraph breaks. Literal scalars retain line breaks.
    if style.startswith(">"):
        pieces: list[str] = []
        paragraph: list[str] = []
        for line in content:
            if line == "":
                if paragraph:
                    pieces.append(" ".join(paragraph))
                    paragraph = []
                elif pieces:
                    pieces.append("")
            else:
                paragraph.append(line)
        if paragraph:
            pieces.append(" ".join(paragraph))
        result = "\n".join(pieces)
    else:
        result = "\n".join(content)

    indicator = style[-1:] if style[-1:] in ("-", "+") else ""
    if indicator == "-":
        return result.rstrip("\n")
    if indicator == "+":
        return result + "\n" * (trailing_blank_lines + 1) if lines else result
    return result + "\n" if lines else result


def parse_frontmatter(block: str) -> dict[str, str]:
    """Parse top-level scalar metadata and folded/literal block descriptions.

    Nested mappings (such as the spec's optional ``metadata`` map) are ignored;
    only top-level scalar keys are collected. This is a deliberately bounded,
    dependency-free YAML subset, not a replacement for a YAML implementation.
    """
    lines = block.splitlines()
    result: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        match = _TOP_LEVEL_KEY.match(line)
        if not match:
            i += 1
            continue
        key, raw_value = match.groups()
        raw_value = raw_value or ""
        if raw_value and raw_value[0] in (">", "|") and raw_value.strip(" ")[:1] in (">", "|"):
            style_token = raw_value.strip().split()[0]
            style = style_token[0]
            if len(style_token) > 1 and style_token[1] in "-+":
                style += style_token[1]
            start = i + 1
            end = start
            while end < len(lines) and (not lines[end].strip() or lines[end].startswith((" ", "\t"))):
                end += 1
            result[key] = _fold_block(lines[start:end], 0, style)
            i = end
            continue
        if raw_value.startswith(("'", '"')):
            result[key] = _quoted_scalar(raw_value)
        else:
            result[key] = _plain_scalar(raw_value)
        i += 1
    return result


def field(block: str, key: str) -> str:
    """Return one top-level scalar field from a frontmatter block."""
    return parse_frontmatter(block).get(key, "")


def category_for(name: str) -> str:
    lower = name.lower()
    for category, terms in CATEGORY_RULES:
        if any(term in lower for term in terms):
            return category
    return "General Utilities"


def cell(value: str) -> str:
    """Escape content for one Markdown table cell, flattening line breaks."""
    value = value.replace("\\", "\\\\").replace("\r\n", "\n").replace("\r", "\n")
    value = " ".join(part.strip() for part in value.split("\n"))
    return value.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").strip()


def _record_path(skill_file: Path, skills_root: Path) -> str:
    """Keep repository links stable, while making custom-root records portable."""
    resolved_file = skill_file.resolve()
    try:
        return resolved_file.relative_to(REPO.resolve()).as_posix()
    except ValueError:
        return skill_file.relative_to(skills_root).as_posix()


def collect_records(skills_root: Path = SKILLS_ROOT) -> list[dict[str, str]]:
    """Collect catalog records in a stable order from direct skill directories."""
    skills_root = Path(skills_root)
    records: list[dict[str, str]] = []
    skill_files = sorted(
        skills_root.glob("*/SKILL.md"),
        key=lambda item: (item.parent.name.casefold(), item.parent.name),
    )
    for skill_file in skill_files:
        block = frontmatter(skill_file.read_text(encoding="utf-8", errors="replace"))
        metadata = parse_frontmatter(block)
        name = metadata.get("name", "") or skill_file.parent.name
        description = metadata.get("description", "") or "No description provided."
        records.append(
            {
                "name": name,
                "description": description,
                "path": _record_path(skill_file, skills_root),
                "category": category_for(name),
            }
        )
    return records


def _code_span(value: str) -> str:
    """Make a Markdown code span that cannot be closed by embedded backticks."""
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
    contents = value
    if contents.startswith(" ") or contents.endswith(" ") or contents.startswith("`") or contents.endswith("`"):
        contents = f" {contents} "
    return f"{delimiter}{contents}{delimiter}"


def render_catalog(records: list[dict[str, Any]]) -> str:
    """Render records as canonical catalog text, always ending in one newline."""
    categories: dict[str, list[dict[str, Any]]] = {}
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
        "| --- | ---: |",
    ]
    for category in sorted(categories):
        lines.append(f"| {cell(category)} | {len(categories[category])} |")

    lines.extend(["", "## Complete catalog", ""])
    for category in sorted(categories):
        lines.extend([f"### {category}", "", "| Skill | Description |", "| --- | --- |"])
        for record in sorted(categories[category], key=lambda item: (str(item["name"]).casefold(), str(item["name"]))):
            name = _code_span(str(record["name"]))
            description = cell(str(record["description"]))
            path = Path(str(record["path"])).as_posix()
            lines.append(f"| [{name}]({path}) | {description} |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def check_freshness(output: Path = OUTPUT, expected: str | None = None) -> bool:
    """Return whether the generated catalog matches disk; never writes files."""
    if expected is None:
        records = collect_records()
        if not records:
            return False
        expected = render_catalog(records)
    try:
        return Path(output).read_text(encoding="utf-8") == expected
    except (OSError, UnicodeError):
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the catalog is stale; do not write it")
    args = parser.parse_args(argv)

    records = collect_records()
    if not records:
        print(f"No skill definitions found under {SKILLS_ROOT}.", file=sys.stderr)
        return 1

    rendered = render_catalog(records)
    if args.check:
        if check_freshness(OUTPUT, rendered):
            print(f"catalog is current ({len(records)} skills): {OUTPUT}")
            return 0
        print(f"catalog is stale; run `python3 scripts/generate_catalog.py` to refresh {OUTPUT}", file=sys.stderr)
        return 1

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"catalog_skills={len(records)}")
    print(f"catalog={OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
