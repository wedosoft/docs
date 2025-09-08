#!/usr/bin/env python3
"""
📊 CSV 카테고리 분석 스크립트

목적: Freshservice CSV 데이터의 카테고리별 분포를 분석하여 
     다음 작업 우선순위를 결정하는 데 필요한 정보 제공

사용법: python3 scripts/analyze_csv_categories.py
"""

import csv
import os
from collections import defaultdict, Counter
import re

# CSV 필드 크기 제한 증가
csv.field_size_limit(1000000)

def analyze_csv_files():
    """5개 CSV 파일을 분석하여 카테고리별 분포 파악"""
    
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    # 분석 결과 저장용
    categories = defaultdict(int)
    folders = defaultdict(int)
    images_count = 0
    total_docs = 0
    
    # 복잡도 분석용
    simple_docs = 0  # 이미지 없고 짧은 문서
    medium_docs = 0  # 이미지 있거나 중간 길이
    complex_docs = 0 # 이미지 많고 긴 문서
    
    print("📊 Freshservice CSV 카테고리 분석")
    print("=" * 50)
    
    for i, file_path in enumerate(csv_files, 1):
        if not os.path.exists(file_path):
            print(f"❌ Part {i}: 파일 없음 - {file_path}")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader)
                
                # 필요한 컬럼 인덱스 찾기
                try:
                    category_idx = headers.index('category_name')
                    folder_idx = headers.index('folder_name') 
                    description_idx = headers.index('description')
                    title_idx = headers.index('title')
                except ValueError as e:
                    print(f"❌ Part {i}: 필요한 컬럼을 찾을 수 없음 - {e}")
                    continue
                
                part_count = 0
                for row in reader:
                    if len(row) <= max(category_idx, folder_idx, description_idx, title_idx):
                        continue
                        
                    category = row[category_idx] if row[category_idx] else "미분류"
                    folder = row[folder_idx] if row[folder_idx] else "미분류"
                    description = row[description_idx] if row[description_idx] else ""
                    title = row[title_idx] if row[title_idx] else ""
                    
                    categories[category] += 1
                    folders[folder] += 1
                    part_count += 1
                    total_docs += 1
                    
                    # 이미지 포함 여부 확인
                    img_count = len(re.findall(r'<img[^>]*>', description))
                    if img_count > 0:
                        images_count += 1
                    
                    # 복잡도 분석
                    content_length = len(description)
                    if img_count == 0 and content_length < 2000:
                        simple_docs += 1
                    elif img_count <= 2 and content_length < 5000:
                        medium_docs += 1
                    else:
                        complex_docs += 1
                
                print(f"✅ Part {i}: {part_count}개 문서 분석 완료")
                
        except Exception as e:
            print(f"❌ Part {i}: 오류 발생 - {e}")
    
    # 결과 출력
    print(f"\n📈 전체 분석 결과")
    print("=" * 50)
    print(f"총 문서 수: {total_docs:,}개")
    print(f"이미지 포함 문서: {images_count:,}개 ({images_count/total_docs*100:.1f}%)")
    print(f"카테고리 수: {len(categories)}개")
    print(f"폴더 수: {len(folders)}개")
    
    print(f"\n📊 복잡도별 분포")
    print("=" * 30)
    print(f"간단 (이미지 없음, 짧음): {simple_docs:,}개 ({simple_docs/total_docs*100:.1f}%)")
    print(f"보통 (이미지 적음, 중간): {medium_docs:,}개 ({medium_docs/total_docs*100:.1f}%)")
    print(f"복잡 (이미지 많음, 긺): {complex_docs:,}개 ({complex_docs/total_docs*100:.1f}%)")
    
    print(f"\n🗂️ 상위 카테고리 (TOP 10)")
    print("=" * 40)
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
        percentage = count/total_docs*100
        print(f"{category:30} {count:3}개 ({percentage:4.1f}%)")
    
    print(f"\n📁 상위 폴더 (TOP 15)")
    print("=" * 40)
    for folder, count in sorted(folders.items(), key=lambda x: x[1], reverse=True)[:15]:
        percentage = count/total_docs*100
        print(f"{folder:35} {count:3}개 ({percentage:4.1f}%)")
    
    # 추천 다음 작업 폴더
    print(f"\n🎯 다음 작업 추천")
    print("=" * 30)
    print("1. 간단한 문서부터 시작 (이미지 없는 문서)")
    print("2. 기존 완성된 카테고리 확장")
    print("3. 문서 수가 많은 폴더 우선")
    
    # 기존 완성된 폴더와 매칭
    completed_folders = {
        'form-fields-and-form-templates': 16,
        'user-management': 20, 
        'setting-up-freshservice': 9,
        'self-service-portal-introduction': 5
    }
    
    print(f"\n📋 우선 작업 후보")
    print("=" * 25)
    for folder, count in sorted(folders.items(), key=lambda x: x[1], reverse=True):
        if count >= 5:  # 5개 이상인 폴더만
            folder_clean = folder.lower().replace(' ', '-')
            if folder_clean not in [f.lower() for f in completed_folders.keys()]:
                print(f"• {folder} ({count}개 문서)")
                if count >= 20:
                    print("  → 우선순위 높음 (문서 수 많음)")
                elif count >= 10:
                    print("  → 우선순위 보통")
                else:
                    print("  → 우선순위 낮음")

def main():
    """메인 실행 함수"""
    if not os.path.exists('raw_data'):
        print("❌ raw_data 폴더가 존재하지 않습니다.")
        return
    
    analyze_csv_files()
    
    print(f"\n✅ 분석 완료!")
    print(f"📝 다음 단계: documents/project-status.md에 결과 반영")

if __name__ == "__main__":
    main()
