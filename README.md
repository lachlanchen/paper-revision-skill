# Paper Revision Skill

A plan-gated workflow for revising academic papers with coding agents.

The central rule is simple:

> Plan first, edit second.

Before an agent makes a meaningful manuscript change, it should create or read a concrete markdown plan, execute only that plan, compile the paper, verify the PDF, generate redlines when possible, and commit the completed work package.

## What Is Included

- `SKILL.md`: active Codex skill.
- `references/plan-first-revision-method.md`: full explanation of the plan-gated method.
- `references/latex-revision-file-map.md`: file conventions for `main.tex`, `sm.tex`, baselines, latest files, and redlines.
- `references/response-letter-proof-workflow.md`: response-letter and proof-correction workflow.
- `references/origin-chat-plan-gated-revision.md`: cleaned origin conversation in markdown.
- `docs/origin-chat.html`: visual origin-chat tutorial.
- `templates/`: markdown templates for plans, audits, and task indexes.
- `prompts/`: prompts for planning, applying, and auditing revisions.
- `scripts/build_revision_redlines.sh`: generic helper script for compiling and generating redlines.

## Quick Start

1. Copy or install this skill where your agent can read it.
2. Keep manuscript plans in your paper repo's `references/` folder.
3. Use `templates/revision_plan.md` before each substantial edit.
4. Use `prompts/plan_prompt.md` to draft plans.
5. Use `prompts/apply_prompt.md` to execute approved plans.
6. Use `prompts/audit_prompt.md` to verify PDFs and response-letter locations.

## Visual Guide

Open `docs/origin-chat.html` in a browser to read the cleaned chat that inspired the method, with diagrams and practical tips.
