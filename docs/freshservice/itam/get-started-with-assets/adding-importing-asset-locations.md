---
sidebar_position: 15
---

# 자산 위치 추가 및 가져오기

Freshservice를 사용하면 이제 위치를 추가하거나 가져올 수 있어 구성 항목을 더 쉽게 분리하고 찾을 수 있습니다. 또한 부모-자식 계층 구조로 위치를 구성할 수 있습니다(예: 회사가 여러 장소에서 운영되는 경우 맨 위에 국가 이름을 두고 그 다음에 주, 지역, 도시를 둘 수 있습니다). 각 필드는 별도의 레코드가 됩니다.

## 새 위치를 추가하는 방법은?

- Freshservice Admin 콘솔에 로그인합니다

- **Admin** -> **Asset Management** -> **Locations** -> **New Location**으로 이동합니다. 계정에 하나 이상의 작업 공간이 있는 경우 **Admin** -> **Global Settings** -> **Asset Management** -> **Locations** -> **New Location**으로 이동합니다

- 이제 위치의 세부 정보를 채우고 드롭다운에서 부모 위치를 선택한 후 **Save**를 클릭할 수 있습니다

- 완료되면 저장을 누르면 위치가 계층적 형식으로 나열됩니다

## 위치를 가져오는 방법은?

- Freshservice Admin 콘솔에 로그인하고 **Admin** -> **Asset Management** -> **Locations** -> **Import**로 이동합니다. 계정에 하나 이상의 작업 공간이 있는 경우 **Admin** -> **Global Settings** -> **Asset Management** -> **Locations** -> **Import**로 이동합니다

- 여기서 .CSV 파일을 업로드하거나 드래그 앤 드롭하고 **Next**를 클릭할 수 있습니다

- Freshservice 필드를 .CSV 파일에 매핑하고 **Import**를 클릭합니다. 실패, 업데이트된 레코드 수 등도 확인할 수 있습니다.

- 가져오기 상태가 **Completed**로 변경되면 Freshservice에서 업데이트된 전체 필드 목록을 볼 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000688159/original/kKwMhsPrnAqwYduKKmlNmRROQkEiYbdoQQ.gif?1580993011" style={{width: 'auto'}} className="fr-fil fr-dib fr-bordered" data-attachment="[object Object]" data-id="50000688159" />

**참고:**

업로드하기 전에 CSV 파일에 다음이 있는지 확인하세요:

1. 필드 이름이 있는 행 헤더(예: Location Name, Parent Location, Primary Contact 등)
2. 필수 필드 - Location name 컬럼
3. 부모 위치가 계층적 경로에 있는지 확인(예: California의 부모 위치가 USA인 경우 경로가 **USA/ California**로 작성되었는지 확인)
4. UTF-8로 인코딩됨

다음으로 CSV 필드를 Freshservice 필드에 매핑하고 **Import**를 클릭합니다.