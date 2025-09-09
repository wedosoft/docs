#!/usr/bin/env python3
"""
Fix all MDX parsing issues by cleaning up problematic characters.
"""

import os
import re
import glob

def clean_mdx_content(content):
    """
    Clean up content to fix MDX parsing issues.
    """
    # Replace problematic patterns
    
    # Fix workspace name placeholders
    content = re.sub(r'\\?\{Workspace Name\\?\}', r'[Workspace Name]', content)
    
    # Replace angle brackets with arrows for navigation paths
    content = re.sub(r'\s+>\s+', r' → ', content)
    
    # Fix any remaining unescaped braces that aren't JSX
    # This is very conservative - only fixes obvious issues
    content = re.sub(r'(?<!\\)\{(?![a-zA-Z_])', r'\\{', content)
    content = re.sub(r'(?<![a-zA-Z_])\}(?!\\)', r'\\}', content)
    
    # Fix comparison operators that might confuse parser
    content = re.sub(r'(\d+%)\s*<=\s*(\w+)\s*<=\s*(\d+%)', r'\1 ≤ \2 ≤ \3', content)
    content = re.sub(r'(\d+%)\s*<\s*(\w+)\s*<=\s*(\d+%)', r'\1 < \2 ≤ \3', content)
    
    # Clean up any malformed HTML tags
    content = re.sub(r'<>\s*([^<>]*?)\s*</>', r'\\<\\>\1\\</\\>', content)
    
    return content

def process_file(file_path):
    """
    Process a single file to fix MDX issues.
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        fixed_content = clean_mdx_content(content)
        
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
    
    print("\n✅ MDX content cleaning complete!")

if __name__ == "__main__":
    main()
