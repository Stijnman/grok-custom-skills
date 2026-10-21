#!/usr/bin/env python3
"""Validate the collection, refreshing the catalog unless read-only mode is selected.

Skill instructions are never heuristically rewritten: they require human review.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script: str, label: str, *args: str) -> int:
    print(f"\n=== {label} ===", flush=True)
    result = subprocess.run([sys.executable, script, *args], cwd=ROOT)
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--validate-only", action="store_true",
        help="Check catalog freshness and publication rules without writing files.",
    )
    mode.add_argument(
        "--refresh-catalog", action="store_true",
        help="Refresh the generated catalog before validation (the default).",
    )
    args = parser.parse_args(argv)

    codes: list[int] = []
    catalog_args = ("--check",) if args.validate_only else ()
    codes.append(run("scripts/generate_catalog.py", "catalog", *catalog_args))
    codes.append(run("scripts/validate_collection.py", "collection schema validation"))
    codes.append(run("scripts/check_no_private_data.py", "private-data scan"))
    codes.append(run("scripts/publish_safety_check.py", "publication-safety scan"))

    failed = sum(code != 0 for code in codes)
    print(f"\n=== pipeline complete: {failed} stage(s) failed ===")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
