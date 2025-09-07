#!/usr/bin/env python3
"""
문서 제목 다음 부분 서식 통일 스크립트

<div class="subtitle"> 형태를 :::info 문서 목적 형태로 변환합니다.

사용법: python3 fix_subtitle_format.py [폴더경로]
"""

import os
import re
import sys

def fix_subtitle_format(content):
    """subtitle div를 info 블록으로 변환"""
    
    # <div class="subtitle"> 패턴을 :::info 문서 목적으로 변환
    pattern = r'<div class="subtitle">\s*([^<]+)\s*</div>'
    
    def replace_subtitle(match):
        text_content = match.group(1).strip()
        # 앞뒤 공백과 줄바꿈 정리
        text_content = re.sub(r'\s+', ' ', text_content)
        return f':::info 문서 목적\n{text_content}\n:::'
    
    new_content = re.sub(pattern, replace_subtitle, content, flags=re.DOTALL)
    
    return new_content

def process_file(file_path):
    """파일 처리"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # subtitle div가 있는지 확인
        if 'class="subtitle"' not in content:
            return False
        
        new_content = fix_subtitle_format(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"오류 발생 ({file_path}): {e}")
        return False

def main():
    """메인 함수"""
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "docs/freshworks/freshservice/"
    
    if not os.path.exists(target_path):
        print(f"경로가 존재하지 않습니다: {target_path}")
        sys.exit(1)
    
    print("=== 문서 제목 서식 통일 처리 ===")
    print(f"대상 경로: {target_path}")
    print("변환: <div class=\"subtitle\"> → :::info 문서 목적")
    print()
    
    total_files = 0
    fixed_files = 0
    
    # 단일 파일인지 폴더인지 확인
    if os.path.isfile(target_path) and target_path.endswith('.md'):
        total_files = 1
        if process_file(target_path):
            fixed_files = 1
            print(f"✅ {os.path.relpath(target_path)}")
        else:
            print(f"✓ {os.path.relpath(target_path)} (변경사항 없음)")
    else:
        # 폴더 처리
        for root, dirs, files in os.walk(target_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    total_files += 1
                    
                    if process_file(file_path):
                        fixed_files += 1
                        print(f"✅ {os.path.relpath(file_path)}")
                    else:
                        print(f"✓ {os.path.relpath(file_path)} (변경사항 없음)")
    
    print()
    print("=== 처리 완료 ===")
    print(f"전체 파일: {total_files}개")
    print(f"수정된 파일: {fixed_files}개")

if __name__ == "__main__":
    main()
