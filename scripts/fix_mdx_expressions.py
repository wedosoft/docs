#!/usr/bin/env python3
"""
Fix MDX expression parsing errors in translated FAQ files.
Escapes curly braces that are not intended as MDX expressions.
"""

import os
import re
import glob

def fix_mdx_expressions(content):
    """
    Fix MDX expression parsing errors by escaping problematic curly braces.
    """
    # Pattern to find curly braces that are not part of JSX or valid MDX expressions
    # This will escape single curly braces that are not part of JSX components
    
    # First, protect valid JSX components and expressions
    # Look for patterns like {variableName}, {/* comment */}, etc.
    protected_patterns = []
    
    # Find JSX components (like <Component prop={value}>)
    jsx_pattern = r'<[^>]*\{[^}]*\}[^>]*>'
    jsx_matches = re.finditer(jsx_pattern, content)
    for match in jsx_matches:
        protected_patterns.append((match.start(), match.end()))
    
    # Find valid MDX expressions (like {variableName})
    mdx_expr_pattern = r'\{[a-zA-Z_][a-zA-Z0-9_]*\}'
    mdx_matches = re.finditer(mdx_expr_pattern, content)
    for match in mdx_matches:
        # Check if this is not already protected
        start, end = match.span()
        is_protected = any(p_start <= start and end <= p_end for p_start, p_end in protected_patterns)
        if not is_protected:
            protected_patterns.append((start, end))
    
    # Sort protected patterns by start position
    protected_patterns.sort()
    
    # Now escape single curly braces that are not protected
    result = []
    last_pos = 0
    
    for start, end in protected_patterns:
        # Process text before this protected pattern
        before_text = content[last_pos:start]
        result.append(escape_single_braces(before_text))
        
        # Add the protected pattern as-is
        result.append(content[start:end])
        last_pos = end
    
    # Process remaining text
    remaining_text = content[last_pos:]
    result.append(escape_single_braces(remaining_text))
    
    return ''.join(result)

def escape_single_braces(text):
    """
    Escape single curly braces in text that are not part of pairs.
    """
    # Replace single { with \{
    text = re.sub(r'(?<!\\)\{(?![^}]*\})', r'\\{', text)
    # Replace single } with \}
    text = re.sub(r'(?<!\\)\}(?<!\{[^{]*)', r'\\}', text)
    return text

def process_faq_file(file_path):
    """
    Process a single FAQ file to fix MDX expressions.
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        fixed_content = fix_mdx_expressions(content)
        
        # Only write if content changed
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"✅ Fixed: {file_path}")
        else:
            print(f"⚪ No changes: {file_path}")
            
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
        process_faq_file(file_path)
    
    print("\n✅ MDX expression fixing complete!")

if __name__ == "__main__":
    main()
