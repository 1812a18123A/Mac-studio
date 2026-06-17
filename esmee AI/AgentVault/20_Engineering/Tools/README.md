# Obsidian Action Memory Writer

最小本地 adapter，用 Python 标准库把行动记忆写入 Obsidian vault。

## 位置

- Writer: `AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py`
- Tests: `AgentVault/20_Engineering/Tools/test_obsidian_action_memory_writer.py`

## 创建行动记忆

```bash
python3 'esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault 'esmee AI' \
  create \
  --department '工程部' \
  --task-id 'example-task' \
  --title '示例任务' \
  --status 'planned' \
  --risk-level 'low' \
  --current-mode '坤' \
  --user-goal '记录用户目标。' \
  --action-goal '本次只做一个小步行动。'
```

输出两行：
- 新建的 Markdown 文件路径。
- 对应的 `obsidian://open` URI。

## 追加行动日志

```bash
python3 'esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault 'esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md' \
  --message '完成一个小步行动。'
```

## 生成 Obsidian 打开链接

```bash
python3 'esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault 'esmee AI' \
  uri \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md'
```

## 更新完成状态

```bash
python3 'esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault 'esmee AI' \
  set-status \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/example.md' \
  --status 'completed' \
  --current-mode '坤-兑'
```

## 验证

```bash
python3 -m unittest discover -s 'esmee AI/AgentVault/20_Engineering/Tools' -p 'test_*.py'
```

## 边界

- 不安装 Obsidian 插件。
- 不调用 REST API。
- 不修改 `.obsidian` 配置。
- 写入路径必须在 vault 内。
