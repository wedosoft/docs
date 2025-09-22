---
sidebar_position: 4
---

# Freshservice에서 인시던트에 하위 티켓 추가하기

비즈니스에 심각한 중단을 일으키는 주요 인시던트가 보고되면 신속한 주의와 빠른 해결이 필요합니다.

이러한 상황에서는 서비스 데스크가 동일한 문제이거나 그로 인한 더 표면적인 문제에 대한 끝없는 티켓을 받는 경우가 많습니다.

원본 티켓이 비즈니스에 더 큰 우선순위이므로 다른 모든 티켓을 하위 티켓으로 추가할 수 있습니다. 그런 다음 진행하면서 하위 티켓을 업데이트하면서 상위 티켓을 처리할 수 있습니다.

## 인시던트에 하위 티켓을 추가하는 방법

1. 티켓의 상세 보기에서 **관련 티켓** 탭으로 이동하여 **+ 하위 티켓 추가**를 클릭합니다
2. 하위 티켓 추가 대화상자가 열리며 **새 티켓**을 생성하거나 **기존 티켓**을 추가할 수 있습니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006670321/original/z48BYzjJa1RkUeX79aRKw6TA8vOJTJ1ClA.png?1666003823" style={{width: 'auto', maxWidth: '100%'}} />

3. 새 티켓을 생성하려면 양식을 작성하고 **저장**을 누릅니다
4. 기존 티켓을 추가하려면 기존 티켓 옵션을 선택합니다. 제목 줄을 기반으로 유사한 인시던트 목록이 표시됩니다
5. 상위 티켓에 추가할 티켓 옆의 확인란을 체크합니다. 나열되지 않은 티켓에 접근하려면 검색 필드를 사용할 수 있습니다
6. **추가**를 클릭합니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006670705/original/UmbUVDWo_NHHMFeSLGrYHtiQ3A12_-109A.png?1666005781" style={{width: 'auto', maxWidth: '100%'}} />

7. 모든 하위 티켓이 관련 티켓 섹션에 추가됩니다. 해당하는 **'-' 기호**를 클릭하여 이 목록에서 티켓을 제거할 수 있습니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006670756/original/jlWNzK8Upi34DGR5AKlt0OehPzRLRwGt7g.png?1666006028" style={{width: 'auto', maxWidth: '100%'}} />

상위 티켓은 다른 모든 티켓과 연결되어 에이전트가 하위 티켓으로 구별할 수 있도록 도와줍니다.

## 연결된 하위 티켓에서 작업을 수행하는 방법

1. **관리자 -> 워크플로우 자동화 -> 새 자동화 -> 티켓**으로 이동합니다. 계정에 둘 이상의 워크스페이스가 있는 경우 **관리자 > {워크스페이스 이름} > 워크플로우 자동화 > 새 자동화 > 티켓**으로 이동합니다
2. 이벤트 노드를 드래그 앤 드롭하고 드롭다운에서 **인시던트가 업데이트됨**을 선택하고 **완료**를 클릭합니다
3. 다음으로 조건 노드를 드래그 앤 드롭하고 **상태가 해결됨**을 선택하고 **완료**를 클릭합니다
4. 마지막으로 작업 노드를 드래그 앤 드롭하고 이러한 작업 수행에서 **연결된 하위 티켓**을 선택합니다
5. **상태를 해결됨으로 설정**을 추가하고 "+"를 클릭하여 **메모 추가**로 다른 작업을 추가합니다
6. 메모의 설명에서 플레이스홀더에서 티켓 URL을 선택하고 "티켓 URL이 해결됨"으로 언급하고 **완료**를 클릭한 다음 **활성화**를 클릭합니다

<iframe src="https://fast.wistia.net/embed/iframe/8civkzmxgz" title="Associated Child Tickets Video" frameborder="0" width="640" height="360" style={{maxWidth: '100%'}} allowfullscreen="" sandbox="allow-scripts allow-forms allow-same-origin allow-presentation"></iframe>