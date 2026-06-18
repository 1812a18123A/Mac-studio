#!/usr/bin/env python3
"""Read-only audit for Chinese-first Obsidian retrieval metadata."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Mapping, Sequence


DEFAULT_VAULT = Path(__file__).resolve().parents[3]
DEFAULT_ROOT = Path("AgentVault")

TITLE_KEYS = ("中文标题", "chinese_title", "title_zh")
SUMMARY_KEYS = ("中文摘要", "summary_zh", "summary_zh_cn")
SEARCH_KEYS = ("检索元素", "search_keywords", "search_terms_zh", "检索词", "keywords")
INDEX_BLOCK_MARKERS = (
    "## 中文检索索引",
    "## 中文检索入口",
    "## 0. 中文检索入口",
    "中文检索索引",
    "中文检索入口",
)
PRIVATE_PARTS = {
    "Private",
    ".obsidian",
    ".git",
    ".external",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "screenshots",
    "Screenshots",
    "raw",
    "Raw",
    "logs",
    "Logs",
}
CHINESE_TEXT = re.compile(r"[\u4e00-\u9fff]")


@dataclass(frozen=True)
class Finding:
    path: str
    missing: Sequence[str]
    severity: str


@dataclass(frozen=True)
class AuditResult:
    scanned: int
    passed: int
    skipped: int
    findings: Sequence[Finding]


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


def markdown_files(root: Path) -> Iterable[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def should_skip(path: Path, include_private: bool) -> bool:
    if include_private:
        return False
    return any(part in PRIVATE_PARTS for part in path.parts)


def split_frontmatter(text: str) -> tuple[Mapping[str, List[str]], str]:
    if not text.startswith("---\n"):
        return {}, text
    lines = text.splitlines()
    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, text
    fields: dict[str, List[str]] = {}
    current_key: str | None = None
    for line in lines[1:end_index]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line.startswith((" ", "\t")) and stripped.startswith("- ") and current_key:
            value = stripped[2:].strip().strip('"').strip("'")
            fields.setdefault(current_key, []).append(value)
            continue
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            current_key = key.strip()
            fields.setdefault(current_key, [])
            value = value.strip().strip('"').strip("'")
            if value:
                fields[current_key].append(value)
    body = "\n".join(lines[end_index + 1 :])
    return fields, body


def has_field(fields: Mapping[str, Sequence[str]], keys: Sequence[str]) -> bool:
    return any(key in fields for key in keys)


def has_body_marker(body: str, markers: Sequence[str]) -> bool:
    return any(marker in body for marker in markers)


def has_chinese_retrieval_text(body: str) -> bool:
    markers = ("中文关键词", "中文检索词", "常用搜索词", "中文检索元素")
    return any(marker in body for marker in markers)


def severity_for(relative_path: str, missing: Sequence[str]) -> str:
    if (
        relative_path.endswith("/README.md")
        or "/Baselines/" in relative_path
        or "/20_Engineering/Tools/" in relative_path
    ):
        return "low"
    if "Action_Logs/" in relative_path or "Department_Handoffs/" in relative_path:
        return "high" if len(missing) >= 2 else "medium"
    return "medium" if len(missing) >= 2 else "low"


def audit_file(path: Path, relative_path: str) -> Finding | None:
    text = path.read_text(encoding="utf-8")
    fields, body = split_frontmatter(text)
    missing: list[str] = []
    if not has_field(fields, TITLE_KEYS):
        missing.append("中文标题")
    if not has_field(fields, SUMMARY_KEYS):
        missing.append("中文摘要")
    if not has_field(fields, SEARCH_KEYS) and not has_chinese_retrieval_text(body):
        missing.append("中文检索词")
    if not has_body_marker(body, INDEX_BLOCK_MARKERS):
        missing.append("中文检索索引")
    if not missing:
        return None
    return Finding(relative_path, missing, severity_for(relative_path, missing))


def audit_vault(vault: Path, root: Path, include_private: bool = False) -> AuditResult:
    root_path = resolve_inside_vault(vault, root)
    scanned = 0
    skipped = 0
    findings: list[Finding] = []
    vault_root = vault.expanduser().resolve()
    for path in markdown_files(root_path):
        relative_path = path.relative_to(vault_root).as_posix()
        if should_skip(path.relative_to(root_path), include_private):
            skipped += 1
            continue
        scanned += 1
        finding = audit_file(path, relative_path)
        if finding:
            findings.append(finding)
    return AuditResult(scanned, scanned - len(findings), skipped, findings)


def render_markdown(result: AuditResult, root: str, max_findings: int) -> str:
    lines = [
        "# 中文检索只读审计报告",
        "",
        f"- 扫描根目录：`{root}`",
        f"- 扫描文件数：{result.scanned}",
        f"- 通过文件数：{result.passed}",
        f"- 缺失文件数：{len(result.findings)}",
        f"- 跳过文件数：{result.skipped}",
        "",
    ]
    if not result.findings:
        lines.extend(["## 结果", "", "未发现缺失项。"])
        return "\n".join(lines)

    lines.extend(
        [
            "## 缺失清单",
            "",
            "| 严重度 | 文件 | 缺失项 |",
            "| --- | --- | --- |",
        ]
    )
    shown = result.findings[:max_findings]
    for finding in shown:
        missing = "、".join(finding.missing)
        lines.append(f"| {finding.severity} | `{finding.path}` | {missing} |")
    remaining = len(result.findings) - len(shown)
    if remaining > 0:
        lines.extend(["", f"还有 {remaining} 个文件未显示；可提高 `--max-findings` 查看更多。"])
    return "\n".join(lines)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        description="Read-only audit for Chinese-first Obsidian retrieval fields."
    )
    root.add_argument("--vault", default=str(DEFAULT_VAULT), help="Vault root path.")
    root.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Vault-relative directory to scan. Defaults to AgentVault.",
    )
    root.add_argument(
        "--include-private",
        action="store_true",
        help="Include Private/.obsidian/.git paths. Off by default.",
    )
    root.add_argument(
        "--max-findings",
        type=int,
        default=80,
        help="Maximum findings to print in the report.",
    )
    root.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="Exit with status 1 when missing Chinese retrieval metadata is found.",
    )
    return root


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    result = audit_vault(Path(args.vault), Path(args.root), args.include_private)
    print(render_markdown(result, args.root, max(0, args.max_findings)))
    if args.fail_on_findings and result.findings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
