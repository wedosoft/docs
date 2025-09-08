#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
특정 문서 추출 및 변환 시작 스크립트
"""

import csv
import os
from pathlib import Path

def extract_single_document(target_title):
    """특정 제목의 문서를 찾아서 추출"""
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    csv_files = [
        "merged_articles_links_replaced_freshservice_part1.csv",
        "merged_articles_links_replaced_freshservice_part2.csv", 
        "merged_articles_links_replaced_freshservice_part3.csv",
        "merged_articles_links_replaced_freshservice_part4.csv",
        "merged_articles_links_replaced_freshservice_part5.csv"
    ]
    
    # CSV 필드 크기 제한 증가
    csv.field_size_limit(1000000)
    
    print(f"🔍 '{target_title}' 문서 검색 중...")
    
    for csv_file in csv_files:
        csv_path = raw_data_dir / csv_file
        if not csv_path.exists():
            continue
            
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = row.get('title', '').strip()
                    if target_title.lower() in title.lower():
                        print(f"✅ 문서 발견: {title}")
                        print(f"📁 폴더: {row.get('folder_name', '')}")
                        print(f"📂 카테고리: {row.get('category_name', '')}")
                        print()
                        print("📄 내용:")
                        print("=" * 60)
                        print(row.get('content', '')[:2000])
                        if len(row.get('content', '')) > 2000:
                            print("...")
                        print("=" * 60)
                        return row
                        
        except Exception as e:
            print(f"❌ {csv_file} 처리 중 오류: {e}")
    
    print("❌ 문서를 찾을 수 없습니다.")
    return None

if __name__ == "__main__":
    # 두 번째 타겟 문서 - 더 구체적인 제목
    target = "Configure the ClearPass Aruba Integration App"
    document = extract_single_document(target)
    
    if document:
        print(f"\n🎯 다음 단계: 이 문서를 수작업으로 Markdown 변환")
        print(f"💡 참조: docs/freshworks/freshservice/ 기존 완성 문서들의 품질 기준 따라하기")
