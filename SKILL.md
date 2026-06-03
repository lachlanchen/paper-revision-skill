---
name: latex-paper-revision
description: Plan-first academic manuscript revision workflow for LaTeX papers, supplements, response letters, proof corrections, redlined versions, figure and equation reference checks, reviewer-comment planning, build verification, and submission packaging. Use when Codex needs to edit, review, build, or prepare a revised paper while preserving baselines and traceable reasoning.
---

# LaTeX Paper Revision

## Core Workflow

1. Identify the revision stage: reviewer response, major revision, minor revision, proof correction, or final submission package.
2. Inspect the relevant files before editing: active `main.tex`, active `sm.tex`, baselines, response letter, PDFs, and build scripts.
3. For substantive writing changes, create or update a plan markdown under `references/` before touching TeX files. Define scope, reasoning, target files, before and after wording, and verification steps.
4. Keep active filenames stable. Treat `main.tex` and `sm.tex` as the current latest editable files; preserve previous versions as named baselines.
5. Edit only within the accepted plan. Keep technical claims supported by data, figures, tables, or user-confirmed facts.
6. Rebuild current PDFs and refresh matching redlined files after manuscript changes.
7. Verify changes from compiled PDFs, not only source TeX. Use page, column, and paragraph anchors when line numbers are unavailable.
8. Commit and push after each completed revision unit when the project workflow expects it.

## Plan Discipline

- Separate thinking from editing. First decide what should change and why; then execute that bounded plan.
- If the plan feels broad, fragile, or hard to verify, split it into smaller plans.
- Store plan markdown files by task or revision unit, not by every chat turn.
- If another model or human drafts the strategy, save that strategy into the plan markdown before execution.
- If the plan changes, update the plan before applying the edit.

## Redline Discipline

- Keep baseline files such as `original_main.tex`, `original_sm.tex`, `major_revision_main.tex`, or `major_revision_sm.tex`.
- Generate redlined files such as `redlined_main.tex`, `redlined_sm.tex`, `redlined_minor_main.tex`, and `redlined_minor_sm.tex`.
- If `latexdiff` breaks math or display environments, make a repeatable script fix instead of relying on one-time manual edits.
- Use redlines as internal verification even when the journal does not require submitting them.

## Response And Proof Rules

- For reviewer responses, answer what changed, why it addresses the concern, and where it appears.
- Use the current manuscript PDF for final locations. Use redlined files to identify changes, not as the only source of location truth.
- For proof corrections, use `Request Revisions` when any correction remains. Itemize exact location, current proof text, and corrected text.
- Avoid unsupported claims. If a calculation or experiment was not actually performed, remove or soften the statement.

## References

Read these when needed:

- `references/plan-first-revision-method.md` for the full planning method.
- `references/latex-revision-file-map.md` for main, supplement, baseline, latest, and redline file conventions.
- `references/response-letter-proof-workflow.md` for response-letter and proof-correction patterns.
