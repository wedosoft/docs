---
sidebar_position: 1
---

# 연동 및 통합 FAQ

연동 및 통합에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>add Apps to my Freshdesk 계정하는 방법은 무엇인가요?</strong></summary>

You can add apps to your Freshdesk 계정 from the Freshdesk Apps Gallery. Based on an app's complexity and the availability of its features, it is either free or comes with a charge.To install an app,- Go to  **관리자 **>** 지원 Operations **>** Apps** >** Marketplace**
- Search for the app you wish to add and click **Install.**
- Under **설정, **configure your **Freshdesk** **Domain URL **and **API Key.****![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50007628783/original/pMz9X4pdeCCFrZ4wyYlta7V3-IvIf9FvVQ.png?1676533180)**Your Freshdesk URL will be in the format .freshdesk.com](//yourcompanyname.freshdesk.com). You can fetch the URL from your address bar.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50007628830/original/CcsUKVd840Usk8roJ8IU6ULrLWSrl5myjQ.png?1676533556)To fetch your API Key,Go to **Profile icon **>** Profile 설정** >** Your API Key****![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50007629119/original/6bq626_T7G56iz8v-gHm89_whV5YUSki2g.png?1676535429)**

</details>

<details>
<summary><strong>왜 is it that a comment in JIRA is added in Freshdesk under a different 사용자명인가요?</strong></summary>

When a user posts a comment in JIRA, an equivalent 계정 is created in Freshdesk with one's JIRA 이메일 and the 참고 is added to the Freshdesk ticket.If the 이메일 address of the user is **hidden** in JIRA 설정, the JIRA integration in your 헬프데스크 will not be able to fetch it, and so a generic one will be used.

</details>

<details>
<summary><strong>왜 is a ticket created in Freshdesk whenever a comment is added in JIRA인가요?</strong></summary>

This usually happens when you configure notifications in JIRA and it is linked to one of the 지원 addresses configured in Freshdesk.You can just remove the 지원 이메일 address from the **notification 설정 **within JIRA to prevent this.

</details>

<details>
<summary><strong>왜 isn't status mapping in JIRA working for me인가요?</strong></summary>

To understand why the status mapping in JIRA is not working,1. Navigate to **관리자 -> 지원 Operations -> Apps -> JIRA Plus app 설정 -> General 설정** to check how the status sync between JIRA and Freshdesk is setup.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001119719/original/wgC0wmSBYKHKKy14EF0Y2DXHM7Xc2bW7Sg.png?1589863092)2. Also, verify how your custom statuses on Freshdesk is mapped to the 문제 status on Jira![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001119735/original/KiZtcKRsdYB9Qju8c9TNDMTn3Pzm7gqo-g.png?1589863423)

</details>

<details>
<summary><strong>attach files which are larger than 20 MB하는 방법은 무엇인가요?</strong></summary>

Freshdesk has many 3rd party integrations like Dropbox or OneDrive with which 상담원/customers can use to send files larger than 20 MB. To set up the integrations with Google Drive, refer to [this article](https://지원.freshdesk.com/해결책/articles/232355-the-google-drive-app) and for Dropbox, you can click [here](https://지원.freshdesk.com/지원/solutions/articles/55359-the-dropbox-app).

</details>

<details>
<summary><strong>왜 aren't messages being pushed to Slack인가요?</strong></summary>

Please check if the corresponding channel is configured under **관리자 -> 지원 Operations -> Apps -> Slack -> Edit. **If the channel has been** deleted**, the messages will not be pushed to the Slack channel.

</details>

<details>
<summary><strong>avoid the entire HTML code that comes out when the comment section is included in the message sent to Slack하는 방법은 무엇인가요?</strong></summary>

When you are using dynamic variables to configure custom messages for Slack, please use the following variables for** ticket description, last public 참고, and last private 참고** so that only the text content of the description and notes is sent to Slack.Otherwise, the **HTML** tags will get pushed to slack as well.You can replace the placeholder with **\{\{ticket.description_text\}\} or \{\{ticket.description | strip_html\}\} instead of \{\{ticket.description\}\}** and this will just have the text portion included in the notification.

</details>

<details>
<summary><strong>왜 am I unable to execute Slash Commands인가요?</strong></summary>

Please check the following in the Slack app:1. Make sure **"****Allow Slash Commands" **is checked in the app configuration page. Please navigate to **관리자 -> 지원 Operations -> Apps ->** click on slash integration to see the 설정 (gear icon) where you could see this configuration.2. Make sure that the** correct Slash command token** (obtainable when you create the slash command) is copied to Freshdesk-Slack app 설정 page.3. Make sure the **** entered along with the /fd_ticket command is the right one.

</details>

<details>
<summary><strong>Do we have any limit to the number of Public and Private channels?</strong></summary>

Yes, the integration allows only **20 private and public channels**.Of these, at least one channel should be available as Public (independent of the private channels).

</details>

<details>
<summary><strong>hide certain ticket fields to certain 상담원할 수 있나요?</strong></summary>

You can integrate Freshdesk with the app called 'Hide/Disable Ticket Fields'.When there are several irrelevant default and custom Ticket fields it is time-consuming for an agent to scroll through these fields while creating/updating a ticket. All Ticket fields except the mandatory fields will be available to Hide and/or Disable.
- Ability to display 티켓 fields relevant to 상담원
- Useful when a ticket field is used to hold background information that is of no relevance of value to an agent
- Reduce unnecessary clutter on 상담원’ interface
- Improve 상담원’ productivityRefer this [link](https://apps.freshdesk.com/hidedisable_ticket_fields/) for more details.

</details>

<details>
<summary><strong>왜 is only part of the conversation in Slack being converted into a ticket in Freshdesk인가요?</strong></summary>

As per the integration, the latest **200 messages** would only be included in the text of the ticket.The** text content** only from conversations will be included in the ticket. All files attached and snippets will be available as a clickable Slack link in your ticket.

</details>

<details>
<summary><strong>use dynamic variables when setting up user-defined Slack messages할 수 있나요?</strong></summary>

Yes, this is possible- however, please use the following variables for ticket description, last public 참고, and last private 참고 so that only the text content of the description and notes is sent to Slack; otherwise, the **HTML tags **will get pushed to slack as well.-
Use \{\{ticket.description_text\}\} in place of  \{\{ticket.description\}-
Use  \{\{ticket.latest_public_comment_text\}\} in place of \{\{ticket.latest_public_comment\}\}- Use \{\{ticket.latest_private_comment_text\}\} in place of \{\{ticket.latest_private_comment\}\}

</details>

<details>
<summary><strong>I want to know what the customers are viewing in the website?</strong></summary>

With the Freshmarketer integration, you can now view 고객 sessions on every ticket generated in Freshdesk. A session replay is a recording of the 고객’s journey on a website or within a web application.Benefits of this Session replay integration:-
Get context about the 문제 that the 고객 has been facing, without having to ask them to elaborate the 문제. For e.g. If a 고객 has been facing trouble with routing emails, you can look at the session replay and understand what went wrong.-
Lesser 이메일 threads leading to decrease in resolution time.-
Understand which part of your website/product is confusing to the 고객.-
Reduces the need to ask customers for screenshots. Instead replay the sessions.-
Identify the 해결책 articles visited by the 고객 to make sure that the 지원 agent does not suggest the same.Please refer this [link](https://지원.freshdesk.com/지원/solutions/articles/235353-how-to-integrate-freshmarketer-s-session-replay-with-freshdesk-) for more details.

</details>

<details>
<summary><strong>I typed my auth token incorrectly while calling “/fd_ticket” - what can I do?</strong></summary>

You may call the **slash command** again with the correct token, and the app will override the previously-stored incorrect one.Please navigate to **관리자 -> 지원 Operations -> Apps -> Slack** where this could be checked and modified.

</details>

<details>
<summary><strong>왜 am I getting a failure message at the time of ticket creation, and being asked to contact 지원@freshdesk.com인가요?</strong></summary>

This could happen due to the following reasons:- The ticket **format or description** is incorrect.- Ticket creation is done without **mandatory** fields (priority, source etc).- Slack is not able to process certain details to Freshdesk.

</details>

<details>
<summary><strong>create mailing lists when writing emails할 수 있나요?</strong></summary>

You cannot create mailing lists in Freshdesk. However, you can make use of the Mailchimp integration with Freshdesk to create mailing lists in Mailchimp and to send out emails in bulk. Please refer this[ link ](https://지원.freshdesk.com/지원/solutions/articles/41745-the-mailchimp-app)for more details about Mailchimp.

</details>

<details>
<summary><strong>Where is the Mailchimp widget located please?</strong></summary>

Please navigate to **"apps.freshdesk.com"** and search for MailChimp to install this. Kindly make sure you have a MailChimp 계정 to integrate with Freshdesk.Once this is successfully added to your 헬프데스크, the **MailChimp widget **would be available inside the 연락처 under the customers' tab.For instance, you click on that widget inside a contact say, Alex - a window with two tabs namely,** campaigns and mailing lists** would open with several options underneath that would allow you to select which to subscribe and unsubscribe appropriately.

</details>

<details>
<summary><strong>I do not have the e-commerce option even though I am in the Estate 요금제. Please help me with this!</strong></summary>

E-commerce is a recently developed platform on Freshdesk which would enable you to bring the Ebay channel into the 헬프데스크. This is a feature enabled upon request and so kindly contact us on** 지원@freshdesk.com** in order to bring this as an option on the 관리자 tab.Once this is enabled, you could see this in **관리자 -> Channels -> E-commerce** where you can add a new 계정. This new 계정 would need your eBay site information and you would be able to assign product, group and such.

</details>

<details>
<summary><strong>integrate Xero with Freshdesk하는 방법은 무엇인가요?</strong></summary>

Xero is an **Invoicing Tool **which you could integrate with Freshdesk. Using this integration, you would be able to view information about the invoices sent to the requester of the ticket, within that **ticket's details page**.You could **track time for 티켓 **in Freshdesk and **send invoices **for 지원, using the Xero integration.You could integrate Xero with your Freshdesk 계정, by navigating to **관리자 -> Su -> Apps -> Get More Apps-->Time Tracking & 결제-->Xero-->Install**.You would be asked to 로그인 to your Xero 계정 to authorize the integration.

</details>

<details>
<summary><strong>SugarCRM? How do I integrate with my SugarCRM 계정은 무엇인가요?</strong></summary>

SugarCRM is a 고객 Relationship Management tool, which is used to track and keep a record of your 고객 profiles. To provide a better context of 고객 information to the 상담원 working on your Freshdesk 계정, you could integrate SugarCRM with Freshdesk.To integrate SugarCRM, navigate to **관리자 > 지원 Operations > Apps > Get More Apps > CRM > SugarCRM > Install**. This would install the app on your 계정. You could then configure the app by entering the SugarCRM 계정 URL and credentials.

</details>

<details>
<summary><strong>integrate Zoho CRM with Freshdesk하는 방법은 무엇인가요?</strong></summary>

Zoho CRM is a web-based 고객 relationship management application that has a native integration in Freshdesk. This integration would allow you to fetch requester information from this tool which is available in the contact details as well as 티켓 detail page.Please navigate to **관리자 -> 지원 Operations -> Apps -> Get more apps -> choose to install Zoho CRM. **The integration will ask for the Auth Token which can be taken from your Zoho CRM 계정. For more information, please navigate to this [link](https://지원.freshdesk.com/지원/solutions/articles/42657-the-zoho-crm-app) to set this up.

</details>

<details>
<summary><strong>integrate Freshdesk with my Shopify store하는 방법은 무엇인가요?</strong></summary>

At times, you would want to integrate your 헬프데스크 with Shopify so that you can bring your customers' details into the 헬프데스크.Navigate to **관리자 > 지원 Operations > Apps > Get more apps** and search for Shopify.For further instructions on installation and app's capabilities, please refer [this](https://지원.freshdesk.com/지원/solutions/articles/195382-the-shopify-app) article.

</details>

<details>
<summary><strong>convert WordPress comments to Freshdesk 티켓하는 방법은 무엇인가요?</strong></summary>

You can create 티켓 for the comments on your WordPress website using the Freshdesk plugin for WordPress.You can create a ticket for every comment a user writes on your WordPress site users to log in to Freshdesk. To do so, you first need to install the [Freshdesk WordPress plugin](https://wordpress.org/plugins/freshdesk-지원/). You can install the plugin from the plugins directory if your site runs on self-hosted WordPress. If you use WordPress.com, you need to be on the [Business 요금제 or above](https://wordpress.com/pricing/) to install this plugin.[Click here](https://지원.freshdesk.com/지원/solutions/articles/50000001054-converting-wordpress-comments-to-freshdesk-티켓) to read a step-by-step guide on embedding 해결책 articles and the contact form on Shopify in more detail.

</details>

<details>
<summary><strong>the basic Freshdesk - Freshcaller Integration은 무엇인가요?</strong></summary>

The basic Freshdesk - Freshcaller integration helps you convert the calls you manage within your Freshcaller 계정 as 티켓 in Freshdesk. You can follow-up on your calls, i.e, provide post-call 지원 via Freshdesk and also document them for future context.

</details>

<details>
<summary><strong>What is the advanced Freshdesk - Freshcaller Integration</strong></summary>

Apart from attending your calls, providing post-call 지원 by converting calls into 티켓 within Freshdesk, the advanced Freshdesk - Freshcaller integration also helps you **manage your calls within your Freshdesk 계정 **without having to switch tabs to go to your Freshcaller 계정.

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
