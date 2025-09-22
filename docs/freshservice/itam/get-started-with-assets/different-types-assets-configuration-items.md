---
sidebar_position: 1
---

# Freshservice의 다양한 자산/구성 항목 유형

Freshservice의 **CMDB/자산 관리** 모듈은 IT 서비스 데스크에 연결된 모든 자산과 구성 항목의 완전한 목록을 보여줍니다. 기본적으로 Freshservice는 일반적인 IT 서비스 데스크의 모든 필수 요소를 다루는 자산/CI 유형 세트와 함께 제공됩니다. 여기에는 노트북, 워크스테이션, 네트워크 라우터 등과 같은 하드웨어 항목과 운영 체제와 같은 소프트웨어 자산이 포함됩니다.

다음은 Freshservice의 기본 자산/CI 유형의 완전한 목록입니다:

- Cloud
- AWS (EC2, RDS, EBS)
- Hardware
- Computer
- Desktop
- Laptop
- Server
- Unix Server
- Aix Server (Solaris Server, Windows Server)
- Storage (Disk)
- Data Center (Rack, UPS)
- Mobile Devices (Mobile, Tablet)
- Monitor
- Printer
- Projector
- Scanner
- Router
- Switch
- Access Point
- Firewall
- Other Devices
- Software
- Applications
- Database
- MySQL
- MSSQL
- Operating System
- Microsoft
- Linux
- Mac OS X
- Web Server
- IIS
- Apache
- Network
- Services
- IT Service
- Email Service
- Backup Service
- Hosting Service
- Business Service
- Sales Service
- Support Service
- Consumable
- Document
- Others

기본 카테고리가 목적에 맞지 않는 경우, *Admin Settings* 페이지에서 추가 자산/CI 유형을 추가하거나 기존 항목을 편집할 수 있습니다.

**참고:** 기본 자산이나 구성 항목은 삭제할 수 없습니다.

**Freshservice에 새 자산/CI 유형을 추가하는 빠른 가이드:**

1. 계정 관리자로 Freshservice에 로그인합니다.

2. **Admin > Asset Management > Asset Types and Fields**로 이동합니다. 계정에 하나 이상의 작업 공간이 있는 경우 **Admin > Global Settings > Asset Management > Asset Types and Fields**로 이동합니다.

   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006919401/original/O9bQ_ppKsKtfBACmNm99wUJAh1sQ-34ZJQ.png?1668504004"  className="fr-fil fr-dib" data-attachment="[object Object]" data-id="50006919401" />

3. 오른쪽 상단의 **New Asset Type** 버튼을 클릭합니다.

   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000407043/original/34fWiWkEfcfp1z1ruuikQk8OKmzpKVrpFQ.png?1574130558"  className="fr-fic fr-dib fr-bordered" data-id="50000407043" />

4. 자산/CI의 이름과 설명을 입력합니다.

5. 해당하는 경우 자산/CI의 상위 카테고리를 선택합니다.

6. **Save** 버튼을 클릭하여 자산 추가를 완료합니다.

   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000407064/original/g5dMZZjZsYUVDmsRhQTGPYG-aSqB8-fQWQ.png?1574131085"  className="fr-fic fr-dib fr-bordered" data-id="50000407064" />

**참고: 기존 자산 유형 활용:** 시스템에서 제공하는 기본 자산 유형을 활용하세요. 이는 기존 기능과의 호환성을 보장하고 데이터 불일치의 위험을 최소화합니다.

**기존 자산 유형 내 계층 구조:** 사용자 정의 계층 구조를 만드는 대신, 기존 자산 유형의 하위에 자산을 구성하는 옵션을 탐색하세요. 이는 시스템 기능을 희생하지 않으면서도 논리적 구조를 유지합니다.

예: Hardware < Netbook< Computer를 만드는 대신,

Hardware < Computer < Netbook을 만드는 것이 좋습니다.