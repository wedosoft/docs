#!/usr/bin/env python3
import csv
import os
import json
from html import unescape
import re
from bs4 import BeautifulSoup

# CSV 필드 크기 제한 증가
csv.field_size_limit(1000000)

def extract_sample_details():
    """선택된 5개 샘플의 상세 정보 추출"""
    selected_ids = ['217539', '50000006424', '50000009713', '50000005586', '234757']
    samples = {}
    
    for i in range(1, 6):
        filename = f"raw_data/merged_articles_links_replaced_freshservice_part{i}.csv"
        
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('id') in selected_ids:
                        # HTML 내용을 텍스트로 변환
                        description = row.get('description', '')
                        soup = BeautifulSoup(description, 'html.parser')
                        
                        # 이미지 태그 처리
                        for img in soup.find_all('img'):
                            src = img.get('src', '')
                            alt = img.get('alt', 'Image')
                            img.replace_with(f"\n![{alt}]({src})\n")
                        
                        # 링크 태그 처리  
                        for a in soup.find_all('a'):
                            href = a.get('href', '')
                            text = a.get_text()
                            if href and text:
                                a.replace_with(f"[{text}]({href})")
                        
                        clean_text = soup.get_text()
                        
                        sample = {
                            'id': row.get('id'),
                            'title': row.get('title', ''),
                            'description': clean_text,
                            'folder_name': row.get('folder_name', ''),
                            'category_name': row.get('category_name', ''),
                            'path': row.get('path', ''),
                            'tags': row.get('tags', ''),
                            'file_part': i
                        }
                        samples[row.get('id')] = sample
    
    return samples

def save_samples_json(samples):
    """샘플 데이터를 JSON으로 저장"""
    with open('selected_samples.json', 'w', encoding='utf-8') as f:
        json.dump(samples, f, ensure_ascii=False, indent=2)

def main():
    print("🔍 Extracting detailed information for selected samples...")
    samples = extract_sample_details()
    
    print(f"\n📁 Found {len(samples)} samples with details:")
    for sample_id, sample in samples.items():
        print(f"\n📄 ID: {sample_id}")
        print(f"   Title: {sample['title']}")
        print(f"   Category: {sample['category_name']}")
        print(f"   Folder: {sample['folder_name']}")
        print(f"   Content length: {len(sample['description'])} chars")
        print(f"   Path: {sample['path']}")
    
    save_samples_json(samples)
    print(f"\n💾 Saved sample details to 'selected_samples.json'")

if __name__ == "__main__":
    main()
