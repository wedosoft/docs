---
title: 통합 문서 작성 템플릿
version: 3.0
date: 2025-09-06
applyTo: 'all-products'
---

# 통합 문서 작성 템플릿

## 📋 개요

이 문서는 모든 제품(Freshservice, Freshdesk, Freshworks 등)의 기술 문서를 일관성 있게 작성하기 위한 통합 템플릿입니다.

## 🚨 원본 서식 보존 - CRITICAL 지침

### ⚠️ 필수 원칙: 원본 콘텐츠 완전 보존

**모든 원본 콘텐츠를 반드시 보존해야 합니다:**

- ✅ **이미지**: 모든 스크린샷, 다이어그램, 아이콘 그대로 보존
- ✅ **테이블**: HTML 테이블 구조와 스타일 완전 보존  
- ✅ **HTML 마크업**: 원본 HTML 구조와 포맷팅 유지
- ✅ **링크**: 모든 내부/외부 링크 보존
- ✅ **강조/스타일**: Bold, Italic, 색상 등 모든 서식 유지
- ✅ **코드 블록**: 예제 코드와 설정값 그대로 보존

### ❌ 금지사항

- ❌ **완전 재작성**: 원본 내용을 완전히 새로 작성하지 말 것
- ❌ **이미지 삭제**: 원본에 있는 이미지를 임의로 제거하지 말 것  
- ❌ **테이블 단순화**: 복잡한 테이블을 간단하게 바꾸지 말 것
- ❌ **HTML → Markdown 변환**: 손실 없이 보존 가능한 경우만 변환

### ✅ 허용되는 작업

- ✅ **구조 재정리**: FAQ 형식으로 섹션 재구성
- ✅ **번역 및 개선**: 한국어 번역과 실무 중심 설명 추가
- ✅ **콘텐츠 보강**: 원본 기반으로 추가 설명과 예시 보강
- ✅ **UI 개선**: Docusaurus 컴포넌트로 가독성 향상

### 📝 올바른 접근법

**Before (잘못된 방법):**
```markdown
## Change 유형은 무엇인가요?
Change는 Emergency, Normal, Standard 3가지가 있습니다...
(완전히 새로 작성)
```

**After (올바른 방법):**
```markdown
## Change 유형은 무엇인가요?

<p><span style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0);">
Change Lifecycle is used to define and control the lifecycle of a change request based on the Change type...
</span></p>

<span style="border:none;display:inline-block;overflow:hidden;width:624px;height:327px;">
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001047228/original/cMvJwLsyccVH8ozNe4g1IjSdq4BOzS94Xg.png?1588534868" width="624" height="327" />
</span>

[원본 HTML과 이미지를 그대로 보존하면서 필요시 추가 설명만 보강]
```

이 지침을 따르지 않을 경우 **작업 재수행** 필요합니다.

## 🎯 적용 범위

- **모든 제품**: Freshservice, Freshdesk, Freshworks, 기타 모든 제품
- **모든 기능**: 사용자 관리, 자동화, 설정, 워크플로 등
- **모든 작업**: 한국어 번역, 리라이팅, 신규 문서 작성

## 📁 필수 디렉토리 구조

모든 문서는 다음 4단계 구조를 **반드시** 따라야 합니다:

```
docs/{product}/{category}/{folder}/{article}
```

### 구조 설명 및 예시

```
docs/
└── freshservice/         # 1. product (제품명)
    ├── freshservice-faqs/           # 2. category (CSV의 category_name)
    │   └── automations-and-triggers/    # 3. folder (CSV의 folder_name)
    │       └── scenario-automations-email-attachment.md  # 4. article
    └── apps-and-integrations/       # 2. category 
        └── extending-freshservice-integrations/  # 3. folder
            └── native-integrations-blossom.md    # 4. article
```

### 구조 규칙

1. **product**: `freshservice`, `freshdesk` 등
2. **category**: CSV의 `category_name`을 간단한 slug로 변환
3. **folder**: CSV의 `folder_name`을 간단한 slug로 변환  
4. **article**: 개별 문서 파일명 (slug 규칙 적용)

### 카테고리/폴더 간소화 규칙

**카테고리 변환 예시**:
```
"Freshservice FAQs" → "faqs"
"How to Setup Apps and Integrations" → "apps"
"Support Guide: IT Service Management" → "it-service-mgmt"
"Getting started with Freshservice" → "getting-started"
```

**폴더 변환 예시**:
```
"Automations and Triggers" → "automations"
"Extending Freshservice with Integrations" → "integrations"
"Asset Management" → "assets"
"Service Catalog" → "catalog"
```

:::warning 구조 준수 필수
이 4단계 구조를 벗어나면 사이드바 네비게이션과 URL 구조가 깨집니다. 반드시 준수하세요.
:::

## 📝 표준 템플릿

### 기본 구조

```markdown
---
sidebar_position: [숫자]
---

# [문서 제목]

[해당 기능의 목적과 사용법을 1-2문장으로 간단히 설명]

:::info [상황별 안내]
- [중요한 제약사항이나 전제조건]
- [추가로 알아야 할 정보]
:::

## [주요 기능/설정] 방법

### 1단계: [첫 번째 작업]
[작업 설명 1-2문장]

1. **[메뉴 경로]**로 이동
2. **'[버튼/탭명]'** 클릭
3. [세부 설정 내용]

![설명](https://s3.amazonaws.com/.../image.png)

### 2단계: [두 번째 작업]
1. [구체적 액션]
2. [결과 확인 방법]

:::warning [주의사항 제목]
[중요한 제한사항이나 주의할 점]
:::

## [추가 기능/고급 설정] (해당시)

### [세부 기능명]
[설명과 사용 방법]

:::tip [유용한 팁]
[모범 사례나 효율적인 사용법]
:::

## 실무 활용 예시

### 상황 1: [구체적 비즈니스 상황]
**목표**: [달성하고자 하는 목표]
**방법**: 
1. [단계별 해결 과정]
2. [추가 설정 사항]

**결과**: [기대 효과]

### 상황 2: [다른 상황]
[동일한 구조로 2-3개 예시 제공]

## 문제 해결

### 자주 발생하는 문제

#### 문제: [구체적 문제 상황]
**원인**: [문제 발생 이유]
**해결**: [단계별 해결 방법]

:::success [해결 완료]
[성공적인 결과 메시지]
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [관련 문서 1](./relative-path-1)
- [관련 문서 2](./relative-path-2)
- [외부 참조](https://external-link.com)
-->
```

## 🔧 작성 지침

### Frontmatter 규칙
```yaml
---
sidebar_position: 숫자  # 필수: 사이드바 순서
---
```

**제거할 필드들** (Docusaurus가 자동 생성):
- `id`, `title`, `sidebar_label` 등

### 제목 작성법
- **H1 형식**: 명사형 선호 (예: `설정 방법` ❌ → `자동 분류 설정` ✅)
- **간결함**: 3-6단어로 핵심만 표현
- **일관성**: 동일한 제품군 내에서 제목 패턴 통일

### 파일 및 폴더 Slug 규칙

#### 카테고리/폴더명 Slug
- **원칙**: 핵심 키워드만 추출, 3-4개 단어 이내
- **형식**: 소문자 + 하이픈 연결
```
"Freshservice FAQs" → "freshservice-faqs"
"How to Setup Apps and Integrations" → "apps-and-integrations"
"Automations and Triggers" → "automations-and-triggers"
"Asset Management" → "asset-management"
```

#### 문서 파일명 Slug  
- **원칙**: 기능 중심, 질문형 → 기능 설명형 변환
- **길이**: 3-5개 핵심 키워드만 사용
- **형식**: 소문자 + 하이픈 + .md 확장자

**예시 변환**:
```
원본: "If I choose Send Email to... or Add Note using Scenario Automations, would I have the option to add an attachment?"
→ "scenario-automations-email-attachment.md"

원본: "How do I automatically close any resolved ticket after 48 hours?"
→ "auto-close-resolved-tickets-48hours.md"

원본: "Are automations case sensitive when we use the Subject/Description contains?"
→ "automations-case-sensitive-subject-description.md"
```

**Slug 생성 가이드라인**:
1. 불필요한 단어 제거 (I, do, the, any, when, we, use 등)
2. 핵심 기능/개념 키워드 추출
3. 숫자는 유지 (48hours, 365days 등)
4. 약어 사용 가능 (auto, config, mgmt 등)

### Callout 박스 활용

#### 정보 제공
```markdown
:::info 다중 워크스페이스 환경
계정에 여러 워크스페이스가 있는 경우 각각 별도로 설정해야 합니다.
:::
```

#### 주의사항
```markdown
:::warning 플랜 제한
이 기능은 Pro/Enterprise 플랜에서만 사용 가능합니다.
:::
```

#### 유용한 팁
```markdown
:::tip 효율적인 설정
- 테스트 환경에서 먼저 검증
- 사용자 그룹별로 단계적 적용
:::
```

#### 성공 메시지
```markdown
:::success 설정 완료
모든 설정이 완료되었습니다. 이제 새로운 기능을 사용할 수 있습니다.
:::
```

## 📸 이미지 처리

### 기본 형식
```markdown
![설명 텍스트](https://s3.amazonaws.com/cdn.freshdesk.com/.../image.png)
```

### 중요 규칙
- ✅ **원본 URL 유지**: AWS S3 경로 그대로 사용
- ❌ **경로 변경 금지**: 빌드 오류 방지
- ✅ **alt 텍스트**: 의미 있는 설명 추가 권장

## 📊 표(Table) 작성

### 간단한 표 (Markdown)
```markdown
| 필드명 | 설명 | 예시 |
|--------|------|------|
| 이름 | 사용자 이름 | 홍길동 |
| 부서 | 소속 부서 | 개발팀 |
```

### 복잡한 표 (HTML)
셀 내 줄바꿈, 링크, 강조 등이 필요한 경우:

```html
<table>
<thead>
<tr><th>필드명</th><th>설명</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>자리표시자</strong></td>
  <td>동적 값 삽입<br/>예: <code>&#123;&#123;ticket.id&#125;&#125;</code></td>
</tr>
</tbody>
</table>
```

## 🌐 다국어 처리

### 번역 원칙
- **실용 중심**: 단순 직역보다 한국 실무 환경에 맞게 의역
- **용어 통일**: 제품별 고유 용어는 원문 병기
- **예시 현지화**: 외국 회사명 → 한국 기업명으로 변경

### 톤앤매너
- **친근하고 실용적**: 딱딱한 매뉴얼보다 실무 가이드 느낌
- **구체적**: 추상적 설명보다 구체적 예시와 단계
- **완결성**: 해당 문서만으로도 작업 완료 가능한 수준
- **초보자 친화적**: 어려운 용어 뒤에는 괄호로 쉬운 설명 추가
  - 예: "워크플로(업무 흐름)", "자동화 규칙(미리 설정한 동작)", "API(프로그램 간 연결 방법)"

## 🚀 제품별 적용 가이드

### Freshservice
- **경로**: `/docs/freshservice/`
- **특징**: IT 서비스 관리, 티켓 관리, 자산 관리
- **주요 사용자**: IT 관리자, 헬프데스크 담당자

### Freshdesk
- **경로**: `/docs/freshdesk/`
- **특징**: 고객 지원, 티켓 시스템, 지식베이스
- **주요 사용자**: 고객 상담원, 지원팀 관리자

### 기타 제품
- **경로**: `/docs/[제품명]/`
- **특징**: 제품별 고유 기능에 맞게 템플릿 조정
- **사용자**: 해당 제품 실무 담당자

## 📋 품질 체크리스트

### 필수 요소 확인
- [ ] `sidebar_position` 설정
- [ ] H1 제목이 명확하고 간결
- [ ] 1-2문장 개요 설명
- [ ] 단계별 설정 방법 제공
- [ ] 실무 예시 2-3개 포함
- [ ] Callout 박스 적절히 활용
- [ ] 이미지 경로 정상 작동
- [ ] "관련 문서" 섹션 표준 형식

### 품질 기준
- **완성도**: 해당 문서만으로 작업 완료 가능
- **실용성**: 실무자가 바로 적용 가능
- **일관성**: 동일한 구조와 톤앤매너
- **정확성**: 기술적 내용 검증 완료

## 🔧 작업 프로세스

### 1단계: 원본 분석
```bash
# CSV에서 HTML 추출 후 내용 파악
python extract_content.py "[문서 제목]"
```

### 2단계: 구조 설계
- 기존 내용을 표준 템플릿 구조에 맞게 재구성
- 실무 시나리오 및 문제 해결 섹션 추가 계획

### 3단계: 작성 및 번역
- 표준 템플릿 적용
- 한국어 번역 및 실무 중심 리라이팅
- UI 컴포넌트 활용

### 4단계: 검토 및 배포
- 체크리스트 기반 품질 확인
- 빌드 테스트 및 링크 검증
- Git 커밋 및 배포

## 🎯 성공 사례

**user-management 폴더 20개 문서**에서 이 템플릿을 성공적으로 적용:
- ✅ 일관된 구조로 가독성 향상
- ✅ Broken links 제로로 안정적 빌드
- ✅ 실무자 피드백 긍정적

이 성공 패턴을 모든 제품에 확장 적용합니다.

---

**버전 이력**:
- v3.0 (2025-01-06): 통합 템플릿으로 단순화 및 범용화
- v2.0: Freshservice 전용 템플릿
- v1.0: 초기 복잡한 구조 템플릿
