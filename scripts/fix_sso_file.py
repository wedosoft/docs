#!/usr/bin/env python3
"""
Fix the specific Org<>SSO issue in SSO file.
"""

def fix_sso_file():
    file_path = '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/sso/index.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the specific problematic pattern
    content = content.replace('Org<>SSO', 'Org-SSO')
    content = content.replace('<>', '')  # Remove any empty JSX fragments
    
    # Fix any remaining angle bracket issues
    content = content.replace('< >', '')
    content = content.replace('</ >', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed SSO file")

if __name__ == "__main__":
    fix_sso_file()
