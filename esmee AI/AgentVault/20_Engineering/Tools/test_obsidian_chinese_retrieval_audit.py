import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import obsidian_chinese_retrieval_audit as audit


class ObsidianChineseRetrievalAuditTest(unittest.TestCase):
    def test_audit_reports_missing_items_without_reading_private_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            root = vault / "AgentVault"
            (root / "50_Memory").mkdir(parents=True)
            (root / "00_System" / "Private").mkdir(parents=True)
            good = root / "50_Memory" / "good.md"
            good.write_text(
                """---
中文标题: 中文测试
中文摘要: 这是中文摘要。
检索元素:
  - 中文检索
---

# 中文测试

## 中文检索索引

- 中文关键词：中文检索
""",
                encoding="utf-8",
            )
            bad = root / "50_Memory" / "bad.md"
            bad.write_text("# Bad\n\nNo Chinese retrieval block.\n", encoding="utf-8")
            private = root / "00_System" / "Private" / "secret.md"
            private.write_text("# secret\n", encoding="utf-8")

            result = audit.audit_vault(vault, Path("AgentVault"))

        self.assertEqual(result.scanned, 2)
        self.assertEqual(result.passed, 1)
        self.assertEqual(result.skipped, 1)
        self.assertEqual(len(result.findings), 1)
        self.assertEqual(result.findings[0].path, "AgentVault/50_Memory/bad.md")
        self.assertIn("中文标题", result.findings[0].missing)
        self.assertIn("中文检索索引", result.findings[0].missing)

    def test_markdown_report_contains_only_paths_and_categories(self):
        result = audit.AuditResult(
            scanned=1,
            passed=0,
            skipped=0,
            findings=[
                audit.Finding(
                    "AgentVault/example.md",
                    ["中文标题", "中文摘要"],
                    "medium",
                )
            ],
        )

        report = audit.render_markdown(result, "AgentVault", 10)

        self.assertIn("# 中文检索只读审计报告", report)
        self.assertIn("`AgentVault/example.md`", report)
        self.assertIn("中文标题、中文摘要", report)

    def test_fail_on_findings_is_opt_in(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            root = vault / "AgentVault"
            root.mkdir(parents=True)
            (root / "missing.md").write_text("# Missing\n", encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                default_exit = audit.main(["--vault", tmp, "--root", "AgentVault"])
            with redirect_stdout(io.StringIO()):
                strict_exit = audit.main(
                    ["--vault", tmp, "--root", "AgentVault", "--fail-on-findings"]
                )

        self.assertEqual(default_exit, 0)
        self.assertEqual(strict_exit, 1)

    def test_resolve_inside_vault_rejects_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit.resolve_inside_vault(Path(tmp), Path("../outside"))


if __name__ == "__main__":
    unittest.main()
