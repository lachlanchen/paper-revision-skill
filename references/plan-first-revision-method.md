# Plan-First Revision Method

This reference describes a workflow for using an agent to revise academic papers without losing control of scope, reasoning, and traceability.

## Contents

1. Core idea
2. Why plans are saved
3. Standard workflow
4. How to size a plan
5. Plan markdown template
6. Working with multiple agents or models
7. Commit discipline

## 1. Core Idea

Separate the work into two phases:

- Strategy phase: decide what should change, why it should change, where it should change, and how success will be verified.
- Execution phase: apply the accepted plan to files, compile, generate redlines, inspect PDFs, and commit.

The main rule is:

`plan first, edit second.`

This is especially useful for manuscripts because writing changes are easy to overextend. A plan markdown gives the user a checkpoint before the agent edits source files.

## 2. Why Plans Are Saved

Saved plans help in four ways:

- They force explicit reasoning before edits.
- They constrain the agent's editing scope.
- They document why a change was made.
- They give future agents local context about the paper's revision history and writing preferences.

The plan is not just a record. It is an instruction boundary.

## 3. Standard Workflow

Use this loop for substantial revisions:

1. Preserve the previous submission as a baseline.
2. Keep the active filenames stable, usually `main.tex` and `sm.tex`.
3. Draft a concrete plan.
4. Save the plan under `references/`.
5. Review the plan.
6. Apply the plan only after it is accepted.
7. Compile clean PDFs.
8. Generate and compile redlined PDFs.
9. Inspect the compiled PDFs.
10. Commit and push the completed revision unit.

For reviewer comments, repeat the loop for each comment or coherent group of comments.

## 4. How To Size A Plan

Use a single plan for a broad edit when:

- The target text is easy to verify.
- The edit is mechanical.
- The sections involved are tightly related.
- The user has already supplied exact wording.

Split the work into smaller plans when:

- The claim is technically sensitive.
- Figures, equations, and response text must stay synchronized.
- The agent needs to judge wording tone.
- The first plan is vague or difficult to verify.
- The edit touches many unrelated sections.

The unit of planning is the unit of responsibility: one plan should map to one meaningful editing task.

## 5. Plan Markdown Template

Use a structure like this:

```markdown
# Revision Plan: <short topic>

Date: YYYY-MM-DD

## Goal

<What this change should accomplish.>

## Scope

- Files to edit:
- Files to inspect only:
- Files not to touch:

## Current Issue

<Reviewer comment, proof query, or observed problem.>

## Proposed Edit

Before:
`<current wording if available>`

After:
`<planned wording if available>`

## Reasoning

<Why this edit is correct and what risks it avoids.>

## Verification

- Compile:
- Redline:
- PDF check:
- Search check:
```

## 6. Working With Multiple Agents Or Models

Use reasoning models for strategy and wording judgment when useful. Use Codex for concrete file operations:

- Save any external model's plan into markdown before implementation.
- Let Codex read the plan and apply it.
- If the plan is revised through discussion, update the markdown before execution.
- Do not let the execution agent broaden scope beyond the plan.

This division keeps strategic thinking and file editing from becoming tangled.

## 7. Commit Discipline

Commit after each completed revision unit:

- One reviewer comment response.
- One figure or equation correction.
- One proof-correction batch.
- One manuscript-shortening pass.
- One response-letter location update.

When unrelated worktree changes exist, commit only files related to the current task unless explicitly asked to commit all changes.
