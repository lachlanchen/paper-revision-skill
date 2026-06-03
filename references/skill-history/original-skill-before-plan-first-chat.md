# Original Skill Snapshot Before Plan-First Chat Method

This snapshot preserves the compact paper-revision skill created before the later chat history clarified the plan-first markdown method.

```markdown
---
name: paper-writing-revision
description: Academic paper writing and revision workflow for LaTeX manuscripts, response letters, cover letters, reviewer comments, proof corrections, redlined versions, figure references, supplementary material, funding and acknowledgement updates, and final submission packages. Use when Codex needs to edit, verify, build, redline, or respond to journal review or proof-stage requests for a manuscript.
---

# Paper Writing Revision

## Core Workflow

1. Determine the stage: initial drafting, major revision, minor revision, proof correction, or final submission packaging.
2. Inspect the relevant TeX, PDF, response-letter, and reference files before editing. Use `rg`, `pdftotext -layout`, and existing build scripts before making assumptions.
3. Keep edits narrow. Preserve the paper's technical claims and only add statements supported by manuscript text, data, tables, or user-confirmed facts.
4. For any manuscript edit, rebuild the relevant PDF and refresh the matching redlined version when the repo has a redline baseline.
5. For response letters and proof corrections, give precise locations using the current manuscript or proof PDF. Prefer page, column or paragraph-beginning text over fragile line numbers when the journal template does not expose lines.
6. Run `git status --short` before committing. Commit and push after edits when the project convention or user asks for it.

## Revision Letter Rules

- Distinguish figure namespaces clearly: main manuscript uses `Fig.`, supplementary material uses `Fig. S`, and response-letter-only figures should be named as response figures if needed.
- Blend location information into response text instead of adding cluttered `Location:` blocks unless the journal explicitly requests a table.
- Avoid false or over-specific claims. If a calculation, calibration, or data-processing step was not performed, rephrase as a conservative estimate or remove it.
- Quote reviewer comments accurately, then answer with what changed, why it addresses the issue, and where it appears.
- Use current manuscript locations as primary. Use the previous submission or redlined version only to identify changed material or resolve ambiguous locations.

## Build And Redline Rules

- Prefer existing project scripts such as `build_all.sh`, `build_redlined_minor.sh`, and specialized latexdiff fix scripts before inventing new build steps.
- If `latexdiff` mangles an equation or display environment, create a repeatable script fix rather than relying on one-off manual edits.
- Compile both clean and redlined PDFs after changes that affect submission files.
- Treat locale warnings from `latexdiff` as nonfatal unless the output is broken.

## Proof Correction Rules

- Use `Request Revisions` when the proof has corrections such as missing figure citations, funding changes, or acknowledgement edits. Use `Accept Proofs` only when no corrections remain.
- Write proof corrections as itemized edits with exact proof PDF location, current proof text, and corrected text.
- For funding, use the full funder name requested by production when available, and include grant numbers exactly.
- For acknowledgement changes at proof stage, phrase as an author-requested correction because production may decide whether to accept content changes.

## References

For project-specific procedures, examples, wording patterns, and command notes, read the detailed revision reference.
```
