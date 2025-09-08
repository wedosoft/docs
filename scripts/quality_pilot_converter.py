#!/usr/bin/env python3
"""
High-Quality Pilot Converter Script - v3.0 Template Standard
기존 74개 문서 표준을 정확히 따르는 고품질 변환 시스템
"""

import csv
import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Dict, List, Any

def load_selected_samples():
    """선정된 50개 샘플 로드"""
    with open('scripts/selected_samples.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_slug(text):
    """v3.0 표준 slug 생성 (기존 74개 문서 규칙 적용)"""
    # 소문자 변환
    text = text.lower()
    # 괄호 및 특수문자 처리 
    text = re.sub(r'[()&]', '', text)
    # 특수문자를 하이픈으로 변경
    text = re.sub(r'[^a-z0-9\s-]', '-', text)
    # 공백을 하이픈으로 변경
    text = re.sub(r'\s+', '-', text)
    # 연속된 하이픈 제거
    text = re.sub(r'-+', '-', text)
    # 양쪽 하이픈 제거
    return text.strip('-')

def translate_to_korean(title):
    """제목을 한국어로 번역 (실무 중심)"""
    # 기본 번역 사전
    translations = {
        'Setting up': '설정',
        'How to': '방법',
        'Guide': '가이드',
        'Tutorial': '튜토리얼',
        'Introduction': '소개',
        'Overview': '개요',
        'Configuration': '구성',
        'Management': '관리',
        'Integration': '통합',
        'Authentication': '인증',
        'Authorization': '권한',
        'Security': '보안',
        'Policy': '정책',
        'Single Sign-On': 'SSO',
        'Password': '비밀번호',
        'Access': '접근',
        'Restriction': '제한',
        'Mailbox': '메일함',
        'Reauthorization': '재인증'
    }
    
    korean_title = title
    for en, ko in translations.items():
        korean_title = korean_title.replace(en, ko)
    
    return korean_title

def html_to_markdown(html_content):
    """HTML을 고품질 Markdown으로 변환"""
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 이미지 처리 (표준 형식)
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '이미지')
        if src:
            img.replace_with(f'\n\n![{alt}]({src})\n\n')
    
    # 링크 처리
    for link in soup.find_all('a'):
        href = link.get('href', '')
        text = link.get_text()
        if href and text:
            link.replace_with(f'[{text}]({href})')
    
    # 제목 처리
    for i in range(1, 7):
        for heading in soup.find_all(f'h{i}'):
            heading.replace_with(f'\n\n{"#" * i} {heading.get_text()}\n\n')
    
    # 리스트 처리
    for ul in soup.find_all('ul'):
        items = []
        for li in ul.find_all('li'):
            items.append(f'- {li.get_text()}')
        ul.replace_with('\n\n' + '\n'.join(items) + '\n\n')
    
    for ol in soup.find_all('ol'):
        items = []
        for i, li in enumerate(ol.find_all('li'), 1):
            items.append(f'{i}. {li.get_text()}')
        ol.replace_with('\n\n' + '\n'.join(items) + '\n\n')
    
    # 강조 처리
    for strong in soup.find_all('strong'):
        strong.replace_with(f'**{strong.get_text()}**')
    
    for em in soup.find_all('em'):
        em.replace_with(f'*{em.get_text()}*')
    
    # 표 처리 (기본 Markdown 표)
    for table in soup.find_all('table'):
        markdown_table = convert_table_to_markdown(table)
        table.replace_with(f'\n\n{markdown_table}\n\n')
    
    # 최종 텍스트 추출 및 정리
    text = soup.get_text()
    
    # 중복 줄바꿈 정리
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

def convert_table_to_markdown(table):
    """HTML 표를 Markdown 표로 변환"""
    rows = []
    
    # 헤더 처리
    thead = table.find('thead')
    if thead:
        header_row = []
        for th in thead.find_all(['th', 'td']):
            header_row.append(th.get_text().strip())
        rows.append('| ' + ' | '.join(header_row) + ' |')
        rows.append('|' + '---|' * len(header_row))
    
    # 바디 처리
    tbody = table.find('tbody') or table
    for tr in tbody.find_all('tr'):
        row_data = []
        for td in tr.find_all(['td', 'th']):
            row_data.append(td.get_text().strip())
        if row_data:
            rows.append('| ' + ' | '.join(row_data) + ' |')
    
    return '\n'.join(rows)

def create_v3_frontmatter(doc):
    """v3.0 표준 frontmatter 생성 (기존 74개 문서 표준)"""
    return f"""---
sidebar_position: {doc.get('position', 1)}
---"""

def create_korean_subtitle(doc):
    """한국어 부제목 생성"""
    category_ko = translate_to_korean(doc['category_name'])
    folder_ko = translate_to_korean(doc['folder_name'])
    
    return f"""<div class="subtitle">
  이 문서는 "{doc['title']}" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>"""

def create_related_docs_section():
    """관련 문서 섹션 (표준 형식)"""
    return """
## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [관련 문서 1](./relative-path-1)
- [관련 문서 2](./relative-path-2)
- [외부 참조](https://external-link.com)
-->"""

def convert_document_v3(doc):
    """v3.0 표준에 맞는 고품질 문서 변환"""
    
    # v3.0 frontmatter
    frontmatter = create_v3_frontmatter(doc)
    
    # 한국어 제목 (필요시)
    title_ko = translate_to_korean(doc['title'])
    
    # 부제목
    subtitle = create_korean_subtitle(doc)
    
    # 고품질 콘텐츠 변환
    content = html_to_markdown(doc['description'])
    
    # 관련 문서 섹션
    related_docs = create_related_docs_section()
    
    # v3.0 표준 구조
    markdown_content = f"""{frontmatter}

# {title_ko}

{subtitle}

{content}
{related_docs}
"""
    
    return markdown_content

def save_document_v3(doc, content):
    """v3.0 표준 경로에 문서 저장"""
    # 표준 경로 생성
    path_parts = doc['path'].strip('/').split('/')
    
    # docs/freshservice/ 기준 경로 구성
    dir_path = os.path.join('docs', 'freshservice', *path_parts[2:-1])
    os.makedirs(dir_path, exist_ok=True)
    
    # 표준 파일명
    filename = f"{create_slug(doc['title'])}.mdx"
    file_path = os.path.join(dir_path, filename)
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path

def main():
    """고품질 변환 메인 실행"""
    print("🎯 고품질 파일럿 변환 프로그램 시작 (v3.0 표준)")
    print("=" * 60)
    
    samples = load_selected_samples()
    print(f"📊 변환 대상: {len(samples)}개 문서")
    print("🔧 적용 표준: 기존 74개 문서 v3.0 템플릿")
    print()
    
    success_count = 0
    error_count = 0
    error_details = []
    
    for i, doc in enumerate(samples, 1):
        try:
            title_display = doc['title'][:45] + "..." if len(doc['title']) > 45 else doc['title']
            print(f"📝 [{i:2d}/50] {title_display}")
            
            # v3.0 표준 변환
            content = convert_document_v3(doc)
            
            # 표준 경로에 저장
            file_path = save_document_v3(doc, content)
            
            success_count += 1
            print(f"✅ 저장: {file_path}")
            print()
            
        except Exception as e:
            error_count += 1
            error_msg = f"ID {doc['id']}: {str(e)}"
            error_details.append(error_msg)
            print(f"❌ 오류: {error_msg}")
            print()
    
    print("=" * 60)
    print("📈 최종 결과")
    print(f"✅ 성공: {success_count}개")
    print(f"❌ 실패: {error_count}개")
    print(f"📊 성공률: {success_count/len(samples)*100:.1f}%")
    
    if error_details:
        print("\n🔍 오류 상세:")
        for error in error_details:
            print(f"  - {error}")
    
    if success_count == len(samples):
        print("\n🎉 모든 문서가 v3.0 표준으로 성공적으로 변환되었습니다!")
    
    print("\n🎯 고품질 변환 완료!")

if __name__ == "__main__":
    main()
