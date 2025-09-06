# Freshservice 문서화 마스터 플랜

## � 중요: 새로운 AI를 위한 즉시 실행 가이드

### 현재 상황 (2025년 9월 6일)
- **진행 중인 작업**: User Management 폴더의 7번 문서부터 작업 필요
- **다음 즉시 해야 할 일**: "Guidelines to importing requesters from CSV files" 문서 작성
- **작업 위치**: `docs/freshworks/freshservice/getting-started-with-freshservice/user-management/`

### 즉시 실행 커맨드 (복사해서 실행)
```python
# 1. 다음 문서(7번) 내용 확인
cd /Users/alan/GitHub/docs && python3 -c "
import pandas as pd
csv_files = ['./raw_data/merged_articles_links_replaced_freshservice_part1.csv',
             './raw_data/merged_articles_links_replaced_freshservice_part2.csv', 
             './raw_data/merged_articles_links_replaced_freshservice_part3.csv',
             './raw_data/merged_articles_links_replaced_freshservice_part4.csv',
             './raw_data/merged_articles_links_replaced_freshservice_part5.csv']
all_data = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    all_data.append(df)
combined_df = pd.concat(all_data, ignore_index=True)

# 7번 문서 찾기
target_doc = combined_df[combined_df['title'] == 'Guidelines to importing requesters from CSV files'].iloc[0]
print('=== 7번 문서 정보 ===')
print(f'제목: {target_doc[\"title\"]}')
print(f'HTML 내용:')
print(target_doc['description'])
"
```

### 문서 작성 필수 규칙
1. **파일 위치**: `docs/freshworks/freshservice/getting-started-with-freshservice/user-management/csv-import-guidelines.md`
2. **ID 규칙**: `csv-import-guidelines` (간단하게)
3. **템플릿**: `.github/instructions/document-template.md` 기준 준수
4. **sidebars.ts 업데이트**: 새 문서 추가 후 반드시 업데이트
5. **한국어 번역**: 실무 중심으로 번역

---

## 🗂️ 전체 구조 현황

### Freshservice 카테고리별 문서 수 (총 1,557개)
1. **Getting started with Freshservice** - 115개 문서 ⚠️ **현재 작업 중**
2. Support Guide: IT Service Management - 187개 문서
3. Support Guide: IT Asset Management - 95개 문서
4. Enterprise Service Management - 69개 문서
5. IT Operations Management - 95개 문서
6. Platform - 101개 문서
7. How to Setup Apps and Integrations - 87개 문서
8. Security and Policies - 41개 문서
9. Policies and Data Protection - 21개 문서
10. Project & Workload Management - 47개 문서
11. User Guide - Admin/Agent/End User - 62개 문서
12. Freshservice FAQs - 508개 문서 (가장 많음)
13. 기타 카테고리들...

---

## 📍 현재 작업 상태 (2025년 9월 6일 기준)

### ✅ 완료된 작업

#### 1. 기본 설정 완료
- [x] Docusaurus 프로젝트 구조 설정
- [x] CSV 데이터 분석 (5개 파일, 1,557개 문서)
- [x] 문서 템플릿 작성 (`/.github/instructions/document-template.md`)
- [x] Slug 구조 수정 (단순화)
- [x] 올바른 폴더 구조 설정

#### 2. Getting started with Freshservice > User Management 폴더
**위치**: `docs/freshworks/freshservice/getting-started-with-freshservice/user-management/`
**진행률**: 6/19 완료 (31.6%)

| 순번 | 문서 제목 | 파일명 | 상태 |
|------|-----------|--------|------|
| 1 | Understanding Full-time vs. Occasional agents | `understanding-agents.md` | ✅ 완료 |
| 2 | Setting agent roles and permissions | `setting-agent-roles-permissions.md` | ✅ 완료 |
| 3 | Managing requesters in Freshservice | `managing-requesters.md` | ✅ 완료 |
| 4 | Importing requesters from a CSV file | `importing-requesters-csv.md` | ✅ 완료 |
| 5 | How to find the User ID (or Responder ID) of an agent | `finding-agent-user-id.md` | ✅ 완료 |
| 6 | Adding Custom Fields for Users (Requesters & Agents) in Freshservice | `adding-custom-fields-users.md` | ✅ 완료 |
| 7 | Guidelines to importing requesters from CSV files | `csv-import-guidelines.md` | 🔄 다음 작업 |
| 8 | Merging Requesters in Freshservice | `merging-requesters.md` | ⏳ 대기 |
| 9 | Setting up a Password Policy in Freshservice | `password-policy.md` | ⏳ 대기 |
| 10 | Changing Requester Password in Freshservice | `changing-requester-password.md` | ⏳ 대기 |
| 11 | Adding custom fields for requester departments | `custom-fields-departments.md` | ⏳ 대기 |
| 12 | Exporting Agent Information | `exporting-agent-info.md` | ⏳ 대기 |
| 13 | Importing Agent Information | `importing-agent-info.md` | ⏳ 대기 |
| 14 | Automatically Associating Contacts with Companies | `auto-associate-contacts.md` | ⏳ 대기 |
| 15 | Add Members/Observers to Agent Groups | `add-agent-group-members.md` | ⏳ 대기 |
| 16 | Create and Manage Agent Groups | `manage-agent-groups.md` | ⏳ 대기 |
| 17 | Create & Manage Requester Groups | `manage-requester-groups.md` | ⏳ 대기 |
| 18 | Importing departments/companies using a CSV file | `import-departments-csv.md` | ⏳ 대기 |
| 19 | Merging Users in Freshservice (Advanced Scenarios) | `merging-users-advanced.md` | ⏳ 대기 |

---

## 🎯 다음 단계 계획

### 즉시 작업: User Management 폴더 완료
**목표**: 2025년 9월 내 User Management 19개 문서 완료
**예상 소요**: 문서당 30-45분, 총 6-8시간

### 단계별 접근법
1. **7번 문서 작업** (현재 진행 중)
2. **8-19번 문서 순차 작업**
3. **sidebars.ts 업데이트**
4. **User Management 폴더 완료 검증**

---

## 📂 향후 폴더 계획 (Getting started with Freshservice 카테고리 내)

CSV 데이터 분석을 통해 확인된 주요 폴더들:
1. **User Management** - 19개 (현재 작업 중)
2. **Form Fields** - 추정 15-20개
3. **Fresh Themes** - 추정 10-15개
4. **Setting up Freshservice** - 추정 20-25개
5. 기타 폴더들...

---

## 🛠️ 작업 표준화 (다른 AI가 반드시 따라야 할 규칙)

### 문서 작성 필수 체크리스트
- [ ] **CSV에서 원문 추출**: Python 스크립트로 해당 문서 HTML 내용 확인
- [ ] **한국어 번역**: 기계번역 금지, 실무진이 바로 사용할 수 있도록 의역
- [ ] **템플릿 적용**: `document-template.md` 구조 100% 준수
- [ ] **ID 규칙**: 영어 소문자, 하이픈으로 단어 구분 (예: `csv-import-guidelines`)
- [ ] **파일 위치**: `docs/freshworks/freshservice/getting-started-with-freshservice/user-management/{id}.md`
- [ ] **이미지 URL**: 원본 AWS S3 URL 그대로 유지 (절대 변경 금지)
- [ ] **sidebars.ts 업데이트**: 새 문서 ID 추가
- [ ] **마스터 플랜 업데이트**: 상태를 ⏳ → ✅로 변경

### 절대 하지 말아야 할 것들
❌ 파일 위치 임의 변경  
❌ 이미지 URL 수정이나 단축  
❌ 기계번역 그대로 사용  
❌ 템플릿 구조 무시  
❌ sidebars.ts 업데이트 누락  

### 반드시 해야 할 것들
✅ HTML 내용을 실무 중심 한국어로 번역  
✅ 단계별 가이드로 구성  
✅ 경고/주의사항을 인용문으로 강조  
✅ 관련 문서 링크 포함  
✅ 모든 이미지에 설명적 alt 텍스트 추가  

### Frontmatter 표준 형식
```yaml
---
id: {간단한-영어-slug}
title: {한국어 제목}
sidebar_label: {짧은 한국어 라벨}
sidebar_position: {순서 번호}
---
```

### sidebars.ts 업데이트 위치
파일에서 이 부분을 찾아 새 문서 ID 추가:
```typescript
// User Management 폴더 (19개 문서)
{
  type: 'category',
  label: '👥 사용자 관리',
  collapsed: false,
  items: [
    'freshworks/freshservice/getting-started-with-freshservice/user-management/understanding-agents',
    'freshworks/freshservice/getting-started-with-freshservice/user-management/setting-agent-roles-permissions',
    // ... 기존 문서들
    'freshworks/freshservice/getting-started-with-freshservice/user-management/{새-문서-id}', // 여기에 추가
  ],
},
```

---

## 📊 진행률 추적

### 전체 프로젝트 진행률
- **전체 목표**: 1,557개 문서
- **현재 완료**: 6개 문서 (0.4%)
- **현재 카테고리**: Getting started with Freshservice (115개)
- **현재 폴더**: User Management (19개 중 6개 완료)

### 마일스톤
- [ ] **Milestone 1**: User Management 폴더 완료 (19/19)
- [ ] **Milestone 2**: Getting started with Freshservice 카테고리 완료 (115/115)
- [ ] **Milestone 3**: 첫 번째 주요 카테고리 완료
- [ ] **Milestone 4**: 500개 문서 완료
- [ ] **Milestone 5**: 1,000개 문서 완료
- [ ] **Milestone 6**: 전체 프로젝트 완료 (1,557/1,557)

---

## 🚀 재시작 가이드 (다른 AI를 위한 상세 지침)

### STEP 1: 현재 상태 즉시 파악
```bash
# 현재 완료된 문서 확인
ls -la docs/freshworks/freshservice/getting-started-with-freshservice/user-management/

# 결과 예상: understanding-agents.md, setting-agent-roles-permissions.md, managing-requesters.md, importing-requesters-csv.md, finding-agent-user-id.md, adding-custom-fields-users.md (6개 파일)
```

### STEP 2: 다음 작업할 문서 확인
위의 "즉시 실행 커맨드"를 터미널에서 실행하여 7번 문서 내용 확인

### STEP 3: 문서 작성 표준 프로세스
1. **HTML을 한국어로 번역** (구글 번역 X, 실무 중심으로)
2. **템플릿 구조 적용** (document-template.md 참조)
3. **파일 생성** (`create_file` 도구 사용)
4. **sidebars.ts 업데이트** (`replace_string_in_file` 도구 사용)
5. **마스터 플랜 상태 업데이트** (⏳ → ✅ 변경)

### STEP 4: 필수 확인사항
- [ ] 파일이 정확한 위치에 생성되었는가?
- [ ] sidebars.ts에 새 문서가 추가되었는가?
- [ ] 마스터 플랜에서 상태가 업데이트되었는가?
- [ ] 템플릿 구조를 준수했는가?

### STEP 5: 다음 문서로 계속
8번 문서로 넘어가서 동일한 프로세스 반복

---

## 📋 프로젝트 개요

**목표**: CSV 데이터를 기반으로 Freshservice 완전 문서화  
**접근법**: 카테고리 > 폴더 > 문서 순서로 완료  
**구조**: `docs/freshworks/freshservice/{category}/{folder}/{article}.md`

---

## 📝 참고 파일들

- **템플릿**: `/.github/instructions/document-template.md`
- **마크다운 가이드**: `/.github/instructions/markdown-rewriting.instructions.md`
- **사이드바 설정**: `/sidebars.ts`
- **CSV 데이터**: `/raw_data/merged_articles_*.csv` (5개 파일)

---

**최종 업데이트**: 2025년 9월 6일  
**다음 작업**: User Management 7번 문서 "Guidelines to importing requesters from CSV files"
