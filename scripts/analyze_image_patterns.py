#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSV에서 실제 이미지 패턴을 분석하는 스크립트
"""

import csv
import re
from pathlib import Path

def analyze_image_patterns():
    """CSV에서 실제 이미지 패턴들을 분석"""
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    csv_file = "merged_articles_links_replaced_freshservice_part1.csv"
    csv_path = raw_data_dir / csv_file
    
    # CSV 필드 크기 제한 증가
    csv.field_size_limit(1000000)
    
    image_patterns = {
        '<img': 0,
        '![': 0,
        'https://s3.amazonaws.com': 0,
        'src="': 0,
        'src=\'': 0,
        '.png': 0,
        '.jpg': 0,
        '.jpeg': 0,
        '.gif': 0,
        '.svg': 0
    }
    
    sample_images = []
    docs_with_images = 0
    total_docs = 0
    
    print("🔍 이미지 패턴 분석 중...")
    print("=" * 50)
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for i, row in enumerate(reader):
                if i >= 100:  # 처음 100개 문서만 분석
                    break
                    
                total_docs += 1
                content = row.get('content', '')
                title = row.get('title', '')
                
                # 각 패턴 개수 세기
                has_images = False
                for pattern in image_patterns:
                    count = content.count(pattern)
                    image_patterns[pattern] += count
                    if count > 0:
                        has_images = True
                
                if has_images:
                    docs_with_images += 1
                    
                    # 샘플 이미지 추출 (처음 몇 개만)
                    if len(sample_images) < 3:
                        # img 태그 찾기
                        img_matches = re.findall(r'<img[^>]*>', content)
                        if img_matches:
                            sample_images.append({
                                'title': title,
                                'img_tags': img_matches[:2]  # 처음 2개만
                            })
                
    except Exception as e:
        print(f"❌ 오류: {e}")
        return
    
    print("📊 이미지 패턴 분석 결과:")
    print("=" * 40)
    for pattern, count in image_patterns.items():
        print(f"{pattern:25s}: {count:4d}개")
    
    print(f"\n📈 통계:")
    print(f"총 분석 문서: {total_docs}개")
    print(f"이미지 포함 문서: {docs_with_images}개 ({docs_with_images/total_docs*100:.1f}%)")
    
    print(f"\n🖼️ 샘플 이미지 태그:")
    print("=" * 50)
    for i, sample in enumerate(sample_images, 1):
        print(f"{i}. {sample['title']}")
        for img_tag in sample['img_tags']:
            print(f"   {img_tag[:100]}...")
        print()

if __name__ == "__main__":
    analyze_image_patterns()
