---
type: action_memory
date: 2026-06-17
time: "21:46"
department: GUI-自动化部
task_id: mano-p-python-source-review
status: completed
risk_level: medium
current_mode: 坤-坎-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
notify_departments:
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部
requires_user_confirmation: true
---

# 行动记忆：Mano-P Stage 1 Python Source 只读审查

## 1. 用户目标

用户想要什么：
- 继续推进 Mano-P Stage 1，但保持稳定，不运行 mano-cua、不安装下载、不授权或操作 GUI。

## 2. 本次行动目标

这一次只做什么：
- 本次只读审查 Python requirements、visual/vla.py 和安全相关 source entrypoint，并写回行动记忆与 Stage 1 文档。

## 3. 当前上下文

已知信息：
- 上一步 formula/dependency 审查已完成。
- Formula 会执行 `pip install -r requirements.txt`，Homebrew dependency tree 不能覆盖真实 Python runtime dependency surface。
- Runtime wrapper 会读取 `$HOME/.mano/config.json` 的 `python-path`。
- 用户已确认继续执行下一步建议。

未知信息：
- 已安装 artifact 是否保留 `requirements.txt`。
- `visual/vla.py` 是否在 `--help`、`check` 或 import 阶段初始化截图、权限、cloud、SDK/model 或 GUI 控制。
- 是否存在用户本地 `$HOME/.mano/config.json`，以及它是否会影响后续运行风险。

## 4. 涉及资料

需要读取或参考的资料：
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
  - 已安装 `mano-cua` artifact 中的 `requirements.txt`、`visual/vla.py` 和安全相关 Python source。
  - 只读取 `$HOME/.mano/config.json` 是否存在；若存在，只摘要安全键名，不记录隐私值。

禁止使用或不能外发的资料：
  - 本地隐私资料
  - GitHub token、SSH key、账号认证信息
  - 真实内部 thread id
  - 完整个人配置值、截图、窗口内容、设备序列号

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 Python source 只读审查报告。
  - 更新 Stage 1 执行清单、安装计划和 PoC checklist 状态。
  - 更新本行动记忆。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不执行 `mano-cua --help/check/run/install-sdk/install-model`
- 不执行 `brew install/tap/update/upgrade/reinstall`
- 不下载 SDK、模型、binary、Python 包或 skill
- 不授权 Screen Recording、Accessibility、Automation、Full Disk Access 等权限
- 不截图、点击、输入、读取当前 GUI 内容或启用 cloud mode

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：写入和更新可审计行动记忆。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 只读定位已安装 artifact 中的 requirements 和 source entrypoint。
- [x] Step 3: 只读审查 `visual/vla.py` 及安全相关模块引用。
- [x] Step 4: 写入 Python source 审查报告并更新 Stage 1 文档。
- [x] Step 5: 扫描敏感信息、提交并推送文档。

## 10. 风险检查

风险：
- 中。Python source 可能涉及 API key、cloud mode、截图、权限、模型下载、GUI 控制或用户本地配置路径。

缓解措施：
- 只读定位和读取源码，不运行 Python 入口。
- 不保存完整隐私配置值，只记录是否存在和安全键名级摘要。
- 提交前扫描 thread id、token、私钥模式。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 安全部
  - 工程部
  - 记忆部

通知原因：
- GUI 自动化部负责 PoC 路线。
- 安全部关注 cloud/screenshot/permission/GUI control 风险。
- 工程部关注 dependency/source entrypoint 与可维护性。
- 记忆部负责行动记忆归档。

## 12. 执行结果

实际做了什么：
- 只读读取 Homebrew cache tarball 中的 `requirements.txt`，未解压落盘。
- 只读读取已安装 artifact 中的 `visual/vla.py`、config、cloud/local agent、computer executor 和 task model。
- 只读取 `$HOME/.mano/config.json` 的顶层键名，未读取或记录配置值。
- 新增 Python source 审查报告。
- 更新 Stage 1 执行清单、安装计划、PoC checklist 和 formula review 报告。

成功：
- 成功。未运行 `mano-cua`，未安装、未下载、未授权、未截图、未点击、未输入、未启用 cloud mode。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-46_gui-自动化部_mano-p-python-source-review.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Python_Source_Review.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-46_gui-自动化部_mano-p-python-source-review.md

截图/日志/轨迹：
- 无截图。命令输出只摘要写入审查报告。

## 14. 下一步

下一步建议：
- 先写 runtime gate plan，定义 clean HOME、no cloud、no app/url、no bash、no screenshots、no clipboard、no mouse/keyboard 的命令闸门；仍不直接运行 `mano-cua`。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已完成 Python source 只读审查；默认 `run` 是 cloud mode，runtime 有截图、GUI 控制、bash、配置读取等风险。下一步应先写 runtime gate plan，不能直接运行。

## Log 2026-06-17 21:51

- 完成 Python source 只读审查：requirements 未 pin；默认 run 使用 cloud mode；runtime 可截图、打开 app/url、执行鼠标键盘动作、使用 bash，并受 ~/.mano/config.json 影响。下一步应先写 runtime gate plan。
