[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

用於 LaTeX 論文、審稿回覆、redline 和 proof correction 的計劃閘門式修稿工作流。

> 先計劃，再編輯。用 PDF 驗證，用 git 存檔。

## 它解決什麼問題

- 修改前先產生 markdown 計劃，限制 agent 的編輯範圍。
- 保持 `main.tex` 和 `sm.tex` 作為最新可編輯文件。
- 保留 `original_main.tex` 和 `original_sm.tex` 等基線文件。
- 自動產生 redline，方便檢查修改是否越界。
- 根據最終 PDF 更新 response letter 的頁碼、段落、圖表和公式位置。

## 從這裡開始

- 主 README：[../README.md](../README.md)
- Skill 文件：[../SKILL.md](../SKILL.md)
- 視覺化說明：[../docs/origin-chat.html](../docs/origin-chat.html)
- 修改計劃模板：[../templates/revision_plan.md](../templates/revision_plan.md)

## 核心流程

```text
計劃 -> 審核 -> 編輯 -> 編譯 -> PDF 檢查 -> redline -> commit
```
