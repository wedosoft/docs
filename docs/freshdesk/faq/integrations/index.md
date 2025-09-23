---
sidebar_position: 1
---

# 연동 및 통합 FAQ

연동 및 통합에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 계정 및 관리

<details>
<summary><strong>How to add Apps to my Freshdesk Account?</strong></summary>

You can add apps to your Freshdesk account from the Freshdesk Apps Gallery. Based on an app's complexity and the availability of its features, it is either free or comes with a charge.To install an app,- Go to  **Admin **>** Support Operations **>** Apps** >** Marketplace**
- Search for the app you wish to add and click **Install.**
- Under **Settings, **configure your **Freshdesk** **Domain URL **and **API Key.****![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007628783/original/pMz9X4pdeCCFrZ4wyYlta7V3-IvIf9FvVQ.png?1676533180)**Your Freshdesk URL will be in the format .freshdesk.com](//yourcompanyname.freshdesk.com). You can fetch the URL from your address bar.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007628830/original/CcsUKVd840Usk8roJ8IU6ULrLWSrl5myjQ.png?1676533556)To fetch your API Key,Go to **Profile icon **>** Profile settings** >** Your API Key****![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007629119/original/6bq626_T7G56iz8v-gHm89_whV5YUSki2g.png?1676535429)**

</details>

<details>
<summary><strong>Can I use dynamic variables when setting up user-defined Slack messages?</strong></summary>

Yes, this is possible- however, please use the following variables for ticket description, last public note, and last private note so that only the text content of the description and notes is sent to Slack; otherwise, the **HTML tags **will get pushed to slack as well.-
Use \{\{ticket.description_text\}\} in place of  \{\{ticket.description\}-
Use  \{\{ticket.latest_public_comment_text\}\} in place of \{\{ticket.latest_public_comment\}\}- Use \{\{ticket.latest_private_comment_text\}\} in place of \{\{ticket.latest_private_comment\}\}

</details>

<details>
<summary><strong>What is SugarCRM? How do I integrate with my SugarCRM account?</strong></summary>

SugarCRM is a Customer Relationship Management tool, which is used to track and keep a record of your customer profiles. To provide a better context of customer information to the agents working on your Freshdesk Account, you could integrate SugarCRM with Freshdesk.To integrate SugarCRM, navigate to **Admin > Support Operations > Apps > Get More Apps > CRM > SugarCRM > Install**. This would install the app on your account. You could then configure the app by entering the SugarCRM account URL and credentials.

</details>


## 📋 사용자 관리

<details>
<summary><strong>Why is it that a comment in JIRA is added in Freshdesk under a different username?</strong></summary>

When a user posts a comment in JIRA, an equivalent account is created in Freshdesk with one's JIRA email and the note is added to the Freshdesk ticket.If the email address of the user is **hidden** in JIRA settings, the JIRA integration in your helpdesk will not be able to fetch it, and so a generic one will be used.

</details>

<details>
<summary><strong>Is it possible to hide certain ticket fields to certain agents?</strong></summary>

You can integrate Freshdesk with the app called 'Hide/Disable Ticket Fields'.When there are several irrelevant default and custom Ticket fields it is time-consuming for an agent to scroll through these fields while creating/updating a ticket. All Ticket fields except the mandatory fields will be available to Hide and/or Disable.
- Ability to display tickets fields relevant to agents
- Useful when a ticket field is used to hold background information that is of no relevance of value to an agent
- Reduce unnecessary clutter on agents’ interface
- Improve agents’ productivityRefer this [link](https://apps.freshdesk.com/hidedisable_ticket_fields/) for more details.

</details>


## 📋 일반 질문

<details>
<summary><strong>Why is a ticket created in Freshdesk whenever a comment is added in JIRA?</strong></summary>

This usually happens when you configure notifications in JIRA and it is linked to one of the support addresses configured in Freshdesk.You can just remove the support email address from the **notification settings **within JIRA to prevent this.

</details>

<details>
<summary><strong>Why isn't status mapping in JIRA working for me?</strong></summary>

To understand why the status mapping in JIRA is not working,1. Navigate to **관리자 -> Support Operations -> Apps -> JIRA Plus app settings -> General Settings** to check how the status sync between JIRA and Freshdesk is setup.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001119719/original/wgC0wmSBYKHKKy14EF0Y2DXHM7Xc2bW7Sg.png?1589863092)2. Also, verify how your custom statuses on Freshdesk is mapped to the issue status on Jira![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001119735/original/KiZtcKRsdYB9Qju8c9TNDMTn3Pzm7gqo-g.png?1589863423)

</details>

<details>
<summary><strong>How to attach files which are larger than 20 MB?</strong></summary>

Freshdesk has many 3rd party integrations like Dropbox or OneDrive with which agents/customers can use to send files larger than 20 MB. To set up the integrations with Google Drive, refer to [this article](https://support.freshdesk.com/solution/articles/232355-the-google-drive-app) and for Dropbox, you can click [here](https://support.freshdesk.com/support/solutions/articles/55359-the-dropbox-app).

</details>

<details>
<summary><strong>Why aren't messages being pushed to Slack?</strong></summary>

Please check if the corresponding channel is configured under **관리자 -> Support Operations -> Apps -> Slack -> Edit. **If the channel has been** deleted**, the messages will not be pushed to the Slack channel.

</details>

<details>
<summary><strong>How can I avoid the entire HTML code that comes out when the comment section is included in the message sent to Slack?</strong></summary>

When you are using dynamic variables to configure custom messages for Slack, please use the following variables for** ticket description, last public note, and last private note** so that only the text content of the description and notes is sent to Slack.Otherwise, the **HTML** tags will get pushed to slack as well.You can replace the placeholder with **\{\{ticket.description_text\}\} or \{\{ticket.description | strip_html\}\} instead of \{\{ticket.description\}\}** and this will just have the text portion included in the notification.

</details>

<details>
<summary><strong>Why am I unable to execute Slash Commands?</strong></summary>

Please check the following in the Slack app:1. Make sure **"****Allow Slash Commands" **is checked in the app configuration page. Please navigate to **관리자 -> Support Operations -> Apps ->** click on slash integration to see the settings (gear icon) where you could see this configuration.2. Make sure that the** correct Slash command token** (obtainable when you create the slash command) is copied to Freshdesk-Slack app settings page.3. Make sure the **** entered along with the /fd_ticket command is the right one.

</details>

<details>
<summary><strong>Do we have any limit to the number of Public and Private channels?</strong></summary>

Yes, the integration allows only **20 private and public channels**.Of these, at least one channel should be available as Public (independent of the private channels).

</details>

<details>
<summary><strong>Why is only part of the conversation in Slack being converted into a ticket in Freshdesk?</strong></summary>

As per the integration, the latest **200 messages** would only be included in the text of the ticket.The** text content** only from conversations will be included in the ticket. All files attached and snippets will be available as a clickable Slack link in your ticket.

</details>

<details>
<summary><strong>I want to know what the customers are viewing in the website?</strong></summary>

With the Freshmarketer integration, you can now view customer sessions on every ticket generated in Freshdesk. A session replay is a recording of the customer’s journey on a website or within a web application.Benefits of this Session replay integration:-
Get context about the issue that the customer has been facing, without having to ask them to elaborate the issue. For e.g. If a customer has been facing trouble with routing emails, you can look at the session replay and understand what went wrong.-
Lesser email threads leading to decrease in resolution time.-
Understand which part of your website/product is confusing to the customer.-
Reduces the need to ask customers for screenshots. Instead replay the sessions.-
Identify the solution articles visited by the customer to make sure that the support agent does not suggest the same.Please refer this [link](https://support.freshdesk.com/support/solutions/articles/235353-how-to-integrate-freshmarketer-s-session-replay-with-freshdesk-) for more details.

</details>

<details>
<summary><strong>I typed my auth token incorrectly while calling “/fd_ticket” - what can I do?</strong></summary>

You may call the **slash command** again with the correct token, and the app will override the previously-stored incorrect one.Please navigate to **관리자 -> Support Operations -> Apps -> Slack** where this could be checked and modified.

</details>

<details>
<summary><strong>Why am I getting a failure message at the time of ticket creation, and being asked to contact support@freshdesk.com?</strong></summary>

This could happen due to the following reasons:- The ticket **format or description** is incorrect.- Ticket creation is done without **mandatory** fields (priority, source etc).- Slack is not able to process certain details to Freshdesk.

</details>

<details>
<summary><strong>Can I create mailing lists when writing emails?</strong></summary>

You cannot create mailing lists in Freshdesk. However, you can make use of the Mailchimp integration with Freshdesk to create mailing lists in Mailchimp and to send out emails in bulk. Please refer this[ link ](https://support.freshdesk.com/support/solutions/articles/41745-the-mailchimp-app)for more details about Mailchimp.

</details>

<details>
<summary><strong>Where is the Mailchimp widget located please?</strong></summary>

Please navigate to **"apps.freshdesk.com"** and search for MailChimp to install this. Kindly make sure you have a MailChimp account to integrate with Freshdesk.Once this is successfully added to your helpdesk, the **MailChimp widget **would be available inside the contacts under the customers' tab.For instance, you click on that widget inside a contact say, Alex - a window with two tabs namely,** campaigns and mailing lists** would open with several options underneath that would allow you to select which to subscribe and unsubscribe appropriately.

</details>

<details>
<summary><strong>How do I integrate Xero with Freshdesk?</strong></summary>

Xero is an **Invoicing Tool **which you could integrate with Freshdesk. Using this integration, you would be able to view information about the invoices sent to the requester of the ticket, within that **ticket's details page**.You could **track time for tickets **in Freshdesk and **send invoices **for support, using the Xero integration.You could integrate Xero with your Freshdesk Account, by navigating to **관리자 -> Su -> Apps -> Get More Apps-->Time Tracking & Billing-->Xero-->Install**.You would be asked to login to your Xero Account to authorize the integration.

</details>

<details>
<summary><strong>How can I integrate Zoho CRM with Freshdesk?</strong></summary>

Zoho CRM is a web-based customer relationship management application that has a native integration in Freshdesk. This integration would allow you to fetch requester information from this tool which is available in the contact details as well as tickets detail page.Please navigate to **관리자 -> Support Operations -> Apps -> Get more apps -> choose to install Zoho CRM. **The integration will ask for the Auth Token which can be taken from your Zoho CRM account. For more information, please navigate to this [link](https://support.freshdesk.com/support/solutions/articles/42657-the-zoho-crm-app) to set this up.

</details>

<details>
<summary><strong>How to integrate Freshdesk with my Shopify store?</strong></summary>

At times, you would want to integrate your helpdesk with Shopify so that you can bring your customers' details into the helpdesk.Navigate to **Admin > Support Operations > Apps > Get more apps** and search for Shopify.For further instructions on installation and app's capabilities, please refer [this](https://support.freshdesk.com/support/solutions/articles/195382-the-shopify-app) article.

</details>

<details>
<summary><strong>How can I convert WordPress comments to Freshdesk tickets?</strong></summary>

You can create tickets for the comments on your WordPress website using the Freshdesk plugin for WordPress.You can create a ticket for every comment a user writes on your WordPress site users to log in to Freshdesk. To do so, you first need to install the [Freshdesk WordPress plugin](https://wordpress.org/plugins/freshdesk-support/). You can install the plugin from the plugins directory if your site runs on self-hosted WordPress. If you use WordPress.com, you need to be on the [Business plan or above](https://wordpress.com/pricing/) to install this plugin.[Click here](https://support.freshdesk.com/support/solutions/articles/50000001054-converting-wordpress-comments-to-freshdesk-tickets) to read a step-by-step guide on embedding solution articles and the contact form on Shopify in more detail.

</details>

<details>
<summary><strong>What is the basic Freshdesk - Freshcaller Integration?</strong></summary>

The basic Freshdesk - Freshcaller integration helps you convert the calls you manage within your Freshcaller account as tickets in Freshdesk. You can follow-up on your calls, i.e, provide post-call support via Freshdesk and also document them for future context.

</details>

<details>
<summary><strong>What is the advanced Freshdesk - Freshcaller Integration</strong></summary>

Apart from attending your calls, providing post-call support by converting calls into tickets within Freshdesk, the advanced Freshdesk - Freshcaller integration also helps you **manage your calls within your Freshdesk account **without having to switch tabs to go to your Freshcaller account.

</details>


## 📋 요금제 및 결제

<details>
<summary><strong>I do not have the e-commerce option even though I am in the Estate plan. Please help me with this!</strong></summary>

E-commerce is a recently developed platform on Freshdesk which would enable you to bring the Ebay channel into the helpdesk. This is a feature enabled upon request and so kindly contact us on** support@freshdesk.com** in order to bring this as an option on the admin tab.Once this is enabled, you could see this in **관리자 -> Channels -> E-commerce** where you can add a new account. This new account would need your eBay site information and you would be able to assign product, group and such.

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
