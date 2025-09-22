---
sidebar_position: 24
---

# Basic ITAM에서 Advanced ITAM으로 전환하는 영향

Basic에서 Advanced ITAM으로 전환은 discovery hub를 통해 수행할 수 있습니다. discovery hub를 사용하여 단계별 가이드 방식으로 Device42를 설정하세요. 설정하기 전에 Basic과 Advanced ITAM의 차이점을 이해하고 싶다면 **Compare Basic and Advanced**를 클릭하세요.

Device42 설정에는 4가지 주요 단계가 포함됩니다. [여기서](https://support.freshservice.com/en/support/solutions/articles/50000010238-managing-it-assets-with-discovery-hub) 자세히 알아보세요.

1. **Device42 Appliance 설정**: Device42 Main Appliance(MA)를 선택하고 다운로드합니다. Device42 MA에는 기본 암호, 네트워크 주소, NTP 클라이언트 구성 및 시간대 업데이트가 포함됩니다.

2. **라이센스 받기**: 평가판 라이센스 키를 다운로드하고 적용합니다

3. **Remote Collectors 배포**: Remote Collector는 네트워크 인터페이스 구성, NTP 설정, Device42 MA에 대한 연결 등과 같이 글로벌 환경 전반에서 discovery 기능을 확장합니다.

4. **Device42 앱 설치**: Freshservice Domain Name, Cloud Connector, Verification Token 상자에 관련 세부 정보를 입력합니다. Freshservice Default Approver 드롭다운에서 기본 승인자를 선택하고 설치 프로세스를 완료합니다. 완료되면 Freshservice에 Basic에서 Advanced 버전의 자산 관리로의 전환이 알림됩니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760476/original/4PN7AjSDOHobHgXLwSc4hQjBK4gIHOF2Zw.png?1732010377"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760476" />

## Basic에서 Advanced discovery로 이동할 때 basic discovery에 어떤 일이 발생하나요?

계정이 basic에서 advanced discovery로 전환되면 기존 basic discovery 구성이 CMDB에 쓰기를 중단하여 조정 문제를 방지합니다. D42 통합이 discovery를 인수합니다. Advanced discovery로 전환할 때 네이티브 discovery 애플리케이션, 클라우드 자산 및 통합이 영향을 받습니다. 다음은 영향 목록과 중단을 방지하기 위해 수정하는 방법입니다:

- **Discovery가 있는 Marketplace 통합**: Intune, Jamf, Chrome Connector, Automox와 같은 통합이 CMDB에 쓰기를 중단하며 Device42 main appliance에서 재구성해야 합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760475/original/PM38X84rQ0ylahLwAUstjy4sTvGpE_d1bw.png?1732010377"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760475" />

- **Remote Actions가 있는 Marketplace 통합**: Intune, Airwatch, Automox와 같은 앱에서 지원되는 Endpoint Actions는 계속해서 marketplace에서 제공되므로 Device42와 Freshservice Marketplace 모두에서 통합을 설정해야 합니다. Device 42 애플리케이션에서 discovery를 설정하고 Freshservice 애플리케이션에서 actions를 설정해야 합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760477/original/S4x8CLgrBjJc9dcdd4k0jpEvB3hZi3RjEA.jpeg?1732010377"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760477" />

- **Native Discovery Probe 및 Agent 비활성화**: Freshservice Probe와 Agent가 조정 문제를 방지하기 위해 CMDB에 쓰기를 중단합니다. 장치에 있는 경우 agents도 제거를 위해 트리거됩니다. probe는 계속해서 AD User sync를 지원합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760474/original/b8nN6hCRJpNk5DlceBtZbMAlXfAx-XeXKw.png?1732010377"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760474" />

- **ITAM Basic Cloud Discovery 비활성화**: AWS, Azure, GCP, K8S용 Cloud Discovery 앱이 CMDB로 자산 동기화를 중단합니다. AWS Cloud management 앱과 Azure용 orchestration 앱을 통해 orchestration 기능을 계속 활용할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760479/original/n-2sjfYD-1Jq3fsIJo9540Fs6AxkMreCxQ.png?1732010378"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760479" />

- **Cloud Compute의 계층 변경**: ITAM Advanced가 AWS, Azure, GCP, K8S 또는 Vcenter에서 동일한 클라우드 컴퓨팅 리소스를 발견할 수 있게 되면 단일 계층 하에서 device42에서 장치가 모델링되는 방식에 맞추기 위해 해당 자산을 하드웨어 계층으로 이동합니다.

계정이 Advanced discovery로 전환되면 클라우드 discovery 계층 하의 모든 컴퓨팅 리소스가 D42에 의해 하드웨어 자산으로 이동됩니다. 이는 Cloud discovery를 사용하는 고객에게만 적용됩니다. [여기서](https://support.freshservice.com/en/support/solutions/articles/50000010317-deprecation-of-cloud-compute-asset-types) 자세히 알아보세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013760478/original/h8F5q5SGth98hyAavzgKonkI7gzj13wAtw.png?1732010378"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013760478" />

## Basic ITAM으로 다시 전환

Advanced ITAM 사용자가 Basic ITAM으로 다시 전환하면 Device42 애플리케이션이 CMDB에 쓰기를 중단합니다. Basic ITAM Discovery가 CMDB에 다시 쓰기를 시작합니다.