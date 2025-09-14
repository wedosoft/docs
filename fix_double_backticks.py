#!/usr/bin/env python3

import re

def fix_double_backticks_in_file(file_path):
    """Fix double backticks in JSX style attributes in the given file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace style=``{{...}}`` with style={{...}}
    pattern = r'style=``(\{\{[^}]+\}\})``'
    replacement = r'style=\1'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed double backticks in {file_path}")
        return True
    return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fix_double_backticks.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    fix_double_backticks_in_file(file_path)