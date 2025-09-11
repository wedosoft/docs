# 문제 관리 (Problems)

Freshservice의 문제 관리 기능에 대한 자주 묻는 질문들입니다. 총 26개의 FAQ를 포함하고 있습니다.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<details>
<summary><strong>문제에 대한 필드를 설정할 수 있나요?</strong></summary>

<div>

예, Freshservice에서 문제에 대한 필드를 설정할 수 있습니다. 다음 단계를 따라하세요:

1. **Admin** > **Service Management** > **Service Desk Settings** > **Field Manager**로 이동합니다.

2. **Form Fields** 페이지에서 **Problem fields** 모듈을 클릭합니다.

3. 생성하려는 필드 유형(예: 텍스트, 드롭다운, 체크박스 등)을 드래그 앤 드롭합니다.

4. 선택한 필드 유형에 따라 필드를 정의하는 추가 옵션이 나타납니다(예: 기본값, 드롭다운 옵션 등).

5. **Save**를 클릭하여 필드를 저장합니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 템플릿이 있나요?</strong></summary>

<div>

아니요, 현재 문제에 대한 템플릿을 지원하지 않습니다.

</div>
</details>

<details>
<summary><strong>요청자에게 문제에 대한 액세스 권한을 부여할 수 있나요?</strong></summary>

<div>

요청자를 대신하여 문제 요청을 제기할 수 있지만 요청자는 해당 문제를 볼 수 없습니다.

</div>
</details>

<details>
<summary><strong>문제의 기존 상태에 새 상태를 추가할 수 있나요?</strong></summary>

<div>

예. **Admin** > **Form Fields** > **Problem**으로 이동하여 상태 필드를 클릭하면 다른 상태를 추가할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제의 기존 상태명을 변경할 수 있나요?</strong></summary>

<div>

기본 상태의 이름 변경은 허용하지 않지만 설정된 사용자 정의 상태에 대해서는 이 옵션을 사용할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대해 워크플로 자동화를 구성할 수 있나요?</strong></summary>

<div>

문제에 대해 특정 조건과 일치하는 이벤트에 기반하여 작업을 수행하도록 워크플로를 구성할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대해 동적 필드를 사용할 수 있나요?</strong></summary>

<div>

현재 문제에 대한 동적 필드를 지원하지 않습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 공개 URL을 지원하나요?</strong></summary>

<div>

문제에 대한 공개 URL을 지원하지 않습니다. 문제에 대한 범위를 가진 에이전트만 문제에 액세스할 수 있어야 합니다.

</div>
</details>

<details>
<summary><strong>문제에 노트가 추가될 때 알림을 제어할 수 있나요?</strong></summary>

<div>

현재 문제에 노트가 추가될 때 전송되는 알림을 제어할 수 없습니다.

</div>
</details>

<details>
<summary><strong>문제가 닫힐 때 요청자에게 전송되는 알림을 끌 수 있나요?</strong></summary>

<div>

Freshservice에서 문제가 닫힐 때 티켓의 요청자에게 전송되는 알림을 끌 수 있습니다.

이를 위해 **Admin** > **Email Notifications** > **Problem Notification** > **Problem Closed**로 이동하여 요청자에 대한 알림을 비활성화할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 첨부 파일을 추가할 수 있나요?</strong></summary>

<div>

예, 문제에 첨부 파일을 추가할 수 있습니다. 문제 생성 또는 편집 시 파일을 업로드할 수 있는 옵션이 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 우선순위를 설정할 수 있나요?</strong></summary>

<div>

예, 문제에 대한 우선순위를 설정할 수 있습니다. 기본적으로 낮음, 보통, 높음, 긴급의 우선순위 옵션이 제공됩니다.

</div>
</details>

<details>
<summary><strong>문제를 인시던트와 연결할 수 있나요?</strong></summary>

<div>

예, 문제를 하나 이상의 인시던트와 연결할 수 있습니다. 이를 통해 근본 원인을 추적하고 관련 인시던트들을 함께 관리할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 감시자를 추가할 수 있나요?</strong></summary>

<div>

예, 문제에 감시자를 추가할 수 있습니다. 감시자는 문제의 업데이트에 대한 알림을 받게 됩니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 태그를 추가할 수 있나요?</strong></summary>

<div>

예, 문제에 태그를 추가하여 분류하고 검색을 용이하게 할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 자동 할당 규칙을 설정할 수 있나요?</strong></summary>

<div>

예, 워크플로 자동화를 사용하여 특정 조건에 따라 문제를 자동으로 할당하는 규칙을 설정할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제 해결 시 관련 인시던트를 자동으로 닫을 수 있나요?</strong></summary>

<div>

예, 워크플로 자동화를 사용하여 문제가 해결될 때 관련된 인시던트들을 자동으로 닫도록 설정할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 사용자 정의 필드를 만들 수 있나요?</strong></summary>

<div>

예, **Admin** > **Form Fields** > **Problem**에서 사용자 정의 필드를 만들 수 있습니다. 텍스트, 숫자, 드롭다운, 체크박스 등 다양한 필드 유형을 지원합니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 승인 과정을 설정할 수 있나요?</strong></summary>

<div>

문제 관리에서는 별도의 승인 과정이 없습니다. 인시던트나 서비스 요청과 달리 문제는 일반적으로 내부 분석 및 해결 과정을 거칩니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 SLA를 설정할 수 있나요?</strong></summary>

<div>

SLA는 인시던트와 서비스 요청에만 적용됩니다. 문제에 대해서는 작업 마감일을 설정할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 변경 관리와의 연동이 가능한가요?</strong></summary>

<div>

예, 문제 해결을 위해 필요한 변경사항을 변경 관리 프로세스와 연동할 수 있습니다. 문제와 변경 요청을 연결하여 추적할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 근본 원인 분석을 기록할 수 있나요?</strong></summary>

<div>

예, 문제의 설명 필드나 사용자 정의 필드를 사용하여 근본 원인 분석 결과를 상세히 기록할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 팀 허들을 사용할 수 있나요?</strong></summary>

<div>

변경 티켓에 대해서는 팀 허들을 지원하지 않습니다. 문제 관리에서도 마찬가지로 팀 허들 기능을 사용할 수 없습니다.

</div>
</details>

<details>
<summary><strong>문제 생성 시 에이전트 알림을 활성화할 수 있나요?</strong></summary>

<div>

예, **Admin** > **Email Notification** > **Problem Notification** > **Incident Associated to Problem**에서 에이전트 알림을 활성화할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제와 연결된 인시던트에 대한 알림을 비활성화할 수 있나요?</strong></summary>

<div>

예, **Admin** > **Email Notification** > **Problem Notification** > **Incident Associated to Problem**에서 에이전트 알림을 비활성화할 수 있습니다.

</div>
</details>

<details>
<summary><strong>문제에 대한 Task 사용자 정의 상태를 지원하나요?</strong></summary>

<div>

현재 Task에 대한 사용자 정의 상태는 지원되지 않습니다.

</div>
</details>
