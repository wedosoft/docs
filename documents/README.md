# Freshservice 문서 구조 JSON 활용 가이드

이 문서는 CSV 파일로부터 생성된 Freshservice 문서 구조 JSON 파일들의 사용법을 설명합니다.

## 생성된 파일들

### 1. 카테고리별 JSON 파일 (20개)
**개별 카테고리 구조 파일들** - `documents/categories/` 폴더에 위치
```json
{
  "카테고리명": {
    "폴더명": [
      {
        "title": "아티클 제목",
        "position": 위치번호,
        "description": "HTML 포함 아티클 설명"
      }
    ]
  }
}
```

### 2. `categories/index.json`
**카테고리 인덱스 파일** - 모든 카테고리 JSON 파일의 목록
```json
{
  "total_categories": 20,
  "categories": [
    {
      "category": "카테고리명",
      "slug": "파일명용-slug",
      "filename": "파일명.json",
      "folder_count": 폴더수,
      "article_count": 아티클수
    }
  ]
}
```

### 3. `document_stats.json`
**통계 정보 파일** - 전체 구조의 요약 정보 (기존과 동일)

## 구조 개요

총 **20개 카테고리**, **193개 폴더**, **1,557개 아티클**로 구성

### 생성된 카테고리 JSON 파일들
1. **freshservice-faqs.json** - 508개 아티클 (28개 폴더)
2. **support-guide-it-service-management.json** - 187개 아티클 (25개 폴더)
3. **getting-started-with-freshservice.json** - 115개 아티클 (14개 폴더)
4. **platform.json** - 101개 아티클 (8개 폴더)
5. **orchestration-saas-management-apps.json** - 98개 아티클 (48개 폴더)
... 총 20개 파일

## 사용 방법

### 1. Python에서 활용
```python
import json

# 특정 카테고리 로드 (전체 계층구조)
with open('documents/categories/freshservice-faqs.json', 'r', encoding='utf-8') as f:
    faqs_data = json.load(f)

# category.folder.article 접근
category_name = list(faqs_data.keys())[0]  # "Freshservice FAQs"
folders = faqs_data[category_name]

# 특정 폴더의 아티클들
folder = "Service Desk FAQ"
articles = folders[folder]
for article in articles:
    print(f"- {article['title']} (위치: {article['position']})")
    print(f"  HTML 설명: {article['description'][:100]}...")
```

### 2. 인덱스 파일 활용
```python
# 모든 카테고리 목록 조회
with open('documents/categories/index.json', 'r', encoding='utf-8') as f:
    index = json.load(f)

print(f"총 {index['total_categories']}개 카테고리:")
for category in index['categories']:
    print(f"- {category['filename']}: {category['category']}")
    print(f"  ({category['folder_count']}개 폴더, {category['article_count']}개 아티클)")
```

### 3. 제공된 도구 스크립트 사용
```bash
# 전체 구조 보기 및 검색 기능 (업데이트 필요)
python scripts/use_document_structure.py
```

### 4. 문서 작업 활용 사례

#### A. 특정 카테고리 작업
```python
import json

def load_category(category_slug):
    """카테고리 JSON 파일 로드 (전체 계층구조)"""
    with open(f'documents/categories/{category_slug}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 예시: FAQ 카테고리 작업
faqs_full = load_category('freshservice-faqs')
category_name = list(faqs_full.keys())[0]  # "Freshservice FAQs"
folders = faqs_full[category_name]

for folder_name, articles in folders.items():
    print(f"## {folder_name}")
    for article in sorted(articles, key=lambda x: x['position']):
        print(f"- {article['title']}")
```

#### B. 모든 카테고리 검색
```python
import os
import json

def search_all_categories(keyword):
    """모든 카테고리에서 키워드 검색"""
    results = []
    
    for filename in os.listdir('documents/categories/'):
        if filename.endswith('.json') and filename != 'index.json':
            with open(f'documents/categories/{filename}', 'r', encoding='utf-8') as f:
                category_data = json.load(f)
            
            # category.folder.article 구조 처리
            category_name = list(category_data.keys())[0]
            folders = category_data[category_name]
            
            for folder_name, articles in folders.items():
                for article in articles:
                    if keyword.lower() in article['title'].lower():
                        results.append({
                            'file': filename,
                            'category': category_name,
                            'folder': folder_name,
                            'article': article
                        })
    
    return results
```

#### C. HTML 설명 활용
```python
def get_article_html(category_slug, folder_name, article_title):
    """특정 아티클의 HTML 설명 가져오기"""
    with open(f'documents/categories/{category_slug}.json', 'r', encoding='utf-8') as f:
        category_data = json.load(f)
    
    # category.folder.article 구조 처리
    category_name = list(category_data.keys())[0]
    folders = category_data[category_name]
    
    for article in folders[folder_name]:
        if article['title'] == article_title:
            return article['description']  # 완전한 HTML 포함
    
    return None
```

## 데이터 품질 정보

- **HTML 보존**: 모든 설명에서 원본 HTML 태그와 스타일 완전 유지
- **개별 파일**: 카테고리별 작업 시 필요한 데이터만 로드 가능
- **위치 정렬**: 각 폴더 내 아티클들이 position 필드로 정렬됨
- **인코딩**: UTF-8로 한글 완전 지원

## 재생성 방법

CSV 파일이 업데이트되면 다음 명령으로 JSON을 재생성할 수 있습니다:

```bash
python scripts/create_document_structure.py
```

- **입력**: `documents/merged_articles_links_replaced_freshservice_part*.csv`
- **출력**: `documents/categories/` 폴더에 20개 JSON 파일 + 인덱스 파일

## 문서 작업 팁

1. **카테고리별 작업**: 필요한 카테고리 JSON 파일만 로드해서 효율적 작업
2. **인덱스 활용**: `index.json`으로 전체 구조 파악 후 필요한 파일 선택
3. **HTML 활용**: `description` 필드의 완전한 HTML로 rich content 처리
4. **위치 정보 활용**: `position` 필드로 아티클 순서 유지

이제 카테고리별로 분리된 JSON 구조를 활용해서 효율적인 문서 작업을 시작할 수 있습니다! 🚀