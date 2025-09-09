#!/usr/bin/env python3
"""
API and Webhooks FAQ 추출기
해당 폴더의 모든 FAQ를 추출하여 하나의 index.md로 통합
"""

import pandas as pd
import re
import json
from pathlib import Path

def extract_api_webhooks_faqs():
    """API and Webhooks 관련 FAQ들을 추출"""
    
    # CSV 파일들 읽기
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    api_webhooks_faqs = []
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            print(f"검색 중: {csv_file} ({len(df)}개 항목)")
            
            for idx, row in df.iterrows():
                title = str(row.get('title', ''))
                description = str(row.get('description', ''))
                path = str(row.get('path', ''))
                
                # API and Webhooks 관련 FAQ 필터링
                if 'api' in path.lower() or 'webhook' in path.lower() or \
                   'api' in title.lower() or 'webhook' in title.lower():
                    
                    faq_info = {
                        'title': title,
                        'description': description,
                        'path': path,
                        'content_length': len(description),
                        'csv_file': csv_file,
                        'row_index': idx
                    }
                    
                    api_webhooks_faqs.append(faq_info)
                    print(f"  찾음: {title}")
        
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {csv_file}")
        except Exception as e:
            print(f"오류 발생 ({csv_file}): {e}")
    
    print(f"\n📊 총 {len(api_webhooks_faqs)}개의 API/Webhooks FAQ 발견")
    
    # 결과를 JSON 파일로 저장
    with open('api_webhooks_faqs.json', 'w', encoding='utf-8') as f:
        json.dump(api_webhooks_faqs, f, ensure_ascii=False, indent=2)
    
    print(f"결과가 'api_webhooks_faqs.json'에 저장되었습니다.")
    
    # 발견된 FAQ 목록 출력
    if api_webhooks_faqs:
        print("\n" + "="*70)
        print("🔗 발견된 API/Webhooks FAQ 목록")
        print("="*70)
        for i, faq in enumerate(api_webhooks_faqs):
            print(f"{i+1:2d}. {faq['title']}")
            print(f"     경로: {faq['path']}")
            print(f"     길이: {faq['content_length']:,}자")
            print()

if __name__ == "__main__":
    extract_api_webhooks_faqs()
