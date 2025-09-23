---
sidebar_position: 1
---

# 이메일 알림 FAQ

이메일 알림에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>enable or disable 이메일 notifications하는 방법은 무엇인가요?</strong></summary>

You can enable or disable 이메일 notifications for a wide range of workflows within Freshdesk with a simple click of a button.Here's how you do it.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
You will notice that there are four types of notifications on this page.-
Agent Notifications alert the agent when a 고객 replies to a ticket, when a ticket is assigned to an agent, and so on-
Requester Notifications alert a 고객 when an agent solves a ticket, closes a ticket, sends a 비밀번호 reset 이메일, and so on.-
CC Notifications alert the 이메일 addresses added in the CC field when a new ticket is created or when a public 참고 is added.-
and Reply Templates customize and prefill default information in agent ticket replies, such as dynamic content like the requestor name, ticket URLs, and agent signatures.-
You can toggle ON/OFF the green button next to any 이메일 notification to enable or disable them.![How to enable or disable 이메일 notifications in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008501686/original/o2mrEyl2OAaTuHNESNkrQE9QzcptVjBmAQ.gif?1685598848)

</details>

<details>
<summary><strong>왜 am I, as an agent, not getting notifications when a new ticket is created인가요?</strong></summary>

The "**New ticket created" **agent notification 이메일 can be set to be sent to 상담원 whenever a ticket is created in your Freshdesk 계정. This can be configured under **관리자 > Workflows > 이메일 Notifications > Agent Notifications > New Ticket ****Created****.**![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/42332575/original/4ceZtAwQe62jZk_JQE_IIkZSdX9MKBh4tQ.png?1544759157)If the 상담원 do not receive this 이메일, kindly check if it is toggled on. Further, Only the 상담원 whose names are added under the '**Notify 상담원' **section would receive this 이메일 each time a ticket is created.  You can add as many numbers of 상담원 under this section.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/42332497/original/hciQaX6ral6jP6UjAZR0N4KDEusyLwzSeA.png?1544758747)**Similar articles****[](https://지원.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**[](https://지원.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)[Configuring 이메일 notifications](https://지원.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)[](https://지원.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**[](https://지원.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**

</details>

<details>
<summary><strong>왜 are my requesters receiving two emails notifications when a new ticket is created인가요?</strong></summary>

Apart from the default **New ticket 이메일 notification **(관리자 > Workflows > 이메일 notifications > Requester notifications), there might be a **Ticket creation automation ****rule **(관리자 > Workflows > Automation > ticket creation) that sends an 이메일 every time a new ticket is created to the requester. Please check on the reported ticket's[ Show Activities](https://지원.freshdesk.com/en/지원/solutions/articles/37589-viewing-ticket-activity-history) to see if there was any automation rule executed on that ticket.You can navigate to the corresponding automation rule by clicking on the rule link for that activity. From within the automation rule, verify if there is an action *'Send 이메일 to requester'* within the rule. If so, you can remove this action or add another action *'Skip new ticket 이메일 notification* to the automation rule, to prevent notification 이메일 duplication in cases where this automation rule is triggered on 티켓.

</details>

<details>
<summary><strong>stop my users from receiving an 이메일 to sign up for the 포털하는 방법은 무엇인가요?</strong></summary>

To turn off this sign up 이메일 from being sent to the requesters, please go to **관리자 --> Workflows --> 이메일 Notifications**** --> Requestor notifications** and turn off **User activation 이메일.**

</details>

<details>
<summary><strong>edit automatic 이메일 notifications하는 방법은 무엇인가요?</strong></summary>

Using Freshdesk’s automatic 이메일 notifications, you can prioritize your work and be aware of new 티켓, 고객 responses, and much more from within your 헬프데스크.Please follow the below steps to edit the 이메일 notifications to customize them per your business requirement.-
로그인 to your Freshdesk 계정 as an 관리자.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
Click on the Edit icon next to any 이메일 notification.-
You can make use of the “Insert Placeholder” option to add dynamic content and personalize the 이메일 subject and its content.-
Click Save.![How to edit automatic 이메일 notification and add dynamic content in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008501704/original/j2l7ZoY-23lOdDPk3etCzrtejtZisKTeHA.gif?1685598955)

</details>

<details>
<summary><strong>notify the 고객 when a ticket is closed or resolved하는 방법은 무엇인가요?</strong></summary>

To notify the 고객 when a ticket is closed or resolved, please navigate to **관리자 --> Workflows --> 이메일 Notifications -->Requester Notification-->Turn on** the notification for **Agent closes the ticket** and **Agent Resolves a ticket**. This would send a notification 이메일 whenever a ticket raised by them is marked as Resolved/Closed.

</details>

<details>
<summary><strong>stop the ticket closure notification for a specific ticket하는 방법은 무엇인가요?</strong></summary>

There could be instances where you would like to close specific 티켓 without notifying the requester that the ticket was closed.In such cases, you could click on the ticket from the 티켓 list, which would take you to the ticket details page. Within the ticket details page, to the top, you would find the "Close" option. You could click on the "Shift" key and simultaneously click on the Close option.This would close that particular ticket, without sending out the default notification for when "Agent Closes a Ticket", to the requester.

</details>

<details>
<summary><strong>set up 이메일 notifications and reminders for SLA violation하는 방법은 무엇인가요?</strong></summary>

SLAs in 고객 지원 서비스 are time-based deadlines agreed upon by the 고객 and outlined in contracts or terms of 서비스. After you [set up SLA in your Freshdesk](https://지원.freshdesk.com/en/지원/solutions/folders/273282) 계정, you can configure SLA reminders and SLA violation notifications to alert 상담원 of upcoming SLA breaches.Please follow the steps below to set up the first response SLA notification 이메일 and resolution SLA notification emails.-
로그인 to your Freshdesk 계정 as an 관리자.-
Navigate to 관리자 from the menu and select Workflows. Click on 이메일 Notifications.-
Under the Agent Notifications tab, turn on the following notifications based on your requirementsFirst Response SLA reminder,
Time SLA reminder, First Response SLA violation, and Resolution Time SLA violation notifications.![Set up 이메일 notifications and reminders for SLA violation](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008539466/original/ApBBWnm42xjSepPpF09AGnDzbNxCFxTyvQ.gif?1686035655)

</details>

<details>
<summary><strong>notify customers when agent adds public 참고하는 방법은 무엇인가요?</strong></summary>

Your Freshdesk 계정 comes equipped with a default automation rule to notify customers when an agent adds a public 참고 to their ticket. This helps bring the agent's response to the 고객's attention immediately and keeps them informed of the progress in their 문제.Please follow the below steps to enable the automation rule to notify customers when an agent adds a public 참고.-
로그인 to your Freshdesk 계정 as an 관리자.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
Under the Requester Notifications tab, turn on the Agent Adds Comment to Ticket notification.![Notifying customers when agent adds public 참고](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008479467/original/0mmqXssoFG0WlkWPD58q69W2YmuwMKCpmA.gif?1685436172)-
Click **Edit** to customize the subject and the description of the 이메일.

</details>

<details>
<summary><strong>prevent 이메일 notifications for merged 티켓하는 방법은 무엇인가요?</strong></summary>

When **merging **2 티켓, you can prevent the 이메일 notification from being sent to customers that ticket has been closed.While merging 티켓 in Freshdesk, there is an option to set as** Not visible to contact**, choosing which, the merge action will not be notified to the customers. This has to be enabled in all the 티켓 that are being merged into one, i.e., the original ticket as well as the ticket(s) being merged.You can also edit the content of the 참고 by clicking on **Edit 참고 **option** **as shown below:![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/40834312/original/b87gaInqAEPCKaYt1NuOL6qUOEqcHzej5A.png?1537320737)![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/42278121/original/ZBxLb5slf6Tq-MlNHB1CUxghUl0fCAdjWQ.png?1544587154)

</details>

<details>
<summary><strong>set up agent reply templates하는 방법은 무엇인가요?</strong></summary>

A template helps maintain a standard of 지원 replies across a large 지원 팀. Typically, an agent reply template has greetings and signatures, so 상담원 needn’t spend time on them but instead concentrate on solving the 문제. The templates can also contain pre-written answers for specific 지원 scenarios, like refund requests, etc.Please follow the below steps to set up agent reply templates in Freshdesk.-
로그인 to your Freshdesk 계정 as an 관리자.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
Under the Templates tab, click on the Edit icon next to the Agent Reply Template.-
You can make use of the “Insert Placeholder” option to add dynamic content to the Reply editor and personalize the agent replies.-
Click Save.![How to set up agent reply template in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538791/original/--3dhUDm56nx00GAxvrSa2a6vAX-7_4VnA.gif?1686032239)Here is a youtube video with a detailed demonstration providing specific examples for 참고 자료: setting up agent reply templates to help you get started.

</details>

<details>
<summary><strong>setup automatic 이메일 response to customers for new 티켓하는 방법은 무엇인가요?</strong></summary>

이메일 notification templates in Freshdesk allow you to customize unique, 고객-centric notification emails. Freshdesk comes equipped with a default 이메일 notification that automatically responds to customers when they create a ticket. You can edit the message and subject of the notification to suit your business needs.Please follow the steps below to edit or customize the New Ticket Created notification.-
로그인 to your Freshdesk 계정 as an 관리자.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
Under the Requester Notifications tab, click on the Edit button next to any New Ticket Created notification.-
Make the necessary modifications and click on Save.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50011320075/original/r9ax5qZ0IcAPtOFl1skS4VEUwPDUGBxzcQ.gif?1711102145)**참고:** You can edit the Message or Subject of the notification and save it to send a custom notification to the requesters.

</details>

<details>
<summary><strong>I am not getting notified when I am assigned on a ticket. Please help.</strong></summary>

To notify 상담원 on new ticket assignment,- Go to **관리자 > Workflows > 이메일 Notifications > Agent notifications**
- Toggle on notification for "Ticket assigned to agent"![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008005664/original/Fa9vN54fw4RSPpzl23ScjYTjNlWr0YYfhQ.gif?1680241886)After enabling notifications, If the 상담원 are not notified of 티켓 assigned to them, write to **지원@freshdesk.com** for further help**.**

</details>

<details>
<summary><strong>Is there any way to see the automated responses the 고객 receives for a ticket ?</strong></summary>

The automated response the 고객 receives after a ticket is created is the default 이메일 notification you have set up under **관리자 > Workflows > 이메일 Notifications > Requester Notification > New ticket created**. You can edit the subject of the notification to your preference.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008005666/original/zYRPEY0NJDyRTzzpfsZK-_RmQw_WrRaQpw.gif?1680241963)

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
