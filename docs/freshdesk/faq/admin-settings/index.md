---
sidebar_position: 1
---

# 관리자 설정 FAQ

관리자 설정에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 계정 및 관리

<details>
<summary><strong>I want to login as Administrator</strong></summary>

Your account's Administrator will be able to assign the role of Administrator to you under **Admin > Team > Agents**.

</details>

<details>
<summary><strong>How to make myself an Account Administrator?</strong></summary>

Only another Account Administrator would be able to grant you the Account Administrator Role. If you are already an Admin you would be able to identify who the Account Admin is by going to **Admin > Team > Agents** and the profile that you cannot edit would be the Account Admin's.The Account Admin would be able to give you this by navigating to the **Admin > Team > Agents >Edit**, and if you're able to scroll further you would be able to assign roles to the agent. Please ensure you're given only the Account Administrator role and remove any other role if assigned.
Also, If that person is currently not associated with the company, please send an email to support@freshdesk.com with the person added in the CC so that we could do the needful for you.

</details>

<details>
<summary><strong>What to do if account is blocked due to high traffic?</strong></summary>

Freshdesk constantly monitors every account's activities for suspicious spam activity, like a sudden surge of emails or multiple hits on your portal within a timeframe. Freshdesk may temporarily disable access to your portal to ensure account protection and service availability. However, your portal will automatically be unblocked after an hour. We highly recommend that you identify the reason for the sudden surge in accessing your portal multiple times to avoid this in the future.Also, as an immediate solution, you can use a different web browser or network to sign in to your Freshdesk URL again.Please reach out to [support@freshdesk.com](mailto:support@freshdesk.com) if the issue persists and one of our Product Specialists will assist you further.

</details>

<details>
<summary><strong>As an admin, can I get a notification if an agent is deleted ?</strong></summary>

Under Admin > Security, there will be an option to send notifications to admin(s) of the Account when an agent is added or deleted, also when IP whitelist setting is modified.

</details>


## 📋 일반 질문

<details>
<summary><strong>Can I download Freshdesk?</strong></summary>

Freshdesk is a cloud-based software and is not an On-premise software that can be downloaded. However, you can use Freshdesk on your mobile device by download the ioS or the Android mobile app.

</details>

<details>
<summary><strong>Hi, is there a storage limit on your platform?</strong></summary>

There is no storage limit on the Freshdesk platform. All the data is stored in Cloud. [Click here to learn more](https://support.freshdesk.com/en/support/solutions/articles/196893).

</details>

<details>
<summary><strong>How can I allow customers to access Solution articles without signing in ?</strong></summary>

Change the settings under **Admin > Channels > Portals > Settings > Who can view solutions **and choose the option** everybody, **so that the customers can access the knowledge base without signing into the portal.

</details>

<details>
<summary><strong>Unable to allocate a day pass</strong></summary>

If you are not able to login to the account and if an error throws that says **'Unable to allocate a day pass for you, please contact your administrator'**, it indicates that you are added as an Occasional Agent in your account and your account does not have sufficient day passes to log in.You can contact your Account Administrators and they can help you in purchasing day passes for logging in. A new day pass can be added to your account from under** Admin > Account > Day passes.** You can also view the day pass Usage History from under the same page.

</details>

<details>
<summary><strong>How do I edit ticket fields?</strong></summary>

To edit ticket fields,- Go to **Admin > Workflows > Ticket fields**
- Click on the field and make changes.
- Click **Save Field****![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008161427/original/yfNMURr8G0Lf-cF1Z60MLlrstHNJukMdVA.png?1681986676)**

</details>

<details>
<summary><strong>How do I remove the Freshdesk branding?</strong></summary>

The Freshdesk branding at the bottom of the customer support portal would automatically be removed once your account is upgraded to a paid plan.

</details>

<details>
<summary><strong>Does the order of the SLA policies matter?</strong></summary>

The order of your SLA policies is important. The first SLA Policy that matches all conditions for a ticket will be applied to it, so remember to order your important rules closer to the top.

</details>

<details>
<summary><strong>How to edit a canned response?</strong></summary>

An agent can edit the canned responses created by oneself under **Admin > Agent Productivity > Canned responses**.

</details>

<details>
<summary><strong>How can I avoid spam tickets created from portal?</strong></summary>

You can enable **Captcha** under **Admin > Channels > Portals > Edit > Manage Sections.**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008161523/original/UXVS4USq9sS-nToLyEAzcchfzmp3Ll7x9A.png?1681986988)This will help you avoid automated spam tickets raised from the portal.

</details>

<details>
<summary><strong>How to create a new portal?</strong></summary>

You can create a portal by navigating to **Admin > Support Operations > Multiple Products > Create New product**. You have to set a new support email address for the portal and then have a CNAME and TXT record created for that portal in your DNS.

</details>

<details>
<summary><strong>What is Audit log?</strong></summary>

**Audit Log** in Freshdesk helps admins oversee the changes made in the account by others. This feature focuses on-
What the change was-
Who made this change and-
When it was madeThese logs will now assist Admins or Super Admins to go back to an older working setup if the latest changes, made by another Admin, doesn’t work too well.Audit Log will assist you in viewing changes made to four specific modules:-
Account Subscription-
Agent-
Automation Rules-
Knowledge BaseRefer this [link](https://support.freshdesk.com/support/solutions/articles/235745-track-helpdesk-changes-using-audit-log) for more details.

</details>

<details>
<summary><strong>What are the cases in which the SLA would not run on tickets?</strong></summary>

The SLA timer will not run on tickets when the ticket is in an SLA OFF status. You could check if the SLA timer for the statuses that you had mentioned is turned OFF under **Admin > Workflows > Ticket fields > Status.**Also, the SLA timer would not be running on tickets outside the business hours that you have configured for individual groups. You could check the business hours settings under **Admin > Team > Groups**.But the automated emails sent through the email notifications/automation rules would not be considered as responses on the tickets as these are system generated events. Only a reply/public note from an agent would be considered as a first response on the ticket.

</details>

<details>
<summary><strong>I would like to change the Freshworks profile email</strong></summary>

Any email that is added to a Freshworks product as an agent will have a Freshworks profile. If you want to change the email addresses associated with your product then it will have to be changed in the Admin settings of the product and not from your Freshworks profile.There will be a different Freshworks profile created for that email address and you can set a new password for the same.

</details>

<details>
<summary><strong>I need to find how to change a survey response</strong></summary>

Once a survey response is sent by the customer we will not be able to edit it even if this was an error made by the customer. The survey response will be removed from the Reports if the ticket is deleted or marked as spam.

</details>


## 📋 사용자 관리

<details>
<summary><strong>As an agent, how can I update the email address for my profile ?</strong></summary>

You can contact your account's Administrator to change your email address under **Admin > Team > Agents.**

</details>

<details>
<summary><strong>Agent is locked due to multiple incorrect logins</strong></summary>

When an agent is locked due to multiple login attempts in the Freshworks login, an email would be immediately triggered to the agent's mailbox along with a link to unlock the account. The agent can themselves unlock their account by using that link.If this was not received, you can always reach out to support@freshdesk.com so that we can help you out with this.

</details>

<details>
<summary><strong>Is there also limit for adding Occasional agents?</strong></summary>

There is no limit for the number of occasional agents in your account. You could add as many occasional agents as you want. But occaisonal agents need a day pass to login to the account. For further information please refer this [link](https://support.freshdesk.com/support/solutions/articles/227571-what-is-a-day-pass-).

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
