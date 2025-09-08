#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV 필드 구조 확인 및 실제 category_name, folder_name 추출
"""

import csv
import os
from pathlib import Path
from collections import Counter

def analyze_csv_structure():
    """CSV 필드 구조와 실제 데이터 확인"""
    
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
    
    all_categories = []
    all_folders = []
    integration_related = []
    
    print("🔍 CSV 필드 구조 및 데이터 분석 중...")
    print("=" * 60)
    
    for i, csv_file in enumerate(csv_files, 1):
        csv_path = raw_data_dir / csv_file
        if not csv_path.exists():
            print(f"❌ 파일 없음: {csv_file}")
            continue
            
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                # 첫 번째 파일에서 필드명 확인
                if i == 1:
                    print(f"📋 CSV 필드명들:")
                    if reader.fieldnames:
                        for field in reader.fieldnames:
                            print(f"  - {field}")
                    print()
                
                # 데이터 수집
                for row_num, row in enumerate(reader):
                    category = row.get('category_name', '').strip()
                    folder = row.get('folder_name', '').strip()
                    title = row.get('title', '').strip()
                    
                    if category:
                        all_categories.append(category)
                    
                    if folder:
                        all_folders.append(folder)
                    
                    # Integration/Extending 관련 찾기
                    if any(keyword in (category + ' ' + folder + ' ' + title).lower() 
                           for keyword in ['integration', 'extending', 'apps', 'connector']):
                        integration_related.append({
                            'category': category,
                            'folder': folder,
                            'title': title
                        })
                    
                    # 처음 몇 개 행 샘플 출력 (첫 번째 파일만)
                    if i == 1 and row_num < 3:
                        print(f"📄 샘플 행 {row_num + 1}:")
                        print(f"  Category: {category}")
                        print(f"  Folder: {folder}")
                        print(f"  Title: {title[:100]}...")
                        print()
                        
        except Exception as e:
            print(f"❌ {csv_file} 처리 중 오류: {e}")
    
    # 통계 출력
    category_counts = Counter(all_categories)
    folder_counts = Counter(all_folders)
    
    print(f"✅ 총 카테고리: {len(set(all_categories))}개")
    print(f"✅ 총 폴더: {len(set(all_folders))}개")
    print(f"✅ Integration 관련: {len(integration_related)}개")
    print()
    
    print("🏷️ 상위 카테고리 (TOP 10):")
    print("=" * 50)
    for category, count in category_counts.most_common(10):
        print(f"{count:3d}개 - {category}")
    
    print()
    print("📁 상위 폴더 (TOP 15):")
    print("=" * 50)
    for folder, count in folder_counts.most_common(15):
        print(f"{count:3d}개 - {folder}")
    
    print()
    print("🔌 Integration 관련 문서들:")
    print("=" * 60)
    for item in integration_related[:10]:  # 처음 10개만
        print(f"📁 {item['category']} > {item['folder']}")
        print(f"📄 {item['title']}")
        print()
    
    return category_counts, folder_counts, integration_related

if __name__ == "__main__":
    category_counts, folder_counts, integration_related = analyze_csv_structure()
    
    print("🎯 다음 단계: 정확한 폴더명으로 문서 추출 스크립트 수정")
