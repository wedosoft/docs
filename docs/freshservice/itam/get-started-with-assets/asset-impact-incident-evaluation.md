---
sidebar_position: 12
---

# Asset Impact를 사용하여 인시던트에 대한 자산의 영향 평가

티켓의 영향은 IT 서비스 데스크에서 중요한 역할을 합니다. 이는 회사의 IT 팀이 적절한 시기에 올바른 티켓을 우선순위로 정하는 데 도움이 됩니다. 인시던트 티켓의 영향은 일반적으로 에이전트 자신이 할당합니다.

그러나 더 높은 영향을 가진 자산을 추가해도 인시던트 티켓의 영향은 변경되지 않습니다. 예를 들어 "medium" 영향의 인시던트 티켓에 높은 영향 자산을 추가해도 영향은 여전히 "medium"으로 유지됩니다. 이는 인시던트의 근본 원인을 해결하는 데 지연을 야기하여 더 많은 복잡성을 만들 수 있습니다.

## Asset Impact란 무엇인가요?

Freshservice의 자산 영향 기능은 자산이 인시던트 티켓과 연결될 때 인시던트 티켓의 영향을 자동으로 재평가합니다. 결과는 티켓의 "impact" 필드 값에 반영됩니다.

우선순위 매트릭스가 활성화된 경우, 새로 할당된 영향 상태는 티켓의 우선순위에도 영향을 미칩니다.

**참고:** 자산 영향 기능은 인시던트 및 알림 티켓에서만 사용할 수 있습니다.

## 작동 방식은?

자산 영향은 티켓 세부 정보 페이지의 기존 "impact" 필드를 새로 연결된 자산의 영향과 비교하고 값을 더 높은 쪽으로 업데이트합니다.

예를 들어, 영향 필드에 "medium"이 있는 티켓을 상상해 보세요. "high" 영향 자산이 티켓에 연결되면 영향 필드의 값이 "medium"에서 "high"로 변경됩니다.

영향의 변화는 항상 낮은 값에서 높은 값으로만 이루어지며 그 반대는 아닙니다. "medium"에서 "high"로 갈 수 있지만 "high"에서 "medium"으로는 갈 수 없습니다.

**참고:** 인시던트 티켓의 영향 필드 변경 사항을 추적하려면 **Activities** 섹션을 사용할 수 있습니다.

## Asset Impact 활성화

Asset Impact를 활성화하려면:

- **Admin > Service Management > Service Desk Settings > Priority Matrix**로 이동합니다. 계정에 하나 이상의 작업 공간이 있는 경우 **Admin > {작업 공간 이름} > Service Management > Service Desk Settings > Priority Matrix**로 이동합니다.
- **Asset Impact** 섹션까지 스크롤하고 **Pass associated Asset impact to Ticket**이라고 표시된 토글 스위치를 활성화합니다.

<img className="fr-dii" src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/36508585/original/myk6SNWCEY2uuTz84tRmBHBPZvk3A09Q3g.png?1513940499" data-filelink="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/36508585/original/myk6SNWCEY2uuTz84tRmBHBPZvk3A09Q3g.png?1513940499" data-fileid="36508585" data-uniquekey="1513939484754" />

## 우선순위 매트릭스에 대한 Asset Impact의 효과

자산 영향과 함께 우선순위 매트릭스가 활성화된 경우, 새 자산을 연결한 후 티켓의 영향도 티켓의 우선순위에 영향을 미칩니다.

티켓의 긴급도가 "medium"이고 영향이 "low"인 예를 들어보겠습니다. 이제 우선순위 매트릭스에 따라 티켓의 우선순위는 "low"가 됩니다.

새 "medium" 영향 자산을 티켓에 연결하면 티켓의 영향이 "medium"으로 변경되고 티켓의 우선순위가 "low"에서 "urgent"로 이동합니다.

계정에서 우선순위 매트릭스가 비활성화된 경우, 자산 연결로 인한 영향의 변화는 티켓의 우선순위에 영향을 미치지 않습니다.

## 티켓에서 자산 연결 해제

인시던트 티켓에서 자산을 제거해도 티켓의 영향은 변경되지 않습니다. 영향 필드의 값은 동일하게 유지됩니다.