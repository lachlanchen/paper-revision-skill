[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

用于 LaTeX 论文、审稿回复、redline 和 proof correction 的计划闸门式修稿工作流。

> 先计划，再编辑。用 PDF 验证，用 git 存档。

## 它解决什么问题

- 修改前先生成 markdown 计划，限制 agent 的编辑范围。
- 保持 `main.tex` 和 `sm.tex` 作为最新可编辑文件。
- 保留 `original_main.tex` 和 `original_sm.tex` 等基线文件。
- 自动生成 redline，方便检查修改是否越界。
- 根据最终 PDF 更新 response letter 的页码、段落、图表和公式位置。

## 从这里开始

- 主 README：[../README.md](../README.md)
- Skill 文件：[../SKILL.md](../SKILL.md)
- Skill 中文版：[SKILL.zh-Hans.md](SKILL.zh-Hans.md)
- 安装转交说明：[../HANDOFF.md](../HANDOFF.md)
- 可视化说明：[../docs/origin-chat.html](../docs/origin-chat.html)
- 修改计划模板：[../templates/revision_plan.md](../templates/revision_plan.md)

## 核心流程

```text
计划 -> 审核 -> 编辑 -> 编译 -> PDF 检查 -> redline -> commit
```
