---
sidebar_position: 1
---

# 고급 티켓 기능 FAQ

고급 티켓 기능에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Can a related ticket be unlinked ?</strong></summary>

Yes it is possible. To unlink the ticket from the Tracker, Go to **Linked 티켓** and click** Unlink**. This permanently unlinks the ticket from that tracker and CANNOT be undone.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008082321/original/02y8OJhzp0wL5LyM2RIfLFT5optAT689JA.gif?1681213289)

</details>

<details>
<summary><strong>create parent and child 티켓하는 방법은 무엇인가요?</strong></summary>

You may open a ticket, click on ‘Add Child’ and choose between "Using a Template" and "New Child Ticket". The original ticket will become the parent ticket and the child ticket will be created as a new ticket. This feature is available from the Estate 요금제 onwards on Freshdesk.

</details>

<details>
<summary><strong>link 티켓 in Freshdesk할 수 있나요?</strong></summary>

Yes, it is possible. By using trackers ,티켓 can be linked in Freshdesk.

</details>

<details>
<summary><strong>언제 does Shared Ownership come into play인가요?</strong></summary>

When there are multiple 상담원 involved in a single ticket, we could make use of Shared Ownership. Whether it is a 고객 facing agent or an internal agent, all are kept in the loop on any action done within the ticket.

</details>

<details>
<summary><strong>view all the related 티켓 to a specific tracker하는 방법은 무엇인가요?</strong></summary>

Yes, it would be possible to view all the 티켓 linked to a tracker.Here are the steps:Step 1: Filter the 티켓 of tracker type in the Association Type field.Step 2: Select the tracker, the one you wish to view all the related 티켓.Step 3: Click on X Related 티켓 on the right hand side of the page.The list of all the related 티켓 is shown.Here X= Number of related 티켓.However as of now, this information is not available as a metrics with 보고서.

</details>

<details>
<summary><strong>Sample scenario for Shared Ownership?</strong></summary>

A ticket comes from an e-commerce company which has issues relating to a bug as well a query regarding a feature.Query is solved by the 고객 facing agent(Primary agent).Bug is solved by the internal agent(Developer).Shared Ownership helps in dynamically checking the status of work on a single ticket, keeping both the 상담원 in the loop.

</details>

<details>
<summary><strong>언제 can we close the parent ticket인가요?</strong></summary>

A Child Ticket is essentially a subdivision of the Parent Ticket. The Parent Ticket can be closed only if all of its Child 티켓 are either Closed or Resolved.

</details>

<details>
<summary><strong>Where/How do you link 티켓 ?</strong></summary>

Go to the **티켓 Tab > Click on the required ticket > Expand the 'Linked 티켓' panel on the extreme right > Create a new tracker or choose to link it to an existing tracker.**This feature is available only from the** Pro/Garden 요금제 **onwards in Freshdesk.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008082368/original/NbcMcB7LAHSM3Bc9hCY_NBMtaVT-EFNgnQ.gif?1681213449)Click [here](https://지원.freshdesk.com/지원/solutions/articles/224695-setting-up-linked-티켓) to know more about Linked 티켓.

</details>

<details>
<summary><strong>filter 티켓 according to a specific tracker 할 수 있나요?</strong></summary>

No, it is not possible to do so. In order to view all the related 티켓 of that tracker, go to the tracker itself and click on related 티켓.

</details>

<details>
<summary><strong>add multiple child 티켓 to a parent ticket하는 방법은 무엇인가요?</strong></summary>

After creating a new child ticket, click on ’Save and New Child’ to add a new child. You could also click on "Add Child" option within a Parent Ticket to create a new child ticket.

</details>

<details>
<summary><strong>set up Shared Ownership하는 방법은 무엇인가요?</strong></summary>

You would have to install the Shared Ownership App on your 계정 as shown in this [해결책 article](https://지원.freshdesk.com/지원/solutions/articles/224194-enabling-shared-ownership).After this is done, there are two steps involved.**1. Map internal groups to a ticket status:**Go to **관리자 > Workflows > Ticket fields **Excluding the 4 basic statuses of ticket, map the custom statuses under Mapped Internal Groups.참고: Don't forget to include 고객 responded.**2. Set up automation rules to make sure everyone's in the loop:**Go to **관리자 > Workflows > Automations > Ticket updates > New rule****Set up a new automation rule as below:****When an action is performed by**Requester**Involves any of these events**Reply IS sent**On 티켓 with these properties**Status is NOT > Open OR Waiting on Third party OR Waiting on Sellers 팀**Perform these actions:**Set status as > OPENSend 이메일 to Agent > Assigned Agent

</details>

<details>
<summary><strong>view all related 티켓하는 방법은 무엇인가요?</strong></summary>

In the 티켓 list page, the ticket with the separate tag that indicates **Tracker** is the main tracker ticket. Also, it is possible to filter all the tracker 티켓 in the 헬프데스크. This can be done by choosing **T****racker** in the** Association Type dropdown field**.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393)To view related 티켓,Go to **티켓 **>select the** Tracker ticket** > click on **Related**** 티켓.****![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008082503/original/eqhZkkU-mU63zvJidlVrWLevLlvnWMP90A.png?1681214101)**

</details>

<details>
<summary><strong>Can we edit the the related ticket widget ? i.e show more details of the tracker?</strong></summary>

No it is not possible to show more details of the tracker in the widget. In order to get more details of the tracker , the agent can view it separately.

</details>

<details>
<summary><strong>know which is the tracker ticket 하는 방법은 무엇인가요?</strong></summary>

In the 티켓 list page, the ticket with the separate tag that indicates **Tracker** is the main tracker ticket. Also, it is possible to filter all the tracker 티켓 in the 헬프데스크. This can be done by choosing **T****racker** in the** Association Type dropdown field**.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393)

</details>

<details>
<summary><strong>view all related 티켓하는 방법은 무엇인가요?</strong></summary>

In the 티켓 tab, the 티켓 having the tag Related Ticket are related/linked to a ticket.

</details>

<details>
<summary><strong>create templates for child 티켓하는 방법은 무엇인가요?</strong></summary>

Under **관리자 > Agent Productivity > Ticket Templates > New Template**, you could add a new ticket template and choose "Save and Add Child" to create a template for Parent Ticket. Once this is done, you would be able to add Child Ticket Templates under this Parent Ticket Template.To apply a template to the child ticket click on ‘**Use existing template**’ while creating a new child ticket.

</details>

<details>
<summary><strong>setup Shared Ownership for existing 티켓하는 방법은 무엇인가요?</strong></summary>

On the ticket details page select and update following:- Internal Groups- Internal Agent

</details>

<details>
<summary><strong>Is the Linked 티켓 tracker same as that of the time tracker ? Are they related ?</strong></summary>

No, both the trackers are completely different. The first one is used to link 티켓 which creates a separate tracker ticket.Whereas the latter is used to calculate the amount of time spent on a particular ticket.

</details>

<details>
<summary><strong>What would be the source of a child ticket?</strong></summary>

Since the ticket is created by an agent, the source of the ticket would be phone.

</details>

<details>
<summary><strong>Does the Linked Ticket Actions appear in the activities tab?</strong></summary>

All the activities that are carried out with respect to the ticket are shown in the activities tab. In this case, even when 티켓 are linked to a tracker is shown in the activities tab,

</details>

<details>
<summary><strong>assign large number of groups and 상담원 for Shared Ownership하는 방법은 무엇인가요?</strong></summary>

There are 2 ways to do it.- **Bulk Mode**Select the necessary 티켓 to perform bulk actions.- **Using Scenario Automation**Option to execute a scenario is directly available in the drop down menu.

</details>

<details>
<summary><strong>How many child 티켓 can be added to a parent ticket?</strong></summary>

We can add a maximum of 50 child 티켓 to a parent ticket.

</details>

<details>
<summary><strong>Is there a bulk action to unlink multiple 티켓 at once ?</strong></summary>

No. It is only possible to unlink a ticket in the ticket details page. Multiple unlinks are not available as of now.

</details>

<details>
<summary><strong>An agent is able to view all the related 티켓 but not view it separately? Why ?</strong></summary>

That agent would be having restricted or group access and hence the related 티켓 are out of the agent's scope.To can give the agent access to view 티켓,- Go to **관리자 > Teams > 상담원 > Edit Agent**
- Scroll down to Scope and edit the scope of the agent.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008160291/original/TIFYobjfeUFvt7PXfoX9aZ6tM0TfYTMC9Q.png?1681981895)Learn more about agent scope [here](https://지원.freshdesk.com/en/지원/solutions/articles/50000002804).

</details>

<details>
<summary><strong>Can we delete a tracker ? Even if there are 티켓 related to it ?</strong></summary>

Yes it is possible to delete a tracker.- Go to the **Tracker.**
- Click on the three dots for **More options** and select **Delete.**
- Once you delete a tracker, its related 티켓 will be permanently unlinked which **cannot** be restored.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008159545/original/Dbierwi181NTLNSV3Ysus6SYeV6hp0VLrg.png?1681978661)

</details>

<details>
<summary><strong>create a parent ticket 하는 방법은 무엇인가요?</strong></summary>

**Quick guide to set up Parent Child Ticketing:**- Log in to your Freshdesk 포털 as an 관리자.
- Go to **관리자**** > 지원 Operations > Advanced Ticketing**.
- Enable the toggle for **Parent-Child Ticketing**.
**![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50014611980/original/XDx7Ns6N2tFvlXc-c5htt4IBVbL1_fG2sA.png?1739862101)**Parent-Child Ticketing will now be enabled in your 계정.To create a parent-child relationship, add a child ticket to any existing or new ticket.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008218906/original/SVLN2BZviELr6OmdDO2_F324WlXPejTnkw.gif?1682592971)

</details>

<details>
<summary><strong>What happens when you delete a parent ticket?</strong></summary>

The parent ticket will be deleted and the associated child 티켓 will be unlinked from the parent ticket.

</details>

<details>
<summary><strong>the use of the Broadcast button은 무엇인가요?</strong></summary>

With all the related 티켓 linked to the Tracker, the 팀 working on it can notify the 상담원 on the progress by using an internal broadcast message.Once the message is broadcasted on the Tracker ticket, it would be relayed on all the related 티켓 automatically. This broadcast message would be visible only to 상담원 on the 계정.-
To broadcast an internal message to 상담원 who are assigned to related 티켓, click on **Broadcast**.**참고:** Only 상담원 who have access to the Tracker ticket will be able to send a broadcast message.- Enter the message and click Broadcast. The message will be sent to all the related 티켓 that are linked with the Tracker.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008160392/original/dBoFEUUFs7c85TkDWLle35uhswqkX9ByaA.gif?1681982296)The broadcast message will be added to any new 티켓 linked to the Tracker. At any point of time, any related ticket will only have the last broadcasted message. That is, if a new message is broadcasted, it will replace the existing message with the new one. The 상담원 can include the message in their replies on the related 티켓 using the **Insert this message into reply** option**참고:** When a message is broadcasted from the Tracker ticket, a hardcoded 이메일 notification will be sent to the assigned agent and the [watcher(s)](https://지원.freshdesk.com/지원/solutions/articles/37560-monitoring-중요-티켓-by-becoming-a-watcher-) added on the related 티켓.

</details>

<details>
<summary><strong>Does updating the status of parent ticket affect the child ticket?</strong></summary>

No, changing the status of the parent ticket will not impact the status of the child 티켓. However, if you wish to achieve this, you can utilize an automation rule. Here is a sample automation rule summary -![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008678782/original/mY2_Ecv8_bs1P_gnr9kACXz4Tv4GJI_CxQ.png?1687347180)

</details>

<details>
<summary><strong>How many number of 티켓 can be linked to a tracker ?</strong></summary>

To a single tracker, a maximum of 300 티켓 can be linked to it.

</details>

<details>
<summary><strong>link multiple 티켓 at once할 수 있나요?</strong></summary>

To link multiple 티켓, we have to goto the ticket details page separately of each ticket and link them individually to a tracker. As of now there is no option under Bulk Actions to carry out this function.

</details>

<details>
<summary><strong>What happens when you mark a parent ticket as spam?</strong></summary>

The child 티켓 associated with the parent ticket will be unlinked and the changes cannot be restored. However, the child 티켓 would not be marked as spam.

</details>

<details>
<summary><strong>Can we filter out 티켓 based on parent and child 티켓?</strong></summary>

Yes, we can filter out 티켓 based on parent and child 티켓.- Go to** 티켓**.
- Under the **Filters section** on the left hand side, click on **Association Type**.
- Select the type of association as **Parent or Child** to filter out the corresponding 티켓.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008160690/original/YBx8VYi-VxUpEaAl6xWDWLTLKEgnAl-Y0A.png?1681983393)

</details>

<details>
<summary><strong>link 티켓 using automations 할 수 있나요?</strong></summary>

No. 티켓 cannot be linked to trackers by using any of the four automations.

</details>

<details>
<summary><strong>Can a linked ticket also be a child/parent ticket ?</strong></summary>

No, 티켓 can be associated via trackers or the parent-child method, but not both.

</details>

<details>
<summary><strong>Can we filter out child 티켓 based on parent ticket?</strong></summary>

No, you cannot filter out child 티켓 based on the parent ticket. However, you can go to the parent ticket and view the child 티켓 associated with it.

</details>

<details>
<summary><strong>the mandatory fields while creating a new tracker은 무엇인가요?</strong></summary>

Two fields are mandatory while creating a new tracker :1. **Requester field** -
The agent creating the tracker ticket is also the requester.There is an option for the agent to create the tracker under their name or the name of one of their colleagues.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008676240/original/cRimC_yjTCaTKLz6xk5iVs-ViH5EKrfgHg.png?1687336095)2. **Subject field** - This defines the name/description of the tracker.If there are any additional fields designated as mandatory under the 관리자 > Ticket fields section, those fields should also be filled in to create a tracker.

</details>

<details>
<summary><strong>Is there a way to disable the 'link to a tracker' option for specific groups/상담원?</strong></summary>

You can create a custom role and manage the **Ticket** access for the 상담원 assigned to the role under **Permissions.**To disable the option for 상담원 to link 티켓,- Go to **관리자 > Teams > Roles **
- Create a **New Role **or click **Edit **next to an existing custom role.
- Scroll down to **Permissions.**
- Under the 티켓 tab, uncheck the box next to **Create a linked ticket.**![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008160952/original/mJCRH2QV4LV1taceyTdzCWShoLGBd8EnmA.png?1681984502)You can now, assign this role to all the 상담원 who should not have access to create linked 티켓.

</details>

<details>
<summary><strong>Can an agent link a ticket to any tracker?</strong></summary>

An agent can only link 티켓 to a tracker that are present in his/her scope. So, if an agent has group/restricted access he/she wont be able to view all the trackers that are present in the 헬프데스크.

</details>

<details>
<summary><strong>Would an agent with Restricted access be able to view Shared Ownership 티켓?</strong></summary>

When the agent has restricted access, still he would be able to see 티켓 assigned to him as an internal agent even if he is not the assigned agent on the ticket.

</details>

<details>
<summary><strong>Would an agent with Group access be able to view Shared Ownership 티켓?</strong></summary>

When an agent has group access, he will have access to the 티켓 which have the internal group assigned as the agent’s group even though the ticket belongs to a different group.

</details>

<details>
<summary><strong>Can internal group or 상담원 be included in automation rules?</strong></summary>

Internal groups or 상담원 can be set in the Conditions and Actions in automation rules that run on ticket creation or ticket updates.

</details>

<details>
<summary><strong>trigger an action using the Ticket Update automation if the Internal group is changed할 수 있나요?</strong></summary>

Within the Ticket Update automation rule, the Internal group can be included in the Conditions and Actions sections, but it is not possible to trigger an Event specifically when the internal group is changed.

</details>

<details>
<summary><strong>enable the Linked Ticket feature on my 계정하는 방법은 무엇인가요?</strong></summary>

To enable Linked 티켓,Go to **관리자>지원 operation>Advanced ticketing> **toggle on** Linked 티켓****![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008161191/original/gJ5yCAjOibRrFXCrBilcySKTavEOr2KxqA.png?1681985565)**

</details>

<details>
<summary><strong>use a template to create a new ticket할 수 있나요?</strong></summary>

We understand that you might want to create 티켓 on-the-go.
Freshdesk allows you to create templates from **관리자  > Agent Productivity > Ticket Templates**. These templates can be used while creating a ticket from the **“Select a template”** option.[This](https://지원.freshdesk.com/지원/solutions/articles/220141-creating-and-using-ticket-templates) article will give you more details on its usage.

</details>

<details>
<summary><strong>Can a linked ticket be merged with another ticket?</strong></summary>

Yes, you can merge 티켓 to a ticket linked to a tracker.

</details>

<details>
<summary><strong>왜 am I not able to link 티켓 to a tracker인가요?</strong></summary>

A ticket cannot be linked to a tracker when any of the following is true :- When the **mandatory or required ticket fields are not filled** in for a ticket, the ticket cannot be linked to a tracker. Make sure all the mandatory ticket fields are filled in for a ticket before linking it to a tracker ticket.- When the ticket is **already associated with a parent or a child ticket**, it will not be possible to link such 티켓 to a tracker.- When a ticket is **merged with another ticket**. The primary ticket which is closed will not have the Linked 티켓 option. In those cases, please use the secondary ticket for linking it to a tracker.

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
