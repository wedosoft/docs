#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV에서 실제 content 내용을 확인하는 스크립트
"""

import csv
from pathlib import Path

def check_content_samples():
    """CSV에서 실제 content 샘플들을 확인"""
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    csv_file = "merged_articles_links_replaced_freshservice_part1.csv"
    csv_path = raw_data_dir / csv_file
    
    # CSV 필드 크기 제한 증가
    csv.field_size_limit(1000000)
    
    print("🔍 실제 content 내용 샘플 확인...")
    print("=" * 60)
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # 필드명 확인
            print("📋 CSV 필드명들:")
            fieldnames = reader.fieldnames
            for i, field in enumerate(fieldnames, 1):
                print(f"{i:2d}. {field}")
            print()
            
            # 처음 3개 문서의 content 샘플 확인
            for i, row in enumerate(reader):
                if i >= 3:
                    break
                    
                title = row.get('title', 'No Title')
                category = row.get('category_name', 'No Category')
                folder = row.get('folder_name', 'No Folder')
                content = row.get('content', '')
                
                print(f"📄 문서 {i+1}: {title}")
                print(f"📁 카테고리: {category}")
                print(f"📂 폴더: {folder}")
                print(f"📝 Content 길이: {len(content):,}자")
                print("📋 Content 샘플 (처음 500자):")
                print("-" * 50)
                print(content[:500])
                print("-" * 50)
                
                # 이미지 관련 키워드 검색
                image_keywords = ['img', 'image', 'src=', 'amazonaws', '.png', '.jpg', '.gif', 'attachment', 'figure']
                found_keywords = []
                for keyword in image_keywords:
                    if keyword.lower() in content.lower():
                        count = content.lower().count(keyword.lower())
                        found_keywords.append(f"{keyword}({count})")
                
                if found_keywords:
                    print(f"🖼️ 이미지 관련 키워드: {', '.join(found_keywords)}")
                else:
                    print("🖼️ 이미지 관련 키워드 없음")
                print()
                
    except Exception as e:
        print(f"❌ 오류: {e}")
        return

if __name__ == "__main__":
    check_content_samples()
