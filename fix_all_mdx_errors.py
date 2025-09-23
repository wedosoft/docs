#!/usr/bin/env python3
"""
Comprehensive MDX error fixer for all Freshdesk FAQ files
"""

import os
import re
import glob

def fix_mdx_errors(content):
    """Fix various MDX compatibility issues"""
    
    # 1. Fix complex brace expressions that cause acorn parsing errors
    # Replace {{#123;`{{#123;...}}`#125;}}`#125;` patterns
    content = re.sub(r'`{{#123;`{{#123;([^}]+)}}`#125;}}`#125;`', r'`\1`', content)
    content = re.sub(r'{{#123;`{{#123;([^}]+)}}`#125;}}`#125;', r'`\1`', content)
    
    # 2. Fix JSON objects in paragraph tags
    def fix_json_in_p_tags(match):
        json_content = match.group(1)
        return f'<code>{json_content}</code>'
    
    content = re.sub(r'<span[^>]*>\s*(\{[^}]+\})\s*</span>', fix_json_in_p_tags, content)
    
    # 3. Fix broken HTML structure in code blocks
    # Fix p tags inside script tags
    content = re.sub(r'<script>([^<]+)<p><span[^>]*>([^<]+)</span></p><p><span[^>]*>([^<]+)</span></p></script>', 
                     r'<script>\n\1\n\2\n\3\n</script>', content)
    
    # 4. Fix nested span tag issues
    # Remove unnecessary nested spans with same styles
    content = re.sub(r'<span style=\{\{ fontSize: "16px" \}\}><span style=\{\{ fontSize: "16px" \}\}><span style=\{\{ fontSize: "16px" \}\}>([^<]+)</span></span></span>', 
                     r'<span style={{ fontSize: "16px" }}>\1</span>', content)
    
    # 5. Fix broken details tags structure
    # Ensure proper details tag closure
    content = re.sub(r'(<details>\s*<summary>[^<]+</summary>\s*.*?)</details>\s*(<details>)', 
                     r'\1</details>\n\n\2', content, flags=re.DOTALL)
    
    # 6. Fix broken div tag structures
    # Close unclosed div tags before paragraph ends
    lines = content.split('\n')
    fixed_lines = []
    div_stack = []
    
    for line in lines:
        # Track div tags
        div_opens = re.findall(r'<div[^>]*>', line)
        div_closes = re.findall(r'</div>', line)
        
        for div_open in div_opens:
            div_stack.append('div')
        
        for div_close in div_closes:
            if div_stack and div_stack[-1] == 'div':
                div_stack.pop()
        
        # If we're at end of a paragraph and have unclosed divs, close them
        if line.strip() == '' and div_stack:
            while div_stack and div_stack[-1] == 'div':
                fixed_lines.append('</div>')
                div_stack.pop()
        
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # 7. Fix specific problematic patterns
    # Fix malformed code blocks
    content = re.sub(r'```html\s*<script>[^<]*<p><span[^>]*>([^<]+)</span></p><p><span[^>]*>([^<]+)</span></p></script>\s*```',
                     r'```html\n<script>\n\1\n\2\n</script>\n```', content)
    
    # 8. Fix broken attribute quotes
    content = re.sub(r'(\w+)=[""]([^"]+)[""]', r'\1="\2"', content)
    
    # 9. Escape JavaScript expressions in text
    # Convert {code} to `code` when it's clearly meant to be code
    content = re.sub(r'(\s|>)\{([^}]+)\}(\s|<)', r'\1`\2`\3', content)
    
    return content

def process_file(filepath):
    """Process a single MDX file"""
    print(f"Processing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixed_content = fix_mdx_errors(content)
        
        if fixed_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"  ✅ Fixed: {filepath}")
            return True
        else:
            print(f"  ⏭️  No changes needed: {filepath}")
            return False
            
    except Exception as e:
        print(f"  ❌ Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all problematic files"""
    files_to_fix = [
        'docs/freshdesk/faq/analytics/index.md',
        'docs/freshdesk/faq/api-webhooks/index.md', 
        'docs/freshdesk/faq/integrations/index.md',
        'docs/freshdesk/faq/mobile-apps/index.md',
        'docs/freshdesk/faq/multiple-products/index.md',
        'docs/freshdesk/faq/self-service-portal/index.md',
        'docs/freshdesk/faq/ssl-security/index.md',
        'docs/freshdesk/faq/ticketing-workflow/index.md'
    ]
    
    print("🔧 Starting comprehensive MDX error fixing...")
    
    fixed_count = 0
    for filepath in files_to_fix:
        if os.path.exists(filepath):
            if process_file(filepath):
                fixed_count += 1
        else:
            print(f"  ⚠️  File not found: {filepath}")
    
    print(f"\n🎉 Completed! Fixed {fixed_count} files.")

if __name__ == "__main__":
    main()