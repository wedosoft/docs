#!/usr/bin/env python3
"""
Convert HTML-escaped <br> tags (e.g., &lt;br/>, &lt;br />) in Markdown files to proper
line breaks so they don't render as literal text.

Rules
- Inside Markdown tables (lines that look like table rows), replace with real '<br />'
  so line breaks render within the same cell.
- Outside tables, collapse double breaks like '.&lt;br/>&lt;br/>' into paragraph breaks
  (".\n\n"), and single breaks into a Markdown hard break ('  \n').
- Skip code blocks fenced by triple backticks or tildes.

Targets: docs/ and blog/ with .md or .mdx files.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [ROOT / "docs", ROOT / "blog"]
EXTS = {".md", ".mdx"}

# Patterns for escaped <br> variants.
# Many files contain hybrid-escaped tags like "&lt;br />" (only the '<' is escaped)
# as well as fully escaped "&lt;br/&gt;". Support both endings: literal '>' or '&gt;'.
ESC_BR = re.compile(r"\s*&lt;\s*br\s*/?\s*(?:&gt;|>)\s*", re.IGNORECASE)
ESC_BR_RAW = re.compile(r"&lt;\s*br\s*/?\s*(?:&gt;|>)", re.IGNORECASE)

# Detect likely table row: starts with '|' or has pipes with surrounding spaces
TABLE_LINE = re.compile(r"^\s*\|.*\|\s*$|\s\|\s")

FENCE = re.compile(r"^\s*(```|~~~)")

def process_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out_lines = []
    in_code = False
    changes = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        # Toggle code fence state
        if FENCE.match(line):
            in_code = not in_code
            out_lines.append(line)
            i += 1
            continue

        if in_code:
            out_lines.append(line)
            i += 1
            continue

        # If line contains escaped <br> tokens
        if ESC_BR_RAW.search(line):
            if TABLE_LINE.search(line):
                # In tables: unescape to real <br /> to keep cell integrity
                new_line, n = ESC_BR_RAW.subn("<br />", line)
                if n:
                    changes += n
                out_lines.append(new_line)
                i += 1
                continue
            else:
                # Paragraph/text: convert double breaks to blank line, single to hard break
                # First, expand all to a placeholder token, then post-process
                tokens = ESC_BR.split(line)
                # Count occurrences by reconstructing
                occ = len(tokens) - 1
                if occ == 0:
                    out_lines.append(line)
                    i += 1
                    continue

                changes += occ

                # Heuristic: treat consecutive breaks (>1 in a row) as paragraph break.
                # We'll rebuild by scanning ESC_BR matches in the original line.
                rebuilt = []
                pos = 0
                for m in ESC_BR_RAW.finditer(line):
                    rebuilt.append(line[pos:m.start()])
                    pos = m.end()
                    # Lookahead to see if the next thing is another escaped br immediately
                    nxt = ESC_BR_RAW.match(line, pos)
                    if nxt:
                        # paragraph break
                        rebuilt.append("\n\n")
                        pos = nxt.end()
                    else:
                        # hard line break
                        rebuilt.append("  \n")
                rebuilt.append(line[pos:])
                new_line = "".join(rebuilt)
                out_lines.append(new_line)
                i += 1
                continue

        # Default: passthrough
        out_lines.append(line)
        i += 1

    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else ""), changes

def main() -> None:
    total_files = 0
    total_changes = 0
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() in EXTS and path.is_file():
                original = path.read_text(encoding="utf-8")
                fixed, n = process_text(original)
                if n and fixed != original:
                    path.write_text(fixed, encoding="utf-8")
                    total_files += 1
                    total_changes += n
                    print(f"Fixed {n:>3} br tag(s) in {path.relative_to(ROOT)}")
    if total_files:
        print(f"\nDone. Updated {total_files} file(s), {total_changes} replacement(s). ✅")
    else:
        print("No escaped <br> tags found to fix. ✅")

if __name__ == "__main__":
    main()
