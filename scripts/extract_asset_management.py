import pandas as pd
import json

def extract_asset_management_faqs():
    """Asset Management 관련 FAQ들을 추출합니다."""
    
    # CSV 파일 경로들
    csv_files = [
        'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
        'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
    ]
    
    asset_management_faqs = []
    
    for csv_file in csv_files:
        try:
            print(f"Processing {csv_file}...")
            df = pd.read_csv(csv_file)
            
            for index, row in df.iterrows():
                folder_name = str(row['folder_name']) if pd.notna(row['folder_name']) else ''
                
                # folder_name이 'Asset Management'인 FAQ들만 추출
                if folder_name == 'Asset Management':
                    faq_data = {
                        'title': row['title'],
                        'description': row['description'],
                        'path': row['path'],
                        'content_length': len(str(row['description'])) if pd.notna(row['description']) else 0,
                        'csv_file': csv_file,
                        'row_index': index
                    }
                    asset_management_faqs.append(faq_data)
                    print(f"Found: {row['title']}")
        
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
    
    # JSON 파일로 저장
    output_file = 'asset_management_faqs.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(asset_management_faqs, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== 추출 완료 ===")
    print(f"총 {len(asset_management_faqs)}개의 Asset Management FAQ를 추출했습니다.")
    print(f"결과 파일: {output_file}")
    
    return asset_management_faqs

if __name__ == "__main__":
    faqs = extract_asset_management_faqs()
