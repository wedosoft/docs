#!/usr/bin/env python3
"""
문서 구조 JSON 활용 예시 (카테고리별 파일 버전)

이 스크립트는 생성된 카테고리별 JSON 파일들을 활용하는 방법을 보여줍니다.
문서 작업을 쉽게 할 수 있도록 다양한 검색/조회 기능을 제공합니다.

사용법:
    python scripts/use_document_structure.py
"""

import json
import os
from typing import Dict, List, Any


class DocumentStructureHelper:
    """문서 구조 JSON을 활용하기 위한 헬퍼 클래스 (카테고리별 파일 버전)"""
    
    def __init__(self, categories_dir: str):
        """카테고리 디렉토리 설정"""
        self.categories_dir = categories_dir
        self.index_file = os.path.join(categories_dir, "index.json")
        
        # 인덱스 파일 로드
        with open(self.index_file, 'r', encoding='utf-8') as f:
            self.index = json.load(f)
        
        print(f"✅ 카테고리 인덱스 로드 완료: {self.index['total_categories']}개 카테고리")
    
    def load_category(self, category_slug: str) -> Dict[str, Any]:
        """특정 카테고리 JSON 파일 로드"""
        filepath = os.path.join(self.categories_dir, f"{category_slug}.json")
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"카테고리 파일을 찾을 수 없습니다: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def list_categories(self):
        """모든 카테고리 목록 출력"""
        print("\n=== 카테고리 목록 ===")
        for i, category in enumerate(self.index['categories'], 1):
            print(f"{i:2d}. {category['category']} ({category['filename']})")
            print(f"    {category['folder_count']}개 폴더, {category['article_count']}개 아티클")
    
    def search_articles(self, keyword: str):
        """키워드로 아티클 검색 (모든 카테고리)"""
        keyword = keyword.lower()
        results = []
        
        for category_info in self.index['categories']:
            try:
                category_data = self.load_category(category_info['slug'])
                
                for folder_name, articles in category_data.items():
                    for article in articles:
                        if (keyword in article['title'].lower() or 
                            keyword in article['description'].lower()):
                            results.append({
                                'category': category_info['category'],
                                'folder': folder_name,
                                'article': article
                            })
            except Exception as e:
                print(f"⚠️ {category_info['filename']} 검색 중 오류: {e}")
                continue
        
        print(f"\n=== '{keyword}' 검색 결과: {len(results)}개 ===")
        for i, result in enumerate(results[:10], 1):  # 상위 10개만 표시
            print(f"{i}. [{result['category']}] > [{result['folder']}]")
            print(f"   📄 {result['article']['title']}")
            print(f"   📝 {result['article']['description'][:80]}...")
            print()
        
        if len(results) > 10:
            print(f"... 외 {len(results) - 10}개 결과 더")
    
    def get_category_details(self, category_slug: str):
        """특정 카테고리의 상세 정보"""
        # 인덱스에서 카테고리 정보 찾기
        category_info = None
        for cat in self.index['categories']:
            if cat['slug'] == category_slug:
                category_info = cat
                break
        
        if not category_info:
            print(f"❌ 카테고리 '{category_slug}'을 찾을 수 없습니다.")
            return
        
        try:
            category_data = self.load_category(category_slug)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return
        
        print(f"\n=== {category_info['category']} 상세 정보 ===")
        print(f"파일명: {category_info['filename']}")
        print(f"폴더 수: {len(category_data)}")
        
        total_articles = sum(len(articles) for articles in category_data.values())
        print(f"총 아티클 수: {total_articles}")
        
        print(f"\n📁 폴더 목록:")
        for i, (folder_name, articles) in enumerate(category_data.items(), 1):
            print(f"{i:2d}. {folder_name} ({len(articles)}개 아티클)")
    
    def get_folder_details(self, category_slug: str, folder_name: str):
        """특정 폴더의 상세 정보"""
        try:
            category_data = self.load_category(category_slug)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return
        
        if folder_name not in category_data:
            print(f"❌ 폴더 '{folder_name}'을 찾을 수 없습니다.")
            return
        
        articles = category_data[folder_name]
        
        print(f"\n=== [{category_slug}] > [{folder_name}] ===")
        print(f"아티클 수: {len(articles)}")
        
        print(f"\n📄 아티클 목록:")
        for i, article in enumerate(articles, 1):
            print(f"{i:2d}. {article['title']} (위치: {article['position']})")
            print(f"    📝 {article['description'][:60]}...")
            print(f"    🏷️ HTML 포함: {'<' in article['description']}")
    
    def generate_category_markdown(self, category_slug: str):
        """카테고리의 마크다운 목차 생성"""
        try:
            category_data = self.load_category(category_slug)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            return
        
        # 카테고리 정보 찾기
        category_name = category_slug
        for cat in self.index['categories']:
            if cat['slug'] == category_slug:
                category_name = cat['category']
                break
        
        print(f"\n=== {category_name} 마크다운 목차 ===")
        print(f"# {category_name}\n")
        
        for folder_name, articles in category_data.items():
            print(f"## {folder_name}")
            print()
            
            for article in sorted(articles, key=lambda x: x['position']):
                print(f"- {article['title']}")
            
            print()


def main():
    """메인 실행 함수"""
    
    # 카테고리 디렉토리 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    categories_dir = os.path.join(repo_root, "documents", "categories")
    
    if not os.path.exists(categories_dir):
        print(f"❌ 카테고리 디렉토리를 찾을 수 없습니다: {categories_dir}")
        print("먼저 create_document_structure.py를 실행해주세요.")
        return
    
    # 헬퍼 클래스 초기화
    helper = DocumentStructureHelper(categories_dir)
    
    # 예시 사용법들
    print("\n" + "="*60)
    print("📚 문서 구조 JSON 활용 예시 (카테고리별 파일 버전)")
    print("="*60)
    
    # 1. 전체 카테고리 목록
    helper.list_categories()
    
    # 2. 키워드 검색 예시
    helper.search_articles("ticket")
    
    # 3. 특정 카테고리 상세 정보
    helper.get_category_details("freshservice-faqs")
    
    # 4. 특정 폴더 상세 정보
    helper.get_folder_details("freshservice-faqs", "Service Desk FAQ")
    
    # 5. 마크다운 목차 생성 예시
    helper.generate_category_markdown("end-user-guide")
    
    print("\n" + "="*60)
    print("✅ 예시 실행 완료!")
    print("이제 카테고리별 JSON 파일들을 활용해서 문서 작업을 시작할 수 있습니다.")
    print("="*60)


if __name__ == "__main__":
    main()