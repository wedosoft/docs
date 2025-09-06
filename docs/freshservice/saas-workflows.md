---
sidebar_position: 5
---

# SaaS 액션 자동화를 위한 워크플로우 설정

오케스트레이션 앱을 사용하여 워크플로우를 생성함으로써 상담원의 개입 없이 SaaS 애플리케이션에서 작업을 자동화할 수 있습니다. 자동화를 통해 선택한 작업을 트리거하여 애플리케이션에 즉시 영향을 미칠 수 있습니다.

## 사용 사례 - Zoom을 위한 SaaS 액션 자동화

![Zoom 자동화 예시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438587/original/PqB2kS3OH-obdyhAHNbxPJLyL5qOT-U9Ow.png?1612778188)

### 워크플로우 자동화 도구 접근

**기본 경로**: **관리자 → 자동화 & 생산성 → 자동화 → 워크플로우 자동화 도구**로 이동합니다.

#### 멀티 워크스페이스 환경인 경우:

:::info 워크스페이스별 설정
- **글로벌 워크플로우 수정**: **관리자 → 글로벌 설정 → 자동화 & 생산성 → 자동화 → 워크플로우 자동화 도구**
- **워크스페이스별 워크플로우 수정**: **관리자 → 워크스페이스 설정 → [워크스페이스 이름] → 자동화 & 생산성 → 자동화 → 워크플로우 자동화 도구**
:::

#### 중요 사항

:::warning 워크플로우 실행 순서
**워크스페이스 관리자**는 해당 워크스페이스에 적용되는 글로벌 및 로컬 워크플로우 목록을 볼 수 있습니다. 

**실행 순서**:
1. **글로벌 워크플로우**가 먼저 실행
2. **워크스페이스 레벨 워크플로우**가 다음에 실행

이를 통해 워크스페이스 레벨 워크플로우가 글로벌 워크플로우보다 우선적으로 적용됩니다.

**예시**: 글로벌 워크플로우에서 제목/설명을 기반으로 티켓을 적절한 워크스페이스로 라우팅하도록 구성할 수 있습니다.
:::

## 워크플로우 설정 단계

### 1단계: 새 자동화 도구 생성

**티켓용 새 자동화 도구를 생성**합니다.

![워크플로우 생성](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438618/original/NvGCPSVquxDlxxa93IpRV8Ynjd0-5WAA9A.png?1612778318)

### 2단계: 이벤트 설정

**서비스 요청이 제기될 때** 워크플로우를 트리거하는 이벤트를 생성합니다.

## 시나리오 1: 사용량 부족 알림

### 조건 설정

**사용량 부족에 대해 사용자에게 알리기 위해** 제기되는 SaaS 액션 서비스 요청에 대한 액션을 트리거하는 조건을 생성합니다.

![사용량 부족 알림 조건](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438639/original/3MRZTrescnAdX_FTjDc2h9925Xp3hXWVEg.png?1612778473)

![조건 상세 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438627/original/ssyDZQ5Blg_Mo-qXU39JC08OvP4R5uFoCg.png?1612778435)

### 액션 설정

요청자에게 **사용량 부족에 대한 이메일**을 트리거하는 액션을 생성합니다.

![이메일 액션 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438638/original/ClWATT1uUCsS4bznOlB5Wv-tiRs6nEPVUw.png?1612778472)

## 시나리오 2: 플랜 업그레이드

### 업그레이드 조건 설정

**Zoom을 Pro 플랜으로 업그레이드**하기 위해 제기되는 SaaS 액션 서비스 요청에 대한 액션을 트리거하는 조건을 생성합니다.

![플랜 업그레이드 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438641/original/Mw1xhsO9AGdvNKkqir-bdpcrHFHklTcpfA.png?1612778500)

![업그레이드 조건](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438643/original/vjE1-tQJMBcIeiwhRV-urLwdosp2RobtWQ.png?1612778532)

### 앱 액션 노드 생성

**Zoom 오케스트레이션 앱**을 사용하여 사용자의 플랜을 업데이트하는 앱 액션 노드를 생성합니다.

![Zoom 앱 액션](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002438662/original/QvsrHqRSmWYzdZNrHu2O10Ec-b2UXZzapQ.png?1612778664)

## 워크플로우 구성 모범 사례

### 이벤트 트리거 설정

:::tip 효과적인 트리거 설정
1. **명확한 이벤트 정의**: 워크플로우를 트리거할 정확한 조건을 명시하세요
2. **우선순위 고려**: 글로벌 vs 워크스페이스 레벨 워크플로우의 실행 순서를 고려하세요
3. **중복 방지**: 유사한 워크플로우가 중복 실행되지 않도록 조건을 세밀하게 설정하세요
:::

### 조건 설정 지침

1. **구체적인 조건**: 너무 광범위한 조건보다는 구체적인 조건을 설정하여 정확한 액션을 트리거하세요
2. **테스트 가능한 조건**: 설정한 조건이 실제로 예상대로 작동하는지 테스트할 수 있도록 구성하세요
3. **에러 핸들링**: 조건이 충족되지 않을 경우의 대체 액션도 고려하세요

### 액션 설정 최적화

:::info 액션 설정 팁
- **단계별 접근**: 복잡한 액션은 여러 단계로 나누어 설정하세요
- **로깅 활용**: 액션 실행 결과를 추적할 수 있도록 로깅을 설정하세요
- **알림 설정**: 중요한 액션 완료 시 관련 담당자에게 알림을 보내도록 설정하세요
:::

## 자동화 효과

### 즉시 처리

- **수동 개입 제거**: 상담원이 직접 처리할 필요 없이 자동으로 액션이 실행됩니다
- **일관된 처리**: 매번 동일한 기준과 절차로 요청이 처리됩니다
- **24/7 대응**: 업무 시간에 관계없이 자동으로 요청이 처리됩니다

### 효율성 향상

- **응답 시간 단축**: 즉시 자동 처리로 사용자 대기 시간이 단축됩니다
- **리소스 절약**: 반복적인 작업의 자동화로 상담원이 더 중요한 업무에 집중할 수 있습니다
- **오류 감소**: 수동 처리에서 발생할 수 있는 인적 오류를 방지합니다

:::success 성공적인 자동화를 위한 핵심
SaaS 액션 자동화를 통해 조직의 생산성을 크게 향상시킬 수 있습니다. 명확한 조건 설정과 체계적인 액션 구성을 통해 안정적이고 효율적인 자동화 시스템을 구축하세요.
:::
