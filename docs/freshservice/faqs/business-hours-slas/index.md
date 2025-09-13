# 비즈니스 시간 및 SLA (Business Hours and SLAs)

Freshservice의 비즈니스 시간 및 SLA 설정에 대한 자주 묻는 질문들입니다.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<details>
<summary><strong>SLA가 왜 중요한가요?</strong></summary>

<div>

SLA(서비스 수준 계약)는 고객(요청자)과의 기대치를 설정하기 때문에 중요합니다. 요청자에게는 해결 시간의 예상치를 제공하여 실망할 가능성을 줄여주고, 요청을 처리하는 에이전트에게는 추적하고 해결 및 응답 시간을 개선하는 데 도움이 됩니다.

</div>
</details>

<details>
<summary><strong>어떤 필드에 SLA를 적용할 수 있나요?</strong></summary>

<div>

단락 및 콘텐츠 필드를 제외한 모든 티켓 필드를 기반으로 특정 SLA 정책이 언제 적용되어야 하는지 선택할 수 있습니다.

</div>
</details>

<details>
<summary><strong>어떤 플랜에서 여러 SLA를 추가할 수 있나요?</strong></summary>

<div>

Growth, Pro 및 Enterprise 플랜에서 여러 SLA 정책을 추가할 수 있습니다.

</div>
</details>

<details>
<summary><strong>자동화 규칙은 비즈니스 시간을 기준으로 실행되나요, 아니면 달력 시간을 기준으로 실행되나요?</strong></summary>

<div>

자동화 규칙은 비즈니스 시간 또는 달력 시간을 기준으로 실행되도록 구성할 수 있습니다.

</div>
</details>

<details>
<summary><strong>비즈니스 시간을 설정하는 방법은 무엇인가요?</strong></summary>

<div>

비즈니스 시간을 설정하려면:

1. **Admin** > **Account Settings** > **Business Hours**로 이동합니다.
2. 각 요일별로 운영 시간을 설정합니다.
3. 휴일 및 공휴일을 추가할 수 있습니다.
4. 시간대를 올바르게 설정했는지 확인합니다.

</div>
</details>

<details>
<summary><strong>SLA 정책에서 에스컬레이션을 설정할 수 있나요?</strong></summary>

<div>

예, SLA 정책에서 에스컬레이션을 설정할 수 있습니다. **Admin** > **Service Management** > **Service Desk Settings** > **SLA and OLA Policies**로 이동하여 에스컬레이션 규칙과 계층을 '마감일이 다가오거나 SLA가 위반될 때 발생하는 일' 섹션에서 추가할 수 있습니다.

</div>
</details>

<details>
<summary><strong>OLA(운영 수준 계약)와 SLA의 차이점은 무엇인가요?</strong></summary>

<div>

- **SLA(서비스 수준 계약)**: 고객과 서비스 제공업체 간의 약속으로, 고객에게 표시됩니다.
- **OLA(운영 수준 계약)**: 내부 팀 간의 약속으로, 내부 운영 목표를 설정하며 고객에게는 표시되지 않습니다.

</div>
</details>

<details>
<summary><strong>여러 시간대를 가진 조직에서 비즈니스 시간을 어떻게 관리하나요?</strong></summary>

<div>

여러 시간대를 가진 조직의 경우:

1. 각 지역별로 별도의 그룹을 생성합니다.
2. 각 그룹에 해당하는 비즈니스 시간을 설정합니다.
3. SLA 정책에서 그룹별로 다른 비즈니스 시간을 적용할 수 있습니다.

</div>
</details>

<details>
<summary><strong>SLA 위반 시 자동으로 알림을 보낼 수 있나요?</strong></summary>

<div>

예, SLA 정책 설정에서 에스컬레이션 규칙을 구성하여 SLA 위반 시 또는 마감일이 다가올 때 자동으로 특정 에이전트나 그룹에게 알림을 보낼 수 있습니다.

</div>
</details>

<details>
<summary><strong>휴일에 SLA 타이머가 일시 중지되나요?</strong></summary>

<div>

예, 비즈니스 시간 설정에서 휴일을 구성하면 해당 날짜에는 SLA 타이머가 일시 중지됩니다. 이는 비즈니스 시간 기반 SLA에만 적용되며, 24시간 기반 SLA는 계속 진행됩니다.

</div>
</details>
