#!/usr/bin/env python3
"""
문서 구조 JSON 활용 예시

이 스크립트는 생성된 document_structure.json 파일을 활용하는 방법을 보여줍니다.
문서 작업을 쉽게 할 수 있도록 다양한 검색/조회 기능을 제공합니다.

사용법:
    python scripts/use_document_structure.py
"""

import json
import os
from typing import Dict, List, Any


class DocumentStructureHelper:
    """문서 구조 JSON을 활용하기 위한 헬퍼 클래스"""
    
    def __init__(self, json_file: str):
        """JSON 파일을 로드"""
        with open(json_file, 'r', encoding='utf-8') as f:
            self.structure = json.load(f)
        
        print(f"✅ 문서 구조 로드 완료: {len(self.structure)}개 카테고리")
    
    def list_categories(self):
        """모든 카테고리 목록 출력"""
        print("\n=== 카테고리 목록 ===")
        for i, category in enumerate(self.structure.keys(), 1):
            folder_count = len(self.structure[category])
            article_count = sum(len(articles) for articles in self.structure[category].values())
            print(f"{i:2d}. {category} ({folder_count}개 폴더, {article_count}개 아티클)")
    
    def search_articles(self, keyword: str):
        """키워드로 아티클 검색"""
        keyword = keyword.lower()
        results = []
        
        for category_name, folders in self.structure.items():
            for folder_name, articles in folders.items():
                for article in articles:
                    if (keyword in article['title'].lower() or 
                        keyword in article['description'].lower()):
                        results.append({
                            'category': category_name,
                            'folder': folder_name,
                            'article': article
                        })
        
        print(f"\n=== '{keyword}' 검색 결과: {len(results)}개 ===")
        for i, result in enumerate(results[:10], 1):  # 상위 10개만 표시
            print(f"{i}. [{result['category']}] > [{result['folder']}]")
            print(f"   📄 {result['article']['title']}")
            print(f"   📝 {result['article']['description'][:80]}...")
            print()
        
        if len(results) > 10:
            print(f"... 외 {len(results) - 10}개 결과 더")
    
    def get_category_details(self, category_name: str):
        """특정 카테고리의 상세 정보"""
        if category_name not in self.structure:
            print(f"❌ 카테고리 '{category_name}'을 찾을 수 없습니다.")
            return
        
        folders = self.structure[category_name]
        
        print(f"\n=== {category_name} 상세 정보 ===")
        print(f"폴더 수: {len(folders)}")
        
        total_articles = sum(len(articles) for articles in folders.values())
        print(f"총 아티클 수: {total_articles}")
        
        print(f"\n📁 폴더 목록:")
        for i, (folder_name, articles) in enumerate(folders.items(), 1):
            print(f"{i:2d}. {folder_name} ({len(articles)}개 아티클)")
    
    def get_folder_details(self, category_name: str, folder_name: str):
        """특정 폴더의 상세 정보"""
        if category_name not in self.structure:
            print(f"❌ 카테고리 '{category_name}'을 찾을 수 없습니다.")
            return
        
        if folder_name not in self.structure[category_name]:
            print(f"❌ 폴더 '{folder_name}'을 찾을 수 없습니다.")
            return
        
        articles = self.structure[category_name][folder_name]
        
        print(f"\n=== [{category_name}] > [{folder_name}] ===")
        print(f"아티클 수: {len(articles)}")
        
        print(f"\n📄 아티클 목록:")
        for i, article in enumerate(articles, 1):
            print(f"{i:2d}. {article['title']} (위치: {article['position']})")
            print(f"    📝 {article['description'][:60]}...")
    
    def generate_category_markdown(self, category_name: str):
        """카테고리의 마크다운 목차 생성"""
        if category_name not in self.structure:
            print(f"❌ 카테고리 '{category_name}'을 찾을 수 없습니다.")
            return
        
        folders = self.structure[category_name]
        
        print(f"\n=== {category_name} 마크다운 목차 ===")
        print(f"# {category_name}\n")
        
        for folder_name, articles in folders.items():
            print(f"## {folder_name}")
            print()
            
            for article in articles:
                print(f"- {article['title']}")
            
            print()


def main():
    """메인 실행 함수"""
    
    # JSON 파일 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    json_file = os.path.join(repo_root, "documents", "document_structure.json")
    
    if not os.path.exists(json_file):
        print(f"❌ JSON 파일을 찾을 수 없습니다: {json_file}")
        print("먼저 create_document_structure.py를 실행해주세요.")
        return
    
    # 헬퍼 클래스 초기화
    helper = DocumentStructureHelper(json_file)
    
    # 예시 사용법들
    print("\n" + "="*60)
    print("📚 문서 구조 JSON 활용 예시")
    print("="*60)
    
    # 1. 전체 카테고리 목록
    helper.list_categories()
    
    # 2. 키워드 검색 예시
    helper.search_articles("ticket")
    
    # 3. 특정 카테고리 상세 정보
    helper.get_category_details("Freshservice FAQs")
    
    # 4. 특정 폴더 상세 정보
    helper.get_folder_details("Freshservice FAQs", "Service Desk FAQ")
    
    # 5. 마크다운 목차 생성 예시
    helper.generate_category_markdown("End User Guide")
    
    print("\n" + "="*60)
    print("✅ 예시 실행 완료!")
    print("이제 document_structure.json을 활용해서 문서 작업을 시작할 수 있습니다.")
    print("="*60)


if __name__ == "__main__":
    main()