#!/usr/bin/env python3
"""
FAQ 아코디언 최종 통합 처리 (한국어화 포함)
- 모든 FAQ를 폴더별 아코디언으로 통합
- 한국어 제목 및 구조 적용
- 깔끔한 front matter 구조
"""

import pandas as pd
import json
import os
import re
from pathlib import Path
from collections import defaultdict

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

def get_korean_title(folder_slug):
    """폴더 slug에 대한 한국어 제목 반환"""
    korean_titles = {
        'affiliate-marketing': 'Affiliate 마케팅',
        'agents-groups': '에이전트 및 그룹',
        'analytics': '분석 및 리포트',
        'announcements': '공지사항',
        'api-webhooks': 'API 및 웹훅',
        'asset-management': '자산 관리',
        'automations-triggers': '자동화 및 트리거',
        'business-hours-slas': '업무시간 및 SLA',
        'changes': '변경 관리',
        'email': '이메일',
        'email-notifications': '이메일 알림',
        'feedback-widget': '피드백 위젯',
        'gamification-arcade': '게임화 및 아케이드',
        'incidents-service-request': '인시던트 및 서비스 요청',
        'orchestration': '오케스트레이션',
        'pricing': '가격 정책',
        'priority-matrix': '우선순위 매트릭스',
        'problems': '문제 관리',
        'project-management': '프로젝트 관리',
        'releases': '릴리스 관리',
        'reports': '리포트',
        'sandbox': '샌드박스',
        'service-catalog': '서비스 카탈로그',
        'service-desk': '서비스 데스크',
        'sso': 'SSO (Single Sign-On)',
        'tasks': '작업 관리',
        'ticketing-workflow': '티켓 워크플로우',
        'workspaces': '워크스페이스'
    }
    
    return korean_titles.get(folder_slug, folder_slug.replace('-', ' ').title())

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

def create_final_accordion_content(folder_slug, faqs):
    """최종 아코디언 통합 콘텐츠 생성 (한국어화 포함)"""
    
    if not faqs:
        return ""
    
    korean_title = get_korean_title(folder_slug)
    text_count = sum(1 for faq in faqs if faq['complexity'] == 'AUTO')
    complex_count = sum(1 for faq in faqs if faq['complexity'] == 'MANUAL')
    
    # 메타데이터 (깔끔한 YAML)
    metadata = f"""---
title: "{korean_title} FAQ"
sidebar_position: 1
---

# {korean_title} FAQ

{korean_title}와 관련된 자주 묻는 질문들입니다.

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

def process_final_accordion():
    """최종 아코디언 통합 처리 실행"""
    
    print("🌏 FAQ 최종 아코디언 통합 (한국어화)")
    print("=" * 60)
    
    # 1. 폴더별 FAQ 그룹화
    folders_faqs = group_faqs_by_folder()
    
    # 2. 최종 index.md 생성
    processed_folders = 0
    total_faqs = 0
    
    for folder_slug, faqs in folders_faqs.items():
        folder_path = Path(f'docs/freshworks/freshservice/faqs/{folder_slug}')
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # 최종 아코디언 콘텐츠 생성
        final_content = create_final_accordion_content(folder_slug, faqs)
        
        # index.md 파일 생성
        index_path = folder_path / 'index.md'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        korean_title = get_korean_title(folder_slug)
        text_count = sum(1 for faq in faqs if faq['complexity'] == 'AUTO')
        complex_count = sum(1 for faq in faqs if faq['complexity'] == 'MANUAL')
        
        print(f"✅ {folder_slug} → {korean_title}")
        print(f"   📊 {len(faqs)}개 FAQ (텍스트: {text_count}, 복합: {complex_count})")
        
        processed_folders += 1
        total_faqs += len(faqs)
    
    return processed_folders, total_faqs

if __name__ == "__main__":
    print("🌏 FAQ 최종 통합 처리 시작...")
    
    try:
        processed_folders, total_faqs = process_final_accordion()
        
        print(f"\n✅ 최종 아코디언 통합 완료!")
        print(f"📁 처리된 폴더: {processed_folders}개")
        print(f"📊 통합된 FAQ: {total_faqs}개")
        
        print(f"\n🎯 최종 결과:")
        print(f"✅ 한국어 제목 및 구조 적용")
        print(f"✅ 깔끔한 YAML front matter")
        print(f"✅ 아코디언 UI 최적화")
        print(f"✅ 사이드바 연동 준비")
        
        print(f"\n🚀 다음 단계:")
        print(f"1. 빌드 테스트")
        print(f"2. 사이드바 확인") 
        print(f"3. UI/UX 검증")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
