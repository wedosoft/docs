#!/usr/bin/env python3
"""
FAQ 전용 복잡도 분석기
Freshservice FAQs 카테고리만 분석하여 효율적인 작업 계획 수립
"""

import pandas as pd
import re
import json
from pathlib import Path
import html

def analyze_content_complexity(html_content):
    """HTML 콘텐츠의 복잡도를 분석"""
    if pd.isna(html_content):
        return {
            'complexity_score': 0,
            'has_images': False,
            'has_tables': False,
            'has_code_blocks': False,
            'has_lists': False,
            'has_formatting': False,
            'image_count': 0,
            'content_length': 0,
            'processing_recommendation': 'AUTO'
        }
    
    html_str = str(html_content)
    content_length = len(html_str)
    complexity_score = 0
    
    # 이미지 분석
    image_count = html_str.count('<img')
    has_images = image_count > 0
    if has_images:
        complexity_score += 5 * image_count  # 이미지마다 5점
    
    # 테이블 분석
    has_tables = '<table' in html_str or '<th>' in html_str or '<td>' in html_str
    if has_tables:
        table_count = html_str.count('<table')
        complexity_score += 3 * table_count  # 테이블마다 3점
    
    # 코드 블록 분석
    has_code_blocks = '<pre>' in html_str or '<code>' in html_str
    if has_code_blocks:
        code_count = html_str.count('<pre>') + html_str.count('<code>')
        complexity_score += 2 * code_count  # 코드 블록마다 2점
    
    # 리스트 분석
    has_lists = '<ul>' in html_str or '<ol>' in html_str
    if has_lists:
        list_count = html_str.count('<ul>') + html_str.count('<ol>')
        complexity_score += 1 * list_count  # 리스트마다 1점
    
    # 서식 분석 (굵게, 기울임, 제목 등)
    formatting_patterns = ['<strong>', '<b>', '<em>', '<i>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>']
    has_formatting = any(pattern in html_str for pattern in formatting_patterns)
    if has_formatting:
        formatting_count = sum(html_str.count(pattern) for pattern in formatting_patterns)
        complexity_score += 0.5 * formatting_count  # 서식마다 0.5점
    
    # 전체 길이 보너스
    if content_length > 2000:
        complexity_score += 2
    elif content_length > 1000:
        complexity_score += 1
    
    # 처리 방법 결정
    if complexity_score >= 10:
        processing_recommendation = 'MANUAL'  # 수동 처리
    elif complexity_score >= 5:
        processing_recommendation = 'REVIEW'  # 검토 필요
    else:
        processing_recommendation = 'AUTO'    # 자동 처리
    
    return {
        'complexity_score': complexity_score,
        'has_images': has_images,
        'has_tables': has_tables,
        'has_code_blocks': has_code_blocks,
        'has_lists': has_lists,
        'has_formatting': has_formatting,
        'image_count': image_count,
        'content_length': content_length,
        'processing_recommendation': processing_recommendation
    }

def analyze_faq_only():
    """FAQ 카테고리만 분석하여 복잡도별로 분류"""
    
    # CSV 파일들 읽기
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
            # FAQ 카테고리만 필터링
            faq_df = df[df['category_name'] == 'Freshservice FAQs']
            
            if len(faq_df) == 0:
                print(f"처리 중: {csv_file} (FAQ 문서 없음)")
                continue
                
            print(f"처리 중: {csv_file} (FAQ 문서 {len(faq_df)}개)")
            
            for idx, row in faq_df.iterrows():
                title = str(row.get('title', ''))
                description = str(row.get('description', ''))
                html_content = str(row.get('description', ''))  # 실제 HTML은 description 컬럼에 있음
                folder_name = str(row.get('folder_name', ''))
                
                # 복잡도 분석
                complexity = analyze_content_complexity(html_content)
                
                result = {
                    'title': title,
                    'folder_name': folder_name,
                    'description_preview': description[:100] + '...' if len(description) > 100 else description,
                    **complexity
                }
                
                all_results.append(result)
                
        except Exception as e:
            print(f"오류 발생 {csv_file}: {e}")
    
    return all_results

def generate_faq_summary_report(results):
    """FAQ 분석 결과 요약 리포트 생성"""
    
    # 폴더별 분류
    by_folder = {}
    for result in results:
        folder = result['folder_name']
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(result)
    
    # 처리 방법별 분류
    manual_count = len([r for r in results if r['processing_recommendation'] == 'MANUAL'])
    review_count = len([r for r in results if r['processing_recommendation'] == 'REVIEW'])
    auto_count = len([r for r in results if r['processing_recommendation'] == 'AUTO'])
    
    print("=" * 60)
    print("📊 FAQ 전용 복잡도 분석 결과")
    print("=" * 60)
    print(f"총 FAQ 수: {len(results)}")
    print(f"🔥 수동 처리 필요: {manual_count}개 ({manual_count/len(results)*100:.1f}%)")
    print(f"⚡ 검토 필요: {review_count}개 ({review_count/len(results)*100:.1f}%)")
    print(f"🤖 자동 처리 가능: {auto_count}개 ({auto_count/len(results)*100:.1f}%)")
    print()
    
    # 폴더별 상세 분석 (자동 처리 가능한 순서대로)
    print("📋 폴더별 분석 (자동 처리 가능 문서 많은 순):")
    print("-" * 60)
    
    folder_stats = []
    for folder, items in by_folder.items():
        manual = len([i for i in items if i['processing_recommendation'] == 'MANUAL'])
        review = len([i for i in items if i['processing_recommendation'] == 'REVIEW'])
        auto = len([i for i in items if i['processing_recommendation'] == 'AUTO'])
        
        folder_stats.append({
            'folder': folder,
            'total': len(items),
            'auto': auto,
            'review': review,
            'manual': manual,
            'auto_ratio': auto / len(items) * 100
        })
    
    # 자동 처리 가능 비율 순으로 정렬
    folder_stats.sort(key=lambda x: x['auto_ratio'], reverse=True)
    
    for stat in folder_stats:
        print(f"{stat['folder'][:35]:35} | 자동:{stat['auto']:2}개 검토:{stat['review']:2}개 수동:{stat['manual']:2}개 | 총:{stat['total']:2}개 ({stat['auto_ratio']:4.1f}% 자동)")
    
    print()
    
    # 수동 처리가 필요한 항목들 상세 정보
    manual_items = [r for r in results if r['processing_recommendation'] == 'MANUAL']
    if manual_items:
        print("🔥 수동 처리 필요 항목들 (상위 10개):")
        print("-" * 60)
        
        for item in sorted(manual_items, key=lambda x: x['complexity_score'], reverse=True)[:10]:
            features = []
            if item['has_images']:
                features.append(f"이미지 {item['image_count']}개")
            if item['has_tables']:
                features.append("테이블")
            if item['has_lists']:
                features.append("목록")
            
            feature_text = ", ".join(features) if features else "긴 문서"
            print(f"- [{item['folder_name']}] {item['title'][:40]}...")
            print(f"  점수: {item['complexity_score']}, 특징: {feature_text}")
    
    return {
        'total': len(results),
        'manual': manual_count,
        'review': review_count,
        'auto': auto_count,
        'folder_stats': folder_stats
    }

def save_faq_results(results, output_file='faq_only_analysis.json'):
    """상세 분석 결과를 JSON 파일로 저장"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"📁 상세 분석 결과 저장: {output_file}")
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")

if __name__ == "__main__":
    print("🔍 FAQ 전용 복잡도 분석 시작...")
    
    # FAQ만 분석 실행
    results = analyze_faq_only()
    
    if not results:
        print("❌ FAQ 문서를 찾을 수 없습니다.")
        exit(1)
    
    # 요약 리포트 생성
    summary = generate_faq_summary_report(results)
    
    # 상세 결과 저장
    save_faq_results(results)
    
    print("\n✅ FAQ 분석 완료!")
    print(f"📊 요약: 수동 {summary['manual']}개, 검토 {summary['review']}개, 자동 {summary['auto']}개")
