[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Plan-gated manuscript revision for LaTeX papers, reviewer responses, redlines, and proof corrections.

> Plan first. Edit second. Verify from the PDF. Commit the work package.

## What It Does

- Creates a markdown plan before substantial manuscript edits.
- Keeps `main.tex` and `sm.tex` as the latest editable files.
- Preserves baselines such as `original_main.tex` and `original_sm.tex`.
- Generates redlined files for internal verification.
- Synchronizes response letters with verified PDF locations.

## Start Here

- Main README: [../README.md](../README.md)
- Active skill: [../SKILL.md](../SKILL.md)
- Visual guide: [../docs/origin-chat.html](../docs/origin-chat.html)
- Revision plan template: [../templates/revision_plan.md](../templates/revision_plan.md)

## Core Rule

Every meaningful revision should move through:

```text
plan -> approval -> edit -> build -> PDF check -> redline -> commit
```
