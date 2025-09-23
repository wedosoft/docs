---
sidebar_position: 1
---

# 이메일 알림 FAQ

이메일 알림에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>How to enable or disable email notifications?</strong></summary>

You can enable or disable email notifications for a wide range of workflows within Freshdesk with a simple click of a button.Here's how you do it.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
You will notice that there are four types of notifications on this page.-
Agent Notifications alert the agent when a customer replies to a ticket, when a ticket is assigned to an agent, and so on-
Requester Notifications alert a customer when an agent solves a ticket, closes a ticket, sends a password reset email, and so on.-
CC Notifications alert the email addresses added in the CC field when a new ticket is created or when a public note is added.-
and Reply Templates customize and prefill default information in agent ticket replies, such as dynamic content like the requestor name, ticket URLs, and agent signatures.-
You can toggle ON/OFF the green button next to any email notification to enable or disable them.![How to enable or disable email notifications in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008501686/original/o2mrEyl2OAaTuHNESNkrQE9QzcptVjBmAQ.gif?1685598848)

</details>

<details>
<summary><strong>Why are my requesters receiving two emails notifications when a new ticket is created?</strong></summary>

Apart from the default **New ticket email notification **(Admin > Workflows > Email notifications > Requester notifications), there might be a **Ticket creation automation ****rule **(Admin > Workflows > Automation > ticket creation) that sends an email every time a new ticket is created to the requester. Please check on the reported ticket's[ Show Activities](https://support.freshdesk.com/en/support/solutions/articles/37589-viewing-ticket-activity-history) to see if there was any automation rule executed on that ticket.You can navigate to the corresponding automation rule by clicking on the rule link for that activity. From within the automation rule, verify if there is an action *'Send email to requester'* within the rule. If so, you can remove this action or add another action *'Skip new ticket email notification* to the automation rule, to prevent notification email duplication in cases where this automation rule is triggered on tickets.

</details>

<details>
<summary><strong>How to edit automatic email notifications?</strong></summary>

Using Freshdesk’s automatic email notifications, you can prioritize your work and be aware of new tickets, customer responses, and much more from within your helpdesk.Please follow the below steps to edit the email notifications to customize them per your business requirement.-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
Click on the Edit icon next to any email notification.-
You can make use of the “Insert Placeholder” option to add dynamic content and personalize the email subject and its content.-
Click Save.![How to edit automatic email notification and add dynamic content in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008501704/original/j2l7ZoY-23lOdDPk3etCzrtejtZisKTeHA.gif?1685598955)

</details>

<details>
<summary><strong>How to notify the customer when a ticket is closed or resolved?</strong></summary>

To notify the customer when a ticket is closed or resolved, please navigate to **Admin --> Workflows --> Email Notifications -->Requester Notification-->Turn on** the notification for **Agent closes the ticket** and **Agent Resolves a ticket**. This would send a notification email whenever a ticket raised by them is marked as Resolved/Closed.

</details>

<details>
<summary><strong>How to stop the ticket closure notification for a specific ticket?</strong></summary>

There could be instances where you would like to close specific tickets without notifying the requester that the ticket was closed.In such cases, you could click on the ticket from the tickets list, which would take you to the ticket details page. Within the ticket details page, to the top, you would find the "Close" option. You could click on the "Shift" key and simultaneously click on the Close option.This would close that particular ticket, without sending out the default notification for when "Agent Closes a Ticket", to the requester.

</details>

<details>
<summary><strong>How to set up email notifications and reminders for SLA violation?</strong></summary>

SLAs in customer support service are time-based deadlines agreed upon by the customer and outlined in contracts or terms of service. After you [set up SLA in your Freshdesk](https://support.freshdesk.com/en/support/solutions/folders/273282) account, you can configure SLA reminders and SLA violation notifications to alert agents of upcoming SLA breaches.Please follow the steps below to set up the first response SLA notification email and resolution SLA notification emails.-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu and select Workflows. Click on Email Notifications.-
Under the Agent Notifications tab, turn on the following notifications based on your requirementsFirst Response SLA reminder,
Time SLA reminder, First Response SLA violation, and Resolution Time SLA violation notifications.![Set up email notifications and reminders for SLA violation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008539466/original/ApBBWnm42xjSepPpF09AGnDzbNxCFxTyvQ.gif?1686035655)

</details>

<details>
<summary><strong>How to prevent email notifications for merged tickets?</strong></summary>

When **merging **2 tickets, you can prevent the email notification from being sent to customers that ticket has been closed.While merging tickets in Freshdesk, there is an option to set as** Not visible to contact**, choosing which, the merge action will not be notified to the customers. This has to be enabled in all the tickets that are being merged into one, i.e., the original ticket as well as the ticket(s) being merged.You can also edit the content of the note by clicking on **Edit note **option** **as shown below:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40834312/original/b87gaInqAEPCKaYt1NuOL6qUOEqcHzej5A.png?1537320737)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42278121/original/ZBxLb5slf6Tq-MlNHB1CUxghUl0fCAdjWQ.png?1544587154)

</details>

<details>
<summary><strong>How to setup automatic email response to customers for new tickets?</strong></summary>

Email notification templates in Freshdesk allow you to customize unique, customer-centric notification emails. Freshdesk comes equipped with a default email notification that automatically responds to customers when they create a ticket. You can edit the message and subject of the notification to suit your business needs.Please follow the steps below to edit or customize the New Ticket Created notification.-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
Under the Requester Notifications tab, click on the Edit button next to any New Ticket Created notification.-
Make the necessary modifications and click on Save.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011320075/original/r9ax5qZ0IcAPtOFl1skS4VEUwPDUGBxzcQ.gif?1711102145)**참고:** You can edit the Message or Subject of the notification and save it to send a custom notification to the requesters.

</details>

<details>
<summary><strong>I am not getting notified when I am assigned on a ticket. Please help.</strong></summary>

To notify agents on new ticket assignment,- Go to **Admin > Workflows > Email Notifications > Agent notifications**
- Toggle on notification for "Ticket assigned to agent"![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008005664/original/Fa9vN54fw4RSPpzl23ScjYTjNlWr0YYfhQ.gif?1680241886)After enabling notifications, If the agents are not notified of tickets assigned to them, write to **support@freshdesk.com** for further help**.**

</details>

<details>
<summary><strong>Is there any way to see the automated responses the customer receives for a ticket ?</strong></summary>

The automated response the customer receives after a ticket is created is the default email notification you have set up under **Admin > Workflows > Email Notifications > Requester Notification > New ticket created**. You can edit the subject of the notification to your preference.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008005666/original/zYRPEY0NJDyRTzzpfsZK-_RmQw_WrRaQpw.gif?1680241963)

</details>


## 📋 사용자 관리

<details>
<summary><strong>Why am I, as an agent, not getting notifications when a new ticket is created?</strong></summary>

The "**New ticket created" **agent notification email can be set to be sent to agents whenever a ticket is created in your Freshdesk account. This can be configured under **Admin > Workflows > Email Notifications > Agent Notifications > New Ticket ****Created****.**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42332575/original/4ceZtAwQe62jZk_JQE_IIkZSdX9MKBh4tQ.png?1544759157)If the agents do not receive this email, kindly check if it is toggled on. Further, Only the agents whose names are added under the '**Notify agents' **section would receive this email each time a ticket is created.  You can add as many numbers of agents under this section.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42332497/original/hciQaX6ral6jP6UjAZR0N4KDEusyLwzSeA.png?1544758747)**Similar articles****[](https://support.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**[](https://support.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)[Configuring Email notifications](https://support.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)[](https://support.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**[](https://support.freshdesk.com/a/solutions/articles/220676?lang=en&portalId=2)**

</details>

<details>
<summary><strong>How do I stop my users from receiving an email to sign up for the portal?</strong></summary>

To turn off this sign up email from being sent to the requesters, please go to **Admin --> Workflows --> Email Notifications**** --> Requestor notifications** and turn off **User activation email.**

</details>

<details>
<summary><strong>How to notify customers when agent adds public note?</strong></summary>

Your Freshdesk account comes equipped with a default automation rule to notify customers when an agent adds a public note to their ticket. This helps bring the agent's response to the customer's attention immediately and keeps them informed of the progress in their issue.Please follow the below steps to enable the automation rule to notify customers when an agent adds a public note.-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
Under the Requester Notifications tab, turn on the Agent Adds Comment to Ticket notification.![Notifying customers when agent adds public note](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008479467/original/0mmqXssoFG0WlkWPD58q69W2YmuwMKCpmA.gif?1685436172)-
Click **Edit** to customize the subject and the description of the email.

</details>

<details>
<summary><strong>How to set up agent reply templates?</strong></summary>

A template helps maintain a standard of support replies across a large support team. Typically, an agent reply template has greetings and signatures, so agents needn’t spend time on them but instead concentrate on solving the issue. The templates can also contain pre-written answers for specific support scenarios, like refund requests, etc.Please follow the below steps to set up agent reply templates in Freshdesk.-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
Under the Templates tab, click on the Edit icon next to the Agent Reply Template.-
You can make use of the “Insert Placeholder” option to add dynamic content to the Reply editor and personalize the agent replies.-
Click Save.![How to set up agent reply template in Freshdesk.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008538791/original/--3dhUDm56nx00GAxvrSa2a6vAX-7_4VnA.gif?1686032239)Here is a youtube video with a detailed demonstration providing specific examples for Video: setting up agent reply templates to help you get started.

</details>


---

## 🔗 관련 자료

추가적인 도움이 필요하시면 다음 자료들을 참고해 주세요:

- [Freshdesk 도움말 센터](https://support.freshdesk.com)
- [커뮤니티 포럼](https://community.freshworks.com)
- [비디오 튜토리얼](https://freshdesk.com/resources/videos)

:::tip 도움말
더 자세한 정보나 개별 상담이 필요하시면 고객지원팀(support@freshdesk.com)으로 연락해 주세요.
:::
