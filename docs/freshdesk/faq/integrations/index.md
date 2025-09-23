---
sidebar_position: 1
---

# 통합

이 섹션에서는 통합와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 기본 설정 및 구성

<details>
<summary>할 수 있나요 use dynamic variables when setting up user-defined Slack messages?</summary>

<p ><span style={{ fontSize: "16px" }}>Yes, this is possible- however, please use the following variables for ticket description, last public note, and last private note so that only the text content of the description and notes is sent to Slack; otherwise, the <strong>HTML tags </strong>will get pushed to slack as well.</span></p><ul><li ><span style={{ fontSize: "16px" }}></span><span style={{ fontSize: "16px" }}>Use ``{{#123;`{{#123;ticket.description_text}}`#125;}}`#125;` in place of ``{{#123;`{{#123;ticket.description}}`#125;}}`#125;`</span></li><li ><span style={{ fontSize: "16px" }}></span><span style={{ fontSize: "16px" }}>Use ``{{#123;`{{#123;ticket.latest_public_comment_text}}`#125;}}`#125;` in place of ``{{#123;`{{#123;ticket.latest_public_comment}}`#125;}}`#125;`</span><span style={{ fontSize: "16px" }}></span><span style={{ fontSize: "16px" }}></span></li><li ><span style={{ fontSize: "16px" }}>Use ``{{#123;`{{#123;ticket.latest_private_comment_text}}`#125;}}`#125;` in place of ``{{#123;`{{#123;ticket.latest_private_comment}}`#125;}}`#125;`</span></li></ul>

</details>


## 고급 기능 및 사용법

<details>
<summary>I want to know what the customers are viewing in the website?</summary>

<p>With the Freshmarketer integration, you can now view customer sessions on every ticket generated in Freshdesk. A session replay is a recording of the customer’s journey on a website or within a web application.</p><p><br /></p><p>Benefits of this Session replay integration:</p><p><br /></p><ul><li dir="ltr"><p>Get context about the issue that the customer has been facing, without having to ask them to elaborate the issue. For e.g. If a customer has been facing trouble with routing emails, you can look at the session replay and understand what went wrong.</p></li><li dir="ltr"><p>Lesser email threads leading to decrease in resolution time.</p></li><li dir="ltr"><p>Understand which part of your website/product is confusing to the customer. </p></li><li dir="ltr"><p>Reduces the need to ask customers for screenshots. Instead replay the sessions. </p></li><li dir="ltr"><p>Identify the solution articles visited by the customer to make sure that the support agent does not suggest the same. </p></li></ul><p><br /></p><p>Please refer this <a href="https://support.freshdesk.com/support/solutions/articles/235353-how-to-integrate-freshmarketer-s-session-replay-with-freshdesk-" target="_blank" rel="noreferrer noopener">link</a> for more details.</p><p><br /></p>

</details>

<details>
<summary>무엇인가요 the advanced Freshdesk - Freshcaller Integration</summary>

<p><span>Apart from attending your calls, providing post-call support by converting calls into tickets within Freshdesk, the advanced Freshdesk - Freshcaller integration also helps you <strong>manage your calls within your Freshdesk account </strong>without having to switch tabs to go to your Freshcaller account. </span></p>

</details>


## 통합 및 연동

<details>
<summary>무엇인가요 the basic Freshdesk - Freshcaller Integration?</summary>

<p>The basic Freshdesk - Freshcaller integration helps you convert the calls you manage within your Freshcaller account as tickets in Freshdesk. You can follow-up on your calls, i.e, provide post-call support via Freshdesk and also document them for future context. </p><p><br /></p>

</details>


## 관리 및 유지보수

<details>
<summary>방법 add Apps to my Freshdesk Account?</summary>

<p><span dir="ltr" style={{ fontSize: "16px" }}>You can add apps to your Freshdesk account from the Freshdesk Apps Gallery. <span dir="ltr" style={{ fontSize: "16px" }}>Based on an app's complexity and the availability of its features, it is either free or comes with a charge.</span></span></p><p><br /></p><p><span dir="ltr" style={{ fontSize: "16px" }}>To install an app,</span></p><p><br /></p><ul><li><span dir="ltr" style={{ fontSize: "16px" }}>Go to &nbsp;<strong dir="ltr">Admin&nbsp;</strong>&gt;<strong dir="ltr">&nbsp;Support Operations&nbsp;</strong>&gt;<strong dir="ltr">&nbsp;Apps</strong> &gt;<strong dir="ltr">&nbsp;Marketplace</strong></span></li><li><span dir="ltr" style={{ fontSize: "16px" }}>Search for the app you wish to add and click <strong dir="ltr">Install.</strong></span></li><li><span dir="ltr" style={{ fontSize: "16px" }}>Under <strong dir="ltr">Settings,&nbsp;</strong>configure your <strong>Freshdesk</strong><strong dir="ltr">Domain URL&nbsp;</strong>and <strong dir="ltr">API Key.</strong></span></li></ul><p></p><p><strong dir="ltr"><br /></strong></p><p><strong dir="ltr"><img src="#" style={{ width: "684px" }} class="fr-fic fr-fil fr-dib fr-bordered" /></strong></p><p><br /></p><p dir="ltr"><span dir="ltr" style={{ fontSize: "16px" }}>Your Freshdesk URL will be in the format <span style={{ color: "rgb(44, 130, 201)" }}>&lt;<a dir="ltr" href="//yourcompanyname.freshdesk.com">yourcompanyname&gt;.freshdesk.com</a></span>. You can fetch the URL from your address bar.</span></p><p dir="ltr"><br /></p><p dir="ltr"><img src="#" style={{ width: "684px" }} class="fr-fic fr-fil fr-dib fr-bordered" /></p><p dir="ltr"><br /><span dir="ltr" style={{ fontSize: "16px" }}>To fetch your API Key,</span></p><p dir="ltr" style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><br /></span></p><p dir="ltr" style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Go to <strong>Profile icon&nbsp;</strong>&gt;<strong>&nbsp;Profile settings</strong> &gt;<strong>&nbsp;Your API Key</strong></span></p><p dir="ltr"><br /></p><p dir="ltr"><strong dir="ltr"><img src="#" style={{ width: "684px" }} class="fr-fic fr-fil fr-dib fr-bordered" /></strong><br /></p><p><span dir="ltr" style={{ fontSize: "16px" }}><strong dir="ltr"><br /></strong></span></p>

</details>

<details>
<summary>왜인가요 it that a comment in JIRA is added in Freshdesk under a different username?</summary>

<p ><span rel="tempredactor" style={{ fontSize: "16px" }}>When a user posts a comment in JIRA, an equivalent account is created in Freshdesk with one's JIRA email and the note is added to the Freshdesk ticket. </span></p><p ><br /></p><p ><span rel="tempredactor" style={{ fontSize: "16px" }}>If the email address of the user is <strong>hidden</strong> in JIRA settings, the JIRA integration in your helpdesk will not be able to fetch it, and so a generic one will be used.</span></p><p ><br /></p><p ><span rel="tempredactor" style={{ fontSize: "16px" }}><br /></span></p><p><br /></p>

</details>

<details>
<summary>왜인가요 a ticket created in Freshdesk whenever a comment is added in JIRA?</summary>

<p ><span style={{ fontSize: "16px" }}>This usually happens when you configure notifications in JIRA and it is linked to one of the support addresses configured in Freshdesk. </span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>You can just remove the support email address from the <strong>notification settings </strong>within JIRA to prevent this.</span></p>

</details>

<details>
<summary>Why isn't 상태 mapping in JIRA working for me?</summary>

<p>To understand why the status mapping in JIRA is not working,<br /><br />1. Navigate to <strong dir="ltr">Admin -&gt; Support Operations -&gt; Apps -&gt; JIRA Plus app settings -&gt; General Settings</strong> to check how the status sync between JIRA and Freshdesk is setup.<br /><br /><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "inherit", lineHeight: "1.6", wordBreak: "normal", overflowWrap: "break-word" }}>2. Also, verify how your custom statuses on Freshdesk is mapped to the issue status on Jira<br /><br /><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "inherit", lineHeight: "1.6", wordBreak: "normal", overflowWrap: "break-word" }}><br /></p><p><br /></p>

</details>

<details>
<summary>방법 attach files which are larger than 20 MB?</summary>

<p>Freshdesk has many 3rd party integrations like Dropbox or OneDrive with which agents/customers can use to send files larger than 20 MB. To set up the integrations with Google Drive, refer to <a href="https://support.freshdesk.com/solution/articles/232355-the-google-drive-app" target="_blank" rel="noreferrer noopener">this article</a> and for Dropbox, you can click <a href="https://support.freshdesk.com/support/solutions/articles/55359-the-dropbox-app" target="_blank" rel="noreferrer noopener">here</a>.</p><p><br /></p>

</details>

<details>
<summary>Why aren't messages being pushed to Slack?</summary>

<p><span style={{ fontSize: "16px" }}>Please check if the corresponding channel is configured under <strong dir="ltr">Admin -&gt; Support Operations -&gt; Apps -&gt; Slack -&gt; Edit. </strong></span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>If the channel has been<strong> deleted</strong>, the messages will not be pushed to the Slack channel. </span></p>

</details>

<details>
<summary>어떻게 할 수 있나요 avoid the entire HTML code that comes out when the comment section is included in the message sent to Slack?</summary>

<p><span style={{ fontSize: "16px" }}>When you are using dynamic variables to configure custom messages for Slack, please use the following variables for<strong> ticket description, last public note, and last private note</strong> so that only the text content of the description and notes is sent to Slack. </span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>Otherwise, the <strong>HTML</strong> tags will get pushed to slack as well.</span></p><p><br /></p><p ><span style={{ fontSize: "16px" }}>You can replace the placeholder with <strong>``{{#123;`{{#123;ticket.description_text}}`#125;}}`#125;` or ``{{#123;`{{#123;ticket.description | strip_html}}`#125;}}`#125;` instead of ``{{#123;`{{#123;ticket.description}}`#125;}}`#125;`</strong> and this will just have the text portion included in the notification.</span></p><p ><br /></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}><br /></span></p>

</details>

<details>
<summary>Why am I unable to execute Slash Commands?</summary>

<p><span style={{ fontSize: "16px" }}>Please check the following in the Slack app:</span></p><p><span style={{ fontSize: "16px" }}></span></p><p><span dir="ltr" style={{ fontSize: "16px" }}>1. Make sure <strong>"</strong><strong>Allow Slash Commands" </strong>is checked in the app configuration page. Please navigate to <strong>Admin -&gt; Support Operations -&gt; Apps -&gt;</strong> click on slash integration to see the settings (gear icon) where you could see this configuration. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>2. Make sure that the<strong> correct Slash command token</strong> (obtainable when you create the slash command) is copied to Freshdesk-Slack app settings page.</span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>3. Make sure the <strong>&lt;user API token&gt;</strong> entered along with the /fd_ticket command is the right one.</span></p><p><br /></p>

</details>

<details>
<summary>Do we have any limit to the number of Public and Private channels?</summary>

<p ><span style={{ fontSize: "16px" }}>Yes, the integration allows only <strong>20 private and public channels</strong>. </span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>Of these, at least one channel should be available as Public (independent of the private channels).</span></p>

</details>

<details>
<summary>가능한가요 to hide certain ticket fields to certain agents?</summary>

<p>You can integrate Freshdesk with the app called 'Hide/Disable Ticket Fields'. </p><p><br /></p><p>When there are several irrelevant default and custom Ticket fields it is time-consuming for an agent to scroll through these fields while creating/updating a ticket. All Ticket fields except the mandatory fields will be available to Hide and/or Disable.<br />- Ability to display tickets fields relevant to agents<br />- Useful when a ticket field is used to hold background information that is of no relevance of value to an agent<br />- Reduce unnecessary clutter on agents’ interface<br />- Improve agents’ productivity</p><p><br /></p><p>Refer this <a href="https://apps.freshdesk.com/hidedisable_ticket_fields/" target="_blank" rel="noreferrer noopener">link</a> for more details.</p><p><br /></p><p><br /></p>

</details>

<details>
<summary>왜인가요 only part of the conversation in Slack being converted into a ticket in Freshdesk?</summary>

<p ><span style={{ fontSize: "16px" }}>As per the integration, the latest <strong>200 messages</strong> would only be included in the text of the ticket. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>The<strong> text content</strong> only from conversations will be included in the ticket. All files attached and snippets will be available as a clickable Slack link in your ticket.</span></p><p><br /></p><p ><span style={{ fontSize: "16px" }}></span><br /></p><p ><br /></p>

</details>

<details>
<summary>I typed my auth token incorrectly while calling “/fd_ticket” - what 할 수 있나요 do?</summary>

<p><span style={{ fontSize: "16px" }}>You may call the <strong>slash command</strong> again with the correct token, and the app will override the previously-stored incorrect one. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>Please navigate to <strong dir="ltr">Admin -&gt; Support Operations -&gt; Apps -&gt; Slack</strong> where this could be checked and modified. </span></p>

</details>

<details>
<summary>Why am I getting a failure message at the time of ticket creation, and being asked to contact support@freshdesk.com?</summary>

<p ><span style={{ fontSize: "16px" }}>This could happen due to the following reasons: </span></p><ul><li ><span style={{ fontSize: "16px" }}>The ticket <strong>format or description</strong> is incorrect.</span></li><li><span style={{ fontSize: "16px" }}>Ticket creation is done without <strong>mandatory</strong> fields (priority, source etc).</span></li><li ><span style={{ fontSize: "16px" }}>Slack is not able to process certain details to Freshdesk.</span></li></ul><p ><br /></p><p ><span style={{ fontSize: "16px" }}><br /></span></p>

</details>

<details>
<summary>할 수 있나요 create mailing lists when writing emails?</summary>

<p>You cannot create mailing lists in Freshdesk. However, you can make use of the Mailchimp integration with Freshdesk to create mailing lists in Mailchimp and to send out emails in bulk. Please refer this<a href="https://support.freshdesk.com/support/solutions/articles/41745-the-mailchimp-app" target="_blank" rel="noreferrer noopener"> link </a>for more details about Mailchimp.</p>

</details>

<details>
<summary>Where is the Mailchimp 위젯 located please?</summary>

<p><span style={{ fontSize: "16px" }}>Please navigate to <strong>"apps.freshdesk.com"</strong> and search for MailChimp to install this. Kindly make sure you have a MailChimp account to integrate with Freshdesk. </span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>Once this is successfully added to your helpdesk, the <strong>MailChimp widget </strong>would be available inside the contacts under the customers' tab. </span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>For instance, you click on that widget inside a contact say, Alex - a window with two tabs namely,<strong> campaigns and mailing lists</strong> would open with several options underneath that would allow you to select which to subscribe and unsubscribe appropriately. </span></p>

</details>

<details>
<summary>I do not have the e-commerce option even though I am in the Estate plan. Please help me with this!</summary>

<p ><span style={{ fontSize: "16px" }}>E-commerce is a recently developed platform on Freshdesk which would enable you to bring the Ebay channel into the helpdesk. This is a feature enabled upon request and so kindly contact us on<strong > support@freshdesk.com</strong> in order to bring this as an option on the admin tab. </span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>Once this is enabled, you could see this in <strong dir="ltr">Admin -&gt; Channels -&gt; E-commerce</strong> where you can add a new account. This new account would need your eBay site information and you would be able to assign product, group and such. </span></p>

</details>

<details>
<summary>어떻게 통합하다 Xero with Freshdesk?</summary>

<p><span style={{ fontSize: "16px" }}>Xero is an <strong>Invoicing Tool </strong>which you could integrate with Freshdesk. Using this integration, you would be able to view information about the invoices sent to the requester of the ticket, within that <strong>ticket's details page</strong>. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>You could <strong>track time for tickets </strong>in Freshdesk and <strong>send invoices </strong>for support, using the Xero integration.</span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>You could integrate Xero with your Freshdesk Account, by navigating to <strong dir="ltr">Admin -&gt; Su -&gt; Apps -&gt; Get More Apps--&gt;Time Tracking &amp; Billing--&gt;Xero--&gt;Install</strong>. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>You would be asked to login to your Xero Account to authorize the integration.</span></p>

</details>

<details>
<summary>무엇인가요 SugarCRM? 어떻게 통합하다 with my SugarCRM account?</summary>

<p>SugarCRM is a Customer Relationship Management tool, which is used to track and keep a record of your customer profiles. To provide a better context of customer information to the agents working on your Freshdesk Account, you could integrate SugarCRM with Freshdesk.</p><p><br /></p><p dir="ltr">To integrate SugarCRM, navigate to <strong>Admin &gt; Support Operations &gt; Apps &gt; Get More Apps &gt; CRM &gt; SugarCRM &gt; Install</strong>. This would install the app on your account. You could then configure the app by entering the SugarCRM account URL and credentials. </p>

</details>

<details>
<summary>어떻게 할 수 있나요 통합하다 Zoho CRM with Freshdesk?</summary>

<p>Zoho CRM is a web-based customer relationship management application that has a native integration in Freshdesk. This integration would allow you to fetch requester information from this tool which is available in the contact details as well as tickets detail page. </p><p><br /></p><p>Please navigate to <strong dir="ltr">Admin -&gt; Support Operations -&gt; Apps -&gt; Get more apps -&gt; choose to install Zoho CRM. </strong></p><p>The integration will ask for the Auth Token which can be taken from your Zoho CRM account. For more information, please navigate to this <a href="https://support.freshdesk.com/support/solutions/articles/42657-the-zoho-crm-app" rel="noreferrer noopener">link</a> to set this up. </p><p><br /></p><p><br /></p><p><br /></p><p><br /></p>

</details>

<details>
<summary>방법 통합하다 Freshdesk with my Shopify store?</summary>

<p>At times, you would want to integrate your helpdesk with Shopify so that you can bring your customers' details into the helpdesk.</p><p><br /></p><p dir="ltr">Navigate to <strong>Admin &gt; Support Operations &gt; Apps &gt; Get more apps</strong> and search for Shopify.</p><p>For further instructions on installation and app's capabilities, please refer <a href="https://support.freshdesk.com/support/solutions/articles/195382-the-shopify-app" rel="noreferrer noopener" target="_blank">this</a> article.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 convert WordPress comments to Freshdesk tickets?</summary>

<p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", textAlign: "justify" }}>You can create tickets for the comments on your WordPress website using the Freshdesk plugin for WordPress.</p><p ><br /></p><p dir="ltr" style={{ textAlign: "justify" }}>You can create a ticket for every comment a user writes on your WordPress site users to log in to Freshdesk. To do so, you first need to install the <a href="https://wordpress.org/plugins/freshdesk-support/" rel="noopener noreferrer" target="_blank">Freshdesk WordPress plugin</a>. You can install the plugin from the plugins directory if your site runs on self-hosted WordPress. If you use WordPress.com, you need to be on the <a href="https://wordpress.com/pricing/" rel="noreferrer" target="_blank">Business plan or above</a> to install this plugin.<span dir="ltr" style={{ color: "rgb(0, 0, 0)", fontFamily: "-apple-system, system-ui, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif", fontSize: "13px", fontWeight: "400", textAlign: "justify", textIndent: "0px" }}></span></p><p style={{ textAlign: "justify" }}><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", textAlign: "justify" }}><a href="https://support.freshdesk.com/support/solutions/articles/50000001054-converting-wordpress-comments-to-freshdesk-tickets" rel="noopener noreferrer" style={{ boxSizing: "border-box", color: "rgb(44, 92, 197)" }} target="_blank">Click here</a> to read a step-by-step guide on embedding solution articles and the contact form on Shopify in more detail.</p>

</details>

