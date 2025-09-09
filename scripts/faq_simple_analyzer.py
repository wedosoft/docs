#!/usr/bin/env python3
"""
FAQ 단순화된 2단계 복잡도 분석기
- AUTO: 순수 텍스트만 있는 문서 (이미지, 테이블, 코드 없음)
- MANUAL: 그 외 모든 문서 (이미지, 테이블, 코드 등 포함)
"""

import pandas as pd
import re
import json
from pathlib import Path
import html

def analyze_simple_complexity(html_content):
    """단순화된 복잡도 분석 - 텍스트만 vs 기타 요소 포함"""
    if pd.isna(html_content):
        return {
            'is_text_only': True,
            'has_images': False,
            'has_tables': False,
            'has_code_blocks': False,
            'processing_recommendation': 'AUTO'
        }
    
    html_str = str(html_content)
    
    # 복잡 요소 검사
    has_images = '<img' in html_str
    has_tables = '<table' in html_str or '<th>' in html_str or '<td>' in html_str
    has_code_blocks = '<pre>' in html_str or '<code>' in html_str
    
    # 단순 텍스트 여부 판단
    is_text_only = not (has_images or has_tables or has_code_blocks)
    
    # 처리 방법 결정
    processing_recommendation = 'AUTO' if is_text_only else 'MANUAL'
    
    return {
        'is_text_only': is_text_only,
        'has_images': has_images,
        'has_tables': has_tables,
        'has_code_blocks': has_code_blocks,
        'image_count': html_str.count('<img') if has_images else 0,
        'processing_recommendation': processing_recommendation
    }

def analyze_faq_simple():
    """FAQ 단순화된 분석"""
    
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    all_results = []
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            faq_df = df[df['category_name'] == 'Freshservice FAQs']
            
            if len(faq_df) == 0:
                print(f"처리 중: {csv_file} (FAQ 문서 없음)")
                continue
                
            print(f"처리 중: {csv_file} (FAQ 문서 {len(faq_df)}개)")
            
            for idx, row in faq_df.iterrows():
                title = str(row.get('title', ''))
                description = str(row.get('description', ''))
                folder_name = str(row.get('folder_name', ''))
                position = row.get('position', 999)
                
                # 단순화된 복잡도 분석
                complexity = analyze_simple_complexity(description)
                
                result = {
                    'title': title,
                    'folder_name': folder_name,
                    'position': position,
                    'description_preview': description[:100] + '...' if len(description) > 100 else description,
                    **complexity
                }
                
                all_results.append(result)
                
        except Exception as e:
            print(f"오류 발생 {csv_file}: {e}")
    
    return all_results

def generate_simple_summary(results):
    """단순화된 요약 리포트"""
    
    # 폴더별 분류
    by_folder = {}
    for result in results:
        folder = result['folder_name']
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(result)
    
    # 처리 방법별 분류
    auto_count = len([r for r in results if r['processing_recommendation'] == 'AUTO'])
    manual_count = len([r for r in results if r['processing_recommendation'] == 'MANUAL'])
    
    print("=" * 60)
    print("📊 FAQ 단순화된 분석 결과 (텍스트만 vs 기타 요소)")
    print("=" * 60)
    print(f"총 FAQ 수: {len(results)}")
    print(f"🤖 자동 처리 (텍스트만): {auto_count}개 ({auto_count/len(results)*100:.1f}%)")
    print(f"🔥 수동 처리 (이미지/테이블/코드 포함): {manual_count}개 ({manual_count/len(results)*100:.1f}%)")
    print()
    
    # 폴더별 상세 분석 (자동 처리 비율 순)
    print("📋 폴더별 분석 (텍스트만 문서 비율 순):")
    print("-" * 60)
    
    folder_stats = []
    for folder, items in by_folder.items():
        auto = len([i for i in items if i['processing_recommendation'] == 'AUTO'])
        manual = len([i for i in items if i['processing_recommendation'] == 'MANUAL'])
        
        folder_stats.append({
            'folder': folder,
            'total': len(items),
            'auto': auto,
            'manual': manual,
            'auto_ratio': auto / len(items) * 100
        })
    
    # 텍스트만 비율 순으로 정렬
    folder_stats.sort(key=lambda x: x['auto_ratio'], reverse=True)
    
    for stat in folder_stats:
        print(f"{stat['folder'][:35]:35} | 텍스트:{stat['auto']:2}개 복합:{stat['manual']:2}개 | 총:{stat['total']:2}개 ({stat['auto_ratio']:4.1f}% 텍스트)")
    
    print()
    
    # 복합 요소가 있는 문서들 예시
    manual_items = [r for r in results if r['processing_recommendation'] == 'MANUAL']
    if manual_items:
        print("🔥 복합 요소 포함 문서들 (상위 10개):")
        print("-" * 60)
        
        for item in manual_items[:10]:
            features = []
            if item['has_images']:
                features.append(f"이미지 {item['image_count']}개")
            if item['has_tables']:
                features.append("테이블")
            if item['has_code_blocks']:
                features.append("코드")
            
            feature_text = ", ".join(features) if features else "복합 요소"
            print(f"- [{item['folder_name']}] {item['title'][:40]}...")
            print(f"  특징: {feature_text}")
    
    return {
        'total': len(results),
        'auto': auto_count,
        'manual': manual_count,
        'folder_stats': folder_stats
    }

def save_simple_results(results, output_file='faq_simple_analysis.json'):
    """단순화된 분석 결과 저장"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"📁 상세 분석 결과 저장: {output_file}")
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")

if __name__ == "__main__":
    print("🔍 FAQ 단순화된 분석 시작...")
    print("📋 분류 기준:")
    print("  🤖 AUTO: 순수 텍스트만 (이미지/테이블/코드 없음)")
    print("  🔥 MANUAL: 복합 요소 포함 (이미지/테이블/코드 있음)")
    print()
    
    # 단순화된 분석 실행
    results = analyze_faq_simple()
    
    if not results:
        print("❌ FAQ 문서를 찾을 수 없습니다.")
        exit(1)
    
    # 요약 리포트 생성
    summary = generate_simple_summary(results)
    
    # 상세 결과 저장
    save_simple_results(results)
    
    print("\n✅ 단순화된 FAQ 분석 완료!")
    print(f"📊 요약: 텍스트만 {summary['auto']}개, 복합 요소 {summary['manual']}개")
