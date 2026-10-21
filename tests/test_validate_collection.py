"""Isolated fixtures for collection validation, independent of live skill text."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_collection import validate_collection


class CollectionValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="skills fixtures ")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def skill(self, name="sample-skill", description="Check samples. Use when reviewing samples."):
        directory = self.root / name
        directory.mkdir()
        path = directory / "SKILL.md"
        path.write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\n# Sample\n",
            encoding="utf-8",
        )
        return path

    def test_valid_package(self):
        self.skill()
        self.assertEqual(validate_collection(self.root), (1, []))

    def test_empty_collection_fails(self):
        count, errors = validate_collection(self.root)
        self.assertEqual(count, 0)
        self.assertIn("No skill definitions found.", errors)

    def test_missing_definition_is_not_silently_ignored(self):
        self.skill()
        (self.root / "forgotten-skill").mkdir()
        count, errors = validate_collection(self.root)
        self.assertEqual(count, 1)
        self.assertTrue(any("missing SKILL.md" in error for error in errors))

    def test_invalid_name_and_description_length(self):
        self.skill("x" * 65, "Use when " + "x" * 1024)
        _, errors = validate_collection(self.root)
        self.assertTrue(any("64 characters" in error for error in errors))
        self.assertTrue(any("1024 characters" in error for error in errors))

    def test_invalid_utf8_is_reported(self):
        path = self.skill()
        path.write_bytes(b"\xff")
        _, errors = validate_collection(self.root)
        self.assertTrue(any("cannot read UTF-8" in error for error in errors))

    def test_directory_name_mismatch(self):
        path = self.skill()
        path.write_text(path.read_text().replace("name: sample-skill", "name: other-skill"))
        _, errors = validate_collection(self.root)
        self.assertTrue(any("does not match directory" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
