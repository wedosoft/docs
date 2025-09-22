---
sidebar_position: 4
---

# 티켓 속성 관리하기

티켓 작업 중에도 상태를 변경하거나, 다른 카테고리로 재분류하거나, 팀의 다른 담당자에게 할당하는 등 일반적으로 속성을 업데이트하고 싶을 수 있습니다. "티켓 속성" 옵션을 사용하면 사이드바에서 티켓과 연관된 모든 필드를 수정하고 업데이트할 수 있습니다.

티켓 필드 외에도 SLA 정책에 따라 자동으로 설정되는 티켓의 마감 시간(Due By time)을 클릭하여 수정할 수 있습니다.

## 티켓 속성 관리 가이드

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006668145/original/mx7TRAjSIeQgOMK8RNqs6m5o7e4l2Maivg.png?1665993350" style={{width: '325px'}} className="fr-fic fr-dib fr-bordered" data-attachment="[object Object]" data-id="50006668145" />

1. **티켓 열기**
   - 대시보드나 티켓 목록에서 원하는 티켓을 클릭하여 세부 정보를 확인합니다

2. **티켓 속성 섹션으로 이동**
   - 오른쪽 메뉴의 **Ticket Properties** 섹션으로 이동합니다

3. **속성 편집**
   - 드롭다운 박스를 사용하여 우선순위, 상태 및 티켓 속성 목록의 기타 필드를 선택하고 편집합니다

4. **업데이트 완료**
   - 작업이 완료되면 **Update** 버튼을 클릭합니다

## 티켓 마감 시간 수동 변경 가이드

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009280159/original/Ds45jTOHkmq3UJ8bV2qgr9uoUWnYnXAhdA.png?1692962313" style={{width: '361px'}} className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50009280159" />

1. **티켓 열기**
   - 대시보드나 티켓 목록에서 원하는 티켓을 클릭하여 세부 정보를 확인합니다

2. **현재 마감일 확인**
   - 화면 오른쪽 상단에 현재 첫 응답 및 해결 마감일이 표시됩니다

3. **해결 마감일 편집**
   - **Resolution due**를 클릭하여 편집합니다
   - 상황별 날짜 옵션(오늘, 내일, 다음 주 등)에서 선택하거나 **Pick date and time**을 클릭하여 특정 날짜와 시간을 입력합니다

4. **사용자 정의 날짜 설정**
   - 원하는 날짜와 시간을 설정하고 **Update** 버튼을 클릭합니다

## 자주 묻는 질문

### 1. 티켓 속성을 변경하려면 어떻게 해야 하나요?

**Admin** 설정으로 이동합니다 (티켓과 동일한 워크스페이스에 있는지 확인) > **Field Manager > Ticket Fields** > 원하는 필드를 클릭하여 기존 값을 변경하거나 새 값을 추가하거나, 상단에 있는 사용 가능한 필드 유형 목록에서 새 필드를 생성 > 저장.

### 2. 회색으로 표시되어 편집할 수 없는 필드가 있습니다. 어떻게 편집 가능하게 만들 수 있나요?

이 필드는 비즈니스 규칙에 의해 비활성화되어 있습니다. Admin 설정 > Business rules로 이동하여 해당 필드를 비활성화한 규칙을 찾아 끄거나 규칙에서 해당 필드를 제거하세요.

:::tip 실무 팁
티켓 속성을 효율적으로 관리하려면 팀에서 자주 사용하는 속성 값들을 미리 정의해두고, 비즈니스 규칙을 통해 자동화할 수 있는 부분은 자동화하는 것이 좋습니다.
:::