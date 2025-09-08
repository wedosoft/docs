#!/usr/bin/env python3
import pandas as pd
import re

# 자동화 FAQ 관련 데이터만 추출하여 품질 분석
df = pd.read_csv('raw_data/merged_articles_links_replaced_freshservice_part1.csv')

# 'automations-and-triggers'가 path에 포함된 항목 필터링
automations_faqs = df[df['path'].str.contains('automations-and-triggers', case=False, na=False)]

print(f"총 automations FAQ 개수: {len(automations_faqs)}")
print("=" * 60)

# 첫 번째 FAQ 샘플 분석
if len(automations_faqs) > 0:
    sample = automations_faqs.iloc[0]
    
    print(f"제목: {sample['title']}")
    print("-" * 40)
    
    # 원본 HTML 내용
    original_html = str(sample['description'])
    print("원본 HTML 내용 길이:", len(original_html))
    
    # 변환된 텍스트 내용
    converted_text = str(sample['desc_un_html'])
    print("변환된 텍스트 길이:", len(converted_text))
    
    print("\n품질 비교:")
    print("-" * 40)
    
    # 이미지 개수
    img_count = len(re.findall(r'<img[^>]*src=', original_html, re.IGNORECASE))
    print(f"원본 이미지 개수: {img_count}")
    
    # 코드 블록
    code_count = len(re.findall(r'<code[^>]*>|<pre[^>]*>', original_html, re.IGNORECASE))
    print(f"원본 코드 블록 개수: {code_count}")
    
    # 리스트 항목
    list_count = len(re.findall(r'<[uo]l[^>]*>|<li[^>]*>', original_html, re.IGNORECASE))
    print(f"원본 리스트 관련 태그 개수: {list_count}")
    
    # 강조 텍스트
    bold_count = len(re.findall(r'<strong[^>]*>|<b[^>]*>', original_html, re.IGNORECASE))
    print(f"원본 강조 텍스트 개수: {bold_count}")
    
    print(f"\n변환 후 텍스트 샘플 (처음 500자):")
    print("-" * 40)
    print(converted_text[:500] + "..." if len(converted_text) > 500 else converted_text)
    
print("\n전체 automations FAQ에서 이미지 통계:")
print("=" * 60)

total_images = 0
for idx, row in automations_faqs.iterrows():
    html_content = str(row['description'])
    img_count = len(re.findall(r'<img[^>]*src=', html_content, re.IGNORECASE))
    total_images += img_count

print(f"전체 automations FAQ의 총 이미지 개수: {total_images}")
print(f"FAQ당 평균 이미지 개수: {total_images / len(automations_faqs):.1f}")
