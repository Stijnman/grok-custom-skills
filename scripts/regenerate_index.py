#!/usr/bin/env python3
"""Backward-compatible entry point for the canonical skills catalog generator.

Use ``python3 scripts/generate_catalog.py`` for new automation. This wrapper preserves
older local commands while ensuring they generate exactly the same SKILLS_INDEX.md.
"""

from generate_catalog import main


if __name__ == "__main__":
    raise SystemExit(main())
