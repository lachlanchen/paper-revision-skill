#!/usr/bin/env python3
"""Find PDF-backed location anchors for response letters and proof notes.

This helper uses pdftotext output to find candidate page and paragraph anchors.
It is intentionally conservative: extracted text positions are not journal line
numbers. Use the results as evidence to inspect the final PDF, then cite page,
section, figure/table/equation, and paragraph-beginning text.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def extract_page(pdf: Path, page: int) -> str:
    cmd = [
        "pdftotext",
        "-layout",
        "-f",
        str(page),
        "-l",
        str(page),
        str(pdf),
        "-",
    ]
    return subprocess.check_output(cmd, text=True, errors="replace")


def page_count(pdf: Path) -> int:
    if shutil.which("pdfinfo"):
        out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, errors="replace")
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":", 1)[1].strip())

    # Fallback: increment until pdftotext stops producing usable output.
    page = 1
    while True:
        try:
            extract_page(pdf, page)
        except subprocess.CalledProcessError:
            return page - 1
        page += 1


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def paragraph_anchor(lines: list[str], idx: int) -> str:
    start = idx
    while start > 0 and lines[start - 1].strip():
        start -= 1
    para = " ".join(line.strip() for line in lines[start : min(len(lines), start + 5)] if line.strip())
    if not para:
        para = lines[idx].strip()
    return para[:220]


def column_guess(line: str) -> str:
    if not line.strip():
        return "unknown"
    leading = len(line) - len(line.lstrip(" "))
    if leading >= 42:
        return "right column candidate"
    return "left column or full-width candidate"


def find_terms(pdf: Path, terms: list[str]) -> int:
    if not shutil.which("pdftotext"):
        raise SystemExit("Missing required command: pdftotext")

    pages = page_count(pdf)
    found = 0
    normalized_terms = [(term, normalize(term)) for term in terms]

    for page in range(1, pages + 1):
        text = extract_page(pdf, page)
        lines = text.splitlines()
        normalized_page = normalize(text)
        for original, needle in normalized_terms:
            if needle not in normalized_page:
                continue
            for idx, line in enumerate(lines):
                if needle in normalize(line):
                    found += 1
                    print(f"PDF: {pdf}")
                    print(f"Search term: {original}")
                    print(f"Page: {page}")
                    print(f"Extracted text line: {idx + 1} (not a journal manuscript line number)")
                    print(f"Column estimate: {column_guess(line)}")
                    print(f"Line text: {line.strip()}")
                    print(f"Paragraph anchor: {paragraph_anchor(lines, idx)}")
                    print("-" * 72)
                    break
            else:
                found += 1
                print(f"PDF: {pdf}")
                print(f"Search term: {original}")
                print(f"Page: {page}")
                print("Location: term found in page text; inspect PDF visually for paragraph anchor.")
                print("-" * 72)

    if found == 0:
        print("No matches found.")
    return 0 if found else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find conservative PDF-backed location anchors for manuscript edits."
    )
    parser.add_argument("pdf", type=Path, help="Compiled PDF to search")
    parser.add_argument("terms", nargs="+", help="Exact phrases or distinctive terms to locate")
    args = parser.parse_args()
    return find_terms(args.pdf, args.terms)


if __name__ == "__main__":
    raise SystemExit(main())
