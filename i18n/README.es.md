[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Flujo de revisión con puerta de planificación para manuscritos LaTeX, respuestas a revisores, redlines y correcciones de pruebas.

> Primero planificar. Después editar. Verificar con el PDF. Registrar el paquete de trabajo.

## Qué Hace

- Crea un plan en markdown antes de cambios importantes.
- Mantiene `main.tex` y `sm.tex` como archivos actuales editables.
- Conserva versiones base como `original_main.tex` y `original_sm.tex`.
- Genera redlines para verificación interna.
- Sincroniza la carta de respuesta con ubicaciones verificadas en el PDF.

## Empieza Aquí

- README principal: [../README.md](../README.md)
- Skill activo: [../SKILL.md](../SKILL.md)
- Guía visual: [../docs/origin-chat.html](../docs/origin-chat.html)
- Plantilla de plan: [../templates/revision_plan.md](../templates/revision_plan.md)

## Regla Central

```text
plan -> aprobación -> edición -> compilación -> revisión PDF -> redline -> commit
```
