#!/usr/bin/env python3
"""
파일 끝의 불필요한 문자들을 제거하고 올바른 형식으로 정리하는 스크립트
"""

import re
import os

def cleanup_file_ending(file_path):
    """
    파일 끝을 정리합니다.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 불필요한 문자들 제거
    content = re.sub(r'[^\w\s\n<>/.-]+', '', content)
    
    # 파일이 </details>로 끝나도록 정리
    content = content.strip()
    if not content.endswith('</details>'):
        content += '\n</details>'
    
    # 다시 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned up {file_path}")

def main():
    files_to_clean = [
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/asset-management/index.md',
        '/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/reports/index.md'
    ]
    
    for file_path in files_to_clean:
        if os.path.exists(file_path):
            print(f"Cleaning {file_path}...")
            cleanup_file_ending(file_path)
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
