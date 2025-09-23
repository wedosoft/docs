---
sidebar_position: 1
---

# 업무 시간 및 SLA FAQ

업무 시간 및 SLA에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>SLA 그리고 생성 new SLA policy?하는 방법이란은 무엇인가요?</strong></summary>

SLA (서비스 Level Agreement) is agreed-upon time period within which response 그리고/또는 resolution should be provided 위해 ticket. Within Freshdesk, you can 생성 SLA policy under **관리자 > Workflows > SLA policies > 추가 Policy**. You can set SLA Targets 그리고 set rules 위해 which this SLA will have 로 apply. You also have option 로 associate 특정한 Business Hours 와 함께 SLA so that SLA applies only 위해 that business hour (time period).

</details>

<details>
<summary><strong>Can individual SLA policies be set up 위해 different 회사?</strong></summary>

Freshdesk has 다수의 SLA policies that could be set up 로 apply 로 four categories - Sources, Types, Groups, 회사, 그리고 Products. Kindly make sure you are 에 **Pro** ( previously **Estate**) 요금제 위해 this. Please 이동 로 **관리자 --> Workflows --> SLA policies --> 편집**,****where you can 선택 option 로 have concerned SLA adhered 로 에 의해 only 특정한 회사, under section **Apply this 로 -> 회사**.****

</details>

<details>
<summary><strong>언제 ticket is created, does timer start right away? stop timer when I respond 로 고객?하는 방법은 무엇인가요?</strong></summary>

언제 ticket is newly created 에 포털, 기본값 status 의 this ticket is "open." So this is when SLA timer begins 에 ticket 그리고 time gets calculated 에 ticket. response time 그리고 resolution time 에 ticket are determined 에 의해 SLA policy applied 로 this ticket 그리고 details 의 this could be checked 에서 **관리자 ->Workflows -> SLA policies**. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008007613/original/UL4beJYOovT-u6IfVYA4Ba_8TYhvRsieRA.gif?1680253660) 언제 you reply 로 고객 또는 wait 위해 third party 로 give you information, you could change status 로 pending 또는 "waiting 에 third-party response." SLA timer could be switched off 위해 such statuses 에서 **관리자 -> Workflows -> ticket fields ->** 클릭 에 **status dropdown** 로 toggle off respective times next 로 these statuses. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008005673/original/D8NbLWTlIPTf-OEJLEybKCP8xeVj1wkPdQ.gif?1680242088)

</details>

<details>
<summary><strong>change Due Time 의 Ticket?하는 방법은 무엇인가요?</strong></summary>

Go 로 **티켓 tab -> 클릭 에 ticket**, 에서 **Ticket details page**, you'll find '편집' option right above Subject 의 ticket. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50000625239/original/ZOcOxhP-eV2aiK4TRoD9Cm3XFU2SsmWleQ.png?1579675221) **참고:** 1) option 로 change due date will only show up 언제 ticket is assigned 로 statuses that have **SLA timer 에** (example: Open). You can 확인하다 which statuses have their SLA timers 에 또는 OFF under **관리자 > Workflows > Ticket Fields > Status** 필드. Once 수동 change is done 로 Due Time 의 ticket, it will not change again 언제 ticket properties (위해 example, change 에서 priority) are updated. 2) due 에 의해 date 그리고 time can always be updated only 로 value greater than First response time, which is 'Response due' time 에 ticket.

</details>

<details>
<summary><strong>difference between "response due" 그리고 "overdue"?이란은 무엇인가요?</strong></summary>

언제 ticket is created 에서 your 포털, you could set priority 로 ticket according 로 subject 그리고 level 의 urgency expressed 에 의해 고객. 에서 SLA policy, you would be able 로 set first response time as well as resolution time. Please 이동 로 **관리자 -> Workflows -> SLA policies -> 클릭 에 편집** next 로 policy. 언제 first response time is violated ticket would contain **"response due"** tag which could be seen when you see this ticket 에서 queue within your 티켓 list view. resolution time 언제 violated would give ticket tag called **"overdue"** which can also be seen when you 확인하다 your queue.

</details>

<details>
<summary><strong>escalate SLA violation 로 another group 또는 third party who is not agent?하는 방법은 무엇인가요?</strong></summary>

While configuring SLA, you would also have 로 option 로 set up escalation rules, which would send out notifications 로 chosen 상담원, whenever configured SLA is violated. This could be set up under **관리자 > Workflows > SLA Policies > 편집 >"What happens 언제 this SLA is violated?"**where you could 추가 다수의 levels 의 escalation. However, only 상담원(any agent within your Freshdesk 계정, even 에서 different group) 에서 your 계정 could be added under this section 그리고 third parties could not be added.

</details>

<details>
<summary><strong>Is private 참고 counted as response under SLA policies?</strong></summary>

에서 Agent's point 의 view, only **reply 또는 public 참고 will** be classified as response. These are ones that could be viewed 에 ticket 에 의해 고객 그리고 response time would be calculated based 에 this. SLA policy 그리고 timer is tied 로 response sent 에 의해 agent 에 ticket. **private 참고** isn't visible 로 고객 그리고 hence wouldn't be considered 로 be response/first response 의 that 의 agent.

</details>

<details>
<summary><strong>send escalation emails 로 unresponsive 상담원?하는 방법은 무엇인가요?</strong></summary>

Escalations can crop up 위해 many reasons, like miscommunication 와 함께 상담원, technical delays, missed SLAs, etc. It is 필수적인 로 set up right processes 그리고 mechanisms 로 effectively manage escalations 그리고 prevent them 에서 achieving great 고객 experience. Freshdesk enables you 로 configure **Escalation Rules** 그리고 **Supervisor Rules** 언제 agent has not sent first response within set time. **Escalation Rules** Please follow steps below 로 configure Escalation Rules under SLA Policies. - 이동 로 관리자. 선택 Workflows 그리고 클릭 에 SLA Policies. - 클릭 에 편집 next 로 SLA Policy you wish 로 set up escalation rule. - Under Send escalation 언제 SLA is violated section, 클릭 에 추가 new escalations. - Now, 선택 When First response target is not met escalate immediately (또는 선택 any preferred time interval) 로 Assigned agent (그리고/또는 Supervisor). - 클릭 에 저장. ![set up escalation rules 위해 unresponsive 상담원 through SLA Policy 설정?하는 방법](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008578235/original/XIHrBsX4Vy64l6QzUHX--CtjgzCRUsuE5A.gif?1686305539) **Supervisor Rules** You can also set up Supervisor Rules through automations, enabling you 로 사용자 정의하다 your escalation 이메일 sent 로 agent’s supervisor. Here is how you can do it. - 이동 로 관리자 에서 menu. Under Workflows, 클릭 에 Automations. - **선택 티켓 tab 그리고 그러면 Hourly Triggers** (FKA Time Triggers). - 클릭 에 New Rule button 그리고 제공하다 rule name. - Under 에 티켓 와 함께 these properties: section, 클릭 에 Match ALL 의 below option. - 선택 에서 티켓, 만약 Hours since first response due, Greater than 1. - 클릭 에 추가 new condition. - 그러면, 선택 에서 티켓, 만약 Hours since first response due, Less than 2. - Under Perform these actions: section, 선택 Send 이메일 로 agent option 에서 dropdown. - 사용자 정의하다 your 이메일 와 함께 dynamic content using Insert Placeholder option. - 클릭 에 Preview 그리고 저장 그리고 그러면 저장 그리고 활성화. ![send escalation emails 로 unresponsive 상담원 through automations 에서 Freshdesk?하는 방법](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008578246/original/03_DiKGWk89fQF78ffYbHj251aKtPPBvCA.gif?1686305582) Please 문의하다 로 [지원@freshdesk.com](mailto:지원@freshdesk.com) 만약 you require further assistance.

</details>

<details>
<summary><strong>Which agent is attributed under 티켓 resolved/Resolution metric 언제 there are 다수의 상담원 working 에 particular ticket?</strong></summary>

티켓 resolved metric will be attributed 로 **"****Assigned agent 의 ticket"**, irrespective 의 who ticket is resolved 또는 closed 에 의해. 위해 example, 만약 ticket #100 is assigned 로 **Agent ,** 그리고 is marked as 'Resolved' 에 의해 **Agent B**- 그러면 resolved count 위해 this ticket will be attributed 로 **Agent .**

</details>

<details>
<summary><strong>configure business hours?하는 방법은 무엇인가요?</strong></summary>

You could configure Business Hours 에 your 계정, based 에 your active time period 위해 each day 의 week. This could be done 에서 under **관리자 > 서비스 Management > 서비스 desk 설정 > Business Hours > 편집** 그리고 change under "Business Hours". ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50009501117/original/EcK_NQYihexvvPNaO28Xrl1tcTuMo2Nkgg.png?1695116728) Once this is done, you could associate SLA 로 work based 에 Business Hours.

</details>

<details>
<summary><strong>set holidays 그리고 change calendar holidays 로 working day?하는 방법은 무엇인가요?</strong></summary>

Effectively managing holidays 그리고 configuring calendar is 필수적인 위해 maintaining efficient 지원 operations. **Article Navigation** - [Setting Holidays](#Setting-Holidays) - [Changing Calendar Holidays](#Changing-Calendar-Holidays) **Setting Holidays** 로 set holidays 에 your Freshdesk Business Calendar, follow these simple steps: - Go 로 **관리자 > 팀 > Business Hours**. - 클릭 에 your configured Business Hours 로 편집 it. - 선택 **Holidays** tab 그리고 클릭 에 **추가 Holidays**. - 입력 **date** 그리고 **name** under **Exclusive** 또는 **Regional Holidays** category as per your requirement 그리고 클릭 **추가**. - 클릭 **저장**로 confirm your changes. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008742392/original/waOoMHT41oDnbVWti_vmixqHX516ctN92A.png?1687943383) Once you have added holiday 로 your Freshdesk Business Calendar, it will be marked as non-working day 에 your calendar. **Changing Calendar Holidays** 만약 you need 로 change calendar holiday 로 working day, you can do so 에 의해 following these steps: - Go 로 **관리자 > 팀 > Business Hours**. - 클릭 에 your configured Business Hours 로 편집 it. - 선택 **Holidays** tab 그리고 find holiday you want 로 change. - 클릭 에 **제거** button next 로 holiday. - 클릭 에 **저장** 로 confirm changes. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008742409/original/VgbFOmAr6wdX884O2Lmg4tUsH2pzIv35Ww.png?1687943491) Removing holiday 에서 your Freshdesk Business Calendar will be marked as working day 에 your calendar. yearly holiday list needs 로 be updated annually. 사용자 정의 leaves allocated 위해 current year cannot be carried forward 로 future years. 로 확인하다 accurate holiday configurations, it is necessary 로 업데이트 holiday list each year manually.

</details>

<details>
<summary><strong>change 헬프데스크's TimeZone?하는 방법은 무엇인가요?</strong></summary>

Please 이동 로**관리자 -> 계정 -> 헬프데스크 설정**로 see option 로 change time zone. Kindly change it 와 함께 respect 로 your location 그리고 it would reflect 에서 your 포털.

</details>

<details>
<summary><strong>change my Agent Profile's TimeZone?하는 방법은 무엇인가요?</strong></summary>

Please 이동 로 Profile 설정 에 의해 clicking 에 your Agent Avatar 에서 top-right corner 의 your Freshdesk 계정. You could 그러면 change Time Zone 에 의해 choosing it 에서 corresponding dropdown. 다수의 Timezone feature is 사용 가능한 only 에서 **Pro** (previously **Estate**) 요금제 에서 Freshdesk. So, you would not be able 로 make this change 에 Free Sprout 또는 Blossom 요금제.

</details>

<details>
<summary><strong>Will reopening 의 Resolved ticket count against Average Resolution time?</strong></summary>

Yes, every time ticket is moved 로 status where SLA timer is toggled 에, it will affect **Response** 그리고 **Resolution time** 의 ticket. Please 이동 로 **관리자 > Workflows > Ticket Fields > Status**where statuses which have SLA timer have been toggled 에 could be viewed.

</details>

<details>
<summary><strong>display clock 에서 24-hour time format?할 수 있나요은 무엇인가요?</strong></summary>

As 의 now, Freshdesk does not have option 로 have **Time Format** 로 be 사용 가능한 에서 **24-hour** format.

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
