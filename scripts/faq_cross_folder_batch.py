#!/usr/bin/env python3
"""
FAQ 크로스 폴더 배치 처리 시스템
- 복잡도별로 모든 폴더를 크로스하여 처리
- 최종에는 원본 position 순서로 재배치
"""

import pandas as pd
import json
from collections import defaultdict
import os

def load_faq_data_with_positions():
    """FAQ 데이터를 원본 position 정보와 함께 로드"""
    
    # CSV 파일들 읽기
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv'
    ]
    
    all_faq_data = []
    
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        faq_df = df[df['category_name'] == 'Freshservice FAQs']
        
        for idx, row in faq_df.iterrows():
            faq_data = {
                'id': row['id'],
                'title': str(row['title']),
                'description': str(row['description']),
                'folder_name': str(row['folder_name']),
                'position': row.get('position', 999),  # 기본값 999
                'csv_file': csv_file
            }
            all_faq_data.append(faq_data)
    
    return all_faq_data

def load_complexity_analysis():
    """복잡도 분석 결과 로드"""
    with open('faq_only_analysis.json', 'r') as f:
        return json.load(f)

def create_cross_folder_batches():
    """크로스 폴더 배치 생성"""
    
    # 원본 데이터와 복잡도 분석 결과 로드
    faq_data = load_faq_data_with_positions()
    complexity_data = load_complexity_analysis()
    
    # title을 키로 하는 복잡도 매핑 생성
    complexity_map = {item['title']: item['processing_recommendation'] for item in complexity_data}
    
    # 복잡도별로 분류
    batches = {
        'AUTO': [],     # SIMPLE 복잡도
        'REVIEW': [],   # 중간 복잡도  
        'MANUAL': []    # 높은 복잡도
    }
    
    # 폴더별로 원본 순서 추적
    folder_positions = defaultdict(list)
    
    for faq in faq_data:
        title = faq['title']
        folder = faq['folder_name']
        
        # 복잡도 정보 추가
        complexity = complexity_map.get(title, 'AUTO')
        faq['complexity'] = complexity
        
        # 배치에 추가
        batches[complexity].append(faq)
        
        # 폴더별 원본 순서 기록
        folder_positions[folder].append({
            'title': title,
            'position': faq['position'],
            'complexity': complexity
        })
    
    return batches, folder_positions

def generate_batch_work_plan():
    """배치 작업 계획 생성"""
    
    batches, folder_positions = create_cross_folder_batches()
    
    print("🚀 FAQ 크로스 폴더 배치 처리 계획")
    print("=" * 60)
    
    # 배치별 통계
    for batch_name, items in batches.items():
        folder_counts = defaultdict(int)
        for item in items:
            folder_counts[item['folder_name']] += 1
        
        print(f"\n📦 {batch_name} 배치: {len(items)}개 문서")
        print("-" * 40)
        
        # 폴더별 개수 표시 (많은 순)
        sorted_folders = sorted(folder_counts.items(), key=lambda x: x[1], reverse=True)
        for folder, count in sorted_folders[:10]:  # 상위 10개만
            print(f"  {folder[:30]:30} {count:2}개")
        if len(sorted_folders) > 10:
            print(f"  ... 및 {len(sorted_folders)-10}개 폴더 더")
    
    # 폴더별 원본 순서 분석
    print(f"\n📁 폴더별 원본 순서 분석")
    print("-" * 40)
    
    for folder, positions in list(folder_positions.items())[:5]:  # 상위 5개 폴더만
        sorted_positions = sorted(positions, key=lambda x: x['position'])
        print(f"\n{folder}:")
        for pos in sorted_positions[:3]:  # 첫 3개만
            print(f"  {pos['position']:2}. {pos['title'][:40]}... [{pos['complexity']}]")
        if len(sorted_positions) > 3:
            print(f"  ... 및 {len(sorted_positions)-3}개 더")
    
    return batches, folder_positions

def generate_reorder_script():
    """원본 순서 재배치 스크립트 생성"""
    
    _, folder_positions = create_cross_folder_batches()
    
    reorder_commands = []
    
    print(f"\n🔄 원본 순서 재배치 명령어")
    print("-" * 40)
    
    for folder, positions in folder_positions.items():
        # 원본 순서로 정렬
        sorted_positions = sorted(positions, key=lambda x: x['position'])
        
        reorder_command = f"""
# {folder} 폴더 재배치
folder_path = "docs/freshworks/freshservice/freshservice-faqs/{folder.lower().replace(' ', '-').replace('&', 'and')}"
original_order = {[pos['title'] for pos in sorted_positions]}
reorder_faq_file(folder_path, original_order)
"""
        reorder_commands.append(reorder_command)
    
    # 재배치 스크립트 파일 생성
    script_content = f"""#!/usr/bin/env python3
'''
FAQ 원본 순서 재배치 스크립트
복잡도 순으로 작업 완료 후 원본 Freshservice 순서로 재배치
'''

def reorder_faq_file(folder_path, original_order):
    '''특정 폴더의 FAQ를 원본 순서로 재배치'''
    # 구현 예정
    pass

if __name__ == "__main__":
    print("FAQ 원본 순서 재배치 시작...")
    
    {''.join(reorder_commands)}
    
    print("재배치 완료!")
"""
    
    with open('scripts/faq_reorder.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("📁 재배치 스크립트 생성: scripts/faq_reorder.py")

if __name__ == "__main__":
    try:
        batches, folder_positions = generate_batch_work_plan()
        generate_reorder_script()
        
        print(f"\n✅ 크로스 폴더 배치 계획 완료!")
        print(f"📊 AUTO: {len(batches['AUTO'])}개, REVIEW: {len(batches['REVIEW'])}개, MANUAL: {len(batches['MANUAL'])}개")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
