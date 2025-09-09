#!/usr/bin/env python3
"""
Fix MDX curly brace issues in translated FAQ files by escaping them.
"""

import os
import re
import glob

def fix_curly_braces(content):
    """
    Escape curly braces that are causing MDX parsing issues.
    """
    # Replace single { with \{
    content = re.sub(r'(?<!\\)\{', r'\\{', content)
    # Replace single } with \}
    content = re.sub(r'(?<!\\)\}', r'\\}', content)
    
    return content

def process_file(file_path):
    """
    Process a single file to fix curly braces.
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        fixed_content = fix_curly_braces(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ Fixed: {file_path}")
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def main():
    """
    Main function to process all FAQ files.
    """
    # Get all FAQ index.md files
    faq_pattern = "/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/*/index.md"
    faq_files = glob.glob(faq_pattern)
    
    print(f"Found {len(faq_files)} FAQ files to process")
    
    for file_path in faq_files:
        process_file(file_path)
    
    print("\n✅ Curly brace fixing complete!")

if __name__ == "__main__":
    main()
