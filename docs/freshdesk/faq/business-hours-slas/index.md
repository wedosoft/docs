---
sidebar_position: 1
---

# 비즈니스 시간 & SLAs FAQ

비즈니스 시간 & SLAs에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>What is SLA 및 how do I 생성하다 새로운 SLA policy? 는 무엇인가요?</strong></summary>

SLA (서비스 수준 계약) is agreed-upon time period within response 및/또는 resolution 되어야 합니다 provided 위해 ticket. Within Freshdesk, you 할 수 있습니다 생성하다 SLA policy 하위에서 **Admin > Workflows > SLA 정책 > Add Policy**. You 할 수 있습니다 set SLA 목표 및 set 규칙 위해 this SLA 할 것입니다 해야 합니다 apply. You 또한 have option 로 associate 특정 비즈니스 시간 함께 SLA 따라서 SLA applies 만 위해 business hour (time period).

</details>

<details>
<summary><strong>할 수 있습니다 individual SLA 정책 be set up 위해 다른 companies? ?</strong></summary>

Freshdesk has multiple SLA 정책 될 수 있습니다 set up 로 apply 로 four categories - Sources, Types, Groups, Companies, 및 Products. Kindly make sure you are 에서 **Pro** ( previously **Estate**) plan 위해 this. Please navigate 로 **Admin --> Workflows --> SLA 정책 --> Edit**, ****you 할 수 있습니다 choose option 로 have concerned SLA adhered 로 에 의해 만 특정 companies, 하위에서 section **Apply this 로 -> Companies**. ****

</details>

<details>
<summary><strong>ticket is created, does timer start right away? How 할 수 있습니다 I stop timer I respond 로 customer? ?</strong></summary>

ticket is newly created 에서 portal, default status 의 this ticket is "open. " 따라서 this is SLA timer begins 에서 ticket 및 time gets calculated 에서 ticket. response time 및 resolution time 에서 ticket are determined 에 의해 SLA policy applied 로 this ticket 및 details 의 this 될 수 있습니다 checked 에서 **Admin ->Workflows -> SLA 정책**.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008007613/original/UL4beJYOovT-u6IfVYA4Ba_8TYhvRsieRA. gif? 1680253660) you reply 로 customer 또는 wait 위해 third party 로 give you information, you 할 수 있습니다 change status 로 pending 또는 "waiting 에서 서드파티 response. " SLA timer 될 수 있습니다 switched off 위해 그러한 statuses 에서 **Admin -> Workflows -> ticket fields ->** click 에서 **status dropdown** 로 toggle off respective times next 로 these statuses.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008005673/original/D8NbLWTlIPTf-OEJLEybKCP8xeVj1wkPdQ. gif? 1680242088)

</details>

<details>
<summary><strong>How do I change Due Time 의 Ticket? 는 무엇인가요?</strong></summary>

Go 로 **Tickets tab -> click 에서 ticket**, 에서 **Ticket details page**, you'll find 'Edit' option right 위에 Subject 의 ticket.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50000625239/original/ZOcOxhP-eV2aiK4TRoD9Cm3XFU2SsmWleQ. png? 1579675221) **Note: ** 1) option 로 change due date 할 것입니다 만 show up ticket is assigned 로 statuses have **SLA timer 에서** (example: Open). You 할 수 있습니다 check statuses have their SLA timers 에서 또는 OFF 하위에서 **Admin > Workflows > Ticket Fields > Status** field. Once manual change is done 로 Due Time 의 ticket, it 할 것입니다 not change again ticket properties (위해 example, change 에서 priority) are updated. 2) due 에 의해 date 및 time 할 수 있습니다 always be updated 만 로 value greater than First response time, which is 'Response due' time 에서 ticket.

</details>

<details>
<summary><strong>What is difference 사이에 "response due" 및 "overdue"? 는 무엇인가요?</strong></summary>

ticket is created 에서 your portal, you 할 수 있습니다 set priority 로 ticket according 로 subject 및 level 의 urgency expressed 에 의해 customer. 에서 SLA policy, you 할 수 있을 것입니다 set first response time as well as resolution time. Please navigate 로 **Admin -> Workflows -> SLA 정책 -> click 에서 edit** next 로 policy. first response time is violated ticket 할 것입니다 contain **"response due"** tag 될 수 있습니다 seen you see this ticket 에서 queue within your tickets list view. resolution time violated 할 것입니다 give ticket tag called **"overdue"** 할 수 있습니다 또한 be seen you check your queue.

</details>

<details>
<summary><strong>How 로 escalate SLA violation 로 다른 group 또는 third party who is not agent? 는 무엇인가요?</strong></summary>

While configuring SLA, you 할 것입니다 또한 해야 합니다 option 로 set up escalation 규칙, 할 것입니다 send out notifications 로 chosen agents, whenever configured SLA is violated. This 될 수 있습니다 set up 하위에서 **Admin > Workflows > SLA 정책 > Edit >"What happens this SLA is violated? "**you 할 수 있습니다 add multiple levels 의 escalation. 하지만, 만 agents(any agent within your Freshdesk Account, 심지어 에서 다른 group) 에서 your account 될 수 있습니다 added 하위에서 this section 및 third parties 할 수 있습니다 not be added.

</details>

<details>
<summary><strong>Is private note counted as response 하위에서 SLA 정책? 는 무엇인가요?</strong></summary>

에서 Agent's point 의 view, 만 **reply 또는 public note 할 것입니다** be classified as response. These are ones 될 수 있습니다 viewed 에서 ticket 에 의해 customer 및 response time 될 것입니다 calculated based 에서 this. SLA policy 및 timer is tied 로 response sent 에 의해 agent 에서 ticket. **private note** isn't visible 로 customer 및 hence wouldn't be considered 로 be response/first response 의 의 agent.

</details>

<details>
<summary><strong>How 로 send escalation emails 로 unresponsive agents? 는 무엇인가요?</strong></summary>

Escalations 할 수 있습니다 crop up 위해 많은 reasons, like miscommunication 함께 agents, technical delays, missed SLAs, etc. It is essential 로 set up right processes 및 mechanisms 로 effectively manage escalations 및 prevent them 에서 achieving great customer experience. Freshdesk enables you 로 구성하다 **Escalation 규칙** 및 **Supervisor 규칙** agent has not sent first response within set time. ## **Escalation 규칙** Please follow steps 아래에 로 구성하다 Escalation 규칙 하위에서 SLA 정책. - Navigate 로 Admin. Select Workflows 및 click 에서 SLA 정책. - Click 에서 Edit next 로 SLA Policy you wish 로 set up escalation rule. - 하위에서 Send escalation SLA is violated section, click 에서 Add 새로운 escalations. - Now, select First response target is not met escalate immediately (또는 select any preferred time interval) 로 Assigned agent (및/또는 Supervisor). - Click 에서 Save.! [How 로 set up escalation 규칙 위해 unresponsive agents 통해 SLA Policy settings? ](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008578235/original/XIHrBsX4Vy64l6QzUHX--CtjgzCRUsuE5A. gif? 1686305539) ## **Supervisor 규칙** You 할 수 있습니다 또한 set up Supervisor 규칙 통해 automations, enabling you 로 사용자 정의하다 your escalation email sent 로 agent’s supervisor. Here is how you 할 수 있습니다 do it. - Navigate 로 Admin 에서 menu. 하위에서 Workflows, click 에서 Automations. - **Choose Tickets tab 및 then Hourly Triggers** (FKA Time Triggers). - Click 에서 새로운 Rule button 및 provide rule name. - 하위에서 에서 tickets 함께 these properties: section, click 에서 Match 모든 의 아래에 option. - Select 에서 Tickets, if Hours since first response due, Greater than 1. - Click 에서 Add 새로운 condition. - Then, select 에서 Tickets, if Hours since first response due, 덜 than 2. - 하위에서 Perform these actions: section, select Send email 로 agent option 에서 dropdown. - 사용자 정의하다 your email 함께 dynamic content using Insert Placeholder option. - Click 에서 Preview 및 Save 및 then Save 및 활성화.! [How 로 send escalation emails 로 unresponsive agents 통해 automations 에서 Freshdesk? ](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008578246/original/03_DiKGWk89fQF78ffYbHj251aKtPPBvCA. gif? 1686305582) Please reach out 로 [support@freshdesk. com](mailto: support@freshdesk. com) if you require further assistance.

</details>

<details>
<summary><strong>agent is attributed 하위에서 Tickets resolved/Resolution metric there are multiple agents working 에서 특정 ticket? 는 무엇인가요?</strong></summary>

Tickets resolved metric 될 것입니다 attributed 로 **"****Assigned agent 의 ticket"**, irrespective 의 ticket is resolved 또는 closed 에 의해. 위해 example, if ticket #100 is assigned 로 **Agent A, ** 및 is marked as 'Resolved' 에 의해 **Agent B**- then resolved count 위해 this ticket 될 것입니다 attributed 로 **Agent A. **

</details>

<details>
<summary><strong>How 로 구성하다 비즈니스 시간? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 구성하다 비즈니스 시간 에서 your account, based 에서 your active time period 위해 각 day 의 week. This 될 수 있습니다 done 에서 하위에서 **Admin > Service Management > Service desk settings > 비즈니스 시간 > Edit** 및 change 하위에서 "비즈니스 시간".! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50009501117/original/EcK_NQYihexvvPNaO28Xrl1tcTuMo2Nkgg. png? 1695116728) Once this is done, you 할 수 있습니다 associate SLA 로 work based 에서 비즈니스 시간.

</details>

<details>
<summary><strong>How 로 set holidays 및 change calendar holidays 로 working day? 는 무엇인가요?</strong></summary>

Effectively managing holidays 및 configuring calendar is essential 위해 maintaining efficient support operations. **Article Navigation** - Setting Holidays - Changing Calendar Holidays ## **Setting Holidays** 로 set holidays 에서 your Freshdesk Business Calendar, follow these 간단한 steps: - Go 로 **Admin > Team > 비즈니스 시간**. - Click 에서 your configured 비즈니스 시간 로 edit it. - Select **Holidays** tab 및 click 에서 **Add Holidays**. - Enter **date** 및 **name** 하위에서 **Exclusive** 또는 **Regional Holidays** category as per your requirement 및 click **Add**. - Click **Save**로 확인하다 your changes.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008742392/original/waOoMHT41oDnbVWti_vmixqHX516ctN92A. png? 1687943383) Once you have added holiday 로 your Freshdesk Business Calendar, it 될 것입니다 marked as non-working day 에서 your calendar. ## **Changing Calendar Holidays** If you 해야 합니다 change calendar holiday 로 working day, you 할 수 있습니다 do 따라서 에 의해 following these steps: - Go 로 **Admin > Team > 비즈니스 시간**. - Click 에서 your configured 비즈니스 시간 로 edit it. - Select **Holidays** tab 및 find holiday you 하고 싶습니다 change. - Click 에서 **Remove** button next 로 holiday. - Click 에서 **Save** 로 확인하다 changes.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008742409/original/VgbFOmAr6wdX884O2Lmg4tUsH2pzIv35Ww. png? 1687943491) Removing holiday 에서 your Freshdesk Business Calendar 될 것입니다 marked as working day 에서 your calendar. yearly holiday list needs 로 be updated annually. Custom leaves allocated 위해 current year cannot be carried forward 로 future years. 로 보장하다 accurate holiday configurations, it is necessary 로 업데이트 holiday list 각 year manually.

</details>

<details>
<summary><strong>How do I change Helpdesk's TimeZone? 는 무엇인가요?</strong></summary>

Please navigate 로**Admin -> Account -> Helpdesk Settings**로 see option 로 change time zone. Kindly change it 함께 respect 로 your location 및 it 할 것입니다 reflect 에서 your portal.

</details>

<details>
<summary><strong>How do I change my Agent Profile's TimeZone? 는 무엇인가요?</strong></summary>

Please navigate 로 프로필 설정 에 의해 clicking 에서 your Agent Avatar 에서 top-right corner 의 your Freshdesk Account. You 할 수 있습니다 then change Time Zone 에 의해 choosing it 에서 corresponding dropdown. Multiple Timezone 기능 is 사용 가능 만 에서 the**Pro** (previously **Estate**) Plan 에서 Freshdesk. 따라서, you 할 것입니다 not be able 로 make this change 에서 Free Sprout 또는 Blossom plans.

</details>

<details>
<summary><strong>할 것입니다 reopening 의 Resolved ticket count against Average Resolution time? 는 무엇인가요?</strong></summary>

Yes, 모든 time ticket is moved 로 status SLA timer is toggled 에서, it 할 것입니다 affect **Response** 및 **Resolution time** 의 ticket. Please navigate 로 **Admin > Workflows > Ticket Fields > Status**statuses have SLA timer have been toggled 에서 될 수 있습니다 viewed.

</details>

<details>
<summary><strong>Is it possible 로 display clock 에서 24-hour time format? 는 무엇인가요?</strong></summary>

As 의 now, Freshdesk does not have option 로 have **Time Format** 로 be 사용 가능 에서 **24-hour** format.

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
