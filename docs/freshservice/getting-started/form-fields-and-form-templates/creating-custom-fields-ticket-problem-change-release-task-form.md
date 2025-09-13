---
sidebar_position: 4
---

# 사용자 정의 필드 생성

:::info 문서 목적
이 문서는 "Custom Fields(사용자 정의 필드)" 기능의 개념과 생성 방법을 안내해요.
:::

Freshservice는 티켓, 문제, 변경, 릴리스와 관련된 작업을 효율적으로 관리할 수 있도록 작업(Task) 생성 기능을 제공해요. 큰 작업을 작은 단위로 나누어 부서 간 협업을 통해 업무를 추진할 수 있으며, 비즈니스 유형이나 지원 프로세스에 맞는 사용자 정의 필드를 추가해서 작업 폼을 완전히 커스터마이징할 수 있어요.

## 사용자 정의 필드의 필요성

### 기본 작업 폼의 한계
기본 작업 폼에는 다음과 같은 표준 필드들이 포함되어 있어요:
- **제목** (Title)
- **메모** (Note)
- **그룹** (Group)
- **담당자** (Assign to)
- **상태** (Status)
- **알림 시점** (Notify before)
- **마감일** (Due date)

### 커스터마이징의 장점
:::info 비즈니스 맞춤형 필드의 필요성
표준 필드만으로는 조직의 특별한 업무 프로세스나 산업별 요구사항을 충족하기 어려울 수 있어요. 사용자 정의 필드를 통해 조직의 고유한 워크플로우에 완벽하게 맞는 작업 관리 시스템을 구축할 수 있어요.
:::

## 사용자 정의 필드 설정 방법

### 1단계: Field Manager 접근

**Admin → Service Management → Service Desk Settings → Field Manager**로 이동해요.

![Field Manager 접근](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838232/original/R8omFCRr1VNX3kDmTdShngSb25sllEkPQA.png?1678706282)

### 2단계: 작업 필드 유형 선택

다음 중에서 설정하고자 하는 작업 필드 유형을 선택해요:
- **Ticket's Task Fields** - 티켓 작업 필드
- **Problem's Task Fields** - 문제 작업 필드  
- **Change's Task Fields** - 변경 작업 필드
- **Release's Task Fields** - 릴리스 작업 필드

![작업 필드 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838233/original/EGHYJbzHvaz8zmEVcM84TYfAZzpP70dwGg.png?1678706283)

### 3단계: 드래그 앤 드롭으로 필드 추가

드래그 앤 드롭 필드 영역에서 원하는 필드 유형을 선택해서 작업 폼에 추가해요.

![필드 추가](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838234/original/m6SA1yieYmOKHWSuuZbDdOeilzTOY8oxQg.png?1678706283)

## 사용자 정의 필드 유형별 가이드

![필드 유형 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838231/original/AJOwK6zHokykR8uqkdzNoUkd8Fy0bY-8TA.png?1678706282)

Freshservice는 다양한 정보 유형과 수준을 캡처할 수 있는 여러 종류의 작업 필드를 제공해요.

### 필드 유형별 상세 안내

| 필드 유형 | 활용 사례 | 작업당 최대 개수 |
|-----------|-----------|------------------|
| **Single line text** | 작업 ID, 간단한 텍스트 | 150개 |
| **Multiline text** | 추가 설명, 주소, 상세 메모 | 30개 |
| **Checkbox** | 구독 여부, 약관 동의 | 15개 |
| **Number** | 주문 ID, 전화번호 | 15개 |
| **Dropdown** | 수량, 크기, 카테고리 | 15개 |
| **Date** | 구매일, 접수일, 완료 예정일 | 10개 |
| **Decimal** | 백분율, 소수점 값 | 10개 |
| **URL** | 링크, 웹사이트 주소 | 제한 없음 |

### 각 필드 유형의 특징

#### Single Line Text (한 줄 텍스트)
:::tip 활용 팁
- 짧은 식별 정보나 키워드에 적합해요
- 작업당 최대 150개까지 추가 가능
- 검색과 필터링이 용이해요
:::

#### Multiline Text (여러 줄 텍스트)
- 상세한 설명이나 긴 메모에 사용
- 주소나 복합적인 정보 입력에 적합
- 작업당 최대 30개 제한

#### Checkbox (체크박스)
- 예/아니오 형태의 선택사항
- 조건 확인이나 승인 프로세스에 활용
- 간단한 상태 표시에 효과적

#### Number & Decimal (숫자 & 소수점)
- 정확한 수치 데이터 입력
- 통계 분석과 보고서 생성에 유용
- 계산 기능과 연동 가능

#### Dropdown (드롭다운)
- 미리 정의된 옵션에서 선택
- 데이터 일관성 보장
- 사용자 입력 오류 최소화

#### Date (날짜)
- 일정 관리와 마감일 추적
- 시간 기반 워크플로우 구성
- 자동 알림 기능과 연동

#### URL (웹 주소)
- 외부 리소스 링크
- 참조 문서나 웹사이트 연결
- 클릭 가능한 링크로 표시

## 필드 속성 설정

![필드 속성 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838235/original/hqp2QxTvw1z8MiHJiFXGO0zcZwsXs_1gFw.png?1678706283)

새 필드를 추가하고 재배열하는 것 외에도, 작업 폼의 각 필드에 대한 속성을 정의할 수 있습니다. 필드 속성을 통해 상담원이 작업 폼에서 보게 될 내용을 제어하고 헬프데스크 워크플로우를 더 효과적으로 관리할 수 있습니다.

### 주요 필드 속성

| 속성 | 의미 |
|------|------|
| **Required when creating a task** | 작업 생성 시 반드시 입력해야 하는 필드 |
| **Required when completing the task** | 작업 완료 시 반드시 입력해야 하는 필드 |
| **Field Name** | 상담원에게 표시되는 필드 이름 |

### 속성 활용 전략

#### 작업 생성 시 필수 필드
:::warning 중요 정보 누락 방지
작업 시작에 꼭 필요한 정보를 필수 필드로 설정하여 초기 데이터 품질을 보장하세요.
:::

**적용 예시:**
- 작업 카테고리
- 담당 부서
- 우선순위 수준

#### 작업 완료 시 필수 필드
완료 단계에서 품질 관리와 추후 분석을 위한 필수 정보를 설정합니다.

**적용 예시:**
- 실제 소요 시간
- 완료 결과 평가
- 이슈 발생 여부

## 필드 관리 모범 사례
5. **테스트 완료율** (Decimal) - 백분율로 입력

## 멀티 모듈 설정

:::info 모든 모듈에 동일 적용
Problem, Change, Release 작업 필드도 동일한 방법으로 설정할 수 있습니다. 각 모듈의 특성에 맞는 사용자 정의 필드를 구성하여 통합적인 서비스 관리 환경을 구축하세요.
:::

### 모듈별 권장 필드

#### Problem Task Fields (문제 작업 필드)
- 근본 원인 분석 결과
- 영향을 받은 사용자 수
- 해결책 문서 링크

#### Change Task Fields (변경 작업 필드)
- 변경 승인 번호
- 롤백 계획 여부
- 리스크 평가 점수

#### Release Task Fields (릴리스 작업 필드)
- 릴리스 버전 번호
- 배포 환경
- 테스트 통과율

## 모범 사례

### 필드 설계 원칙
1. **목적 명확성**: 각 필드의 수집 목적을 명확히 정의
2. **일관성 유지**: 유사한 유형의 작업에는 동일한 필드 구조 적용
3. **사용자 편의성**: 입력하기 쉽고 이해하기 쉬운 필드명 사용
4. **데이터 품질**: 필수 필드와 선택 필드의 적절한 균형

### 성능 고려사항
:::warning 필드 수 제한 주의
각 필드 유형별로 최대 개수 제한이 있으므로, 필요한 필드를 우선순위에 따라 선별하여 추가하세요.
:::

### 운영 및 유지보수
- 정기적인 필드 사용률 검토
- 불필요한 필드 제거
- 사용자 피드백 기반 개선

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [폼 필드 기본 설정](./setting-up-form-fields-tickets-problems-changes-releases)
- [다양한 티켓 필드 유형 이해](./understanding-different-types-ticket-fields)
- [드롭다운 필드 설정](./setting-up-dropdown-fields)
- [종속 필드 이해](./understanding-dependent-fields)
-->
