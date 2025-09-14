# 그룹 내 에이전트에게 티켓 자동 할당 (라운드 로빈)

그룹은 에이전트들을 하나로 모으고 접근 권한을 제어하는 것 외에도, 들어오는 티켓과 요청을 그룹에 속한 다양한 에이전트에게 할당하는 데 사용할 수 있습니다. 이는 보다 대상이 명확한 방식으로 수동으로 수행하거나, 요청을 담당하는 전용 관리자의 개입 없이 자동으로 수행할 수도 있습니다.

일반적으로 티켓은 그룹 또는 개별 에이전트에게 할당됩니다. 이는 팀의 구성원 중 한 명이나 워크플로 자동화를 사용하여 생성된 사전 정의된 규칙 또는 조건에 따라 수행됩니다. 예를 들어, 모든 높은 영향도 쿼리는 팀의 경험 많은 에이전트 중 한 명에게 직접 할당될 수 있고, 밤에 들어오는 티켓은 해당 교대 근무자에게 할당될 수 있습니다.

그러나 티켓이 그룹에 할당된다고 해서 그룹의 에이전트에게 할당되었다는 의미는 아닙니다(무작위로든 어떤 방법으로든). 이는 단순히 해당 그룹의 에이전트 중 누구든지 티켓을 자신에게 할당하거나 감독자가 대신 할당하도록 할 수 있음을 의미합니다.

다음은 이 전체 프로세스를 자동화하는 몇 가지 방법입니다.

## 방법 1: 라운드 로빈으로 모든 티켓 자동 할당

두 번째 방법은 간단하고 설정이 매우 쉽습니다. 헬프데스크의 모든 그룹에 대해 "자동 티켓 할당" 옵션을 켜면 모든 것이 저절로 처리됩니다. 티켓은 라운드 로빈 순서로 그룹의 모든 에이전트에게 분배됩니다. 이렇게 하면 모든 에이전트가 동일한 수의 티켓을 답변하게 됩니다.

**관리자 &gt; 사용자 관리 &gt; 에이전트 그룹**으로 이동하기만 하면 됩니다.

**계정에 여러 워크스페이스가 있는 경우:**

전역 워크플로를 수정하려면 **관리자 &gt; 전역 설정 &gt; 사용자 관리 &gt; 에이전트 그룹**으로 이동합니다.

워크스페이스 수준 워크플로를 수정하려면 **관리자 &gt; 워크스페이스 설정 > [워크스페이스 이름] > 사용자 관리 &gt; 에이전트 그룹**으로 이동합니다.

이제 라운드 로빈 할당을 켜고자 하는 그룹을 열고 **자동** 라디오 버튼을 클릭합니다.

이를 수행하는 방법에 대한 자세한 지침은 여기에서 찾을 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004108697/original/H_o7gs_N5evn7tBfJTsf8r_n3kiDQOAtmQ.png?1636384165" style="width: auto;" className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50004108697" / />

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004036126/original/UHoFVYRKFPYzvgmp-rHT8NsBjZEJqR9PnQ.png?1635320942" style="width: auto;" className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50004036126" / />

### 라운드 로빈 활성화 방법

프로필 아이콘 클릭 &gt; 자동 할당 티켓 활성화

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011900137/original/p8H_AU3fdukSGLUmnFLLftq8mlp6fdaMqA.png?1716298139" style="width: 200px;" className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011900137" / />

## 방법 2: 워크플로 자동화를 사용한 티켓 자동 할당

이 방법은 지원 팀에 각각 특정 영역에서 잘 작업하는 에이전트 그룹이 있을 때 특히 유용합니다. 워크플로 규칙을 만들고 전문 분야에 따라 티켓을 제공하는 것이 합리적입니다. 전문 영역의 키워드를 찾아 티켓의 제목이나 설명을 기반으로 티켓을 할당할 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000045065/original/PHZOUgwbYk5by7BCikR7tsmx8y8RvrUylA.png?1564038600" style="width: auto;" className="fr-dib fr-bordered" data-id="50000045065" / />

이는 지원 팀이 몇 가지 유형의 문제만 처리할 수 있을 때 상황을 처리하는 좋은 방법입니다. 그룹의 에이전트 수에 따라 설정하기 어려울 수 있습니다. 특정 워크플로 규칙을 수동으로 생성해야 하기 때문입니다.

에이전트가 해결해야 할 티켓 수가 동일하다는 보장은 없습니다. 하지만 조금만 생각하고 시간을 들이면 팀의 강점에 맞게 미세 조정된 자동 할당 마법을 만들어낼 수 있습니다.

**참고:** 워크플로 자동화를 사용하여 처음에 티켓을 그룹에 할당하거나 지원 이메일을 설정할 때 동일한 작업을 수행해야 합니다. 그렇지 않으면 자동 할당 기능이 작동하지 않습니다. 이 기능은 라운드 로빈 기능에서만 작동하며 수동으로 할당된 티켓에서 에이전트를 제외하지 않습니다.

## 자주 묻는 질문

**1. 에이전트가 라운드 로빈 할당에 활성화될 때 로그/알림을 받을 수 있는 방법이 있나요?**

현재 에이전트의 로그인 알림 및 가용성 옵션이 없습니다.

**2. 자동 할당 티켓이 작동하지 않는 경우 이 문제를 해결하는 방법은?**

해당 에이전트 그룹(**관리자/해당 워크스페이스 &gt; 에이전트 그룹**)에 대해 자동 할당 설정이 활성화되어 있고 에이전트의 프로필에서 "자동 할당 티켓" 체크박스가 활성화되어 있는지 확인하세요.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011900138/original/JMd-F7IF8etPWfmEdLJY1zukEB0h5OzeIA.png?1716298146" style="width: 226px;" className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011900138" / />

**3. 내 에이전트 중 한 명이 '자동 할당 티켓' 또는 라운드 로빈이 활성화되어 있는지 확인하는 방법은? 누군가에게 티켓 자동 할당에서 사용자를 추가하거나 제거할 수 있는 액세스 권한을 부여하는 방법은?**

이 작업에는 에이전트에 대해 할당된 에이전트 가용성 관리 액세스 권한이 있는 관리자 수준 권한이 필요합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011900837/original/yDjlUZI07V9z9c-27GH1pmvqEWJUMXCMdA.png?1716299801" style="width: 698px;" className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011900837" / />

대시보드로 이동하여 **세 개의 점 &gt; 편집 &gt; 에이전트 가용성 위젯 선택 &gt; 라운드 로빈이 활성화된 그룹 선택 &gt; 저장**을 클릭합니다.

생성된 위젯에서 **자세한 정보**를 클릭하면 에이전트의 라운드 로빈을 개별적으로 관리할 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011900288/original/3Y6bF7g8B-OTkVpW2Cb8vIlEpjKkXwG1mg.png?1716298430" style="width: 226px;" className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011900288" / />

**4. 에이전트가 로그인할 때 자동 티켓 할당/라운드 로빈 상태가 재설정되나요?**

아니요, 에이전트가 로그인해도 Freshservice에서 자동 티켓 할당 상태가 재설정되지 않습니다. 상태는 로그인 이전과 동일하게 유지되어 할당 프로세스의 연속성을 보장합니다. 수동으로 라운드 로빈을 활성화하거나 **에이전트 가용성 위젯**이 구성된 경우 관리자가 대시보드에서 이를 수행할 수 있습니다.

**5. 그룹의 관찰자 에이전트에게 티켓을 할당할 수 있나요?**

관찰자는 티켓만 볼 수 있고 할당될 수 없습니다.

**6. '작업'을 에이전트 그룹에 할당하고 자동 할당이 해당 티켓을 다음 사용 가능한 에이전트에게 라우팅하도록 할 수 있나요?**

현재 라운드 로빈 할당은 티켓에만 사용할 수 있고 작업에는 사용할 수 없습니다.

**7. 에이전트의 가용성을 관리(활성화 또는 비활성화)하는 방법은?**

대시보드로 이동하여 라운드 로빈을 활성화 또는 비활성화할 수 있는 에이전트 가용성 위젯을 클릭하세요. (권한에 대해서는 FAQ 2를 참조하세요)

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012030199/original/9Nf5zp9DMjgwueRqCmI-RicDWvVm8RZW4Q.png?1717418199" style="width: 678px;" className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50012030199" / />