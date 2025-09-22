---
sidebar_position: 8
---

# 다양한 자산 상태 이해

Freshservice의 모든 자산에는 티켓, 문제 또는 변경과 마찬가지로 가용성 상태가 있습니다. 이는 자산의 가용성을 나타내고 조직에서 자산 할당이나 조달 결정을 계획하는 데 도움이 되는 중요한 속성입니다.

기본적으로 Freshservice에는 5가지 자산 상태가 있습니다:

- **사용 중(In Use):** 자산이 현재 조직의 누군가에 의해 사용되고 있습니다
- **분실(Missing):** 자산이 사용되고 있지 않지만 분실되어 사용할 수 없습니다
- **운송 중(In Transit):** 자산이 공급업체에게 주문되었거나 이동 중입니다
- **재고(In Stock):** 자산을 즉시 사용할 수 있습니다
- **폐기(Retired):** 자산이 너무 오래되었거나 작동하지 않아 폐기되었습니다

요구 사항에 따라 사용자 정의 자산 상태를 정의할 수도 있습니다. 이를 위해 **Admin -> Asset Management -> Asset Types & Fields**(또는 CI Types & Fields)로 이동합니다. 계정에 하나 이상의 작업 공간이 있는 경우 **Admin -> Global Settings -> Asset Management -> Asset Types & Fields**로 이동합니다.

새 상태를 생성할 자산 유형의 연필 아이콘을 클릭하여 **편집**합니다.

**Asset State** 필드를 클릭합니다.

**Field Properties** 팝업에서 새 **State Choices**를 생성하고 **Done**을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011965239/original/G32WhfWZkvKXUAZImzDi9MIQAzgSrN878Q.png?1716880984" style={{width: '610px'}} className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011965239" />

## FAQ

**1. 자산 상태를 기준으로 자산을 필터링하는 방법은?**

Inventory - Asset 페이지 왼쪽의 자산 필터 패널에서 아래와 같이 **드롭다운**에서 **자산 유형**을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011951759/original/BfVyU0YGAnfwijWa_ItCfyoZvs13C221WA.png?1716771802" style={{width: '136px'}} className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50011951759" />

선택되면 아래와 같이 필터 패널 끝까지 스크롤하여 **More** 옵션에서 **Asset State** 필드를 선택할 수 있습니다. 필드가 필터에 추가되면 필요한 자산 상태를 선택하고 필터링할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011951760/original/LUCarw9ZA8jak-7OB5AjvHhjR1xB2ikHWw.png?1716771826" style={{width: '130px'}} className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50011951760" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011951771/original/Za9W5eEUDfTmHi1MhMVe6UYvXwq4RIDUcw.png?1716771993" style={{width: '128px'}} className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50011951771" />

*참고: Hardware 및 Consumable 자산 유형은 기본적으로 'Asset State' 필드가 Admin >> Asset Types and Fields에 추가되어 있습니다*

**2. 특정/필요한 자산 상태를 기준으로 자산을 내보내는 방법은?**

위 단계(FAQ 1)에 따라 자산 유형을 기준으로 필요한 자산 상태가 필터링된 상태에서 **Export**(오른쪽 상단)를 선택하면 내보내기는 **Current View**와 **Asset type**에서 내보내기를 위한 두 가지 옵션을 제공합니다.

필터가 미리 적용되어 있으므로 여기서 **Current View** 옵션을 사용하여 적용된 필터 결과와 필요한 필드를 함께 내보낼 수 있습니다. 아래 스크린샷 참조를 확인하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011951797/original/FtmUnanVfpZvyLuMw-u2Xt28VWW0LSWoCg.png?1716772702" style={{width: '459px'}} className="fr-fil fr-dib" data-id="50011951797" data-attachment="[object Object]" />