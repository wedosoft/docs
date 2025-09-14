#!/usr/bin/env python3
"""
Unescape HTML-escaped <img .../> sequences inside MDX files where they appear
as text (e.g., &lt;img ... /&gt;), convert them to real JSX <img ... /> tags, and
normalize attributes:
 - Replace class="..." with className="..."
 - Normalize stray spaces and duplicate slashes before />

This targets known problematic Analytics docs to avoid overreach.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGET_FILES = [
    ROOT / 'docs/freshservice/platform/analytics/comparing-multiple-metrics-in-a-widget.md',
    ROOT / 'docs/freshservice/platform/analytics/exporting-data-from-analytics-to-power-bi.md',
    ROOT / 'docs/freshservice/platform/analytics/exporting-data-from-analytics-to-tableau.md',
    ROOT / 'docs/freshservice/platform/analytics/generate-intuitive-reports-using-analytics-pro.md',
]

# Matches an escaped <img ... /> sequence like: &lt;img ... /&gt;
# Use DOTALL to allow newlines inside attributes.
ESCAPED_IMG_RE = re.compile(r"&lt;\s*img\b(.*?)\s*/\s*&gt;", re.DOTALL)

def normalize_img_attrs(attrs: str) -> str:
    s = attrs
    # Fix accidental ' / /' duplicates from sources
    s = s.replace('/ /', '/ ')
    # Replace class= with className=
    s = re.sub(r'\bclass=', 'className=', s)
    # Ensure proper spacing
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def unescape_imgs(text: str) -> tuple[str, int]:
    count = 0
    def _repl(m: re.Match) -> str:
        nonlocal count
        attrs = normalize_img_attrs(m.group(1))
        count += 1
        # Ensure self-closing
        attrs_clean = attrs.strip()
        # Avoid duplicate trailing slash from malformed inputs
        attrs_clean = attrs_clean.rstrip('/')
        return f"<img{(' ' + attrs_clean) if attrs_clean else ''} />"
    new_text, n = ESCAPED_IMG_RE.subn(_repl, text)
    return new_text, n

def main() -> None:
    total = 0
    for fp in TARGET_FILES:
        if not fp.exists():
            continue
        txt = fp.read_text(encoding='utf-8')
        new_txt, n = unescape_imgs(txt)
        if n:
            fp.write_text(new_txt, encoding='utf-8')
            total += n
            print(f"Fixed {n} escaped <img> in {fp.relative_to(ROOT)}")
    print(f"Done. Total fixes: {total}")

if __name__ == '__main__':
    main()
