#!/usr/bin/env python3
"""
Extract Reports FAQs from CSV files
"""

import pandas as pd
import json
import os
from pathlib import Path

def extract_reports_faqs():
    """Extract FAQs with folder_name='Reports' from all CSV files"""
    
    # CSV 파일들이 있는 디렉토리
    csv_dir = Path("/Users/alan/GitHub/docs/raw_data")
    
    all_faqs = []
    
    # 모든 CSV 파일 처리
    csv_files = [
        "merged_articles_links_replaced_freshservice_part1.csv",
        "merged_articles_links_replaced_freshservice_part2.csv", 
        "merged_articles_links_replaced_freshservice_part3.csv",
        "merged_articles_links_replaced_freshservice_part4.csv",
        "merged_articles_links_replaced_freshservice_part5.csv"
    ]
    
    for csv_file in csv_files:
        csv_path = csv_dir / csv_file
        if csv_path.exists():
            print(f"Processing {csv_file}...")
            
            try:
                # CSV 파일 읽기
                df = pd.read_csv(csv_path, encoding='utf-8')
                
                # folder_name이 'Reports'인 행들만 필터링
                reports_rows = df[df['folder_name'] == 'Reports'].copy()
                
                print(f"Found {len(reports_rows)} Reports FAQs in {csv_file}")
                
                # FAQ 정보 추출
                for idx, row in reports_rows.iterrows():
                    faq_info = {
                        "title": str(row.get('title', '')).strip(),
                        "description": str(row.get('description', '')).strip() if pd.notna(row.get('description')) else "",
                        "path": str(row.get('path', '')).strip() if pd.notna(row.get('path')) else "",
                        "content_length": len(str(row.get('description', ''))) if pd.notna(row.get('description')) else 0,
                        "csv_file": csv_file,
                        "row_index": idx
                    }
                    
                    if faq_info["title"] and faq_info["title"] != 'nan':
                        all_faqs.append(faq_info)
                        
            except Exception as e:
                print(f"Error processing {csv_file}: {e}")
                continue
    
    # 중복 제거 (제목 기준)
    seen_titles = set()
    unique_faqs = []
    
    for faq in all_faqs:
        if faq["title"] not in seen_titles:
            unique_faqs.append(faq)
            seen_titles.add(faq["title"])
        else:
            print(f"Duplicate title found: {faq['title']}")
    
    print(f"\nTotal unique Reports FAQs found: {len(unique_faqs)}")
    
    # JSON 파일로 저장
    output_file = "/Users/alan/GitHub/docs/reports_faqs.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_faqs, f, ensure_ascii=False, indent=2)
    
    print(f"Reports FAQs saved to: {output_file}")
    
    # 제목들 출력
    print("\nReports FAQ titles:")
    for i, faq in enumerate(unique_faqs, 1):
        print(f"{i:2d}. {faq['title']}")
    
    return unique_faqs

if __name__ == "__main__":
    extract_reports_faqs()
