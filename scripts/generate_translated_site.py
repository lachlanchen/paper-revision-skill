#!/usr/bin/env python3
"""Generate static translated GitHub Pages files from docs/origin-chat.html.

The script translates visible text nodes with the public Google Translate
endpoint. It deliberately skips code, pre, style, script, select, and option
content so commands, filenames, language labels, and snippets remain stable.
"""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    from bs4 import BeautifulSoup, NavigableString
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: beautifulsoup4. Install with `python -m pip install beautifulsoup4`.") from exc

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SOURCE = DOCS / "origin-chat.html"
CACHE = ROOT / ".translation_cache.json"

LANGS: Dict[str, Tuple[str, str]] = {
    "ar": ("العربية", "ar"),
    "es": ("Español", "es"),
    "fr": ("Français", "fr"),
    "ja": ("日本語", "ja"),
    "ko": ("한국어", "ko"),
    "vi": ("Tiếng Việt", "vi"),
    "zh-Hans": ("中文 (简体)", "zh-CN"),
    "zh-Hant": ("中文（繁體）", "zh-TW"),
    "de": ("Deutsch", "de"),
    "ru": ("Русский", "ru"),
}

LANG_OPTIONS = [
    ("en", "English"),
    ("ar", "العربية"),
    ("es", "Español"),
    ("fr", "Français"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("vi", "Tiếng Việt"),
    ("zh-Hans", "中文 (简体)"),
    ("zh-Hant", "中文（繁體）"),
    ("de", "Deutsch"),
    ("ru", "Русский"),
]

SKIP_TAGS = {"style", "script", "code", "pre", "select", "option"}
PRESERVE_TERMS = [
    "Paper Revision Skill",
    "Plan-Gated Paper Revision Skill",
    "GitHub",
    "Codex",
    "ChatGPT",
    "AI",
    "PDF",
    "LaTeX",
    "Markdown",
    "README",
    "SKILL.md",
    "LazyingArt",
    "Chen Miao",
    "Feifei Robbie",
    "Zhuge Liang",
    "Zhao Yun",
    "original_main.tex",
    "main.tex",
    "sm.tex",
    "redlined_main.tex",
    "response_letter.tex",
    "main.pdf",
    "response_letter.pdf",
    "references/*.md",
    "references/",
    "reviewer1_comment1_revision1.md",
    "figure4_caption_shorten_plan.md",
    "main_text_shorten_plan.md",
    "references/reviewer1_comment1_revision1.md",
    "references/reviewer2_comment6_reanalysis_plan.md",
    "paper-revision-agent-skill/",
    "revision_plan.md",
    "response_trace_audit.md",
    "revision_task_index.md",
    "plan_prompt.md",
    "apply_prompt.md",
    "audit_prompt.md",
]
PRESERVE_TERMS = sorted(PRESERVE_TERMS, key=len, reverse=True)


def load_cache() -> Dict[str, str]:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: Dict[str, str]) -> None:
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def should_skip(text: str, parent_name: str | None, parent_classes: Iterable[str] = ()) -> bool:
    core = normalize_text(text)
    if not core:
        return True
    if parent_name in SKIP_TAGS:
        return True
    if "avatar" in set(parent_classes):
        return True
    if core in PRESERVE_TERMS:
        return True
    if re.fullmatch(r"[A-Z]", core):
        return True
    if re.fullmatch(r"[0-9]+", core):
        return True
    if re.fullmatch(r"[,.:;()\[\]{}\-–—/\\]+", core):
        return True
    return False


def protect(text: str) -> Tuple[str, Dict[str, str]]:
    mapping: Dict[str, str] = {}
    out = text
    idx = 0
    for term in PRESERVE_TERMS:
        if term in out:
            token = f"ZXQTERM{idx:03d}QXZ"
            out = out.replace(term, token)
            mapping[token] = term
            idx += 1
    return out, mapping


def restore(text: str, mapping: Dict[str, str]) -> str:
    out = text
    for token, term in mapping.items():
        out = out.replace(token, term).replace(token.lower(), term)
    return out


def google_translate(text: str, target: str, timeout: int = 20) -> str:
    params = urllib.parse.urlencode({"client": "gtx", "sl": "en", "tl": target, "dt": "t", "q": text})
    request = urllib.request.Request(
        "https://translate.googleapis.com/translate_a/single?" + params,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8"))
    return "".join(part[0] for part in data[0])


def translate_items(items: List[str], target: str, cache: Dict[str, str]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    pending = [item for item in items if f"{target}\n{item}" not in cache]

    # Batch by protected text length. Delimiters are preserved well by the endpoint.
    batch: List[str] = []
    batch_original: List[str] = []
    batch_mappings: List[Dict[str, str]] = []

    def flush() -> None:
        nonlocal batch, batch_original, batch_mappings
        if not batch:
            return
        delimiters = [f"ZXQSEG{i:04d}QXZ" for i in range(len(batch) - 1)]
        joined_parts: List[str] = []
        for i, text in enumerate(batch):
            joined_parts.append(text)
            if i < len(delimiters):
                joined_parts.append(delimiters[i])
        joined = "\n".join(joined_parts)
        for attempt in range(4):
            try:
                translated_joined = google_translate(joined, target)
                parts = translated_joined
                for delimiter in delimiters:
                    parts = parts.replace(delimiter.lower(), delimiter)
                split = [part.strip() for part in parts.split("\n") if part.strip()]
                cleaned: List[str] = []
                for part in split:
                    if re.fullmatch(r"ZXQSEG[0-9]{4}QXZ", part):
                        continue
                    cleaned.append(part)
                if len(cleaned) != len(batch):
                    raise RuntimeError(f"split mismatch: {len(cleaned)} translated for {len(batch)} items")
                for original, translated, mapping in zip(batch_original, cleaned, batch_mappings):
                    cache[f"{target}\n{original}"] = restore(translated, mapping)
                break
            except Exception as exc:
                if attempt == 3:
                    # Conservative fallback: translate one by one, preserving English if still failing.
                    for original, protected_text, mapping in zip(batch_original, batch, batch_mappings):
                        try:
                            cache[f"{target}\n{original}"] = restore(google_translate(protected_text, target), mapping)
                        except Exception:
                            cache[f"{target}\n{original}"] = original
                    break
                time.sleep(1.5 + attempt)
        batch = []
        batch_original = []
        batch_mappings = []

    for original in pending:
        protected, mapping = protect(original)
        projected = sum(len(x) + 20 for x in batch) + len(protected)
        if projected > 3200 or len(batch) >= 24:
            flush()
        batch.append(protected)
        batch_original.append(original)
        batch_mappings.append(mapping)
    flush()

    for item in items:
        result[item] = cache.get(f"{target}\n{item}", item)
    return result


def localized_header(current: str) -> str:
    options = []
    for code, label in LANG_OPTIONS:
        value = "../origin-chat.html" if code == "en" else f"origin-chat.{code}.html"
        selected = " selected" if code == current else ""
        options.append(f'<option value="{value}"{selected}>{label}</option>')
    return f'''    <header class="site-header" aria-label="Site navigation">
      <a class="site-brand" href="../index.html">Paper Revision Skill</a>
      <nav class="site-nav" aria-label="Primary navigation">
        <a href="../origin-chat.html">Full Guide</a>
        <a href="../origin-chat-downloaded-package.html">Standalone</a>
        <a href="https://github.com/lachlanchen/paper-revision-skill">GitHub</a>
      </nav>
      <div class="language-menu">
        <label class="sr-only" for="language-select">Choose language</label>
        <select id="language-select" data-language-select aria-label="Choose language">
{chr(10).join(options)}
        </select>
      </div>
    </header>'''


def make_i18n_source(current: str) -> str:
    html = SOURCE.read_text(encoding="utf-8")
    lang_attr = f'<html lang="{current}" dir="rtl">' if current == "ar" else f'<html lang="{current}">'
    html = html.replace('<html lang="en">', lang_attr)
    html = html.replace('<link rel="stylesheet" href="site.css">', '<link rel="stylesheet" href="../site.css">\n  <link rel="stylesheet" href="style.css">')
    html = html.replace('<script defer src="site.js"></script>', '<script defer src="../site.js"></script>')
    html = html.replace('href="assets/lazyingart-logo.png"', 'href="../assets/lazyingart-logo.png"')
    start = html.index('    <header class="site-header"')
    end = html.index('    <header class="hero">', start)
    return html[:start] + localized_header(current) + "\n" + html[end:]


def write_english_mirror() -> None:
    html = make_i18n_source("en")
    (DOCS / "i18n" / "origin-chat.en.html").write_text(html, encoding="utf-8")


def translate_page(code: str, target: str, label: str, cache: Dict[str, str]) -> None:
    soup = BeautifulSoup(make_i18n_source(code), "html.parser")
    nodes: List[NavigableString] = []
    originals: List[str] = []
    for node in soup.find_all(string=True):
        parent_name = node.parent.name if node.parent else None
        parent_classes = node.parent.get("class", []) if node.parent else []
        text = str(node)
        if should_skip(text, parent_name, parent_classes):
            continue
        core = normalize_text(text)
        nodes.append(node)
        originals.append(core)
    unique = list(dict.fromkeys(originals))
    translations = translate_items(unique, target, cache)
    for node, original in zip(nodes, originals):
        leading = str(node)[: len(str(node)) - len(str(node).lstrip())]
        trailing = str(node)[len(str(node).rstrip()) :]
        node.replace_with(NavigableString(leading + translations.get(original, original) + trailing))
    title = soup.find("title")
    if title:
        title.string = f"Paper Revision Skill — {label}"
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        desc = meta.get("content", "")
        if desc:
            meta["content"] = translations.get(normalize_text(desc), desc)
    html = fix_svg_serialization(str(soup))
    (DOCS / "i18n" / f"origin-chat.{code}.html").write_text(html, encoding="utf-8")


def fix_svg_serialization(html: str) -> str:
    """Restore SVG attribute names that html.parser lowercases."""
    replacements = {
        "viewbox=": "viewBox=",
        "markerheight=": "markerHeight=",
        "markerwidth=": "markerWidth=",
        "markerunits=": "markerUnits=",
        "refx=": "refX=",
        "refy=": "refY=",
        "preserveaspectratio=": "preserveAspectRatio=",
        "stddeviation=": "stdDeviation=",
        "<fedropshadow": "<feDropShadow",
        "</fedropshadow>": "</feDropShadow>",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def main() -> None:
    cache = load_cache()
    write_english_mirror()
    for code, (label, target) in LANGS.items():
        print(f"Translating {code} -> {target}")
        translate_page(code, target, label, cache)
        save_cache(cache)
    save_cache(cache)


if __name__ == "__main__":
    main()
