#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
우선순위 폴더의 문서 목록 추출 스크립트
첫 번째 타겟: "Extending Freshservice with Integrations" 폴더 (60개 문서)
"""

import csv
import os
from pathlib import Path

def extract_folder_documents(folder_name, max_docs=10):
    """특정 폴더의 문서들을 추출하여 복잡도별로 정렬"""
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    csv_files = [
        "merged_articles_links_replaced_freshservice_part1.csv",
        "merged_articles_links_replaced_freshservice_part2.csv", 
        "merged_articles_links_replaced_freshservice_part3.csv",
        "merged_articles_links_replaced_freshservice_part4.csv",
        "merged_articles_links_replaced_freshservice_part5.csv"
    ]
    
    matching_docs = []
    
    print(f"🔍 '{folder_name}' 폴더의 문서 검색 중...")
    print("=" * 60)
    
    for csv_file in csv_files:
        csv_path = raw_data_dir / csv_file
        if not csv_path.exists():
            print(f"❌ 파일 없음: {csv_file}")
            continue
            
        try:
            # CSV 필드 크기 제한 증가
            csv.field_size_limit(1000000)
            
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # 폴더명 확인 (정확한 필드명 사용)
                    folder_name_csv = row.get('folder_name', '').strip()
                    if folder_name_csv == folder_name:
                        # 복잡도 계산
                        content = row.get('desc_un_html', '') or row.get('description', '')
                        title = row.get('title', '')
                        
                        # 이미지 수 계산
                        image_count = content.count('<img') + content.count('![')
                        
                        # 내용 길이
                        content_length = len(content)
                        
                        # 복잡도 점수 (이미지 수 * 100 + 내용 길이 / 100)
                        complexity_score = image_count * 100 + content_length / 100
                        
                        # 복잡도 카테고리
                        if image_count == 0 and content_length < 3000:
                            complexity = "간단"
                            priority = 1
                        elif image_count <= 2 and content_length < 8000:
                            complexity = "보통"
                            priority = 2
                        else:
                            complexity = "복잡"
                            priority = 3
                        
                        matching_docs.append({
                            'title': title,
                            'folder': folder_name_csv,
                            'category': row.get('category_name', ''),
                            'content_length': content_length,
                            'image_count': image_count,
                            'complexity': complexity,
                            'complexity_score': complexity_score,
                            'priority': priority,
                            'slug': row.get('slug', ''),
                            'id': row.get('id', ''),
                            'content': content[:200] + "..." if len(content) > 200 else content
                        })
                        
        except Exception as e:
            print(f"❌ {csv_file} 처리 중 오류: {e}")
    
    # 복잡도 순으로 정렬 (간단한 것부터)
    matching_docs.sort(key=lambda x: (x['priority'], x['complexity_score']))
    
    print(f"✅ 총 {len(matching_docs)}개 문서 발견")
    print()
    
    # 복잡도별 통계
    simple_count = len([d for d in matching_docs if d['complexity'] == '간단'])
    medium_count = len([d for d in matching_docs if d['complexity'] == '보통'])
    complex_count = len([d for d in matching_docs if d['complexity'] == '복잡'])
    
    print("📊 복잡도별 분포:")
    print(f"  간단: {simple_count}개")
    print(f"  보통: {medium_count}개")
    print(f"  복잡: {complex_count}개")
    print()
    
    # 상위 문서들 출력 (간단한 것부터)
    print(f"🎯 우선 작업 추천 (간단한 문서 {min(max_docs, len(matching_docs))}개):")
    print("=" * 80)
    
    for i, doc in enumerate(matching_docs[:max_docs], 1):
        print(f"{i:2d}. [{doc['complexity']}] {doc['title']}")
        print(f"    📁 {doc['folder']}")
        print(f"    📷 이미지: {doc['image_count']}개 | 📝 길이: {doc['content_length']:,}자")
        print(f"    🆔 ID: {doc['id']} | 🔗 Slug: {doc['slug']}")
        print()
    
    return matching_docs

if __name__ == "__main__":
    folder_name = "Automations and Triggers"
    docs = extract_folder_documents(folder_name, max_docs=15)
    
    print(f"📋 다음 단계: 위 목록에서 간단한 문서부터 수작업 변환 시작")
    print(f"💡 품질 기준: docs/freshworks/freshservice/ 기존 완성 문서 참조")
