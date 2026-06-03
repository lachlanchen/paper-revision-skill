[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

LaTeX 논문, 리뷰어 응답, redline, proof correction을 위한 plan-gated 원고 수정 워크플로입니다.

> 먼저 계획하고, 그다음 편집합니다. PDF로 확인하고 작업 단위를 commit합니다.

## 하는 일

- 중요한 원고 수정 전에 markdown 계획을 만듭니다.
- `main.tex`와 `sm.tex`를 최신 편집 파일로 유지합니다.
- `original_main.tex`와 `original_sm.tex` 같은 기준 파일을 보존합니다.
- 내부 검증을 위한 redline을 생성합니다.
- response letter를 PDF에서 확인한 위치와 동기화합니다.

## 시작하기

- 메인 README: [../README.md](../README.md)
- 활성 Skill: [../SKILL.md](../SKILL.md)
- 시각 가이드: [../docs/origin-chat.html](../docs/origin-chat.html)
- 수정 계획 템플릿: [../templates/revision_plan.md](../templates/revision_plan.md)

## 핵심 규칙

```text
계획 -> 승인 -> 편집 -> 빌드 -> PDF 확인 -> redline -> commit
```
