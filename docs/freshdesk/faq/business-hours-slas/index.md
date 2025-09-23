---
sidebar_position: 1
---

# 업무 시간 및 SLA FAQ

업무 시간 및 SLA에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>an SLA and how do I create a new SLA policy은 무엇인가요?</strong></summary>

An SLA (서비스 Level Agreement) is an agreed-upon time period within which a response and/or resolution should be provided for a ticket.Within Freshdesk, you can create an SLA policy under **관리자 > Workflows > SLA policies > Add Policy**. You can set the SLA Targets and set rules for which this SLA will have to apply.You also have the option to associate specific Business Hours with the SLA so that the SLA applies only for that business hour (time period).

</details>

<details>
<summary><strong>Can individual SLA policies be set up for different companies?</strong></summary>

Freshdesk has multiple SLA policies that could be set up to apply to four categories - Sources, Types, Groups, Companies, and Products. Kindly make sure you are on the **Pro** ( previously **Estate**) 요금제 for this.Please navigate to **관리자 --> Workflows --> SLA policies --> Edit**,** **where you can choose the option to have the concerned SLA adhered to by only specific companies, under the section **Apply this to -> Companies**. ****

</details>

<details>
<summary><strong>언제 a ticket is created, does the timer start right away? How can I stop the timer when I respond to a 고객인가요?</strong></summary>

When a ticket is newly created on the 포털, the default status of this ticket is "open." So this is when the SLA timer begins on the ticket and the time gets calculated on the ticket. The response time and resolution time on a ticket are determined by the SLA policy applied to this ticket and the details of this could be checked in **관리자 ->Workflows -> SLA policies**.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008007613/original/UL4beJYOovT-u6IfVYA4Ba_8TYhvRsieRA.gif?1680253660)When you reply to a 고객 or wait for a third party to give you information, you could change the status to pending or "waiting on third-party response." The SLA timer could be switched off for such statuses in **관리자 -> Workflows -> ticket fields ->** click on the **status dropdown** to toggle off the respective times next to these statuses.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008005673/original/D8NbLWTlIPTf-OEJLEybKCP8xeVj1wkPdQ.gif?1680242088)

</details>

<details>
<summary><strong>change the Due Time of a Ticket하는 방법은 무엇인가요?</strong></summary>

Go to the **티켓 tab -> click on a ticket**, in the **Ticket details page**, you'll find the 'Edit' option right above the Subject of the ticket.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50000625239/original/ZOcOxhP-eV2aiK4TRoD9Cm3XFU2SsmWleQ.png?1579675221)**참고:**1) The option to change the due date will only show up when the ticket is assigned to statuses that have the **SLA timer ON** (example: Open).You can check which statuses have their SLA timers ON or OFF under **관리자 > Workflows > Ticket Fields > Status** field. Once a manual change is done to the Due Time of a ticket, it will not change again when the ticket properties (for example, a change in priority) are updated.2) The due by date and time can always be updated only to a value greater than the First response time, which is the 'Response due' time on the ticket.

</details>

<details>
<summary><strong>the difference between "response due" and "overdue"은 무엇인가요?</strong></summary>

When a ticket is created in your 포털, you could set a priority to the ticket according to the subject and level of urgency expressed by the 고객. In the SLA policy, you would be able to set a first response time as well as resolution time. Please navigate to **관리자 -> Workflows -> SLA policies -> click on edit** next to the policy.When the first response time is violated the ticket would contain a **"response due"** tag which could be seen when you see this ticket in the queue within your 티켓 list view.The resolution time when violated would give the ticket a tag called **"overdue"** which can also be seen when you check your queue.

</details>

<details>
<summary><strong>escalate SLA violation to another group or third party who is not an agent하는 방법은 무엇인가요?</strong></summary>

While configuring SLA, you would also have to option to set up escalation rules, which would send out notifications to the chosen 상담원, whenever the configured SLA is violated. This could be set up under **관리자 > Workflows > SLA Policies > Edit >"What happens when this SLA is violated?" **where you could add multiple levels of escalation.However, only 상담원(any agent within your Freshdesk 계정, even from a different group) in your 계정 could be added under this section and third parties could not be added.

</details>

<details>
<summary><strong>Is a private 참고 counted as a response under SLA policies?</strong></summary>

From an Agent's point of view, only a **reply or a public 참고 will** be classified as a response. These are the ones that could be viewed on a ticket by a 고객 and the response time would be calculated based on this.SLA policy and timer is tied to the response sent by an agent on a ticket. A **private 참고** isn't visible to the 고객 and hence wouldn't be considered to be a response/first response of that of an agent.

</details>

<details>
<summary><strong>send escalation emails to unresponsive 상담원하는 방법은 무엇인가요?</strong></summary>

Escalations can crop up for many reasons, like miscommunication with 상담원, technical delays, missed SLAs, etc. It is essential to set up the right processes and mechanisms to effectively manage escalations and prevent them from achieving a great 고객 experience.Freshdesk enables you to configure **Escalation Rules** and **Supervisor Rules** when an agent has not sent the first response within a set time.
**Escalation Rules**
Please follow the steps below to configure Escalation Rules under SLA Policies.-
Navigate to 관리자. Select Workflows and click on SLA Policies.-
Click on Edit next to the SLA Policy you wish to set up the escalation rule.-
Under the Send escalation when the SLA is violated section, click on Add new escalations.-
Now, select When First response target is not met escalate immediately (or select any preferred time interval) to Assigned agent (and/or the Supervisor).-
Click on Save.![How to set up escalation rules for unresponsive 상담원 through SLA Policy 설정?](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008578235/original/XIHrBsX4Vy64l6QzUHX--CtjgzCRUsuE5A.gif?1686305539)**Supervisor Rules**
You can also set up Supervisor Rules through automations, enabling you to customize your escalation 이메일 sent to the agent’s supervisor. Here is how you can do it.-
Navigate to 관리자 from the menu. Under Workflows, click on Automations.-
**Choose the 티켓 tab and then Hourly Triggers** (FKA Time Triggers).-
Click on the New Rule button and provide a rule name.-
Under the On 티켓 with these properties: section, click on Match ALL of the below option.-
Select In 티켓, if Hours since first response due, Greater than 1.-
Click on Add new condition.-
Then, select In 티켓, if Hours since first response due, Less than 2.-
Under the Perform these actions: section, select Send 이메일 to agent option from the dropdown.-
Customize your 이메일 with dynamic content using Insert Placeholder option.-
Click on Preview and Save and then Save and enable.![How to send escalation emails to unresponsive 상담원 through automations in Freshdesk?](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008578246/original/03_DiKGWk89fQF78ffYbHj251aKtPPBvCA.gif?1686305582)Please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com) if you require further assistance.

</details>

<details>
<summary><strong>Which agent is attributed under the 티켓 resolved/Resolution metric when there are multiple 상담원 working on a particular ticket?</strong></summary>

The 티켓 resolved metric will be attributed to the **"****Assigned agent of the ticket"**, irrespective of who the ticket is resolved or closed by.For example, if ticket #100 is assigned to **Agent A,** and is marked as 'Resolved' by **Agent B **- then the resolved count for this ticket will be attributed to **Agent A.**

</details>

<details>
<summary><strong>configure business hours하는 방법은 무엇인가요?</strong></summary>

You could configure Business Hours on your 계정, based on your active time period for each day of the week. This could be done from under **관리자 > 서비스 Management  > 서비스 desk 설정 > Business Hours > Edit** and change under "Business Hours".![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009501117/original/EcK_NQYihexvvPNaO28Xrl1tcTuMo2Nkgg.png?1695116728)Once this is done, you could associate the SLA to work based on Business Hours.

</details>

<details>
<summary><strong>set holidays and change calendar holidays to working day하는 방법은 무엇인가요?</strong></summary>

Effectively managing holidays and configuring the calendar is essential for maintaining efficient 지원 operations.**Article Navigation**- [Setting Holidays](#Setting-Holidays)
- [Changing Calendar Holidays](#Changing-Calendar-Holidays)**Setting Holidays**To set holidays on your Freshdesk Business Calendar, follow these simple steps:- Go to **관리자 > 팀 > Business Hours**.
- Click on your configured Business Hours to edit it.
- Select the **Holidays** tab and click on **Add Holidays**.
- Enter the **date** and the **name** under the **Exclusive** or **Regional Holidays** category as per your requirement and click **Add**.
- Click **Save **to confirm your changes.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008742392/original/waOoMHT41oDnbVWti_vmixqHX516ctN92A.png?1687943383)Once you have added a holiday to your Freshdesk Business Calendar, it will be marked as a non-working day on your calendar.**Changing Calendar Holidays**If you need to change a calendar holiday to a working day, you can do so by following these steps:- Go to **관리자 > 팀 > Business Hours**.
- Click on your configured Business Hours to edit it.
- Select the **Holidays** tab and find the holiday you want to change.
- Click on the **Remove** button next to the holiday.
- Click on **Save** to confirm the changes.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008742409/original/VgbFOmAr6wdX884O2Lmg4tUsH2pzIv35Ww.png?1687943491)Removing a holiday from your Freshdesk Business Calendar will be marked as a working day on your calendar.The yearly holiday list needs to be updated annually. Custom leaves allocated for the current year cannot be carried forward to future years. To ensure accurate holiday configurations, it is necessary to update the holiday list each year manually.

</details>

<details>
<summary><strong>change the 헬프데스크's TimeZone하는 방법은 무엇인가요?</strong></summary>

Please navigate to** 관리자 -> 계정 -> 헬프데스크 설정 **to see the option to change the time zone.Kindly change it with respect to your location and it would reflect in your 포털.

</details>

<details>
<summary><strong>change my Agent Profile's TimeZone하는 방법은 무엇인가요?</strong></summary>

Please navigate to the Profile 설정 by clicking on your Agent Avatar at the top-right corner of your Freshdesk 계정. You could then change the Time Zone by choosing it from the corresponding dropdown.The Multiple Timezone feature is available only from the** Pro** (previously **Estate**) 요금제 in Freshdesk. So, you would not be able to make this change on the Free Sprout or Blossom 요금제.

</details>

<details>
<summary><strong>Will the reopening of a Resolved ticket count against Average Resolution time?</strong></summary>

Yes, every time a ticket is moved to a status where the SLA timer is toggled on, it will affect the **Response** and **Resolution time** of a ticket.Please navigate to **관리자 > Workflows > Ticket Fields > Status **where the statuses which have the SLA timer have been toggled on could be viewed.

</details>

<details>
<summary><strong>display the clock in the 24-hour time format할 수 있나요?</strong></summary>

As of now, Freshdesk does not have an option to have the **Time Format** to be available in a **24-hour** format.

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
