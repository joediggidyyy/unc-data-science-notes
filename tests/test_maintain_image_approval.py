import json
import tempfile
import unittest
from pathlib import Path


class TestMaintainImageApprovalParsing(unittest.TestCase):
    def test_extracts_unapproved_images_from_report(self) -> None:
        # Import lazily so the module can still be used as a script.
        import maintain as maintain_mod

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "notes").mkdir(parents=True, exist_ok=True)

            # One real file that should be returned.
            img1 = root / "notes" / "a.png"
            img1.write_bytes(b"fake")

            # One file that is missing and should be ignored.
            missing = "notes/missing.png"

            report = {
                "counts": {"error": 0, "warn": 1, "total": 1},
                "findings": [
                    {
                        "severity": "WARN",
                        "path": "notes/a.png",
                        "message": "Image file present; manual privacy review required.",
                        "hint": "...",
                    },
                    {
                        "severity": "WARN",
                        "path": missing,
                        "message": "Image file present; manual privacy review required.",
                        "hint": "...",
                    },
                    # Not an image
                    {
                        "severity": "WARN",
                        "path": "notes/a.pdf",
                        "message": "Image file present; manual privacy review required.",
                        "hint": "...",
                    },
                    # Wrong message
                    {
                        "severity": "WARN",
                        "path": "notes/other.png",
                        "message": "Something else",
                        "hint": "...",
                    },
                ],
            }

            report_path = root / "reports" / "compliance_report.json"
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(report), encoding="utf-8")

            got = maintain_mod._load_unapproved_images_from_compliance_report(
                repo_root=root,
                report_path=report_path,
            )

            self.assertEqual(got, ["notes/a.png"])


if __name__ == "__main__":
    unittest.main()
