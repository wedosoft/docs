# Freshservice FAQ 자동화 프로젝트 인수인계 문서

## 프로젝트 개요

**목적**: Freshservice 영문 FAQ를 한국어로 번역하여 Docusaurus 기반 문서 사이트에 통합
**현재 상태**: Automations & Triggers FAQ 품질 개선 및 검증 단계
**작업 기간**: 2024년 12월 - 진행 중

## 디렉토리 구조 및 파일 위치

### 핵심 디렉토리 구조
```
/Users/alan/GitHub/docs/
├── docs/
│   └── freshworks/
│       └── freshservice/
│           └── faqs/
│               ├── automations-triggers/          # 현재 작업 완료
│               │   └── index.md
│               ├── api-webhooks/                  # 다음 작업 대상
│               │   └── index.md
│               └── [기타 카테고리들...]
├── raw_data/                                      # 원본 영문 데이터
│   ├── merged_articles_links_replaced_freshservice_part1.csv
│   ├── merged_articles_links_replaced_freshservice_part2.csv
│   ├── merged_articles_links_replaced_freshservice_part3.csv
│   ├── merged_articles_links_replaced_freshservice_part4.csv
│   └── merged_articles_links_replaced_freshservice_part5.csv
├── scripts/                                       # 자동화 스크립트들
│   ├── enhanced_faq_converter.py
│   ├── faq_korean_translator.py
│   └── [기타 스크립트들...]
├── sidebars.ts                                    # 네비게이션 구조
└── .github/instructions/unified-doc-template.md   # 문서 템플릿 가이드
```

### 필수 준수 구조
- **5단계 디렉토리 구조**: `docs/{vendor}/{product}/{category}/{folder}/{article}`
- **실제 경로**: `docs/freshworks/freshservice/faqs/automations-triggers/index.md`

## 작업 프로세스

### 1. 원본 데이터 분석
```bash
# 특정 카테고리 FAQ 검색
grep -i "automation\|trigger\|workflow" /Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv

# 특정 질문 내용 검색
grep -A 10 -B 10 "workflow.*supervisor" /Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv
```

### 2. 품질 검증 프로세스
1. **원본 영문 내용 확인**: CSV 파일에서 정확한 영문 FAQ 내용 추출
2. **번역 완전성 검증**: 모든 FAQ가 완전히 번역되었는지 확인
3. **포맷팅 검증**: HTML 이미지 태그, 링크, 구조 보존 확인
4. **내용 일치성 검증**: 원본과 번역본의 내용이 일치하는지 비교

### 3. 현재 작업 패턴 (검증된 방법)

#### 3.1 원본 내용 확인
```bash
# 해당 카테고리의 모든 FAQ 검색
grep -n "automation\|workflow\|trigger" raw_data/merged_articles_links_replaced_freshservice_part*.csv | head -20

# 특정 질문의 완전한 원본 내용 추출
grep -A 20 -B 5 "특정질문내용" raw_data/merged_articles_links_replaced_freshservice_part*.csv
```

#### 3.2 생성된 내용과 원본 비교
```bash
# 생성된 FAQ 파일 확인
cat docs/freshworks/freshservice/faqs/automations-triggers/index.md | head -100

# 원본과 번역본 동시 비교를 위한 터미널 분할 작업
```

#### 3.3 품질 문제 해결
1. **번역 누락**: 원본 FAQ가 번역본에서 빠진 경우
2. **내용 불일치**: 번역본이 원본과 다른 내용을 포함하는 경우
3. **포맷 손상**: HTML 태그, 이미지, 링크가 깨진 경우

## 핵심 파일들

### 1. 생성된 FAQ 파일
- **위치**: `/Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/automations-triggers/index.md`
- **현재 상태**: 59개 FAQ 포함, 품질 검증 필요
- **문제점**: 일부 번역 불완전, 원본과 내용 불일치

### 2. 원본 데이터 파일
- **위치**: `/Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv`
- **구조**: CSV 형식, 각 행이 하나의 FAQ 아티클
- **중요 컬럼**: 제목, 본문 내용, 카테고리, URL 등

### 3. 네비게이션 설정
- **파일**: `/Users/alan/GitHub/docs/sidebars.ts`
- **현재 설정**: `faqs/automations-triggers` 경로로 수정 완료
- **주의사항**: 새 FAQ 카테고리 추가시 sidebar 업데이트 필요

## 발견된 주요 문제점

### 1. 번역 품질 문제
```
사용자 피드백: "모든 문서의 번역이 안됨 절반만 된 거도 있음"
```
- **원인**: AI 번역 과정에서 일부 내용 누락
- **해결 방법**: 원본 CSV와 생성된 번역본 1:1 비교 검증

### 2. 포맷팅 문제
```
사용자 피드백: "원본 서식이 유지 안되는 경우도 있음"
```
- **원인**: HTML 태그, 이미지 링크 변환 과정에서 손상
- **해결 방법**: 원본 HTML 구조 보존하여 재생성

### 3. 내용 확장 문제
- **문제**: 원본보다 과도하게 상세한 설명 추가
- **예시**: Workflow automator vs Supervisor automation 차이점 설명
- **해결**: 원본 내용에 충실한 번역으로 수정

## 다음 단계 작업 계획

### 1. 현재 파일 수정
1. automations-triggers FAQ 원본 대조 후 완전한 번역으로 교체
2. 누락된 FAQ 항목 추가
3. 포맷팅 문제 수정

### 2. API Webhooks FAQ 작업
- **대상 파일**: `docs/freshworks/freshservice/faqs/api-webhooks/index.md`
- **원본 데이터**: CSV 파일에서 API, webhook 관련 FAQ 추출
- **적용 방법**: 검증된 번역 프로세스 적용

### 3. 기타 카테고리 FAQ
- 현재 faqs 폴더 내 다른 하위 디렉토리들 확인
- 우선순위에 따른 순차적 작업

## 중요 명령어 및 도구

### 원본 데이터 검색
```bash
# 특정 키워드로 FAQ 검색
grep -i "키워드" /Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv

# 컨텍스트와 함께 검색 (앞뒤 10줄)
grep -A 10 -B 10 "검색어" /Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv

# 라인 번호와 함께 검색
grep -n "검색어" /Users/alan/GitHub/docs/raw_data/merged_articles_links_replaced_freshservice_part*.csv
```

### 파일 구조 확인
```bash
# FAQ 디렉토리 구조 확인
ls -la /Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/

# 생성된 파일 내용 미리보기
head -50 /Users/alan/GitHub/docs/docs/freshworks/freshservice/faqs/automations-triggers/index.md
```

## 품질 보증 체크리스트

### 번역 완전성
- [ ] 모든 원본 FAQ가 번역본에 포함되어 있는가?
- [ ] 각 FAQ의 제목과 내용이 완전히 번역되었는가?
- [ ] 원본의 구조와 순서가 보존되었는가?

### 포맷팅 무결성
- [ ] HTML 이미지 태그가 올바르게 보존되었는가?
- [ ] 링크가 정상적으로 작동하는가?
- [ ] Docusaurus 문법 (details, summary 등)이 올바른가?

### 내용 정확성
- [ ] 번역본이 원본의 의미를 정확히 전달하는가?
- [ ] 기술적 용어가 일관되게 번역되었는가?
- [ ] 불필요한 내용 추가나 삭제가 없는가?

## 이슈 해결 가이드

### 문제: "번역이 절반만 되어 있음"
1. 원본 CSV에서 해당 FAQ 완전한 내용 확인
2. 생성된 번역본과 1:1 대조
3. 누락된 부분을 원본 기준으로 재번역

### 문제: "원본 서식이 유지되지 않음"
1. 원본 HTML 태그 구조 확인
2. 이미지 링크 및 포맷팅 태그 보존
3. Docusaurus 호환 형태로 변환

### 문제: "내용이 원본과 다름"
1. 원본 영문 내용 정확히 파악
2. 의역이나 확장 해석 최소화
3. 기술적 정확성 우선으로 번역

## 연락처 및 참고사항

- **프로젝트 담당**: 현재 작업자
- **다음 담당자**: [인수인계 받을 담당자 정보]
- **긴급 이슈**: GitHub Issues 또는 팀 채널 활용

---

## 마지막 업데이트
- **날짜**: 2024년 12월 11일
- **작업자**: [현재 작업자]
- **다음 작업**: Automations-Triggers FAQ 품질 개선 완료 후 API-Webhooks FAQ 작업 시작
