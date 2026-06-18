---
type: action_memory
date: 2026-06-17
time: "21:33"
department: GUI-自动化部
task_id: mano-p-formula-review
status: completed
risk_level: medium
current_mode: 坤-坎-兑
related_skills:
  - obsidian-memory
related_plugins:
  - none
related_files:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
  - AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Metadata_Query_Result.md
notify_departments:
  - GUI 自动化部
  - 安全部
  - 记忆部
requires_user_confirmation: true
---

# 行动记忆：Mano-P Stage 1 Formula 只读审查

## 1. 用户目标

用户想要什么：
- 继续推进 Mano-P Stage 1，但保持项目稳定，不执行安装、运行、下载、授权或 GUI 自动化。

## 2. 本次行动目标

这一次只做什么：
- 本次只读审查 Homebrew formula 内容和依赖树，并把结论写回 Obsidian 行动记忆与 Stage 1 文档。

## 3. 当前上下文

已知信息：
- 用户已确认“继续执行”，上下文中的上一轮建议是只读审查 Homebrew formula 内容和依赖树。
- 上一轮 Option B 已完成，只查询了本机和 Homebrew metadata。
- `mano-cua` 与 `Mininglamp-AI/tap` 在本轮前已经存在于本机 Homebrew 环境。
- 本轮目标是只读分析，不运行 `mano-cua`。

未知信息：
- `mano-cua.rb` formula 是否包含 post-install、caveats、下载资源、依赖声明或运行入口细节。
- Homebrew dependency tree 是否揭示额外运行时风险。

## 4. 涉及资料

需要读取或参考的资料：
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
  - AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Metadata_Query_Result.md
  - `/opt/homebrew/Library/Taps/mininglamp-ai/homebrew-tap/Formula/mano-cua.rb`
  - Homebrew dependency metadata for `mininglamp-ai/tap/mano-cua`

禁止使用或不能外发的资料：
  - 本地隐私资料
  - GitHub token、SSH key、账号认证信息
  - 真实内部 thread id
  - 完整隐私路径清单、设备序列号、截图或窗口内容

## 5. 需要修改什么

计划修改的文件、配置、skill、插件、脚本：
  - 新增 formula/dependency 只读审查报告。
  - 更新 Stage 1 执行清单、安装计划和 PoC checklist 的状态与下一步。
  - 更新本行动记忆。

## 6. 不能做什么

本次明确禁止：
- 不删除文件，除非用户明确确认
- 不发送邮件、消息、付款、提交表单，除非用户明确确认
- 不上传截图、音频、记忆文件到外部服务，除非用户明确确认
- 不覆盖已有 skill，除非先备份
- 不跳过 Obsidian 行动记录
- 不执行 `brew install`、`brew tap`、`brew upgrade` 或 `brew update`
- 不执行 `mano-cua check/run/install-sdk/install-model`
- 不执行 `clawhub install`
- 不安装 SDK、模型、binary、skill 或依赖
- 不授权 Screen Recording、Accessibility、Automation、Full Disk Access 等权限
- 不截图、点击、输入、读取当前 GUI 内容或启用 cloud mode

## 7. 需要调用的 skill

本次需要：
  - obsidian-memory：创建并更新可审计行动记忆。

## 8. 需要使用的 Codex App 插件功能

本次需要：
  - none

## 9. 行动步骤

- [x] Step 1: 记录行动记忆。
- [x] Step 2: 只读读取 formula 文件内容。
- [x] Step 3: 只读读取 Homebrew dependency metadata。
- [x] Step 4: 写入审查报告并更新 Stage 1 文档。
- [x] Step 5: 扫描敏感信息、提交并推送文档。

## 10. 风险检查

风险：
- 中。Homebrew formula/dependency 信息可能包含本地路径、下载 URL、依赖来源或安装状态；若误执行命令可能触发安装、下载或运行。

缓解措施：
- 只用只读命令，设置 `HOMEBREW_NO_AUTO_UPDATE=1` 和 `HOMEBREW_NO_ANALYTICS=1`。
- 只写摘要，不保存完整长日志。
- 提交前扫描 thread id、token、私钥模式。

## 11. 部门通知

需要通知哪个部门：
  - GUI 自动化部
  - 安全部
  - 记忆部

通知原因：
- GUI 自动化部负责 Mano-P PoC 路线。
- 安全部关注安装/运行/权限/cloud mode 边界。
- 记忆部负责行动记忆与文档归档。

## 12. 执行结果

实际做了什么：
- 只读读取本地 Homebrew tap 中的 `mano-cua.rb` formula。
- 只读读取 `mininglamp-ai/tap/mano-cua` 的 Homebrew dependency tree 和 flat dependency list。
- 新增 formula/dependency 审查报告。
- 更新 Stage 1 执行清单、安装计划和 PoC checklist 的状态。

成功：
- 成功。未执行安装、tap、update、upgrade、`mano-cua` runtime、SDK/model 下载、权限授权、截图、点击、输入或 cloud mode。

失败：
- 无。

## 13. 产生的新资料

新增文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-33_gui-自动化部_mano-p-formula-review.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Research/2026-06-17_Mano-P_Stage_1_Formula_Dependency_Review.md

更新文件：
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Execution_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Isolated_Install_Plan.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/30_GUI_Automation/PoC_Checklists/Mano-P_PoC_Checklist.md
- /Users/peipei/Documents/esmee AI/esmee AI/AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_21-33_gui-自动化部_mano-p-formula-review.md

截图/日志/轨迹：
- 无截图。命令输出只做摘要写入审查报告。

## 14. 下一步

下一步建议：
- 等待用户确认是否只读审查 Python requirements、`visual/vla.py` 和 config/cloud/screenshot/permission/SDK/model 入口。

## 15. 给用户的简短汇报

用简短中文告诉用户：
- 已完成 formula/dependency 只读审查；发现 formula 会执行 `pip install -r requirements.txt`，所以还不能运行 `mano-cua`。下一步建议只读审查 Python requirements 和 source entrypoint。

## Log 2026-06-17 21:38

- 完成 formula/dependency 只读审查：formula 会执行 pip install -r requirements.txt；Homebrew deps 不能覆盖 Python runtime 依赖；下一步需确认只读审查 requirements/source entrypoint。
