#!/usr/bin/env python3
"""
Freshservice 문서 변환 자동화 스크립트
원본 CSV에서 특정 제목의 HTML 내용을 추출하여 새로운 Markdown 템플릿으로 변환

사용법:
python extract_content.py "문서 제목"
"""

import pandas as pd
import sys
import glob
from pathlib import Path

def extract_content_from_csv(title_to_search):
    """CSV 파일에서 특정 제목의 내용을 추출"""
    
    # raw_data 폴더의 모든 CSV 파일 찾기
    csv_files = glob.glob("raw_data/merged_articles_links_replaced_freshservice_part*.csv")
    
    if not csv_files:
        print("❌ CSV 파일을 찾을 수 없습니다.")
        return None
    
    print(f"🔍 '{title_to_search}' 검색 중...")
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            
            # 제목으로 검색 (대소문자 구분 없이)
            matches = df[df['title'].str.contains(title_to_search, case=False, na=False)]
            
            if not matches.empty:
                print(f"✅ {csv_file}에서 발견!")
                match = matches.iloc[0]
                
                print(f"📋 제목: {match['title']}")
                print(f"📂 카테고리: {match.get('category_name', 'N/A')}")
                print(f"📁 폴더: {match.get('folder_name', 'N/A')}")
                print("=" * 80)
                print("📄 HTML 내용:")
                print("=" * 80)
                print(match['description'])
                print("=" * 80)
                
                return {
                    'title': match['title'],
                    'category': match.get('category_name', ''),
                    'folder': match.get('folder_name', ''),
                    'content': match['description']
                }
                
        except Exception as e:
            print(f"❌ {csv_file} 읽기 오류: {e}")
            continue
    
    print(f"❌ '{title_to_search}' 제목을 찾을 수 없습니다.")
    return None

def suggest_similar_titles(search_term):
    """유사한 제목들을 제안"""
    
    csv_files = glob.glob("raw_data/merged_articles_links_replaced_freshservice_part*.csv")
    all_titles = []
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            all_titles.extend(df['title'].dropna().tolist())
        except:
            continue
    
    # 검색어를 포함하는 제목들 찾기
    suggestions = [title for title in all_titles if search_term.lower() in title.lower()]
    
    if suggestions:
        print(f"\n💡 유사한 제목들:")
        for i, suggestion in enumerate(suggestions[:10], 1):
            print(f"  {i}. {suggestion}")
    
    return suggestions

def main():
    if len(sys.argv) != 2:
        print("사용법: python extract_content.py \"문서 제목\"")
        print("\n예시:")
        print("python extract_content.py \"Add members\"")
        print("python extract_content.py \"Creating departments\"")
        sys.exit(1)
    
    title_to_search = sys.argv[1]
    
    # 내용 추출
    result = extract_content_from_csv(title_to_search)
    
    if not result:
        # 유사한 제목 제안
        suggest_similar_titles(title_to_search)
        
        print(f"\n💡 사용 가능한 명령어:")
        print(f"python extract_content.py \"members observers\"")
        print(f"python extract_content.py \"departments\"")
        print(f"python extract_content.py \"user information\"")

if __name__ == "__main__":
    main()
