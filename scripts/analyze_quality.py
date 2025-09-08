#!/usr/bin/env python3
import pandas as pd
import html
import re

# automations FAQ 중 하나의 원본 HTML 내용을 확인해보기
df = pd.read_csv('raw_data/merged_articles_links_replaced_freshservice_part1.csv')
automations_faqs = df[df['path'].str.contains('automations-and-triggers', case=False, na=False)]

# 첫 번째 FAQ의 원본 description 확인
if len(automations_faqs) > 0:
    first_faq = automations_faqs.iloc[0]
    print(f'제목: {first_faq["title"]}')
    print('=' * 50)
    
    # HTML 태그가 포함된 원본 description
    original_desc = str(first_faq['description'])
    print('원본 HTML 내용 (일부):')
    print(original_desc[:1000] + '...' if len(original_desc) > 1000 else original_desc)
    print()
    print('=' * 50)
    
    # 이미 변환된 desc_un_html과 비교
    converted_desc = str(first_faq['desc_un_html'])
    print('변환된 텍스트 내용 (일부):')
    print(converted_desc[:1000] + '...' if len(converted_desc) > 1000 else converted_desc)
    
    print('\n' + '=' * 50)
    print('HTML 태그 분석:')
    # img 태그 개수
    img_count = len(re.findall(r'<img[^>]*>', original_desc))
    print(f'이미지 개수: {img_count}')
    
    # 기타 포맷팅 태그들
    code_count = len(re.findall(r'<code[^>]*>.*?</code>', original_desc, re.DOTALL))
    print(f'코드 블록 개수: {code_count}')
    
    pre_count = len(re.findall(r'<pre[^>]*>.*?</pre>', original_desc, re.DOTALL))
    print(f'pre 블록 개수: {pre_count}')
    
    ol_count = len(re.findall(r'<ol[^>]*>', original_desc))
    ul_count = len(re.findall(r'<ul[^>]*>', original_desc))
    print(f'순서 목록 개수: {ol_count}')
    print(f'비순서 목록 개수: {ul_count}')
