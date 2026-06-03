[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Paper Revision Skill

**Plan-gated manuscript revision for LaTeX papers, reviewer responses, redlines, and proof corrections.**

[![Website](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![GitHub](https://img.shields.io/badge/GitHub-lachlanchen-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lachlanchen)
[![Skill](https://img.shields.io/badge/Codex-Skill-2563eb?style=for-the-badge&logo=openai&logoColor=white)](SKILL.md)
[![Origin Guide](https://img.shields.io/badge/Guide-Origin%20Chat-16a34a?style=for-the-badge&logo=readthedocs&logoColor=white)](https://lachlanchen.github.io/paper-revision-skill/origin-chat.html)

Paper Revision Skill turns manuscript revision into a controlled agent workflow:

> **Plan first. Edit second. Verify from the PDF. Commit the work package.**

It is designed for academic papers where uncontrolled agent edits are expensive: major revisions, response letters, Supplementary Material, figure and equation references, `latexdiff` redlines, proof corrections, and final submission packages.

## Why This Exists

AI agents are strong at file editing, builds, search, and bookkeeping. They are less reliable when they must simultaneously decide the scientific strategy, rewrite text, update response letters, compile LaTeX, and infer what should not be touched.

This skill separates the workflow:

| Phase | Purpose | Artifact |
| --- | --- | --- |
| Think | Diagnose reviewer or editor intent | `references/<task>_plan.md` |
| Gate | Human reviews scope and reasoning | approved plan |
| Execute | Codex edits only within the plan | `main.tex`, `sm.tex`, response letter |
| Verify | Build, inspect PDF, generate redline | PDFs and `redlined_*.tex` |
| Record | Commit the completed work package | git commit |

## Workflow

```text
Reviewer comment or proof query
              |
              v
       Draft response logic
              |
              v
  Save a markdown revision plan
              |
              v
       Human checks scope
              |
       +------+------+
       |             |
       v             v
   Plan OK       Split/refine
       |
       v
  Codex applies only the plan
       |
       v
 Build clean PDF and redline
       |
       v
 Inspect current PDF locations
       |
       v
 Update response or proof note
       |
       v
 Commit and push
```

## Quick Start

Use the active skill:

```text
Use $latex-paper-revision to revise this paper.
First create a plan in references/.
Do not edit outside the plan.
Build the manuscript and redline after execution.
```

For a manuscript repository, keep this convention when possible:

```text
paper-project/
  Manuscript/
    main.tex                 # current latest main manuscript
    sm.tex                   # current latest Supplementary Material
    original_main.tex        # frozen previous baseline
    original_sm.tex          # frozen previous supplement baseline
    redlined_main.tex        # generated diff
    redlined_sm.tex          # generated diff
  ResponseLetter/
    response_letter.tex
  references/
    reviewer1_comment1_plan.md
  build_all.sh
```

## What Is Included

| Path | Use |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Active Codex skill instructions |
| [`references/plan-first-revision-method.md`](references/plan-first-revision-method.md) | Full method for plan-gated revision |
| [`references/latex-revision-file-map.md`](references/latex-revision-file-map.md) | File conventions for latest, original, and redlined versions |
| [`references/response-letter-proof-workflow.md`](references/response-letter-proof-workflow.md) | Response-letter and proof-correction patterns |
| [`references/origin-chat-plan-gated-revision.md`](references/origin-chat-plan-gated-revision.md) | Cleaned origin conversation and teaching guide |
| [`docs/origin-chat.html`](docs/origin-chat.html) | Visual chat guide with diagrams and practical tips |
| [`templates/revision_plan.md`](templates/revision_plan.md) | Plan template before each substantial edit |
| [`templates/response_trace_audit.md`](templates/response_trace_audit.md) | Response-letter verification template |
| [`templates/revision_task_index.md`](templates/revision_task_index.md) | Index for many plans |
| [`prompts/plan_prompt.md`](prompts/plan_prompt.md) | Prompt for a strategist or reasoning agent |
| [`prompts/apply_prompt.md`](prompts/apply_prompt.md) | Prompt for an execution agent |
| [`prompts/audit_prompt.md`](prompts/audit_prompt.md) | Prompt for a PDF and response-letter auditor |
| [`scripts/build_revision_redlines.sh`](scripts/build_revision_redlines.sh) | Generic LaTeX build and redline helper |

## Three Agent Roles

| Role | Does | Avoids |
| --- | --- | --- |
| Strategist | diagnoses comments, drafts response logic, writes the plan | direct TeX editing |
| Executor | applies approved plan, builds PDFs, generates redlines | changing scope or inventing claims |
| Auditor | checks PDFs, locations, references, and response fidelity | adding new manuscript content |

## Standard Codex Instruction

```text
You are working on an academic manuscript revision.

First read the relevant plan in references/.
Do not edit anything outside the plan.
If the plan is too broad or vague, stop and propose a smaller plan.
Apply only the approved edits.
After editing, update the plan's Execution Notes.
Run the build command.
Inspect the generated PDF if available.
Update the response letter only with verified changes.
Generate the redlined version when a baseline is available.
Show git diff summary.
Commit and push this work package.
```

## Build Helper

The helper script compiles current files, generates redlines, and compiles the redlined TeX:

```bash
./scripts/build_revision_redlines.sh Manuscript
```

Override names when needed:

```bash
MAIN_BASELINE=major_revision_main.tex \
SM_BASELINE=major_revision_sm.tex \
REDLINED_MAIN=redlined_minor_main.tex \
REDLINED_SM=redlined_minor_sm.tex \
./scripts/build_revision_redlines.sh Manuscript
```

## Visual Origin Guide

Open the HTML guide locally or through GitHub Pages:

- [Live guide on GitHub Pages](https://lachlanchen.github.io/paper-revision-skill/origin-chat.html)
- [`docs/origin-chat.html`](docs/origin-chat.html)
- [`references/origin-chat-plan-gated-revision.md`](references/origin-chat-plan-gated-revision.md)

GitHub README files cannot safely embed local HTML or iframes, so the visual chat is published as a separate GitHub Pages page and linked from this README.

The guide explains the original conversation behind the method, with the unrelated parts removed and the practical workflow expanded.

## Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

[![Website](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Email](https://img.shields.io/badge/Email-lach@lazying.art-0ea5e9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lach@lazying.art)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-lachlanchen-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/lachlanchen)

Build less. Revise cleaner.
