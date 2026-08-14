#!/usr/bin/env python3
"""Run deterministic repository validation and optionally refresh the generated catalog.

This helper deliberately does not rewrite skill text. Metadata and instructions require
human review because heuristic rewriting can corrupt wording or routing triggers.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script: str, label: str) -> int:
    print(f"\n=== {label} ===")
    result = subprocess.run([sys.executable, script], cwd=ROOT)
    return result.returncode


def main() -> int:
    validate_only = "--validate-only" in sys.argv
    allowed = {"--validate-only", "--refresh-catalog"}
    unknown = [arg for arg in sys.argv[1:] if arg not in allowed]
    if unknown:
        print("Unsupported option(s): " + ", ".join(unknown), file=sys.stderr)
        return 2

    codes: list[int] = []
    if not validate_only:
        codes.append(run("scripts/generate_catalog.py", "refresh catalog"))
    codes.append(run("scripts/validate_collection.py", "collection schema validation"))
    codes.append(run("scripts/check_no_private_data.py", "private-data scan"))
    codes.append(run("scripts/publish_safety_check.py", "publication-safety scan"))

    failed = sum(code != 0 for code in codes)
    print(f"\n=== pipeline complete: {failed} stage(s) failed ===")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
