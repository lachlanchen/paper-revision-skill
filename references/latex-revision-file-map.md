# LaTeX Revision File Map

This reference gives a reusable file convention for manuscript revisions with main text, supplementary material, baselines, current versions, and redlined outputs.

## Contents

1. Recommended directory structure
2. Active latest files
3. Baseline files
4. Redlined files
5. Response and cover letters
6. Build scripts
7. Editing sequence

## 1. Recommended Directory Structure

Use a layout like this:

```text
paper-project/
├── Manuscript/
│   ├── main.tex
│   ├── sm.tex
│   ├── original_main.tex
│   ├── original_sm.tex
│   ├── major_revision_main.tex
│   ├── major_revision_sm.tex
│   ├── redlined_main.tex
│   ├── redlined_sm.tex
│   ├── redlined_minor_main.tex
│   ├── redlined_minor_sm.tex
│   ├── figures/
│   └── figures_sm/
├── ResponseLetter/
│   ├── response_letter.tex
│   └── response_letter_minor.tex
├── references/
│   ├── reviewer_comments/
│   ├── proofreading/
│   └── revision_plans/
├── build_all.sh
└── build_redlined_minor.sh
```

The exact names can vary, but the roles should stay stable.

## 2. Active Latest Files

Treat these as the editable current manuscript:

- `Manuscript/main.tex`: current latest main manuscript.
- `Manuscript/sm.tex`: current latest supplementary material.

Do not rename these for every revision. Keeping active names stable makes build scripts, response letters, and figure paths easier to maintain.

If a journal requires upload names such as `latest_main.tex`, create those as export copies near submission time, not as the main editing target.

## 3. Baseline Files

Use baseline files to preserve previous submissions:

- `original_main.tex`: original submitted main manuscript.
- `original_sm.tex`: original submitted supplementary material.
- `major_revision_main.tex`: accepted or submitted major-revision main manuscript used as the baseline for minor redlines.
- `major_revision_sm.tex`: accepted or submitted major-revision supplement used as the baseline for minor redlines.

Never edit baselines unless intentionally resetting the comparison point.

## 4. Redlined Files

Use `latexdiff` or an equivalent tool to create redlines:

- `redlined_main.tex`: diff from `original_main.tex` to `main.tex`.
- `redlined_sm.tex`: diff from `original_sm.tex` to `sm.tex`.
- `redlined_minor_main.tex`: diff from `major_revision_main.tex` to `main.tex`.
- `redlined_minor_sm.tex`: diff from `major_revision_sm.tex` to `sm.tex`.

Compile redlined TeX into PDFs and inspect the output. Redline files are useful even when not submitted because they expose unintended edits.

## 5. Response And Cover Letters

Keep response letters separate from the manuscript:

- `ResponseLetter/response_letter.tex`: detailed reviewer response for a major revision.
- `ResponseLetter/response_letter_minor.tex`: concise response for a minor revision.
- `Manuscript/cover_letter_revision.tex`: cover letter when required by the journal.

Response letters should cite current manuscript locations after the clean PDF is built.

## 6. Build Scripts

Useful script responsibilities:

- Compile `main.tex`.
- Compile `sm.tex`.
- Generate redlined main and supplementary files from the selected baselines.
- Compile redlined PDFs.
- Compile response and cover letters when relevant.
- Move LaTeX auxiliary files into a build-artifact folder.

If `latexdiff` fails on a particular equation, make the fix repeatable in the script.

## 7. Editing Sequence

For a planned manuscript edit:

1. Save a plan markdown under `references/`.
2. Edit `main.tex` or `sm.tex`.
3. Compile the clean PDF.
4. Generate redlined TeX.
5. Compile redlined PDF.
6. Inspect the PDF for layout, references, and figure/equation numbering.
7. Update response-letter locations if needed.
8. Commit and push.

For proof corrections:

1. Inspect the proof PDF.
2. Write a correction note with location, current proof text, and corrected text.
3. Submit through the journal proof system.
4. Update local files only if the project wants a matching archive.
