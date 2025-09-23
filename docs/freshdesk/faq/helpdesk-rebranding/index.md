---
sidebar_position: 1
---

# 헬프데스크 리브랜딩 FAQ

헬프데스크 리브랜딩에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>What is the difference between the New > Ticket and the New > Email option?</strong></summary>

The option to raise a **new ticket** or send a **new email** is available as part of the '**+ New**' quick access dropdown on the top right corner near the Search icon. You will also find '**New contact**', and '**New Company**' options as part of the dropdown for quick access.**+ New Ticket: **This option can be used by the agents to create a new ticket on behalf of the requester, ideally after a phone call. The source of this ticket will be set as **Phone**. Also, on this page, you will be able to add a new contact. The 'Create another' option will open another new ticket page with the same properties as the previous ticket you just raised.**+ New Email: **This option can be used by agents to send outbound emails to customers from Freshdesk, for any intimation. This email will also be converted into a ticket. Here, you will not have an option to add a contact like the one available in the new ticket page. The 'Send another' option will open another new email page with the same properties as the previous email you just sent.If you would like to create a ticket on behalf of the customer then you can use the 'New Ticket' option and if you would like to send an outbound email to one of your customers then you can use the 'New Email' option.

</details>

<details>
<summary><strong>How do I save the filters I apply under the Tickets tab?</strong></summary>

After applying the filters under the Filter Tickets section of the Ticket view page, please click on the **Tick mark **next to the list view name (All tickets).This will allow you to save these filters and give it a relevant heading as well which you could use later.Here's a[ detailed article](https://support.freshdesk.com/support/solutions/articles/37559-filtering-tickets-using-views) that will help you set it up.

</details>

<details>
<summary><strong>Why is a different language being displayed when I log in to the portal?</strong></summary>

Please check the language options which is applied to your profile - you could check this under Agent Avatar-->Profile Settings.

</details>

<details>
<summary><strong>How can I disable the option for requesters to sign up to our helpdesk?</strong></summary>

Please navigate to **관리자 -> Channels -> Portals -> Settings **and choose the option "**No" **under **Allow users to Sign Up from the customer portal**.This **would not allow** users to sign up from the portal - you would have to send them an activation email to create an account with your system.

</details>

<details>
<summary><strong>How do I remove the Forums tab from the portal entirely?</strong></summary>

Please navigate to **관리자 -> 계정 -> Helpdesk Settings **where you would be able to find a toggle button next to forums. Disabling this would hide the forums tab for all users on every product portal of your system.In order to hide this only for your customers, please get in touch with us **(support@freshdesk.com)** where we could give you a CSS code to hide the tab on the user end.

</details>

<details>
<summary><strong>How to communicate with a third party from a Freshdesk ticket without involving the customer?</strong></summary>

If you are looking to initiating a private conversation with a third party vendor who isn't a part of your Freshdesk Account, you could use the **Forward** option on the Ticket details page.Please navigate to the **Tickets** tab -> click on the ticket on which you would want to perform this action -> and click on "**forward" **next to the reply option.This sends the entire thread or individual reply (depending on which Forward is used) to the third party and it would not be visible to the customer. A reply to this email will be added as a private note to the ticket, which would also not be visible to the customer.

</details>

<details>
<summary><strong>Customers are not able to open the ticket URL in the response. How can I rectify this?</strong></summary>

When you send out responses to your customers - the ticket URL would be available to the users depending on the user permission which can be understood by navigating to **관리자 -> Channels -> Portals -> Settings**. So there are two options - logged-in users or anyone with a **public ticket **URL.Considering the question, the option in your settings is "logged in users" who would need to be verified to have an account in your portal so that they could log in and check. There are two options to do this - make sure you send out an activation URL manually from the customers' tab or automate it in **Adnin > Workflows > Email notifications > Requester notifications > User activation**. Finally, if you would want a quicker alternative, you could guide them to do a password reset on the portal.

</details>


## 📋 사용자 관리

<details>
<summary><strong>How do I auto-fill fields when I'm creating a new ticket as an Agent?</strong></summary>

You have agents with a busy schedule who are on calls and creating tickets for customers as you believe in first-hand support. When your agents are creating a new ticket or sending an outbound email, you can use the Ticket Templates feature to pre-fill regularly used fields.Under **Admin > Agent Productivity > Ticket templates**, you can set up a template that your agents can select with one click. This solution article walks you through the process.The Ticket templates feature is available from the Garden plan onwards.

</details>

<details>
<summary><strong>How do I change the Helpdesk name in the left corner on the Agent portal?</strong></summary>

Please navigate to 관리자 -> 계정 -> Helpdesk Settings to change the portal name displayed on the left side of the navigation bar.You will find a field called **Helpdesk name** in the Helpdesk settings, where you can enter the desired helpdesk name.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009297345/original/zhQF9PjRqJrJFWJVXVqmVKv8vmbClTPphg.png?1693233538)

</details>

<details>
<summary><strong>How do I rebrand the Agent side of the portal and change its colors?</strong></summary>

To change the colors of the Agent side of the portal, please go to **Admin > Account > Helpdesk Settings > **Click on** Edit Branding **and make the necessary changes to **Helpdesk colors**.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009272133/original/Xisbv1VyF-9As4wXDp9KlrG0-w4xaf78SA.png?1692892903)

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How to cancel my Freshdesk Account?</strong></summary>

We, at Freshdesk, are always available to assist you with any issues that you are facing and will be happy to make your experience better. If there is anything we can help you with, feel free to write to us at **support@freshdesk.com**.However, if you're certain that you'd like to delete your account, please click on **Admin** (represented by a gear icon from the navigation panel on the left)** > Account > Account Details **and click on '**Cancel Account**'.**Note that you will have to be an 'Account Administrator' on the portal to find this section.**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41662165/original/A4iAu0m5oQfkKBgT_42D9y6RztF6ysCDQg.png?1541575768)It would be really helpful if you share your feedback and the reason behind canceling your account with us. You can then hit the '**Request Cancellation**' button on the next page and confirm the action on the following pop-up window.You will have **24 hours before your account gets suspended**, and **14 days (2 weeks) before we delete your account and account data permanently**.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41662167/original/WxaC4O6i8X3X2Axjw1yd2KEP83dj1lTq0A.png?1541575787)Furthermore, we would advise you to export your account data by using the '**Export Now**' option on the same page before canceling your Freshdesk Account.**Note**: If you're getting an error while deleting your account, please reach out to our support team at support@freshdesk.com

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
