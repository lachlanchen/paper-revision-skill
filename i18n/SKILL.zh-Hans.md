# Paper Revision Skill 中文版

> 说明：这是根目录 [`SKILL.md`](../SKILL.md) 的简体中文说明版，方便阅读、教学和转交给合作者。正式安装给 Codex 使用时，active skill 仍然是根目录的 `SKILL.md`。

## 核心工作流

1. 先判断当前修稿阶段：审稿回复、大修、小修、proof correction，或最终提交包。
2. 编辑前先检查相关文件：当前 `main.tex`、当前 `sm.tex`、基线文件、response letter、PDF 和 build scripts。
3. 对于实质性写作修改，必须先在 `references/` 下创建或更新一个计划 markdown，再修改 TeX 文件。计划要写清楚范围、理由、目标文件、修改前后文本和验证步骤。
4. 保持 active 文件名稳定。通常把 `main.tex` 和 `sm.tex` 作为当前最新可编辑文件，把旧版本保存为命名清楚的基线文件。
5. 只在已接受的计划范围内编辑。技术性 claim 必须由数据、图、表，或用户确认的事实支持。
6. 修改 manuscript 后，重新编译当前 PDF，并刷新对应的 redlined 文件。
7. 从编译后的 PDF 验证修改，而不只看源 TeX。没有行号时，使用页码、栏位和段落开头作为定位锚点。
8. 如果项目工作流要求，每完成一个 revision unit 后就 commit and push。

## 必需的仓库约定

- 保持 active manuscript 文件名稳定，通常是 `main.tex` 和 `sm.tex`。
- 保留基线文件，例如 `original_main.tex`、`original_sm.tex`、`major_revision_main.tex` 和 `major_revision_sm.tex`。
- 生成 redline 文件，例如 `redlined_main.tex`、`redlined_sm.tex`、`redlined_minor_main.tex` 和 `redlined_minor_sm.tex`。
- 把任务计划、审查记录和修改理由存放在 `references/` 下。
- 不要悄悄覆盖基线文件。如果没有基线文件，记录 redline 生成受到限制。

## 计划纪律

- 把思考和编辑分开。先决定应该改什么、为什么改；然后只执行这个有边界的计划。
- 如果计划太大、太脆弱，或难以验证，就拆成更小的计划。
- 计划 markdown 按任务或 revision unit 存储，不需要每一轮聊天都生成一个文件。
- 如果另一个模型或合作者给出了修改策略，先把策略保存到 plan markdown，再执行。
- 如果计划发生变化，先更新计划，再应用修改。

## 计划命名与范围

- 使用 lowercase snake_case 文件名，例如 `references/reviewer1_comment1_revision2_tone_softening.md`。
- 尽量以来源开头，例如 `reviewer1_comment3`、`editor_comment`、`figure4`、`main_text`、`response_letter`、`supplement`、`proof` 或 `global`。
- 当一个已执行过的任务需要再次修改时，加入 `revisionN`。
- 除非用户明确批准全局 pass，否则一个 plan 对应一个可执行 work package。
- 如果一个 plan 同时混合科学逻辑、格式、图像工作、response 写作和 build repair，而且没有单一清晰目的，就拆分它。

## 执行阶段

1. 冻结并梳理 active 文件、基线文件、图、bibliography 和 build scripts。
2. 如果涉及 reviewer comments，先草拟 response strategy，再改 manuscript。
3. 创建或更新 markdown plan，写清楚允许修改的文件、允许修改的位置、禁止修改的内容、理由、验收标准、build steps 和 response-letter 影响。
4. 只应用已批准的计划。
5. 根据需要编译 manuscript、supplement、response letter、cover letter 和 redlines。优先使用项目已有 build script；如果没有，可以使用 `scripts/build_all_revision_artifacts.sh` 或 `scripts/build_revision_redlines.sh`。
6. 从最终 PDF 验证位置之后，才更新 response letter 或 proof-correction 文本。
7. 在 plan 或 audit note 中记录偏离计划的地方、未解决问题和 build 状态。

## Redline 纪律

- 保留基线文件，例如 `original_main.tex`、`original_sm.tex`、`major_revision_main.tex` 或 `major_revision_sm.tex`。
- 生成 redline 文件，例如 `redlined_main.tex`、`redlined_sm.tex`、`redlined_minor_main.tex` 和 `redlined_minor_sm.tex`。
- 如果 `latexdiff` 破坏数学公式或 display environments，写一个可重复运行的脚本修复，而不是依赖一次性的手动修改。
- 即使期刊不要求提交 redline，也把 redline 作为内部验证工具。

## Response 与 Proof 规则

- 对 reviewer response，要回答三个问题：改了什么、为什么能解决 concern、修改出现在什么位置。
- 最终位置要根据当前 manuscript PDF 确认。redlined 文件用于识别修改，但不能作为唯一的位置依据。
- 定位修改时，可以用 `pdftotext -layout` 或 `scripts/pdf_location_audit.py` 搜索编译后的 PDF。提取出的行号只能作为搜索辅助，不是期刊 manuscript line number。最终 response 中应使用页码、section、figure/table/equation、视觉确认后的 column，以及 paragraph-beginning anchor。
- 对 proof corrections，如果仍有任何错误需要修改，应选择 `Request Revisions`。逐条写清楚准确位置、当前 proof 文本和建议修改后的文本。
- 避免没有支持的 claim。如果某个计算或实验实际上没有做，就删除或弱化相关表述。

## 计划质量检查清单

编辑前确认 plan 回答了这些问题：

- 这个修改解决的具体问题是什么？
- 它对应哪位 reviewer、editor、proof query，或内部目标？
- 哪些文件和位置可以修改？
- 哪些内容明确不在范围内？
- 哪个 claim 被新增、删除、弱化或澄清？
- 如何通过 PDF、redline、log 或搜索验证结果？
- response letter 或 proof note 应该如何同步更新？

## 失败处理

- 如果任务在执行中变大，停止并创建新 plan，不要悄悄扩大范围。
- 如果 response letter 过度声称，弱化 response，或在新的批准计划下修改 manuscript。
- 如果 build 失败，只修复当前 plan 导致的 build error。除非用户授权，不做更大范围 cleanup。
- 如果 PDF 位置无法验证，不要编造页码、行号、段落、图、表或公式引用。
- 如果发现范围外问题，把它记录为 `Out-of-Scope Discovery`，不要静默修复。

## Agent 操作契约

- 创建或读取相关计划之前，不编辑 manuscript 文件。
- 不超过计划范围。
- 未经允许，不合并无关 reviewer comments。
- 不编造验证细节。
- 不让 build 状态保持未知。
- 不隐藏不确定性；显式记录未解决事项。
- 保持 `references/` 对下一位 agent 有用。

## 参考资源

需要时阅读这些文件：

- [`references/plan-first-revision-method.md`](../references/plan-first-revision-method.md)：完整的计划闸门式修稿方法。
- [`references/latex-revision-file-map.md`](../references/latex-revision-file-map.md)：main、supplement、baseline、latest 和 redline 文件约定。
- [`references/response-letter-proof-workflow.md`](../references/response-letter-proof-workflow.md)：response letter 和 proof correction 模式。
- [`references/origin-chat-plan-gated-revision.md`](../references/origin-chat-plan-gated-revision.md)：清理后的起源对话和教学说明。
- [`templates/revision_plan.md`](../templates/revision_plan.md)：标准的 pre-edit plan 模板。
- [`templates/response_trace_audit.md`](../templates/response_trace_audit.md)：response-letter 验证模板。
- [`prompts/plan_prompt.md`](../prompts/plan_prompt.md)、[`prompts/apply_prompt.md`](../prompts/apply_prompt.md) 和 [`prompts/audit_prompt.md`](../prompts/audit_prompt.md)：strategist、executor 和 auditor 工作流提示词。
- [`scripts/build_all_revision_artifacts.sh`](../scripts/build_all_revision_artifacts.sh)：编译常见 manuscript、supplement、response、cover 和 redline artifacts。
- [`scripts/pdf_location_audit.py`](../scripts/pdf_location_audit.py)：查找保守的 PDF-backed location anchors。
