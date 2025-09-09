#!/usr/bin/env python3
import os
from pathlib import Path
import re

def count_text_in_file(file_path):
    """파일의 텍스트 글자 수 계산 (제목과 본문 분리)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # YAML front matter 제거
        content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
        
        # 마크다운 헤더 제거
        content = re.sub(r'^# .*\n', '', content, flags=re.MULTILINE)
        
        # HTML 태그 제거 (details, summary)
        content = re.sub(r'</?details>', '', content)
        
        # summary 태그에서 제목 추출
        summary_titles = re.findall(r'<summary>(.*?)</summary>', content, re.DOTALL)
        
        # summary 태그 제거
        content = re.sub(r'<summary>.*?</summary>', '', content, re.DOTALL)
        
        # 남은 내용 (FAQ 본문들)
        body_content = re.sub(r'</details>', '', content)
        body_content = body_content.strip()
        
        # 제목들 합치기
        titles_text = '\n'.join(summary_titles)
        
        return {
            'titles': titles_text,
            'titles_chars': len(titles_text),
            'body': body_content,
            'body_chars': len(body_content),
            'total_chars': len(titles_text) + len(body_content)
        }
    except Exception as e:
        print(f"오류 처리 중 {file_path}: {e}")
        return {'titles': '', 'titles_chars': 0, 'body': '', 'body_chars': 0, 'total_chars': 0}

def main():
    faq_base_path = Path("docs/freshworks/freshservice/faqs")
    
    total_titles_chars = 0
    total_body_chars = 0
    total_files = 0
    
    print("FAQ 파일별 글자 수 분석:")
    print("=" * 80)
    
    for category_folder in sorted(faq_base_path.iterdir()):
        if not category_folder.is_dir():
            continue
            
        index_file = category_folder / "index.md"
        if not index_file.exists():
            continue
        
        result = count_text_in_file(index_file)
        total_files += 1
        total_titles_chars += result['titles_chars']
        total_body_chars += result['body_chars']
        
        print(f"{category_folder.name:30} | 제목: {result['titles_chars']:,}자 | 본문: {result['body_chars']:,}자 | 총: {result['total_chars']:,}자")
    
    print("=" * 80)
    print(f"총 {total_files}개 파일")
    print(f"제목 총 글자 수: {total_titles_chars:,}자")
    print(f"본문 총 글자 수: {total_body_chars:,}자")
    print(f"전체 총 글자 수: {total_titles_chars + total_body_chars:,}자")
    print()
    
    if total_titles_chars + total_body_chars > 500000:
        print("🚨 50만자 초과! 번역 API 비용이 많이 들 수 있습니다.")
    else:
        print("✅ 50만자 이하입니다.")
    
    # 번역 비용 추정 (Google Translate API 기준)
    total_chars = total_titles_chars + total_body_chars
    cost_per_million = 20  # USD
    estimated_cost = (total_chars / 1000000) * cost_per_million
    print(f"📊 Google Translate API 예상 비용: ${estimated_cost:.2f} USD")

if __name__ == "__main__":
    main()
