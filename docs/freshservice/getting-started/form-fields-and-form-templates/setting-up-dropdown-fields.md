---
sidebar_position: 3
---

# 드롭다운 필드 설정

:::info 문서 목적
이 문서는 "Dropdown Fields(드롭다운 필드)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
:::

드롭다운 필드는 사용자가 미리 정의된 옵션 목록에서 값을 선택할 수 있도록 하는 필드 유형입니다. Freshservice에서 티켓, 문제, 변경, 릴리스에 모두 사용할 수 있으며, 서비스 카탈로그의 사용자 정의 필드를 만들 때도 활용할 수 있습니다.

## 드롭다운 필드의 주요 특징

### 선택 옵션 제공
- 사용자가 드롭다운 메뉴에서 미리 정의된 옵션을 선택
- 데이터 일관성 및 정확성 보장
- 사용자 입력 오류 최소화

### 다양한 활용 영역
- **티켓**: 우선순위, 카테고리, 상태 등
- **문제 관리**: 영향도, 긴급도 설정
- **변경 관리**: 변경 유형, 승인 상태
- **릴리스 관리**: 릴리스 타입, 상태
- **서비스 카탈로그**: 요청 항목의 사용자 정의 필드

## 드롭다운 필드 설정 방법

### 1단계: Field Manager 접근

:::info 접근 경로
**Admin Settings > Global Settings > Field Manager**
:::

#### 특별한 경우의 접근 경로

| 용도 | 접근 경로 |
|------|-----------|
| **서비스 카탈로그** | Admin Settings > Global Settings > Service Catalog > Catalog Item |
| **개별 워크스페이스** | Admin Settings > Global Settings > Workspace Settings > Field Manager |

### 2단계: 티켓 필드 선택

**Ticket Fields** 섹션을 선택합니다.

![티켓 필드 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013325153/original/946HWtEEBuIUW1e4qM2UyQlVmrJQV17dNg.png?1728413909)

### 3단계: 드롭다운 필드 추가

드래그 앤 드롭 필드 박스에서 **Dropdown**을 클릭하여 필드를 추가합니다.

### 4단계: 필드 속성 설정

다음 항목들을 설정합니다:

#### 기본 설정
- **필드 가시성**: 어떤 사용자에게 표시될지 결정
- **편집 가능 여부**: 사용자가 값을 수정할 수 있는지 설정
- **필수 필드 여부**: 티켓 제출 시 반드시 입력해야 하는지 설정

#### 필드 이름 사용자 정의
상담원과 요청자를 위한 필드 이름을 각각 설정합니다.

![필드 속성 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013325145/original/HS9rb9D6hjTvJVXjntdYmI0Gibjyr6iN1g.png?1728413804)

### 5단계: 드롭다운 유형 선택

두 가지 옵션 중 하나를 선택합니다:

#### Custom Dropdown (사용자 정의 드롭다운)
- 드롭다운에 표시될 선택 항목을 직접 추가
- 완전한 제어 가능
- 정적인 옵션 목록에 적합

#### Select from Data Source (데이터 소스에서 선택)
- 기존 데이터 소스에서 옵션을 가져옴
- 동적인 데이터 연동 가능
- 다른 시스템과의 연계에 적합

### 6단계: 선택 항목 추가

드롭다운에 표시될 선택 항목을 추가합니다.

#### 일괄 선택 항목 추가 (Bulk Add Choices)
:::tip 효율적인 입력 방법
- 여러 선택 항목을 한 번에 입력 가능
- Enter 키를 사용하여 새 선택 항목 추가
- 중복된 선택 항목은 자동으로 건너뜀
- 기존 선택 항목을 새로운 항목으로 일괄 대체 가능
:::

### 7단계: 설정 저장

1. **Done** 클릭하여 필드 설정 저장
2. **Save** 클릭하여 전체 폼 저장

:::warning 워크스페이스 워크플로 주의사항
워크스페이스 관리자는 해당 워크스페이스에 적용되는 글로벌 및 로컬 워크플로 목록을 확인할 수 있습니다. 글로벌 워크플로가 먼저 실행되고, 이어서 워크스페이스 수준 워크플로가 실행됩니다.
:::

## 드롭다운 필드 활용 팁

### 데이터 일관성 향상
- 표준화된 값으로 보고서 품질 향상
- 오타 및 입력 오류 방지
- 데이터 분석 시 정확성 보장

### 사용자 경험 개선
- 빠른 선택을 통한 입력 시간 단축
- 명확한 옵션 제공으로 혼란 최소화
- 직관적인 인터페이스 제공

### 업무 효율성 증대
- 일관된 분류 체계 구축
- 자동화 규칙 적용 용이
- 데이터 분석 및 보고서 생성 효율성 향상

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [티켓 필드 설정 가이드](./setting-up-form-fields-tickets-problems-changes-releases)
- [다양한 티켓 필드 유형 이해](./understanding-different-types-ticket-fields)
- [사용자 정의 필드 생성](./creating-custom-fields-ticket-problem-change-release-task-form)
-->
