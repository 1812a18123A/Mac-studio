---
type: gui_help_only_execution_confirmation_package
project_id: mano-p
date: 2026-06-17
confirmation_package_id: mano-p-stage-1-help-only-exec-confirm-2026-06-17
owner_department: GUI 自动化部
status: prepared_waiting_department_review
risk_level: high
current_mode: 坎-艮-兑
related_runtime_gate_plan:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Runtime_Gate_Plan.md
related_candidate_package:
  - AgentVault/30_GUI_Automation/Plans/2026-06-17_Mano-P_Stage_1_Help_Only_Runtime_Candidate_Package.md
related_candidate_review:
  - AgentVault/50_Memory/Department_Handoffs/real-v0-3-mano-p-help-only-candidate-review_summary.md
related_action_memory:
  - AgentVault/50_Memory/Action_Logs/2026-06-17/2026-06-17_22-30_gui-自动化部_mano-p-help-only-execution-confirmation-package.md
requires_user_confirmation_before_execution: true
requires_department_review_before_execution: true
execution_authorized: false
runner_file_creation_authorized: false
---

# Mano-P Stage 1 Help-only Execution Confirmation Package

重要：本确认包仍不是执行授权。它只用于下一轮安全部、工程部、记忆部复审和用户确认；当前不允许创建 runner 文件，也不允许执行 `/opt/homebrew/bin/mano-cua --help`。

## 1. Confirmation 结论

当前状态：

- `confirmation_package_id`: mano-p-stage-1-help-only-exec-confirm-2026-06-17
- `command_class`: help-only
- `execution_confirmation_package_prepared`: yes
- `execution_authorized`: no
- `runner_file_creation_authorized`: no
- `runner_pseudocode_review_only`: yes
- `exact_binary_status`: documented_not_executed
- `clean_home_status`: placeholder_defined_not_created
- `run_cwd_status`: placeholder_defined_not_created
- `environment_allowlist_status`: documented_not_applied
- `full_output_storage_allowed`: false
- `pre_secret_scan_required`: true
- `department_review_required`: yes
- `user_confirmation_required`: yes

下一步只允许：

```text
让安全部、工程部、记忆部复审本确认包。
```

仍然禁止：

```text
执行 help-only runtime。
```

## 2. Scope

未来唯一候选 runtime 形态：

- binary: `/opt/homebrew/bin/mano-cua`
- arguments: `--help`
- command class: `help-only`
- shell: not allowed
- GUI: not allowed
- network/cloud/session: not expected and treated as stop condition
- full output storage: not allowed

本确认包不允许：

- `mano-cua run`
- `mano-cua check`
- `mano-cua config`
- `mano-cua stop`
- `mano-cua install-sdk`
- `mano-cua install-model`
- `mano-cua --local`
- Homebrew tap/install/update/upgrade/reinstall
- any app/url launch
- any screenshot
- any permission grant
- any cloud or local model session
- any model, SDK, binary, package, or skill download

## 3. Exact Binary

Candidate binary:

```text
/opt/homebrew/bin/mano-cua
```

Recorded read-only status from candidate package:

- file type: symbolic link
- symlink target: `../Cellar/mano-cua/1.1.4/bin/mano-cua`
- resolved Homebrew wrapper: `/opt/homebrew/Cellar/mano-cua/1.1.4/bin/mano-cua`
- wrapper was read, not executed.

Future preflight may only verify:

- file metadata
- symlink target
- wrapper text summary
- repository status

Future preflight must not:

- execute the wrapper
- import `visual`
- call any Python entrypoint
- read real `$HOME/.mano/config.json` values
- create cloud sessions
- open apps or URLs
- create screenshots
- write config

## 4. Directory Lifecycle

Clean HOME placeholder:

```text
<CLEAN_HOME>
```

Run cwd placeholder:

```text
<RUN_CWD>
```

Lifecycle rules:

- Directories are not created by this confirmation package.
- A future separately reviewed runner may create the directories immediately before a future approved run.
- Both paths must be outside the repository and outside the real user HOME.
- `<CLEAN_HOME>` must not contain `.mano` before the future run unless the test setup explicitly creates it and records why.
- Public docs should keep placeholders; do not commit private real paths if they reveal sensitive local structure.
- Cleanup must be reviewed after post-run inspection.
- Cleanup must use exact recorded paths only; no fuzzy deletion and no broad recursive deletion patterns.

## 5. Environment Allowlist

Future execution must use an empty inherited environment plus explicit allowlist only.

Allowed environment summary:

```text
HOME=<CLEAN_HOME>
PATH=/opt/homebrew/bin:/usr/bin:/bin
LANG=en_US.UTF-8
LC_ALL=en_US.UTF-8
MANO_RUNTIME_GATE=help-only
```

Disallowed inherited environment:

- token variables
- API keys
- SSH agent variables
- GitHub auth variables
- browser automation variables
- agent shell variables
- real HOME
- model path variables
- SDK path variables
- any variable that points to private project or account state

## 6. Runner Pseudocode

This is pseudocode only. Do not save it as a file. Do not execute it.

```text
PSEUDOCODE ONLY

require all confirmations:
  user_confirmation_scope == "help-only"
  safety_confirmation == approved
  engineering_confirmation == approved
  memory_confirmation == approved

define argv as:
  [EXACT_BINARY, "--help"]

define env as:
  HOME=<CLEAN_HOME>
  PATH=/opt/homebrew/bin:/usr/bin:/bin
  LANG=en_US.UTF-8
  LC_ALL=en_US.UTF-8
  MANO_RUNTIME_GATE=help-only

define cwd as:
  <RUN_CWD>

start child process:
  shell=false
  argv=list_only
  cwd=<RUN_CWD>
  env=allowlist_only
  stdout=memory_only
  stderr=memory_only
  timeout_seconds=10

on timeout:
  terminate child
  mark stop_condition_hit=true
  store no full output

on output:
  apply size limits before summarization
  redact forbidden categories
  store summary fields only
```

Runner constraints:

- no shell
- no inherited environment
- no executable runner file in this step
- no one-click command in docs
- stdout/stderr memory only
- timeout: 10 seconds
- output summary only

## 7. Output Limits

Full stdout and stderr must not be committed or stored in action memory.

Future runner limits before summarization:

- stdout maximum: 64 KiB or 200 lines, whichever is reached first.
- stderr maximum: 64 KiB or 200 lines, whichever is reached first.
- output beyond limits must be discarded after setting `output_limit_hit: true`.
- if output contains sensitive content, record only `sensitive_output_intercepted: true`.

Allowed summary fields:

```text
exit_code:
duration_ms:
stdout_line_count:
stderr_line_count:
stdout_truncated:
stderr_truncated:
contains_usage_text:
contains_network_terms:
contains_permission_terms:
contains_gui_terms:
contains_config_value_like_text:
secret_scan_result:
stop_condition_hit:
sensitive_output_intercepted:
```

Forbidden output storage:

- full stdout
- full stderr
- real HOME path
- config values
- device id
- session id
- token-like strings
- stack traces containing private paths
- output beyond approved size limits

## 8. Redaction Policy

Redact or intercept these categories before saving any summary:

- real HOME path
- `$HOME/.mano/config.json` values
- API keys, access tokens, OAuth strings, GitHub tokens, SSH key material
- device identifiers and serial-like values
- session identifiers
- cloud endpoint session bodies
- local private paths outside approved placeholders
- stack traces that contain private paths
- browser, app, account, chat, payment, or private document context

If any category appears:

```text
sensitive_output_intercepted: true
```

Do not save the sensitive text itself.

## 9. Preflight Checklist

Before any future execution, all items must be checked and recorded:

- [ ] User has explicitly confirmed help-only scope.
- [ ] 安全部 has approved this confirmation package.
- [ ] 工程部 has approved this confirmation package.
- [ ] 记忆部 has approved this confirmation package.
- [ ] Repository status is clean.
- [ ] No `mano-cua` runtime command has been executed in this step.
- [ ] Exact binary metadata is checked without execution.
- [ ] Symlink target is checked without execution.
- [ ] Wrapper text is summarized without execution.
- [ ] `<CLEAN_HOME>` is outside repository and outside real HOME.
- [ ] `<RUN_CWD>` is outside repository and outside real HOME.
- [ ] Real `$HOME/.mano/config.json` values are not read.
- [ ] Environment allowlist is exactly defined.
- [ ] Output size limits are defined.
- [ ] Secret scan rules are ready before execution.
- [ ] Stop conditions are reviewed.

Forbidden preflight activity:

- executing `/opt/homebrew/bin/mano-cua`
- importing `visual`
- calling Python entrypoints
- reading real config values
- opening GUI/apps/URLs
- taking screenshots
- granting permissions
- installing, downloading, tapping, updating, or upgrading

## 10. Required Confirmations

All four confirmations are required before any future execution:

```text
user_confirmation_scope:
safety_confirmation:
engineering_confirmation:
memory_confirmation:
```

Required user confirmation scope:

```text
Only /opt/homebrew/bin/mano-cua with --help, isolated clean HOME, isolated run cwd, no GUI, no screenshot, no cloud/local mode, no install/download, redacted summary only.
```

Department confirmations must explicitly mention:

- no cloud/local
- no GUI/screenshot/permission
- no config value read
- no full output storage
- no inherited secrets
- stop on network/session/cloud/config/GUI/permission/download/install terms

## 11. Post-run Verification Checklist

If a future separately approved run occurs, immediately verify and record:

- [ ] Repository status unchanged.
- [ ] No real HOME `.mano` write.
- [ ] `<CLEAN_HOME>` writes summarized by relative path and count only.
- [ ] No GUI/window/app/browser opened.
- [ ] No permission prompt appeared.
- [ ] No download/install/model/SDK occurred.
- [ ] No cloud/session/network text appeared in output.
- [ ] stdout/stderr saved only as redacted summary.
- [ ] Secret scan found no token-like output.
- [ ] stop condition state recorded.
- [ ] sensitive output interception state recorded.

## 12. Stop Conditions

Immediately stop and escalate if any of these occur:

- timeout
- network/session/cloud text appears
- permission prompt appears
- GUI overlay/window/browser/app appears
- screenshot-related text appears
- config value appears
- write outside `<CLEAN_HOME>` appears
- real HOME path appears
- token-like text appears
- download/install/model/SDK text appears
- non-help subcommand text appears
- command attempts fallback to `check`, `config`, `run`, `stop`, `install-sdk`, or `install-model`
- stdout/stderr exceeds approved limits

## 13. Action Memory Fields For Future Execution

Before any future execution, create a fresh action memory with:

```text
confirmation_package_id: mano-p-stage-1-help-only-exec-confirm-2026-06-17
command_class: help-only
exact_binary:
exact_binary_status:
wrapper_target_summary:
clean_home:
clean_home_status:
run_cwd:
run_cwd_status:
environment_allowlist_summary:
timeout_seconds: 10
redaction_policy:
full_output_storage_allowed: false
pre_secret_scan_required: true
expected_network: none
expected_permissions: none
expected_gui: none
expected_writes:
preflight_result:
user_confirmation:
user_confirmation_scope:
safety_confirmation:
engineering_confirmation:
memory_confirmation:
department_confirmations:
actual_exit_code:
actual_duration_ms:
actual_output_summary:
post_run_verification:
post_verification_result:
secret_scan_result:
post_secret_scan_result:
stop_condition_hit:
sensitive_output_intercepted:
next_step:
```

## 14. Go / No-Go

Current decision:

- `go_review_confirmation_package`: yes
- `go_create_runner_file`: no
- `go_execute_help_only_runtime`: no
- `go_gui`: no
- `go_screenshot`: no
- `go_cloud`: no
- `go_local`: no
- `go_install_or_download`: no

## 15. Next Step

下一步只允许：

```text
让安全部、工程部、记忆部复审本确认包。
```

仍然禁止：

```text
执行 /opt/homebrew/bin/mano-cua --help
```
