---
sidebar_position: 18
---

# Freshservice에서 티켓으로 변환되지 않는 이메일

이 문제에 대해 확인해야 할 몇 가지 단계가 있습니다:

## 1. 전달 규칙 확인

지원 이메일 주소로 오는 모든 이메일에 대한 문제인 경우 링크에 표시된 대로 전달 규칙이 설정되었는지 확인하세요. 전달 규칙이 설정된 경우에만 메일박스의 이메일이 Freshservice로 티켓으로 전달됩니다. **관리자 > 채널 > 이메일 설정 및 메일박스**에 표시된 전달 주소로 직접 이메일을 보내어 전달 주소가 작동하는지 확인할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838384/original/LrMR5W6Sm1lj-Nh5SU8_C-QPux2uUub9Mg.png?1678706894"  />

## 2. 발신자와 수신자 주소 확인

이메일의 '발신자'와 '수신자' 주소가 동일하면 Freshservice에서 티켓으로 생성되지 않습니다. '답장' 주소와 '수신자' 주소가 동일한 경우에도 마찬가지입니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838355/original/qBohDGAwetCisBebMECWo16mgO2kAm12QQ.png?1678706812"  />

## 3. 서비스 데스크 제한 설정 확인

서비스 데스크 제한(특정 도메인의 이메일만 티켓으로 생성될 수 있음)을 활성화했는지 확인하세요. **관리자 > 채널 > 지원 포털 설정**으로 이동하여 아래로 스크롤하여 확인하세요. '지정된 도메인의 사용자'를 선택한 경우 '모든 도메인의 사용자'로 변경하고 변경 사항을 저장하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838354/original/hQYzz72AFIHMVWfuUDjEZqEn0ub1J3BzNA.png?1678706812"  />

## 4. 스팸 폴더 확인

**티켓** 탭 > 뷰 이름(목록) 클릭 > **스팸 폴더** 선택 > 티켓이 여기에 있는지 확인하세요.

만약 있다면:
- 티켓 복원 > 오른쪽 상단의 **활동**을 클릭하고 티켓에서 작업했거나 스팸으로 표시한 자동화(티켓 생성, 시간 트리거 등)가 있는지 확인합니다. 이는 향후 이메일이 티켓으로 들어오도록 보장하기 위함입니다.

만약 없다면:
- 티켓 오른쪽에 표시된 요청자 이름 클릭 > 요청자가 삭제되거나 비활성화되었는지 확인합니다. 요청자를 다시 활성화하면 향후 해당 요청자의 모든 이메일이 티켓으로 들어옵니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007838353/original/WSmAZPAvW-9RO-cnGUHBTMXhhGMcgMABzw.png?1678706812"  />