---
sidebar_position: 3
---

# 자산 가져오기

CSV 파일을 가져와서 자산을 대량으로 생성하거나 업데이트할 수 있습니다. 다음은 자산 가져오기에 대한 일반적인 가이드라인입니다.

## 첫 번째 자산 가져오기 준비

- 사용자 정의 자산 유형을 생성해야 하는 경우, 가져오기를 시작하기 전에 생성하세요. (Admin -> Asset Types로 이동하여 새 자산 유형을 생성할 수 있습니다)
- 각 자산 유형에 대한 사용자 정의 자산 필드를 생성해야 하는 경우, 가져오기를 시작하기 전에 생성하세요
- 선택 항목이 있는 드롭다운 필드와 같은 새 필드를 생성한 경우, 가져오기 전에 Admin -> Asset Types에서 선택 항목을 추가했는지 확인하세요

## 업로드할 CSV 파일 준비

- **자산 유형별로 CSV 파일 분할 -** 한 번에 하나의 자산 유형의 자산만 가져올 수 있습니다. 첫 번째 단계로 각 자산 유형에 대해 별도의 파일을 만드세요.
- 필수 컬럼
  - 기본적으로 **Display Name**은 Freshservice에서 자산에 필요한 유일한 필드입니다. CSV에 이 컬럼이 있는지 확인하세요
  - 필수로 구성한 필드가 있는 경우, 이러한 필드도 CSV에서 사용할 수 있는지 확인하세요
  - 노트북 자산 유형에 대한 샘플 CSV 파일이 첨부되어 있습니다 (팁: Freshservice에서 샘플 자산을 생성하고 내보내서 모든 자산 유형에 대한 템플릿을 얻을 수 있습니다. 해당 자산 유형에 대한 모든 가능한 필드를 얻으려면 파일을 내보낼 때 All Fields를 선택해야 합니다)
- 자산에 사용자를 할당하려면 Used By 필드에 사용자의 이메일 ID를 지정하세요.
- 자산에 에이전트를 Managed By로 할당하려면 Managed By 필드에 에이전트의 이메일 ID를 지정하세요

## 파일 가져오기

<img className="fr-dib" src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40326448/original/qrnCM4u051udnrv3L5YYkzemNkOscPpfqQ.png?1534774375" data-filelink="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40326448/original/qrnCM4u051udnrv3L5YYkzemNkOscPpfqQ.png?1534774375" data-fileid="40326448" data-uniquekey="1534774364343" />

- **Inventory -> Import**로 이동
- 가져올 자산 유형 선택
- CSV 파일 업로드
- CSV의 레코드를 Freshservice의 자산과 일치시키는 방법 선택:
  - Import Hardware 또는 해당 하위 유형에 대해 자산 유형이 선택된 경우, 시리얼 번호(기본값), 표시 이름 또는 자산 태그로 레코드를 일치시킬 수 있습니다.
  - 다른 자산 유형이 선택된 경우, 레코드를 전혀 일치시키지 않거나(기본값 - CSV의 모든 항목을 새 자산으로 생성) 표시 이름 또는 자산 태그로 레코드를 일치시킬 수 있습니다
- **Next** 클릭

## 필드 매핑

<img className="fr-dib" src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40317835/original/Ibse-4bydd7bRqVP3Bq21KpYrp413SyZjg.png?1534748615" data-filelink="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40317835/original/Ibse-4bydd7bRqVP3Bq21KpYrp413SyZjg.png?1534748615" data-fileid="40317835" data-uniquekey="1534748532539" />

- Freshservice는 CSV의 헤더를 기반으로 CSV의 필드를 자동으로 매핑합니다. CSV 파일의 첫 번째 자산 항목 값도 매핑 옆에 예시로 표시됩니다
- 이 매핑을 검토하고 필요에 따라 변경할 수 있습니다
- 날짜 필드를 업데이트하려는 경우 선택한 날짜 형식과 CSV의 날짜 형식이 일치하는지 확인하세요
- **Import**를 클릭하여 가져오기 프로세스를 시작합니다.
- 가져오기 상태 화면에 가져오기의 현재 상태가 표시됩니다. 상태는 30초마다 업데이트됩니다
- 가져오기가 완료되면 가져오기 상태와 가져오기 중 발생한 오류의 빠른 요약을 받게 됩니다
- 가져오기가 완료되면 가져오기 상태 보고서가 포함된 이메일도 보고서를 시작한 사용자에게 전송됩니다

**일반적인 자산 오류:**

**시리얼 번호는 고유해야 합니다:** 위의 "시리얼 번호는 고유해야 합니다" 오류를 방지하려면 해당 자산이 인벤토리 휴지통 폴더에 포함되지 않았는지 확인하세요. 휴지통에 액세스하려면 인벤토리 옆의 3개 선을 클릭 > 휴지통을 클릭하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011982079/original/rpDte-uAFuTNY_8qUssuaL9Myp0RR6WPKg.png?1716975208"  className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011982079" />

**자산 유형 불일치:** 가져오기 중에 자산 유형이 올바르게 매핑되었는지 확인하세요. 이 오류는 자산이 이미 인벤토리의 다른 자산 유형으로 있는 경우에도 발생할 수 있습니다.

**날짜 형식 불일치:** CSV의 날짜 형식이 포털에서 가져오기를 수행하는 동안 선택한 날짜 형식과 일치하는지 확인하세요.

해당 자산 유형에 대한 인벤토리 모듈에서 샘플 파일을 내보낸 다음 해당 파일을 사용하여 데이터를 가져오세요. 이렇게 하면 필드가 전달되는 형식을 식별할 수 있습니다. 또한 아래 사항들을 확인해 주세요.

- 자산 가져오기에 사용된 CSV 파일을 검증하세요.
- 아래와 같이 CSV의 날짜 형식이 가져오기를 수행하는 동안 선택한 날짜 형식과 일치하는지 확인하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011982667/original/iOe7WvaQi6wiEwnls7UO9dyfu8KfovYt4Q.png?1716977412" width="320" height="207" className="fr-fic fr-dii inline-image"  data-attachment="[object Object]" data-id="50011982667" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011982666/original/elVx9mfSDqY_ltcUL2puXwSmodZi78ci4g.png?1716977412" width="371" height="266" className="fr-fic fr-dii inline-image"  data-attachment="[object Object]" data-id="50011982666" />

- 날짜 형식이 예상대로 업데이트되면 시스템이 날짜 필드를 성공적으로 인식하고 자산을 업로드합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011982665/original/hA6RYRGv0tPZfRcjXO1dUYdqBv40P9Qr9g.png?1716977411" width="489" height="103" className="fr-fic fr-dii inline-image"  data-attachment="[object Object]" data-id="50011982665" />