---
id: managing-sla-policy
title: Freshservice SLA 정책 관리
sidebar_label: Freshservice SLA 정책 관리
sidebar_position: 9
---

<div class="subtitle">
  이 문서는 "Freshservice SLA 정책 관리(Managing SLA Policy in Freshservice)" 기능의 설정, 구성, 최적화 방법을 안내하는 문서입니다.
</div>

Freshservice SLA (Service Level Agreement) 정책은 IT 서비스의 품질을 보장하고 고객 기대치를 관리하는 핵심 도구입니다. 올바른 SLA 정책 설정을 통해 티켓 처리 시간을 체계적으로 관리하고 서비스 품질을 향상시킬 수 있습니다.

## 개요

SLA 정책은 티켓의 우선순위에 따라 응답 및 해결 시간을 정의하고, 위반 시 자동 에스컬레이션을 통해 서비스 품질을 보장합니다. Freshservice는 기본 SLA 정책과 사용자 정의 다중 SLA 정책을 모두 지원합니다.

:::info SLA 정책의 핵심 구성 요소
- **Time-Priority Matrix**: 우선순위별 응답/해결 시간 정의
- **Trigger Conditions**: SLA 정책이 적용되는 조건 설정
- **Escalation Rules**: SLA 위반 시 자동 에스컬레이션 규칙
- **Business Hours Integration**: 업무 시간 또는 24시간 기준 계산
- **Multi-level Escalation**: 최대 4단계 해결 에스컬레이션 + 1단계 응답 에스컬레이션
:::

## SLA 정책 접근 경로

### 단일 워크스페이스 환경
**Admin > Service Management > Service Desk Settings > SLA and OLA Policies**

### 다중 워크스페이스 환경

#### 글로벌 SLA 정책 (모든 워크스페이스 적용)
**Admin > Global Settings > Service Management > Service Desk Settings > SLA and OLA Policies**

#### 워크스페이스별 SLA 정책
**Admin > Workspace Settings > &#123;워크스페이스명&#125; > Service Management > Service Desk Settings > SLA and OLA Policies**

:::warning SLA 정책 실행 순서
1. **워크스페이스별 SLA**: 특정 워크스페이스에 생성된 로컬 SLA 정책 우선 적용
2. **글로벌 SLA**: 로컬 조건에 맞지 않으면 글로벌 정책 적용
3. **기본 SLA**: 위 두 정책 모두 적용되지 않으면 기본 정책 적용
:::

## 기본 SLA 정책 설정

### 기본 정책 구성 단계

#### 1단계: 기본 SLA 정책 편집
1. SLA 정책 페이지에서 **Default SLA Policy** 찾기
2. **Edit** 버튼 클릭
3. 정책명 변경 및 설명 추가 (선택사항)

#### 2단계: Time-Priority Matrix 설정

우선순위별 목표 시간을 설정합니다:

<table>
<thead>
<tr>
<th style={{ width: '20%' }}>Priority Level</th>
<th style={{ width: '25%' }}>First Response</th>
<th style={{ width: '25%' }}>Resolution Time</th>
<th style={{ width: '30%' }}>권장 설정 예시</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Critical (긴급)</strong></td>
<td>15분</td>
<td>4시간</td>
<td>시스템 다운, 보안 사고</td>
</tr>
<tr>
<td><strong>High (높음)</strong></td>
<td>1시간</td>
<td>8시간</td>
<td>주요 기능 오류</td>
</tr>
<tr>
<td><strong>Medium (보통)</strong></td>
<td>4시간</td>
<td>24시간</td>
<td>일반적인 문제</td>
</tr>
<tr>
<td><strong>Low (낮음)</strong></td>
<td>8시간</td>
<td>72시간</td>
<td>개선 요청, 문의사항</td>
</tr>
</tbody>
</table>

#### 3단계: 시간 계산 기준 선택
- **Business Hours**: 설정된 업무 시간만 포함
- **Calendar Hours**: 24시간 기준 (주말, 휴일 포함)

#### 4단계: 에스컬레이션 설정
1. **Escalation Email** 토글을 On으로 설정
2. 에스컬레이션 계층 구조 정의:
   - **Response Escalation**: 1단계 (응답 시간 위반 시)
   - **Resolution Escalation**: 최대 4단계 (해결 시간 위반 시)

#### 5단계: 저장 및 활성화
**Save** 버튼을 클릭하여 설정 완료

## 다중 SLA 정책 생성

### 새 SLA 정책 생성 단계

#### 1단계: 새 정책 생성
1. SLA 정책 페이지에서 **New SLA Policy** 클릭
2. 정책명 및 설명 입력
3. Time-Priority Matrix 설정 (기본 정책과 동일 방식)

#### 2단계: 트리거 조건 정의

SLA 정책이 적용될 조건을 설정합니다:

##### 기본 조건 필드
- **Ticket Type**: Incident 또는 Service Request
- **Department**: 특정 부서
- **Agent Group**: 담당 에이전트 그룹
- **Requester Group**: 요청자 그룹
- **Priority**: 티켓 우선순위
- **Source**: 티켓 생성 경로 (Email, Portal, Phone 등)

##### 고급 조건 필드
- **Custom Fields**: 사용자 정의 필드 기반 조건
- **Service Category**: 서비스 카테고리
- **Service Item**: 특정 서비스 아이템
- **Location**: 요청자 위치
- **Customer**: 특정 고객 또는 회사

#### 3단계: 조건 매칭 방식 선택
- **Match All**: 모든 조건을 만족해야 함 (AND 조건)
- **Match Any**: 하나 이상의 조건을 만족하면 됨 (OR 조건)

### SLA 정책 우선순위 관리

#### 정책 순서의 중요성
여러 SLA 정책이 있을 때, **위에서부터** 조건을 확인하고 **첫 번째로 매칭되는 정책**을 적용합니다.

#### 모범 사례: 정책 순서 배치
```
1. 가장 구체적/제한적인 조건 (예: VIP 고객 + 긴급 우선순위)
2. 중간 수준 조건 (예: 특정 부서 + 높은 우선순위)
3. 일반적인 조건 (예: 특정 그룹)
4. 기본 SLA 정책 (가장 마지막)
```

#### 정책 재정렬
SLA 정책 목록에서 **드래그 앤 드롭**으로 순서 변경 가능

## 에스컬레이션 규칙 구성

### 에스컬레이션 유형

#### 응답 에스컬레이션 (Response Escalation)
- **1단계만 가능**
- 최초 응답 시간 초과 시 발동
- 지정된 에이전트/그룹에게 알림 발송

#### 해결 에스컬레이션 (Resolution Escalation)
- **최대 4단계 설정 가능**
- 해결 시간 접근/초과 시 단계별 발동
- 각 단계별 다른 담당자/그룹 지정 가능

### 에스컬레이션 설정 옵션

#### 시간 설정
- **Percentage-based**: SLA 시간의 특정 퍼센트 (예: 80%, 100%, 120%)
- **Fixed Time**: 고정 시간 (예: 2시간 후, 4시간 후)

#### 에스컬레이션 대상
- **Specific Agents**: 개별 에이전트 지정
- **Agent Groups**: 에이전트 그룹 지정
- **Managers**: 해당 그룹의 관리자
- **Custom Recipients**: 외부 이메일 주소

:::tip 에스컬레이션 설계 모범 사례
1. **점진적 확대**: 1차 → 팀리더 → 부서장 → 경영진 순으로 에스컬레이션
2. **적절한 간격**: 너무 짧거나 긴 간격보다는 적절한 시간 여유 제공
3. **명확한 책임**: 각 단계별 명확한 담당자 지정
4. **자동화 연계**: 워크플로우 자동화와 연계하여 추가 액션 수행
5. **모니터링**: 에스컬레이션 발생 빈도 및 패턴 정기 검토
:::

## 특수 SLA 정책 시나리오

### 고객 등급별 SLA

#### VIP 고객 SLA 예시
```
조건:
- Customer: VIP_Customers 그룹
- 모든 우선순위에 적용

시간 매트릭스:
- Critical: 5분 응답 / 2시간 해결
- High: 15분 응답 / 4시간 해결
- Medium: 30분 응답 / 8시간 해결
- Low: 1시간 응답 / 24시간 해결
```

#### 일반 고객 SLA 예시
```
조건:
- Customer: Standard_Customers 그룹

시간 매트릭스:
- Critical: 30분 응답 / 8시간 해결
- High: 2시간 응답 / 24시간 해결
- Medium: 8시간 응답 / 72시간 해결
- Low: 24시간 응답 / 120시간 해결
```

### 부서별 SLA

#### IT 인프라 팀 SLA
```
조건:
- Agent Group: Infrastructure Team
- Service Category: Infrastructure

특징:
- 24/7 Calendar Hours 적용
- 더 엄격한 응답/해결 시간
```

#### 일반 지원 팀 SLA
```
조건:
- Agent Group: General Support
- Service Category: General Support

특징:
- Business Hours 적용
- 표준 응답/해결 시간
```

### 서비스 유형별 SLA

#### 사고(Incident) 처리 SLA
```
조건:
- Ticket Type: Incident

특징:
- 빠른 응답/해결 시간
- 강화된 에스컬레이션
```

#### 서비스 요청(Service Request) SLA
```
조건:
- Ticket Type: Service Request

특징:
- 상대적으로 여유로운 시간
- 승인 프로세스 고려
```

## SLA 정책 복제 및 관리

### SLA 정책 복제

기존 정책을 기반으로 새 정책을 만들 때:

1. 복제할 정책 옆의 **Clone** 버튼 클릭
2. 자동으로 복제된 정책 생성 (이름에 "Copy" 접미사 추가)
3. 필요한 부분만 수정하여 시간 절약

### 정책 비활성화

일시적으로 정책을 중단하려면:
1. 해당 정책의 **Status** 토글을 Off로 변경
2. 비활성화된 정책은 적용되지 않음
3. 필요시 언제든 재활성화 가능

## SLA 타이머 제어

### SLA 타이머 일시정지

특정 상황에서 SLA 계산을 중단해야 할 때:

#### 설정 방법
1. **Admin > Field Manager > Ticket Fields > Status**로 이동
2. 새 커스텀 상태 생성
3. **SLA Timer** 옵션을 **Off**로 설정
4. 해당 상태로 티켓 변경 시 SLA 타이머 정지

#### 사용 시나리오
- **Pending Customer**: 고객 응답 대기 중
- **Pending Vendor**: 외부 업체 대응 대기 중
- **On Hold**: 기타 외부 요인으로 인한 대기

:::warning SLA 정책 제한사항
- **SLA 완전 비활성화 불가**: 특정 티켓에 대해 SLA를 완전히 끌 수는 없음
- **수동 Due By 설정**: 티켓의 Due By를 수동으로 설정하면 에스컬레이션 이메일이 발송되지 않음
- **Private Note**: 비공개 메모는 SLA 응답으로 간주되지 않음
:::

## SLA 성과 모니터링

### 주요 성과 지표 (KPI)

#### SLA 준수율
- **First Response Time Compliance**: 최초 응답 시간 준수율
- **Resolution Time Compliance**: 해결 시간 준수율
- **Overall SLA Achievement**: 전체 SLA 달성률

#### 에스컬레이션 분석
- **Escalation Frequency**: 에스컬레이션 발생 빈도
- **Escalation by Priority**: 우선순위별 에스컬레이션 패턴
- **Escalation Resolution Rate**: 에스컬레이션 후 해결률

### 보고서 및 대시보드

#### SLA 성과 리포트
- **SLA Trends**: 시간별 SLA 성과 추이
- **Agent Performance**: 에이전트별 SLA 준수 현황
- **Department Analysis**: 부서별 SLA 성과 비교

#### 실시간 모니터링
- **SLA Dashboard**: 실시간 SLA 현황 대시보드
- **Breach Alerts**: SLA 위반 임박 알림
- **Escalation Notifications**: 자동 에스컬레이션 알림

## 문제 해결 (Troubleshooting)

### 일반적인 문제와 해결책

#### SLA가 예상대로 적용되지 않는 경우
**문제**: 설정한 SLA 정책이 티켓에 적용되지 않음
**해결**:
1. 정책 순서 확인 (위에서부터 조건 매칭)
2. 트리거 조건 재검토
3. 정책 활성화 상태 확인
4. 워크스페이스별/글로벌 정책 우선순위 확인

#### 에스컬레이션 이메일이 발송되지 않는 경우
**문제**: SLA 위반 시 에스컬레이션 이메일이 오지 않음
**해결**:
1. 에스컬레이션 이메일 토글 확인
2. 이메일 주소 정확성 검증
3. 수동 Due By 설정 여부 확인
4. 이메일 서버 연결 상태 점검

#### SLA 시간 계산 오류
**문제**: Business Hours 설정이 제대로 반영되지 않음
**해결**:
1. Business Hours 설정 재확인
2. 휴일 설정 검토
3. 시간대(Timezone) 설정 확인
4. SLA 정책의 시간 기준 설정 재검토

### 성능 최적화

#### SLA 정책 최적화
- **정책 수 최소화**: 너무 많은 정책은 성능 저하 유발
- **조건 단순화**: 복잡한 조건보다는 단순하고 명확한 조건 사용
- **정기 검토**: 사용하지 않는 정책 정리

#### 에스컬레이션 최적화
- **적절한 간격**: 너무 짧은 에스컬레이션 간격 지양
- **담당자 확인**: 에스컬레이션 대상자의 가용성 확인
- **알림 조절**: 과도한 알림으로 인한 피로도 방지

## OLA (Operational Level Agreement) 연계

### OLA와 SLA의 차이점
- **SLA**: 고객과의 외부 약속 (External Agreement)
- **OLA**: 내부 팀 간의 운영 약속 (Internal Agreement)

### TPCR 태스크 OLA 설정
TPCR (Tickets, Problems, Changes, Releases) 내부 태스크에 대한 OLA 정책을 별도로 설정하여 내부 서비스 품질을 관리할 수 있습니다.

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [비즈니스 시간 설정](./configuring-business-hours)
- [워크플로우 자동화](./workflow-automation-setup)
- [에스컬레이션 관리](./escalation-management)
- [사용자 그룹 관리](./managing-user-groups)
- [시간대 설정](./time-zones-supported)
-->
