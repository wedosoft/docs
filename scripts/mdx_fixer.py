#!/usr/bin/env python3
"""
Freshservice 문서 MDX 호환성 자동 처리 스크립트

이 스크립트는 Freshservice CSV에서 변환된 Markdown 문서의
MDX 호환성 문제를 자동으로 해결합니다.

주요 처리 내용:
1. Freshservice placeholder {ticket.id} → `{ticket.id}` (인라인 코드)
2. 일반 중괄호 {워크스페이스명} → &#123;워크스페이스명&#125; (이스케이프)
3. style="..." → style={{...}} (JSX 스타일 변환)

사용법:
    python3 mdx_fixer.py [폴더경로]
    
예시:
    python3 mdx_fixer.py docs/freshworks/freshservice/
"""

import os
import re
import sys

# Freshservice placeholder 패턴들
FRESHSERVICE_PLACEHOLDERS = [
    r'\{ticket\.id\}',
    r'\{ticket\.number\}', 
    r'\{ticket\.subject\}',
    r'\{ticket\.description\}',
    r'\{ticket\.priority\}',
    r'\{ticket\.status\}',
    r'\{ticket\.category\}',
    r'\{ticket\.subcategory\}',
    r'\{ticket\.department\}',
    r'\{ticket\.group\}',
    r'\{ticket\.agent\}',
    r'\{requester\.name\}',
    r'\{requester\.email\}',
    r'\{requester\.phone\}',
    r'\{agent\.name\}',
    r'\{agent\.email\}',
    r'\{company\.name\}',
    r'\{company\.domain\}',
    r'\{asset\.name\}',
    r'\{asset\.tag\}',
    r'\{workspace\.name\}',
    r'\{workspace\.domain\}',
    r'\{solution\.title\}',
    r'\{solution\.description\}',
]

def fix_freshservice_placeholders(content):
    """Freshservice placeholder를 인라인 코드로 변환"""
    for pattern in FRESHSERVICE_PLACEHOLDERS:
        # {placeholder} → `{placeholder}`
        content = re.sub(pattern, lambda m: f'`{m.group()}`', content)
    
    return content

def fix_korean_braces(content):
    """한글이 포함된 중괄호를 이스케이프 처리"""
    def replace_korean_brace(match):
        full_match = match.group()
        inner = full_match[1:-1]  # 중괄호 제거
        
        # 이미 처리된 것들 건너뛰기
        if '&#123;' in full_match or full_match.startswith('`{'):
            return full_match
        
        # 한글이 포함된 경우만 이스케이프
        if re.search(r'[가-힣]', inner):
            return f'&#123;{inner}&#125;'
        
        return full_match
    
    # 백틱으로 감싸지지 않은 중괄호만 처리
    pattern = r'(?<!`)\{[^}]*\}(?!`)'
    return re.sub(pattern, replace_korean_brace, content)

def fix_style_attributes(content):
    """HTML style 속성을 JSX 형식으로 변환"""
    # style="color: red" → style={{color: 'red'}}
    def convert_style(match):
        style_content = match.group(1)
        # 간단한 변환 (복잡한 경우는 수동 처리 필요)
        jsx_style = style_content.replace('"', "'")
        return f"style={{{jsx_style}}}"
    
    pattern = r'style="([^"]*)"'
    return re.sub(pattern, convert_style, content)

def fix_subtitle_format(content):
    """subtitle div를 info 블록으로 변환"""
    # <div class="subtitle"> 패턴을 :::info 문서 목적으로 변환
    pattern = r'<div class="subtitle">\s*([^<]+)\s*</div>'
    
    def replace_subtitle(match):
        text_content = match.group(1).strip()
        # 앞뒤 공백과 줄바꿈 정리
        text_content = re.sub(r'\s+', ' ', text_content)
        return f':::info 문서 목적\n{text_content}\n:::'
    
    return re.sub(pattern, replace_subtitle, content, flags=re.DOTALL)

def process_file(file_path):
    """파일 처리"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        
        # 1. Freshservice placeholder 처리
        new_content = fix_freshservice_placeholders(content)
        if new_content != content:
            changes.append("Freshservice placeholder → 인라인 코드")
            content = new_content
        
        # 2. 한글 중괄호 이스케이프
        new_content = fix_korean_braces(content)
        if new_content != content:
            changes.append("한글 중괄호 → 이스케이프")
            content = new_content
        
        # 3. Style 속성 변환
        new_content = fix_style_attributes(content)
        if new_content != content:
            changes.append("HTML style → JSX style")
            content = new_content
        
        # 4. Subtitle div 변환
        new_content = fix_subtitle_format(content)
        if new_content != content:
            changes.append("subtitle div → info 블록")
            content = new_content
        
        # 변경사항이 있으면 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return []
        
    except Exception as e:
        print(f"오류 발생 ({file_path}): {e}")
        return []

def main():
    """메인 함수"""
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "docs/freshworks/freshservice/"
    
    if not os.path.exists(target_path):
        print(f"경로가 존재하지 않습니다: {target_path}")
        sys.exit(1)
    
    print("=== Freshservice 문서 MDX 호환성 자동 처리 ===")
    print(f"대상 경로: {target_path}")
    print()
    
    total_files = 0
    fixed_files = 0
    all_changes = []
    
    # 단일 파일인지 폴더인지 확인
    if os.path.isfile(target_path) and target_path.endswith('.md'):
        # 단일 파일 처리
        total_files = 1
        changes = process_file(target_path)
        if changes:
            fixed_files = 1
            print(f"✅ {os.path.relpath(target_path)}")
            for change in changes:
                print(f"   - {change}")
            all_changes.extend(changes)
        else:
            print(f"✓ {os.path.relpath(target_path)} (변경사항 없음)")
    else:
        # 폴더 처리
        for root, dirs, files in os.walk(target_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    total_files += 1
                    
                    changes = process_file(file_path)
                    if changes:
                        fixed_files += 1
                        print(f"✅ {os.path.relpath(file_path)}")
                        for change in changes:
                            print(f"   - {change}")
                        all_changes.extend(changes)
                    else:
                        print(f"✓ {os.path.relpath(file_path)} (변경사항 없음)")
    
    print()
    print("=== 처리 완료 ===")
    print(f"전체 파일: {total_files}개")
    print(f"수정된 파일: {fixed_files}개")
    
    if all_changes:
        print("\n수행된 작업:")
        for change_type in set(all_changes):
            count = all_changes.count(change_type)
            print(f"- {change_type}: {count}건")

if __name__ == "__main__":
    main()
