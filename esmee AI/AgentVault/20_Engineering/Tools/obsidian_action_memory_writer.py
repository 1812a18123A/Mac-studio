#!/usr/bin/env python3
"""Minimal Obsidian action memory writer.

Creates and appends local Markdown action-memory files in an Obsidian vault.
No Obsidian plugin, REST API, or external dependency is required.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import quote


DEFAULT_VAULT = Path(__file__).resolve().parents[3]
ACTION_LOG_ROOT = Path("AgentVault/50_Memory/Action_Logs")


def split_csv(value: Optional[str]) -> List[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def slugify(value: str) -> str:
    allowed = []
    for char in value.strip().lower():
        if char.isalnum():
            allowed.append(char)
        elif char in (" ", "-", "_", ".", "/"):
            allowed.append("-")
    slug = "".join(allowed).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "task"


def yaml_bool(value: bool) -> str:
    return "true" if value else "false"


def yaml_list(items: Iterable[str]) -> str:
    values = list(items)
    if not values:
        return "  - none"
    return "\n".join(f"  - {item}" for item in values)


def resolve_inside_vault(vault: Path, target: Path) -> Path:
    vault = vault.expanduser().resolve()
    target = target.expanduser()
    if not target.is_absolute():
        target = vault / target
    target = target.resolve()
    try:
        target.relative_to(vault)
    except ValueError as exc:
        raise ValueError(f"target path escapes vault: {target}") from exc
    return target


def memory_path(vault: Path, when: datetime, department: str, task_id: str) -> Path:
    date = when.strftime("%Y-%m-%d")
    time = when.strftime("%H-%M")
    filename = f"{date}_{time}_{slugify(department)}_{slugify(task_id)}.md"
    return resolve_inside_vault(vault, ACTION_LOG_ROOT / date / filename)


def obsidian_open_uri(vault_name: str, vault_relative_file: str) -> str:
    return (
        "obsidian://open?"
        f"vault={quote(vault_name, safe='')}"
        f"&file={quote(vault_relative_file, safe='')}"
    )


def build_memory(args: argparse.Namespace, path: Path, when: datetime) -> str:
    title = args.title or args.task_id
    return f"""---
type: action_memory
date: {when.strftime("%Y-%m-%d")}
time: "{when.strftime("%H:%M")}"
department: {args.department}
task_id: {args.task_id}
status: {args.status}
risk_level: {args.risk_level}
current_mode: {args.current_mode}
related_skills:
{yaml_list(split_csv(args.skills))}
related_plugins:
{yaml_list(split_csv(args.plugins))}
related_files:
{yaml_list(split_csv(args.related_files))}
notify_departments:
{yaml_list(split_csv(args.notify))}
requires_user_confirmation: {yaml_bool(args.requires_user_confirmation)}
---

# 行动记忆：{title}

## 1. 用户目标

用户想要什么：
- {args.user_goal}

## 2. 本次行动目标

这一次只做什么：
- {args.action_goal}

## 3. 当前上下文

已知信息：
- {args.context}

未知信息：
- {args.unknowns}

## 4. 涉及资料

需要读取或参考的资料：
{yaml_list(split_csv(args.materials))}

禁止使用或不能外发的资料：
{yaml_list(split_csv(args.forbidden_materials))}

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
{yaml_list(split_csv(args.planned_changes))}

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录

## 7. 需要调用的 skill

本次需要：
{yaml_list(split_csv(args.skills))}

## 8. 需要使用的 Codex App 插件功能

本次需要：
{yaml_list(split_csv(args.plugins))}

## 9. 行动步骤

- [ ] Step 1: {args.first_step}

## 10. 风险检查

风险：
- {args.risks}

缓解措施：
- {args.mitigations}

## 11. 部门通知

需要通知哪个部门：
{yaml_list(split_csv(args.notify))}

通知原因：
- {args.notify_reason}

## 12. 执行结果

实际做了什么：
- 待执行。

成功：
- 待记录。

失败：
- 待记录。

## 13. 产生的新资料

新增文件：
- {path}

更新文件：
- 待记录。

截图/日志/轨迹：
- 待记录。

## 14. 下一步

下一步建议：
- {args.next_step}

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 行动记忆已创建，等待执行结果。
"""


def create_memory(args: argparse.Namespace) -> int:
    vault = Path(args.vault).expanduser().resolve()
    when = datetime.strptime(args.when, "%Y-%m-%dT%H:%M") if args.when else datetime.now()
    path = memory_path(vault, when, args.department, args.task_id)
    if path.exists() and not args.overwrite:
        raise FileExistsError(f"memory file already exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_memory(args, path, when), encoding="utf-8")
    rel_path = path.relative_to(vault).as_posix()
    print(path)
    print(obsidian_open_uri(args.vault_name, rel_path))
    return 0


def append_log(args: argparse.Namespace) -> int:
    vault = Path(args.vault).expanduser().resolve()
    path = resolve_inside_vault(vault, Path(args.file))
    timestamp = args.when or datetime.now().strftime("%Y-%m-%d %H:%M")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n## Log {timestamp}\n\n- {args.message}\n")
    print(path)
    return 0


def set_frontmatter_fields(text: str, updates: dict) -> str:
    if not text.startswith("---\n"):
        raise ValueError("file does not start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter closing marker not found")

    frontmatter = text[4:end].splitlines()
    body = text[end:]
    remaining = {key: value for key, value in updates.items() if value is not None}
    changed = False
    lines = []
    for line in frontmatter:
        key = line.split(":", 1)[0].strip()
        if key in remaining:
            lines.append(f"{key}: {remaining.pop(key)}")
            changed = True
        else:
            lines.append(line)
    for key, value in remaining.items():
        lines.append(f"{key}: {value}")
        changed = True
    if not changed:
        return text
    return "---\n" + "\n".join(lines) + body


def set_status(args: argparse.Namespace) -> int:
    if args.status is None and args.current_mode is None:
        raise ValueError("provide --status or --current-mode")
    vault = Path(args.vault).expanduser().resolve()
    path = resolve_inside_vault(vault, Path(args.file))
    text = path.read_text(encoding="utf-8")
    updated = set_frontmatter_fields(
        text,
        {"status": args.status, "current_mode": args.current_mode},
    )
    path.write_text(updated, encoding="utf-8")
    print(path)
    return 0


def print_uri(args: argparse.Namespace) -> int:
    vault = Path(args.vault).expanduser().resolve()
    path = resolve_inside_vault(vault, Path(args.file))
    print(obsidian_open_uri(args.vault_name, path.relative_to(vault).as_posix()))
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="Write Obsidian action memory files.")
    root.add_argument("--vault", default=str(DEFAULT_VAULT), help="Obsidian vault path.")
    root.add_argument("--vault-name", default=DEFAULT_VAULT.name, help="Obsidian vault name.")
    sub = root.add_subparsers(dest="command", required=True)

    create = sub.add_parser("create", help="Create a standard action memory file.")
    create.add_argument("--department", required=True)
    create.add_argument("--task-id", required=True)
    create.add_argument("--title")
    create.add_argument("--status", default="planned")
    create.add_argument("--risk-level", default="low")
    create.add_argument("--current-mode", default="坤")
    create.add_argument("--skills", default="")
    create.add_argument("--plugins", default="")
    create.add_argument("--related-files", default="")
    create.add_argument("--notify", default="")
    create.add_argument("--requires-user-confirmation", action="store_true")
    create.add_argument("--user-goal", default="待补充。")
    create.add_argument("--action-goal", default="待补充。")
    create.add_argument("--context", default="待补充。")
    create.add_argument("--unknowns", default="待确认。")
    create.add_argument("--materials", default="")
    create.add_argument("--forbidden-materials", default="本地隐私资料")
    create.add_argument("--planned-changes", default="")
    create.add_argument("--first-step", default="记录行动记忆。")
    create.add_argument("--risks", default="低。")
    create.add_argument("--mitigations", default="小步执行并记录。")
    create.add_argument("--notify-reason", default="无需通知。")
    create.add_argument("--next-step", default="执行并记录结果。")
    create.add_argument("--when", help="Local time in YYYY-MM-DDTHH:MM format.")
    create.add_argument("--overwrite", action="store_true")
    create.set_defaults(func=create_memory)

    append = sub.add_parser("append-log", help="Append a timestamped log block.")
    append.add_argument("--file", required=True, help="Vault-relative or absolute memory file path.")
    append.add_argument("--message", required=True)
    append.add_argument("--when")
    append.set_defaults(func=append_log)

    status = sub.add_parser("set-status", help="Update status/current_mode frontmatter.")
    status.add_argument("--file", required=True, help="Vault-relative or absolute memory file path.")
    status.add_argument("--status")
    status.add_argument("--current-mode")
    status.set_defaults(func=set_status)

    uri = sub.add_parser("uri", help="Print an Obsidian open URI for a vault file.")
    uri.add_argument("--file", required=True, help="Vault-relative or absolute file path.")
    uri.set_defaults(func=print_uri)
    return root


def main() -> int:
    args = parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
