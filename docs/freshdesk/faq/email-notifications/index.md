---
sidebar_position: 1
---

# 이메일 알림 FAQ

이메일 알림에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>활성화 또는 비활성화 이메일 notifications?하는 방법은 무엇인가요?</strong></summary>

You can 활성화 또는 비활성화 이메일 notifications 위해 wide range 의 workflows within Freshdesk 와 함께 simple 클릭 의 button. Here's how you do it. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - You will notice that there are four types 의 notifications 에 this page. - Agent Notifications alert agent 언제 고객 replies 로 ticket, when ticket is assigned 로 agent, 그리고 so 에 - Requester Notifications alert 고객 언제 agent solves ticket, closes ticket, sends 비밀번호 reset 이메일, 그리고 so 에. - CC Notifications alert 이메일 addresses added 에서 CC 필드 언제 new ticket is created 또는 when public 참고 is added. - 그리고 Reply Templates 사용자 정의하다 그리고 prefill 기본값 information 에서 agent ticket replies, such as dynamic content like requestor name, ticket URLs, 그리고 agent signatures. - You can toggle 에/OFF green button next 로 any 이메일 notification 로 활성화 또는 비활성화 them. ![활성화 또는 비활성화 이메일 notifications 에서 Freshdesk.하는 방법](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008501686/original/o2mrEyl2OAaTuHNESNkrQE9QzcptVjBmAQ.gif?1685598848)

</details>

<details>
<summary><strong>왜 am I, as agent, not getting notifications 언제 new ticket is created?</strong></summary>

"**New ticket created"**agent notification 이메일 can be set 로 be sent 로 상담원 whenever ticket is created 에서 your Freshdesk 계정. This can be configured under **관리자 > Workflows > 이메일 Notifications > Agent Notifications > New Ticket****Created****.** ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/42332575/original/4ceZtAwQe62jZk_JQE_IIkZSdX9MKBh4tQ.png?1544759157) 만약 상담원 do not receive this 이메일, kindly 확인하다 만약 it is toggled 에. Further, Only 상담원 whose names are added under '**Notify 상담원'**section would receive this 이메일 each time ticket is created. You can 추가 as many numbers 의 상담원 under this section. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/42332497/original/hciQaX6ral6jP6UjAZR0N4KDEusyLwzSeA.png?1544758747)**Similar articles****[](https://지원.freshdesk.com//solutions/articles/220676?lang=en&portalId=2)**[](https://지원.freshdesk.com//solutions/articles/220676?lang=en&portalId=2)[Configuring 이메일 notifications](https://지원.freshdesk.com//solutions/articles/220676?lang=en&portalId=2)[](https://지원.freshdesk.com//solutions/articles/220676?lang=en&portalId=2)**[](https://지원.freshdesk.com//solutions/articles/220676?lang=en&portalId=2)**

</details>

<details>
<summary><strong>왜 are my requesters receiving two emails notifications 언제 new ticket is created?</strong></summary>

Apart 에서 기본값 **New ticket 이메일 notification**(관리자 > Workflows > 이메일 notifications > Requester notifications), there might be **Ticket creation automation****rule**(관리자 > Workflows > Automation > ticket creation) that sends 이메일 every time new ticket is created 로 requester. Please 확인하다 에 reported ticket's[Show Activities](https://지원.freshdesk.com/en/지원/solutions/articles/37589-viewing-ticket-activity-history) 로 see 만약 there was any automation rule executed 에 that ticket. You can 이동 로 corresponding automation rule 에 의해 clicking 에 rule link 위해 that activity. 에서 within automation rule, 확인하다 만약 there is action *'Send 이메일 로 requester'* within rule. 만약 so, you can 제거 this action 또는 추가 another action *'Skip new ticket 이메일 notification* 로 automation rule, 로 prevent notification 이메일 duplication 에서 cases where this automation rule is triggered 에 티켓.

</details>

<details>
<summary><strong>stop my users 에서 receiving 이메일 로 sign up 위해 포털?하는 방법은 무엇인가요?</strong></summary>

로 turn off this sign up 이메일 에서 being sent 로 requesters, please go 로 **관리자 --> Workflows --> 이메일 Notifications****--> Requestor notifications** 그리고 turn off **User activation 이메일.**

</details>

<details>
<summary><strong>편집 자동 이메일 notifications?하는 방법은 무엇인가요?</strong></summary>

Using Freshdesk’s 자동 이메일 notifications, you can prioritize your work 그리고 be aware 의 new 티켓, 고객 responses, 그리고 much more 에서 within your 헬프데스크. Please follow below steps 로 편집 이메일 notifications 로 사용자 정의하다 them per your business requirement. - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - 클릭 에 편집 icon next 로 any 이메일 notification. - You can make use 의 “Insert Placeholder” option 로 추가 dynamic content 그리고 personalize 이메일 subject 그리고 its content. - 클릭 저장. ![편집 자동 이메일 notification 그리고 추가 dynamic content 에서 Freshdesk.하는 방법](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008501704/original/j2l7ZoY-23lOdDPk3etCzrtejtZisKTeHA.gif?1685598955)

</details>

<details>
<summary><strong>notify 고객 언제 ticket is closed 또는 resolved?하는 방법은 무엇인가요?</strong></summary>

로 notify 고객 언제 ticket is closed 또는 resolved, please 이동 로 **관리자 --> Workflows --> 이메일 Notifications -->Requester Notification-->Turn 에** notification 위해 **Agent closes ticket** 그리고 **Agent Resolves ticket**. This would send notification 이메일 whenever ticket raised 에 의해 them is marked as Resolved/Closed.

</details>

<details>
<summary><strong>stop ticket closure notification 위해 특정한 ticket?하는 방법은 무엇인가요?</strong></summary>

There could be instances where you would like 로 close 특정한 티켓 without notifying requester that ticket was closed. 에서 such cases, you could 클릭 에 ticket 에서 티켓 list, which would take you 로 ticket details page. Within ticket details page, 로 top, you would find "Close" option. You could 클릭 에 "Shift" key 그리고 simultaneously 클릭 에 Close option. This would close that particular ticket, without sending out 기본값 notification 위해 언제 "Agent Closes Ticket", 로 requester.

</details>

<details>
<summary><strong>set up 이메일 notifications 그리고 reminders 위해 SLA violation?하는 방법은 무엇인가요?</strong></summary>

SLAs 에서 고객 지원 서비스 are time-based deadlines agreed upon 에 의해 고객 그리고 outlined 에서 contracts 또는 terms 의 서비스. After you [set up SLA 에서 your Freshdesk](https://지원.freshdesk.com/en/지원/solutions/folders/273282) 계정, you can configure SLA reminders 그리고 SLA violation notifications 로 alert 상담원 의 upcoming SLA breaches. Please follow steps below 로 set up first response SLA notification 이메일 그리고 resolution SLA notification emails. - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu 그리고 선택 Workflows. 클릭 에 이메일 Notifications. - Under Agent Notifications tab, turn 에 following notifications based 에 your requirements First Response SLA reminder, Time SLA reminder, First Response SLA violation, 그리고 Resolution Time SLA violation notifications. ![Set up 이메일 notifications 그리고 reminders 위해 SLA violation](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008539466/original/ApBBWnm42xjSepPpF09AGnDzbNxCFxTyvQ.gif?1686035655)

</details>

<details>
<summary><strong>notify customers 언제 agent adds public 참고?하는 방법은 무엇인가요?</strong></summary>

Your Freshdesk 계정 comes equipped 와 함께 기본값 automation rule 로 notify customers 언제 agent adds public 참고 로 their ticket. This helps bring agent's response 로 고객's attention immediately 그리고 keeps them informed 의 progress 에서 their 문제. Please follow below steps 로 활성화 automation rule 로 notify customers 언제 agent adds public 참고. - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - Under Requester Notifications tab, turn 에 Agent Adds Comment 로 Ticket notification. ![Notifying customers 언제 agent adds public 참고](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008479467/original/0mmqXssoFG0WlkWPD58q69W2YmuwMKCpmA.gif?1685436172) - 클릭 **편집** 로 사용자 정의하다 subject 그리고 description 의 이메일.

</details>

<details>
<summary><strong>prevent 이메일 notifications 위해 merged 티켓?하는 방법은 무엇인가요?</strong></summary>

언제 **merging**2 티켓, you can prevent 이메일 notification 에서 being sent 로 customers that ticket has been closed. While merging 티켓 에서 Freshdesk, there is option 로 set as**Not visible 로 연락하다**, choosing which, merge action will not be notified 로 customers. This has 로 be enabled 에서 all 티켓 that are being merged into one, i.e., original ticket as well as ticket(s) being merged. You can also 편집 content 의 참고 에 의해 clicking 에 **편집 참고**option****as shown below: ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/40834312/original/b87gaInqAEPCKaYt1NuOL6qUOEqcHzej5A.png?1537320737) ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/42278121/original/ZBxLb5slf6Tq-MlNHB1CUxghUl0fCAdjWQ.png?1544587154)

</details>

<details>
<summary><strong>set up agent reply templates?하는 방법은 무엇인가요?</strong></summary>

template helps maintain standard 의 지원 replies across large 지원 팀. Typically, agent reply template has greetings 그리고 signatures, so 상담원 needn’t spend time 에 them 하지만 instead concentrate 에 solving 문제. templates can also contain pre-written answers 위해 특정한 지원 scenarios, like refund requests, etc. Please follow below steps 로 set up agent reply templates 에서 Freshdesk. - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - Under Templates tab, 클릭 에 편집 icon next 로 Agent Reply Template. - You can make use 의 “Insert Placeholder” option 로 추가 dynamic content 로 Reply editor 그리고 personalize agent replies. - 클릭 저장. ![set up agent reply template 에서 Freshdesk.하는 방법](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008538791/original/--3dhUDm56nx00GAxvrSa2a6vAX-7_4VnA.gif?1686032239) Here is youtube video 와 함께 detailed demonstration providing 특정한 examples 위해 참고 자료: setting up agent reply templates 로 help you get started.

</details>

<details>
<summary><strong>설정 자동 이메일 response 로 customers 위해 new 티켓?하는 방법은 무엇인가요?</strong></summary>

이메일 notification templates 에서 Freshdesk allow you 로 사용자 정의하다 unique, 고객-centric notification emails. Freshdesk comes equipped 와 함께 기본값 이메일 notification that automatically responds 로 customers 언제 they 생성 ticket. You can 편집 message 그리고 subject 의 notification 로 suit your business needs. Please follow steps below 로 편집 또는 사용자 정의하다 New Ticket Created notification. - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - Under Requester Notifications tab, 클릭 에 편집 button next 로 any New Ticket Created notification. - Make necessary modifications 그리고 클릭 에 저장. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50011320075/original/r9ax5qZ0IcAPtOFl1skS4VEUwPDUGBxzcQ.gif?1711102145) **참고:** You can 편집 Message 또는 Subject 의 notification 그리고 저장 it 로 send 사용자 정의 notification 로 requesters.

</details>

<details>
<summary><strong>I am not getting notified 언제 I am assigned 에 ticket. Please help.은 무엇인가요?</strong></summary>

로 notify 상담원 에 new ticket assignment, - Go 로 **관리자 > Workflows > 이메일 Notifications > Agent notifications** - Toggle 에 notification 위해 "Ticket assigned 로 agent" ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008005664/original/Fa9vN54fw4RSPpzl23ScjYTjNlWr0YYfhQ.gif?1680241886) After enabling notifications, 만약 상담원 are not notified 의 티켓 assigned 로 them, write 로 **지원@freshdesk.com** 위해 further help**.**

</details>

<details>
<summary><strong>Is there any way 로 see automated responses 고객 receives 위해 ticket ?</strong></summary>

automated response 고객 receives after ticket is created is 기본값 이메일 notification you have set up under **관리자 > Workflows > 이메일 Notifications > Requester Notification > New ticket created**. You can 편집 subject 의 notification 로 your preference. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008005666/original/zYRPEY0NJDyRTzzpfsZK-_RmQw_WrRaQpw.gif?1680241963)

</details>

---

## 🔗 관련 자료

추가적인 도움이 필요하시면 다음 자료들을 참고해 주세요:

- [Freshdesk 도움말 센터](https://support.freshdesk.com)
- [커뮤니티 포럼](https://community.freshworks.com)
- [고객지원팀 문의](mailto:support@freshdesk.com)

:::tip 도움말
더 자세한 정보나 개별 상담이 필요하시면 고객지원팀으로 연락해 주세요.
:::
