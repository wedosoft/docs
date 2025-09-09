#!/usr/bin/env python3
"""
Fix specific MDX parsing issues in problematic FAQ files.
"""

import re

def fix_mdx_file(file_path):
    """Fix MDX issues in a specific file."""
    print(f"Fixing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix workspace name placeholder
    content = re.sub(r'\\?\{Workspace Name\\?\}', '[Workspace Name]', content)
    
    # Fix navigation arrows
    content = re.sub(r'\s+>\s+', ' → ', content)
    
    # Fix comparison operators that cause parsing issues
    content = re.sub(r'(\d+%)\s*<=\s*(\w+)\s*<=\s*(\d+%)', r'\1 ≤ \2 ≤ \3', content)
    content = re.sub(r'(\d+%)\s*<\s*(\w+)\s*<=\s*(\d+%)', r'\1 < \2 ≤ \3', content)
    
    # Fix any remaining problematic patterns
    content = re.sub(r'<>\s*([^<>]*?)\s*</>', r'', content)  # Remove empty JSX fragments
    
    # Fix unescaped single braces that aren't part of valid syntax
    content = re.sub(r'(?<!\\)\{(?![a-zA-Z_])', r'\\{', content)
    content = re.sub(r'(?<![a-zA-Z_])\}(?!\\)', r'\\}', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed: {file_path}")

def main():
    # Fix the two problematic files
    problematic_files = [
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/service-desk/index.md',
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/sso/index.md'
    ]
    
    for file_path in problematic_files:
        try:
            fix_mdx_file(file_path)
        except Exception as e:
            print(f"❌ Error fixing {file_path}: {e}")

if __name__ == "__main__":
    main()
