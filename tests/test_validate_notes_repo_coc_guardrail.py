import tempfile
import unittest
from pathlib import Path

import tools.validate_notes_repo as validate_notes_repo


class TestCodeOfConductGuardrail(unittest.TestCase):
    def test_forbidden_contributor_covenant_suggestion_warns(self) -> None:
        forbidden = "(If you prefer a formal, widely-used policy, you can adopt the Contributor Covenant and link it here.)"

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)

            # Create the validator's expected baseline files so the test focuses on the guardrail.
            (root / "README.md").write_text("# README\n", encoding="utf-8")
            (root / "COMPLIANCE.md").write_text("# Compliance\n", encoding="utf-8")
            (root / "LICENSE.md").write_text("License\n", encoding="utf-8")
            (root / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")

            (root / "CODE_OF_CONDUCT.md").write_text(
                "# Code of Conduct\n\n" + forbidden + "\n",
                encoding="utf-8",
            )

            findings = validate_notes_repo.validate_repo(root)

            hits = [
                f
                for f in findings
                if f.severity == "WARN"
                and f.path == "CODE_OF_CONDUCT.md"
                and "disallowed templated suggestion line" in f.message
            ]

            self.assertTrue(hits, "Expected a WARN finding when forbidden line appears in CODE_OF_CONDUCT.md")


if __name__ == "__main__":
    unittest.main()
