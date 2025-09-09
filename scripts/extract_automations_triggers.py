import pandas as pd
import json

def extract_automations_triggers_faqs():
    """자동화 및 트리거 관련 FAQ들을 추출합니다."""
    
    # CSV 파일 경로들
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    # 자동화 및 트리거 관련 키워드들
    automation_keywords = [
        'automation', 'automator', 'trigger', 'workflow', 'rule', 'condition',
        'event', 'escalation', 'dispatch', 'routing', 'notification',
        'scheduler', 'cron', 'time', 'recurring', 'repeat', 'schedule',
        'business rule', 'workflow rule', 'auto assign', 'auto close',
        'auto reply', 'auto update', 'observer', 'watcher', 'approval',
        'sla', 'escalation matrix', 'time trigger', 'field update'
    ]
    
    automations_faqs = []
    
    for csv_file in csv_files:
        try:
            print(f"Processing {csv_file}...")
            df = pd.read_csv(csv_file)
            
            for index, row in df.iterrows():
                title = str(row['title']).lower() if pd.notna(row['title']) else ''
                description = str(row['description']).lower() if pd.notna(row['description']) else ''
                path = str(row['path']).lower() if pd.notna(row['path']) else ''
                
                # 키워드 매칭 검사
                content_to_check = f"{title} {description} {path}"
                
                # 자동화/트리거 관련 키워드 확인
                if any(keyword in content_to_check for keyword in automation_keywords):
                    # 폴더 경로도 확인 (automations, triggers, workflow 등)
                    if any(folder_keyword in path for folder_keyword in 
                           ['automation', 'trigger', 'workflow', 'escalation', 'dispatch', 'routing']):
                        
                        faq_data = {
                            'title': row['title'],
                            'description': row['description'],
                            'path': row['path'],
                            'content_length': len(str(row['description'])) if pd.notna(row['description']) else 0,
                            'csv_file': csv_file,
                            'row_index': index
                        }
                        
                        automations_faqs.append(faq_data)
                        print(f"Found automation/trigger FAQ: {row['title'][:80]}...")
                        
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
            continue
    
    # 결과를 JSON 파일로 저장
    output_file = 'automations_triggers_faqs.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(automations_faqs, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 자동화 및 트리거 FAQ 추출 완료 ===")
    print(f"총 {len(automations_faqs)}개의 FAQ 발견")
    print(f"결과가 {output_file}에 저장되었습니다.")
    
    # 컨텐츠 길이별 분포 출력
    if automations_faqs:
        lengths = [faq['content_length'] for faq in automations_faqs]
        print(f"컨텐츠 길이 - 최소: {min(lengths)}, 최대: {max(lengths)}, 평균: {sum(lengths)//len(lengths)}")
        
        # 상위 10개 출력
        print("\n상위 10개 FAQ:")
        for i, faq in enumerate(automations_faqs[:10]):
            print(f"{i+1}. {faq['title'][:100]}")
    
    return automations_faqs

if __name__ == "__main__":
    extract_automations_triggers_faqs()
