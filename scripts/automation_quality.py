#!/usr/bin/env python3
import pandas as pd
import re

# part4 파일에서 automation 관련 데이터 분석
df = pd.read_csv('raw_data/merged_articles_links_replaced_freshservice_part4.csv')

# 'automation' 관련 항목 필터링
automation_faqs = df[df['path'].str.contains('automation', case=False, na=False)]

print(f"총 automation FAQ 개수: {len(automation_faqs)}")
print("=" * 60)

# 첫 번째 FAQ 샘플 분석
if len(automation_faqs) > 0:
    sample = automation_faqs.iloc[0]
    
    print(f"제목: {sample['title']}")
    print(f"경로: {sample['path']}")
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
    
    print(f"\n변환 후 텍스트 샘플 (처음 300자):")
    print("-" * 40)
    print(converted_text[:300] + "..." if len(converted_text) > 300 else converted_text)
    
    print(f"\n원본 HTML 샘플 (처음 500자):")
    print("-" * 40)
    print(original_html[:500] + "..." if len(original_html) > 500 else original_html)

print("\n전체 automation FAQ에서 이미지 통계:")
print("=" * 60)

total_images = 0
faqs_with_images = 0
for idx, row in automation_faqs.iterrows():
    html_content = str(row['description'])
    img_count = len(re.findall(r'<img[^>]*src=', html_content, re.IGNORECASE))
    total_images += img_count
    if img_count > 0:
        faqs_with_images += 1

print(f"전체 automation FAQ의 총 이미지 개수: {total_images}")
if len(automation_faqs) > 0:
    print(f"FAQ당 평균 이미지 개수: {total_images / len(automation_faqs):.1f}")
    print(f"이미지가 있는 FAQ 비율: {faqs_with_images / len(automation_faqs) * 100:.1f}%")

# 이미지가 많은 상위 5개 FAQ
print(f"\n이미지가 많은 상위 5개 FAQ:")
print("-" * 40)
image_counts = []
for idx, row in automation_faqs.iterrows():
    html_content = str(row['description'])
    img_count = len(re.findall(r'<img[^>]*src=', html_content, re.IGNORECASE))
    image_counts.append((row['title'], img_count, row['path']))

# 이미지 개수로 정렬
image_counts.sort(key=lambda x: x[1], reverse=True)
for i, (title, count, path) in enumerate(image_counts[:5]):
    print(f"{i+1}. {title[:50]}... ({count}개 이미지)")
