#!/usr/bin/env python3
"""
FAQ 크로스 폴더 텍스트 전용 배치 처리기
- 329개 텍스트 전용 문서 자동 변환
- 원본 position 순서 유지
- MDX 호환성 보장
"""

import pandas as pd
import json
import os
import re
from pathlib import Path

def load_csv_data():
    """CSV 데이터 로드 및 병합"""
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    all_data = []
    for file in csv_files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            all_data.append(df)
            print(f"✅ {file}: {len(df)}개 로드")
    
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"📊 총 {len(combined_df)}개 문서 로드")
        return combined_df
    return None

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

def create_doc_slug(title):
    """문서 제목을 slug로 변환"""
    # 특수문자 제거 및 kebab-case 변환
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    slug = slug.strip('-')
    
    # 숫자로 시작하면 prefix 추가
    if slug and slug[0].isdigit():
        slug = f"faq-{slug}"
    
    return slug

def clean_content_for_mdx(content):
    """MDX 호환성을 위한 콘텐츠 정리"""
    if pd.isna(content):
        return ""
    
    content = str(content)
    
    # HTML 태그 기본 정리
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'<p>', '\n', content)
    content = re.sub(r'</p>', '\n', content)
    
    # 이미지 태그 변환
    content = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>', r'![Image](\1)', content)
    
    # 링크 태그 변환
    content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content)
    
    # 기타 HTML 태그 제거
    content = re.sub(r'<[^>]+>', '', content)
    
    # 연속 줄바꿈 정리
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def process_text_only_documents():
    """텍스트 전용 문서 처리"""
    
    # 분석 결과 로드
    with open('faq_simple_analysis.json', 'r') as f:
        analysis_data = json.load(f)
    
    # CSV 데이터 로드
    df = load_csv_data()
    if df is None:
        print("❌ CSV 데이터를 로드할 수 없습니다.")
        return
    
    # FAQ 카테고리만 필터링
    faq_df = df[df['category'] == 'FAQ'].copy()
    
    print(f"\n🎯 텍스트 전용 문서 처리 시작")
    print("=" * 60)
    
    processed_count = 0
    error_count = 0
    
    # 폴더별로 그룹화
    folders_processed = {}
    
    for item in analysis_data:
        if item['processing_recommendation'] != 'AUTO':
            continue
            
        try:
            # CSV에서 해당 문서 찾기
            doc_row = faq_df[faq_df['id'] == item['id']]
            if doc_row.empty:
                print(f"⚠️ 문서 {item['id']} CSV에서 찾을 수 없음")
                continue
                
            doc = doc_row.iloc[0]
            folder_slug = create_faq_slug(item['folder_name'])
            
            # 폴더별 카운트
            if folder_slug not in folders_processed:
                folders_processed[folder_slug] = 0
            
            # 문서 slug 생성
            doc_slug = create_doc_slug(doc['title'])
            
            # 파일 경로
            folder_path = Path(f'docs/freshworks/freshservice/faqs/{folder_slug}')
            file_path = folder_path / f'{doc_slug}.mdx'
            
            # 폴더 생성
            folder_path.mkdir(parents=True, exist_ok=True)
            
            # 콘텐츠 정리
            content = clean_content_for_mdx(doc.get('desc_un_html', ''))
            
            # MDX 파일 생성
            mdx_content = f"""---
title: "{doc['title']}"
sidebar_position: {doc.get('position', 1)}
---

# {doc['title']}

{content}

---
*원본 ID: {doc['id']} | 폴더: {item['folder_name']}*
"""
            
            # 파일 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(mdx_content)
            
            folders_processed[folder_slug] += 1
            processed_count += 1
            
            if processed_count % 50 == 0:
                print(f"📄 처리 중... {processed_count}개 완료")
                
        except Exception as e:
            error_count += 1
            print(f"❌ 문서 {item['id']} 처리 오류: {e}")
    
    print(f"\n✅ 텍스트 전용 문서 처리 완료!")
    print(f"📊 성공: {processed_count}개, 오류: {error_count}개")
    print(f"\n📁 폴더별 처리 결과:")
    
    for folder_slug, count in sorted(folders_processed.items()):
        print(f"  {folder_slug:25} {count}개")
    
    return processed_count, folders_processed

def create_index_files():
    """각 폴더에 index.mdx 파일 생성"""
    
    print(f"\n📋 Index 파일 생성")
    print("=" * 60)
    
    base_path = Path('docs/freshworks/freshservice/faqs')
    created_indexes = 0
    
    for folder_path in base_path.iterdir():
        if not folder_path.is_dir():
            continue
            
        folder_slug = folder_path.name
        index_path = folder_path / 'index.mdx'
        
        # 폴더 내 MDX 파일 목록
        mdx_files = list(folder_path.glob('*.mdx'))
        mdx_files = [f for f in mdx_files if f.name != 'index.mdx']
        
        # 폴더명을 제목으로 변환
        folder_title = folder_slug.replace('-', ' ').title()
        
        # Index 파일 내용 생성
        index_content = f"""---
title: "{folder_title}"
sidebar_position: 1
---

# {folder_title}

이 섹션에는 {folder_title}와 관련된 자주 묻는 질문들이 포함되어 있습니다.

## 문서 목록

총 {len(mdx_files)}개의 FAQ가 있습니다.

---
*자동 생성된 index 파일*
"""
        
        # 파일 저장
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        created_indexes += 1
        print(f"✅ {folder_slug:25} index.mdx 생성 ({len(mdx_files)}개 FAQ)")
    
    print(f"\n📋 총 {created_indexes}개 index 파일 생성 완료")
    return created_indexes

if __name__ == "__main__":
    print("🚀 FAQ 텍스트 전용 배치 처리 시작...")
    
    try:
        # 1. 텍스트 전용 문서 처리
        result = process_text_only_documents()
        if result is None:
            print("❌ 처리 실패")
            exit(1)
            
        processed_count, folders_processed = result
        
        # 2. Index 파일 생성
        index_count = create_index_files()
        
        print(f"\n🎉 배치 처리 완료!")
        print(f"📄 텍스트 전용 문서: {processed_count}개 처리")
        print(f"📋 Index 파일: {index_count}개 생성")
        print(f"📁 처리된 폴더: {len(folders_processed)}개")
        
        print(f"\n🎯 다음 단계:")
        print(f"1. sidebars.ts 설정 추가")
        print(f"2. 복합 요소 문서 179개 수동 처리")
        print(f"3. 빌드 테스트 실행")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
