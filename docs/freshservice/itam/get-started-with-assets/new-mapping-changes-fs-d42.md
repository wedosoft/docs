---
sidebar_position: 22
---

# FS와 D42의 새로운 매핑 변경사항

Freshservice는 Device42 모델과의 일관성을 보장하고 조정 문제를 최소화하기 위해 Cloud와 Hardware 계층 간의 컴퓨팅을 통합하여 자산 유형 구조를 변경하고 있습니다.

Virtual Machines, Hosts, K8s Nodes 및 해당 하위 유형(AWS VM, Azure VM, VMware vCenter Host 등)을 포함한 모든 클라우드 컴퓨팅 리소스는 이제 Hardware-Computer 계층으로 통합됩니다. Device42 장치 모델과의 이러한 정렬은 보고서와 워크플로우를 간소화하여 통합된 구조 내에서 모든 컴퓨팅 리소스를 더 쉽게 관리할 수 있게 합니다.

## 영향 사항

- **워크플로우 및 보고서에 미치는 영향**: 클라우드 자산 유형을 기반으로 한 워크플로우나 보고서가 있는 경우 12월 4일 이전에 새로운 구조를 반영하도록 업데이트하세요. 이는 일회성 활동입니다.
- **연결 또는 활동의 변경 없음**: 기존의 모든 연결, 관계 및 활동은 영향을 받지 않습니다.

따라서 현재 Cloud로 분류된 모든 컴퓨팅 리소스는 12월 4일 변경 사항이 구현되고 동기화되면 Hardware 계층으로 전환됩니다. 업데이트된 매핑에 대한 자세한 내용은 아래를 참조하세요:

## 매핑 테이블

| Device42 데이터 유형 | 현재 FS 매핑 | 새로운 FS 매핑 | 참고 |
|---------------------|-------------|-------------|------|
| F5 또는 NetScaler OS가 있는 Device | Load Balancer | Hardware - Computer | AWS, Azure 등의 Cloud Load Balancer는 계속 Cloud에 쓰기됩니다<br/><br/>언급된 OS를 실행하는 기타 장치는 Hardware -Computer에 쓰기됩니다 |
| Virtual/Container Host 플래그가 설정되고 ESXi OS가 있는 Device | VMware VCenter Host | Hardware - Computer-Host - VMware Host | |
| Virtual/Container Host 플래그가 설정된 Device | Host | Hardware - Computer-Host | |
| 가상 유형이고 VMWare 하위 유형인 Device | VMware VCenter VM | Hardware - Computer-Server - VMware VM | |
| 가상 유형이고 Amazon EC2 Instance 하위 유형인 Device | AWS VM | Hardware - Computer-Server - AWS VM | |
| 가상 유형이고 Azure Virtual Machine 하위 유형인 Device | Azure VM | Hardware - Computer-Server - Azure VM | |
| 가상 유형이고 GCE Virtual Machine 하위 유형인 Device | | Hardware - Computer-Server - GCP VM | |
| 가상 유형이고 위의 더 구체적인 자산 유형 중 하나와 일치하지 않는 Device | Virtual Machine | Hardware - Computer-Server | 새로운 'Type' 필드가 'Virtual'로 설정됩니다 |
| 물리적 유형이고 위의 더 구체적인 자산 유형 중 하나와 일치하지 않는 Device | Server | N/A | 새로운 'Type' 필드가 'Physical'로 설정됩니다 |