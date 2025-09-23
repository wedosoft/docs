---
sidebar_position: 1
---

# 고급 티켓 기능 FAQ

고급 티켓 기능에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>Can a related ticket be unlinked ?</strong></summary>

Yes it is possible. To unlink the ticket from the Tracker, Go to **Linked Tickets** and click** Unlink**. This permanently unlinks the ticket from that tracker and CANNOT be undone.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082321/original/02y8OJhzp0wL5LyM2RIfLFT5optAT689JA.gif?1681213289)

</details>

<details>
<summary><strong>How to create parent and child tickets?</strong></summary>

You may open a ticket, click on ‘Add Child’ and choose between "Using a Template" and "New Child Ticket". The original ticket will become the parent ticket and the child ticket will be created as a new ticket. This feature is available from the Estate Plan onwards on Freshdesk.

</details>

<details>
<summary><strong>Is it possible to link tickets in Freshdesk?</strong></summary>

Yes, it is possible. By using trackers ,tickets can be linked in Freshdesk.

</details>

<details>
<summary><strong>When does Shared Ownership come into play?</strong></summary>

When there are multiple agents involved in a single ticket, we could make use of Shared Ownership. Whether it is a customer facing agent or an internal agent, all are kept in the loop on any action done within the ticket.

</details>

<details>
<summary><strong>How to view all the related tickets to a specific tracker?</strong></summary>

Yes, it would be possible to view all the tickets linked to a tracker.Here are the steps:Step 1: Filter the tickets of tracker type in the Association Type field.Step 2: Select the tracker, the one you wish to view all the related tickets.Step 3: Click on X Related tickets on the right hand side of the page.The list of all the related tickets is shown.Here X= Number of related tickets.However as of now, this information is not available as a metrics with Reports.

</details>

<details>
<summary><strong>Sample scenario for Shared Ownership?</strong></summary>

A ticket comes from an e-commerce company which has issues relating to a bug as well a query regarding a feature.Query is solved by the customer facing agent(Primary agent).Bug is solved by the internal agent(Developer).Shared Ownership helps in dynamically checking the status of work on a single ticket, keeping both the agents in the loop.

</details>

<details>
<summary><strong>When can we close the parent ticket?</strong></summary>

A Child Ticket is essentially a subdivision of the Parent Ticket. The Parent Ticket can be closed only if all of its Child Tickets are either Closed or Resolved.

</details>

<details>
<summary><strong>Where/How do you link tickets ?</strong></summary>

Go to the **Tickets Tab > Click on the required ticket > Expand the 'Linked Tickets' panel on the extreme right > Create a new tracker or choose to link it to an existing tracker.**This feature is available only from the** Pro/Garden Plan **onwards in Freshdesk.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082368/original/NbcMcB7LAHSM3Bc9hCY_NBMtaVT-EFNgnQ.gif?1681213449)Click [here](https://support.freshdesk.com/support/solutions/articles/224695-setting-up-linked-tickets) to know more about Linked tickets.

</details>

<details>
<summary><strong>Can I filter tickets according to a specific tracker ?</strong></summary>

No, it is not possible to do so. In order to view all the related tickets of that tracker, go to the tracker itself and click on related tickets.

</details>

<details>
<summary><strong>How to add multiple child tickets to a parent ticket?</strong></summary>

After creating a new child ticket, click on ’Save and New Child’ to add a new child. You could also click on "Add Child" option within a Parent Ticket to create a new child ticket.

</details>

<details>
<summary><strong>How to set up Shared Ownership?</strong></summary>

You would have to install the Shared Ownership App on your account as shown in this [solution article](https://support.freshdesk.com/support/solutions/articles/224194-enabling-shared-ownership).After this is done, there are two steps involved.**1. Map internal groups to a ticket status:**Go to **Admin > Workflows > Ticket fields **Excluding the 4 basic statuses of ticket, map the custom statuses under Mapped Internal Groups.NOTE: Don't forget to include Customer responded.**2. Set up automation rules to make sure everyone's in the loop:**Go to **Admin > Workflows > Automations > Ticket updates > New rule****Set up a new automation rule as below:****When an action is performed by**Requester**Involves any of these events**Reply IS sent**On tickets with these properties**Status is NOT > Open OR Waiting on Third party OR Waiting on Sellers team**Perform these actions:**Set status as > OPENSend email to Agent > Assigned Agent

</details>

<details>
<summary><strong>How to view all related tickets?</strong></summary>

In the tickets list page, the ticket with the separate tag that indicates **Tracker** is the main tracker ticket. Also, it is possible to filter all the tracker tickets in the helpdesk. This can be done by choosing **T****racker** in the** Association Type dropdown field**.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393)To view related tickets,Go to **Tickets **>select the** Tracker ticket** > click on **Related**** Tickets.****![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082503/original/eqhZkkU-mU63zvJidlVrWLevLlvnWMP90A.png?1681214101)**

</details>

<details>
<summary><strong>Can we edit the the related ticket widget ? i.e show more details of the tracker?</strong></summary>

No it is not possible to show more details of the tracker in the widget. In order to get more details of the tracker , the agent can view it separately.

</details>

<details>
<summary><strong>How do i know which is the tracker ticket ?</strong></summary>

In the tickets list page, the ticket with the separate tag that indicates **Tracker** is the main tracker ticket. Also, it is possible to filter all the tracker tickets in the helpdesk. This can be done by choosing **T****racker** in the** Association Type dropdown field**.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393)

</details>

<details>
<summary><strong>How do I view all related tickets?</strong></summary>

In the tickets tab, the tickets having the tag Related Ticket are related/linked to a ticket.

</details>

<details>
<summary><strong>How to create templates for child tickets?</strong></summary>

Under **Admin > Agent Productivity > Ticket Templates > New Template**, you could add a new ticket template and choose "Save and Add Child" to create a template for Parent Ticket. Once this is done, you would be able to add Child Ticket Templates under this Parent Ticket Template.To apply a template to the child ticket click on ‘**Use existing template**’ while creating a new child ticket.

</details>

<details>
<summary><strong>How to setup Shared Ownership for existing tickets?</strong></summary>

On the ticket details page select and update following:- Internal Groups- Internal Agent

</details>

<details>
<summary><strong>Is the Linked tickets tracker same as that of the time tracker ? Are they related ?</strong></summary>

No, both the trackers are completely different. The first one is used to link tickets which creates a separate tracker ticket.Whereas the latter is used to calculate the amount of time spent on a particular ticket.

</details>

<details>
<summary><strong>What would be the source of a child ticket?</strong></summary>

Since the ticket is created by an agent, the source of the ticket would be phone.

</details>

<details>
<summary><strong>Does the Linked Ticket Actions appear in the activities tab?</strong></summary>

All the activities that are carried out with respect to the ticket are shown in the activities tab. In this case, even when tickets are linked to a tracker is shown in the activities tab,

</details>

<details>
<summary><strong>How many child tickets can be added to a parent ticket?</strong></summary>

We can add a maximum of 50 child tickets to a parent ticket.

</details>

<details>
<summary><strong>Is there a bulk action to unlink multiple tickets at once ?</strong></summary>

No. It is only possible to unlink a ticket in the ticket details page. Multiple unlinks are not available as of now.

</details>

<details>
<summary><strong>Can we delete a tracker ? Even if there are tickets related to it ?</strong></summary>

Yes it is possible to delete a tracker.- Go to the **Tracker.**
- Click on the three dots for **More options** and select **Delete.**
- Once you delete a tracker, its related tickets will be permanently unlinked which **cannot** be restored.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008159545/original/Dbierwi181NTLNSV3Ysus6SYeV6hp0VLrg.png?1681978661)

</details>

<details>
<summary><strong>How to create a parent ticket ?</strong></summary>

**Quick guide to set up Parent Child Ticketing:**- Log in to your Freshdesk portal as an Administrator.
- Go to **Admin**** > Support Operations > Advanced Ticketing**.
- Enable the toggle for **Parent-Child Ticketing**.
**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50014611980/original/XDx7Ns6N2tFvlXc-c5htt4IBVbL1_fG2sA.png?1739862101)**Parent-Child Ticketing will now be enabled in your account.To create a parent-child relationship, add a child ticket to any existing or new ticket.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008218906/original/SVLN2BZviELr6OmdDO2_F324WlXPejTnkw.gif?1682592971)

</details>

<details>
<summary><strong>What happens when you delete a parent ticket?</strong></summary>

The parent ticket will be deleted and the associated child tickets will be unlinked from the parent ticket.

</details>

<details>
<summary><strong>What is the use of the Broadcast button?</strong></summary>

With all the related tickets linked to the Tracker, the team working on it can notify the agents on the progress by using an internal broadcast message.Once the message is broadcasted on the Tracker ticket, it would be relayed on all the related tickets automatically. This broadcast message would be visible only to agents on the account.-
To broadcast an internal message to agents who are assigned to related tickets, click on **Broadcast**.**참고:** Only agents who have access to the Tracker ticket will be able to send a broadcast message.- Enter the message and click Broadcast. The message will be sent to all the related tickets that are linked with the Tracker.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008160392/original/dBoFEUUFs7c85TkDWLle35uhswqkX9ByaA.gif?1681982296)The broadcast message will be added to any new tickets linked to the Tracker. At any point of time, any related ticket will only have the last broadcasted message. That is, if a new message is broadcasted, it will replace the existing message with the new one. The agents can include the message in their replies on the related tickets using the **Insert this message into reply** option**참고:** When a message is broadcasted from the Tracker ticket, a hardcoded email notification will be sent to the assigned agent and the [watcher(s)](https://support.freshdesk.com/support/solutions/articles/37560-monitoring-important-tickets-by-becoming-a-watcher-) added on the related tickets.

</details>

<details>
<summary><strong>Does updating the status of parent ticket affect the child ticket?</strong></summary>

No, changing the status of the parent ticket will not impact the status of the child tickets. However, if you wish to achieve this, you can utilize an automation rule. Here is a sample automation rule summary -![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008678782/original/mY2_Ecv8_bs1P_gnr9kACXz4Tv4GJI_CxQ.png?1687347180)

</details>

<details>
<summary><strong>How many number of tickets can be linked to a tracker ?</strong></summary>

To a single tracker, a maximum of 300 tickets can be linked to it.

</details>

<details>
<summary><strong>Is it possible to link multiple tickets at once?</strong></summary>

To link multiple tickets, we have to goto the ticket details page separately of each ticket and link them individually to a tracker. As of now there is no option under Bulk Actions to carry out this function.

</details>

<details>
<summary><strong>What happens when you mark a parent ticket as spam?</strong></summary>

The child tickets associated with the parent ticket will be unlinked and the changes cannot be restored. However, the child tickets would not be marked as spam.

</details>

<details>
<summary><strong>Can we filter out tickets based on parent and child tickets?</strong></summary>

Yes, we can filter out tickets based on parent and child tickets.- Go to** Tickets**.
- Under the **Filters section** on the left hand side, click on **Association Type**.
- Select the type of association as **Parent or Child** to filter out the corresponding tickets.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008160690/original/YBx8VYi-VxUpEaAl6xWDWLTLKEgnAl-Y0A.png?1681983393)

</details>

<details>
<summary><strong>Is it possible to link tickets using automations ?</strong></summary>

No. Tickets cannot be linked to trackers by using any of the four automations.

</details>

<details>
<summary><strong>Can a linked ticket also be a child/parent ticket ?</strong></summary>

No, tickets can be associated via trackers or the parent-child method, but not both.

</details>

<details>
<summary><strong>Can we filter out child tickets based on parent ticket?</strong></summary>

No, you cannot filter out child tickets based on the parent ticket. However, you can go to the parent ticket and view the child tickets associated with it.

</details>

<details>
<summary><strong>What are the mandatory fields while creating a new tracker?</strong></summary>

Two fields are mandatory while creating a new tracker :1. **Requester field** -
The agent creating the tracker ticket is also the requester.There is an option for the agent to create the tracker under their name or the name of one of their colleagues.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008676240/original/cRimC_yjTCaTKLz6xk5iVs-ViH5EKrfgHg.png?1687336095)2. **Subject field** - This defines the name/description of the tracker.If there are any additional fields designated as mandatory under the Admin > Ticket fields section, those fields should also be filled in to create a tracker.

</details>

<details>
<summary><strong>Is it possible to trigger an action using the Ticket Update automation if the Internal group is changed?</strong></summary>

Within the Ticket Update automation rule, the Internal group can be included in the Conditions and Actions sections, but it is not possible to trigger an Event specifically when the internal group is changed.

</details>

<details>
<summary><strong>Can I use a template to create a new ticket?</strong></summary>

We understand that you might want to create tickets on-the-go.
Freshdesk allows you to create templates from **Admin  > Agent Productivity > Ticket Templates**. These templates can be used while creating a ticket from the **“Select a template”** option.[This](https://support.freshdesk.com/support/solutions/articles/220141-creating-and-using-ticket-templates) article will give you more details on its usage.

</details>

<details>
<summary><strong>Can a linked ticket be merged with another ticket?</strong></summary>

Yes, you can merge tickets to a ticket linked to a tracker.

</details>

<details>
<summary><strong>Why am I not able to link tickets to a tracker?</strong></summary>

A ticket cannot be linked to a tracker when any of the following is true :- When the **mandatory or required ticket fields are not filled** in for a ticket, the ticket cannot be linked to a tracker. Make sure all the mandatory ticket fields are filled in for a ticket before linking it to a tracker ticket.- When the ticket is **already associated with a parent or a child ticket**, it will not be possible to link such tickets to a tracker.- When a ticket is **merged with another ticket**. The primary ticket which is closed will not have the Linked tickets option. In those cases, please use the secondary ticket for linking it to a tracker.

</details>


## 📋 사용자 관리

<details>
<summary><strong>How can I assign large number of groups and agents for Shared Ownership?</strong></summary>

There are 2 ways to do it.- **Bulk Mode**Select the necessary tickets to perform bulk actions.- **Using Scenario Automation**Option to execute a scenario is directly available in the drop down menu.

</details>

<details>
<summary><strong>An agent is able to view all the related tickets but not view it separately? Why ?</strong></summary>

That agent would be having restricted or group access and hence the related tickets are out of the agent's scope.To can give the agent access to view tickets,- Go to **Admin > Teams > Agents > Edit Agent**
- Scroll down to Scope and edit the scope of the agent.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008160291/original/TIFYobjfeUFvt7PXfoX9aZ6tM0TfYTMC9Q.png?1681981895)Learn more about agent scope [here](https://support.freshdesk.com/en/support/solutions/articles/50000002804).

</details>

<details>
<summary><strong>Is there a way to disable the 'link to a tracker' option for specific groups/agents?</strong></summary>

You can create a custom role and manage the **Ticket** access for the agents assigned to the role under **Permissions.**To disable the option for agents to link tickets,- Go to **Admin > Teams > Roles **
- Create a **New Role **or click **Edit **next to an existing custom role.
- Scroll down to **Permissions.**
- Under the Tickets tab, uncheck the box next to **Create a linked ticket.**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008160952/original/mJCRH2QV4LV1taceyTdzCWShoLGBd8EnmA.png?1681984502)You can now, assign this role to all the agents who should not have access to create linked tickets.

</details>

<details>
<summary><strong>Can an agent link a ticket to any tracker?</strong></summary>

An agent can only link tickets to a tracker that are present in his/her scope. So, if an agent has group/restricted access he/she wont be able to view all the trackers that are present in the helpdesk.

</details>

<details>
<summary><strong>Would an agent with Restricted access be able to view Shared Ownership tickets?</strong></summary>

When the agent has restricted access, still he would be able to see tickets assigned to him as an internal agent even if he is not the assigned agent on the ticket.

</details>

<details>
<summary><strong>Would an agent with Group access be able to view Shared Ownership tickets?</strong></summary>

When an agent has group access, he will have access to the tickets which have the internal group assigned as the agent’s group even though the ticket belongs to a different group.

</details>

<details>
<summary><strong>Can internal group or agents be included in automation rules?</strong></summary>

Internal groups or agents can be set in the Conditions and Actions in automation rules that run on ticket creation or ticket updates.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How do I enable the Linked Ticket feature on my account?</strong></summary>

To enable Linked Tickets,Go to **Admin>Support operation>Advanced ticketing> **toggle on** Linked tickets****![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008161191/original/gJ5yCAjOibRrFXCrBilcySKTavEOr2KxqA.png?1681985565)**

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
