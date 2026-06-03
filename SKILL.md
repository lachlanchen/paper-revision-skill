---
name: paper-revision-skill
description: Plan-gated academic manuscript revision workflow for LaTeX papers, supplements, response letters, proof corrections, redlined versions, figure and equation reference checks, reviewer-comment planning, build verification, and submission packaging. Use when Codex needs to edit, review, build, audit, or prepare a revised paper while preserving baselines, scope control, and traceable reasoning.
---

# Paper Revision Skill

## Core Workflow

1. Identify the revision stage: reviewer response, major revision, minor revision, proof correction, or final submission package.
2. Inspect the relevant files before editing: active `main.tex`, active `sm.tex`, baselines, response letter, PDFs, and build scripts.
3. For substantive writing changes, create or update a plan markdown under `references/` before touching TeX files. Define scope, reasoning, target files, before and after wording, and verification steps.
4. Keep active filenames stable. Treat `main.tex` and `sm.tex` as the current latest editable files; preserve previous versions as named baselines.
5. Edit only within the accepted plan. Keep technical claims supported by data, figures, tables, or user-confirmed facts.
6. Rebuild current PDFs and refresh matching redlined files after manuscript changes.
7. Verify changes from compiled PDFs, not only source TeX. Use page, column, and paragraph anchors when line numbers are unavailable.
8. Commit and push after each completed revision unit when the project workflow expects it.

## Required Repository Convention

- Keep active manuscript filenames stable, usually `main.tex` and `sm.tex`.
- Preserve baselines such as `original_main.tex`, `original_sm.tex`, `major_revision_main.tex`, and `major_revision_sm.tex`.
- Generate redlines such as `redlined_main.tex`, `redlined_sm.tex`, `redlined_minor_main.tex`, and `redlined_minor_sm.tex`.
- Store task plans, audits, and rationale under `references/`.
- Never silently overwrite a baseline. If no baseline exists, record that redline generation is limited.

## Plan Discipline

- Separate thinking from editing. First decide what should change and why; then execute that bounded plan.
- If the plan feels broad, fragile, or hard to verify, split it into smaller plans.
- Store plan markdown files by task or revision unit, not by every chat turn.
- If another model or human drafts the strategy, save that strategy into the plan markdown before execution.
- If the plan changes, update the plan before applying the edit.

## Plan Naming And Scope

- Use lowercase snake_case names such as `references/reviewer1_comment1_revision2_tone_softening.md`.
- Start with the origin when possible: `reviewer1_comment3`, `editor_comment`, `figure4`, `main_text`, `response_letter`, `supplement`, `proof`, or `global`.
- Add `revisionN` when revisiting a previously executed task.
- Keep one plan per executable work package unless the user explicitly approves a global pass.
- Split the plan when it mixes scientific logic, formatting, figure work, response writing, and build repair without a single unifying purpose.

## Execution Phases

1. Freeze and map active files, baselines, figures, bibliography, and build scripts.
2. Draft response strategy before manuscript edits when reviewer comments are involved.
3. Create or update the markdown plan with allowed files, allowed locations, forbidden edits, rationale, acceptance criteria, build steps, and response-letter impact.
4. Apply only the approved plan.
5. Build the manuscript, supplement, response letter, cover letter, and redlines as applicable. Prefer the project build script first. If none exists, use `scripts/build_all_revision_artifacts.sh` or `scripts/build_revision_redlines.sh`.
6. Verify locations from the final PDF before updating response-letter or proof-correction text.
7. Record deviations, unresolved issues, and build status in the plan or audit note.

## Redline Discipline

- Keep baseline files such as `original_main.tex`, `original_sm.tex`, `major_revision_main.tex`, or `major_revision_sm.tex`.
- Generate redlined files such as `redlined_main.tex`, `redlined_sm.tex`, `redlined_minor_main.tex`, and `redlined_minor_sm.tex`.
- If `latexdiff` breaks math or display environments, make a repeatable script fix instead of relying on one-time manual edits.
- Use redlines as internal verification even when the journal does not require submitting them.

## Response And Proof Rules

- For reviewer responses, answer what changed, why it addresses the concern, and where it appears.
- Use the current manuscript PDF for final locations. Use redlined files to identify changes, not as the only source of location truth.
- To locate edits, search the compiled PDF with `pdftotext -layout` or `scripts/pdf_location_audit.py`. Treat extracted line numbers as search aids, not journal line numbers. Final wording should use page, section, figure/table/equation, column when visually confirmed, and paragraph-beginning anchors.
- For proof corrections, use `Request Revisions` when any correction remains. Itemize exact location, current proof text, and corrected text.
- Avoid unsupported claims. If a calculation or experiment was not actually performed, remove or soften the statement.

## Plan Quality Checklist

Before editing, confirm the plan answers:

- What exact problem does this solve?
- Which reviewer, editor, proof query, or internal goal does it address?
- Which files and locations may be modified?
- What is explicitly out of scope?
- What claim is being added, removed, softened, or clarified?
- How will the result be verified from PDFs, redlines, logs, or searches?
- How will the response letter or proof note be updated?

## Failure Handling

- If the task becomes larger during execution, stop and create a new plan instead of silently expanding scope.
- If the response letter overclaims, soften the response or revise the manuscript under a new approved plan.
- If the build fails, fix only build errors caused by the current plan unless the user authorizes broader cleanup.
- If PDF locations cannot be verified, do not invent page, line, paragraph, figure, table, or equation references.
- If an out-of-scope issue is discovered, record it as an `Out-of-Scope Discovery` instead of fixing it silently.

## Agent Operating Contract

- Do not edit manuscript files before creating or reading the relevant plan.
- Do not exceed the plan scope.
- Do not merge unrelated reviewer comments without permission.
- Do not invent verification details.
- Do not leave build status unknown.
- Do not hide uncertainty; record unresolved items explicitly.
- Keep `references/` useful for the next agent.

## References

Read these when needed:

- `references/plan-first-revision-method.md` for the full planning method.
- `references/latex-revision-file-map.md` for main, supplement, baseline, latest, and redline file conventions.
- `references/response-letter-proof-workflow.md` for response-letter and proof-correction patterns.
- `references/origin-chat-plan-gated-revision.md` for the cleaned origin conversation and teaching guide.
- `templates/revision_plan.md` for the standard pre-edit plan template.
- `templates/response_trace_audit.md` for response-letter verification.
- `prompts/plan_prompt.md`, `prompts/apply_prompt.md`, and `prompts/audit_prompt.md` for strategist, executor, and auditor workflows.
- `scripts/build_all_revision_artifacts.sh` for compiling common manuscript, supplement, response, cover, and redline artifacts.
- `scripts/pdf_location_audit.py` for finding conservative PDF-backed location anchors.
