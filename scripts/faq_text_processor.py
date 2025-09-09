#!/usr/bin/env python3
"""
FAQ 텍스트 전용 문서 배치 처리 (Markdown 생성)
- 순수 텍스트 FAQ를 .md 파일로 생성
- 복잡한 컴포넌트 없이 간단한 마크다운 구조
- 빠른 렌더링과 편집 용이성 확보
"""

import pandas as pd
import json
import os
import re
from pathlib import Path
from datetime import datetime

def clean_html_content(content):
    """HTML 태그 제거 및 마크다운 변환"""
    if not content or pd.isna(content):
        return ""
    
    # HTML 태그 제거
    content = re.sub(r'<[^>]+>', '', str(content))
    
    # HTML 엔티티 변환
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")
    content = content.replace('&nbsp;', ' ')
    
    # 연속된 공백 정리
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()
    
    return content

def create_markdown_slug(title):
    """제목을 마크다운 파일명으로 변환"""
    if not title:
        return "untitled"
    
    # 특수문자 제거 및 소문자 변환
    slug = re.sub(r'[^\w\s-]', '', str(title).lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    slug = slug.strip('-')
    
    # 길이 제한 (50자)
    if len(slug) > 50:
        slug = slug[:50].rstrip('-')
    
    return slug or "untitled"

def generate_markdown_content(faq_item):
    """FAQ 아이템을 마크다운 콘텐츠로 변환"""
    
    title = clean_html_content(faq_item.get('title', ''))
    description = clean_html_content(faq_item.get('description', ''))
    
    # 메타데이터 설정
    metadata = f"""---
title: {title}
sidebar_position: {faq_item.get('position', 1)}
tags:
  - FAQ
  - {faq_item.get('folder_name', 'General')}
---

"""
    
    # 본문 내용
    content = f"""# {title}

{description}

---

*이 문서는 Freshservice FAQ에서 자동 생성되었습니다.*
"""
    
    return metadata + content

def process_text_only_faqs():
    """텍스트 전용 FAQ 처리"""
    
    # 복잡도 분석 결과 로드
    with open('faq_simple_analysis.json', 'r') as f:
        complexity_data = json.load(f)
    
    # 텍스트 전용 문서만 필터링
    text_only_faqs = [item for item in complexity_data 
                      if item['processing_recommendation'] == 'AUTO']
    
    print(f"🚀 텍스트 전용 FAQ 배치 처리 시작")
    print(f"📊 처리 대상: {len(text_only_faqs)}개 문서")
    print("=" * 60)
    
    processed_count = 0
    folders_created = set()
    
    for faq in text_only_faqs:
        try:
            # 폴더 slug 생성
            folder_name = faq['folder_name']
            folder_slug = create_faq_slug(folder_name)
            
            # 폴더 경로 설정
            folder_path = Path(f'docs/freshworks/freshservice/faqs/{folder_slug}')
            folder_path.mkdir(parents=True, exist_ok=True)
            
            if folder_slug not in folders_created:
                folders_created.add(folder_slug)
                print(f"📁 {folder_name} → {folder_slug}")
            
            # 파일명 생성
            title_slug = create_markdown_slug(faq.get('title', ''))
            filename = f"{title_slug}.md"
            file_path = folder_path / filename
            
            # 마크다운 콘텐츠 생성
            markdown_content = generate_markdown_content(faq)
            
            # 파일 생성
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            processed_count += 1
            
            if processed_count % 50 == 0:
                print(f"⚡ {processed_count}개 처리 완료...")
        
        except Exception as e:
            print(f"❌ 오류 - {faq.get('title', 'Unknown')}: {e}")
    
    return processed_count, folders_created

def create_faq_slug(folder_name):
    """지침서 규칙에 따른 FAQ 폴더 slug 생성"""
    slug_map = {
        'API & Webhooks': 'api-webhooks',
        'Affliate Marketing': 'affiliate-marketing', 
        'Agents and Groups': 'agents-groups',
        'Analytics FAQs': 'analytics',
        'Announcements': 'announcements',
        'Asset Management': 'asset-management',
        'Automations and Triggers': 'automations-triggers',
        'Business Hours and SLAs': 'business-hours-slas',
        'Changes': 'changes',
        'Email': 'email',
        'Email Notifications': 'email-notifications',
        'Feedback Widget': 'feedback-widget',
        'Gamification and Arcade': 'gamification-arcade',
        'Incidents & Service Request': 'incidents-service-request',
        'New-Gen Project Mgmt': 'project-management',
        'Orchestration': 'orchestration',
        'Pricing FAQ': 'pricing',
        'Priority Matrix': 'priority-matrix',
        'Problem': 'problems',
        'Release': 'releases',
        'Reports': 'reports',
        'SSO': 'sso',
        'Sandbox': 'sandbox',
        'Service Catalog': 'service-catalog',
        'Service Desk FAQ': 'service-desk',
        'Tasks': 'tasks',
        'Ticketing Workflow': 'ticketing-workflow',
        'Workspaces': 'workspaces'
    }
    
    return slug_map.get(folder_name, folder_name.lower().replace(' ', '-').replace('&', 'and'))

def create_folder_index_files(folders_created):
    """각 폴더에 index.md 파일 생성"""
    
    print(f"\n📋 폴더별 index.md 파일 생성")
    print("-" * 40)
    
    for folder_slug in folders_created:
        folder_path = Path(f'docs/freshworks/freshservice/faqs/{folder_slug}')
        index_path = folder_path / 'index.md'
        
        # 폴더명을 제목으로 변환
        folder_title = folder_slug.replace('-', ' ').title()
        
        index_content = f"""---
title: {folder_title} FAQs
sidebar_position: 1
---

# {folder_title} FAQs

이 섹션에서는 {folder_title}와 관련된 자주 묻는 질문들을 다룹니다.

---

*이 문서는 Freshservice FAQ에서 자동 생성되었습니다.*
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"✅ {folder_slug}/index.md")
    
    return len(folders_created)

if __name__ == "__main__":
    print("🔍 FAQ 텍스트 전용 배치 처리 시작...")
    
    try:
        # 1. 텍스트 전용 FAQ 처리
        processed_count, folders_created = process_text_only_faqs()
        
        # 2. 폴더별 index.md 생성
        index_count = create_folder_index_files(folders_created)
        
        print(f"\n✅ 텍스트 전용 FAQ 배치 완료!")
        print(f"📊 처리된 문서: {processed_count}개")
        print(f"📁 생성된 폴더: {len(folders_created)}개")
        print(f"📋 index.md 파일: {index_count}개")
        
        print(f"\n🎯 다음 단계:")
        print(f"1. 생성된 .md 파일들 확인")
        print(f"2. sidebars.ts 설정 추가")
        print(f"3. 복합 요소 문서 수동 처리")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
