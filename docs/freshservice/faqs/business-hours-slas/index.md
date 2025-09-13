# 비즈니스 시간 및 SLA

비즈니스 시간과 SLA 설정에서 자주 발생하는 질문들과 실무에서 검증된 해결 방법을 정리했습니다.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<details>
<summary><strong>SLA가 왜 중요한가요?</strong></summary>

**답변:** SLA(서비스 수준 계약)는 고객과의 기대치를 명확하게 설정하는 핵심 도구입니다. 요청자에게는 해결 시간의 명확한 기준을 제공하여 불필요한 문의를 줄이고, 에이전트에게는 응답 및 해결 시간을 체계적으로 관리할 수 있는 기준을 제공합니다.

**실무 팁:** 현실적이고 달성 가능한 SLA를 설정하여 팀의 부담을 줄이면서도 고객 만족도를 높일 수 있습니다.

</details>

<details>
<summary><strong>어떤 필드에 SLA를 적용할 수 있나요?</strong></summary>

**답변:** 단락 및 콘텐츠 필드를 제외한 모든 티켓 필드를 기반으로 SLA 정책 적용 조건을 설정할 수 있습니다.

**활용 예시:**
- 우선순위별 SLA 설정 (긴급, 높음, 보통, 낮음)
- 카테고리별 SLA 설정 (하드웨어, 소프트웨어, 액세스 권한)
- 그룹별 SLA 설정 (IT팀, HR팀, 영업팀)
- 요청자 유형별 SLA 설정 (VIP 고객, 일반 사용자)

</details>

<details>
<summary><strong>어떤 플랜에서 여러 SLA를 추가할 수 있나요?</strong></summary>

**답변:** Growth, Pro, Enterprise 플랜에서 여러 SLA 정책을 추가할 수 있습니다.

**참고:** Starter 플랜은 기본 SLA 정책 하나만 지원되므로, 복잡한 SLA 운영이 필요한 경우 플랜 업그레이드를 고려해보세요.

</details>

<details>
<summary><strong>자동화 규칙은 비즈니스 시간을 기준으로 실행되나요?</strong></summary>

**답변:** 자동화 규칙은 설정에 따라 비즈니스 시간 또는 달력 시간(24시간) 기준으로 실행할 수 있습니다.

**설정 방법:**
1. **Admin** > **Workflow Automator** > **Automations**로 이동
2. 규칙 생성 시 조건에서 **Business Hours** 또는 **Calendar Hours** 선택
3. 비즈니스 시간 선택 시 휴일과 주말은 자동으로 제외됩니다

**권장사항:** 긴급하지 않은 알림이나 작업은 비즈니스 시간으로, 즉시 처리가 필요한 작업은 달력 시간으로 설정하세요.

</details>

<details>
<summary><strong>비즈니스 시간을 설정하는 방법은 무엇인가요?</strong></summary>

**단계별 설정:**
1. **Admin** > **Account Settings** > **Business Hours**로 이동
2. 각 요일별로 운영 시간 설정
3. 점심시간이나 브레이크 타임도 세부적으로 설정 가능
4. 휴일 및 공휴일 추가
5. 시간대(Timezone) 정확히 설정

**실무 팁:**
- 여러 지역 운영 시 각 지역별로 별도 비즈니스 시간 생성
- 24/7 운영팀은 별도 비즈니스 시간 그룹으로 분리 관리
- 휴일 캘린더는 매년 초 미리 업데이트해두기

</details>

<details>
<summary><strong>SLA 정책에서 에스컬레이션을 설정할 수 있나요?</strong></summary>

**답변:** 네, SLA 에스컬레이션을 통해 지연 상황을 체계적으로 관리할 수 있습니다.

**설정 경로:**
1. **Admin** > **Service Management** > **Service Desk Settings** > **SLA and OLA Policies**
2. SLA 정책 편집 또는 신규 생성
3. **What happens when the deadline approaches or SLA is violated** 섹션에서 에스컬레이션 규칙 추가

**에스컬레이션 옵션:**
- 특정 시간 전 담당자에게 알림
- SLA 위반 시 상위 관리자에게 자동 할당
- 여러 단계의 에스컬레이션 체인 설정
- 이메일, 슬랙 등 다양한 알림 채널 활용

</details>

<details>
<summary><strong>OLA와 SLA의 차이점은 무엇인가요?</strong></summary>

**주요 차이점:**

| 구분 | SLA (Service Level Agreement) | OLA (Operational Level Agreement) |
|------|-------------------------------|-----------------------------------|
| **대상** | 고객과 서비스 제공업체 간 약속 | 내부 팀 간 약속 |
| **표시** | 고객에게 공개적으로 표시 | 내부 운영 목적으로만 사용 |
| **목적** | 고객 기대치 관리 | 내부 프로세스 효율성 향상 |
| **측정** | 고객 만족도 중심 | 운영 효율성 중심 |

**실무 활용:**
- **SLA**: 고객 응답 시간, 해결 시간 등
- **OLA**: 팀 간 업무 인계 시간, 내부 승인 프로세스 등

</details>

<details>
<summary><strong>여러 시간대를 가진 조직에서 비즈니스 시간을 어떻게 관리하나요?</strong></summary>

**다중 시간대 관리 전략:**

1. **지역별 그룹 생성**
   - 각 지역별로 별도의 에이전트 그룹 생성
   - 지역명을 포함한 명확한 그룹명 사용 (예: IT_Seoul, IT_Tokyo)

2. **지역별 비즈니스 시간 설정**
   - **Admin** > **Account Settings** > **Business Hours**에서 지역별 생성
   - 각 지역의 로컬 휴일과 근무 문화 반영

3. **SLA 정책 차별화**
   - 그룹별로 다른 비즈니스 시간 적용
   - 시간대별 우선순위 조정 고려

**실무 팁:**
- Follow the Sun 모델로 24시간 지원 체계 구축
- 지역 간 업무 인계 프로세스 표준화
- 각 지역의 문화적 특성을 고려한 SLA 설계

</details>

<details>
<summary><strong>SLA 위반 시 자동으로 알림을 보낼 수 있나요?</strong></summary>

**답변:** 네, SLA 에스컬레이션 기능으로 다양한 상황에서 자동 알림을 설정할 수 있습니다.

**알림 설정 방법:**
1. SLA 정책 설정에서 **Escalation Rules** 구성
2. 알림 시점 설정 (예: 마감 2시간 전, 위반 즉시)
3. 수신자 지정 (담당자, 상위 관리자, 특정 그룹)
4. 알림 채널 선택 (이메일, 인앱 알림, 슬랙 등)

**실용적인 알림 시나리오:**
- **1차 알림**: SLA 마감 4시간 전 → 담당 에이전트
- **2차 알림**: SLA 마감 1시간 전 → 담당자 + 팀 리더
- **3차 알림**: SLA 위반 시 → 모든 관련자 + 상급 관리자

**주의사항:** 너무 빈번한 알림은 피로감을 유발하므로 적절한 빈도로 설정하세요.

</details>

<details>
<summary><strong>휴일에 SLA 타이머가 일시 중지되나요?</strong></summary>

**답변:** 비즈니스 시간 기반 SLA는 휴일에 자동으로 일시 중지되지만, 24시간 기반 SLA는 계속 진행됩니다.

**SLA 타입별 동작:**

| SLA 유형 | 휴일 동작 | 활용 시나리오 |
|----------|-----------|---------------|
| **Business Hours SLA** | 타이머 일시중지 | 일반적인 업무 요청 |
| **Calendar Hours SLA** | 타이머 계속 진행 | 긴급 장애 대응 |

**설정 확인 방법:**
1. **Admin** > **Account Settings** > **Business Hours**
2. 휴일 캘린더 등록 여부 확인
3. SLA 정책에서 Business Hours 기반으로 설정되었는지 확인

**실무 권장사항:**
- 긴급도가 높은 시스템 장애: 24시간 기반 SLA
- 일반적인 사용자 요청: 비즈니스 시간 기반 SLA
- 중요도에 따른 혼합 운영으로 효율성 극대화

</details>
