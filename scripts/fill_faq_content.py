#!/usr/bin/env python3
import pandas as pd
import json
import os
import re
from pathlib import Path

def clean_text(text):
    """텍스트 정리"""
    if pd.isna(text) or text == '':
        return ''
    text = str(text).strip()
    # HTML 태그 제거
    text = re.sub(r'<[^>]+>', '', text)
    # 특수 문자 정리
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    return text

def escape_yaml_value(value):
    """YAML 값에서 특수 문자 이스케이프"""
    if not value:
        return '""'
    
    # 따옴표가 포함된 경우 전체를 따옴표로 감싸고 내부 따옴표는 이스케이프
    if '"' in value or "'" in value or ':' in value or value.strip() != value:
        return f'"{value.replace(chr(34), chr(92)+chr(34))}"'
    
    return value

def translate_title(english_title):
    """제목 번역 (기본적인 번역)"""
    translations = {
        'API': 'API',
        'FAQ': 'FAQ',
        'Affiliate Marketing FAQ': 'Affiliate 마케팅 FAQ',
        'Asset and CI FAQ': '자산 및 CI FAQ', 
        'Backup and Restore FAQ': '백업 및 복원 FAQ',
        'Billing FAQ': '청구 FAQ',
        'Business Rules FAQ': '비즈니스 규칙 FAQ',
        'Change FAQ': '변경 FAQ',
        'Conversations FAQ': '대화 FAQ',
        'Custom Objects FAQ': '사용자 정의 객체 FAQ',
        'Department and SLA FAQ': '부서 및 SLA FAQ',
        'Email FAQ': '이메일 FAQ',
        'Field FAQ': '필드 FAQ',
        'Forms FAQ': '양식 FAQ',
        'Insights and Widgets FAQ': '인사이트 및 위젯 FAQ',
        'Integration FAQ': '통합 FAQ',
        'Marketplace FAQ': '마켓플레이스 FAQ',
        'Mobile and Onboarding FAQ': '모바일 및 온보딩 FAQ',
        'Onboarding FAQ': '온보딩 FAQ',
        'Portal FAQ': '포털 FAQ',
        'Pricing FAQ': '가격 FAQ',
        'Problem FAQ': '문제 FAQ',
        'Release FAQ': '릴리스 FAQ',
        'Reports FAQ': '보고서 FAQ',
        'Service Catalog FAQ': '서비스 카탈로그 FAQ',
        'Service Desk FAQ': '서비스 데스크 FAQ',
        'SSO (Single Sign-On) FAQ': 'SSO (Single Sign-On) FAQ',
        'Ticket FAQ': '티켓 FAQ',
        'Time Tracking FAQ': '시간 추적 FAQ',
        'Workspace FAQ': '워크스페이스 FAQ'
    }
    
    return translations.get(english_title, english_title)

def main():
    # CSV 파일들 로드
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    print("CSV 파일들 로딩중...")
    all_data = []
    for csv_file in csv_files:
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            all_data.append(df)
            print(f"로드됨: {csv_file} ({len(df)} 행)")
    
    if not all_data:
        print("CSV 파일을 찾을 수 없습니다!")
        return
    
    # 모든 데이터 합치기
    combined_df = pd.concat(all_data, ignore_index=True)
    print(f"총 {len(combined_df)}개 FAQ 로드됨")
    
    # FAQ 폴더 확인
    faq_base_path = Path("docs/freshworks/freshservice/faqs")
    
    for category_folder in faq_base_path.iterdir():
        if not category_folder.is_dir():
            continue
            
        index_file = category_folder / "index.md"
        if not index_file.exists():
            continue
            
        category_name = category_folder.name.replace('-', ' ').title()
        print(f"\n처리중: {category_name}")
        
        # 해당 카테고리의 FAQ들 찾기
        category_faqs = combined_df[
            combined_df['folder_name'].str.contains(category_name, case=False, na=False) |
            combined_df['folder_name'].str.contains(category_folder.name, case=False, na=False) |
            combined_df['path'].str.contains(category_folder.name, case=False, na=False)
        ].copy()
        
        if len(category_faqs) == 0:
            print(f"  {category_name}에 대한 FAQ를 찾을 수 없습니다.")
            continue
        
        print(f"  {len(category_faqs)}개 FAQ 발견")
        
        # 한국어 제목 생성
        korean_title = translate_title(f"{category_name} FAQ")
        
        # 새로운 index.md 내용 생성
        content = f"""---
sidebar_position: 1
title: {escape_yaml_value(korean_title)}
---

# {korean_title}

"""
        
        # FAQ 항목들 추가
        for idx, row in category_faqs.iterrows():
            title = clean_text(row.get('title', ''))
            body = clean_text(row.get('desc_un_html', ''))
            
            if not title:
                continue
                
            content += f"""<details>
<summary>{title}</summary>

{body if body else '이 FAQ에 대한 상세 내용이 준비 중입니다.'}

</details>

"""
        
        # 파일 저장
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ {index_file} 업데이트됨 ({len(category_faqs)}개 FAQ)")

if __name__ == "__main__":
    main()
