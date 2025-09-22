---
sidebar_position: 2
---

# 기본 SLA 정책 정의하기

Freshservice의 기본 SLA 정책은 헬프데스크로 들어오는 모든 티켓에 적용됩니다. 티켓의 우선순위에 따라 티켓의 마감 시간을 정의합니다. 시스템에 구성하면 상담원이 다음에 작업해야 할 티켓을 순차적으로 알려주어 매일 상담원의 업무 방식을 제어합니다.

:::info 중요 사항
워크스페이스 관리자는 워크스페이스 수준에서 SLA 정책을 생성할 수 있습니다.
1. 글로벌 SLA 정책은 모든 워크스페이스의 티켓에 적용됩니다
2. 기본 SLA 정책은 글로벌 수준에서 기본적으로 생성되고 활성화됩니다
3. 실행 순서: 티켓의 SLA 정책은 특정 워크스페이스용으로 생성된 로컬 SLA 정책에 의해 결정됩니다. 로컬 SLA 정책의 지정된 조건이 일치하지 않으면 글로벌 정책을 따릅니다. 두 정책 모두 적용되지 않으면 기본 SLA 정책이 티켓에 적용됩니다.
:::

## 기본 SLA 정책 생성을 위한 빠른 가이드

### 1단계: SLA 정책 설정 페이지 접근

**Admin > Service Management > Service Desk Settings > SLA and OLA Policies**를 클릭합니다.

**계정에 워크스페이스가 여러 개 있는 경우:**
- 글로벌 워크플로우 수정: **Admin > Global Settings > Service Management > Service Desk Settings > SLA and OLA Policies**로 이동
- 워크스페이스 수준 워크플로우 수정: **Admin > Workspace Settings > {Workspace Name} > Service Management > Service Desk Settings > SLA and OLA Policies**로 이동

### 2단계: 기본 SLA 정책 편집

기본 SLA 정책 아래에서 **Edit** 버튼을 클릭합니다.

### 3단계: 정책 설정

1. 선택적으로 기본 정책의 이름을 바꾸고 간단한 설명을 제공합니다.
2. **시간-우선순위 매트릭스**를 완성합니다.
3. SLA 정책은 티켓 우선순위에 따라 결정됩니다. 높은 우선순위나 낮은 우선순위 티켓을 구성하는 요소를 수동으로 정의하거나 워크플로우 자동화기를 사용하여 자동화할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006967159/original/zZtH_5UjJhG99efqKiFeuZDuF6OQrB3vNQ.png?1669027996" style={{width: 'auto'}} />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000085168/original/XJ0qMY6oTzyXQanYzcAjuzos4fx5fPZcHQ.gif?1565263006" style={{width: '624px', height: '395px'}} />

### 4단계: SLA 시간 계산 방법 선택

SLA 시간을 **비즈니스 시간 또는 달력 시간** 기준으로 계산할지 선택해야 합니다.

### 5단계: 에스컬레이션 설정 (선택사항)

1. 서비스 수준이 위반될 때 에스컬레이션을 활성화하려면 **에스컬레이션 이메일 버튼**을 켜기로 전환합니다.
2. 티켓이 언제, 누구에게 에스컬레이션되어야 하는지 정의하여 **에스컬레이션 계층구조**를 설정합니다.
3. 티켓 해결을 위해 최대 4단계의 에스컬레이션과 티켓 응답을 위해 1단계를 설정할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000085167/original/JKUz5OhuYqEItuU4S5nmhUbcT_ZBsOG-mw.png?1565262983" style={{width: '624px', height: '285px'}} />

### 6단계: 정책 저장

**Save** 버튼을 클릭하여 SLA 정책 설정을 완료합니다.

## 다중 SLA 정책

Freshservice에서 다양한 고객 계층, 제품, 상담원 그룹 등을 위한 여러 SLA 정책을 생성할 수도 있습니다. 예를 들어, 고가치 고객을 위한 "Express Support" SLA 정책을 가질 수 있습니다. 다중 SLA 정책 설정에 대한 자세한 내용은 [여기](https://support.freshservice.com/support/solutions/articles/156459-creating-multiple-sla-policies-for-specific-departments-and-groups)를 클릭하세요.

:::warning 참고사항
관리자는 이제 **티켓/문제/변경 및 릴리스(TPCR) 작업**에 대해 내부 **운영 수준 계약(OLA)**을 정의할 수 있습니다. 이는 상담원이 **TPCR 내부의 작업**을 완료해야 하는 시간을 지시하여 지속적인 서비스 제공과 규정 준수를 보장합니다. 자세한 내용은 [여기](https://support.freshservice.com/en/support/solutions/articles/50000004246-setting-up-ola-policies-for-tasks?utm_source=SLA_solutionarticle&utm_medium=SLA_solutionarticle&utm_campaign=SLA_solutionarticle)를 참조하세요.
:::