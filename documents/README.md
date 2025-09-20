# Freshservice 문서 구조 JSON 활용 가이드

이 문서는 CSV 파일로부터 생성된 Freshservice 문서 구조 JSON 파일들의 사용법을 설명합니다.

## 생성된 파일들

### 1. `document_structure.json` (440KB)
**메인 문서 구조 파일** - 3depth 계층 구조로 구성
```json
{
  "카테고리명": {
    "폴더명": [
      {
        "title": "아티클 제목",
        "position": 위치번호,
        "description": "아티클 설명 (HTML 제거됨)"
      }
    ]
  }
}
```

### 2. `document_stats.json` (16KB)
**통계 정보 파일** - 전체 구조의 요약 정보
```json
{
  "total_categories": 20,
  "total_folders": 193,
  "total_articles": 1557,
  "categories": {
    "카테고리명": {
      "folder_count": 폴더수,
      "article_count": 아티클수,
      "folders": {
        "폴더명": {
          "article_count": 아티클수
        }
      }
    }
  }
}
```

## 구조 개요

총 **20개 카테고리**, **193개 폴더**, **1,557개 아티클**로 구성

### 주요 카테고리별 아티클 수
1. **Freshservice FAQs** - 508개 아티클 (28개 폴더)
2. **Support Guide: IT Service Management** - 187개 아티클 (25개 폴더)
3. **Getting started with Freshservice** - 115개 아티클 (14개 폴더)
4. **Platform** - 101개 아티클 (8개 폴더)
5. **Orchestration + SaaS Management Apps** - 98개 아티클 (48개 폴더)

## 사용 방법

### 1. Python에서 활용
```python
import json

# JSON 구조 로드
with open('documents/document_structure.json', 'r', encoding='utf-8') as f:
    structure = json.load(f)

# 특정 카테고리의 폴더 목록
category = "Freshservice FAQs"
folders = structure[category].keys()
print(f"{category}의 폴더들: {list(folders)}")

# 특정 폴더의 아티클들
folder = "Service Desk FAQ"
articles = structure[category][folder]
for article in articles:
    print(f"- {article['title']} (위치: {article['position']})")
```

### 2. 제공된 도구 스크립트 사용
```bash
# 전체 구조 보기 및 검색 기능
python scripts/use_document_structure.py
```

### 3. 문서 작업 활용 사례

#### A. 카테고리별 문서 목차 생성
```python
def generate_toc(category_name):
    folders = structure[category_name]
    for folder_name, articles in folders.items():
        print(f"## {folder_name}")
        for article in sorted(articles, key=lambda x: x['position']):
            print(f"- {article['title']}")
```

#### B. 키워드 기반 아티클 검색
```python
def search_articles(keyword):
    results = []
    for category, folders in structure.items():
        for folder, articles in folders.items():
            for article in articles:
                if keyword.lower() in article['title'].lower():
                    results.append({
                        'path': f"{category} > {folder}",
                        'article': article
                    })
    return results
```

#### C. 위치 순서 정렬된 아티클 목록
```python
def get_sorted_articles(category_name, folder_name):
    articles = structure[category_name][folder_name]
    return sorted(articles, key=lambda x: x['position'])
```

## 데이터 품질 정보

- **HTML 정리**: 모든 설명에서 HTML 태그가 제거되고 텍스트만 유지
- **설명 길이 제한**: 150자로 제한하여 가독성 향상
- **위치 정렬**: 각 폴더 내 아티클들이 position 필드로 정렬됨
- **인코딩**: UTF-8로 한글 완전 지원

## 재생성 방법

CSV 파일이 업데이트되면 다음 명령으로 JSON을 재생성할 수 있습니다:

```bash
python scripts/create_document_structure.py
```

- **입력**: `documents/merged_articles_links_replaced_freshservice_part*.csv`
- **출력**: `documents/document_structure.json`, `documents/document_stats.json`

## 문서 작업 팁

1. **카테고리 탐색**: 먼저 `document_stats.json`으로 전체 구조 파악
2. **검색 활용**: 키워드 검색으로 관련 아티클들 빠르게 찾기
3. **위치 정보 활용**: `position` 필드로 아티클 순서 결정
4. **설명 활용**: `description` 필드로 아티클 내용 미리보기

이제 체계적으로 정리된 JSON 구조를 활용해서 효율적인 문서 작업을 시작할 수 있습니다! 🚀