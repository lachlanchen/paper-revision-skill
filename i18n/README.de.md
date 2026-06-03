[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Plan-gesteuerter Workflow für LaTeX-Manuskripte, Reviewer-Antworten, Redlines und Korrekturfahnen.

> Erst planen. Dann editieren. Im PDF prüfen. Das Arbeitspaket committen.

## Was Es Leistet

- Erstellt vor größeren Änderungen einen Markdown-Plan.
- Hält `main.tex` und `sm.tex` als aktuelle editierbare Dateien stabil.
- Bewahrt Baselines wie `original_main.tex` und `original_sm.tex`.
- Erzeugt Redlines zur internen Kontrolle.
- Synchronisiert Antwortschreiben mit geprüften PDF-Positionen.

## Einstieg

- Haupt-README: [../README.md](../README.md)
- Aktiver Skill: [../SKILL.md](../SKILL.md)
- Visuelle Anleitung: [../docs/origin-chat.html](../docs/origin-chat.html)
- Planvorlage: [../templates/revision_plan.md](../templates/revision_plan.md)

## Kernregel

```text
Plan -> Freigabe -> Editieren -> Build -> PDF-Prüfung -> Redline -> Commit
```
