---
sidebar_position: 5
---

# 자산 대량 업데이트

자산 관리자는 종종 자산 그룹의 속성을 업데이트해야 합니다. 이러한 자산을 하나씩 업데이트하는 것은 특히 업데이트할 자산이 몇 개 이상인 경우 지루할 수 있습니다. Freshservice에서는 **대량 업데이트** 옵션을 사용하여 하나 이상의 자산 속성을 대량으로 업데이트할 수 있습니다.

이 솔루션은 다음을 다룹니다:

- [대량 업데이트 기본사항](#bulk-update-basics)
- [필드 값 지우기](#clearing-the-values-in-fields)
- [대량으로 업데이트할 수 있는 속성](#properties-that-can-be-updated-in-bulk)
- [대량 업데이트에서 사용 가능한 필드](#fields-available-in-bulk-update)
- [대량 업데이트에서 자산 유형 변경](#changing-the-asset-type-in-bulk-update)

### 대량 업데이트 기본사항 {#bulk-update-basics}

업데이트하려는 자산을 선택하고 대량 업데이트 옵션을 클릭할 수 있습니다. Freshservice에서 자산을 대량 업데이트하려면 다음 단계를 따르세요:

1. **Assets**로 이동하여 **Inventory**를 클릭합니다.
2. 업데이트하려는 자산을 선택합니다.
3. **Bulk Update**를 클릭하여 팝업 창을 엽니다.
4. 팝업 창에는 선택한 자산에 대해 업데이트할 수 있는 모든 필드가 나열됩니다.
5. 특정 필드의 값을 선택하면 업데이트 표시됩니다.
6. **Update**를 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008256289/original/uJkPB6MNebKA3X0fR0WhydLb_-qEfBJG2Q.gif?1683091033"  className="fr-dib" data-attachment="[object Object]" data-id="50008256289" alt="Updating Assets in Bulk" />

### 필드 값 지우기 {#clearing-the-values-in-fields}

Freshservice의 대량 업데이트 기능을 사용하여 여러 자산의 특정 필드 값을 지우려면 다음 단계를 따르세요:

1. **Assets**로 이동하여 **Inventory**를 클릭합니다.
2. 업데이트하려는 자산을 선택합니다.
3. **Bulk Update**를 클릭하여 팝업 창을 엽니다.
4. 나타나는 팝업 창에서 지우려는 필드의 체크박스를 선택하되 값은 선택하지 마세요.
5. **Update**를 클릭하여 선택한 모든 자산에 변경 사항을 적용합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008256292/original/ecrM6nW19GL4GUVnK6111FonlA492fEJcA.gif?1683091077"  className="fr-dib" data-attachment="[object Object]" data-id="50008256292" alt="Clearing values using Bulk Update" />

예를 들어, 선택한 모든 자산의 Company 필드를 지우려면 Company 체크박스를 선택하되 값은 선택하지 마세요. Update를 클릭하면 선택한 모든 자산의 Company 필드가 지워집니다.

자산에 대해 어떤 필드가 업데이트되었는지 알려면 해당 자산을 클릭하고 자산 활동으로 이동하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011179226/original/75jCdLbIUuSZCj5NOx8yQ5fB8qR5angzxg.png?1710081141"  className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011179226" />

### 대량으로 업데이트할 수 있는 속성 {#properties-that-can-be-updated-in-bulk}

대량 업데이트 팝업에서 업데이트할 수 있는 필드는 선택한 보기를 기반으로 합니다. 예를 들어, All Assets 보기(기본값)에서는 Location, Department, Asset Type과 같은 공통 필드만 편집할 수 있습니다.

자산 목록이 자산 유형을 기반으로 필터링되면 해당 자산 유형과 관련된 필드가 표시됩니다. 예를 들어, 목록이 Hardware와 같은 자산 유형으로 필터링되면 Hardware 속성도 업데이트할 수 있습니다.

### 대량 업데이트에서 사용 가능한 필드 {#fields-available-in-bulk-update}

다음 필드 유형이 대량 업데이트에서 사용 가능합니다. 다음 유형의 사용자 정의 필드도 대량으로 업데이트할 수 있습니다.

- 드롭다운 필드
- 중첩 필드
- 날짜 필드

### 대량 업데이트에서 자산 유형 변경 {#changing-the-asset-type-in-bulk-update}

대량 업데이트를 사용하여 여러 자산의 자산 유형을 변경할 수도 있습니다. 그러나 여러 자산의 자산 유형을 변경하면 일부 자산 필드에서 정보가 손실될 수 있습니다.

- 대량 업데이트 팝업에서 새 자산 유형을 선택하면 일부 필드 데이터가 손실될 수 있다는 확인 메시지가 표시됩니다
- 그러면 대량 업데이트 양식이 재설정되고 선택한 새 자산 유형과 관련된 모든 필드가 표시됩니다
- 선택한 새 자산 유형에는 일부 필드가 필수일 수 있습니다. 예를 들어, Desktop 자산 유형을 선택하면 Product, Vendor, Asset State 필드가 필수가 됩니다. 이러한 필드는 기본적으로 선택되며 이러한 값을 업데이트해야만 대량 업데이트를 완료할 수 있습니다
- 이전 자산 유형과 새 자산 유형 간에 공통 속성이 있는 경우 선택한 각 자산에 대해 이러한 속성이 유지됩니다. 예를 들어, 자산 유형이 수정되었기 때문에 used by, location, department 등은 덮어쓰지 않습니다.

**FAQ**

**1. 자산 유형을 삭제하려고 하는데 해당 유형에 할당된 모든 자산을 먼저 제거해야 한다는 안내를 받은 경우 어떻게 해야 하나요?**

이 특정 자산 유형과 연결된 모든 자산을 제거해야 합니다. 때로는 해당 자산이 휴지통에 있는 경우에도 여전히 이 문제가 발생할 수 있습니다.

휴지통에서 삭제하려면 왼쪽 상단 모서리의 자산 인벤토리에서 3개 선을 클릭하고 목록에서 **Trash**를 클릭하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011417739/original/Yf7mbq5MSXTD8uSGLOhrhMRbXfHhZEMI1Q.png?1712060870"  className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011417739" />

**2. 자산의 관리 그룹을 대량으로 업데이트하는 방법은?**

Admin 섹션으로 이동한 다음 Workflow Automator를 선택하고 Scheduled Workflow를 클릭합니다. 거기서 New Workflow를 선택하고 모듈을 assets으로 설정합니다. 특정 사용 사례에 따라 이벤트와 조건을 정의합니다. 다음으로 아래 제공된 이미지에 따라 액션 노드를 구성하고 관련 그룹에 할당합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012122549/original/OPvQx8R-AGWKn3svRrv-35oskIsQkOYa2Q.png?1718114281"  className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50012122549" />