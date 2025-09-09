#!/usr/bin/env python3
"""
누락된 </details> 태그를 추가하는 스크립트
"""

import re
import os

def fix_details_tags(file_path):
    """
    파일에서 누락된 </details> 태그를 추가합니다.
    각 <details> 태그 다음에 나오는 다음 <details> 태그나 파일 끝 전에 </details>를 추가합니다.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    fixed_lines = []
    in_details = False
    
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        
        # <details> 태그를 찾으면
        if '<details>' in line:
            in_details = True
        
        # 다음 <details> 태그나 파일 끝을 만나면 이전 details를 닫음
        elif in_details and (i == len(lines) - 1 or 
                           (i + 1 < len(lines) and '<details>' in lines[i + 1])):
            # 현재 라인이 </details>가 아니면 추가
            if line.strip() != '</details>':
                fixed_lines.append('</details>')
            in_details = False
    
    # 마지막에 details가 열려있으면 닫기
    if in_details:
        fixed_lines.append('</details>')
    
    # 파일에 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print(f"Fixed {file_path}")

def main():
    files_to_fix = [
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/asset-management/index.md',
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/reports/index.md'
    ]
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            print(f"Processing {file_path}...")
            fix_details_tags(file_path)
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
