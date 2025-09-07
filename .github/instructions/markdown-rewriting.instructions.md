---
applyTo: '**'
---

⸻

id: markdown-rewriting-guidelines
title: 마크다운 자동화 지침서
sidebar_label: 자동화 지침서

<div class="subtitle">
  이 문서는 📁 문서 저장 구조

**콘텐츠 문서 (실제 고객 대상 문서):**

docs/{{product_slug}}/{{category_slug}}/{{folder_slug}}/{{slug}}.md

**프로젝트 관리 문서:**

- **documents/**: 프로젝트 현황, 계획, 가이드라인 등 관리 문서
- **scripts/**: 자동화 스크립트 및 변환 도구
- **.github/instructions/**: 작업 지침 및 표준 문서

	•	slug 규칙:
	•	소문자
	•	공백은 하이픈(-)
	•	특수문자는 제거 또는 하이픈 치환
	•	버전, 날짜, "final", "temp" 등 포함 금지

예시:
	•	"Create & Manage Users" → create-manage-users
	•	"CSAT (Customer Satisfaction Survey)" → csat-customer-satisfaction-survey

**파일 위치 결정 가이드:**
	•	고객용 기술 문서 → docs/ 하위
	•	프로젝트 관리 문서 → documents/
	•	변환/처리 스크립트 → scripts/
	•	작업 표준/지침 → .github/instructions/를 자동 변환하는 작업에서 지켜야 할 작성 규칙과 스타일 지침을 정리한 내부용 가이드입니다.
</div>


📌 문서 목적

Docusaurus 기반 기술 문서 포털(docs.wedosoft.net)에 포함될 고객지원 문서를
CSV 원문 → Markdown(.md) 문서로 자동 변환하는 과정에서 다음 사항을 준수합니다:
	•	문서를 한국어로 번역 및 실용 중심으로 리라이팅
	•	실무자가 바로 활용 가능한 업무 흐름 기반 구성
	•	Markdown 문법, JSX 문법, Docusaurus 렌더링 특성을 모두 반영

⸻

🎯 주요 독자
	•	신입 상담원, 헬프데스크 관리자, 일반 실무 담당자
	•	복잡한 기술 지식이 없는 사람도 쉽게 이해할 수 있도록 작성

⸻

✍️ 리라이팅 목적
	•	단순 번역이 아닌, 실제 업무 흐름에 맞춘 실용 문서로 재작성
	•	문서 목적이 명확히 드러나도록 구성
	•	예시 중심 설명, 필요한 경우 팁/주의사항을 인용문으로 강조

⸻

🧭 제목 및 부제목 작성 지침
	•	제목(title): 문장이 아닌 핵심 키워드 조합으로 짧고 간결하게 작성
	•	불필요한 동사/조사 생략 (예: 설정하는 방법 ❌ → 설정 가이드 ✅)

예시:
	•	공통 응답 템플릿
	•	자리표시자 기능
	•	자동 분류 설정

Frontmatter 예시:

---
id: {{slug}}
title: {{md_title}}
sidebar_label: {{md_title}}
---

부제목:

<div class="subtitle">
  이 문서는 "{{topic_korean}}({{topic_english}})" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>


⸻

🛠️ 마크다운(MD) 작성 지침
	•	문단 구분: 빈 줄(\n\n)
	•	강조: **텍스트**, 기울임: *텍스트*
	•	인라인 코드: `코드`
	•	중괄호 {{...}} 는 &#123;&#123;...&#125;&#125; 로 이스케이프
	•	코드 블럭: ``` 코드내용 ```
	•	리스트: - 항목, 1. 항목
	•	인용문: > 인용 내용 (후처리 시 Callout 컴포넌트로 변환됨)

⸻

🧠 style 속성 처리 규칙

React 렌더링 오류 방지를 위한 필수 규칙 (Docusaurus에서 .md도 JSX로 처리됨)

변환 지시:
	1.	style="..." 형식은 모두 style={{ ... }} 형식으로 치환
	2.	속성명은 camelCase 변환 (margin-right → marginRight)
	3.	값은 문자열로 처리 (1em → '1em')
	4.	HTML 주석 안의 style은 변경하지 않음

예시:

<!-- 잘못된 예시 -->
<span style="color: red;">텍스트</span>

<!-- 올바른 변환 -->
<span style={{ color: 'red' }}>텍스트</span>


⸻

🖼️ 이미지 및 첨부파일 처리 지침
	•	Markdown 이미지 형식만 사용:

![설명](https://s3.amazonaws.com/.../image.png)

금지 사항:
	•	<img src="...">, assets/image.png, style, class 포함 ❌
	•	alt 텍스트는 가능하면 삽입, 생략 가능
	•	경로 단축, 변형 절대 금지 (빌드 오류 유발)

⸻

📊 표(Table) 작성 지침
	•	기본: Markdown 표 형식 사용

| 자리표시자 | 설명 |
|------------|------|
| {{ticket.id}} | 고유 티켓 ID |

	•	다음 조건이면 반드시 HTML <table> 사용:
	•	셀 안에 줄바꿈, 리스트, 링크, 강조, 이미지, 코드 등 포함될 경우

HTML 표 예시:

<table>
<thead>
<tr><th>Key</th><th>설명</th></tr>
</thead>
<tbody>
<tr>
  <td><code>&#123;&#123;ticket.id&#125;&#125;</code></td>
  <td>고유 티켓 ID</td>
</tr>
</tbody>
</table>


⸻

📁 문서 저장 구조

docs/{{product_slug}}/{{category_slug}}/{{folder_slug}}/{{slug}}.md

	•	slug 규칙:
	•	소문자
	•	공백은 하이픈(-)
	•	특수문자는 제거 또는 하이픈 치환

예시:
	•	“Create & Manage Users” → create-manage-users
	•	“CSAT (Customer Satisfaction Survey)” → csat-customer-satisfaction-survey

⸻

🔗 참조 문서 링크 처리 지침

broken links 방지를 위한 단계별 접근 방식:

처리 원칙:
	•	모든 문서 생성 완료 전까지는 참조 문서 링크를 추가하지 않음
	•	문서 하단에 "관련 문서" 섹션 제목만 생성
	•	최종 작업 단계에서 일괄적으로 링크 연결 작업 수행
	•	Broken links 방지를 위한 필수 절차

작성 형식:

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

금지 사항:
	•	존재하지 않는 문서로의 링크 생성 ❌
	•	상대 경로 추측을 통한 링크 생성 ❌
	•	임시 또는 가정적 링크 생성 ❌
	•	빌드 오류를 유발하는 broken links 생성 ❌

⸻

✅ 향후 확장 포인트
	•	예외 케이스 정리: 빈 제목, 누락된 필드, 이미지 없는 문서 등
	•	전처리 자동화 로직: Python 기반 CLI 도구로 단계별 처리
	•	향후 .mdx 전환 시 JSX 컨포넌트 지원 지침 추가 예정