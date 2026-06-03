# Origin Chat: Plan-Gated Linear Revision

This document is a cleaned, translated, and expanded version of the chat that inspired this skill. It removes unrelated banter and keeps the practical method: use plans as gates, keep edits linear, verify with PDFs and redlines, and commit each work package.

## Contents

1. The short version
2. The cleaned chat
3. What the chat really means
4. Workflow diagram
5. Roles and responsibilities
6. Plan size guide
7. Practical tips
8. Standard instruction for Codex

## 1. The Short Version

The method can be summarized as:

> Do not let an agent decide what to change while it is editing the paper. First force the revision idea into a markdown plan, then let the agent execute only that plan.

This turns paper revision from a messy free-writing process into a controlled engineering workflow.

## 2. The Cleaned Chat

The conversation below is rewritten in English and lightly elaborated for readability. The speakers are kept as:

- **Chen**: the person explaining the workflow.
- **Robbie**: the person learning the workflow.

### Scene 1: Start With A Baseline

**Chen:** I have a workflow for paper revisions. Locally, keep the previous submitted file as `original_main.tex`. Keep the editable file name unchanged as `main.tex`.

**Chen:** Let Codex automatically generate `redlined_main.tex`. Even if you do not submit the redline, generating it is useful because it shows what changed.

**Robbie:** So the old version stays fixed, and the current version is always `main.tex`?

**Chen:** Exactly. The original file is the anchor. The latest working file keeps the same name. The redline is generated from the two.

### Scene 2: Response First, Plan Second, Edit Third

**Chen:** First, use AI to draft responses to all reviewer comments. Then inspect the responses one by one.

**Chen:** For each comment, first revise the response logic. Then ask the AI to create a manuscript revision plan. Save that plan as markdown. Check the plan. Only then execute it.

**Robbie:** So the response letter and the manuscript are linked through the plan?

**Chen:** Yes. The response says what you claim to have fixed. The plan defines how the paper will actually be changed to support that response.

### Scene 3: Automate The Boring Parts

**Chen:** Write a script that compiles the latest response letter, latest manuscript, and redlined version.

**Chen:** After all changes are done, let Codex read the PDF and update the response letter with accurate locations: which page, which paragraph, which figure, which equation.

**Robbie:** Why read the PDF instead of using the TeX lines?

**Chen:** Because journals often do not provide line numbers, and redlined pages may not match final pages. The current PDF is the truth.

### Scene 4: The Markdown Plan Is A Gate

**Chen:** You must generate a revision plan. It can be created by ChatGPT, another reasoning model, or Codex itself. But it must be saved to markdown before execution.

**Robbie:** Is the markdown what I want it to do, or what it did afterward?

**Chen:** For paper revision, definitely before editing. The plan shows the reasoning. Otherwise, later you only see the result and cannot remember why the change was made.

**Chen:** The markdown also helps Codex understand your preferences and the context of the paper. It becomes external memory.

### Scene 5: Split Thinking From Editing

**Chen:** This is divide and conquer. Separate the thinking task from the editing task. That lowers the difficulty of each step and improves quality.

**Robbie:** So ChatGPT can help decide how to revise, and Codex performs the file edits?

**Chen:** Right. Knowledge and strategy from ChatGPT. Technical execution from Codex.

### Scene 6: One Work Package, One Plan

**Robbie:** Should one issue have one markdown file that keeps growing, or should every revision attempt have a new markdown?

**Chen:** Usually multiple markdown files. Each meaningful execution package gets one plan.

**Chen:** A package can be small, like one reviewer comment, or broad, like shortening several paragraphs. The size is dynamic.

**Robbie:** If there are many markdown files, how do you know the order?

**Chen:** Time is the order. Filename timestamps or revision numbers help. You usually do not reread everything, but the agent can.

### Scene 7: The Plan Must Be Concrete

**Chen:** Every step should be concrete and measurable, not vague.

**Chen:** A plan should say which file can be changed, which section can be changed, what must not be changed, and how to verify success.

**Robbie:** So the plan is not just "make it better."

**Chen:** Exactly. "Make it better" is how agents start wandering.

### Scene 8: If The Plan Is Too Hard, Split It

**Chen:** If you give the agent a big comment and the plan feels difficult, split it into smaller tasks.

**Chen:** For example, "shorten the paper" might become three separate plans: shorten the introduction, tighten a figure discussion, and compress the conclusion.

**Robbie:** So a plan's size depends on whether the agent can handle it reliably.

**Chen:** Yes. You can feel it from the plan. If the plan is clear, execute it. If not, split it.

### Scene 9: Small Tuning Does Not Need A New Plan

**Robbie:** What if the plan was executed but I am not fully satisfied and need small adjustments?

**Chen:** Small tuning does not matter. You do not need to record every tiny chat turn.

**Chen:** What matters is that the final executable plan is the one you approve. If the plan is wrong, update the plan first. Then execute.

### Scene 10: Why This Works

**Chen:** When the agent is weak at a task, direct editing becomes uncontrolled. It starts changing too much, then the work gets messy.

**Chen:** With a plan, the agent becomes much more controlled. The core is scope control.

**Robbie:** So the plan reduces the thinking burden while editing.

**Chen:** Yes. Otherwise the agent must decide what to change and also modify files at the same time.

## 3. What The Chat Really Means

The chat describes a practical agent-control pattern:

| Problem | Plan-gated solution |
|---|---|
| Agent edits too broadly | Require a scoped markdown plan before editing |
| Response letter does not match manuscript | Update response locations only after PDF verification |
| Revision history becomes hard to understand | Store the reason for each meaningful edit in `references/` |
| Redline is forgotten or stale | Generate redline automatically from baseline and current files |
| One task becomes too large | Split into smaller execution packages |
| AI loses context in new sessions | Let future agents read plan markdowns as external memory |

The key principle:

> The plan is not bureaucracy. The plan is the boundary of agent behavior.

## 4. Workflow Diagram

```text
Reviewer comment or internal goal
              |
              v
      Draft response logic
              |
              v
   Create markdown revision plan
              |
              v
        Human checks plan
              |
       +------+------+
       |             |
       v             v
   Plan OK       Plan too broad
       |             |
       v             v
 Execute plan   Split/refine plan
       |
       v
 Compile manuscript and supplement
       |
       v
 Generate redline
       |
       v
 Inspect PDF
       |
       v
 Update response letter locations
       |
       v
 Commit and push
```

## 5. Roles And Responsibilities

| Role | Main responsibility | Should avoid |
|---|---|---|
| Strategist | Understand reviewer concerns, draft response logic, write the plan | Directly editing TeX |
| Executor | Apply the accepted plan, compile, redline, commit | Reinterpreting the scientific claim |
| Auditor | Read PDFs, verify locations, check response fidelity | Introducing new edits |
| Human | Approve direction, decide task size, accept final result | Micromanaging every mechanical edit |

This is the human-agent version of divide and conquer.

## 6. Plan Size Guide

Use one plan when the task is coherent:

- One reviewer comment.
- One figure-caption correction.
- One proof-correction batch.
- One manuscript-shortening pass with clearly listed paragraphs.

Split the plan when the task mixes different types of work:

- Scientific claim changes plus wording polish.
- Main manuscript plus supplementary tables plus response letter.
- Figure replacement plus equation rewrite.
- Broad style changes plus technical validation.

The plan size should match the amount of control needed.

## 7. Practical Tips

Use stable file names:

```text
original_main.tex       previous submitted baseline
main.tex                current latest manuscript
original_sm.tex         previous submitted supplement
sm.tex                  current latest supplement
redlined_main.tex       generated redline
redlined_sm.tex         generated redline supplement
response_letter.tex     active response letter
references/             plans, audits, notes
```

Use concrete plan filenames:

```text
references/reviewer1_comment1_revision1.md
references/figure2_missing_reference_plan.md
references/proof_corrections_2026-03-12.md
references/main_text_shorten_pass2.md
```

Use build scripts:

```bash
bash build_all.sh
bash build_redlined_minor.sh
```

Use PDF inspection:

```bash
pdftotext -layout main.pdf - | rg "target phrase"
pdftotext -layout -f 2 -l 2 main.pdf -
```

Use linear Git checkpoints:

```bash
git status --short
git diff --stat
git add <files>
git commit -m "Revise reviewer 1 response location"
git push
```

## 8. Standard Instruction For Codex

Use this prompt when asking Codex to execute a revision:

```text
You are working on an academic manuscript revision.

First read the relevant plan in references/.
Do not edit anything outside the plan.
If the plan is too broad or vague, stop and propose a smaller plan.
Apply only the approved edits.
After editing, update the plan's Execution Notes.
Run the build command.
Inspect the generated PDF if available.
Update the response letter only with verified changes.
Generate the redlined version when a baseline is available.
Show git diff summary.
Commit and push this work package.
```

## Closing Summary

This method works because it changes the agent from a free-writing assistant into a controlled revision operator.

Without the plan gate:

```text
Comment -> AI edits freely -> scope expands -> response and paper drift apart
```

With the plan gate:

```text
Comment -> plan -> approval -> bounded edit -> PDF check -> redline -> response sync -> commit
```

The value of the `references/` folder is that every meaningful revision has:

- a boundary
- an intention
- a rationale
- a verification path
- a history

That is why this method is useful for paper revision, code changes, app development, and any agent workflow where uncontrolled edits are expensive.
