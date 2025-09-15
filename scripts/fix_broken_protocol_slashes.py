#!/usr/bin/env python3
"""
Fix malformed URLs in markdown/MDX files where the protocol is followed by a single slash
instead of double slashes, e.g. "https:/s3.amazonaws.com/...".

This script scans the docs/ and blog/ folders and rewrites:
  - "https:/(?!/)" -> "https://"
  - "http:/(?!/)"  -> "http://"

It prints a small summary of the changes.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [ROOT / "docs", ROOT / "blog"]
EXTS = {".md", ".mdx"}

# Precompile regexes: Look for protocol with only a single slash after colon
HTTPS_SINGLE_SLASH = re.compile(r"https:/(?!/)")
HTTP_SINGLE_SLASH = re.compile(r"http:/(?!/)")

def fix_content(text: str) -> tuple[str, int]:
    count = 0
    new_text, n1 = HTTPS_SINGLE_SLASH.subn("https://", text)
    count += n1
    new_text, n2 = HTTP_SINGLE_SLASH.subn("http://", new_text)
    count += n2
    return new_text, count

def main() -> None:
    total_files = 0
    total_changes = 0
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() in EXTS and path.is_file():
                text = path.read_text(encoding="utf-8")
                new_text, changes = fix_content(text)
                if changes:
                    path.write_text(new_text, encoding="utf-8")
                    total_changes += changes
                    total_files += 1
                    print(f"Fixed {changes:>3} issue(s) in {path.relative_to(ROOT)}")

    if total_files == 0:
        print("No files needed changes. ✅")
    else:
        print(f"\nDone. Fixed {total_changes} occurrence(s) across {total_files} file(s). ✅")

if __name__ == "__main__":
    main()
