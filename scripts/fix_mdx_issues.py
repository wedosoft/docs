#!/usr/bin/env python3
"""
Fix specific MDX parsing issues in translated FAQ files.
"""

import os
import re
import glob

def fix_mdx_issues(content):
    """
    Fix specific MDX parsing issues in the content.
    """
    # Fix unescaped curly braces that are not part of JSX
    # Don't escape JSX attributes like prop={value}
    
    # First, let's handle specific problematic patterns
    
    # Fix workspace placeholder that became problematic
    content = re.sub(r'\\?\{Workspace Name\\?\}', r'{Workspace Name}', content)
    
    # Fix any broken JSX tags
    content = re.sub(r'<>\s*([^<>]*?)\s*</>', r'\\<\\>\\1\\</\\>', content)
    
    # Fix unmatched angle brackets in text
    content = re.sub(r'(?<!<)\s*<\s*(?![/\w])', r' \\< ', content)
    content = re.sub(r'(?<![/\w])\s*>\s*(?!>)', r' \\> ', content)
    
    # Escape standalone curly braces (but not JSX expressions)
    # This is more conservative - only escape obvious standalone braces
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip lines that look like JSX or markdown frontmatter
        if line.strip().startswith('---') or '<' in line and '>' in line:
            fixed_lines.append(line)
            continue
            
        # Only escape braces that are clearly standalone text
        # Look for {word} patterns that are not JSX
        line = re.sub(r'(?<![\w<])\{([^}]*)\}(?![>}])', r'\\{\1\\}', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_file(file_path):
    """
    Process a single file to fix MDX issues.
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        fixed_content = fix_mdx_issues(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ Fixed: {file_path}")
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """
    Main function to process specific problematic files.
    """
    # Focus on the files that had errors
    problem_files = [
        "/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/service-desk/index.md",
        "/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/sso/index.md"
    ]
    
    print(f"Found {len(problem_files)} problematic files to fix")
    
    for file_path in problem_files:
        if os.path.exists(file_path):
            process_file(file_path)
        else:
            print(f"File not found: {file_path}")
    
    print("\n✅ MDX issue fixing complete!")

if __name__ == "__main__":
    main()
