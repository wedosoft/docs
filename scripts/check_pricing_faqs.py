#!/usr/bin/env python3
import json
import sys
import os

# 프로젝트 루트 디렉토리로 이동
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(project_root)

# 복잡도 분석 데이터 로드
with open('faq_complexity_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# pricing 카테고리 찾기
pricing_faqs = [item for item in data if item['category'] == 'pricing']
print(f'pricing 카테고리 FAQ 수: {len(pricing_faqs)}')
print()

for i, faq in enumerate(pricing_faqs, 1):
    print(f'{i}. {faq["title"]}')
    print(f'   복잡도: {faq["complexity_score"]}')
    print(f'   분류: {faq.get("classification", "N/A")}')
    if faq.get("description_preview"):
        preview = faq["description_preview"][:100].replace('\n', ' ')
        print(f'   내용: {preview}...')
    print()
