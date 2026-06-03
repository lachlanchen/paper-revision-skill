# Agent Instructions

This repository defines the `paper-revision-skill` workflow. Treat [`SKILL.md`](SKILL.md) as the single source of truth.

Use this workflow when revising academic manuscripts, LaTeX papers, supplements, response letters, proof corrections, redlines, or submission packages.

Compatibility target:

- AgInTiFlow SkillMesh: highlighted integration, tool at <https://flow.lazying.art>, repo at <https://github.com/lazyingart/AgInTiFlow>.
- Codex: active skill through `SKILL.md`.
- Claude Code: `CLAUDE.md`.
- Gemini CLI: `GEMINI.md`.
- GitHub Copilot: `.github/copilot-instructions.md`.

Operating rule:

```text
Plan first. Edit second. Verify from the PDF. Commit the work package.
```

Required behavior:

- Read `SKILL.md` before doing manuscript revision work.
- Create or update a bounded plan under `references/` before substantive TeX edits.
- Preserve stable active filenames such as `main.tex` and `sm.tex`; do not silently overwrite baselines.
- Edit only inside the accepted plan scope.
- Build PDFs and redlines when the project has the required toolchain or scripts.
- Verify final response-letter or proof locations from the compiled PDF, not only from TeX source.
- Record unresolved items explicitly instead of inventing verification details.

Helpful files:

- `templates/revision_plan.md`
- `templates/response_trace_audit.md`
- `templates/revision_task_index.md`
- `prompts/plan_prompt.md`
- `prompts/apply_prompt.md`
- `prompts/audit_prompt.md`
- `scripts/build_all_revision_artifacts.sh`
- `scripts/build_revision_redlines.sh`
- `scripts/pdf_location_audit.py`

Boundary:

- Do not add project-specific manuscript facts to this skill repository.
- Keep this repository adapter-neutral; tool-specific files should only point back to `SKILL.md`.
