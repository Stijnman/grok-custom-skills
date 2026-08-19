#!/usr/bin/env python3
"""Regression tests for the generated skills catalog."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_catalog  # noqa: E402


class CatalogGeneratorTests(unittest.TestCase):
    """Validate deterministic rendering and the committed catalog artifact."""

    def test_rendered_catalog_has_exactly_one_final_newline(self) -> None:
        rendered = generate_catalog.render_catalog(generate_catalog.collect_records())

        self.assertTrue(rendered.endswith("\n"))
        self.assertFalse(rendered.endswith("\n\n"))

    def test_committed_catalog_matches_canonical_renderer(self) -> None:
        expected = generate_catalog.render_catalog(generate_catalog.collect_records())
        actual = (REPO / "SKILLS_INDEX.md").read_text(encoding="utf-8")

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
