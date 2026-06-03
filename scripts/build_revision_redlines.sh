#!/usr/bin/env bash
set -euo pipefail

WORK_DIR="${1:-.}"
MAIN_TEX="${MAIN_TEX:-main.tex}"
SM_TEX="${SM_TEX:-sm.tex}"
MAIN_BASELINE="${MAIN_BASELINE:-original_main.tex}"
SM_BASELINE="${SM_BASELINE:-original_sm.tex}"
REDLINED_MAIN="${REDLINED_MAIN:-redlined_main.tex}"
REDLINED_SM="${REDLINED_SM:-redlined_sm.tex}"
LATEX_FLAGS="${LATEX_FLAGS:--interaction=nonstopmode}"

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  }
}

compile_tex() {
  local tex="$1"
  local job="${tex%.tex}"

  [ -f "$tex" ] || return 0

  printf 'Compiling %s\n' "$tex"
  pdflatex $LATEX_FLAGS "$tex" >/dev/null
  if [ -f "$job.aux" ]; then
    bibtex "$job" >/dev/null 2>&1 || true
  fi
  pdflatex $LATEX_FLAGS "$tex" >/dev/null
  pdflatex $LATEX_FLAGS "$tex" >/dev/null
}

make_redline() {
  local baseline="$1"
  local current="$2"
  local output="$3"

  if [ ! -f "$baseline" ] || [ ! -f "$current" ]; then
    printf 'Skipping redline: need %s and %s\n' "$baseline" "$current"
    return 0
  fi

  printf 'Generating %s from %s -> %s\n' "$output" "$baseline" "$current"
  latexdiff "$baseline" "$current" > "$output"
}

need_cmd pdflatex
need_cmd latexdiff

cd "$WORK_DIR"

compile_tex "$MAIN_TEX"
compile_tex "$SM_TEX"

make_redline "$MAIN_BASELINE" "$MAIN_TEX" "$REDLINED_MAIN"
make_redline "$SM_BASELINE" "$SM_TEX" "$REDLINED_SM"

if [ -f "${MAIN_TEX%.tex}.bbl" ] && [ -f "$REDLINED_MAIN" ]; then
  cp "${MAIN_TEX%.tex}.bbl" "${REDLINED_MAIN%.tex}.bbl"
fi

if [ -f "${SM_TEX%.tex}.bbl" ] && [ -f "$REDLINED_SM" ]; then
  cp "${SM_TEX%.tex}.bbl" "${REDLINED_SM%.tex}.bbl"
fi

compile_tex "$REDLINED_MAIN"
compile_tex "$REDLINED_SM"

printf 'Revision build complete.\n'
