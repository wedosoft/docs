---
sidebar_position: 3
---

# 특정 부서 및 그룹을 위한 다중 SLA 정책 생성하기

Freshservice에서 사용하는 특정 부서나 그룹을 기반으로 티켓에 다른 SLA 정책을 적용하여 서비스 데스크에서 여러 SLA 정책을 생성할 수 있습니다. 예를 들어, 특정 고객이나 특정 부서와 관련된 티켓에 대해 다른 SLA 정책을 가질 수 있습니다.

:::info 중요 사항
**워크스페이스 관리자는 워크스페이스 수준에서 SLA 정책을 생성할 수 있습니다.**

1. 워크스페이스 관리자는 워크스페이스 수준에서 SLA 정책을 생성할 수 있습니다
2. 글로벌 SLA 정책은 모든 워크스페이스의 티켓에 적용됩니다
3. 기본 SLA 정책은 글로벌 수준에서 기본적으로 생성되고 활성화됩니다

**실행 순서:** 티켓의 SLA 정책은 특정 워크스페이스용으로 생성된 로컬 SLA 정책에 의해 결정됩니다. 로컬 SLA 정책의 지정된 조건이 일치하지 않으면 글로벌 정책을 따릅니다. 두 정책 모두 적용되지 않으면 기본 SLA 정책이 티켓에 적용됩니다.
:::

## 다중 SLA 구성을 위한 빠른 가이드

### 1단계: SLA 정책 설정 페이지 접근

**Admin > Service Management > Service Desk Settings > SLA and OLA Policies**로 이동합니다.

**계정에 워크스페이스가 여러 개 있는 경우:**
- 글로벌 워크플로우 수정: **Admin > Global Settings > Service Management > Service Desk Settings > SLA and OLA Policies**
- 워크스페이스 수준 워크플로우 수정: **Admin > Workspace Settings > &#123;Workspace Name&#125; > Service Management > Service Desk Settings > SLA and OLA Policies**

### 2단계: 새 SLA 정책 생성

1. **New SLA Policy**를 클릭합니다
2. 각 티켓 우선순위에 대한 SLA 목표를 선택합니다
3. 트리거 조건을 선택합니다 (이 규칙이 언제 적용되어야 하는지)
4. 최대 3단계의 에스컬레이션 계층구조를 입력합니다
5. 정책을 **저장**합니다
6. 가장 제한적인 규칙이 먼저 오도록 정책을 재정렬합니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006967183/original/4FNH0pwMklYLITXu0P0tr8S7jtSXB9gmhw.png?1669028084"  />

### 3단계: SLA 정책 설정

새 SLA 정책을 적용하려면 SLA 정책 페이지에서 New SLA Policy 버튼을 클릭합니다. 기본 SLA 정책과 마찬가지로 각 티켓 우선순위에 대한 SLA 목표를 정의해야 합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011603315/original/qf6ZUf4ruQjpjE3_CUslrGWK5sHfQeT1Ug.png?1713719555"  />

다음으로 트리거 조건을 선택하여 이 SLA가 언제 활성화될지 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000085288/original/Y9ROGyfj6t73RymXT5VbkSYO855v-feBwg.png?1565264195"  />

## 트리거 조건 정의

각 SLA 정책에 대해 최소 하나의 트리거 조건을 정의해야 합니다.

사용자 정의 필드를 기반으로 다양한 SLA 조건을 정의할 수 있습니다. 이를 통해 사용자는 모든 티켓 필드를 기반으로 여러 SLA를 설정할 수 있는 유연성을 얻습니다. 여러 트리거 조건을 설정하고 SLA를 트리거하기 위해 해당 조건 중 모든 조건 또는 일부 조건을 일치시킬지 선택할 수 있습니다.

인시던트와 서비스 요청에 대해 다른 SLA를 설정할 수도 있습니다. 서비스 요청의 경우 서비스 항목 및 서비스 카테고리를 기반으로 여러 하위 조건을 추가하고 SLA가 트리거되도록 해당 조건 중 모든 조건 또는 일부 조건을 일치시킬지 선택할 수도 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003199901/original/h0NDpa73wNWlQq7umYj4x7HsKTHLXpNuTQ.png?1623846113"  />

## SLA 정책 순서의 중요성

기억하세요 - SLA 정책의 순서가 중요합니다. 여러 SLA 정책이 있는 경우 일치하는 조건이 있는 첫 번째 정책이 티켓에 적용됩니다.

예를 들어, 특정 고객 A의 티켓에 대한 특별 SLA 정책(SLA 1)과 그룹 X에 할당된 티켓에 대한 다른 정책(SLA 2)이 있고 SLA 1이 맨 위에, SLA 2가 두 번째로 정렬되어 있다고 가정합시다. 고객 A의 티켓이 그룹 X에 할당되면 SLA 1의 규칙(맨 위에 있음)과 일치하므로 SLA 1이 적용됩니다.

가장 제한적인(엄격한) 규칙이 순서에서 더 높게 위치하도록 SLA 규칙을 재정렬하고 구성할 수 있습니다.

## 에스컬레이션 규칙 정의

사용자 정의 SLA를 생성할 때 에스컬레이션 규칙도 설정할 수 있습니다. 예를 들어, 특정 시간 간격 동안 티켓이 해결되지 않았을 때 티켓을 누구에게 에스컬레이션할지 선택할 수 있습니다.

티켓 해결을 위해 최대 4단계의 에스컬레이션과 티켓 응답을 위해 1단계를 설정할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000087587/original/JnI3MVNyne8hMuHYmf1QNoBOnrB-jCvgZw.png?1565328873"  />

:::warning 참고사항
티켓에서 마감일이 수동으로 설정된 경우 에스컬레이션 이메일이 전송되지 않습니다.
:::

## SLA 복제

SLA 정책을 복제할 수도 있습니다:

1. **Admin > Service Management > Service Desk Settings > SLA and OLA Policies**로 이동합니다
2. SLA 정책(예: 네트워크 팀용 SLA) 옆의 **Clone** 옵션을 클릭하면 해당 정책이 즉시 복제됩니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011603317/original/GgMZOBwZSr3DCHWJF-AwuJqIdf0nO0LoSg.png?1713719628"  />

## 자주 묻는 질문

### 1. 특정 티켓에 대해 SLA를 비활성화하는 방법은?

SLA는 티켓이 생성될 때부터 종료될 때까지 계산되므로 비활성화할 수 없습니다. 대신 필요에 따라 티켓에서 SLA 타이머를 일시 중지할 수 있습니다. 이를 위해서는 **Admin > Field Manager > Ticket Fields > Status**에서 사용자 정의 상태를 구성한 다음 SLA 타이머를 끄고 티켓에서 해당 상태를 설정해야 합니다.

:::warning 참고사항
관리자는 이제 **티켓/문제/변경 및 릴리스(TPCR) 작업**에 대해 내부 **운영 수준 계약(OLA)**을 정의할 수 있습니다. 이는 상담원이 **TPCR 내부의 작업**을 완료해야 하는 시간을 지시하여 지속적인 서비스 제공과 규정 준수를 보장합니다. 자세한 내용은 [여기](https://support.freshservice.com/en/support/solutions/articles/50000004246-setting-up-ola-policies-for-tasks?utm_source=SLA_solutionarticle&utm_medium=SLA_solutionarticle&utm_campaign=SLA_solutionarticle)를 참조하세요.
:::