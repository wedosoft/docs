#!/usr/bin/env python3
"""
FAQ 지침서 규칙 적용 폴더 생성 및 배치 시스템
- 지침서 slug 규칙 완전 적용
- 크로스 폴더 텍스트/복합 요소 배치
- 원본 position 순서 유지
"""

import pandas as pd
import json
import os
from pathlib import Path

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

def load_faq_data_with_complexity():
    """FAQ 데이터를 복잡도 정보와 함께 로드"""
    
    # 단순화된 분석 결과 로드
    with open('faq_simple_analysis.json', 'r') as f:
        complexity_data = json.load(f)
    
    # 폴더별로 분류
    folders_data = {}
    
    for item in complexity_data:
        folder_name = item['folder_name']
        folder_slug = create_faq_slug(folder_name)
        
        if folder_slug not in folders_data:
            folders_data[folder_slug] = {
                'original_name': folder_name,
                'slug': folder_slug,
                'text_only': [],
                'complex': [],
                'total': 0
            }
        
        # 복잡도에 따라 분류
        if item['processing_recommendation'] == 'AUTO':
            folders_data[folder_slug]['text_only'].append(item)
        else:
            folders_data[folder_slug]['complex'].append(item)
        
        folders_data[folder_slug]['total'] += 1
    
    return folders_data

def create_folder_structure():
    """FAQ 폴더 구조 생성"""
    
    folders_data = load_faq_data_with_complexity()
    base_path = Path('docs/freshworks/freshservice/faqs')
    
    print("📁 FAQ 폴더 구조 생성 (지침서 규칙 적용)")
    print("=" * 60)
    
    created_folders = []
    
    for folder_slug, data in folders_data.items():
        folder_path = base_path / folder_slug
        
        # 폴더 생성
        folder_path.mkdir(parents=True, exist_ok=True)
        
        print(f"✅ {data['original_name']:35} → {folder_slug}")
        print(f"   📍 {folder_path}")
        print(f"   📊 텍스트: {len(data['text_only'])}개, 복합: {len(data['complex'])}개, 총: {data['total']}개")
        print()
        
        created_folders.append({
            'original_name': data['original_name'],
            'slug': folder_slug,
            'path': str(folder_path),
            'text_count': len(data['text_only']),
            'complex_count': len(data['complex']),
            'total_count': data['total']
        })
    
    return created_folders

def generate_batch_processing_plan():
    """배치 처리 계획 생성"""
    
    folders_data = load_faq_data_with_complexity()
    
    print("\n🚀 크로스 폴더 배치 처리 계획")
    print("=" * 60)
    
    # 텍스트 전용 배치
    total_text = sum(len(data['text_only']) for data in folders_data.values())
    total_complex = sum(len(data['complex']) for data in folders_data.values())
    
    print(f"📦 1단계 - 텍스트 전용 배치: {total_text}개 문서")
    print("-" * 40)
    
    # 텍스트 100% 폴더들
    text_100_folders = [(slug, data) for slug, data in folders_data.items() 
                       if len(data['complex']) == 0 and len(data['text_only']) > 0]
    
    if text_100_folders:
        print("🎯 100% 텍스트 폴더들 (즉시 완료 가능):")
        for slug, data in text_100_folders:
            print(f"  {slug:25} {len(data['text_only'])}개")
    
    # 텍스트 90%+ 폴더들
    text_90_folders = [(slug, data) for slug, data in folders_data.items() 
                      if len(data['complex']) > 0 and len(data['text_only']) > 0 
                      and len(data['text_only']) / data['total'] >= 0.9]
    
    if text_90_folders:
        print("\n⚡ 90%+ 텍스트 폴더들 (빠른 처리):")
        for slug, data in text_90_folders:
            ratio = len(data['text_only']) / data['total'] * 100
            print(f"  {slug:25} {len(data['text_only'])}개 텍스트 ({ratio:.1f}%)")
    
    print(f"\n📦 2단계 - 복합 요소 배치: {total_complex}개 문서")
    print("-" * 40)
    
    # 복합 요소가 많은 폴더들
    complex_folders = [(slug, data) for slug, data in folders_data.items() 
                      if len(data['complex']) > 0]
    complex_folders.sort(key=lambda x: len(x[1]['complex']), reverse=True)
    
    print("🔥 복합 요소 많은 폴더들 (수동 처리 필요):")
    for slug, data in complex_folders[:10]:  # 상위 10개
        print(f"  {slug:25} {len(data['complex'])}개 복합")
    
    return {
        'total_text': total_text,
        'total_complex': total_complex,
        'text_100_folders': text_100_folders,
        'text_90_folders': text_90_folders,
        'complex_folders': complex_folders
    }

def generate_sidebars_config():
    """sidebars.ts 설정 생성"""
    
    folders_data = load_faq_data_with_complexity()
    
    print("\n📋 Sidebars 설정 (sidebars.ts)")
    print("=" * 60)
    
    sidebar_items = []
    for folder_slug in sorted(folders_data.keys()):
        sidebar_items.append(f"        'freshworks/freshservice/faqs/{folder_slug}/index',")
    
    sidebar_config = f"""
// FAQ 카테고리 추가
{{
  type: 'category',
  label: 'Freshservice FAQs',
  items: [
{chr(10).join(sidebar_items)}
  ],
}},
"""
    
    print("📁 sidebars.ts에 추가할 설정:")
    print(sidebar_config)
    
    return sidebar_config

if __name__ == "__main__":
    print("🔍 FAQ 지침서 규칙 적용 시작...")
    
    try:
        # 1. 폴더 구조 생성
        created_folders = create_folder_structure()
        
        # 2. 배치 처리 계획 생성
        batch_plan = generate_batch_processing_plan()
        
        # 3. Sidebars 설정 생성
        sidebar_config = generate_sidebars_config()
        
        print(f"\n✅ FAQ 폴더 구조 생성 완료!")
        print(f"📊 총 {len(created_folders)}개 폴더 생성")
        print(f"📦 텍스트 전용: {batch_plan['total_text']}개")
        print(f"🔥 복합 요소: {batch_plan['total_complex']}개")
        
        print(f"\n🎯 다음 단계:")
        print(f"1. 텍스트 전용 문서부터 크로스 폴더 배치")
        print(f"2. 각 폴더에 index.md 파일 생성")
        print(f"3. sidebars.ts 설정 추가")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
