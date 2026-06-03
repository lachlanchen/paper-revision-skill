# Revision Plan: <task_origin> — <short_action>

## 1. Task Metadata

- Plan file: `references/<file_name>.md`
- Created: <YYYY-MM-DD HH:MM>
- Task origin: <reviewer/editor/global/figure/table/response-letter>
- Revision pass: <initial/revision1/revision2/...>
- Target files: `<main.tex>`, `<response_letter.tex>`, `<supplement.tex>`, `<figs/...>`
- Build command: `<bash build_all.sh>`
- Status: <draft / approved / executed / verified / committed>

## 2. Source Comment or Motivation

Paste the reviewer/editor comment or internal revision goal here.

## 3. Problem Diagnosis

Explain the real issue in the current manuscript or response letter.

- What is unclear, missing, overstated, inconsistent, or too long?
- Why does it matter for the reviewer/editor?
- What should not be changed?

## 4. Intended Scope

### Files allowed to change

- `<file path>` — <reason>

### Locations allowed to change

- `<section/figure/table/equation/paragraph>` — <specific change>

### Explicitly forbidden changes

- Do not change <file/section/claim/style element>.
- Do not introduce new experiments, metrics, citations, or claims unless listed below.

## 5. Proposed Edits

| Step | Location | Edit | Rationale | Acceptance criterion |
|---|---|---|---|---|
| 1 | <file + section> | <specific edit> | <why> | <how to verify> |
| 2 | <file + section> | <specific edit> | <why> | <how to verify> |

## 6. Response-Letter Impact

Draft the response-letter change here, but mark location details as pending until PDF verification.

Suggested wording:

> We thank the reviewer for ... We have revised ... [verified location pending].

## 7. Verification Plan

- Compile manuscript.
- Compile response letter.
- Generate redline if possible.
- Check cross-references.
- Check bibliography.
- Inspect final PDF at the modified locations.
- Confirm response-letter location references.

## 8. Execution Notes

Record actual implementation details here after editing.

- Files changed:
- Deviations from plan:
- Build results:
- PDF locations verified:
- Redline status:

## 9. Final Status

- Manuscript compiled: <yes/no>
- Response letter compiled: <yes/no>
- Redline generated: <yes/no/not applicable>
- Response letter updated: <yes/no>
- Git commit: `<hash or pending>`
- Remaining issues:
