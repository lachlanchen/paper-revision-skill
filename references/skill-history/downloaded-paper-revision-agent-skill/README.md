# Paper Revision Agent Skill Package

This package contains a plan-gated workflow for reviewer-response manuscript revision.

Files:

- `SKILL.md` — full operating skill for the agent.
- `templates/revision_plan.md` — per-task plan template.
- `templates/response_trace_audit.md` — response-letter verification template.
- `templates/revision_task_index.md` — optional index for many plan files.
- `prompts/plan_prompt.md` — prompt for a reasoning/strategy agent.
- `prompts/apply_prompt.md` — prompt for a coding/editing agent.
- `prompts/audit_prompt.md` — prompt for PDF and response-letter verification.

Recommended use:

1. Copy `SKILL.md` into the agent's skill or instruction folder.
2. Keep all task plans in the manuscript repository's `references/` directory.
3. Use `plan_prompt.md` to create a plan.
4. Review and approve the plan.
5. Use `apply_prompt.md` to execute it.
6. Use `audit_prompt.md` after compilation to update the response letter.

## Origin chat and visual tutorial

This repository includes a cleaned, translated, and visually formatted origin chat that explains the idea behind the workflow:

- `docs/origin-chat.html` — readable chat source, diagrams, tables, and practical tips.

The page is designed for GitHub Pages or direct browser viewing. It is not a raw transcript; unrelated discussion has been removed and the technical ideas have been lightly elaborated for clarity.
