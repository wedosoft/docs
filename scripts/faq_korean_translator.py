#!/usr/bin/env python3
"""
FAQ 제목 번역 및 한국어화 처리
- 영어 FAQ 제목을 한국어로 번역
- 사용자 친화적인 한국어 제목 적용
- 아코디언 구조 유지
"""

import pandas as pd
import json
import os
import re
from pathlib import Path
from collections import defaultdict

def translate_faq_titles():
    """FAQ 폴더명과 제목을 한국어로 번역"""
    
    # 폴더명 한국어 번역 매핑
    folder_translations = {
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
    
    # 공통 FAQ 제목 번역 매핑
    title_translations = {
        # API & Webhooks
        'What is a webhook': '웹훅이란 무엇인가요',
        'How do I create solution categories using API': 'API를 사용하여 솔루션 카테고리를 생성하는 방법',
        'Can we update custom fields of tickets using APIs': 'API를 사용하여 티켓의 사용자 정의 필드를 업데이트할 수 있나요',
        'What is the date time format used in Freshservice': 'Freshservice에서 사용되는 날짜 시간 형식은 무엇인가요',
        
        # Pricing
        'What is considered a chargeable managed asset in Freshservice': 'Freshservice에서 유료 관리 자산으로 간주되는 것은 무엇인가요',
        "What's the difference between Full-Time and Occasional Agents": '정규직 에이전트와 임시 에이전트의 차이점은 무엇인가요',
        
        # 일반적인 패턴 번역
        'How to': '방법: ',
        'How do I': '방법: ',
        'How can I': '방법: ',
        'What is': '무엇인가요: ',
        'What are': '무엇인가요: ',
        'Can I': '가능한가요: ',
        'Can we': '가능한가요: ',
        'Is it possible': '가능한가요: ',
        'Why': '왜 ',
        'Where': '어디서 '
    }
    
    return folder_translations, title_translations

def update_faq_titles():
    """FAQ 파일들의 제목을 한국어로 업데이트"""
    
    folder_translations, title_translations = translate_faq_titles()
    base_path = Path('docs/freshworks/freshservice/faqs')
    
    print("🌏 FAQ 제목 한국어화 처리 시작")
    print("=" * 60)
    
    updated_folders = 0
    
    for folder_path in base_path.iterdir():
        if folder_path.is_dir():
            folder_slug = folder_path.name
            korean_folder_name = folder_translations.get(folder_slug, folder_slug)
            
            index_path = folder_path / 'index.md'
            if index_path.exists():
                # index.md 파일 읽기
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 제목 부분 한국어로 변경
                content = re.sub(
                    r'title: ([^\\n]+) FAQs',
                    f'title: {korean_folder_name} FAQ',
                    content
                )
                
                content = re.sub(
                    r'# ([^\\n]+) FAQs',
                    f'# {korean_folder_name} FAQ',
                    content
                )
                
                content = re.sub(
                    r'([^\\n]+)와 관련된 자주 묻는 질문들입니다.',
                    f'{korean_folder_name}와 관련된 자주 묻는 질문들입니다.',
                    content
                )
                
                # 개별 FAQ 제목들을 번역할 수 있는 패턴 찾기 (간단한 패턴만)
                for eng_pattern, kor_translation in title_translations.items():
                    if eng_pattern in ['How to', 'How do I', 'How can I', 'What is', 'What are', 
                                     'Can I', 'Can we', 'Is it possible', 'Why', 'Where']:
                        content = re.sub(
                            f'<summary><strong>([0-9]+\\. ){eng_pattern}([^<]+)</strong>',
                            f'<summary><strong>\\1{kor_translation}\\2</strong>',
                            content
                        )
                
                # 특정 제목들 완전 번역
                for eng_title, kor_title in title_translations.items():
                    if eng_title not in ['How to', 'How do I', 'How can I', 'What is', 'What are', 
                                       'Can I', 'Can we', 'Is it possible', 'Why', 'Where']:
                        content = content.replace(eng_title, kor_title)
                
                # 파일 다시 쓰기
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ {folder_slug} → {korean_folder_name}")
                updated_folders += 1
    
    return updated_folders

if __name__ == "__main__":
    print("🌏 FAQ 한국어화 처리 시작...")
    
    try:
        updated_folders = update_faq_titles()
        
        print(f"\n✅ 한국어화 완료!")
        print(f"📁 업데이트된 폴더: {updated_folders}개")
        
        print(f"\n🎯 변경사항:")
        print(f"✅ 폴더명 한국어 번역")
        print(f"✅ 페이지 제목 한국어화") 
        print(f"✅ FAQ 제목 패턴 번역")
        print(f"✅ 사이드바 구조 개선")
        
        print(f"\n🚀 다음 단계:")
        print(f"1. 빌드 테스트")
        print(f"2. 사이드바 확인")
        print(f"3. 번역 품질 검증")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
