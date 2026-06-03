# Handoff: Install Paper Revision Skill

This note is for collaborators who want to install and use `paper-revision-skill` with Codex.

## What This Skill Does

`paper-revision-skill` is a plan-gated workflow for academic manuscript revision. It helps an agent revise LaTeX papers, supplements, response letters, proof corrections, and redlined versions without uncontrolled edits.

The operating rule is:

```text
Plan first. Edit second. Verify from the PDF. Commit the work package.
```

## Repository

- GitHub: <https://github.com/lachlanchen/paper-revision-skill>
- Visual guide: <https://lachlanchen.github.io/paper-revision-skill/origin-chat.html>
- Active skill file: [`SKILL.md`](SKILL.md)
- Chinese skill guide: [`i18n/SKILL.zh-Hans.md`](i18n/SKILL.zh-Hans.md)

## Install For Codex

Clone the repository:

```bash
git clone https://github.com/lachlanchen/paper-revision-skill.git
cd paper-revision-skill
```

Install it into the Codex skills folder:

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills/paper-revision-skill"
rsync -a --delete --exclude '.git' --exclude '.DS_Store' ./ "$CODEX_HOME/skills/paper-revision-skill/"
```

Restart Codex or start a new Codex session. The skill should be available as:

```text
$paper-revision-skill
```

## Quick Test

In a manuscript repository, ask Codex:

```text
Use $paper-revision-skill to create a revision plan for this reviewer comment.
Do not edit the TeX files yet.
Save the plan under references/.
```

The expected behavior is that Codex reads the skill, creates a bounded Markdown plan first, and does not immediately rewrite the manuscript.

## Update An Existing Install

Pull the newest repository version:

```bash
cd paper-revision-skill
git pull
```

Refresh the installed skill:

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
rsync -a --delete --exclude '.git' --exclude '.DS_Store' ./ "$CODEX_HOME/skills/paper-revision-skill/"
```

## For Non-Codex Users

If you are not using Codex, treat this repository as a workflow manual:

- Read [`SKILL.md`](SKILL.md) for the operating rules.
- Use [`templates/revision_plan.md`](templates/revision_plan.md) before each major edit.
- Use [`prompts/plan_prompt.md`](prompts/plan_prompt.md), [`prompts/apply_prompt.md`](prompts/apply_prompt.md), and [`prompts/audit_prompt.md`](prompts/audit_prompt.md) with your preferred AI tools.
- Keep plans and audits under `references/` in your paper repository.

## Chinese Note

如果你想把这套方法转交给中文用户，可以先让对方阅读 [`i18n/SKILL.zh-Hans.md`](i18n/SKILL.zh-Hans.md)。正式安装时仍然安装整个仓库，并使用根目录的 [`SKILL.md`](SKILL.md) 作为 Codex 的 active skill 文件。
