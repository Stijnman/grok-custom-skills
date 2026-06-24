#!/usr/bin/env python3
"""Fail if tracked skill content contains private or machine-specific data."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = [ROOT / ".grok", ROOT / "scripts"]
SCAN_FILES = [ROOT / "README.md", ROOT / "SKILLS_INDEX.md", ROOT / "SECURITY.md", ROOT / "PUBLISHING.md"]
SKIP_NAMES = {".git"}

# Allowed public patterns (not flagged)
ALLOW_EMAIL = re.compile(
    r"@users\.noreply\.github\.com|@example\.com|noreply@|placeholder@",
    re.I,
)

RULES: list[tuple[str, str, re.Pattern[str]]] = [
    ("private_email", "personal email address", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("home_path", "hardcoded /home/<user> path", re.compile(r"/home/[a-zA-Z0-9_-]+/")),
    ("private_ip", "private IP address", re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b")),
    ("hostname", "machine hostname", re.compile(r"\b(?:linuxmint|VivoBook|ASUSLaptop)\b", re.I)),
    ("session_port", "session-specific port example", re.compile(r"\bport\s+445\b", re.I)),
    ("session_service", "session-specific service name", re.compile(r"\bSamba/Apache\b")),
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for p in SCAN_FILES:
        if p.is_file():
            files.append(p)
    for base in SCAN_DIRS:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in {".md", ".py", ".json", ".yml", ".yaml", ".toml"}:
                if p.name == "check_no_private_data.py":
                    continue
                files.append(p)
    return sorted(set(files))


def check_file(path: Path) -> list[str]:
    hits: list[str] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return [str(e)]

    for line_no, line in enumerate(text.splitlines(), 1):
        for rule_id, label, pattern in RULES:
            if rule_id == "private_email":
                for m in pattern.finditer(line):
                    email = m.group(0)
                    if ALLOW_EMAIL.search(email):
                        continue
                    hits.append(f"L{line_no}: {label} ({email})")
                continue
            if pattern.search(line):
                hits.append(f"L{line_no}: {label}")
    return hits


def main() -> int:
    failed = 0
    checked = 0
    for path in iter_files():
        checked += 1
        hits = check_file(path)
        if hits:
            failed += 1
            rel = path.relative_to(ROOT)
            print(f"FAIL {rel}")
            for h in hits:
                print(f"  {h}")
    print(f"\nChecked {checked} files, {failed} with private data")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())