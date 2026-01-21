import tempfile
import unittest
from pathlib import Path


class TestGenerateRepoDocs(unittest.TestCase):
    def test_index_updates_on_directory_only_week_add(self) -> None:
        # Import lazily so the module can still be used as a script.
        import tools.generate_repo_docs as gen

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "reports").mkdir(parents=True, exist_ok=True)
            (root / "notes").mkdir(parents=True, exist_ok=True)

            # Minimal repo layout validation requires README.md and notes/
            (root / "README.md").write_text("# Test Repo\n", encoding="utf-8")

            # Initial week with at least one file so the first run definitely generates.
            week01 = root / "notes" / "Spring_2026" / "DATA999" / "Week01"
            week01.mkdir(parents=True, exist_ok=True)
            (week01 / "README.md").write_text("# Week01\n", encoding="utf-8")

            rc1 = gen.run(root, dry_run=False, verbose=False)
            self.assertEqual(rc1, 0)

            idx_path = root / "notes" / "INDEX.md"
            self.assertTrue(idx_path.exists(), "expected notes/INDEX.md to be generated")
            idx1 = idx_path.read_text(encoding="utf-8")
            self.assertIn("Week01", idx1)
            self.assertNotIn("Week02", idx1)

            # Add a new empty week directory (no files) — previously this would not
            # be detected by the file-based manifest and the index wouldn't refresh.
            week02 = root / "notes" / "Spring_2026" / "DATA999" / "Week02"
            week02.mkdir(parents=True, exist_ok=True)

            rc2 = gen.run(root, dry_run=False, verbose=False)
            self.assertEqual(rc2, 0)

            idx2 = idx_path.read_text(encoding="utf-8")
            self.assertIn("Week02", idx2, "expected index to include newly created empty week directory")


if __name__ == "__main__":
    unittest.main()
