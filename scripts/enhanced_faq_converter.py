#!/usr/bin/env python3
"""
고품질 FAQ 변환기
원본 HTML 구조를 최대한 보존하여 Markdown으로 변환
"""

import pandas as pd
import re
from bs4 import BeautifulSoup
import html

def clean_html_to_markdown(html_content):
    """HTML을 구조화된 Markdown으로 변환"""
    if pd.isna(html_content) or html_content == '':
        return ""
    
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')
    
    markdown_parts = []
    
    # 각 요소를 Markdown으로 변환
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'li', 'strong', 'em', 'code', 'pre', 'img']):
        if element.name == 'h1':
            markdown_parts.append(f"# {element.get_text().strip()}")
        elif element.name == 'h2':
            markdown_parts.append(f"## {element.get_text().strip()}")
        elif element.name == 'h3':
            markdown_parts.append(f"### {element.get_text().strip()}")
        elif element.name == 'h4':
            markdown_parts.append(f"#### {element.get_text().strip()}")
        elif element.name == 'p':
            text = element.get_text().strip()
            if text:
                markdown_parts.append(text)
        elif element.name == 'ul':
            for li in element.find_all('li', recursive=False):
                markdown_parts.append(f"- {li.get_text().strip()}")
        elif element.name == 'ol':
            for i, li in enumerate(element.find_all('li', recursive=False), 1):
                markdown_parts.append(f"{i}. {li.get_text().strip()}")
        elif element.name == 'strong':
            markdown_parts.append(f"**{element.get_text().strip()}**")
        elif element.name == 'em':
            markdown_parts.append(f"*{element.get_text().strip()}*")
        elif element.name == 'code':
            markdown_parts.append(f"`{element.get_text().strip()}`")
        elif element.name == 'pre':
            markdown_parts.append(f"```\n{element.get_text().strip()}\n```")
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '이미지')
            if src:
                markdown_parts.append(f"![{alt}]({src})")
                markdown_parts.append(f"<!-- 이미지 원본: {src} -->")
    
    return "\n\n".join(markdown_parts)

def analyze_faq_complexity(title, description, html_content):
    """FAQ의 복잡도를 분석하여 처리 우선순위 결정"""
    complexity_score = 0
    
    # 제목 기반 점수
    important_keywords = ['setup', 'configure', 'install', 'troubleshoot', 'error']
    for keyword in important_keywords:
        if keyword.lower() in title.lower():
            complexity_score += 2
    
    # HTML 복잡도
    if html_content and len(html_content) > 1000:
        complexity_score += 3
    
    # 이미지 포함 여부
    if '<img' in str(html_content):
        complexity_score += 5
    
    # 코드 블록 포함 여부
    if '<pre>' in str(html_content) or '<code>' in str(html_content):
        complexity_score += 3
    
    # 목록 구조 포함 여부
    if '<ul>' in str(html_content) or '<ol>' in str(html_content):
        complexity_score += 1
    
    return complexity_score

def categorize_faq_priority(complexity_score):
    """복잡도 점수 기반 우선순위 분류"""
    if complexity_score >= 8:
        return "HIGH"  # 수동 처리 필요
    elif complexity_score >= 4:
        return "MEDIUM"  # 반자동 처리
    else:
        return "LOW"  # 자동 처리 가능

def process_faq_category(csv_path, category_path_filter, output_file=None):
    """특정 카테고리의 FAQ를 분석하고 처리"""
    
    df = pd.read_csv(csv_path)
    
    # 카테고리 필터링
    category_faqs = df[df['path'].str.contains(category_path_filter, case=False, na=False)].copy()
    
    results = []
    
    for idx, row in category_faqs.iterrows():
        title = str(row['title'])
        description = str(row['description']) if pd.notna(row['description']) else ""
        html_content = str(row['desc_un_html']) if pd.notna(row['desc_un_html']) else ""
        
        # 복잡도 분석
        complexity = analyze_faq_complexity(title, description, html_content)
        priority = categorize_faq_priority(complexity)
        
        # Markdown 변환
        markdown_content = clean_html_to_markdown(description)
        
        # 이미지 개수 세기
        image_count = html_content.count('<img')
        
        results.append({
            'title': title,
            'priority': priority,
            'complexity_score': complexity,
            'image_count': image_count,
            'original_html_length': len(html_content),
            'markdown_content': markdown_content,
            'needs_manual_review': priority == "HIGH"
        })
    
    # 결과 정리
    high_priority = [r for r in results if r['priority'] == 'HIGH']
    medium_priority = [r for r in results if r['priority'] == 'MEDIUM']
    low_priority = [r for r in results if r['priority'] == 'LOW']
    
    print(f"=== {category_path_filter} 카테고리 분석 결과 ===")
    print(f"총 FAQ 수: {len(results)}")
    print(f"HIGH 우선순위 (수동 처리): {len(high_priority)}개")
    print(f"MEDIUM 우선순위 (반자동): {len(medium_priority)}개") 
    print(f"LOW 우선순위 (자동 처리): {len(low_priority)}개")
    print()
    
    if high_priority:
        print("🔥 HIGH 우선순위 FAQ들:")
        for item in high_priority[:5]:  # 상위 5개만 표시
            print(f"- {item['title']} (이미지: {item['image_count']}개)")
        print()
    
    return results

if __name__ == "__main__":
    # 예시: automations 카테고리 분석
    import glob
    
    csv_files = glob.glob('raw_data/merged_articles_links_replaced_freshservice_part*.csv')
    
    all_results = {}
    
    # 각 카테고리별 분석
    categories = [
        'automations-and-triggers',
        'changes', 
        'asset-management',
        'reports'
    ]
    
    for category in categories:
        print(f"\n{'='*50}")
        print(f"분석 중: {category}")
        print('='*50)
        
        category_results = []
        for csv_file in csv_files:
            results = process_faq_category(csv_file, category)
            category_results.extend(results)
        
        all_results[category] = category_results
    
    # 전체 요약
    print(f"\n{'='*50}")
    print("전체 요약")
    print('='*50)
    
    total_high = sum(len([r for r in results if r['priority'] == 'HIGH']) for results in all_results.values())
    total_medium = sum(len([r for r in results if r['priority'] == 'MEDIUM']) for results in all_results.values())
    total_low = sum(len([r for r in results if r['priority'] == 'LOW']) for results in all_results.values())
    
    print(f"전체 FAQ 수: {total_high + total_medium + total_low}")
    print(f"수동 처리 필요: {total_high}개 ({total_high/(total_high + total_medium + total_low)*100:.1f}%)")
    print(f"반자동 처리: {total_medium}개 ({total_medium/(total_high + total_medium + total_low)*100:.1f}%)")
    print(f"자동 처리 가능: {total_low}개 ({total_low/(total_high + total_medium + total_low)*100:.1f}%)")
