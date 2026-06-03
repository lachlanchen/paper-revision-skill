[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Flux de révision avec plan préalable pour articles LaTeX, réponses aux reviewers, redlines et corrections d'épreuves.

> Planifier d'abord. Éditer ensuite. Vérifier dans le PDF. Commiter le paquet de travail.

## Ce Que Fait L'outil

- Crée un plan markdown avant les modifications importantes.
- Garde `main.tex` et `sm.tex` comme fichiers actifs.
- Préserve les versions de base comme `original_main.tex` et `original_sm.tex`.
- Génère des redlines pour la vérification.
- Aligne la response letter avec les emplacements vérifiés dans le PDF.

## Commencer

- README principal : [../README.md](../README.md)
- Skill actif : [../SKILL.md](../SKILL.md)
- Guide visuel : [../docs/origin-chat.html](../docs/origin-chat.html)
- Modèle de plan : [../templates/revision_plan.md](../templates/revision_plan.md)

## Règle Centrale

```text
plan -> approbation -> édition -> compilation -> vérification PDF -> redline -> commit
```
