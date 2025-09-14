#!/usr/bin/env python3
"""
Fix inline HTML style attributes in MDX/Markdown files to React JSX style objects.

Example:
  <img style="width: 100px; border: 1px solid #ccc;" />
becomes
  <img style={{ width: "100px", border: "1px solid #ccc" }} />

Notes:
 - Converts kebab-case CSS properties to camelCase (e.g., background-color -> backgroundColor)
 - Trims extra whitespace and trailing semicolons
 - Wraps all values as strings to be safe (e.g., "600px", "#ccc")
 - Handles both style="..." and style='...'
 - Skips files under build/
"""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"

# Regex to match style attribute with either single or double quotes
STYLE_ATTR_RE = re.compile(r"style=(\"([^\"]*)\"|'([^']*)')")

def kebab_to_camel(s: str) -> str:
    parts = s.split('-')
    if not parts:
        return s
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def parse_css_to_jsx_object(css: str) -> str:
    # Split by ; but ignore empty entries
    decls = [d.strip() for d in css.split(';') if d.strip()]
    props = []
    for decl in decls:
        if ':' not in decl:
            continue
        prop, value = decl.split(':', 1)
        prop = kebab_to_camel(prop.strip())
        # Normalize quotes inside value and trim
        value = value.strip()
        # Unescape common HTML entity quotes and backslashes
        value = value.replace('&quot;', '"').replace('&#34;', '"').replace('&#39;', "'")
        # Strip wrapping quotes if present
        if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
            value = value[1:-1]
        # Collapse internal escaped quotes from CSV origins
        value = value.replace('\\"', '"').replace("\\'", "'")
        # Build as a JS string
        # Escape backslashes and double quotes for JS string literal inside JSX
        js_value = value.replace('\\', r'\\').replace('"', r'\"')
        props.append(f'{prop}: "{js_value}"')
    return '{{ ' + ', '.join(props) + ' }}'

def transform_content(text: str) -> tuple[str, int]:
    count = 0
    def _repl(m: re.Match) -> str:
        nonlocal count
        full = m.group(0)
        inner = m.group(2) if m.group(2) is not None else m.group(3) or ''
        jsx_obj = parse_css_to_jsx_object(inner)
        count += 1
        return f'style={jsx_obj}'

    new_text, n = STYLE_ATTR_RE.subn(_repl, text)
    return new_text, n

def should_process(path: Path) -> bool:
    if 'build' in path.parts:
        return False
    if path.suffix.lower() in {'.md', '.mdx'}:
        return True
    return False

def main() -> None:
    files_changed = 0
    total_replacements = 0
    for root, _, files in os.walk(DOCS_DIR):
        for name in files:
            p = Path(root) / name
            if not should_process(p):
                continue
            try:
                text = p.read_text(encoding='utf-8')
            except Exception:
                continue
            new_text, n = transform_content(text)
            if n > 0:
                p.write_text(new_text, encoding='utf-8')
                files_changed += 1
                total_replacements += n
                print(f"Fixed {n:>3} style attr(s) in {p.relative_to(ROOT)}")
    print(f"\nDone. Files changed: {files_changed}, style attrs fixed: {total_replacements}")

if __name__ == '__main__':
    main()
