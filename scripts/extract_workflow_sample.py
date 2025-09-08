import csv
import json
from bs4 import BeautifulSoup
import re

# CSV 필드 크기 제한 증가
csv.field_size_limit(1000000)

# 타겟 ID
target_id = '50000003284'

csv_files = [
    'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
    'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
    'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
    'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
    'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
]

for file_path in csv_files:
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == target_id:
                    # HTML을 깨끗한 텍스트로 변환
                    soup = BeautifulSoup(row['description'], 'html.parser')
                    
                    # 이미지 태그를 마크다운 형식으로 변환
                    for img in soup.find_all('img'):
                        src = img.get('src', '')
                        alt = img.get('alt', 'Image')
                        if src:
                            img.replace_with(f'![{alt}]({src})')
                    
                    # 링크 태그를 마크다운 형식으로 변환  
                    for link in soup.find_all('a'):
                        href = link.get('href', '')
                        text = link.get_text()
                        if href and text:
                            link.replace_with(f'[{text}]({href})')
                    
                    # 텍스트 추출
                    clean_text = soup.get_text()
                    
                    # 여러 줄바꿈을 정리
                    clean_text = re.sub(r'\n\s*\n', '\n\n', clean_text)
                    clean_text = clean_text.strip()
                    
                    sample_data = {
                        'id': row['id'],
                        'title': row['title'],
                        'description': clean_text,
                        'folder_name': row.get('folder_name', ''),
                        'category_name': row.get('category_name', ''),
                        'path': row.get('path', ''),
                        'tags': row.get('tags', ''),
                        'file_part': row.get('file_part', '')
                    }
                    
                    # JSON 파일로 저장
                    with open('workflow_sample.json', 'w', encoding='utf-8') as f:
                        json.dump(sample_data, f, ensure_ascii=False, indent=2)
                    
                    print(f'샘플 추출 완료: {row["title"]}')
                    print(f'카테고리: {row["category_name"]}')
                    print(f'설명 길이: {len(clean_text)} 문자')
                    print(f'\n첫 500자 미리보기:')
                    print(clean_text[:500] + '...')
                    exit()
    except Exception as e:
        print(f'오류 {file_path}: {e}')

print('샘플을 찾을 수 없습니다.')
