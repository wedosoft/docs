#!/usr/bin/env python3
"""
단순 텍스트 분석기
기준: 순수 텍스트만 있는 문서 VS 나머지 모든 문서
"""

import pandas as pd
import re
import json
from pathlib import Path

def is_pure_text(html_content):
    """
    순수 텍스트인지 판단 (간단한 기준)
    - 복잡 문서: 이미지, 테이블, 리스트, 코드블록 등이 있는 문서
    - 단순 문서: 위 요소들이 없는 나머지 모든 문서
    """
    if pd.isna(html_content) or html_content == '':
        return True  # 빈 내용은 순수 텍스트로 간주
    
    html_str = str(html_content)
    
    # 복잡한 요소들 (이것들이 있으면 복잡 문서)
    complex_elements = [
        '<img',           # 이미지
        '<table',         # 테이블
        '<tr>',           # 테이블 행
        '<th>',           # 테이블 헤더  
        '<td>',           # 테이블 셀
        '<ul>',           # 순서없는 리스트
        '<ol>',           # 순서있는 리스트
        '<li>',           # 리스트 아이템
        '<pre>',          # 코드 블록
        '<code>',         # 인라인 코드
        '<iframe',        # 프레임
        '<video',         # 비디오
        '<audio',         # 오디오
        'style=',         # 인라인 스타일
        '<script',        # 스크립트
        '<form',          # 폼
        '<input',         # 입력 필드
        '<select',        # 선택 박스
        '<textarea',      # 텍스트 영역
    ]
    
    # 하나라도 복잡한 요소가 있으면 복잡 문서
    for element in complex_elements:
        if element in html_str:
            return False
    
    return True  # 복합 요소가 없으면 순수 텍스트

def analyze_faq_documents():
    """FAQ 문서만 분석하여 순수 텍스트와 복합 문서로 분류"""
    
    # CSV 파일들 읽기
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    pure_text_docs = []
    complex_docs = []
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            print(f"분석 중: {csv_file} ({len(df)}개 항목)")
            
            for idx, row in df.iterrows():
                title = str(row.get('title', ''))
                description = str(row.get('description', ''))
                html_content = str(row.get('description', ''))
                path = str(row.get('path', ''))
                
                # FAQ 문서만 필터링
                if 'faq' not in path.lower():
                    continue
                
                doc_info = {
                    'title': title,
                    'path': path,
                    'content_length': len(html_content),
                    'csv_file': csv_file,
                    'row_index': idx
                }
                
                if is_pure_text(html_content):
                    pure_text_docs.append(doc_info)
                else:
                    complex_docs.append(doc_info)
        
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {csv_file}")
        except Exception as e:
            print(f"오류 발생 ({csv_file}): {e}")
    
    # 결과 요약
    total_docs = len(pure_text_docs) + len(complex_docs)
    pure_text_ratio = len(pure_text_docs) / total_docs * 100 if total_docs > 0 else 0
    
    print("\n" + "="*50)
    print("📊 분석 결과")
    print("="*50)
    print(f"전체 문서: {total_docs:,}개")
    print(f"순수 텍스트: {len(pure_text_docs):,}개 ({pure_text_ratio:.1f}%)")
    print(f"복합 문서: {len(complex_docs):,}개 ({100-pure_text_ratio:.1f}%)")
    print()
    
    print("🤖 자동번역 권장:")
    print(f"  - 순수 텍스트 {len(pure_text_docs):,}개 → 즉시 자동번역 가능")
    print(f"  - 복합 문서 {len(complex_docs):,}개 → 수동 처리 필요")
    
    # 결과를 JSON 파일로 저장
    results = {
        'summary': {
            'total_docs': total_docs,
            'pure_text_count': len(pure_text_docs),
            'complex_count': len(complex_docs),
            'pure_text_ratio': pure_text_ratio
        },
        'pure_text_docs': pure_text_docs,
        'complex_docs': complex_docs
    }
    
    with open('simple_text_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n결과가 'simple_text_analysis.json'에 저장되었습니다.")
    
    # 순수 텍스트 문서 샘플 보기
    if pure_text_docs:
        print("\n" + "="*50)
        print("📝 순수 텍스트 문서 샘플 (처음 5개)")
        print("="*50)
        for i, doc in enumerate(pure_text_docs[:5]):
            print(f"{i+1}. {doc['title']}")
            print(f"   경로: {doc['path']}")
            print(f"   길이: {doc['content_length']}자")
            print()
    
    # 복합 문서 샘플 보기
    if complex_docs:
        print("\n" + "="*50)
        print("🔧 복합 문서 샘플 (처음 5개)")
        print("="*50)
        for i, doc in enumerate(complex_docs[:5]):
            print(f"{i+1}. {doc['title']}")
            print(f"   경로: {doc['path']}")
            print(f"   길이: {doc['content_length']}자")
            print()

if __name__ == "__main__":
    analyze_faq_documents()
