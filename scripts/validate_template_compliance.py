#!/usr/bin/env python3
"""
Template.md Validation Script for getting-started-with-tickets folder

This script validates that all documents in the getting-started-with-tickets folder
follow the template.md standards exactly.

Usage:
    python3 validate_template_compliance.py docs/freshservice/itsm/getting-started-with-tickets/

Validation Rules:
1. Must have sidebar_position in frontmatter
2. Must have H1 title followed by 1-2 sentence description
3. Must have :::info box after description
4. Must NOT have separate "개요" or "소개" sections
5. Must include at least one practical example
6. Must preserve all original HTML/images/tables
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Any

def validate_document(file_path: Path) -> Dict[str, Any]:
    """Validate a single document against template.md standards"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'file': file_path.name,
        'valid': True,
        'errors': [],
        'warnings': []
    }
    
    # Check 1: Frontmatter with sidebar_position
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        results['errors'].append("❌ Missing frontmatter")
        results['valid'] = False
    else:
        frontmatter = frontmatter_match.group(1)
        if 'sidebar_position:' not in frontmatter:
            results['errors'].append("❌ Missing sidebar_position in frontmatter")
            results['valid'] = False
    
    # Check 2: H1 title followed by description
    h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if not h1_match:
        results['errors'].append("❌ Missing H1 title")
        results['valid'] = False
    else:
        # Check for description after H1
        h1_pos = h1_match.end()
        next_section = content[h1_pos:h1_pos+500]  # Next 500 chars
        if not re.search(r'\n\n[^#]', next_section):
            results['errors'].append("❌ Missing 1-2 sentence description after H1")
            results['valid'] = False
    
    # Check 3: Info box presence
    if ':::info' not in content:
        results['errors'].append("❌ Missing required :::info box")
        results['valid'] = False
    
    # Check 4: Forbidden sections
    forbidden_sections = ['## 개요', '## 소개', '## Overview', '## Introduction']
    for forbidden in forbidden_sections:
        if forbidden in content:
            results['errors'].append(f"❌ Forbidden section found: {forbidden}")
            results['valid'] = False
    
    # Check 5: Practical examples
    if '실무 활용 예시' not in content and '## 실무' not in content:
        results['warnings'].append("⚠️  No practical examples found (recommended)")
    
    # Check 6: HTML preservation
    html_tags = re.findall(r'<[^>]+>', content)
    if html_tags:
        results['warnings'].append(f"📝 HTML content found: {len(html_tags)} tags (ensure preservation)")
    
    # Check 7: Image preservation
    image_links = re.findall(r'!\[.*?\]\(.*?\)', content)
    s3_images = [img for img in image_links if 's3.amazonaws.com' in img]
    if s3_images:
        results['warnings'].append(f"🖼️  AWS S3 images found: {len(s3_images)} (preserve links)")
    
    return results

def validate_folder(folder_path: Path) -> List[Dict[str, Any]]:
    """Validate all markdown files in the folder"""
    
    if not folder_path.exists():
        print(f"❌ Folder not found: {folder_path}")
        return []
    
    md_files = list(folder_path.glob("*.md"))
    # Exclude reference/template files
    md_files = [f for f in md_files if not any(exclude in f.name.lower() 
                                               for exclude in ['readme', 'template', 'example', 'sidebar-config'])]
    
    if not md_files:
        print(f"📁 No documents found in {folder_path}")
        print("   (Only .gitkeep or reference files present)")
        return []
    
    results = []
    for md_file in md_files:
        result = validate_document(md_file)
        results.append(result)
    
    return results

def print_results(results: List[Dict[str, Any]]):
    """Print validation results in a formatted way"""
    
    if not results:
        print("✅ Folder ready for documents (currently empty)")
        print("📋 Template.md compliance will be validated when documents are added")
        return
    
    total_files = len(results)
    valid_files = sum(1 for r in results if r['valid'])
    
    print(f"\n📊 Validation Summary: {valid_files}/{total_files} files compliant")
    print("=" * 60)
    
    for result in results:
        status = "✅" if result['valid'] else "❌"
        print(f"\n{status} {result['file']}")
        
        if result['errors']:
            for error in result['errors']:
                print(f"  {error}")
        
        if result['warnings']:
            for warning in result['warnings']:
                print(f"  {warning}")
    
    if valid_files == total_files:
        print(f"\n🎉 All {total_files} documents are template.md compliant!")
    else:
        invalid_count = total_files - valid_files
        print(f"\n⚠️  {invalid_count} document(s) need standardization")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_template_compliance.py <folder_path>")
        print("Example: python3 validate_template_compliance.py docs/freshservice/itsm/getting-started-with-tickets/")
        sys.exit(1)
    
    folder_path = Path(sys.argv[1])
    
    print("🔍 Template.md Compliance Validation")
    print(f"📁 Target: {folder_path}")
    print("-" * 60)
    
    results = validate_folder(folder_path)
    print_results(results)
    
    # Exit with error code if any files are invalid
    if results and not all(r['valid'] for r in results):
        sys.exit(1)

if __name__ == "__main__":
    main()