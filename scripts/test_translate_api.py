#!/usr/bin/env python3
import requests
import json
import os
import re
from pathlib import Path
import time

# Google Translate API 설정
API_KEY = "AIzaSyAktNTMV9YoM-NnGt-xjjHpyR-38uTOzIw"
TRANSLATE_URL = "https://translation.googleapis.com/v3/projects/faq-translator-439903/locations/us-central1:translateText"

def clean_text(text):
    """텍스트 정리"""
    if not text:
        return ''
    text = str(text).strip()
    # HTML 태그 제거
    text = re.sub(r'<[^>]+>', '', text)
    # 특수 문자 정리
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    return text

def translate_text(text, target_lang='ko', source_lang='en'):
    """Google Cloud Translation API로 텍스트 번역"""
    if not text or len(text.strip()) == 0:
        return text
    
    headers = {
        'Authorization': f'Bearer $(gcloud auth print-access-token)',
        'Content-Type': 'application/json',
        'x-goog-user-project': 'faq-translator-439903'
    }
    
    # 간단한 방법: API 키로 직접 요청
    url_with_key = f"https://translation.googleapis.com/language/translate/v2?key={API_KEY}"
    
    data = {
        'q': text,
        'target': target_lang,
        'source': source_lang,
        'format': 'text'
    }
    
    try:
        response = requests.post(url_with_key, json=data)
        if response.status_code == 200:
            result = response.json()
            return result['data']['translations'][0]['translatedText']
        else:
            print(f"번역 오류 {response.status_code}: {response.text}")
            return text
    except Exception as e:
        print(f"번역 요청 오류: {e}")
        return text

def translate_faq_file(file_path, max_chars=1000):
    """FAQ 파일의 일부만 번역 테스트"""
    print(f"\n📄 {file_path} 번역 테스트 중...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # YAML front matter와 제목 건너뛰기
        lines = content.split('\n')
        start_idx = 0
        
        # YAML front matter 건너뛰기
        if lines[0].startswith('---'):
            for i, line in enumerate(lines[1:], 1):
                if line.startswith('---'):
                    start_idx = i + 1
                    break
        
        # 헤더 건너뛰기
        for i, line in enumerate(lines[start_idx:], start_idx):
            if line.startswith('#'):
                continue
            if line.strip() == '':
                continue
            start_idx = i
            break
        
        # 번역할 텍스트 찾기
        remaining_lines = lines[start_idx:]
        text_to_translate = ""
        char_count = 0
        
        for line in remaining_lines:
            if char_count + len(line) > max_chars:
                break
            text_to_translate += line + '\n'
            char_count += len(line)
        
        if text_to_translate.strip():
            print(f"  원본 ({len(text_to_translate)}자): {text_to_translate[:100]}...")
            translated = translate_text(text_to_translate)
            print(f"  번역 ({len(translated)}자): {translated[:100]}...")
            return len(text_to_translate), len(translated)
        else:
            print("  번역할 텍스트가 없습니다.")
            return 0, 0
            
    except Exception as e:
        print(f"  파일 처리 오류: {e}")
        return 0, 0

def main():
    """메인 함수 - 몇 개 파일만 테스트"""
    print("🔬 Google Translate API 테스트 시작")
    print(f"API 키: {API_KEY[:20]}...")
    
    # 테스트할 파일들 (작은 파일부터)
    test_files = [
        "docs/freshworks/freshservice/faqs/pricing/index.md",
        "docs/freshworks/freshservice/faqs/priority-matrix/index.md", 
        "docs/freshworks/freshservice/faqs/feedback-widget/index.md"
    ]
    
    total_source_chars = 0
    total_translated_chars = 0
    
    for file_path in test_files:
        if os.path.exists(file_path):
            source_chars, translated_chars = translate_faq_file(file_path, max_chars=500)
            total_source_chars += source_chars
            total_translated_chars += translated_chars
            time.sleep(1)  # API 제한 방지
        else:
            print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
    
    print(f"\n📊 테스트 결과:")
    print(f"원본 총 글자 수: {total_source_chars:,}")
    print(f"번역 총 글자 수: {total_translated_chars:,}")
    
    if total_source_chars > 0:
        cost_estimate = (total_source_chars + total_translated_chars) / 1000000 * 10  # $10/M chars
        print(f"예상 비용: ${cost_estimate:.4f} USD")

if __name__ == "__main__":
    main()
