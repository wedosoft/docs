---
sidebar_position: 1
---

# 마감 시간 및 SLA 정책 이해하기

고객들은 티켓을 제기했을 때 언제 응답과 해결을 기대할 수 있는지 알고 싶어합니다. 서비스 수준 계약(SLA) 정책을 통해 지원팀의 성과 표준을 설정할 수 있습니다. 티켓 우선순위에 따라 상담원이 티켓에 응답하고 해결해야 하는 시간을 설정하고, SLA 위반에 대해 특정 상담원에게 알리는 자동 에스컬레이션 규칙도 설정할 수 있습니다.

[SLA 구성 방법을 이해하려면 여기를 클릭하세요.](https://support.freshservice.com/en/support/solutions/articles/156459-creating-multiple-sla-policies-for-specific-departments-and-groups)

1. 워크스페이스 관리자는 워크스페이스 수준에서 SLA 정책을 생성할 수 있습니다.
2. 글로벌 SLA 정책은 모든 워크스페이스의 티켓에 적용됩니다.
3. 기본 SLA 정책은 글로벌 수준에서 기본적으로 생성되고 활성화됩니다.

**실행 순서:** 티켓의 SLA 정책은 특정 워크스페이스를 위해 생성된 로컬 SLA 정책에 의해 결정됩니다. 로컬 SLA 정책의 지정된 조건과 일치하지 않으면 글로벌 정책을 따릅니다. 둘 다 적용되지 않으면 기본 SLA 정책이 티켓에 적용됩니다.

## 마감 시간

SLA 정책은 Freshservice에서 각 티켓의 "첫 번째 응답 마감일"과 "해결 마감일"을 결정하는 데 사용됩니다. 모든 고객에 대한 기본 SLA 정책을 가질 수도 있고, 프리미엄 지원 패키지를 구독한 고객들과 같은 다양한 고객 계층에 대해 여러 SLA 정책을 가질 수도 있습니다. 모든 티켓의 마감 시간은 티켓 오른쪽에서 확인할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006707209/original/H2Y6gxu02eXh4PggOSDHiTTkQ_ywpQwjPw.png?1666271764"  className="fr-fic fr-fil fr-dib fr-bordered" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000084733/original/xOLa2QVNF65nJndBsbyoXveGMKv3KhQ0bA.png?1565256779" width="624" height="313" className="fr-fic fr-dii" />

헬프데스크 모범 사례에서는 SLA 정책이 티켓 우선순위에 따라 결정되도록 권장합니다. Freshservice에서는 긴급, 높음, 보통, 낮음 우선순위 티켓에 대한 서비스 수준을 정의할 수 있습니다. 그런 다음 Freshservice의 다양한 자동화를 사용하거나 수동으로 어떤 티켓이 긴급 우선순위 이슈를 구성하고 어떤 것이 낮은 우선순위인지 지정할 수 있습니다.

**티켓에서 실행된 SLA를 확인하는 방법**

해당 티켓으로 이동하면 티켓에서 실행된 SLA를 확인할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011400844/original/pk6M2Lan_qU-pVK1dOHj5PAn-mUfCyHHwg.png?1711903991"  className="fr-fic fr-fil fr-dib" />

:::info 참고
관리자는 이제 **티켓/문제/변경 및 릴리스(TPCR) 작업**에 대한 내부 **운영 수준 계약(OLA)**을 정의할 수 있습니다. 이는 상담원이 **TPCR 내부의 작업**을 완료해야 하는 시간을 지시하여 지속적인 서비스 제공과 규정 준수를 보장합니다. 자세한 내용은 [여기](https://support.freshservice.com/en/support/solutions/articles/50000004246-setting-up-ola-policies-for-tasks?utm_source=SLA_solutionarticle&utm_medium=SLA_solutionarticle&utm_campaign=SLA_solutionarticle)를 참조하세요.
:::