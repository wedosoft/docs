# 📁 Categories 폴더

> **Categories 폴더는 이 프로젝트의 핵심 데이터 저장소**입니다. Freshservice 문서화 프로젝트에서 카테고리별로 분할된 CSV 데이터를 관리합니다.

## 🎯 폴더 목적

이 폴더는 Freshservice 기술문서를 체계적으로 변환하기 위해 **원본 CSV 데이터를 카테고리별로 분할하여 저장**하는 핵심 저장소입니다.

### 주요 기능
- **카테고리 기반 작업 관리**: 각 CSV 파일은 독립적인 작업 단위
- **순차적 변환 지원**: 카테고리별로 완전 완료 후 다음 단계 진행
- **데이터 무결성 보장**: 원본 1,557개 문서를 20개 카테고리로 체계적 분할

## 📊 파일 구조 및 현황

### 📁 포함된 CSV 파일 (20개)

| 파일명 | 카테고리 | 폴더 수 | 문서 수(예상) | 우선순위 |
|--------|----------|---------|---------------|----------|
| `Contact_Support.csv` | Contact Support | 1개 | ~5개 | 🟡 중간 |
| `End_User_Guide.csv` | End User Guide | 1개 | ~10개 | 🟡 중간 |
| `Enterprise_Service_Management.csv` | Enterprise Service Management | 7개 | ~150개 | 🔴 높음 |
| `Freshservice_FAQs.csv` | **Freshservice FAQs** | 28개 | **~508개** | 🔴 **최우선** |
| `Freshservice_L2.csv` | Freshservice L2 | 1개 | ~5개 | 🟢 낮음 |
| `Freshservice_Mobile.csv` | Freshservice Mobile | 3개 | ~20개 | 🟡 중간 |
| `Getting_started_with_Freshservice.csv` | **Getting started** | 14개 | **~115개** | 🔴 **높음** |
| `How_to_Setup_Apps_and_Integrations.csv` | Apps and Integrations | 3개 | ~50개 | 🟡 중간 |
| `IT_Operations_Management.csv` | IT Operations Management | 8개 | ~80개 | 🟡 중간 |
| `Managed_Service_Provider.csv` | Managed Service Provider | 1개 | ~10개 | 🟢 낮음 |
| `Orchestration_and_SaaS_Management_Apps.csv` | Orchestration + SaaS | 48개 | ~200개 | 🔴 높음 |
| `Platform.csv` | **Platform** | 8개 | **~101개** | 🔴 **높음** |
| `Policies_and_Data_Protection.csv` | Policies and Data Protection | 5개 | ~40개 | 🟡 중간 |
| `Project_&_Workload_Management.csv` | Project & Workload Management | 2개 | ~20개 | 🟡 중간 |
| `Quick_Start_Guides.csv` | Quick Start Guides | 1개 | ~5개 | 🟢 낮음 |
| `Security_and_Policies.csv` | Security and Policies | 7개 | ~60개 | 🟡 중간 |
| `Support_Guide_IT_Asset_Management.csv` | IT Asset Management | 11개 | ~90개 | 🟡 중간 |
| `Support_Guide_IT_Service_Management.csv` | **IT Service Management** | 25개 | **~187개** | 🔴 **최우선** |
| `User_Guide_-_Admin.csv` | User Guide - Admin | 10개 | ~80개 | 🟡 중간 |
| `User_Guide_-_Agent.csv` | User Guide - Agent | 9개 | ~70개 | 🟡 중간 |

### 📈 전체 현황
- **총 카테고리**: 20개
- **총 폴더**: 180개
- **총 문서**: 1,557개
- **평균 문서/카테고리**: ~78개

## 🔄 활용 방법

### 1️⃣ 카테고리별 작업 선택
```bash
# 특정 카테고리 문서 수 확인
wc -l categories/Freshservice_FAQs.csv

# 카테고리 내용 미리보기
head -10 categories/Freshservice_FAQs.csv

# 모든 카테고리 문서 수 확인
wc -l categories/*.csv
```

### 2️⃣ 작업 우선순위 기준
```
🔴 최우선: Freshservice_FAQs (508개), Support_Guide_IT_Service_Management (187개)
🔴 높음: Getting_started_with_Freshservice (115개), Platform (101개)
🟡 중간: 나머지 중간 규모 카테고리들
🟢 낮음: 소규모 카테고리 (Quick_Start_Guides, Freshservice_L2 등)
```

### 3️⃣ 데이터 구조 이해
```bash
# CSV 헤더 확인 (모든 파일 동일 구조)
head -1 categories/Freshservice_FAQs.csv

# 특정 카테고리의 폴더 구조 분석
grep "Automations and Triggers" categories/Freshservice_FAQs.csv
```

## 🛠️ 작업 관련 스크립트

### 카테고리 분석 도구
```bash
# 전체 카테고리 구조 출력
python3 scripts/extract_complete_categories.py

# 특정 카테고리 상세 분석
python3 scripts/analyze_category.py categories/Freshservice_FAQs.csv
```

### CSV 변환 도구
```bash
# 카테고리별 변환 (개발 중)
python3 scripts/convert_category.py categories/Getting_started_with_Freshservice.csv

# 개별 문서 변환
python3 scripts/csv_to_markdown.py [csv_file] [article_id]
```

## 📋 작업 지침

### ✅ 올바른 활용법
1. **한 카테고리 완전 완료** 후 다음 카테고리 진행
2. **우선순위 순서** 준수 (FAQs → IT Service Management → Getting Started → Platform)
3. **원본 데이터 보존** - CSV 파일 수정 금지
4. **진행 상황 추적** - documents/project-status-v3.md 업데이트

### ❌ 주의사항
1. **여러 카테고리 혼재 작업 금지** - 품질 관리 어려움
2. **CSV 파일 직접 수정 금지** - 데이터 무결성 보장
3. **부분 완료 상태 방치 금지** - 완료 또는 원복 결정
4. **임의 우선순위 변경 금지** - 마스터플랜 준수

## 🎯 완료 기준

### 카테고리 완료 조건
```
✅ 모든 문서 Markdown 변환 완료
✅ 한국어 리라이팅 완료  
✅ v3.0 템플릿 적용 완료
✅ MDX 호환성 확인 완료
✅ 빌드 테스트 통과
✅ sidebars.ts 업데이트 완료
```

### 품질 검증
```bash
# 빌드 테스트
npm run build

# MDX 호환성 검사
python3 scripts/mdx_fixer.py docs/freshworks/freshservice/[category]/

# 문서 수 검증
find docs/freshworks/freshservice/[category] -name "*.md" | wc -l
```

## 📚 관련 문서

- **프로젝트 현황**: [documents/project-status-v3.md](../documents/project-status-v3.md)
- **작업 지침**: [documents/work-guidelines.md](../documents/work-guidelines.md)
- **CSV 변환 가이드**: [documents/csv-conversion-guide.md](../documents/csv-conversion-guide.md)
- **카테고리 구조**: [.github/instructions/freshservice-category-structure.md](../.github/instructions/freshservice-category-structure.md)

---

> **💡 핵심**: Categories 폴더는 수작업 기반 고품질 문서 변환의 출발점입니다. 체계적인 카테고리별 접근을 통해 1,557개 문서를 안정적으로 변환할 수 있습니다.