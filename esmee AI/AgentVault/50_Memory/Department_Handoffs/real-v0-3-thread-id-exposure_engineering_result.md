---
type: department_handoff_result
task_id: real-v0-3-thread-id-exposure
department: 工程部
status: recommend_redact_commit
created_at: 2026-06-17
source_handoff: AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_engineering.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_18-34_工程部_real-v0-3-thread-id-exposure.md
---

# 工程部结果：real-v0-3-thread-id-exposure

## 结论

status: `recommend_redact_commit`

工程部建议采用“两步低破坏路径”：先用普通提交把正式 registry 脱敏，再把真实 thread id 迁移到本地私有 registry。暂不建议直接历史重写，除非安全部确认这些 thread id 等同高敏凭据、仓库是公开仓库，或用户明确要求从远端历史中尽力清理。

## 已读取资料

- `AgentVault/50_Memory/Department_Handoffs/real-v0-3-thread-id-exposure_engineering.md`
- `AgentVault/00_System/Department_Thread_Registry.md`
- `AgentVault/00_System/Repository_Policy.md`
- Git 只读状态与 registry 文件提交记录

只读检查结果：

- `Department_Thread_Registry.md` 在提交 `c22c923 docs: add department thread registry` 中加入。
- 本地 `rg` 检查显示真实 thread id 也存在于多份行动记忆中，不只存在于 registry。
- 当前本轮未修改 registry、未修改 `.gitignore`、未执行 rewrite/reset/force push、未提交、未 push、未操作 token 或 SSH key。

## 方案对比

### 1. 保留现状

成本最低，不需要改文件、不需要协调 Git 历史。

风险是正式资产继续公开内部调度入口，后续更多文档可能复制这些 thread id；如果仓库远端可被他人访问，内部操作拓扑会长期暴露。

适用条件：仓库严格私有、thread id 不能直接授权访问、用户接受内部元数据留在正式历史中。

工程部不推荐作为默认路径，只适合作为临时接受风险。

### 2. 普通提交脱敏

做法是在新的普通提交中把正式 registry 的真实 thread id 替换为稳定别名，例如 `control-window`、`engineering-window`，或 `local-only` 占位符；同时在文档中说明真实映射保存在本地私有 registry。

成本低，协作风险小，不破坏已有 clone，不需要 force push。缺点是历史提交中仍然能看到旧 thread id；GitHub 远端历史、fork、缓存或本地 clone 中也可能仍保留。

适用条件：thread id 是内部调度元数据，不是 token/SSH key/密码；目标是减少继续扩散和正式文档暴露，而不是保证历史不可见。

工程部推荐作为默认第一步。

### 3. 本地私有 registry

做法是保留一个脱敏的正式 registry 作为仓库资产，再新增本地私有映射文件，例如 `AgentVault_Local/Department_Thread_Registry.private.md` 或 vault 内被 `.gitignore` 明确忽略的路径。正式 registry 只保留部门、状态、职责、result 路径和别名。

成本中等，需要更新 `.gitignore`、Repository Policy 和调度说明；但长期维护最干净，能让 adapter 明确区分“公开协议”和“本地运行时映射”。

风险是本地私有文件丢失会影响调度，需要备份策略；多机器协作时每台机器都要有自己的私有映射。

工程部建议作为普通提交脱敏后的长期结构。

### 4. Git 历史重写

做法是用 `git filter-repo`、BFG 或等价流程重写包含 thread id 的提交历史，然后 force push，并要求所有协作者重新同步或重新 clone。

成本高，协作风险高，容易破坏已有分支、tag、PR、clone；即使重写，也不能保证已被 fork、拉取、截图、缓存或索引的内容完全消失。GitHub 侧如需清缓存或处理敏感数据，通常还需要仓库管理员配合。

适用条件：安全部判定 thread id 是高敏信息；仓库公开或已广泛共享；用户明确接受重写历史、force push 和协作者重建本地仓库的成本。

工程部不建议作为默认路径，只建议作为安全升级方案。

## 推荐路径

1. 由安全部先给风险等级：thread id 是否能被外部直接利用、仓库远端是否公开、是否已有外部协作者。
2. 若不是高敏凭据，走普通提交脱敏：正式 registry 改用部门别名或占位符，停止继续扩散真实 thread id。
3. 建立本地私有 registry，并把路径加入 `.gitignore`；后续 adapter 优先读取本地私有 registry，缺失时提示总控补齐，不从正式 registry 读取真实 id。
4. 对已存在的行动记忆，普通提交阶段不建议批量改历史；可以新增一份说明文件记录“历史中曾包含 thread id，后续停止公开记录”。
5. 只有当安全部和用户确认需要强清理时，再设计历史重写方案，并单独列出备份、通知、force push、协作者重建步骤。

## 需要用户确认的操作

- 修改正式 registry 脱敏并提交。
- 修改 `.gitignore` 或新增本地私有 registry 路径。
- 任何 `git filter-repo`、BFG、`git reset`、`git push --force`、tag 移动或远端历史处理。
- 联系 GitHub 或仓库管理员处理缓存、fork、公开泄露记录。

## 对后续 adapter 的建议

后续最小 adapter 应读取本地私有 registry 获取真实 thread id；正式 registry 只作为公共协议和部门状态表。这样可以保留 v0.3 调度能力，同时避免把运行时入口继续写入正式仓库资产。
