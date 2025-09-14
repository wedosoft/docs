#!/usr/bin/env python3
"""
Replace HTML line break tags (<br>, <br/>, <br />) and escaped variants (&lt;br/&gt; etc.)
with Markdown newlines. Consecutive <br> groups become empty lines (paragraph break).

Rules:
 - Any of: <br>, <br/>, <br /> (case-insensitive) -> single newline "\n"
 - Escaped forms: &lt;br&gt;, &lt;br/&gt;, &lt;br /&gt; -> single newline
 - Multiple in a row -> collapse to at most 2 newlines (one empty line)
 - Remove stray <p><br/></p> HTML fragments by normalizing p-wrapped breaks
 - Skip build/ directory
Applies to .md and .mdx under docs/
"""
from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / 'docs'

# regexes (case-insensitive, dotall to be robust)
BR_TAG = re.compile(r"<\s*br\s*/?\s*>", re.IGNORECASE)
BR_ESC = re.compile(r"&lt;\s*br\s*/?\s*&gt;", re.IGNORECASE)

# Wrap patterns like <p><br/></p> -> two newlines
P_BR_P = re.compile(r"<\s*p\s*>\s*(?:<\s*br\s*/?\s*>|&lt;\s*br\s*/?\s*&gt;)\s*<\s*/\s*p\s*>", re.IGNORECASE)

def should_process(path: Path) -> bool:
    if 'build' in path.parts:
        return False
    return path.suffix.lower() in {'.md', '.mdx'}

def normalize_newlines(s: str) -> str:
    # Collapse 3+ newlines to 2
    return re.sub(r"\n{3,}", "\n\n", s)

def transform(text: str) -> tuple[str, int, dict]:
    original = text
    # First, normalize <p><br/></p>
    text, n0 = P_BR_P.subn("\n\n", text)
    # Replace raw <br> tags
    text, n1 = BR_TAG.subn("\n", text)
    # Replace escaped &lt;br/&gt; tags
    text, n2 = BR_ESC.subn("\n", text)
    # Normalize excessive newlines
    text = normalize_newlines(text)
    return text, (n0 + n1 + n2), {"p_br_p": n0, "br": n1, "br_esc": n2}

def main() -> None:
    files_changed = 0
    total_replacements = 0
    totals = {"p_br_p": 0, "br": 0, "br_esc": 0}
    for root, _, files in os.walk(DOCS_DIR):
        for name in files:
            p = Path(root) / name
            if not should_process(p):
                continue
            try:
                txt = p.read_text(encoding='utf-8')
            except Exception:
                continue
            new_txt, n, parts = transform(txt)
            if new_txt != txt:
                p.write_text(new_txt, encoding='utf-8')
                files_changed += 1
                total_replacements += n
                totals["p_br_p"] += parts["p_br_p"]
                totals["br"] += parts["br"]
                totals["br_esc"] += parts["br_esc"]
                print(
                    f"Replaced total {n:>3} (p<br>p={parts['p_br_p']}, br={parts['br']}, br_esc={parts['br_esc']}) in {p.relative_to(ROOT)}"
                )
    print(
        f"\nDone. Files changed: {files_changed}, total replacements: {total_replacements} "
        f"(p<br>p={totals['p_br_p']}, br={totals['br']}, br_esc={totals['br_esc']})"
    )

if __name__ == '__main__':
    main()
