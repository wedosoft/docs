#!/usr/bin/env python3
import csv
import os
from collections import defaultdict

# 카테고리와 폴더 구조를 추출하는 스크립트
def extract_categories_and_folders():
    raw_data_path = '/Users/alan/GitHub/docs/raw_data'
    
    # 카테고리/폴더 구조를 저장할 딕셔너리
    structure = defaultdict(set)
    
    # CSV 파일들 처리
    csv_files = [
        'merged_articles_links_replaced_freshservice_part1.csv',
        'merged_articles_links_replaced_freshservice_part2.csv',
        'merged_articles_links_replaced_freshservice_part3.csv',
        'merged_articles_links_replaced_freshservice_part4.csv',
        'merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    for csv_file in csv_files:
        file_path = os.path.join(raw_data_path, csv_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)  # 헤더 스킵
                
                print(f"\n처리 중: {csv_file}")
                print(f"헤더 확인: {header[17]} (18번째 컬럼), {header[27]} (28번째 컬럼)")
                
                for row_num, row in enumerate(reader, start=2):
                    if len(row) >= 28:
                        folder_name = row[17].strip() if row[17] else ""  # 18번째 컬럼 (0-based 17)
                        category_name = row[27].strip() if row[27] else ""  # 28번째 컬럼 (0-based 27)
                        
                        if category_name and folder_name:
                            structure[category_name].add(folder_name)
                    
                    # 처음 몇 줄만 디버깅용으로 출력
                    if row_num <= 5:
                        folder = row[17] if len(row) > 17 else "N/A"
                        category = row[27] if len(row) > 27 else "N/A"
                        print(f"  행 {row_num}: 폴더='{folder}', 카테고리='{category}'")
                        
        except Exception as e:
            print(f"파일 {csv_file} 처리 중 오류: {e}")
            continue
    
    # 결과 출력
    print("\n=== 추출된 카테고리/폴더 구조 ===")
    for category in sorted(structure.keys()):
        print(f"\n📁 {category}")
        for folder in sorted(structure[category]):
            print(f"  └── {folder}")
    
    return structure

if __name__ == "__main__":
    structure = extract_categories_and_folders()
