# 문제 관리 FAQ

문제 관리 운영에서 자주 발생하는 질문들과 실무에서 검증된 해결 방법을 정리했습니다.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<details>
<summary><strong>문제에 대한 필드를 설정할 수 있나요?</strong></summary>

**답변:** 네, 조직의 문제 관리 프로세스에 맞게 커스텀 필드를 추가하고 관리할 수 있습니다.

**설정 방법:**
1. **Admin** > **Service Management** > **Service Desk Settings** > **Field Manager**로 이동
2. **Form Fields** 페이지에서 **Problem fields** 모듈 클릭
3. 필요한 필드 유형을 드래그 앤 드롭으로 추가
   - 텍스트, 드롭다운, 체크박스, 날짜, 숫자 등
4. 필드별 세부 옵션 설정 (기본값, 드롭다운 선택지, 필수 여부)
5. **Save**로 설정 완료

**활용 예시:**
- **영향도 평가 필드**: 사용자 수, 비즈니스 크리티컬 여부
- **근본 원인 분석**: 원인 카테고리, 분석 담당자
- **예방 조치**: 향후 방지 대책, 모니터링 방법

</details>

<details>
<summary><strong>문제에 대한 템플릿이 있나요?</strong></summary>

**답변:** 현재 문제 관리에서는 템플릿 기능을 지원하지 않습니다.

**대안 방법:**
- **지식 베이스**: 문제 분석 가이드라인과 체크리스트를 문서화
- **커스텀 필드**: 표준화된 문제 분석 항목을 필드로 구성
- **자동화 규칙**: 문제 유형별 자동 정보 입력 설정
- **워크플로우**: 단계별 작업 가이드를 자동화로 구현

**실무 팁:** 자주 발생하는 문제 유형에 대해서는 지식 베이스에 표준 분석 절차를 문서화하여 일관된 문제 관리를 유지하세요.

</details>

<details>
<summary><strong>요청자에게 문제에 대한 접근 권한을 부여할 수 있나요?</strong></summary>

**답변:** 현재 요청자는 문제를 직접 볼 수는 없지만, 에이전트가 요청자를 대신하여 문제를 생성할 수 있습니다.

**현재 권한 구조:**
- **에이전트**: 문제 생성, 수정, 조회 가능
- **요청자**: 직접 접근 불가 (보안상 이유)
- **관련 인시던트**: 요청자는 연결된 인시던트를 통해 진행 상황 확인 가능

**실무 활용법:**
- 요청자 대신 문제 생성 후 관련 인시던트로 소통
- 문제 해결 진행 상황을 인시던트 댓글로 업데이트
- 근본 원인 분석 완료 시 요청자에게 결과 공유

**커뮤니케이션 팁:** 문제와 연결된 인시던트를 통해 요청자와 지속적으로 소통하며 투명성을 유지하세요.

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
