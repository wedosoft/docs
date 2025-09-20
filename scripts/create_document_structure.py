#!/usr/bin/env python3
"""
CSV to JSON Document Structure Converter

이 스크립트는 documents/merged*.csv 파일들을 분석해서
카테고리 → 폴더 → 아티클 3depth 구조의 JSON 파일을 생성합니다.

사용법:
    python scripts/create_document_structure.py

출력:
    documents/document_structure.json
"""

import csv
import json
import glob
import os
from typing import Dict, List, Any
import html
import re


def clean_html_description(description: str) -> str:
    """HTML 태그를 제거하고 텍스트만 추출"""
    if not description:
        return ""
    
    # HTML 엔티티 디코드
    description = html.unescape(description)
    
    # HTML 태그 제거
    description = re.sub(r'<[^>]+>', '', description)
    
    # 여러 공백을 하나로 정리
    description = re.sub(r'\s+', ' ', description)
    
    # 앞뒤 공백 제거
    description = description.strip()
    
    # 너무 긴 경우 150자로 제한
    if len(description) > 150:
        description = description[:147] + "..."
    
    return description


def process_csv_files(csv_pattern: str) -> Dict[str, Any]:
    """모든 CSV 파일을 처리해서 문서 구조를 생성"""
    
    document_structure = {}
    total_articles = 0
    
    # CSV 필드 크기 제한 늘리기 (큰 HTML 콘텐츠 처리를 위해)
    csv.field_size_limit(1000000)
    
    # CSV 파일들을 찾아서 처리
    csv_files = glob.glob(csv_pattern)
    csv_files.sort()  # 파일명 순으로 정렬
    
    print(f"처리할 CSV 파일 수: {len(csv_files)}")
    
    for csv_file in csv_files:
        print(f"처리 중: {os.path.basename(csv_file)}")
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # 필요한 필드 추출
                    title = row.get('title', '').strip()
                    category_name = row.get('category_name', '').strip()
                    folder_name = row.get('folder_name', '').strip()
                    description = row.get('description', '').strip()
                    position = row.get('position', '0')
                    
                    # 빈 값 체크
                    if not title or not category_name or not folder_name:
                        continue
                    
                    # Position을 정수로 변환
                    try:
                        position = int(position)
                    except (ValueError, TypeError):
                        position = 0
                    
                    # HTML에서 깨끗한 설명 추출
                    clean_desc = clean_html_description(description)
                    
                    # 문서 구조에 추가
                    if category_name not in document_structure:
                        document_structure[category_name] = {}
                    
                    if folder_name not in document_structure[category_name]:
                        document_structure[category_name][folder_name] = []
                    
                    # 아티클 정보 생성
                    article = {
                        "title": title,
                        "position": position,
                        "description": clean_desc
                    }
                    
                    document_structure[category_name][folder_name].append(article)
                    total_articles += 1
                    
        except Exception as e:
            print(f"오류 발생 in {csv_file}: {e}")
            continue
    
    # 각 폴더의 아티클들을 position 순으로 정렬
    for category_name in document_structure:
        for folder_name in document_structure[category_name]:
            document_structure[category_name][folder_name].sort(
                key=lambda x: x['position']
            )
    
    print(f"\n=== 처리 완료 ===")
    print(f"총 카테고리 수: {len(document_structure)}")
    
    total_folders = sum(len(folders) for folders in document_structure.values())
    print(f"총 폴더 수: {total_folders}")
    print(f"총 아티클 수: {total_articles}")
    
    return document_structure


def generate_summary_stats(structure: Dict[str, Any]) -> Dict[str, Any]:
    """문서 구조의 통계 정보 생성"""
    
    stats = {
        "total_categories": len(structure),
        "total_folders": 0,
        "total_articles": 0,
        "categories": {}
    }
    
    for category_name, folders in structure.items():
        folder_count = len(folders)
        article_count = sum(len(articles) for articles in folders.values())
        
        stats["total_folders"] += folder_count
        stats["total_articles"] += article_count
        
        stats["categories"][category_name] = {
            "folder_count": folder_count,
            "article_count": article_count,
            "folders": {}
        }
        
        # 각 폴더별 아티클 수
        for folder_name, articles in folders.items():
            stats["categories"][category_name]["folders"][folder_name] = {
                "article_count": len(articles)
            }
    
    return stats


def main():
    """메인 실행 함수"""
    
    # 현재 스크립트의 디렉토리를 기준으로 경로 설정
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    # CSV 파일 패턴
    csv_pattern = os.path.join(repo_root, "documents", "merged_articles_links_replaced_freshservice_part*.csv")
    
    print("=== Freshservice 문서 구조 생성 시작 ===")
    print(f"CSV 파일 패턴: {csv_pattern}")
    
    # CSV 파일들 처리
    document_structure = process_csv_files(csv_pattern)
    
    if not document_structure:
        print("처리할 데이터가 없습니다.")
        return
    
    # 통계 정보 생성
    stats = generate_summary_stats(document_structure)
    
    # JSON 출력 파일 경로
    output_file = os.path.join(repo_root, "documents", "document_structure.json")
    stats_file = os.path.join(repo_root, "documents", "document_stats.json")
    
    # JSON 파일로 저장
    try:
        # 메인 문서 구조 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(document_structure, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 문서 구조 JSON 파일 생성 완료: {output_file}")
        
        # 통계 정보 저장
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 통계 정보 JSON 파일 생성 완료: {stats_file}")
        
        # 카테고리 목록 출력
        print(f"\n=== 카테고리 목록 ===")
        for i, (category_name, folders) in enumerate(document_structure.items(), 1):
            folder_count = len(folders)
            article_count = sum(len(articles) for articles in folders.values())
            print(f"{i:2d}. {category_name} ({folder_count}개 폴더, {article_count}개 아티클)")
        
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")


if __name__ == "__main__":
    main()