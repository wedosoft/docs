#!/usr/bin/env python3
"""
문서 스타일 통일 스크립트
- <div class="subtitle"> 스타일을 :::info 문서 목적 callout으로 변경
- 일관된 문서 구조 적용
"""

import os
import re
import glob

def convert_subtitle_to_callout(content):
    """
    <div class="subtitle"> 스타일을 :::info callout으로 변환
    """
    # subtitle div 패턴 찾기
    pattern = r'<div class="subtitle">\s*(.+?)\s*</div>'
    
    def replacement(match):
        subtitle_text = match.group(1).strip()
        return f':::info 문서 목적\n{subtitle_text}\n:::'
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def process_markdown_file(file_path):
    """
    개별 마크다운 파일 처리
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # subtitle 변환
        content = convert_subtitle_to_callout(content)
        
        # 변경사항이 있는 경우에만 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 변환 완료: {file_path}")
            return True
        else:
            print(f"⏭️  변경사항 없음: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 오류 발생 {file_path}: {e}")
        return False

def main():
    """
    메인 실행 함수
    """
    # docs 디렉토리의 모든 .md 파일 찾기
    docs_pattern = "/Users/alan/GitHub/docs/docs/**/*.md"
    md_files = glob.glob(docs_pattern, recursive=True)
    
    # tutorial 파일들 제외 (기본 Docusaurus 파일들)
    md_files = [f for f in md_files if '/tutorial-' not in f]
    
    print(f"🔍 총 {len(md_files)}개의 마크다운 파일 발견")
    
    converted_count = 0
    total_count = len(md_files)
    
    for file_path in md_files:
        if process_markdown_file(file_path):
            converted_count += 1
    
    print(f"\n📊 변환 완료:")
    print(f"   - 총 파일 수: {total_count}")
    print(f"   - 변환된 파일: {converted_count}")
    print(f"   - 변경사항 없음: {total_count - converted_count}")

if __name__ == "__main__":
    main()
