# Claude Instructions

Use [`SKILL.md`](SKILL.md) as the authoritative workflow for manuscript revision tasks in this repository.

When a user asks for paper revision, reviewer-response drafting, proof correction, redline generation, LaTeX manuscript cleanup, or submission-package preparation:

- Start by mapping the current manuscript files, baselines, PDFs, response letter, and build scripts.
- Create or update a plan markdown file under `references/` before substantive edits.
- Do not edit outside the plan scope.
- Do not invent paper locations, line numbers, experiment results, or reviewer-response claims.
- Build and inspect the compiled PDF when possible before claiming completion.
- Use redlines and PDF-backed audits as verification artifacts.

If the task is too broad, split it into smaller revision plans instead of making a sweeping edit.

The core rule is:

```text
Plan first. Edit second. Verify from the PDF. Commit the work package.
```
