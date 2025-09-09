#!/usr/bin/env python3
"""
FAQ 아코디언 통합 처리
- 각 폴더별로 모든 FAQ를 index.md에 통합
- HTML details/summary 아코디언 구조 생성
- 개별 .md 파일들 정리
"""

import pandas as pd
import json
import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

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

def group_faqs_by_folder():
    """폴더별로 FAQ 그룹화"""
    
    with open('faq_simple_analysis.json', 'r') as f:
        complexity_data = json.load(f)
    
    folders_faqs = defaultdict(list)
    
    for faq in complexity_data:
        folder_name = faq['folder_name']
        folder_slug = create_faq_slug(folder_name)
        
        # 텍스트 전용과 복합 요소 모두 포함
        folders_faqs[folder_slug].append({
            'original_folder': folder_name,
            'title': clean_html_content(faq.get('title', '')),
            'description': clean_html_content(faq.get('description', '')),
            'position': faq.get('position', 1),
            'complexity': faq.get('processing_recommendation', 'MANUAL'),
            'url': faq.get('url', ''),
            'folder_slug': folder_slug
        })
    
    # position으로 정렬
    for folder_slug in folders_faqs:
        folders_faqs[folder_slug].sort(key=lambda x: x['position'])
    
    return dict(folders_faqs)

def create_accordion_content(folder_slug, faqs):
    """폴더별 아코디언 통합 콘텐츠 생성"""
    
    if not faqs:
        return ""
    
    folder_title = faqs[0]['original_folder']
    text_count = sum(1 for faq in faqs if faq['complexity'] == 'AUTO')
    complex_count = sum(1 for faq in faqs if faq['complexity'] == 'MANUAL')
    
    # 메타데이터
    metadata = f"""---
title: {folder_title} FAQs
sidebar_position: 1
---

# {folder_title} FAQs

{folder_title}와 관련된 자주 묻는 질문들입니다.

:::info 처리 현황
📊 **총 {len(faqs)}개 FAQ**  
✅ 자동 처리: {text_count}개  
🔧 수동 처리: {complex_count}개  
:::

---

"""
    
    # 아코디언 FAQ 생성
    accordion_content = ""
    
    for i, faq in enumerate(faqs, 1):
        title = faq['title']
        description = faq['description']
        complexity_badge = "🟢 AUTO" if faq['complexity'] == 'AUTO' else "🔧 MANUAL"
        
        # description이 비어있으면 처리 필요 표시
        if not description:
            description = "*⚠️ 이 FAQ는 추가 처리가 필요합니다.*"
        
        accordion_item = f"""<details>
<summary><strong>{i}. {title}</strong> <small>({complexity_badge})</small></summary>

{description}

</details>

"""
        accordion_content += accordion_item
    
    # 푸터
    footer = f"""---

:::tip 추가 도움이 필요하신가요?
- 🔗 [Freshservice 지원 센터](https://support.freshworks.com/en/support/solutions/folders/50000683746)
- 📧 [고객 지원팀 문의](mailto:support@wedosoft.net)
:::

*이 문서는 Freshservice FAQ에서 자동 생성되었습니다. 마지막 업데이트: {pd.Timestamp.now().strftime('%Y-%m-%d')}*
"""
    
    return metadata + accordion_content + footer

def clean_existing_files():
    """기존 개별 FAQ 파일들 정리"""
    
    base_path = Path('docs/freshworks/freshservice/faqs')
    cleaned_count = 0
    
    print("🧹 기존 개별 FAQ 파일들 정리...")
    
    for folder_path in base_path.iterdir():
        if folder_path.is_dir():
            for file_path in folder_path.iterdir():
                if file_path.name != 'index.md' and file_path.suffix == '.md':
                    print(f"🗑️  삭제: {file_path}")
                    file_path.unlink()
                    cleaned_count += 1
    
    return cleaned_count

def process_accordion_integration():
    """아코디언 통합 처리 실행"""
    
    print("🎯 FAQ 아코디언 통합 처리 시작")
    print("=" * 60)
    
    # 1. 기존 파일 정리
    cleaned_count = clean_existing_files()
    print(f"✅ 정리된 파일: {cleaned_count}개\n")
    
    # 2. 폴더별 FAQ 그룹화
    folders_faqs = group_faqs_by_folder()
    
    # 3. 통합 index.md 생성
    processed_folders = 0
    total_faqs = 0
    
    for folder_slug, faqs in folders_faqs.items():
        folder_path = Path(f'docs/freshworks/freshservice/faqs/{folder_slug}')
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # 아코디언 콘텐츠 생성
        accordion_content = create_accordion_content(folder_slug, faqs)
        
        # index.md 파일 생성
        index_path = folder_path / 'index.md'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(accordion_content)
        
        folder_title = faqs[0]['original_folder']
        text_count = sum(1 for faq in faqs if faq['complexity'] == 'AUTO')
        complex_count = sum(1 for faq in faqs if faq['complexity'] == 'MANUAL')
        
        print(f"📁 {folder_title} → {folder_slug}")
        print(f"   🎯 {len(faqs)}개 FAQ 통합 (텍스트: {text_count}, 복합: {complex_count})")
        
        processed_folders += 1
        total_faqs += len(faqs)
    
    return processed_folders, total_faqs

if __name__ == "__main__":
    print("🔄 FAQ 아코디언 통합 처리 시작...")
    
    try:
        processed_folders, total_faqs = process_accordion_integration()
        
        print(f"\n✅ 아코디언 통합 완료!")
        print(f"📁 처리된 폴더: {processed_folders}개")
        print(f"📊 통합된 FAQ: {total_faqs}개")
        
        print(f"\n🎯 결과:")
        print(f"✅ 각 폴더별 index.md에 모든 FAQ 아코디언 통합")
        print(f"✅ HTML details/summary 아코디언 구조")
        print(f"✅ 자동/수동 처리 구분 표시")
        print(f"✅ 개별 .md 파일 정리 완료")
        
        print(f"\n🚀 다음 단계:")
        print(f"1. Docusaurus 빌드 테스트")
        print(f"2. 아코디언 UI 확인")
        print(f"3. sidebars.ts 설정 추가")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
