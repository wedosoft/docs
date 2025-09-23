---
sidebar_position: 1
---

# 자동 티켓 배포 FAQ

자동 티켓 배포에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>Does the Round-Robin functionality work only during business hours?</strong></summary>

The round robin feature or the automatic assignment functionality would work whenever the icon next to the profile photo is togged on. This is not tied to the business hours.As of now, this feature will work irrespective of the portal's business hours. Even if the agent turns on auto ticket assignment during **non-business hours**, the system will continue assigning the tickets to that agent.A workaround would be to not give the agent the permission to turn on the automatic assignment by unchecking **"Allow agents to change their availability for automatic ticket assignment" - **this would give the admins to control the ticket assignment and could manually switch on round robin during business hours in **Dashboard -> Available agents -> ticket assignment.******

</details>

<details>
<summary><strong>Does the Round-Robin assign tickets in alphabetical order?</strong></summary>

The auto-assignment feature will assign the tickets to the agents as per the order in which they have been added to the group. For example, if agents C, A, and B are added to a group in that order and if they are all online to accept tickets, the tickets will also be assigned in the same order.Therefore, if the tickets have to be assigned in alphabetical order, please manually rearrange them accordingly in **Admin > Team > Groups > click on edit** to achieve this.

</details>

<details>
<summary><strong>What is automatic ticket assignment?</strong></summary>

You can automatically assign tickets to agents in various groups by enabling the automatic assignment option for the corresponding group. Below are the steps to enable that;-
Login to your Freshdesk account as an administrator.-
Navigate to Admin from the menu. Under Team, click on Groups.-
Select the group for which you want to enable automatic assignment and click the ‘Edit’ icon.-
Go to Group Properties and enable ‘Automatic ticket assignment.’-
Choose the appropriate assignment mode and agent availability parameter.-
Click ‘Save’ to update the group settings.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008552935/original/ZF2Sn-8Si5T2MUCv2a5buA2ddDOS0Rch3A.gif?1686126546)Please reach out to [support@freshdesk.com](mailto:support@freshdesk.com) if you require further assistance.

</details>


## 📋 사용자 관리

<details>
<summary><strong>What happens to a ticket when the caps for all agents are met?</strong></summary>

When all available agents reach their ticket cap when you have automatic assignment turned on, new incoming tickets will be queued in the unassigned bucket.Please check the cap in** Admin > Team > Groups > click on edit **next to the one you would want to check this for and see the number listed in maximum tickets per agent under **"Load Balanced ticket assignment."**These will be assigned when any one of the agent's ticket count falls below the capped level.

</details>

<details>
<summary><strong>How does Automatic ticket assignment work after an agent logs out</strong></summary>

This depends on whether an agent is a part of groups for which availability is managed centrally by admins ( can be configured under Admin-> Groups)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004910431/original/1q_n2S4M5IxsK9dbrkEcgKKX7lS9K1B7AQ.png?1646382490)**Case 1- Agents have the ability to manage statuses ******If agents have access to change their availability in all the groups that they're a part of, they become unavailable for automatic assignment when they log out.**Case 2- Agent's availability is centrally managed.******If an agent is a part of one or more groups where availability is managed centrally by Admins, the agent's availability prior to logging out is considered for automatic routing.For example, say Agent A and Agent B are part of groups where availability is managed centrally by admins. Agent A's status is available when they log out. Agent B's status is unavailable when they log out. Tickets will continue being assigned to agent A since they were available at the time of log out.

</details>

<details>
<summary><strong>Is there a way to prevent automatic ticket assignment when an agent replies to an unassigned ticket?</strong></summary>

The automatic ticket assignment would be caused by the action of the automation rule that runs on ticket updates - 'Automatically assign the ticket to the first responder'.You could disable this rule if you'd like to have the ticket assigned before being responded to. Go to **Admin > Workflows > Automations > Ticket Updates** toggle this off.

</details>

<details>
<summary><strong>Is it possible to automatically assign tickets based on agent workload?</strong></summary>

Yes, Freshdesk has a feature called **Load-based ticket assignment**, using which tickets could be assigned within a group, based on the current ticket load for an agent.Please navigate to **Admin > Team > Groups > click on edit **next to the group for which this feature has to be enabled and choose the **"Load Balanced Ticket Assignment" **radio button under automatic ticket assignment.

</details>

<details>
<summary><strong>Is there a report on the total time that an agent has been available for ticket assignment?</strong></summary>

Currently, it is not possible to report on the time duration for which the agent has been available to accept tickets through the** "Automatic ticket assignment"** feature.However, please navigate to the **D****ashboard -> agent availability -> ticket assignment **where as an Admin you would be able to see the number of hours since when the agent has been automatically receiving tickets.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How do I enable Round Robin Ticket Assignment in my account?</strong></summary>

Within Freshdesk, you would have the option to automatically assign tickets to agents within a group, in round-robin. To enable automatic ticket assignment for a group, please navigate to **Admin > Team > Groups >** Edit(corresponding to the group) and turn on "**Automatic Ticket Assignment**".  You could choose the mode of Automatic Ticket assignment as " Round Robin".참고: This feature is available only in the Estate and Forest plans.

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
