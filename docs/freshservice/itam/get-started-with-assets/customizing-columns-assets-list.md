---
sidebar_position: 7
---

# 자산 목록 페이지의 컬럼 사용자 정의

자산 페이지는 서비스 데스크의 모든 자산을 목록으로 표시합니다. 자산 목록 보기 페이지에서 다음 컬럼을 표시할 수 있습니다.

| 컬럼 이름 | 설명 |
|-----------|------|
| Asset Type | 자산의 카테고리 또는 분류 |
| Location | 자산의 물리적 또는 논리적 위치 |
| Used By | 자산을 활용하는 사람 또는 엔터티 |
| Department | 자산을 담당하는 조직 단위 |
| Managed By | 자산을 감독하는 개인 또는 그룹 |
| Asset Tag | 자산 추적을 위한 고유 식별자 |
| Impact | 자산이 운영에 미치는 영향 |
| End of Life | 자산이 쓸모없게 되거나 사용할 수 없게 되는 시점 |
| Discovery Enabled | 자산이 Discovery Probe 또는 Agent에 의해 자동으로 발견되도록 구성되었는지 여부를 나타냄 |
| Created by - Source | 자산을 생성한 소스를 지정합니다. 소스에는 Discovery Agent, Discovery Probe, SCCM Probe, Jamf, Chrome Connector, Cloud Discovery 앱, Workflows가 포함됩니다. |
| Created by - User | 자산을 생성한 사용자를 지정합니다. |
| Created Date | 자산 레코드가 처음 생성된 날짜와 시간 |
| Last updated by - Source | 자산을 마지막으로 업데이트한 소스를 지정합니다. 소스에는 Discovery Agent, Discovery Probe, SCCM Probe, Jamf, Chrome Connector, Cloud Discovery 앱, Workflows가 포함됩니다. |
| Last updated by - User | 자산을 업데이트한 사용자를 지정합니다. |
| Updated Date | 자산 레코드가 마지막으로 수정되거나 업데이트된 날짜와 시간 |
| Managed By Group | 자산 관리를 담당하는 그룹 |
| Source | 자산이 발견되고 추적된 소스<br /><br />예: Discovery Agent, Discovery Probe, Device 42, SCCM Probe |

## 컬럼 사용자 정의

컬럼 사용자 정의 도구를 사용하여 자산 목록에 표시되는 컬럼을 수정할 수 있습니다.

자산 목록에서 컬럼을 사용자 정의하는 방법은 다음과 같습니다:

1. 컬럼을 사용자 정의할 **보기**를 선택하고 **컬럼 사용자 정의 도구**를 클릭합니다. [보기 생성/수정 방법](https://support.freshservice.com/en/support/solutions/articles/223850)을 알아보려면 이 솔루션을 참조하세요.

2. 선택한 보기의 자산 유형에 따라 컬럼 사용자 정의 도구의 옵션도 변경됩니다.
   예를 들어, 모든 자산 보기에서는 모든 자산 유형에서 공통된 필드만 표시됩니다. 특정 자산 유형을 선택하면 해당 유형과 관련된 필드도 공통 필드와 함께 표시됩니다. 여기서 고려한 예에서는 선택된 자산 유형이 노트북이고 노트북 자산 유형과 관련된 필드가 표시됩니다.

   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008257335/original/6q1-yftEbJ9ND8R0EDF3v7qt_qPSZLyYuQ.gif?1683097391"  className="fr-dib" data-attachment="[object Object]" data-id="50008257335" alt="Customizing Columns in Assets list page" />

3. 필요한 필드를 선택합니다(최대 10개 필드까지 선택 가능). 컬럼을 재배열하려면 필드를 필요한 위치로 드래그 앤 드롭합니다.

4. **Apply**를 클릭하여 선택한 보기에 구성을 저장합니다.

   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008257342/original/Jdz-UAU1YjyoYSfnL3ium3hmEMrCVughZw.gif?1683097427"  className="fr-dib" data-attachment="[object Object]" data-id="50008257342" alt="Customizing Columns in Assets list page" />

:::info 중요 참고사항
컬럼 사용자 정의 도구는 계층 구조에서는 사용할 수 없으며 자산 보기에서만 사용할 수 있습니다. 컬럼을 사용자 정의하려면 기존 보기를 사용하거나 새 보기를 생성하여 컬럼 구성을 보기에 저장할 수 있도록 하세요.
:::