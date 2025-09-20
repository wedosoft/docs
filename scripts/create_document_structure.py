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
    """HTML 설명을 그대로 유지 (HTML 태그 포함)"""
    if not description:
        return ""
    
    # HTML 엔티티 디코드만 수행
    description = html.unescape(description)
    
    # 앞뒤 공백만 제거
    description = description.strip()
    
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
                    
                    # HTML 설명을 그대로 유지
                    html_desc = clean_html_description(description)
                    
                    # 문서 구조에 추가
                    if category_name not in document_structure:
                        document_structure[category_name] = {}
                    
                    if folder_name not in document_structure[category_name]:
                        document_structure[category_name][folder_name] = []
                    
                    # 아티클 정보 생성
                    article = {
                        "title": title,
                        "position": position,
                        "description": html_desc
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


def create_category_slug(category_name: str) -> str:
    """카테고리명을 파일명에 적합한 slug로 변환"""
    # 특수 문자 제거 및 소문자 변환
    slug = category_name.lower()
    
    # 공백을 하이픈으로 변환
    slug = re.sub(r'\s+', '-', slug)
    
    # 특수 문자 제거 (알파벳, 숫자, 하이픈만 유지)
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    
    # 연속된 하이픈을 하나로 정리
    slug = re.sub(r'-+', '-', slug)
    
    # 앞뒤 하이픈 제거
    slug = slug.strip('-')
    
    return slug


def save_category_json_files(document_structure: Dict[str, Any], output_dir: str):
    """각 카테고리별로 별도의 JSON 파일 생성"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    category_files = []
    
    for category_name, folders in document_structure.items():
        # 카테고리명을 파일명으로 변환
        category_slug = create_category_slug(category_name)
        filename = f"{category_slug}.json"
        filepath = os.path.join(output_dir, filename)
        
        # 카테고리 구조 (폴더 → 아티클)
        category_data = folders
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(category_data, f, ensure_ascii=False, indent=2)
            
            category_files.append({
                'category': category_name,
                'slug': category_slug,
                'filename': filename,
                'folder_count': len(folders),
                'article_count': sum(len(articles) for articles in folders.values())
            })
            
            print(f"✅ {filename} 생성 완료 ({len(folders)}개 폴더, {sum(len(articles) for articles in folders.values())}개 아티클)")
            
        except Exception as e:
            print(f"❌ {filename} 생성 실패: {e}")
    
    return category_files


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
    
    # 카테고리별 JSON 파일 생성
    output_dir = os.path.join(repo_root, "documents", "categories")
    print(f"\n=== 카테고리별 JSON 파일 생성 ===")
    category_files = save_category_json_files(document_structure, output_dir)
    
    # 통계 파일 저장
    stats_file = os.path.join(repo_root, "documents", "document_stats.json")
    
    try:
        # 통계 정보 저장
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 통계 정보 JSON 파일 생성 완료: {stats_file}")
        
        # 카테고리 파일 목록 저장
        category_index = {
            "total_categories": len(category_files),
            "categories": category_files
        }
        
        index_file = os.path.join(output_dir, "index.json")
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(category_index, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 카테고리 인덱스 파일 생성 완료: {index_file}")
        
        # 결과 요약
        print(f"\n=== 생성 완료 ===")
        print(f"총 {len(category_files)}개 카테고리 JSON 파일 생성")
        print(f"총 폴더 수: {stats['total_folders']}")
        print(f"총 아티클 수: {stats['total_articles']}")
        
        # 카테고리 목록 출력
        print(f"\n=== 생성된 JSON 파일 목록 ===")
        for i, category_file in enumerate(category_files, 1):
            print(f"{i:2d}. {category_file['filename']} "
                  f"({category_file['folder_count']}개 폴더, {category_file['article_count']}개 아티클)")
        
    except Exception as e:
        print(f"❌ 파일 저장 오류: {e}")


if __name__ == "__main__":
    main()