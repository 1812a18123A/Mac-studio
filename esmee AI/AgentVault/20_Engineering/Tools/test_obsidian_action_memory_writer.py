import argparse
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

import obsidian_action_memory_writer as writer


class ObsidianActionMemoryWriterTest(unittest.TestCase):
    def test_memory_path_uses_standard_location(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            path = writer.memory_path(
                vault,
                datetime(2026, 6, 17, 12, 45),
                "工程部",
                "Obsidian Writer",
            )

        self.assertEqual(
            path.relative_to(Path(tmp).resolve()).as_posix(),
            "AgentVault/50_Memory/Action_Logs/2026-06-17/"
            "2026-06-17_12-45_工程部_obsidian-writer.md",
        )

    def test_resolve_inside_vault_rejects_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            with self.assertRaises(ValueError):
                writer.resolve_inside_vault(vault, Path("../outside.md"))

    def test_create_append_and_uri(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = argparse.Namespace(
                vault=tmp,
                vault_name="Test Vault",
                department="记忆部",
                task_id="writer-test",
                title="Writer Test",
                status="planned",
                risk_level="low",
                current_mode="坤",
                skills="obsidian-memory",
                plugins="none",
                related_files="source.md",
                notify="工程部",
                requires_user_confirmation=False,
                user_goal="测试创建行动记忆。",
                action_goal="只验证最小写入。",
                context="临时 vault。",
                unknowns="无。",
                materials="source.md",
                forbidden_materials="private.md",
                planned_changes="memory.md",
                first_step="创建文件。",
                risks="路径写错。",
                mitigations="限制在 vault 内。",
                notify_reason="后续实现。",
                next_step="追加日志。",
                when="2026-06-17T12:45",
                overwrite=False,
            )
            with redirect_stdout(io.StringIO()):
                writer.create_memory(args)

            memory_file = (
                Path(tmp)
                / "AgentVault/50_Memory/Action_Logs/2026-06-17/"
                / "2026-06-17_12-45_记忆部_writer-test.md"
            )
            self.assertTrue(memory_file.exists())
            self.assertIn("行动记忆：Writer Test", memory_file.read_text(encoding="utf-8"))

            with redirect_stdout(io.StringIO()):
                writer.append_log(
                    argparse.Namespace(
                        vault=tmp,
                        file=str(memory_file),
                        message="验证追加日志。",
                        when="2026-06-17 12:46",
                    )
                )
            text = memory_file.read_text(encoding="utf-8")
            self.assertIn("## Log 2026-06-17 12:46", text)
            self.assertIn("- 验证追加日志。", text)

            with redirect_stdout(io.StringIO()):
                writer.set_status(
                    argparse.Namespace(
                        vault=tmp,
                        file=str(memory_file),
                        status="completed",
                        current_mode="坤-兑",
                    )
                )
            text = memory_file.read_text(encoding="utf-8")
            self.assertIn("status: completed", text)
            self.assertIn("current_mode: 坤-兑", text)

            uri = writer.obsidian_open_uri(
                "Test Vault",
                "AgentVault/50_Memory/Action_Logs/2026-06-17/test.md",
            )
            self.assertEqual(
                uri,
                "obsidian://open?vault=Test%20Vault&file="
                "AgentVault%2F50_Memory%2FAction_Logs%2F2026-06-17%2Ftest.md",
            )

    def test_set_frontmatter_fields_requires_frontmatter(self):
        with self.assertRaises(ValueError):
            writer.set_frontmatter_fields("not frontmatter", {"status": "completed"})


if __name__ == "__main__":
    unittest.main()
