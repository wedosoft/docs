---
sidebar_position: 1
---

# 스팸 및 휴지통 관리

티켓을 스팸으로 표시하거나 자동/수동으로 삭제할 수 있습니다. 이를 통해 불필요한 티켓이 상담원의 티켓 목록을 어지럽히지 않고, 보고서가 왜곡되는 것을 방지할 수 있습니다.

## 수동으로 스팸 표시 또는 티켓 삭제

각 티켓 위에 있는 해당 버튼을 클릭하여 티켓을 수동으로 스팸으로 표시하거나 삭제할 수 있습니다:

![티켓 스팸/삭제 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008638064/original/GnF4rePGoilSc4122XDLZCi-pfMBGLeclg.png?1686899578)

티켓 목록 페이지에서 삭제하거나 스팸으로 표시할 티켓을 선택하고 상단에서 적절한 작업을 선택하여 대량 작업을 수행할 수도 있습니다:

![대량 스팸/삭제 작업](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008638085/original/96uxL2ssfinHUcnWOWYHTub6_63nehhIEw.png?1686899690)

## 연락처 차단 기능

티켓을 수동으로 스팸으로 표시하면, 스팸 티켓을 보낸 연락처를 차단할 수 있는 옵션이 표시됩니다. 연락처를 차단하면, 해당 연락처가 보내는 후속 티켓들이 자동으로 스팸으로 표시됩니다. 

차단된 연락처는 연락처 페이지의 '삭제됨' 연락처 목록에서 찾을 수 있으며, 필요시 복원할 수 있습니다.

![연락처 차단 과정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011678111/original/FB2tEeYcLvqYn3TwN-LTScXZNU_o_ZhRcQ.gif?1714391584)

## 자동화 규칙으로 스팸/삭제 처리

티켓 생성 자동화 규칙을 설정하여 자동화를 통해 티켓을 스팸으로 표시하거나 삭제할 수 있습니다. 예를 들어, 들어오는 모든 자동 응답을 삭제하거나, 특정 연락처에서 오는 모든 티켓을 자동으로 스팸으로 표시할 수 있습니다.

**설정 방법:**
1. **관리자 > 자동화 > 티켓 생성 > 새 규칙**으로 이동

![자동화 규칙 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008638177/original/tI4mwb41NPVSV_0ooJMfb4I8pzB4X5sG0g.png?1686900211)

## 스팸 및 휴지통 티켓 보기

해당 티켓 보기를 클릭하여 언제든지 스팸 및 휴지통의 모든 티켓을 볼 수 있습니다:

![스팸/휴지통 보기](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35328568/original/AXwIxlG--zdnExt9c01mpIi9UHO9A-IOLA.png?1507299461)

스팸/휴지통 티켓 보기에서는 선택한 티켓을 복원하거나 영구 삭제하는 등의 대량 작업을 수행할 수 있습니다. 오른쪽의 링크를 클릭하여 모든 스팸이나 휴지통을 한 번에 비울 수도 있습니다.

![스팸 폴더 관리](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011677886/original/0j1_CBObnnrQO0swR06LLAOi_kGwkvgFQw.png?1714390139)

![휴지통 관리](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011677892/original/SINGCoYfcbtE7IvHrfq_WTBLItZjZRRong.png?1714390155)

## 중요 참고사항

:::warning 자동 삭제 정책
티켓은 스팸이나 휴지통 보기에 **30일 동안만** 보관되며, 이후 Freshdesk에서 영구적으로 삭제됩니다. 30일 이내에는 티켓 내에서 사용 가능한 옵션을 사용하여 언제든지 티켓을 복원하거나 스팸에서 제거할 수 있습니다.
:::

:::info 보고서 영향
스팸으로 표시된 티켓은 보고서나 분석 지표에 포함되지 않습니다.
:::

## 티켓이 스팸으로 표시되는 경우

티켓이 스팸 폴더에 들어가는 세 가지 경우:

1. **상담원이 수동으로 스팸으로 표시**
2. **자동화 규칙에 의한 스팸 표시** (티켓 생성 또는 티켓 업데이트 규칙)
3. **삭제된 사용자가 제기한 티켓** (자동으로 스팸 처리)

## 스팸 처리된 티켓 복원 방법

### 수동으로 스팸 표시된 경우
1. **티켓 > 티켓 보기 > 스팸**으로 이동
2. 해당 티켓 열기
3. **스팸 아님** 클릭
4. 복원 후 **활동 표시**를 클릭하여 스팸 처리 경위 확인

### 삭제된 연락처의 경우
1. **연락처 > 연락처 보기**에서 해당 연락처 검색
2. 연락처 클릭 후 **복원** 선택
3. 향후 해당 연락처의 티켓은 스팸으로 표시되지 않음

## 스팸 처리 추적 방법

스팸 처리된 티켓을 추적하기 위해 다음과 같이 태그를 활용할 수 있습니다:

![스팸 추적 태그 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011677913/original/rYzUo7Nll-i-QPvNue1yCBL8NYzCCjV_5w.png?1714390301)

이 태그를 분석 보고서의 필터에서 사용하여 스팸으로 표시된 모든 티켓을 추적할 수 있습니다.

## 관련 자료

스팸 공격으로부터 헬프데스크를 보호하는 방법에 대한 자세한 내용은 [스팸 공격으로부터 헬프데스크 보호하기](https://support.freshdesk.com/en/support/solutions/articles/239858-how-to-protect-your-helpdesk-from-spam-attack-) 문서를 참고하세요.
