# 📋 작업 지침서 v3.0

> **목적**: Freshservice 문서 수작업 변환 프로젝트의 표준 작업 절차 및 품질 관리 규칙

## 🎯 수작업 변환 작업 프로세스

### ✏️ **카테고리별 CSV 파일 기반 작업** (2025.09.11 확정)

#### 작업 파일 구조
```
categories/
├── Freshservice_FAQs.csv (508개) - 우선 작업 대상
├── Support_Guide_IT_Service_Management.csv (187개)
├── Getting_started_with_Freshservice.csv (115개)
├── Platform.csv (101개)
└── 기타 16개 카테고리 파일
```

#### 작업 프로세스
```
1단계: 카테고리 CSV 파일 선택
2단계: 문서 하나 선택 (ID, title, description 필드 확인)
3단계: description 필드(HTML)에서 콘텐츠 추출
4단계: HTML → Markdown 기본 변환
5단계: 한국어 실무 중심 리라이팅
6단계: v3.0 템플릿 적용 (sidebar_position)
7단계: MDX 호환성 확인
8단계: 완료 표시 (파일명 변경 또는 별도 관리)
```

#### 수작업 변환의 장점
```
높은 품질 보장:
- 기술 문서의 정확성 최우선
- 한국 실무 환경에 맞는 자연스러운 번역
- 문맥과 의도를 정확히 파악한 변환
- Docusaurus 구조에 최적화된 형태
```

---

## 📝 문서 형태별 표준 템플릿

### 🤖 **FAQ 문서 (아코디언 형태)**
```markdown
---
title: [카테고리명] FAQ
description: [카테고리] 기능에 대한 자주 묻는 질문
sidebar_position: 1
---

# 🤖 [카테고리명] FAQ

[카테고리] 기능에 대한 자주 묻는 질문입니다.

<details>
<summary><strong>Q1. [한국어 질문]</strong></summary>

[한국어 답변]

</details>

<details>
<summary><strong>Q2. [한국어 질문]</strong></summary>

[한국어 답변]

</details>

---

💡 **더 복잡한 설정이나 고급 기능에 대한 질문이 있으시면 지원팀에 문의해 주세요.**
```

### 📄 **일반 문서 (표준 MDX 형태)**
```markdown
---
title: [기능명]
description: [기능에 대한 간단한 설명]
sidebar_position: [순서]
---

# [기능명]

<div class="subtitle">
  이 문서는 "[기능명(영문)]" 기능의 개념과 설정 방법을 안내합니다.
</div>

## 기능 개요
[기능 설명]

## 설정 방법
### 1단계: [단계명]
[설정 내용]

### 2단계: [단계명]  
[설정 내용]

## 주의사항
[주의할 점들]

## 관련 문서
- [관련 문서 링크]
```

---

## 🔄 품질 관리 워크플로우

### **단계별 품질 검사**

#### 1. 문서 생성 후 (개별 문서)
```bash
# 필수 확인 사항
□ 한국어 번역 완료
□ 아코디언/표준 형태 올바름
□ 메타데이터 한국어 설정
□ 이미지 링크 정상 작동
□ MDX 문법 오류 없음
```

#### 2. 폴더 완료 후 (폴더 단위)
```bash
# 필수 확인 사항
□ 모든 문서 번역 완료
□ 폴더 구조 정확함
□ 빌드 테스트 통과 (npm run build)
□ 사이드바 정상 표시
□ 네비게이션 작동 확인
```

#### 3. 카테고리 완료 후 (카테고리 단위)
```bash
# 필수 확인 사항
□ 전체 빌드 성공
□ 사이드바 업데이트 완료
□ 링크 오류 없음
□ 이미지 표시 정상
□ 문서 현황 업데이트
```

### **자동화 스크립트 활용**

#### 복잡도 분석 스크립트
```python
# /scripts/analyze_complexity.py
# 사용법: python scripts/analyze_complexity.py [카테고리명]
# 결과: 복잡도별 문서 분류 및 처리 권장사항
```

#### 대량 변환 스크립트
```python  
# /scripts/bulk_converter.py
# 사용법: python scripts/bulk_converter.py --complexity SIMPLE
# 결과: SIMPLE 복잡도 문서 일괄 변환
```

---

## 🎯 기본 원칙 (기존 유지)

### 1. 문서 품질 우선
- **복잡도 맞춤 처리** → SIMPLE은 자동화, HIGH는 수동
- **원본 서식 보존** → 이미지, 테이블 최대한 유지
- **즉시 활용 가능** → 실무 중심 리라이팅

### 2. 일관성 유지  
- **카테고리별 완주** → 혼재 작업 금지
- **표준 템플릿 준수** → FAQ vs 일반문서 구분
- **순차적 진행** → 복잡도 순서 준수

### 3. 자동화 우선
- **복잡도 분석 자동화** → 스크립트 활용
- **SIMPLE 문서 대량 처리** → 자동 변환
- **품질 검증 자동화** → 빌드 테스트 필수

---

## 📁 파일 및 폴더 규칙

### 폴더 명명 규칙
```bash
# 올바른 예시
form-fields/
user-management/
setting-up-freshservice/

# 잘못된 예시
Form_Fields/
UserManagement/
Setting Up Freshservice/
```

### 파일 명명 규칙
```bash
# 올바른 예시
create-custom-fields.md
configure-user-roles.md
set-up-email-notifications.md

# 잘못된 예시
Create Custom Fields.md
configureUserRoles.md
set_up_email_notifications.md
```

### slug 생성 규칙
```javascript
// 변환 예시
"Create & Manage Users" → "create-manage-users"
"CSAT (Customer Satisfaction Survey)" → "csat-customer-satisfaction-survey"
"Set Up Email Notifications" → "set-up-email-notifications"
```

---

## � 파일 조직화 및 파편화 방지

### 🎯 핵심 원칙
- **단일 진실 원천**: 각 주제에 대해 하나의 문서만 유지
- **적절한 위치**: 문서 유형별 지정된 폴더 사용
- **즉시 정리**: 임시 파일이나 중복 문서는 작업 완료 즉시 정리

### 📂 폴더 사용 규칙
- **documents/**: 프로젝트 관리 문서 (현황, 계획, 가이드라인)
- **scripts/**: 모든 자동화 스크립트 및 변환 도구
- **.github/instructions/**: 작업 지침 및 표준 문서
- **docs/**: 실제 고객 대상 콘텐츠 문서만

### ⚠️ 파편화 방지 규칙
1. **새 문서 생성 전**: 기존 문서에 추가할 수 있는지 먼저 확인
2. **임시 파일 금지**: "temp", "final", "v2" 등이 포함된 파일명 사용 금지
3. **중복 내용 금지**: 비슷한 주제의 여러 문서 대신 하나로 통합
4. **작업 완료 시**: 모든 임시 파일 및 중복 문서 즉시 정리

> **상세 가이드**: [워크스페이스 조직화 지침](../.github/instructions/workspace-organization.md) 참조

---

## �📝 문서 작성 표준

### Frontmatter (v3.0 템플릿)
```yaml
---
sidebar_position: 1
---
```

### 제목 구조
```markdown
# 간결한 기능명

<div class="subtitle">
  이 문서는 "기능명(영문)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>
```

### 섹션 구성 패턴
```markdown
## 기능 개요
## 설정 방법
### 1단계: 기본 설정
### 2단계: 고급 설정
## 사용 예시
## 주의사항
## 관련 문서
```

---

## 🛠️ MDX 호환성 규칙

### 한글 중괄호 처리
```markdown
# 잘못된 예시
{워크스페이스명}
{티켓번호}

# 올바른 예시
&#123;워크스페이스명&#125;
&#123;티켓번호&#125;
```

### Freshservice 자리표시자
```markdown
# 잘못된 예시
{{ticket.id}}
{{user.name}}

# 올바른 예시
`{{ticket.id}}`
`{{user.name}}`
```

### Style 속성 처리
```markdown
# 잘못된 예시
<span style="color: red;">텍스트</span>

# 올바른 예시
<span style={{ color: 'red' }}>텍스트</span>
```

---

## 🖼️ 이미지 및 미디어 처리

### 이미지 링크
```markdown
# 표준 형식 (변경 금지)
![설명](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155123456789/original/image.png)

# 금지 형식
<img src="..." />
![설명](./images/image.png)
![설명](../assets/image.png)
```

### 표(Table) 작성
```markdown
# 기본: Markdown 표
| 자리표시자 | 설명 |
|------------|------|
| `{{ticket.id}}` | 티켓 고유 ID |

# 복잡한 내용: HTML 표
<table>
<thead>
<tr><th>기능</th><th>설명</th></tr>
</thead>
<tbody>
<tr>
  <td><code>&#123;&#123;ticket.id&#125;&#125;</code></td>
  <td>티켓의 고유 식별번호<br/>예: T-12345</td>
</tr>
</tbody>
</table>
```

---

## 🔍 품질 검사 체크리스트

### 문서 작성 후 필수 확인
- [ ] **빌드 테스트**: `npm run build` 오류 없음
- [ ] **링크 검증**: 모든 링크가 정상 작동
- [ ] **이미지 확인**: 모든 이미지가 정상 표시
- [ ] **MDX 호환성**: 중괄호, style 속성 확인
- [ ] **사이드바 위치**: 논리적 순서 확인

### 폴더 완료 후 필수 확인
- [ ] **sidebars.ts 업데이트**: 새 폴더 구조 반영
- [ ] **README 갱신**: 완료 현황 업데이트
- [ ] **Git 커밋**: 의미 있는 커밋 메시지

---

## 🚨 자주 발생하는 실수

### 1. 링크 관련
❌ **하지 말 것**
- 존재하지 않는 문서로 링크
- 상대 경로 추측으로 링크 생성
- 임시 또는 가정적 링크

✅ **해야 할 것**
- 모든 문서 완성 후 링크 작업
- "관련 문서" 섹션만 미리 생성

### 2. 이미지 관련
❌ **하지 말 것**
- 경로 단축 또는 변형
- HTML img 태그 사용
- style, class 속성 추가

✅ **해야 할 것**
- 원본 S3 URL 그대로 사용
- Markdown 이미지 문법만 사용

### 3. 파일명 관련
❌ **하지 말 것**
- 공백, 대문자, 특수문자 사용
- 버전 번호나 날짜 포함
- 임시 파일명 그대로 두기

✅ **해야 할 것**
- 케밥 케이스(kebab-case) 사용
- 기능 중심 명명
- 일관된 규칙 적용

---

## 🔄 워크플로우

### 새 폴더 작업 시
1. **폴더 구조 확인** → 기존 패턴 파악
2. **문서 목록 작성** → 작업 범위 명확화
3. **템플릿 적용** → v3.0 표준 적용
4. **품질 검사** → 체크리스트 확인
5. **사이드바 업데이트** → sidebars.ts 수정
6. **문서화** → 진행 현황 업데이트

### 기존 문서 수정 시
1. **변경 이유 확인** → 필요성 검토
2. **영향 범위 파악** → 관련 문서 확인
3. **백업 생성** → Git 커밋
4. **수정 및 테스트** → 빌드 확인
5. **문서 업데이트** → 변경 사항 기록

---

## 📚 참고 자료

- [프로젝트 현황](./project-status.md) - 전체 진행 상황
- [MDX 문제해결](./mdx-troubleshooting.md) - 기술적 문제 해결
- [마크다운 작성 지침](./.github/instructions/markdown-rewriting.instructions.md) - 상세 작성 규칙

---

> **💡 기억하세요**: 이 지침서는 작업 효율성과 품질을 위한 최소한의 규칙입니다. 새로운 상황이 발생하면 기존 원칙을 확장하여 대응하세요.
