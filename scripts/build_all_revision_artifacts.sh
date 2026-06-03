#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-.}"
LATEX_FLAGS="${LATEX_FLAGS:--interaction=nonstopmode -halt-on-error}"
MANUSCRIPT_DIR="${MANUSCRIPT_DIR:-Manuscript}"
RESPONSE_DIR="${RESPONSE_DIR:-ResponseLetter}"
COVER_DIR="${COVER_DIR:-Manuscript}"
RUN_REDLINE="${RUN_REDLINE:-1}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  }
}

compile_tex() {
  local tex="$1"
  local dir
  local file
  local job

  [ -f "$tex" ] || return 0

  dir="$(cd "$(dirname "$tex")" && pwd)"
  file="$(basename "$tex")"
  job="${file%.tex}"

  printf 'Compiling %s\n' "$tex"
  (
    cd "$dir"
    pdflatex $LATEX_FLAGS "$file" >/dev/null
    if [ -f "$job.aux" ]; then
      bibtex "$job" >/dev/null 2>&1 || true
    fi
    pdflatex $LATEX_FLAGS "$file" >/dev/null
    pdflatex $LATEX_FLAGS "$file" >/dev/null
  )
}

need_cmd pdflatex

ROOT_DIR="$(cd "$ROOT_DIR" && pwd)"

compile_tex "$ROOT_DIR/$MANUSCRIPT_DIR/main.tex"
compile_tex "$ROOT_DIR/$MANUSCRIPT_DIR/sm.tex"
compile_tex "$ROOT_DIR/$RESPONSE_DIR/response_letter.tex"
compile_tex "$ROOT_DIR/$RESPONSE_DIR/Author_response_optica_585766_using_template.tex"
compile_tex "$ROOT_DIR/$COVER_DIR/cover_letter.tex"
compile_tex "$ROOT_DIR/$COVER_DIR/cover_letter_revision1.tex"
compile_tex "$ROOT_DIR/$COVER_DIR/cover_letter_revision_minor.tex"

if [ "$RUN_REDLINE" = "1" ] && [ -x "$SCRIPT_DIR/build_revision_redlines.sh" ]; then
  if [ -d "$ROOT_DIR/$MANUSCRIPT_DIR" ]; then
    "$SCRIPT_DIR/build_revision_redlines.sh" "$ROOT_DIR/$MANUSCRIPT_DIR"
  else
    printf 'Skipping redlines: manuscript directory not found: %s\n' "$ROOT_DIR/$MANUSCRIPT_DIR"
  fi
fi

printf 'All revision artifacts build complete.\n'
