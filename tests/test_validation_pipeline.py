"""Tests for orchestration; no skill resources or external commands are executed."""

from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import optimize_all_skills


class ValidationPipelineTests(unittest.TestCase):
    def invoke(self, args, results):
        with patch.object(optimize_all_skills, "run", side_effect=results) as run:
            with contextlib.redirect_stdout(io.StringIO()):
                code = optimize_all_skills.main(args)
        return code, run.call_args_list

    def test_validate_only_checks_catalog_without_writing(self):
        code, calls = self.invoke(["--validate-only"], [0, 0, 0, 0])
        self.assertEqual(code, 0)
        self.assertEqual(calls[0].args, ("scripts/generate_catalog.py", "catalog", "--check"))
        self.assertEqual(len(calls), 4)

    def test_default_refreshes_catalog(self):
        code, calls = self.invoke([], [0, 0, 0, 0])
        self.assertEqual(code, 0)
        self.assertEqual(calls[0].args, ("scripts/generate_catalog.py", "catalog"))

    def test_failures_do_not_skip_remaining_checks(self):
        code, calls = self.invoke(["--validate-only"], [1, 0, 1, 0])
        self.assertEqual(code, 1)
        self.assertEqual(len(calls), 4)

    def test_conflicting_modes_are_rejected_before_execution(self):
        with patch.object(optimize_all_skills, "run") as run:
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as raised:
                    optimize_all_skills.main(["--validate-only", "--refresh-catalog"])
        self.assertEqual(raised.exception.code, 2)
        run.assert_not_called()

    def test_unknown_flags_are_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                optimize_all_skills.main(["--typo"])
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
