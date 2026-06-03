[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

LaTeX 論文、査読返信、redline、校正対応のための plan-gated な改訂ワークフロー。

> まず計画する。次に編集する。PDF で確認する。作業単位を commit する。

## できること

- 大きな編集の前に markdown の改訂計画を作る。
- `main.tex` と `sm.tex` を最新の編集対象として保つ。
- `original_main.tex` と `original_sm.tex` などの基準版を保存する。
- 内部確認用の redline を生成する。
- response letter を PDF で確認した位置情報に合わせる。

## はじめに

- メイン README: [../README.md](../README.md)
- Skill: [../SKILL.md](../SKILL.md)
- ビジュアルガイド: [../docs/origin-chat.html](../docs/origin-chat.html)
- 改訂計画テンプレート: [../templates/revision_plan.md](../templates/revision_plan.md)

## 中心ルール

```text
計画 -> 承認 -> 編集 -> ビルド -> PDF 確認 -> redline -> commit
```
