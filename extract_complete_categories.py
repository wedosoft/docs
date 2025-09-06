#!/usr/bin/env python3
import csv
import os
from collections import defaultdict

def extract_complete_structure():
    raw_data_path = '/Users/alan/GitHub/docs/raw_data'
    
    # 카테고리/폴더 구조를 저장할 딕셔너리
    structure = defaultdict(set)
    categories = set()
    folders = set()
    
    # CSV 파일들 처리 - 필드 크기 제한 늘림
    csv.field_size_limit(1000000)  # 1MB로 제한 증가
    
    csv_files = [
        'merged_articles_links_replaced_freshservice_part1.csv',
        'merged_articles_links_replaced_freshservice_part2.csv',
        'merged_articles_links_replaced_freshservice_part3.csv',
        'merged_articles_links_replaced_freshservice_part4.csv',
        'merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    total_rows = 0
    processed_rows = 0
    
    for csv_file in csv_files:
        file_path = os.path.join(raw_data_path, csv_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)  # 헤더 스킵
                
                print(f"\n처리 중: {csv_file}")
                
                for row_num, row in enumerate(reader, start=2):
                    total_rows += 1
                    if len(row) >= 28:
                        folder_name = row[17].strip() if row[17] else ""  # folder_name
                        category_name = row[27].strip() if row[27] else ""  # category_name
                        
                        if category_name:
                            categories.add(category_name)
                            
                        if folder_name:
                            folders.add(folder_name)
                            
                        if category_name and folder_name:
                            structure[category_name].add(folder_name)
                            processed_rows += 1
                        
        except Exception as e:
            print(f"파일 {csv_file} 처리 중 오류: {e}")
            continue
    
    print(f"\n=== 처리 결과 ===")
    print(f"총 행 수: {total_rows}")
    print(f"처리된 행 수: {processed_rows}")
    print(f"총 카테고리 수: {len(categories)}")
    print(f"총 폴더 수: {len(folders)}")
    
    # 카테고리 목록 출력
    print(f"\n=== 모든 카테고리 목록 ===")
    for i, category in enumerate(sorted(categories), 1):
        print(f"{i:2d}. {category}")
    
    # 카테고리별 폴더 구조 출력
    print(f"\n=== 카테고리별 폴더 구조 ===")
    for category in sorted(structure.keys()):
        folder_count = len(structure[category])
        print(f"\n📁 {category} ({folder_count}개 폴더)")
        for folder in sorted(structure[category]):
            print(f"  └── {folder}")
    
    return structure, categories, folders

if __name__ == "__main__":
    structure, categories, folders = extract_complete_structure()
