#!/usr/bin/env python3
"""Regression tests for the generated skills catalog."""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
sys.path.insert(0, str(SCRIPTS))

import generate_catalog  # noqa: E402


class CatalogGeneratorTests(unittest.TestCase):
    """Validate metadata parsing, stable rendering, and freshness behavior."""

    def test_rendered_catalog_has_exactly_one_final_newline(self) -> None:
        rendered = generate_catalog.render_catalog(generate_catalog.collect_records())

        self.assertTrue(rendered.endswith("\n"))
        self.assertFalse(rendered.endswith("\n\n"))

    def test_committed_catalog_matches_canonical_renderer(self) -> None:
        expected = generate_catalog.render_catalog(generate_catalog.collect_records())
        actual = (REPO / "SKILLS_INDEX.md").read_text(encoding="utf-8")

        self.assertEqual(actual, expected)

    def test_frontmatter_reads_top_level_fields_and_yaml_quotes(self) -> None:
        block = """name: 'quoted-skill'
description: "A quoted: description with \\"quotes\\"."
metadata:
  name: should-not-override
  description: should-not-override
compatibility: Requires a tool # inline comment
"""
        fields = generate_catalog.parse_frontmatter(block)

        self.assertEqual(fields["name"], "quoted-skill")
        self.assertEqual(fields["description"], 'A quoted: description with "quotes".')
        self.assertEqual(fields["compatibility"], "Requires a tool")
        self.assertNotIn("version", fields)

    def test_frontmatter_supports_folded_and_literal_block_descriptions(self) -> None:
        folded = generate_catalog.parse_frontmatter(
            "name: fold\ndescription: >-\n  First line\n  second line\n\n  New paragraph\nmetadata:\n  version: '1'\n"
        )
        literal = generate_catalog.parse_frontmatter(
            "name: literal\ndescription: |\n  First line\n  second line\n"
        )

        self.assertEqual(folded["description"], "First line second line\nNew paragraph")
        self.assertEqual(literal["description"], "First line\nsecond line\n")

    def test_custom_roots_collect_metadata_and_stable_relative_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "skills"
            (root / "z-skill").mkdir(parents=True)
            (root / "a-skill").mkdir()
            (root / "a-skill" / "SKILL.md").write_text(
                "---\nname: a-skill\ndescription: First\n---\nbody\n", encoding="utf-8"
            )
            (root / "z-skill" / "SKILL.md").write_text(
                "---\nname: z-skill\ndescription: >-\n  Joined\n  description\n---\nbody\n", encoding="utf-8"
            )
            (root / "parent" / "nested").mkdir(parents=True)
            (root / "parent" / "nested" / "SKILL.md").write_text("not a direct skill", encoding="utf-8")

            records = generate_catalog.collect_records(root)

        self.assertEqual([record["name"] for record in records], ["a-skill", "z-skill"])
        self.assertEqual(records[0]["path"], "a-skill/SKILL.md")
        self.assertEqual(records[1]["description"], "Joined description")

    def test_missing_frontmatter_fields_use_directory_and_safe_fallbacks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = root / "fallback"
            skill.mkdir()
            (skill / "SKILL.md").write_text("# No metadata\n", encoding="utf-8")
            records = generate_catalog.collect_records(root)

        self.assertEqual(records[0]["name"], "fallback")
        self.assertEqual(records[0]["description"], "No description provided.")
        self.assertEqual(records[0]["path"], "fallback/SKILL.md")

    def test_render_is_deterministic_and_escapes_untrusted_table_text(self) -> None:
        records = [
            {"name": "skill`name", "description": "one | two\n<script>&", "path": "x/SKILL.md", "category": "General"},
            {"name": "alpha", "description": "plain", "path": "a/SKILL.md", "category": "General"},
        ]

        first = generate_catalog.render_catalog(records)
        second = generate_catalog.render_catalog(list(reversed(records)))

        self.assertEqual(first, second)
        self.assertIn("one \\| two &lt;script&gt;&", first)
        self.assertIn("[``skill`name``](x/SKILL.md)", first)
        self.assertEqual(first.count("\n"), first.rstrip("\n").count("\n") + 1)

    def test_check_mode_reports_freshness_without_writing_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "catalog.md"
            expected = generate_catalog.render_catalog(generate_catalog.collect_records())
            output.write_text(expected, encoding="utf-8")
            before = output.read_bytes()
            with mock.patch.object(generate_catalog, "OUTPUT", output), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(generate_catalog.main(["--check"]), 0)
            self.assertEqual(output.read_bytes(), before)
            self.assertTrue(generate_catalog.check_freshness(output, expected))
            output.write_text("stale\n", encoding="utf-8")
            self.assertFalse(generate_catalog.check_freshness(output, expected))


if __name__ == "__main__":
    unittest.main()
