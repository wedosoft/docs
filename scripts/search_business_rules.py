#!/usr/bin/env python3
import pandas as pd
import glob

# 모든 CSV 파일 찾기
csv_files = glob.glob('raw_data/*.csv')

for csv_file in csv_files:
    try:
        df = pd.read_csv(csv_file)
        if 'title' in df.columns and 'category' in df.columns and 'folder' in df.columns:
            # Business rules 관련 문서 찾기
            business_rules = df[df['title'].str.contains('Business rules', case=False, na=False)]
            if not business_rules.empty:
                print(f'\n=== {csv_file} ===')
                for idx, row in business_rules.iterrows():
                    print(f'제목: {row["title"]}')
                    print(f'폴더: {row["folder"]}')
                    print(f'카테고리: {row["category"]}')
                    print('---')
    except Exception as e:
        print(f'Error reading {csv_file}: {e}')
