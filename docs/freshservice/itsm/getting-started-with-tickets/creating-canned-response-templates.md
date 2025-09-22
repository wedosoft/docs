---
sidebar_position: 3
---

# Canned Response로 공통 답변 템플릿 만들기

모든 서비스 데스크에는 반복적으로 발생하는 공통 질문들이 있습니다. 상담원들은 동일한 질문에 대해 매번 새로 답변을 작성하느라 시간을 낭비하고, 일관성 없는 답변을 제공하게 됩니다. 시간을 절약하기 위해 공통 질문에 대한 미리 서식이 지정된 답변 템플릿을 Canned Response로 만들어 상담원들이 한 번의 클릭으로 재사용할 수 있도록 할 수 있습니다.

:::info 워크스페이스 설정
Canned Response는 워크스페이스 단위로만 설정할 수 있습니다. 상담원이 접근할 수 있는 모든 워크스페이스의 Canned Response가 설정에 표시됩니다.
:::

동적 콘텐츠 플레이스홀더를 사용하여 요청자 이름, 상담원 서명, 티켓 세부 정보로 각 답변을 개인화할 수도 있습니다.

## Canned Response 생성 가이드

1. **관리자 메뉴로 이동**
   - **Admin > Automations & Productivity > Agent Productivity > Canned Response**로 이동합니다
   - 여러 워크스페이스가 있는 경우: **Admin > \{워크스페이스 이름\} > Automations & Productivity > Agent Productivity > Canned Response**로 이동합니다

2. **새 응답 추가**
   - **Add Canned Response** 버튼을 클릭합니다

3. **제목 입력**
   - 상담원이 답변을 사용할 때 쉽게 이해할 수 있는 **Response Title**을 입력합니다

4. **응답 템플릿 작성**
   - 리치 텍스트 에디터에서 서식이 지정된 응답 템플릿을 작성합니다
   - **Insert Placeholder** 버튼을 클릭하여 티켓 ID, 제목, 요청자 이름과 같은 동적 콘텐츠를 자동으로 포함시킬 수 있습니다

5. **첨부파일 추가** (선택사항)
   - 이 응답에 포함하고 싶은 첨부파일을 추가합니다

6. **가시성 및 접근 권한 설정**
   - 이 응답을 본인만 사용할지, 특정 그룹에서 사용할지, 아니면 모든 상담원이 사용할지 선택합니다

7. **폴더 선택**
   - Canned Response를 저장할 폴더를 선택합니다
   - 본인만 볼 수 있는 응답은 기본적으로 'Personal' 폴더에 저장됩니다

<img className="fr-dib" src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35634262/original/1KyLQ8neQVFsnelOLyOfLUjPiiovT3Z_OA.png?1509096869" data-filelink="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35634262/original/1KyLQ8neQVFsnelOLyOfLUjPiiovT3Z_OA.png?1509096869" data-fileid="35634262" data-uniquekey="1509096844785" />

8. **저장**
   - **Save** 버튼을 클릭하여 이 답변을 Canned Response로 저장합니다

생성된 Canned Response 목록은 Canned Response 페이지에서 확인할 수 있습니다. Canned Response 폴더를 만들어 적절히 분류할 수도 있습니다. 이를 통해 특정 상담원 그룹이나 전체 팀과 공유할 수 있습니다.

:::tip 활용 팁
Canned Response를 체계적으로 폴더별로 정리하면 상담원들이 필요한 템플릿을 빠르게 찾아 사용할 수 있습니다.
:::