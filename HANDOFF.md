# Handoff: Install Paper Revision Skill

This note is for collaborators who want to install and use `paper-revision-skill` with Codex, AgInTiFlow, Claude, Gemini, Copilot, or another agent tool.

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

## Install For AgInTiFlow

AgInTiFlow supports this skill through SkillMesh. The root [`SKILL.md`](SKILL.md) uses Codex-style `name:` frontmatter; current AgInTiFlow can normalize that into native SkillMesh `id:` and `label:` metadata during import.

From the AgInTiFlow repository:

```bash
cd /home/lachlan/ProjectsLFS/Agent/AgInTiFlow
node --input-type=module - <<'NODE'
import fs from "node:fs/promises";
import {
  buildSkillPackFromMarkdown,
  enableSkillMeshSkill,
  installSkillPack,
} from "./src/skillmesh.js";

const content = await fs.readFile("/home/lachlan/ProjectsLFS/paper-revision-skill/SKILL.md", "utf8");
const pack = await buildSkillPackFromMarkdown(content, { valueScore: 95 });
await installSkillPack(pack, { enabled: true });
await enableSkillMeshSkill("paper-revision-skill", true);
console.log(JSON.stringify({ ok: true, installedSkills: pack.skills.map((skill) => skill.id), packHash: pack.packHash }, null, 2));
NODE
```

Quick AgInTiFlow selection test:

```bash
cd /home/lachlan/ProjectsLFS/Agent/AgInTiFlow
node --input-type=module - <<'NODE'
import { selectSkillsForGoal } from "./src/skill-library.js";
const selected = selectSkillsForGoal(
  "Use the paper revision workflow to answer reviewer comments before editing LaTeX.",
  { limit: 8, includeBody: false }
);
console.log(selected.map((skill) => `${skill.id}:${skill.source}`).join("\n"));
if (!selected.some((skill) => skill.id === "paper-revision-skill")) {
  throw new Error("paper-revision-skill was not selected");
}
NODE
```

## Other Agent Tools

This repository includes lightweight adapter files that all point back to [`SKILL.md`](SKILL.md):

- [`AGENTS.md`](AGENTS.md) for Codex-style repository instructions.
- [`CLAUDE.md`](CLAUDE.md) for Claude Code.
- [`GEMINI.md`](GEMINI.md) for Gemini CLI-style workflows.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for GitHub Copilot repository instructions.

These files should not fork the workflow. Keep [`SKILL.md`](SKILL.md) as the source of truth.

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

## For Manual Use

If you are not using an agent with skill support, treat this repository as a workflow manual:

- Read [`SKILL.md`](SKILL.md) for the operating rules.
- Use [`templates/revision_plan.md`](templates/revision_plan.md) before each major edit.
- Use [`prompts/plan_prompt.md`](prompts/plan_prompt.md), [`prompts/apply_prompt.md`](prompts/apply_prompt.md), and [`prompts/audit_prompt.md`](prompts/audit_prompt.md) with your preferred AI tools.
- Keep plans and audits under `references/` in your paper repository.

## Chinese Note

如果你想把这套方法转交给中文用户，可以先让对方阅读 [`i18n/SKILL.zh-Hans.md`](i18n/SKILL.zh-Hans.md)。正式安装时仍然安装整个仓库，并使用根目录的 [`SKILL.md`](SKILL.md) 作为 Codex 的 active skill 文件。
