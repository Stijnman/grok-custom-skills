#!/usr/bin/env python3
"""Fail if published skills, scripts, or repository documentation contain private data."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = [ROOT / ".grok" / "skills", ROOT / "scripts", ROOT / ".github"]
ALLOWED_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".toml"}
ALLOW_EMAIL = re.compile(r"@users\.noreply\.github\.com|@example\.com|noreply@|placeholder@", re.I)
RULES: list[tuple[str, str, re.Pattern[str]]] = [
    ("private_email", "personal email address", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("home_path", "hardcoded /home/<user> path", re.compile(r"/home/[a-zA-Z0-9_-]+/")),
    ("private_ip", "private IP address", re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3})\b")),
    ("hostname", "machine hostname", re.compile(r"\b(?:linuxmint|VivoBook|ASUSLaptop)\b", re.I)),
]


def iter_files() -> list[Path]:
    files = list(ROOT.glob("*.md"))
    for base in SCAN_DIRS:
        if base.exists():
            files.extend(path for path in base.rglob("*") if path.is_file() and path.suffix in ALLOWED_SUFFIXES)
    return sorted(set(files))


def check_file(path: Path) -> list[str]:
    hits = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for line_number, line in enumerate(text.splitlines(), start=1):
        for rule_id, label, pattern in RULES:
            if rule_id == "private_email":
                for match in pattern.finditer(line):
                    if not ALLOW_EMAIL.search(match.group(0)):
                        hits.append(f"L{line_number}: {label} ({match.group(0)})")
            elif pattern.search(line):
                hits.append(f"L{line_number}: {label}")
    return hits


def main() -> int:
    failures = 0
    checked = 0
    for path in iter_files():
        if path.name == "check_no_private_data.py":
            continue
        checked += 1
        hits = check_file(path)
        if hits:
            failures += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for hit in hits:
                print(f"  {hit}")
    print(f"Checked {checked} published files; {failures} contained potential private data.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
