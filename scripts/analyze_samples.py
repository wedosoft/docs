#!/usr/bin/env python3
import csv
import os
from html import unescape
import re

# CSV 필드 크기 제한 증가
csv.field_size_limit(1000000)

def analyze_csv_files():
    csv_dir = "raw_data"
    all_articles = []
    
    for i in range(1, 6):
        filename = f"merged_articles_links_replaced_freshservice_part{i}.csv"
        filepath = os.path.join(csv_dir, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # 기본 정보만 추출
                    article = {
                        'id': row.get('id', ''),
                        'title': row.get('title', ''),
                        'folder_name': row.get('folder_name', ''),
                        'category_name': row.get('category_name', ''),
                        'description': row.get('description', ''),
                        'file_part': i
                    }
                    all_articles.append(article)
    
    return all_articles

def select_diverse_samples(articles, count=5):
    """다양한 카테고리에서 샘플 선택"""
    categories = {}
    
    # 카테고리별로 그룹화
    for article in articles:
        cat = article['category_name']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(article)
    
    # 각 카테고리에서 1개씩 선택 (제목이 명확한 것 우선)
    selected = []
    for cat_name, cat_articles in categories.items():
        if len(selected) >= count:
            break
            
        # 제목이 짧고 명확한 것 우선 선택
        cat_articles.sort(key=lambda x: len(x['title']))
        
        for article in cat_articles:
            if len(article['title']) > 10 and len(article['title']) < 100:
                selected.append(article)
                print(f"✓ Selected from '{cat_name}': {article['title'][:60]}...")
                break
    
    return selected[:count]

def main():
    print("📊 Analyzing CSV files...")
    articles = analyze_csv_files()
    print(f"Found {len(articles)} articles total")
    
    print("\n🎯 Selecting diverse samples...")
    samples = select_diverse_samples(articles, 5)
    
    print(f"\n📋 Selected {len(samples)} samples:")
    for i, sample in enumerate(samples, 1):
        print(f"\n{i}. Title: {sample['title']}")
        print(f"   Category: {sample['category_name']}")
        print(f"   Folder: {sample['folder_name']}")
        print(f"   File: part{sample['file_part']}")
        print(f"   ID: {sample['id']}")

if __name__ == "__main__":
    main()
