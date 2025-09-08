#!/usr/bin/env python3
"""
Automations FAQ 재작업 스크립트 - 새로운 품질 기준 적용
복잡도별 차별화 처리로 고품질 변환
"""

import pandas as pd
import os
import re
from pathlib import Path

def clean_text(text):
    """텍스트 정리"""
    if pd.isna(text):
        return ""
    
    text = str(text)
    # 기본 정리
    text = re.sub(r'\s+', ' ', text)  # 여러 공백을 하나로
    text = text.strip()
    return text

def analyze_complexity(html_content):
    """복잡도 분석"""
    if pd.isna(html_content):
        return 'EMPTY', 0, {}
    
    html_str = str(html_content)
    
    indicators = {
        'images': html_str.count('<img'),
        'tables': html_str.count('<table'),
        'lists': html_str.count('<ul') + html_str.count('<ol'),
        'code_blocks': html_str.count('<pre') + html_str.count('<code'),
        'links': html_str.count('<a '),
        'divs': html_str.count('<div')
    }
    
    complexity_score = (
        indicators['images'] * 5 +
        indicators['tables'] * 4 +
        indicators['code_blocks'] * 3 +
        indicators['lists'] * 2 +
        indicators['links'] * 1 +
        indicators['divs'] * 1
    )
    
    if complexity_score >= 10:
        return 'HIGH', complexity_score, indicators
    elif complexity_score >= 5:
        return 'MEDIUM', complexity_score, indicators
    elif complexity_score >= 1:
        return 'LOW', complexity_score, indicators
    else:
        return 'SIMPLE', complexity_score, indicators

def create_simple_faq_content(faqs):
    """SIMPLE 복잡도 FAQ 아코디언 생성"""
    
    content = """---
title: Automations FAQ
description: Freshservice 자동화 관련 자주 묻는 질문들
sidebar_position: 1
---

# 🤖 Automations FAQ

Freshservice의 자동화 기능에 대한 자주 묻는 질문들입니다.

"""
    
    # SIMPLE 복잡도 FAQ들을 아코디언으로 생성
    for i, faq in enumerate(faqs, 1):
        title = clean_text(faq['title'])
        answer = clean_text(faq['desc_clean'])
        
        content += f"""
<details>
<summary><strong>Q{i}. {title}</strong></summary>

{answer}

</details>

"""
    
    content += """
---

💡 **더 복잡한 자동화 설정이나 고급 기능에 대한 질문이 있으시면 지원팀에 문의해 주세요.**
"""
    
    return content

def main():
    """메인 실행 함수"""
    
    # CSV 파일들
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    # Automation FAQ 수집
    all_faqs = []
    
    for csv_file in csv_files:
        if not os.path.exists(csv_file):
            continue
            
        df = pd.read_csv(csv_file)
        
        # automation 관련 FAQ 찾기
        automation_docs = df[df['path'].str.contains('automation', case=False, na=False)]
        
        for idx, row in automation_docs.iterrows():
            complexity, score, indicators = analyze_complexity(row['description'])
            
            all_faqs.append({
                'title': row['title'],
                'path': row['path'],
                'complexity': complexity,
                'complexity_score': score,
                'indicators': indicators,
                'description': row['description'],
                'desc_clean': row['desc_un_html']
            })
    
    # 복잡도별 분류
    complexity_groups = {
        'SIMPLE': [],
        'LOW': [],
        'MEDIUM': [],
        'HIGH': []
    }
    
    for faq in all_faqs:
        complexity_groups[faq['complexity']].append(faq)
    
    # 통계 출력
    print("=== Automations FAQ 복잡도 분석 ===")
    for complexity in ['SIMPLE', 'LOW', 'MEDIUM', 'HIGH']:
        count = len(complexity_groups[complexity])
        print(f"{complexity}: {count}개")
    
    print(f"\n총 {len(all_faqs)}개 FAQ")
    
    # 폴더 생성
    output_dir = Path('docs/freshworks/freshservice/faqs/automations')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1단계: SIMPLE 복잡도 FAQ 생성
    simple_faqs = complexity_groups['SIMPLE']
    if simple_faqs:
        print(f"\n1단계: SIMPLE 복잡도 {len(simple_faqs)}개 처리 중...")
        
        # 제목순 정렬
        simple_faqs.sort(key=lambda x: x['title'])
        
        # 아코디언 형태로 생성
        simple_content = create_simple_faq_content(simple_faqs)
        
        # 파일 저장
        simple_file = output_dir / 'index.md'
        with open(simple_file, 'w', encoding='utf-8') as f:
            f.write(simple_content)
        
        print(f"✅ SIMPLE 복잡도 FAQ 생성 완료: {simple_file}")
        print(f"   - {len(simple_faqs)}개 FAQ 포함")
        print(f"   - 아코디언 형태 적용")
        print(f"   - 순수 텍스트 기반 고속 처리")
    
    # 다음 단계 안내
    print(f"\n=== 다음 작업 단계 ===")
    print(f"2단계: LOW 복잡도 {len(complexity_groups['LOW'])}개 - 자동 + 간단 검토")
    print(f"3단계: MEDIUM 복잡도 {len(complexity_groups['MEDIUM'])}개 - 반자동 (수동 보완)")
    print(f"4단계: HIGH 복잡도 {len(complexity_groups['HIGH'])}개 - 수동 작업 (이미지/테이블)")
    
    return True

if __name__ == "__main__":
    main()
