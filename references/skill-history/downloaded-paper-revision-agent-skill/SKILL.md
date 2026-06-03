---
name: plan-gated-paper-revision
description: Use this skill when revising an academic manuscript, supplementary material, figures, captions, or response letter under reviewer/editor comments. The skill enforces a plan-first, scope-controlled, traceable revision workflow with Markdown plans, PDF/redline verification, and response-letter updates.
---

# Plan-Gated Paper Revision Skill

## Core Principle

Treat every manuscript revision as a controlled experiment:

1. **Think before editing.** Create or update a concrete Markdown plan before touching manuscript files.
2. **The plan is the contract.** Only edit what the accepted plan authorizes.
3. **One plan, one executable work package.** A work package may be small, such as one reviewer comment, or global, such as manuscript shortening. Its size is dynamic, but plan and execution must remain paired.
4. **Separate strategy from execution.** Use stronger reasoning models or human input to design the plan; use the coding/editing agent to apply it precisely.
5. **Keep all reasoning externalized.** Store plans in `references/` so future agents can recover intent, style preferences, constraints, and prior decisions.
6. **Verify from artifacts, not memory.** Compile PDFs, inspect outputs, generate redlines, and update the response letter only with verified page/section/figure locations.
7. **Commit after accepted steps.** Each accepted work package should end with a clean commit, and push when remote access exists.

## Required Repository Convention

Use this structure when possible:

```text
project-root/
  original_main.tex              # frozen pre-revision manuscript, when available
  main.tex                       # current editable manuscript
  response_letter.tex            # editable response letter, when available
  redlined_main.tex              # generated redline, not necessarily submitted
  build_all.sh                   # compiles manuscript, response letter, redline, supplement
  references/                    # revision plans, audits, rationales, decisions
  figs/                          # figures
  ResponseMaterial/              # optional reviewer-response materials
  Manuscript/                    # optional manuscript build directory
  ResponseLetter/                # optional response-letter build directory
```

Never silently overwrite `original_main.tex`. If it is absent, ask whether a pre-revision source exists or record that redline generation will be limited.

## Naming Convention for Plans

Use file names that encode reviewer/comment/task, revision pass, and topic:

```text
references/reviewer1_comment1_revision2_tone_softening.md
references/reviewer2_comment6_reanalysis_plan.md
references/figure4_caption_shorten_plan.md
references/main_text_shorten_plan.md
references/response_letter_ref_numbers.md
references/references_rebalance_plan_v2.md
```

Rules:

- Use lowercase snake_case.
- Start with the task origin: `reviewer1_comment3`, `editor_comment`, `figure4`, `main_text`, `response_letter`, `supplement`, or `global`.
- Add `revisionN` when revisiting a previously executed task.
- Add a short action phrase: `shorten`, `tone_softening`, `caption_rephrase`, `metric_fix`, `citation_move`, `table_reposition`.
- Keep one plan per executable work package. Avoid merging unrelated changes into a single plan unless the user explicitly approves a global pass.

## Work Package Granularity

A work package is the unit handed to the editing agent. It can be:

- one reviewer comment;
- one figure/caption/table revision;
- one response-letter section;
- one global pass, such as shortening, tone harmonization, reference rebalancing, or notation audit.

Before execution, judge whether the current plan is too broad. Split it when any of the following is true:

- the plan touches more than three manuscript regions without a unifying reason;
- the task mixes scientific logic, formatting, and stylistic rewriting;
- acceptance criteria are vague;
- the agent would need to infer unstated decisions;
- the risk of unintended edits is high.

## Standard Workflow

### Phase 0 — Freeze and Map

1. Confirm the active files: manuscript, supplement, response letter, figures, bibliography, build scripts.
2. Confirm whether `original_main.tex` exists.
3. Run a baseline build when possible.
4. Record the current state in `references/handover_state.md` or a task-specific plan.

### Phase 1 — Draft Response Strategy

For each reviewer/editor comment:

1. Write a direct response draft first.
2. Identify what manuscript change is required to make the response true.
3. Separate response wording from manuscript edits.
4. Do not promise changes that have not been made or verified.

### Phase 2 — Create the Plan

Before editing files, create a Markdown plan under `references/` with:

- problem statement;
- reviewer/editor comment being addressed;
- exact intended manuscript locations;
- proposed edits;
- forbidden edits;
- rationale;
- acceptance criteria;
- build and verification steps;
- response-letter impact.

The plan must be specific enough that another agent could execute it without guessing.

### Phase 3 — Human or Strategist Review

The user or a stronger reasoning agent reviews the plan.

- If the plan is wrong, revise the plan first.
- If the plan is too broad, split it.
- If the plan contains speculation, remove or mark it.
- Execution begins only after the plan is accepted or explicitly authorized.

### Phase 4 — Apply the Plan

Modify only files and locations listed in the plan.

During execution:

- keep edits minimal and local;
- preserve author voice unless the plan authorizes rewriting;
- do not introduce new claims, citations, metrics, or figure references without plan support;
- do not reformat unrelated paragraphs;
- update cross-references and labels only when necessary;
- record deviations in the plan under `Execution Notes`.

### Phase 5 — Build and Verify

After edits:

1. Compile the manuscript.
2. Compile the response letter.
3. Generate or update `redlined_main.tex` when original and current sources are available.
4. Inspect PDFs, logs, references, figures, tables, and cross-references.
5. Fix build errors only within the task scope unless the user authorizes a broader cleanup.

### Phase 6 — Trace Changes into the Response Letter

Update the response letter after PDF verification.

For every claim such as “we have revised…”, include verified location information when appropriate:

- section name;
- page number;
- paragraph number;
- figure/table/equation number;
- line number if available from the compiled manuscript or source mapping;
- concise description of the actual change.

Never invent page, paragraph, line, or figure locations. If exact locations cannot be verified, say so and use section/figure identifiers only.

### Phase 7 — Commit and Push

At the end of each accepted work package:

```bash
git status
git diff --stat
git diff -- main.tex response_letter.tex
bash build_all.sh
git add main.tex response_letter.tex redlined_main.tex references/<plan_file>.md
git commit -m "Revise <task-origin>: <short action>"
git push
```

If `git push` is unavailable, commit locally and record the limitation.

## Plan Quality Checklist

A plan is executable only if all answers are clear:

- What exact problem does this revision solve?
- Which reviewer/editor comment or internal goal does it address?
- Which files may be modified?
- Which sections, figures, tables, equations, or paragraphs may be changed?
- What is explicitly out of scope?
- What scientific claim is being added, removed, softened, or clarified?
- How will success be verified?
- How will the response letter be updated?
- What build command must pass?

If any item is missing, improve the plan before editing.

## Response-Letter Rules

The response letter must be faithful to the manuscript.

- First draft the reply in natural, respectful language.
- Keep tone calm, specific, and non-defensive.
- Acknowledge reviewer concerns before describing changes.
- Use “We have revised…” only after the manuscript has actually been revised.
- Prefer concrete evidence over broad reassurance.
- Avoid overclaiming novelty, performance, generality, or clinical readiness.
- Ensure every location reference matches the final compiled PDF.

## Redline Rules

When `original_main.tex` and `main.tex` exist, generate a redline source and PDF using a stable method, for example:

```bash
latexdiff original_main.tex main.tex > redlined_main.tex
latexmk -pdf redlined_main.tex
```

For multi-file LaTeX projects, use a flattening step before `latexdiff` when needed. Record the exact method in the plan or audit notes.

## Failure Modes and Corrections

### Failure Mode: The agent starts rewriting broadly

Correction: Stop, restore unrelated edits, narrow the plan, and execute only listed locations.

### Failure Mode: The plan is vague

Correction: Convert goals such as “improve clarity” into concrete edits, such as “replace the final sentence of the Figure 4 caption with a sentence that states the metric and validation cohort.”

### Failure Mode: The response letter claims more than the paper supports

Correction: Revise the response first, then revise the manuscript or soften the claim.

### Failure Mode: The manuscript compiles but the PDF location is unverified

Correction: Inspect the PDF or logs before adding page/line references.

### Failure Mode: A task becomes larger during execution

Correction: Stop execution, append an `Out-of-Scope Discovery` section to the plan, and create a new plan for the new task.

## Agent Operating Contract

When using this skill, the agent must follow this contract:

1. Do not edit manuscript files before creating or reading the relevant plan.
2. Do not exceed the plan scope.
3. Do not merge unrelated reviewer comments without permission.
4. Do not invent verification details.
5. Do not leave build status unknown.
6. Do not hide uncertainty; record unresolved items explicitly.
7. Always keep `references/` useful for the next agent.

## Minimal Agent Loop

```text
read context -> create/update plan -> request/receive approval -> apply plan -> build -> verify PDF -> update response letter -> generate redline -> commit/push -> record notes
```

This loop is intentionally linear. Linearity prevents uncontrolled coupling between scientific reasoning, manuscript editing, response writing, and build repair.
