# 📄 CSV 변환 가이드

> **목적**: CSV 데이터를 Markdown 문서로 자동 변환하는 2단계 작업 가이드

## 🎯 2단계 작업 개요

### 현재 상황
- **1단계 완료**: 74개 문서 v3.0 템플릿 표준화 ✅
- **데이터 준비**: 5개 CSV 파일 (1,557개 문서) 대기 중
- **목표**: 완전 자동화된 대량 변환 시스템 구축

### CSV 파일 현황
```
/raw_data/
├── merged_articles_links_replaced_freshservice_part1.csv
├── merged_articles_links_replaced_freshservice_part2.csv  
├── merged_articles_links_replaced_freshservice_part3.csv
├── merged_articles_links_replaced_freshservice_part4.csv
└── merged_articles_links_replaced_freshservice_part5.csv
```

---

## 📊 1단계: CSV 데이터 분석

### 데이터 구조 파악
```python
# CSV 분석 스크립트
import pandas as pd

# 모든 CSV 파일 로드
csv_files = [
    './raw_data/merged_articles_links_replaced_freshservice_part1.csv',
    './raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
    './raw_data/merged_articles_links_replaced_freshservice_part3.csv',
    './raw_data/merged_articles_links_replaced_freshservice_part4.csv',
    './raw_data/merged_articles_links_replaced_freshservice_part5.csv'
]

# 데이터 통합 및 분석
all_data = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)
print(f"총 문서 수: {len(combined_df)}")
print(f"컬럼 정보: {combined_df.columns.tolist()}")
```

### 필수 확인 항목
- [ ] **컬럼 스키마**: title, description, category, folder 등 필드 확인
- [ ] **데이터 품질**: 누락된 값, 중복 데이터 점검
- [ ] **HTML 구조**: description 필드의 HTML 태그 패턴 분석
- [ ] **이미지 링크**: S3 URL 패턴 및 유효성 확인
- [ ] **카테고리 구조**: 폴더 계층 구조 파악

---

## 🔧 2단계: 변환 엔진 개발

### 핵심 모듈 구조
```
scripts/
├── csv_converter/
│   ├── __init__.py
│   ├── csv_parser.py          # CSV 데이터 파싱
│   ├── html_to_markdown.py    # HTML → Markdown 변환
│   ├── translator.py          # 한국어 번역 (GPT-4)
│   ├── image_processor.py     # 이미지 링크 처리
│   ├── folder_manager.py      # 폴더 구조 생성
│   ├── sidebar_updater.py     # sidebars.ts 자동 업데이트
│   └── quality_validator.py   # 품질 검증
├── bulk_converter.py          # 대량 변환 실행기
└── validation_suite.py        # 전체 검증 스위트
```

### 변환 파이프라인
```python
# 변환 프로세스 예시
def convert_csv_to_markdown(csv_file):
    # 1. CSV 데이터 로드
    data = load_csv_data(csv_file)
    
    # 2. 카테고리별 분류
    categorized_data = categorize_articles(data)
    
    # 3. HTML → Markdown 변환
    for article in categorized_data:
        markdown_content = html_to_markdown(article['description'])
        
        # 4. 한국어 번역 (실무 중심)
        translated_content = translate_to_korean(markdown_content)
        
        # 5. 이미지 링크 처리
        processed_content = process_images(translated_content)
        
        # 6. 템플릿 적용
        final_content = apply_template(processed_content, article)
        
        # 7. 파일 생성
        create_markdown_file(final_content, article['path'])
    
    # 8. sidebars.ts 업데이트
    update_sidebars(categorized_data)
    
    # 9. 품질 검증
    validate_conversion_quality()
```

---

## 🌐 3단계: 번역 및 리라이팅

### 번역 전략
```python
# GPT-4 기반 실무 번역 프롬프트
TRANSLATION_PROMPT = """
다음 Freshservice 기술문서를 한국어로 번역하되, 다음 지침을 따르세요:

1. 단순 번역이 아닌 실무 중심 리라이팅
2. 헬프데스크 상담원이 바로 사용할 수 있도록 작성
3. 단계별 가이드 형태로 구성
4. 전문 용어는 한글(영문) 병기
5. 예시 중심 설명, 추상적 설명 지양

원문:
{html_content}

번역 결과:
"""
```

### 품질 기준
- **실무 적용성**: 상담원이 즉시 업무에 활용 가능
- **명확성**: 단계별 절차가 명확하게 제시
- **정확성**: 기술적 내용의 정확한 전달
- **일관성**: 용어 및 스타일의 일관된 사용

---

## 🖼️ 4단계: 이미지 링크 처리

### 이미지 URL 패턴 분석
```python
# 이미지 링크 패턴 예시
KNOWN_PATTERNS = [
    'https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/',
    'https://cdn.freshdesk.com/data/helpdesk/attachments/production/',
    # 기타 패턴들...
]

def process_image_links(content):
    # 1. 이미지 URL 추출
    image_urls = extract_image_urls(content)
    
    # 2. URL 유효성 검사
    valid_urls = validate_image_urls(image_urls)
    
    # 3. Markdown 형식으로 변환
    for url in valid_urls:
        alt_text = generate_alt_text(url)
        content = content.replace(
            f'<img src="{url}"',
            f'![{alt_text}]({url})'
        )
    
    return content
```

### 이미지 처리 규칙
- **원본 URL 유지**: S3 링크 절대 변경 금지
- **Alt 텍스트 생성**: 이미지 내용을 설명하는 한국어 텍스트
- **Markdown 형식**: `![설명](URL)` 형식만 사용
- **유효성 검증**: 접근 불가능한 이미지 링크 탐지

---

## 📁 5단계: 폴더 구조 생성

### 자동 폴더 생성
```python
def create_folder_structure(articles):
    folder_mapping = {
        'Getting started with Freshservice': 'getting-started',
        'User Guide - Agent': 'user-guide-agent',
        'User Guide - Admin': 'user-guide-admin',
        # ... 카테고리별 매핑
    }
    
    for article in articles:
        category = folder_mapping.get(article['category'])
        subfolder = slugify(article['folder'])
        
        folder_path = f"docs/freshworks/freshservice/{category}/{subfolder}/"
        os.makedirs(folder_path, exist_ok=True)
```

### 파일명 생성 규칙
```python
def generate_filename(title):
    # 1. 소문자 변환
    # 2. 특수문자 제거
    # 3. 공백을 하이픈으로 변환
    # 4. 연속 하이픈 정리
    
    filename = title.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[\s_]+', '-', filename)
    filename = re.sub(r'-+', '-', filename)
    filename = filename.strip('-')
    
    return f"{filename}.md"
```

---

## 📋 6단계: 품질 검증 자동화

### 자동 검증 항목
```python
class QualityValidator:
    def validate_markdown_files(self, file_paths):
        results = []
        
        for file_path in file_paths:
            result = {
                'file': file_path,
                'markdown_syntax': self.check_markdown_syntax(file_path),
                'mdx_compatibility': self.check_mdx_compatibility(file_path),
                'image_links': self.validate_image_links(file_path),
                'korean_braces': self.check_korean_braces(file_path),
                'template_compliance': self.check_template_format(file_path)
            }
            results.append(result)
        
        return results
```

### 검증 기준
- [ ] **Markdown 문법**: 올바른 문법 사용
- [ ] **MDX 호환성**: 빌드 오류 없음
- [ ] **이미지 링크**: 모든 이미지 접근 가능
- [ ] **한글 중괄호**: 이스케이프 처리 완료
- [ ] **템플릿 준수**: v3.0 템플릿 형식 준수

---

## 🚀 7단계: 대량 변환 실행

### 실행 스크립트
```bash
# 1. 개발 환경 설정
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. CSV 분석 실행
python scripts/analyze_csv.py

# 3. 소규모 테스트 변환
python scripts/bulk_converter.py --test --limit 10

# 4. 품질 검증
python scripts/validation_suite.py --test-files

# 5. 전체 변환 실행
python scripts/bulk_converter.py --full-conversion

# 6. 최종 검증
npm run build
```

### 모니터링 및 로그
- **진행률 추적**: 실시간 변환 진행률 표시
- **오류 로그**: 변환 실패 파일 및 원인 기록
- **품질 리포트**: 검증 결과 요약 리포트
- **성능 지표**: 변환 속도 및 메모리 사용량

---

## 📊 예상 결과 및 성능

### 변환 성능 목표
- **처리 속도**: 분당 10-15개 문서 변환
- **전체 소요시간**: 1,557개 문서 → 약 2-3일
- **성공률**: 95% 이상 자동 변환 성공
- **품질 점수**: 수동 검토 없이 배포 가능한 수준

### 최종 결과물
```
docs/freshworks/freshservice/
├── getting-started/                 (115개 문서)
├── user-guide-agent/               (62개 문서)
├── support-guide-itsm/             (187개 문서)
├── support-guide-itam/             (95개 문서)
├── freshservice-faqs/              (508개 문서)
├── enterprise-service-mgmt/        (69개 문서)
├── it-operations-mgmt/             (95개 문서)
├── platform/                      (101개 문서)
├── apps-integrations/              (87개 문서)
└── 기타 카테고리들/                 (238개 문서)
```

---

## 🔄 다음 단계

### 즉시 착수 가능
1. **CSV 분석 스크립트** 개발 시작
2. **HTML → Markdown 변환기** 프로토타입 구현
3. **소규모 테스트** (10-20개 문서로 검증)

### 단계별 확장
1. **번역 엔진** 통합 (GPT-4 API)
2. **이미지 처리** 자동화
3. **품질 검증** 시스템 구축
4. **대량 변환** 최적화

---

## 📚 관련 문서

- [프로젝트 현황](./project-status.md) - 현재 진행 상황
- [마스터플랜](./freshservice-masterplan.md) - 전체 프로젝트 계획
- [작업 지침서](./work-guidelines.md) - 품질 기준 및 규칙
- [MDX 문제해결](./mdx-troubleshooting.md) - 기술적 문제 해결

---

> **💡 핵심 전략**: 1단계에서 검증된 고품질 표준을 기반으로 완전 자동화된 변환 시스템을 구축하여 1,557개 문서를 효율적으로 처리합니다.
