#!/usr/bin/env python3
"""
Freshservice 문서 파일럿 프로그램용 50개 샘플 선정 스크립트
- 카테고리별 균형 유지
- 복잡도별 다양성 확보 (이미지, 테이블, 링크, 길이)
- 품질 테스트를 위한 대표성 있는 샘플 구성
"""

import pandas as pd
import re
import json
from collections import defaultdict
import random

def analyze_content_complexity(description):
    """콘텐츠 복잡도 분석"""
    desc = str(description)
    
    return {
        'length': len(desc),
        'images': len(re.findall(r'<img[^>]*>', desc)),
        'tables': len(re.findall(r'<table[^>]*>', desc)),
        'links': len(re.findall(r'<a[^>]*>', desc)),
        'lists': len(re.findall(r'<ul[^>]*>|<ol[^>]*>', desc)),
        'headers': len(re.findall(r'<h[1-6][^>]*>', desc))
    }

def categorize_complexity(complexity):
    """복잡도 카테고리 분류"""
    score = (
        complexity['length'] / 1000 +
        complexity['images'] * 2 +
        complexity['tables'] * 3 +
        complexity['links'] * 0.5 +
        complexity['lists'] * 1 +
        complexity['headers'] * 0.5
    )
    
    if score < 5:
        return 'simple'
    elif score < 15:
        return 'medium'
    else:
        return 'complex'

def load_all_data():
    """모든 CSV 파일 로드 및 통합"""
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    all_data = []
    for file_path in csv_files:
        df = pd.read_csv(file_path)
        df['source_file'] = file_path
        all_data.append(df)
    
    return pd.concat(all_data, ignore_index=True)

def select_pilot_samples(df, target_count=50):
    """다양성을 고려한 파일럿 샘플 선정"""
    
    # 각 문서의 복잡도 분석
    df['complexity'] = df['description'].apply(analyze_content_complexity)
    df['complexity_category'] = df['complexity'].apply(categorize_complexity)
    
    # 카테고리별 분포 계산
    category_counts = df['category_name'].value_counts()
    print("=== 전체 카테고리 분포 ===")
    for cat, count in category_counts.items():
        print(f"{cat}: {count}개")
    
    # 복잡도별 분포 계산
    complexity_counts = df['complexity_category'].value_counts()
    print("\n=== 복잡도별 분포 ===")
    for comp, count in complexity_counts.items():
        print(f"{comp}: {count}개")
    
    # 카테고리별 비례 배분 계산
    total_docs = len(df)
    category_targets = {}
    for cat, count in category_counts.items():
        proportion = count / total_docs
        target = max(1, round(proportion * target_count))  # 최소 1개 보장
        category_targets[cat] = target
    
    # 목표 수에 맞게 조정
    total_target = sum(category_targets.values())
    if total_target != target_count:
        # 가장 큰 카테고리에서 조정
        largest_cat = max(category_targets.keys(), key=lambda x: category_targets[x])
        category_targets[largest_cat] += target_count - total_target
    
    print("\n=== 카테고리별 목표 샘플 수 ===")
    for cat, target in category_targets.items():
        print(f"{cat}: {target}개")
    
    # 각 카테고리에서 복잡도별로 균형있게 선정
    selected_samples = []
    
    for category, target_num in category_targets.items():
        cat_df = df[df['category_name'] == category].copy()
        
        if len(cat_df) == 0:
            continue
            
        # 복잡도별 균형 선정
        complexity_types = ['simple', 'medium', 'complex']
        samples_per_complexity = target_num // 3
        remainder = target_num % 3
        
        for i, comp_type in enumerate(complexity_types):
            comp_df = cat_df[cat_df['complexity_category'] == comp_type]
            
            # 해당 복잡도 문서가 없으면 전체에서 선정
            if len(comp_df) == 0:
                comp_df = cat_df
            
            # 이번 복잡도에서 선정할 개수
            num_to_select = samples_per_complexity
            if i < remainder:
                num_to_select += 1
            
            if num_to_select > 0 and len(comp_df) > 0:
                if len(comp_df) >= num_to_select:
                    # 다양성을 위해 랜덤 선택 (재현가능하도록 시드 설정)
                    random.seed(42)
                    selected = comp_df.sample(n=num_to_select, random_state=42)
                else:
                    selected = comp_df
                
                selected_samples.append(selected)
    
    # 결과 통합
    final_samples = pd.concat(selected_samples, ignore_index=True)
    
    print(f"\n=== 최종 선정 결과 ===")
    print(f"총 선정 문서 수: {len(final_samples)}")
    
    # 선정된 샘플의 분포 확인
    final_category_dist = final_samples['category_name'].value_counts()
    print("\n선정된 카테고리 분포:")
    for cat, count in final_category_dist.items():
        print(f"  {cat}: {count}개")
    
    final_complexity_dist = final_samples['complexity_category'].value_counts()
    print("\n선정된 복잡도 분포:")
    for comp, count in final_complexity_dist.items():
        print(f"  {comp}: {count}개")
    
    return final_samples

def main():
    print("Freshservice 파일럿 프로그램용 50개 샘플 선정 시작...")
    
    # 데이터 로드
    df = load_all_data()
    print(f"전체 문서 수: {len(df)}")
    
    # 샘플 선정
    pilot_samples = select_pilot_samples(df, 50)
    
    # 결과 저장
    output_file = 'scripts/pilot_samples.json'
    
    # JSON 직렬화를 위해 복잡도 정보를 문자열로 변환
    pilot_data = []
    for _, row in pilot_samples.iterrows():
        sample_data = {
            'id': row['id'],
            'title': row['title'],
            'category_name': row['category_name'],
            'folder_name': row['folder_name'],
            'path': row['path'],
            'complexity_category': row['complexity_category'],
            'complexity_details': row['complexity'],
            'source_file': row['source_file']
        }
        pilot_data.append(sample_data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(pilot_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n파일럿 샘플 목록이 {output_file}에 저장되었습니다.")
    
    # 선정된 샘플 미리보기
    print("\n=== 선정된 샘플 미리보기 (첫 10개) ===")
    for i, sample in enumerate(pilot_data[:10]):
        print(f"{i+1}. [{sample['complexity_category']}] {sample['title'][:60]}...")
        print(f"   카테고리: {sample['category_name']}")
        print(f"   폴더: {sample['folder_name']}")
        print()

if __name__ == "__main__":
    main()
