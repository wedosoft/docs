# 워크스페이스 (Workspaces)

워크스페이스 설정과 관리에서 자주 발생하는 실무 질문들을 정리했습니다. 총 18개의 FAQ를 포함하고 있습니다.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<details>
<summary><strong>IT 워크스페이스와 비즈니스 워크스페이스의 차이점은 무엇인가요?</strong></summary>

<div>

**워크스페이스 유형 결정:** IT 워크스페이스 템플릿으로 생성하면 IT 워크스페이스가 되고, HR, 시설, 법무, 재무 및 일반 템플릿으로 생성하면 비즈니스 워크스페이스가 됩니다. 빈 템플릿 사용 시에는 선택한 주요 비즈니스 기능에 따라 결정됩니다.

**주요 차이점:**

- **지원 티켓 유형:** IT 워크스페이스는 인시던트, 서비스 요청, 주요 인시던트를 지원하고, 비즈니스 워크스페이스는 케이스(쿼리/이슈/요청)를 지원합니다.

- **지원 기능:** IT 워크스페이스만 문제, 변경, 릴리스, 알림, 온콜 관리 등 IT 전용 기능에 접근할 수 있습니다.

- **에이전트 권한:** 비즈니스 에이전트는 IT 워크스페이스에서 '보기' 권한만 받을 수 있고, IT 및 비즈니스 에이전트 모두 비즈니스 워크스페이스에서 '관리' 권한을 받을 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스에서 에이전트 역할을 어떻게 관리하나요?</strong></summary>

<div>

**Admin** > **User Management** > **Agents**로 이동해서 에이전트를 선택하고 역할 설정을 편집하면 됩니다. 워크스페이스별로 서로 다른 역할을 할당할 수 있고, 전역 설정과 개별 워크스페이스 설정을 구분해서 관리할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 간에 티켓을 이동할 수 있나요?</strong></summary>

<div>

네, 적절한 권한을 가진 에이전트는 티켓을 다른 워크스페이스로 이동할 수 있습니다. 티켓 상세 페이지에서 워크스페이스 변경 옵션을 사용하면 됩니다.

</div>
</details>

<details>
<summary><strong>여러 워크스페이스를 생성할 수 있는 최대 개수는 얼마인가요?</strong></summary>

<div>

생성 가능한 워크스페이스 수는 구독 요금제에 따라 다릅니다. 정확한 제한 사항은 계정 설정에서 확인하거나 지원팀에 문의해 주세요.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 브랜딩을 설정할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 고유한 브랜딩을 설정할 수 있습니다. 로고, 색상, 이메일 템플릿 등을 워크스페이스별로 사용자 정의할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 삭제는 어떻게 하나요?</strong></summary>

<div>

워크스페이스를 삭제하려면 **Admin** > **Global Settings** > **Workspaces**로 이동하여 해당 워크스페이스를 선택하고 삭제 옵션을 사용할 수 있습니다. 단, 기본 워크스페이스는 삭제할 수 없습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 SLA 정책을 설정할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 고유한 SLA 정책을 설정할 수 있습니다. 이를 통해 부서별로 다른 서비스 수준을 제공할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 간에 데이터를 공유할 수 있나요?</strong></summary>

<div>

일부 데이터는 워크스페이스 간에 공유할 수 있습니다. 예를 들어, 에이전트, 요청자, 그룹 등은 여러 워크스페이스에서 공유될 수 있지만, 티켓, 자산 등은 각 워크스페이스에 고유합니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 도메인을 설정할 수 있나요?</strong></summary>

<div>

기본적으로 모든 워크스페이스는 동일한 도메인을 사용하지만, 엔터프라이즈 플랜에서는 워크스페이스별로 다른 서브도메인을 설정할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 템플릿의 종류는 무엇인가요?</strong></summary>

<div>

Freshservice에서 제공하는 워크스페이스 템플릿은 다음과 같습니다:
- IT 워크스페이스
- HR 워크스페이스
- 시설 관리 워크스페이스
- 법무 워크스페이스
- 재무 워크스페이스
- 일반 워크스페이스
- 빈 템플릿

각 템플릿은 해당 부서의 특정 요구사항에 맞는 사전 구성된 설정을 제공합니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 알림 설정을 할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 고유한 이메일 알림 설정을 구성할 수 있습니다. **Admin** > **Email Notifications**에서 워크스페이스별로 다른 알림 규칙을 설정할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스에서 자동화 규칙을 설정할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 고유한 워크플로 자동화 규칙을 설정할 수 있습니다. 이를 통해 부서별로 다른 비즈니스 프로세스를 자동화할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 사용자 정의 필드를 다르게 설정할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 다른 사용자 정의 필드를 설정할 수 있습니다. 이를 통해 부서별 특정 요구사항에 맞는 데이터를 수집할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 간에 보고서를 공유할 수 있나요?</strong></summary>

<div>

보고서는 일반적으로 각 워크스페이스에 고유하지만, 적절한 권한이 있는 사용자는 여러 워크스페이스의 데이터를 포함하는 교차 워크스페이스 보고서를 생성할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스 설정을 백업하고 복원할 수 있나요?</strong></summary>

<div>

현재 워크스페이스 설정의 직접적인 백업/복원 기능은 제공되지 않지만, 구성 내보내기/가져오기 기능을 통해 일부 설정을 다른 워크스페이스로 복사할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 언어 설정을 할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스마다 다른 기본 언어를 설정할 수 있습니다. 이는 다국가 조직에서 지역별로 다른 언어를 사용하는 경우 유용합니다.

</div>
</details>

<details>
<summary><strong>워크스페이스에서 에이전트 성과를 별도로 추적할 수 있나요?</strong></summary>

<div>

예, 각 워크스페이스별로 에이전트 성과 지표를 별도로 추적할 수 있습니다. 대시보드와 보고서를 통해 워크스페이스별 성과를 모니터링할 수 있습니다.

</div>
</details>

<details>
<summary><strong>워크스페이스별로 다른 인증 방법을 설정할 수 있나요?</strong></summary>

<div>

기본 인증 설정은 전역적으로 적용되지만, 엔터프라이즈 플랜에서는 워크스페이스별로 다른 SSO 구성을 설정할 수 있습니다.

</div>
</details>
