[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Plan-gated workflow для правки LaTeX-статей, ответов рецензентам, redline-версий и proof correction.

> Сначала план. Затем правка. Проверка по PDF. Commit рабочего пакета.

## Что Он Делает

- Создает markdown-план перед существенными правками.
- Сохраняет `main.tex` и `sm.tex` как текущие редактируемые файлы.
- Хранит базовые версии вроде `original_main.tex` и `original_sm.tex`.
- Генерирует redline для внутренней проверки.
- Синхронизирует response letter с проверенными местами в PDF.

## Начать Здесь

- Основной README: [../README.md](../README.md)
- Активный skill: [../SKILL.md](../SKILL.md)
- Визуальное руководство: [../docs/origin-chat.html](../docs/origin-chat.html)
- Шаблон плана: [../templates/revision_plan.md](../templates/revision_plan.md)

## Главное Правило

```text
план -> утверждение -> правка -> сборка -> проверка PDF -> redline -> commit
```
