---
type: skill_example_draft
skill: obsidian-memory
status: draft
date: 2026-06-17
owner_department: 技能优化部
not_active_rule: true
related_safety_boundary: AgentVault/70_Safety/Permission_Boundaries.md
---

# obsidian-memory 示例草稿：失败处理与跨部门交接

> 本文件只是 `$obsidian-memory` 的示例草稿，不是已生效规则。
> 使用前应由总控办公室、记忆部、安全部或 SkillOpt 审核。

## 1. 适用场景

这些示例用于帮助部门会话在以下情况保持可审计：

- 执行步骤失败，需要把失败原因写回行动记忆。
- 任务进入风险、权限或不确定状态，需要设置 `status` 和 `current_mode`。
- 需要用户确认，不能继续扩大执行范围。
- 一个部门需要把任务交给另一个部门。
- 接收部门完成后，需要把结果回写到行动记忆或交接结果文件。
- 不确定或高风险时，需要引用安全边界文档。

## 2. 失败时追加行动日志

示例：读取文件失败、命令失败、测试失败、权限不足时，先停止扩大动作，然后追加事实记录。

`append-log` 应用于已经创建好的行动记忆。若本轮还没有行动记忆，应先使用 `create` 创建，再追加失败记录。`create` 会打印真实文件路径和 Obsidian URI；后续 `append-log`、`set-status`、`uri` 的 `--file` 必须使用该输出中的精确路径，或等价的 vault 相对 `AgentVault/...md` 路径，不要手写时间戳文件名。

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_工程部_example-task.md' \
  --message '失败记录：尝试读取指定文件时失败。实际动作：只运行了只读检查。原始命令：sed -n 1,80p path/to/file.md。原始错误：No such file or directory。日志路径：无额外日志文件。失败原因：目标文件不存在。已知信息：父目录存在。未知信息：文件是否改名或尚未创建。下一步：请求总控办公室确认正确路径，不继续创建替代文件。'
```

推荐日志包含：

- 实际做了什么。
- 成功了什么。
- 失败了什么。
- 失败原因或最接近的错误信息。
- 原始错误、原始命令或日志路径。
- 已知信息和未知信息。
- 当前停止点。
- 下一步建议。
- 需要通知的部门。

## 3. 失败时设置状态和卦态

失败后根据情况设置 frontmatter：

- 普通失败：`status: failed`，`current_mode: 坎-兑`。
- 权限或安全风险：`status: blocked`，`current_mode: 坎-艮`。
- 高风险动作等待用户确认：`status: blocked`，`current_mode: 坎-艮-兑`。
- 已恢复并完成：`status: completed`，`current_mode: 坤-兑`。

选择标准：

- 用 `failed`：动作已经失败，且无需等待用户授权即可停止并汇报。
- 用 `blocked`：下一步需要用户确认、权限授权、跨部门判断或安全审查，确认前不能继续。

示例：权限风险导致阻塞。

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  set-status \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_安全部_example-task.md' \
  --status 'blocked' \
  --current-mode '坎-艮'
```

示例：普通失败但已经完成汇报。

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  set-status \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_工程部_example-task.md' \
  --status 'failed' \
  --current-mode '坎-兑'
```

## 4. 需要用户确认时记录待确认事项

当任务涉及删除、外发、上传、安装、全局写入、GUI 控制、`.obsidian` 修改、密钥或隐私资料时，先写入待确认事项并停止。

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_总控办公室_example-task.md' \
  --message '待确认事项：本任务下一步会修改全局 skill 目录，属于 Permission_Boundaries.md 中需要用户确认的动作。已停止执行。需要用户确认：是否允许写入 /Users/peipei/.codex/skills/obsidian-memory/SKILL.md？确认前不修改全局 skill、不安装依赖、不继续扩大范围。通知部门：安全部、技能优化部。'
```

随后设置状态：

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  set-status \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_总控办公室_example-task.md' \
  --status 'blocked' \
  --current-mode '坎-艮-兑'
```

## 5. 跨部门交接包最小模板

交接包建议写入：

`AgentVault/50_Memory/Department_Handoffs/[task-id]_[receiving-department].md`

```markdown
---
type: department_handoff
date: YYYY-MM-DD
initiating_department: 发起部门
receiving_department: 接收部门
task_id: short-task-id
priority: low | medium | high | urgent
status: sent
current_state: 当前状态摘要
completed_work:
  - 已完成动作摘要
related_skills:
  - obsidian-memory
related_plugins:
  - codex_app thread tools
---

# 部门交接包：任务标题

## 背景
为什么需要交给该部门。

## 当前状态
任务当前处于什么阶段，是否有失败、阻塞或待确认事项。

## 已完成工作
- 发起部门已经完成的动作。
- 已读取或生成的资料。

## 相关行动记忆
- AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/example.md

## 相关资料
- 需要接收部门读取的本地文件或 Obsidian 路径。

## 请求接收部门完成
- 只做一个明确小步。

## 禁止事项
- 不删除文件。
- 不外发资料。
- 不安装依赖。
- 不扩大任务范围。

## 成功标准
- 接收部门完成后应满足什么。

## 结果回写
请将结果写入：
`AgentVault/50_Memory/Department_Handoffs/[task-id]_[receiving-department]_result.md`
```

发起部门发送交接包后，也应把交接动作写回自己的行动记忆：

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_总控办公室_example-task.md' \
  --message '已创建部门交接包：AgentVault/50_Memory/Department_Handoffs/example-task_安全部.md。接收部门：安全部。请求动作：审查权限边界。禁止事项：不执行外发、不改配置、不删除文件。'
```

## 6. 接收部门完成后的结果回写样例

接收部门应创建自己的行动记忆，并在完成后写结果文件或回写交接包指定位置。

结果文件示例：

```markdown
---
type: department_handoff_result
date: YYYY-MM-DD
department: 安全部
task_id: short-task-id
status: completed
related_handoff: AgentVault/50_Memory/Department_Handoffs/short-task-id_安全部.md
related_action_memory: AgentVault/50_Memory/Action_Logs/YYYY-MM-DD/YYYY-MM-DD_HH-mm_安全部_short-task-id.md
---

# 交接结果：任务标题

## 实际做了什么
- 读取交接包。
- 读取 Permission_Boundaries.md。
- 判断风险等级。

## 成功
- 已给出安全边界判断。

## 失败或阻塞
- 无。

## 新增资料
- 本结果文件。

## 下一步建议
- 总控办公室可根据本结果决定是否继续执行。
```

接收部门也应更新自己的行动记忆：

这里的 `append-log` 同样假设接收部门已经先创建了自己的行动记忆。

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_安全部_example-task.md' \
  --message '已完成交接任务。结果回写：AgentVault/50_Memory/Department_Handoffs/example-task_安全部_result.md。结论：该动作需要用户确认；确认前不得执行。'
```

## 7. 不确定或高风险时引用安全边界文档

当出现以下动作时，必须引用：

`AgentVault/70_Safety/Permission_Boundaries.md`

高风险或需确认动作包括：

- 删除、覆盖、批量移动、批量重命名。
- 修改 `.obsidian`、全局 skill、全局插件、系统配置。
- 安装依赖、升级工具、修改系统环境。
- 发送邮件、消息、表单、评论、PR、支付或任何外部提交。
- 上传本地文件、截图、音频、记忆文件、代码、密钥或日志。
- 使用 GUI 自动化、鼠标键盘控制、屏幕录制或截图采集。
- 写入 vault 外部路径、跨项目写入、全局目录写入。
- 处理密钥、账号、隐私资料、客户资料或敏感日志。

引用示例：

```bash
python3 '/Users/peipei/Documents/esmee AI/esmee AI/AgentVault/20_Engineering/Tools/obsidian_action_memory_writer.py' \
  --vault '/Users/peipei/Documents/esmee AI/esmee AI' \
  append-log \
  --file 'AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_15-00_GUI自动化部_example-task.md' \
  --message '安全边界引用：根据 AgentVault/70_Safety/Permission_Boundaries.md，启动 GUI 自动化、截图采集、鼠标键盘控制属于需要用户确认的动作。当前转入坎-艮模式，等待确认；确认前不进行点击、输入、截图或屏幕录制。'
```

## 8. 快速选择表

| 情况 | 先做什么 | status | current_mode | 通知部门 |
| --- | --- | --- | --- | --- |
| 文件不存在 | 记录失败事实 | failed 或 blocked | 坎-兑 | 总控办公室 |
| 权限不足 | 停止并记录权限风险 | blocked | 坎-艮 | 安全部 |
| 需要用户确认 | 写待确认事项 | blocked | 坎-艮-兑 | 总控办公室、安全部 |
| 跨部门任务 | 创建交接包 | in_progress | 坤-兑 | 接收部门 |
| 接收部门完成 | 回写结果 | completed | 坤-兑 | 发起部门 |
| 规则反复不够用 | 记录优化建议 | completed 或 blocked | 兑-坤 | 技能优化部 |

## 9. 草稿审核建议

后续若要把本草稿纳入 `$obsidian-memory` 正式规则，建议先做：

- 由记忆部检查路径和行动日志格式。
- 由安全部检查风险边界表述。
- 由技能优化部整理成最小示例，不扩大 skill 主体。
- 由工程部确认 writer 命令示例仍可运行。
- 由总控办公室决定是否发布到 `best_skill.md` 或全局 skill。
