#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV에서 실제 폴더명을 추출하여 확인하는 스크립트
"""

import csv
import os
from pathlib import Path
from collections import Counter

def check_folder_names():
    """CSV에서 실제 폴더명들을 확인"""
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    csv_files = [
        "merged_articles_links_replaced_freshservice_part1.csv",
        "merged_articles_links_replaced_freshservice_part2.csv", 
        "merged_articles_links_replaced_freshservice_part3.csv",
        "merged_articles_links_replaced_freshservice_part4.csv",
        "merged_articles_links_replaced_freshservice_part5.csv"
    ]
    
    all_folders = []
    integration_folders = []
    
    print("🔍 CSV 파일들에서 폴더명 추출 중...")
    print("=" * 60)
    
    # CSV 필드 크기 제한 증가
    csv.field_size_limit(1000000)
    
    for csv_file in csv_files:
        csv_path = raw_data_dir / csv_file
        if not csv_path.exists():
            print(f"❌ 파일 없음: {csv_file}")
            continue
            
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    folder = row.get('folder', '').strip()
                    if folder:
                        all_folders.append(folder)
                        
                        # Integration 관련 폴더 찾기
                        if 'integration' in folder.lower() or 'extending' in folder.lower():
                            integration_folders.append(folder)
                        
        except Exception as e:
            print(f"❌ {csv_file} 처리 중 오류: {e}")
    
    # 폴더 빈도 계산
    folder_counts = Counter(all_folders)
    integration_counts = Counter(integration_folders)
    
    print(f"✅ 총 {len(all_folders)}개 문서, {len(set(all_folders))}개 고유 폴더 발견")
    print()
    
    print("🔌 Integration 관련 폴더들:")
    print("=" * 50)
    for folder, count in integration_counts.most_common():
        print(f"{count:3d}개 - {folder}")
    
    print()
    print("📁 상위 20개 폴더:")
    print("=" * 50)
    for folder, count in folder_counts.most_common(20):
        print(f"{count:3d}개 - {folder}")
    
    return folder_counts, integration_counts

if __name__ == "__main__":
    folder_counts, integration_counts = check_folder_names()
    
    if integration_counts:
        print("\n🎯 다음 단계: Integration 관련 폴더 중 하나를 선택하여 문서 추출")
    else:
        print("\n🔍 'integration' 키워드로 찾을 수 없음. 다른 키워드 시도 필요")
