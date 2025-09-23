---
sidebar_position: 1
---

# 티켓 워크플로우

이 섹션에서는 티켓 워크플로우와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 고급 기능 및 사용법

<details>
<summary>어떻게 create a custom ticket view?</summary>

<p>You can create a view from the <strong>Tickets tab,</strong> where you have to filter out the fields that is required and at the top of the page you would see the <strong>Save as</strong> option. </p><p><br /></p><p><img class="fr-dib fr-draggable fr-bordered" src="#" /></p><p><br /></p>Once that is clicked you can save the new view under a different name.

</details>

<details>
<summary>방법 close a ticket without sending an email 알림 to the customer?</summary>

<p ></p><p ><span style={{ fontSize: "16px" }}>When you are working on tickets, we extend an option to <strong >close </strong>the ticket without an email notification sent out for this.</span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>This can be achieved by clicking on the <strong >"closed"</strong> button inside a ticket (details page) or on the list view which is basically "shift+close" and a notification would not be sent in this case. </span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>When you are completely affirmative that you do not want to send this out at all for any of the tickets, kindly navigate to </span></p><p ><strong ><span dir="ltr" style={{ fontSize: "16px" }}>Admin &gt; Workflows &gt; Email Notifications &gt; Requester Notifications &gt; Turn OFF "Agent Closes the Ticket."</span></strong></p>

</details>

<details>
<summary>Can the Admin and Agents view the same system activities in automations?</summary>

<p>The view for both the Admin and Agents would be different. When Activities is toggled 'ON', Admins would be able to view the automation along with the name of the rule and a hyperlink redirecting to it. However, Agents and Supervisors<span> can</span> only view the name of the automation rule which was executed.</p><p><br /></p>

</details>

<details>
<summary>방법 exclude the full email thread in each customer reply to a ticket?</summary>

<p>When you are replying to a customer from inside a ticket, you can remove the quoted text manually and the customer will not receive the whole thread. Also, you can make use of the <a href="https://apps.freshdesk.com/remove_quoted_text/" rel="noreferrer noopener" target="_blank">Marketplace app</a> to have the quoted text removed when the reply is added in Freshdesk. </p>

</details>

<details>
<summary>I am not able to add more custom fields to the requester 위젯?</summary>

<p>The upper limit to number of fields that could be added to the requester widget is 15. So, it would not be currently possible to add more than 15 fields to the Requester Widget.</p>

</details>

<details>
<summary>가능한가요 to check the ticket history of a particular customer?</summary>

In Freshdesk, you could view the most recent tickets raised by a requester, from within any of the the requester's tickets. To view this list, please click on the<span></span><strong>Recent Tickets</strong><span></span>option present within the requester widget. This would bring up all the past tickets from a particular customer.<p><br /></p>

</details>

<details>
<summary>할 수 있나요 customise the fields under the Tickets tab?</summary>

<p ><span style={{ fontSize: "16px" }}>When you are familiar with the tickets tab, sometimes there will be requirements to alter the arrangement of fields on "The Tickets list view" page. Unfortunately, it is not customizable as the design of the page is set by default and is common for all accounts.</span></p><p ><br /></p><p ><span dir="ltr" style={{ fontSize: "16px" }}>Please note that the custom ticket fields within <strong>Admin &gt; Workflows &gt; Ticket Fields</strong> could be altered in terms of the values and label. These changes would reflect within the filters on the left of the tickets list. </span></p>

</details>

<details>
<summary>Is there a possibility for a customer to check the 상태 of their ticket without logging in?</summary>

<div dir="ltr"><p style={{ lineHeight: "1.38" }}><span style={{ fontSize: "14.6667px", fontFamily: "Arial", color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}>As a customer, it is understandable that they sometimes want to do a quick peruse through the ticket and not log in to the portal. In this scenario, the best recommendation would be to use a <strong>"public ticket URL"</strong> which leads to the ticket and does not require the customer to sign in.</span></p><p style={{ lineHeight: "1.38" }}><span style={{ fontSize: "14.6667px", fontFamily: "Arial", color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}><br /></span></p><p style={{ lineHeight: "1.38" }}><span style={{ fontSize: "14.6667px", fontFamily: "Arial", color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}>This has a placeholder which when included in the description of the ticket will ensure that the customer can view the ticket status without logging into the portal upon clicking this URL. </span></p><p style={{ lineHeight: "1.38" }}><span style={{ fontSize: "14.6667px", fontFamily: "Arial", color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}><br /></span></p><p style={{ lineHeight: "1.38" }}><span style={{ fontSize: "14.6667px", fontFamily: "Arial", color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}>To have the Public Ticket URL available in all replies, please navigate to <strong dir="ltr">Admin &gt; Workflows &gt; Email Notifications &gt; Templates &gt; </strong></span><span style={{ color: "rgb(0, 0, 0)", fontFamily: "Arial", fontSize: "14.6667px", whiteSpace: "pre-wrap" }}><strong>Agent Reply Template</strong> -&gt;<strong> insert placeholder </strong>and include the Public Ticket URL placeholder (please find this under the tickets section within the "insert placeholder" window).</span></p><p><br /></p></div>

</details>

<details>
<summary>How can the customer change the 우선순위 and type of a ticket?</summary>

<div dir="ltr"><p><span style={{ fontSize: "16px", fontFamily: "Helvetica Neue" }}>When customers raise tickets, you would like to extend the ability for them to choose the priority and type of tickets so that you could plan the assignment and tracking of them. </span></p><p><br /></p><p><span style={{ fontSize: "16px", fontFamily: "Helvetica Neue" }}>Please navigate<span id="docs-internal-guid-9b6b1c48-6245-0d35-83ef-77e1a3f8db4c"><span dir="ltr" style={{ color: "rgb(0, 0, 0)", whiteSpace: "pre-wrap" }}> to <strong dir="ltr">Admin &gt; Workflows &gt; Ticket fields</strong> &gt; double click on these fields and verify if the priority field is displayed to the customer. If not, kindly choose the option 'Display to the customer' under customers end in ticket properties and the customer will then be able to edit it.</span></span></span></p></div>

</details>

<details>
<summary>How can customers view their previous conversations after a ticket is closed?</summary>

<div dir="ltr"><div dir="ltr"><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>Customers can view the history of tickets if they have access to your customer portal. </span></span></p><p><br /></p><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>They could log into your portal using the email address used to raise the tickets and view the status of all the tickets raised. You would be able to determine who could view the tickets by changing the permission to <strong>"Logged in Users"</strong> or to <strong>"Everyone"</strong> with a public ticket URL in <strong dir="ltr">Admin -&gt; Channels -&gt; Portals -&gt; Settings. </strong></span></span></p><p><br /></p><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>Customers would also receive an email notification with the ticket details if you have enabled the Requester notifications under </span><strong><span dir="ltr" style={{ fontSize: "medium" }}>Admin -&gt; Workflows -&gt; Email Notifications.</span></strong></span></p></div></div>

</details>

<details>
<summary>어떻게 split a customer response into a new ticket?</summary>

<p >If your customers respond with a new or unrelated query on an existing ticket, you can deal with it separately using the <strong >S</strong><strong >plit</strong><strong >&nbsp;Ticket&nbsp;</strong>option. You can split <strong >only a</strong><strong >customer response</strong> into a new ticket.</p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style={{ width: "639px", height: "216.141px" }} /></p><p ><br /></p><p dir="ltr">This would facilitate better tracking metrics and help regulate your SLA compliance.&nbsp;</p>

</details>

<details>
<summary>할 수 있나요 send bulk emails to customers using Freshdesk?</summary>

<p>No, there isn't an option to send out bulk emails to customers from inside Freshdesk. However, an integration with MailChimp can help you perform this action. </p><p><br /></p><p>Please refer to <a href="https://support.freshdesk.com/support/solutions/articles/41745-the-mailchimp-app" target="_blank" rel="noreferrer noopener">this article</a> on how you can integrate MailChimp with Freshdesk.</p>

</details>

<details>
<summary>Is there a way to send a 알림 to all customer at once?</summary>

<p >We do not have an option to bulk email all your customers at once. You can make use of <a href="https://apps.freshdesk.com/mailchimp/" rel="noreferrer noopener"><strong>Mailchimp</strong></a> to send out these emails. </p><p ><br /></p><p >However, if you are wanting to notify customers who have raised tickets then you can make use of the Bulk Actions present in the <strong>Ticket list view</strong> and send out the emails to 30 tickets at a time. </p>

</details>

<details>
<summary>어디서 할 수 있나요 find the customer fields in ticket page?</summary>

<p >You will not be able to filter the tickets using the Customer fields. However, if you want to view the Contact details in the Ticket details page you can make use of the Requester widget available under <strong dir="ltr">Admin &gt; Support Operations &gt; Customer fields &gt; Customize Requester widget</strong>. This is a feature available from the Estate plan.</p>

</details>


## 관리 및 유지보수

<details>
<summary>어떻게 specify time range for 내보내기?</summary>

<p >After filtering the tickets that you need to export from the Tickets List view page, you would be able to click on the Export icon at the top of the page. In the popup that appears you would be able to enter the date range for which you want to export the tickets. </p><p><br /></p><p><img class="fr-dib fr-draggable fr-bordered" src="#" style={{ width: "279px", height: "263.742px" }} /></p><p><br /></p>

</details>

<details>
<summary>Where is the option to forward a ticket ?</summary>

<p>The <strong>Forward</strong> option for a ticket will be inside the <strong>Ticket details page</strong> as shown below:</p><p><br /></p><p><img class="fr-dib fr-draggable fr-bordered" src="#" style={{ width: "473px", height: "211.109px" }} /></p>

</details>

<details>
<summary>무엇인가요 the maximum size of a file that can be attached to a ticket ?</summary>

<p >You will only be able to attach a maximum size of 20MB when receiving an email and for replies sent out of Freshdesk.</p>

</details>

<details>
<summary>무엇인가요 the size limit for attachments to a ticket reply?</summary>

<p><span id="docs-internal-guid-bffa19b3-0253-fe35-2d9c-5f16432e0d51"></span></p><p dir="ltr"><span rel="tempredactor" style={{ fontSize: "16px" }}></span>Freshdesk lets you send and receive emails with an attachment size limit of <strong>20 MB</strong>/conversation for accounts on the Blossom and above plans. For Sprout and trial accounts, the attachment size limit is 15 MB. </p><p><br /></p><p>By default, the content of the email (excluding attachments) has a 15 MB limit per conversation.</p><p><br /></p><p>However, if you are looking to attach bigger files, you can use <strong>Dropbox</strong> as a workaround. Once you integrate Freshdesk with Dropbox, you can hotlink any file from your Dropbox account (with unlimited file size), and use it as an attachment inside Freshdesk. This file can be directly opened from Dropbox whenever someone clicks on it, and will not be stored anywhere on our end. Another alternative is <strong>OneDrive</strong> which could also help you add files with a greater MB value.</p><p><br /></p><p><strong>Note:</strong> We do not recommend that you use heavy HTML content inside your tickets. Instead, you can attach them as separate files inside the ticket just like any other attachment. </p>

</details>

<details>
<summary>What are tags? 어떻게 할 수 있나요 add/merge tags?</summary>

<p >As an agent when you are working on tickets or accessing articles, characterizing them by adding a tag would help to track and segregate them with respect to issues or requests. </p><p ><br /></p><p >Go to <strong dir="ltr">Admin &gt; Agent Productivity &gt; Tags &gt; Add tag</strong> and add the required tags for the helpdesk. Each tag has a <strong >character limit of 32</strong>. </p><p ><br /></p><p >Once a tag is created, you can associate it with Tickets, Contact, and Articles. You can merge two tags by editing one of the tags and giving it the same name as the other.</p><p ><br /></p><p ><img src="#" style={{ width: "309px" }} class="fr-fic fr-dib fr-bordered" /></p><p ><br /></p><p >Upon adding a tag:</p><p ><br /></p><p ><img src="#" style={{ width: "309px" }} class="fr-fic fr-dib fr-bordered" /></p>

</details>

<details>
<summary>어떻게 add a 태그 to a ticket?</summary>

<div dir="ltr"><p>The '<strong>Tag</strong>' field will be available under the '<strong>Ticket Properties</strong>' panel on the right hand side of the ticket details page. You can either manually type out and create new tags or add existing ones to tickets.</p><p><br /></p><p>If you are using <u>Freshdesk on Mint</u>, the '<strong>Add tag</strong>' option will be available above the main message/description of the ticket, in the ticket details page:</p><p><br /></p><p><img class="fr-dib fr-bordered" src="#" style={{ width: "433px", height: "323.723px" }} /><br /></p><p><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p></div>

</details>

<details>
<summary>할 수 있나요 add tags automatically?</summary>

<div dir="ltr"><p dir="ltr">You can add tags manually and/or automatically. Add them manually inside a ticket or go to <strong dir="ltr">Admin &gt; Agent Productivity &gt; Tags</strong> to add/see the list of tags and the corresponding ticket count.</p><p ><br /></p><p ><span dir="ltr" rel="tempredactor"><a href="https://support.freshdesk.com/en/support/solutions/articles/207276" rel="noreferrer" target="_blank">Add tags automatically using automations rules</a>. Note that in a Supervisor rule, the tag will be added only after an hour if there is no other time-related condition.&nbsp;</span></p></div>

</details>

<details>
<summary>할 수 있나요 attach multiple files while replying to a ticket?</summary>

<p>You can attach multiple files from your system while replying to a ticket. However, for trial accounts and accounts that are on the Sprout plan, the total file size of all the attachments together should not exceed 15 MB. For accounts that are on the Blossom and above plans, the attachment size limit is 20 MB.</p>

</details>

<details>
<summary>Would it be possible to add attachments that are more than 20 MB in size?</summary>

<p><span style={{ fontSize: "16px" }}>The attachment size limit in Freshdesk is 20 MB per email for accounts on the Blossom and above plans and 15 MB for Sprout and accounts that are on Trial. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>This can be extended by making use of third party integration tools such as </span><a href="https://support.freshdesk.com/support/solutions/articles/210996-the-google-drive-app-part-1-developer-console-settings"></a><a href="https://support.freshdesk.com/support/solutions/articles/55359-the-dropbox-app"><span style={{ fontSize: "16px" }}>Dropbox</span></a><span style={{ fontSize: "16px" }}> and </span><a href="https://support.freshdesk.com/support/solutions/articles/213938-the-onedrive-app"><span style={{ fontSize: "16px" }}>OneDrive</span></a><span style={{ fontSize: "16px" }}>.</span></p>

</details>

<details>
<summary>I want to insert a footer into all my replies. 어떻게 do this?</summary>

<p><span rel="tempredactor">You can insert <strong>footers </strong>into all the ticket replies going out of your helpdesk, by adding them in the Agent Reply Template. This template is automatically included in all agent replies, whenever they respond to tickets. </span>To do this</p><ul><li><span style={{ lineHeight: "16px" }}>Please log in to your Freshdesk account as an Administrator</span></li><li>Go to <strong dir="ltr">Admin &gt; Workflows &gt; Email Notifications</strong></li><li><span style={{ lineHeight: "16px" }}>Click on the<strong> Templates</strong> tab <strong>&gt;</strong><strong>Agent Reply Template</strong> and add the footer message to the content of the template</span></li></ul>

</details>

<details>
<summary>가능한가요 to forward the ticket to an email address whenever a new ticket is created ?</summary>

<div style={{ boxSizing: "border-box", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, ", fontSize: "14px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>Yes, you could either set up a new rule under <strong>Admin &gt; Workflows &gt; Automations &gt; Ticket Creation</strong> to add a CC whenever a new ticket is created, or you could add the user's email address under <strong>Admin &gt; Channels &gt; Email &gt; Advanced Settings &gt; Set automatic Bcc email.</strong></div><div style={{ boxSizing: "border-box", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, ", fontSize: "14px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><br /></div><div dir="ltr" style={{ boxSizing: "border-box", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, ", fontSize: "14px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>This email address would be automatically included in all helpdesk communications.</div><p ><br /></p>

</details>

<details>
<summary>가능한가요 to add another agent to a ticket?</summary>

<p><span style={{ fontSize: "14px" }}>You have a workflow set up where tickets are assigned to a particular agent depending upon the job description, the group this concerned agent belongs to and the expertise as well. Sometimes an agent would need another agent to look into something in the thread or receive notifications to go through the discussion. </span></p><p><span style={{ fontSize: "14px" }}><br /></span></p><p><span style={{ fontSize: "14px" }}>In this case, an agent could be added as a <strong>"watcher" </strong>who would receive all the notifications about the thread from the time when the agent is added as a watcher. You could have multiple agents added to a ticket as watchers.</span></p><p><span style={{ fontSize: "14px" }}><br /></span></p><p><span style={{ fontSize: "14px" }}>Only the one added as a watcher could remove oneself from the thread. An occasional agent without a day pass could still follow the ticket in the email thread when added as a watcher on tickets. </span></p>

</details>

<details>
<summary>How do you check if an agent is looking at the same ticket ?</summary>

<p>When an agent is looking into the same ticket, you could be notified regarding this within the ticket. This would help in preventing multiple agents working on the same ticket and to improve internal communication, using Freshdesk.&nbsp;</p><p><br /></p><p>At the top-left, within a ticket, you would find an "Eye" icon. While hovering upon it, the number of agents viewing the ticket would be displayed. You could also click on the icon to view a list of Agent Names of those agents currently viewing the ticket.</p><p><br /></p><p dir="ltr">This functionality is called as <a href="https://support.freshdesk.com/en/support/solutions/articles/218073">Agent Collision detection</a> and is available from the Growth Plan onwards in Freshdesk.</p>

</details>

<details>
<summary>How do we check if an agent is answering/replying to your ticket ?</summary>

<p>If there are multiple agents replying to a ticket, you could be notified regarding that within the ticket as well. There would be a "Pen" icon on the top-left side within a ticket. If the symbol displays a number, it would mean that those many agents are currently replying to the ticket and you could click on the icon to view the agents' names.</p>

</details>

<details>
<summary>어떻게 view the updates made to a ticket?</summary>

<p>After clicking on a ticket, please click on the Activities option to the top-right of the ticket details page. This would display the list of activities performed on the ticket in chronological order, which would contain information on updates made by each of these activities.</p>

</details>

<details>
<summary>While merging tickets, 가능한가요 to change the content of the auto response?</summary>

<div dir="ltr"><div dir="ltr"><p><span style={{ color: "rgb(0, 0, 0)", fontFamily: "Arial", lineHeight: "normal", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>Although the text that is added as a private note when two or more tickets are merged cannot be modified automatically, it still can be modified by the agent manually, by using the "Edit Note" option, while merging the tickets. </span></span></p><p><br /></p><p><span style={{ color: "rgb(0, 0, 0)", fontFamily: "Arial", lineHeight: "normal", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>The Agent will also be provided with the option to add it as a <strong>public note</strong> that would be visible to the requester.</span></span></p></div></div>

</details>

<details>
<summary>Is there a limit in the number of tickets you can have?</summary>

<p >There is no limit on the number of tickets that can be present inside your Freshdesk Account, under any plan. </p>

</details>

<details>
<summary>무엇인가요 a Requester 위젯?</summary>

<p>Requester Widget is a part of the ticket details page. This section would contain Requester Information such as Requester Name, Email Address, Company Name and any custom field which could be associated with this section.</p><p><br /></p><p>The Requester Widget gives more context about the requester to any agent working on the ticket. This functionality is available only from the Blossom plan onwards in Freshdesk.</p>

</details>

<details>
<summary>어떻게 add/remove the fields to be displayed on the requester 위젯?</summary>

<p >You can add or remove the fields being displayed as part of the requester widget, from under <strong dir="ltr">Admin &gt; Support Operations &gt; Customer Fields &gt;</strong><strong >Customize Requester Widget</strong> option. You can also add company fields to be displayed within the Requester Widget.</p><p ><br /></p><p >For more details, please refer to this article on setting up the <a href="https://support.freshdesk.com/support/solutions/articles/37586-driving-additional-context-with-requester-info" rel="noreferrer noopener" target="_blank">Requester Widget</a>.</p><p ><br /></p>

</details>

<details>
<summary>할 수 있나요 edit the requester details directly from the requester 위젯?</summary>

<p>Except the<span></span><strong>Email</strong>, all the requester details can directly be edited from the widget. To edit the contact field values from within the Requester Widget, click on the "Edit" option within the Requester Info section. This would open a pop-up with the fields on the Requester Widget, from where you could edit the values of those Contact/Company Fields.</p>

</details>

<details>
<summary>Can a public note be changed to private?</summary>

<p>No, there is no option to change a public note that is already added into a private note. However, you would be able to delete the public note and add a private note from inside the ticket.</p>

</details>

<details>
<summary>방법 change the requester’s email address in a ticket?</summary>

<p><span style={{ fontSize: "16px" }}>Inside the Ticket details page, click on the <strong>More button -&gt; choose</strong><strong> Edit </strong>to find the option to edit the requester's email address. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>The <strong>Edit </strong>option would not be available for the tickets with Source as <strong>Outbound email. </strong>To edit the requester of an Outbound email ticket, you would have to change the Source of the ticket first under ticket properties. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>If you are using <strong>Freshdesk on Mint</strong>, you will find the 'More' option against the subject of the ticket. Clicking here will give you an option to 'Edit' the details of the ticket.</span></p><p><br /></p><p><span style={{ fontSize: "16px" }}><img src="#" class="fr-fic fr-dib fr-bordered" /></span><br /></p><p><br /></p>

</details>

<details>
<summary>할 수 있나요 see an email after its deleted from trash?</summary>

<p >A ticket will remain in the trash folder inside Freshdesk for 30 days and post which it will be permanently deleted automatically from the database. Once a ticket is deleted from the trash folder manually or automatically there is no option to restore the ticket.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 create a view to see only the tickets I am working on?</summary>

<p>Once you start working with the product and develop a workflow where you are assigned tickets on a regular basis, you require an organized queue of the ones that need your attention. This is called a "view" - when you get tickets assigned to you, a filter can be applied by choosing "me" in the agent field and other properties could be changed to see your prioritized list.&nbsp;</p><p><br /></p><p><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p><p dir="ltr">Say, for instance, you are an agent who works on social tickets on a high priority - please choose the filters accordingly from the filters pane. You can also save the view if needed as <strong dir="ltr">"Tickets I'm working on"</strong>.</p>

</details>

<details>
<summary>어떻게 notify my team members about the proceedings of the tickets?</summary>

<p >You can add the agents as watchers to the ticket so that all the members will receive email notifications about all the activities happening on a ticket. </p><p ><br /></p><p ><img class="fr-dib fr-draggable" src="#" style={{ width: "551px", height: "178.658px" }} /></p>

</details>

<details>
<summary>어디서 할 수 있나요 view the tickets in my account - 어떻게 할 수 있나요 정렬 my queue?</summary>

<p>We have a '<strong>Tickets'</strong> section represented by a ticket icon and this presents all the tickets in your helpdesk. All these tickets from various 'sources' like phone, chat, social, feedback form and such (internally these channels are called sources) are all available on this list within the tickets section and we generally address it as the <strong>tickets list view</strong>.<br /><br /></p><p><img src="#" style={{ width: "60px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-fic fr-dib" /></p><p><br /></p><p><br /></p><p>To achieve an organized structure for accessing tickets, we have filters such as date created, last modified, due by time and other ticket properties such as status or priority. Please refer to this <a href="https://support.freshdesk.com/support/solutions/articles/37559-working-with-the-ticket-list-view" rel="noreferrer noopener"><strong>article</strong></a> on how efficiently the filters could be used.&nbsp;</p><p><br /></p><p>Further, they can be sorted as well in an ascending or descending order. This can be seen when you click on the header of the tickets queue (for example, it would say '<strong>All tickets'</strong>). You can use the available sorting options that is depicted in the image below.</p><p><br /></p><p><img src="#" style={{ width: "121px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-fic fr-dib" /></p><p><br /></p><p><br /></p>

</details>

<details>
<summary>방법 정렬 my tickets such that the oldest tickets are on the top of the tickets queue?</summary>

<p>You have a good volume of tickets to handle on a daily basis and according to you, the tickets that have been sitting in the queue for a greater period of time would need your immediate attention. In this case, please explore the option of sorting in the tickets list view where the option that needs to be chosen is "date created" and in order to have the oldest tickets on top - please choose "ascending" along with this in the dropdown.&nbsp;</p><p><br /></p><p>Please note that this has many other options such as last modified, status, priority and due by date. Within that, you could choose ascending or descending.&nbsp;</p><p><br /></p><p><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p>

</details>

<details>
<summary>How does a ticket get marked as spam?</summary>

<p ><span style={{ fontSize: "16px" }}>There are three ways in which a ticket can end up in the Spam folder -</span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>1. Manually marked as Spam by an Agent.</span></p><p ><span style={{ fontSize: "16px" }}>2. Ticket marked as Spam by an Automation rule such as the <strong >Ticket creation</strong> or the <strong >Ticket Update </strong>rule.</span></p><p ><span style={{ fontSize: "16px" }}>3. Any ticket raised from a <strong >deleted user in Freshdesk </strong>would go to Spam automatically.</span></p><p ><br /></p>

</details>

<details>
<summary>Every ticket for a particular user goes to Spam. Is there a place where we can “clear” the user's email?</summary>

<div dir="ltr"><div dir="ltr"><div dir="ltr"><p ><br /></p><p >There are three ways by which a ticket leads to the Spam folder -</p><ul ><li >Manually marked as Spam by an Agent.&nbsp;</li><li dir="ltr">A ticket marked as Spam by an Automation rule such as the Ticket Creation or Ticket Updates.&nbsp;</li><li >Any ticket raised by a "deleted contact" in Freshdesk would go to Spam automatically.</li></ul><p dir="ltr">To have this resolved, kindly ensure that there are no automation rules that would mark tickets as Spam automatically and also make sure that the contact is restored from the Deleted list under the Customers tab.<br /><br />If you believe that a ticket was not marked as spam from the customer end, you can navigate to your spam folder, unspam it, and check how the ticket was marked as spam in the "Show activities" option in the top right corner.&nbsp;</p><p ><br /></p><p ><span dir="ltr" style={{ lineHeight: "normal", whiteSpace: "pre-wrap" }}><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></span></p></div></div></div>

</details>

<details>
<summary>Will agents be able to respond to tickets on their smartphones using Freshdesk?</summary>

<p>Yes, we do have an Agent specific Freshdesk Mobile app for IOS and Android. You can download the App from the App store/ Play store respectively.</p>

</details>

<details>
<summary>어떻게 view deleted tickets?</summary>

<p ><span style={{ fontSize: "14px" }}>To access the deleted tickets on the helpdesk, navigate to the <strong>Tickets</strong> section and click on the hamburger icon and in there, Choose <strong>Trash</strong> (under the "List View Names" dropdown). You can also find the conversations from a deleted user in the <strong>Spam</strong> folder. </span></p><p ><br /></p><p ><img class="fr-dib fr-draggable fr-bordered" src="#" style={{ width: "196px", height: "143.519px" }} /></p><p ><br /></p><p ><br /></p><p ><span style={{ fontSize: "14px" }}></span></p><p ><img class="fr-dib fr-draggable fr-bordered" src="#" style={{ width: "198px", height: "407.227px" }} /></p><p ><br /></p><p ><br /></p><p ><br /></p><p ><span style={{ fontSize: "14px" }}>You can <strong>Restore, Not spam</strong> or <strong>Delete Forever</strong> those listed tickets, under these ticket views.</span></p><p ><span style={{ fontSize: "14px" }}>Also, tickets in the <strong>trash</strong> folder for more than 30 days will be permanently removed from the portal.</span></p>

</details>

<details>
<summary>어떻게 view the Archived Tickets on my account?</summary>

<p>Any closed ticket with no updates for the past 120 days would be marked as <strong>Archived</strong>. These tickets would be part of the archived tickets list on your helpdesk.&nbsp;</p><p><span style={{ fontSize: "14px" }}><br /></span></p><p>Please go to the Tickets tab and click on the view list &gt; choose <strong>Archive</strong> (under the 'List View Names' dropdown) to see all the archived tickets in the portal.&nbsp;</p><p><br /></p><p dir="ltr">Alternatively, you can access the archived tickets by performing a search in your helpdesk or by directly hitting the ticket ID in the URL. <strong style={{ boxSizing: "border-box", fontWeight: "700" }} dir="ltr"></strong>Under the Global search, if you want the Archived tickets to show up, you have to manually change the search settings to include the archived tickets if required. By default, this option will be turned off.</p><p><br /></p><p>If you are using Freshdesk on Mint, clicking on the Archive view will take you to a page where you can apply the required filters and then export the file to your agent mailbox.</p><p><br /></p>

</details>

<details>
<summary>방법 필터 tickets by creation date?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}>Ticket List Views enable you to group tickets based on a defined set of criteria. You can filter out tickets by source, type, status, assigned agents, tags, products, and even the custom fields&nbsp;</span><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>(dropdown and dependent fields only)</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;you have created. This way, agents can set their priorities and stay customer-centric. Besides these, agents can use the Ticket List Views for changing ticket owners, deleting tickets in bulk, or export the ticket list to a CSV file.<br /><br /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>If you wish to filter tickets based on their date of creation follow the steps below,</span></span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Tickets</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;tab from the menu.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Filters</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;panel on the right, and choose the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Select time period</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;option from the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Created</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;dropdown.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Under the Time period option, select the from and to dates and click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Update</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Now click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Apply</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;button to filter tickets.</span></span></p></li></ol><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginLeft: "36pt", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}><span style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "313px", fontFamily: "Arial"" }}><img alt="How to filter tickets based on creation date in Freshdesk?" title="Filter tickets based on creation date in Freshdesk." src="#" width="624" height="313" class="fr-fic fr-dii fr-bordered fr-shadow" style={{ fontFamily: "Arial"" }} /></span></span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><pre class="fd-callout fd-callout--note" dir="ltr" style={{ fontFamily: "Arial, Helvetica, sans-serif" }}><span style={{ fontFamily: "Helvetica Neue" }}><strong style={{ fontFamily: "Arial"" }}>Note :</strong> Filtering tickets based on a custom date field is not possible.</span></pre>

</details>

<details>
<summary>Is there an option to add more than one email address in 'TO' when replying?</summary>

<p >Since we map the 'To' address based on the requester of the ticket and because there can only be one requester for a ticket, you will not be able to add more than one email address in the 'To' field. You can however add the email addresses in the CC field. </p>

</details>

<details>
<summary>어떻게 내보내기 my tickets from Freshdesk?</summary>

<p dir="ltr"><br /></p><p dir="ltr">Agents can export tickets, contacts, companies, or granular account data easily, and quickly download it anytime, from a centralized window.To export the tickets from your helpdesk, please navigate to the <strong >Tickets</strong> tab and choose the pre-existing '<strong >All tickets</strong>' view from the ticket list page.</p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style={{ width: "238px", height: "380.625px" }} /></p><p ><br /></p><p ><span dir="ltr" style={{ color: "rgb(0, 0, 0)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>You can then choose and apply all the necessary filters such as the created time, agents, groups, type, status etc on the right and set up your filter to display the exact set of tickets you want to export then click on&nbsp;</span><strong style={{ boxSizing: "border-box", fontWeight: "700", color: "rgb(0, 0, 0)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", textAlign: "start", textIndent: "0px" }}>Export</strong><span style={{ color: "rgb(0, 0, 0)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>&nbsp;from the top right corner.</span></p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style={{ width: "757px", height: "64.9411px" }} /></p><p ><br /></p><p >When you click '<strong >Export</strong>', a slider opens out. Here, you can choose the format of the file (<strong >CSV or Excel</strong>) along with desired ticket fields that should be included in the ticket export. Expand the '<strong >Show multiline text fields</strong>' option on this slider to choose to export the '<strong >Description</strong>' or any other custom multiline text field.</p><p ><br /></p><p class="article_note" dir="ltr"><strong >Note</strong>: The time frame set on the ticket list page has to be greater than the time frame set in the Export window. It is recommended to set the Created time field as '<strong >Any time</strong>' on the list page and apply the desired time in the export window. You'll notice that the export function now fetches tickets based on the filter you've applied, ensuring you get precisely the data you're looking for.</p><p ><br /></p><p >This export will NOT give you the entire conversation from the ticket or historical data (archived tickets) - for that, you will have to perform an <a href="https://support.freshdesk.com/support/solutions/articles/225487-how-do-i-export-my-helpdesk-data-" rel="noopener noreferrer" target="_blank">account export</a>.</p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style={{ width: "509px", height: "584.045px" }} /></p><p ><br /></p><p dir="ltr"><br /></p><p dir="ltr">To view previously exported data from your helpdesk, please navigate to Admin &gt; Accounts exports. From here, you can see the export history.&nbsp;</p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}>&nbsp;</p><p dir="ltr">You can also see the progress of downloads and directly download the file from this page.<br />&nbsp;</p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "12pt", fontFamily: "Arial", color: "rgb(51, 51, 51)", fontWeight: "400" }}><span style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "199px" }}><img src="#" width="624" height="199" class="fr-fic fr-dii" /></span></span></p><p dir="ltr"><br />A window pops up when you click on the Details button which provides details about the export. The agent can easily see information like the selected time period, ticket fields, contact fields, company fields, and other information from here.&nbsp;</p><p ><br /></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "12pt", fontFamily: "Arial", color: "rgb(51, 51, 51)", fontWeight: "400" }}><span style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "315px" }}><img src="#" width="624" height="315" class="fr-fic fr-dii" /></span></span></p><p class="article_note" ><br /></p><p class="article_note" dir="ltr"><strong dir="ltr">Note:&nbsp;</strong>If the '<strong >Export</strong>' option is missing for you, it is possible that your Admin has restricted it by setting up a custom role. This setting can be changed under <strong >Admin &gt; Roles</strong> by an Admin.<br /><br /></p>

</details>

<details>
<summary>방법 respond to multiple tickets with a common reply?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Freshdesk offers the following features to respond to multiple tickets with a common reply.</span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Bulk Update option from Ticket list views</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Canned Responses</span></span></p></li></ol><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>The 'Bulk Update’ option from the Ticket list view page enables you to assign a selected set of tickets (maximum of 30 tickets per page) to an Internal group and agent. Please follow the steps below to make bulk updates on tickets in Freshdesk,</span></span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Tickets</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;tab from the menu.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "11pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Select the tickets you want to perform bulk actions on the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Ticket List View page.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "11pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Bulk Update&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>option from the top menu bar.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "11pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Provide a&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>reply message</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;and update the respective&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>ticket status</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>,&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>internal group</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>, and&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>agent</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "11pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span dir="ltr" style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Update</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;to execute this action.</span>&nbsp;</span><br /><br /></p><p><img src="#" style={{ width: "655px" }} class="fr-fil fr-dib fr-bordered fr-shadow" /></p><p></p></li></ol><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><br /><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>With&nbsp;</span><a href="https://support.freshdesk.com/en/support/solutions/articles/37579-using-canned-responses-in-ticket-replies" style={{ fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none", fontFamily: "Arial"" }}>Canned Responses</span></a><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>, your agents can create a predefined set of reply templates they can send out with a single click.</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><a href="https://support.freshdesk.com/en/support/solutions/articles/52630-understanding-dynamic-content-and" style={{ fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none", fontFamily: "Arial"" }}>Using dynamic content placeholders</span></a><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>, agents can ensure customization of each response with the requester's name, agent's signature, and ticket details.&nbsp;</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Here is a detailed demonstration of&nbsp;</span><a href="https://www.youtube.com/watch?v=IlXPXJjsPwc" style={{ fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none", fontFamily: "Arial"" }}>using canned responses in ticket replies</span></a></span><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;on youtube for your reference.</span></p>

</details>

<details>
<summary>How many tickets 할 수 있나요 link to a tracker?</summary>

<p>You can associate upto 300 tickets to a single tracker.</p>

</details>

<details>
<summary>할 수 있나요 download attachments using a Public Ticket URL without being logged in?</summary>

<div dir="ltr"><div dir="ltr"><p><span style={{ fontFamily: "Arial", lineHeight: "18.4px", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>Kindly note that only logged in users would be able to download attachments, even while using the Public Ticket URL. This would be the default behavior of the system to ensure data security and confidentiality.</span></span></p></div></div>

</details>

<details>
<summary>Can details apart from the contact details in Freshdesk be retrieved for a particular requester?</summary>

<p>Third party tools such as Salesforce.com or Zoho CRM can be integrated into Freshdesk, using which contact information from those CRM tools could be brought into Freshdesk. This contact information would be made visible as part of the Requester Info section as well.</p>

</details>

<details>
<summary>할 수 있나요 receive a sound 알림 when a new ticket comes in?</summary>

<div dir="ltr"><div dir="ltr"><p><span dir="ltr" style={{ fontSize: "14px" }}>There is a feature called smart notifications for agents within the portal itself which would give real-time audible<strong>&nbsp;notifications&nbsp;</strong>about new tickets and updates on the ones you are working on. You can open the Notification Center by clicking on the bell icon from the navigation bar next to search.&nbsp;</span></p><p><br /></p><p><span dir="ltr" style={{ fontSize: "14px" }}><img src="#" style={{ width: "298px" }} class="fr-fic fr-fil fr-dib" /></span><br /></p><p><br /></p><p><span dir="ltr" style={{ fontSize: "14px" }}>You could choose the ones you want to get these alerts for by clicking on the desktop icon in the notification center. You could enable <strong>desktop notifications&nbsp;</strong>in this window.</span></p><p><br /></p><p><img src="#" style={{ width: "621px" }} class="fr-fic fr-fil fr-dib" /></p><p><br /><span style={{ fontSize: "14px" }}>Muting is possible by turning on the "silent notifications" within the Preferences tab.&nbsp;</span><br /><br /><span dir="ltr" style={{ fontSize: "14px" }}>For detailed information please refer to <a href="http://%20Built-in%20smart%20notifications%20for%20Agents">this</a> article.</span></p></div></div>

</details>

<details>
<summary>할 수 있나요 일정 a recurring ticket in Freshdesk ?</summary>

<div dir="ltr"><div dir="ltr"><div dir="ltr"><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>As of now, we do not have the ability to schedule recurring tickets. However, as a workaround, you could make use of any third party event scheduler like </span></span><a href="https://support.freshdesk.com/support/solutions/articles/77059-the-google-calendar-app" style={{ fontSize: "medium" }} target="_blank">Google Calendar</a><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}> to trigger an email to the support email address whenever an event is due.</span></span></p><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}><br /></span></span></p><p><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>In that way, you wouldn't miss out on any notification as they would all come in as new tickets on your portal.</span></span></p></div></div></div>

</details>

<details>
<summary>방법 remove ticket number that appears in the subject?</summary>

<div dir="ltr"><div dir="ltr"><p ><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>Ticket numbers appear in the subject of email notifications because of the inclusion of ticket ID. </span></span></p><p ><br /></p><p ><span style={{ fontFamily: "Arial", whiteSpace: "pre-wrap" }}><span style={{ fontSize: "medium" }}>In order to remove this, please navigate to<strong dir="ltr"> Admin -&gt; Workflows -&gt; Email notifications</strong> -&gt;to modify the "Subject" of the email notification by removing the placeholder for "Ticket ID" - ```{{#123;`{{#123;ticket.id}}`#125;}}`#125;``.</span></span></p></div></div>

</details>

<details>
<summary>방법 undo ticket merging?</summary>

Merging is an irreversible process. Once two tickets are merged it cannot be split.

</details>

<details>
<summary>방법 automatically stop the Time Tracker?</summary>

<p><span style={{ fontSize: "14px" }}>The time tracker would automatically <strong>stop</strong> under the following instances:</span></p><p><span style={{ fontSize: "14px" }}></span><span style={{ fontSize: "14px" }}></span></p><ul><li><span style={{ fontSize: "14px" }}>When the status of the ticket is moved to Resolved/Closed.</span></li><li><span style={{ fontSize: "14px" }}>When the agent starts replying on another ticket.</span></li><li><span style={{ fontSize: "14px" }}>When the agent does an update to another ticket.</span></li></ul><p><br /></p>

</details>

<details>
<summary>On what time zone are the ticket counting timers based?</summary>

<p ><span dir="ltr" style={{ fontSize: "16px" }}>The timers are based on the Helpdesk time zone that can be configured according to your location. Please navigate to <strong>Admin -&gt; Account -&gt; Helpdesk Settings</strong> to change the timezone. </span></p>

</details>

<details>
<summary>Ticket field that I created is not present in the filters</summary>

<p >The Single line text fields, Multi line text fields, Number fields and check boxes will not be available in the filters of the ticket list view page. </p>

</details>

<details>
<summary>방법 include ticket thread when forwarding conversation?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}>You can make sure that the entire ticket thread is visible to the person you forward it to by,</span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>enabling the '</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Public ticket URL</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>' option and&nbsp;</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontFamily: "Arial"" }}>inserting '<strong style={{ fontFamily: "Arial"" }}>Public ticket URL</strong>' placeholder</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;in <strong style={{ fontFamily: "Arial"" }}>Agent Forward Template</strong>.</span></span></p></li></ol><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Once done, when an agent clicks on the 'Forward' option, the public ticket URL will be visible to the person you forward it to, and they can view the complete ticket thread.</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>As an administrator, you can enable the '</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Public ticket URL</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>' option by following the steps below.</span></span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Admin</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;from the menu. Click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Channels</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>. Select&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Portals</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Under the Settings tab, navigate to the '</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Who can view tickets on portal'</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;section.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Select the option '</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Anyone with public ticket URL</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.'</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Click&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Save</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p><p><br /></p><img src="#" style={{ width: "645px" }} class="fr-fil fr-dib fr-bordered fr-shadow" alt="Changing portal settings to 'Anyone with public URL'" /><p></p></li></ol><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Users can now view tickets without logging in to your portal using the public ticket URLs.</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(51, 51, 51)", fontWeight: "400", fontFamily: "Arial"" }}>After enabling the</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;'Public ticket URL' option, you should now enable the corresponding placeholder in the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Agent Forward Template</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>. As an administrator of your Freshdesk account, here is how you can do it.</span></span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Admin</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;from the menu. Click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Workflows</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>. Select&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Email Notifications</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Under the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Templates</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;tab, click on the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Edit</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;button next to the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Agent Forward Template</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Place your cursor on the reply editor where you wish to position the Public ticket URL.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Click on the ‘</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Insert Placeholder</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>’ button. Under the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Tickets</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;tab, click on the ‘</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Public Ticket URL’</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;placeholder.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(14, 16, 26)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>Click&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "700", fontFamily: "Arial"" }}>Save</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></span><br /><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(14, 16, 26)", fontWeight: "400", fontFamily: "Arial"" }}><img src="#" style={{ width: "auto" }} class="fr-fil fr-dib" alt="Enabling the placeholder in the Agent Forward Template" /></span></span><span style={{ fontFamily: "Helvetica Neue" }}><br /><br /></span></p></li></ol><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial, Helvetica, sans-serif" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><br /></span></p>

</details>

<details>
<summary>어떻게 할 수 있나요 link an article to the reply of a ticket?</summary>

<p >Please navigate to the "<strong >Tickets</strong>" tab and open the ticket you would like to work on. Kindly click on the "Reply" button within the "<strong >Ticket Details</strong>" page, which will allow you to type your response. Among the various formatting options, you will find a "<strong >book</strong>" symbol that leads to the solution articles. You can either search for the relevant article or choose from the ones listed here.</p><p ><br /></p><p ><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /><br /></p><p dir="ltr">Ensure the article is visible in the customer portal when sharing an article link. &nbsp;Articles can also be inserted as a link or the complete content by clicking the "<strong>Insert</strong><strong >Content</strong>" or "<strong>Insert link</strong>" within the article suggestion.</p><p ><br /></p>

</details>

<details>
<summary>방법 change due by date of a ticket ?</summary>

<p >In the ticket details page, above the subject of the ticket, there is an option to manually edit the 'Due Date' of the ticket as shown below :</p><p ><br /></p><p ><img src="#" style={{ width: "auto" }} class="fr-fic fr-dib fr-bordered" /><br /></p><p ><br /></p><p >You can also change the SLA applied to this ticket under <strong dir="ltr">Admin &gt; Workflows &gt; SLA Policies.</strong> Once the changes are done, you can update some properties for that ticket so that the new SLA will get applied and the due by date will be changed accordingly.<br /><br /><br /></p><p ><strong>Note:</strong></p><p ><br /></p><p >1) The option to change the due date will only show up when the ticket is assigned to statuses that have the <strong>SLA timer ON</strong> (example: Open).</p><p ><br /></p><p dir="ltr">You can check which statuses have their SLA timers ON or OFF under <strong>Admin &gt; Workflows &gt; Ticket Fields &gt; Status</strong> field. Once a manual change is done to the Due Time of a ticket, it will not change again when the ticket properties (for example, a change in priority) are updated.</p><p ><br /></p><p >2) The due by date and time can always be updated only to a value greater than the First response time, that is the 'Response due' time on the ticket.</p><p ><br /></p>

</details>

<details>
<summary>무엇인가요 the E-commerce channel?</summary>

<p>When you are hosted on an online e-commerce store and would like the customer queries from those stores to create tickets within your Freshdesk account, you can make use of the E-commerce channel. You will have the option to <a href="https://support.freshdesk.com/support/solutions/folders/270315" target="_blank" rel="noreferrer noopener">integrate with your eBay account</a> and tickets will get created inside Freshdesk via your eBay shops.</p>

</details>

<details>
<summary>What are flags ? 어떻게 할 수 있나요 fliter using flags?</summary>

<p>Flags are default labels in Freshdesk. They appear in the ticket list view and inside the ticket details page when certain activities occur:</p><p><br /></p><p><strong>New</strong>: This flag shows on a ticket when an agent's response to the customer is pending. It remains until the first response/resolution isn't overdue.</p><p><br /></p><p><strong>Customer Responded: </strong>This flag displays when a customer responds to a ticket.</p><p><br /></p><p><strong>Overdue</strong>: This occurs when the ticket surpasses its resolution time without being resolved.</p><p><br /></p><p><strong>Response due:</strong> This flag appears when the agent's first response isn't sent within a specific time based on the SLA.</p><p><br /></p><p dir="ltr">These flags are default and hardcoded, unalterable or removable. Ticket filtering using these flags isn't an option as of now</p><p><br /></p>

</details>

<details>
<summary>무엇인가요 a ticket?</summary>

<p dir="ltr">Each customer query - be it an email, or a phone call that comes into your account is a ticket. The agent would then be able to click on the ticket to respond to the customer about their query.</p><p><br /></p><p>Tickets raised on your account could be viewed under the Tickets tab, from where you could access them.</p>

</details>

<details>
<summary>왜인가요 an Outbound email set to Close 상태 automatically?</summary>

<p>An Outbound email in Freshdesk is to be used for pro-active external communication directed at the customer. Only when the customer replies, the ticket created from this Outbound email would be considered as an active ticket and set to Open Status. In the meanwhile, the ticket created from this Outbound email would be marked Closed.</p>

</details>

<details>
<summary>When does a Tickets tab auto-refresh?</summary>

<p >In Freshdesk, the auto-refresh notification gives you non-invasive live updates on the ticket. This notification would show up when there is a property update within the ticket or when there is a reply/note added to the ticket. </p>

</details>

<details>
<summary>방법 change the 'From' email address of a ticket?</summary>

<p >While replying, you can use the drop-down arrow mark to choose the 'From' email address as shown in the image below:</p><p ><br /></p><p ><img class="fr-dib" src="#" style={{ width: "268px", height: "84.6761px" }} /></p><p ><br /></p><p >If you want to have a common email from which the replies are sent out, you can make use of the App '<a href="https://www.freshworks.com/apps/freshdesk/customize_from_email_address/" rel="noopener noreferrer" target="_blank">Common From email address</a>'</p>

</details>

<details>
<summary>What happens when the attachment size limit goes beyond the threshold?</summary>

<p>Freshdesk will allow tickets to be created even when the attachments are exceeding the limit - from the email service, we now allow tickets which have attachments upto 50MB to come in, however, all attachments above 20 MB limit will be dropped and this alert will be shown in the ticket - '<strong>Attachment(s) that exceed 20 MB limit have been dropped. Please reach out to the sender.</strong>'</p><p><br /></p><p>This way, the tickets get created and the agents are also notified about the status of the attachment(s).</p><p><br /></p><p><strong>Note:</strong> The limit is 20 MB for Blossom and above accounts. For Sprout and trial accounts, the threshold is 15 MB.</p>

</details>

<details>
<summary>How many child tickets 할 수 있나요 add to a parent ticket?</summary>

<p >You can add up to a maximum of 10 child tickets to a parent ticket.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 delete an archived ticket?</summary>

<p>In order to delete an archived ticket, please go to the corresponding ticket page (either by performing a Search or hitting the ticket ID directly in the URL). Here, you will find the '<strong>Delete forever</strong>' button. Clicking on this button will <strong>permanently delete</strong> the ticket from the helpdesk. </p><p><br /></p><p>This option is only available on Freshdesk Mint.</p>

</details>

<details>
<summary>방법 change the subject of a ticket?</summary>

<p dir="ltr">Inside the ticket details page, click on the three-dotted icon-&gt;select the '<strong>Edit ticket details</strong>' option to edit the subject of the ticket as shown below:</p><p><br /></p><p><img src="#" style={{ width: "auto" }} class="fr-fil fr-dib fr-bordered" /></p><p><br /></p>

</details>

<details>
<summary>When I 내보내기 the tickets for a certain period of time, why don't I get the full count in 내보내기?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontSize: "14px" }}>The ideal way to export tickets is to set the time range under the '<strong>Filter Tickets By</strong>' section in the '<strong>Export Tickets</strong>' section. First, choose the preferred file format, set the desired range select the required fields to export and click '<strong>Ex</strong><strong>port</strong>'. Ensure that the <strong>FILTERS</strong> section in the Tickets list view does not have any date range specified (or) set as <strong>Any time</strong>. If any date range is set there, the export will only include tickets from that specified range.</span></p><p><br /></p><p><br /></p><p><br /></p><p dir="ltr">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img src="#" style={{ width: "341px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-fic fr-dib" /></p><p><br /></p><p><br /></p><p dir="ltr">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img src="#" style={{ width: "549px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-fic fr-dib" /></p><p><br /></p>

</details>

<details>
<summary>My ticket shows 'Response Due' though it has a response already</summary>

<p>Please check if the ticket has a private note/ Forward (Check for a lock symbol next to the note) or if it has a public note/ reply. If the reply is private then it would not be considered as a response by Freshdesk, because it is not displayed to the customer.</p>

</details>

<details>
<summary>어떻게 delete multiple tickets from same person?</summary>

<p dir="ltr">Using Search bar, search for the Requester email address and navigate to <strong>Contacts</strong> tab and click <strong dir="ltr">Show tickets from &lt;contact_name&gt;</strong>.</p><p><br /></p><p><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /><br /><span dir="ltr" style={{ color: "rgb(0, 0, 0)", fontFamily: "-apple-system, ", fontSize: "13px", fontWeight: "400", textAlign: "left", textIndent: "0px", display: "inline !important" }}>You can use bulk actions to delete the tickets (30 tickets at a time) to delete all the tickets associated to the requester email address.</span><br /><br /><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p>

</details>

<details>
<summary>방법 remove CC from a ticket?</summary>

<p>To remove the CC from a ticket you need click on the Reply option &gt; select the addresses in the cc bar and click on the 'x' mark next to it and send the reply. Once removed, the CC address would not appear in the next replies unless added again by the requester or one of the agents manually.&nbsp;</p><p><br /></p><p dir="ltr">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p>

</details>

<details>
<summary>What will be the impact on existing tickets if we 업데이트하다 some dropdown fields?</summary>

<p >When you remove an item or option from the Dropdown field, this would automatically remove the value from the tickets and reports as well. The same happens when you rename or make any changes to the values of the field.</p><p ><br /></p><p dir="ltr">The process that needs to be followed would be to create a new value in the same Dropdown field and Bulk change the values in all the tickets that you need. Once this is done, you can remove the value from <strong>Admin &gt; Workflows &gt; Ticket fields</strong>.</p>

</details>

<details>
<summary>Automatically track the time spent on tickets</summary>

<p>You can make use of the <strong>Auto Start Timer</strong> App to calculate the time spent on tickets based on the statuses you set. To know more about this check out the <a href="https://www.freshworks.com/apps/freshdesk/auto_start_timer/" rel="noopener noreferrer" target="_blank">link</a>.</p>

</details>

<details>
<summary>할 수 있나요 re-open an archived ticket?</summary>

<p >No, you will not be able to change the status or reopen an Archived ticket.</p>

</details>

<details>
<summary>할 수 있나요 unsplit a ticket?</summary>

<p>Make use of the <a href="https://support.freshdesk.com/en/support/solutions/articles/80180">merge feature</a> in Freshdesk to merge the conversations from a secondary ticket to the primary ticket. If once split, you can merge the reply into the original ticket using this feature.</p>

</details>

<details>
<summary>When opening ticket the page scrolls down to latest reply</summary>

If a ticket is assigned to you, then when you access that ticket you will be taken to the latest response automatically. However, this would not be the case when you are viewing a different agent's ticket.

</details>

<details>
<summary>Tickets page keeps loading in Freshdesk</summary>

<p >Please follow the steps below so that we could identify the reason for the same.</p><ul><li >Try accessing the account in the 'Incognito' window of your browser. If this works clear the cache and cookies of the browser and that should do the trick. </li><li >Try in different browsers. This will help us identify if this is a browser specific issue. </li><li >If both the above steps do not work then check the issue on a different network and let us know if that helps (A mobile hotspot should help with this).</li><li >Check out our status page which is <a href="https://updates.freshdesk.com/" rel="noreferrer">https://updates.freshdesk.com/</a> to know if there are currently any issues. </li></ul><p >If none of the above works, please raise a ticket with us so that we could have this checked for you. </p>

</details>

<details>
<summary>Where is the Spam folder?</summary>

<p>You can access the 'Spam' folder by clicking on the hamburger menu in the Ticket list page. </p><p><br /></p><p><img src="#" style={{ width: "262px" }} class="fr-fic fr-dib fr-bordered" /></p><p><br /></p><p>You'll be able to see all the default and custom ticket views of your helpdesk here. Click on 'Spam' to go to the Spam view.</p><p><br /></p><p><img src="#" style={{ width: "172px" }} class="fr-fic fr-dib fr-bordered" /></p>

</details>

<details>
<summary>How did a ticket land in the spam folder?</summary>

<p ><strong>G</strong><strong>iven below are the ways in which a ticket gets spammed</strong> :</p><p >1) An agent can mark the ticket as spam manually. </p><p >2) An automation rule would have acted upon the ticket. </p><p >3) The contact of the ticket would have been deleted or blocked. Restore the ticket &gt; click on the <strong>Activities</strong> at the top right corner and check as to why the ticket has been spammed. Once you restore the contact, all future emails from the contact will come through as tickets.</p><p ><br /></p><p >If none of these were the reasons when checking the Activities please reach out to support@freshdesk.com and we would be glad to help you out.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 내보내기 tickets including the content of the ticket?</summary>

<p dir="ltr">There are multiple ways you can export the tickets with its content.</p><ol ><li dir="ltr">You can print the ticket and save it as a PDF on your system. (OR)</li><li dir="ltr">The Account Admin can export all the data within your account (including tickets, solution articles, etc.) from the Admin section:</li></ol><ul style={{ marginLeft: "40px" }}><li dir="ltr">Navigate to Admin &gt; Account &gt; Account Details.</li><li dir="ltr">Click Export</li><li dir="ltr">The data will be exported to the account administrator's email in XML format. You can then convert the XML data into your preferred format.</li></ul><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}>Watch <a href="https://www.youtube.com/watch?v=DTa_LDg8vng&amp;list=PLsYJ3BsyR4qGFujlW0iDtOBOf4IPVsAqt&amp;index=11" rel="noreferrer" target="_blank">this</a> video for steps to export the account data.</p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><br /></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><br /></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><br /></p>

</details>

<details>
<summary>I am not able to merge a ticket to a child ticket</summary>

<p >When the ticket has an association such as Parent/Child, you will not be able to add another association to it such as linking the ticket to a tracker or merging. </p><p><br /></p>

</details>

<details>
<summary>Is there a possibility to lock a ticket while one agent is answering and working on that?</summary>

<p>The primary step that needs to be taken in such a case would be to assign the ticket to the agent working on the ticket or he/she can pick it up from the list view itself. Each of your agents can have filters to view the tickets that are their names. The Agent collision feature would notify anyone if a different agent is view or replying to that ticket currently.</p>

</details>

<details>
<summary>할 수 있나요 unarchive a ticket?</summary>

Once the ticket is archived you will not be able to make any changes to the ticket. The archiving with take place only on tickets that has been in the Closed status for more than 120 days with no activity on the ticket. If you have tickets that need to be reopened in future then set them in a different status other than Closed.

</details>

<details>
<summary>방법 modify a parent child association ?</summary>

<p>It would not be possible to unlink a child ticket or link it with another parent. Child tickets are created with the association to the parent ticket and the only option would be to have it closed once it is done. You would have to create a new child ticket to be associated with the other parent ticket.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 see drafts by another agent?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontFamily: "Arial"", fontSize: "16px" }}>The draft feature is for each agent; the draft saved by one of the agents cannot be viewed by another.&nbsp;</span></p><p dir="ltr"><br /></p><pre class="fd-callout fd-callout--note" dir="ltr"><strong>Note:</strong> The drafts on the ticket reply editor will be available only for <strong>24 hours</strong>. They will not be available if the agents are drafting the response as a public/private note.</pre><p><br /></p><p dir="ltr"><span dir="ltr" style={{ fontFamily: "Arial"", fontSize: "16px" }}>Using the <a href="https://support.freshdesk.com/en/support/solutions/articles/218073" rel="noopener noreferrer" style={{ fontFamily: "Arial"" }} target="_blank">Agent Collision</a> feature, you can see if another agent is already viewing or replying to a ticket in real-time. This feature is particularly useful for teams working on urgent or complex tickets, as it allows multiple agents to work on the same ticket simultaneously.</span></p><p><span style={{ fontFamily: "Arial"", fontSize: "16px" }}><br /></span></p><p dir="ltr"><br /></p>

</details>

<details>
<summary>If I resolve a tracker ticket, do all the tickets linked to it will become resolved?</summary>

No, resolving the tracker ticket would not resolve the linked tickets by default. You have to manually resolve this as you might need to update your customers before resolving the tickets.

</details>

<details>
<summary>방법 protect your helpdesk from spam attack?</summary>

<p >In Freshdesk, we provide few options to protect your helpdesk from any possible spam tickets coming from sources like Portal and Email.</p><p ><br /></p><p dir="ltr">For spam tickets created via Portal, &nbsp;enable CAPTCHA on your customer support portal. Navigate to <strong dir="ltr">Admin &gt; Channels &gt; Portals &gt; Edit &gt; Manage sections</strong> and select the <strong >'Enable CAPTCHA to help avoid spam'</strong> option.</p><p ><br /></p><p ><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p ><br /></p><p >For spam tickets coming via Email, we enable Proactive Spam Filter from the backend. This spam filter will check all the tickets coming through the Email channel and based on certain pre-defined conditions, a spam score will be associated with each incoming email ticket. If the spam score of the email is 6 and above, the tickets will be marked as a spam automatically.&nbsp;</p><p ><br /></p><p >The purpose of this feature is to ensure that you have optimum spam deflection. However, please note that there are chances that some valid emails can be marked as spam, if in case these emails arrive via a Spam reporting IP or with a high spam score. You could keep track of those tickets in the Spam folder inside the Tickets tab in Freshdesk and restore them if you deem that they are valid.</p><p ><br /></p><p >If you would like this feature to be enabled for your account, please drop an email to <a href="mailto:support@freshdesk.com" rel="noreferrer noopener">support@freshdesk.com</a>. We'd be glad to assist.</p>

</details>

<details>
<summary>What each default SLA flag means on the ticket page</summary>

<p>Freshdesk, by default, classifies tickets with 4 specific flags. These flags help agents quickly take notice of the ticket in question and perform necessary actions.</p><p><br /></p><table style={{ width: "57%", marginRight: "calc(43%)" }}><tbody><tr><td style={{ width: "33.4773%" }}><strong>Flag</strong></td><td style={{ width: "66.3067%" }}><strong>Description</strong></td></tr><tr><td style={{ width: "33.4773%" }}><div><img src="#" class="fr-fic fr-dii" style={{ width: "43px" }} /></div></td><td style={{ width: "66.3067%" }}>Represents all new tickets created on the helpdesk</td></tr><tr><td style={{ width: "33.4773%" }}><div><img src="#" class="fr-fic fr-dii fr-fil" style={{ width: "131px" }} /></div></td><td style={{ width: "66.3067%" }}>Represents tickets the customer has responded to</td></tr><tr><td style={{ width: "33.4773%" }}><div><img src="#" class="fr-fic fr-dib fr-fil" style={{ width: "90px" }} /></div></td><td style={{ width: "66.3067%" }}>Represents tickets for which the first response SLA has been violated</td></tr><tr><td style={{ width: "33.4773%" }}><div><img src="#" class="fr-fic fr-dib fr-fil" style={{ width: "63px" }} /></div></td><td style={{ width: "66.3067%" }}>Represents tickets for which the resolution SLA has been violated</td></tr></tbody></table><p><br /></p><p class="article_note"><strong>Note:</strong> These flag values are hardcoded and cannot be edited. You will not be able to filter tickets based on these flags.</p>

</details>

<details>
<summary>Receiving spam emails to support@domain.freshdesk.com, Please help!</summary>

<p >We have been reported of multiple cases where the Russian Spammers usually create spam tickets by sending an email to the generic forwarding address. And this issue is not just specific to Freshdesk and it has been prevalent across all the helpdesk softwares like Zendesk, HelpScout as well. &nbsp;</p><p ><br /></p><p dir="ltr">The spammers identify the generic forwarding address [like support@domain.freshdesk.com or info@domain.freshdesk.com or help@domain.freshdesk.com] and they create these spam tickets. So, using a generic forwarding address makes an account vulnerable to spam influx. &nbsp;</p><p ><br /></p><p dir="ltr">To mitigate such spams, there is a feature called <strong >'Prevent Wildcard Ticket Create'</strong> where only emails directly sent to the email address configured under the Email config page in Freshdesk will be converted into tickets. Please go to <strong>Admin &gt; Channels &gt; Email &gt; Advanced Settings</strong> and disable <strong>'Allow emails to be sent to the wildcard support address'</strong></p><p dir="ltr"><br /></p><p dir="ltr">Also, we would recommend using domain-specific email addresses like support@domain.com or help@domain.com [emails having your company's domain name] to avoid such issues. Using a domain-specific email address is going to be more advantageous for your business for the following reasons</p><ol><li dir="ltr">It will help you brand the emails and replies sent by your organization from Freshdesk.&nbsp;</li><li dir="ltr">It will allow you to have greater flexibility and control as to which emails need to be converted as tickets and so.&nbsp;</li><li dir="ltr">It will be of help if you would like to use your own mail server to relay emails from and to Freshdesk through our Custom mail server feature.&nbsp;</li><li dir="ltr">Your stakeholders will be able to receive emails authenticated by your own domain using the <a href="https://support.freshdesk.com/en/support/solutions/articles/223779">DKIM</a> feature which ensures proper end-to-end email delivery.</li></ol><p dir="ltr"><br /></p><p dir="ltr">If you have any further queries, please drop us an email at support@freshdesk.com.</p>

</details>

<details>
<summary>방법 stop tickets from being redirected to Ticket List View every time a ticket is closed?</summary>

<p>When the agent sends a reply and resolves or closes the ticket using the 'Send and set as resolved' or 'Send and set as closed' options, the page will be automatically redirected to the Ticket List View. </p><p><br /></p><p>This is the default behavior of the system designed to help the agents to view the other tickets in their queue without any additional clicks. <br /><br />If you do not want the page to be redirected to the Ticket List View upon closing the tickets, you can update the status of the ticket from the Ticket Properties section instead of using the 'Send and set as Resolved/Closed' options. </p>

</details>

<details>
<summary>Is there an option to undo a sent reply?</summary>

<p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>Clicked on ‘<strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Send</strong>’ even before the email was ready to go out to the customer? If you’re on the <strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Blossom or above plan</strong>, you can use the ‘<strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Undo Send</strong>’ button <strong style={{ boxSizing: "border-box", fontWeight: "700" }}>within 10 seconds</strong> of replying to stop it from going out.<br /><br /></p><p ><span style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>Agents will have to enable this option by clicking on their&nbsp;</span><strong style={{ boxSizing: "border-box", fontWeight: "700", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", textAlign: "start", textIndent: "0px" }}>profile picture icon on the top right corner &gt; Profile settings</strong><span style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>&nbsp;and then toggle the feature&nbsp;</span><strong style={{ boxSizing: "border-box", fontWeight: "700", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", textAlign: "start", textIndent: "0px" }}>ON</strong><span style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>:</span></p><p ><span dir="ltr" style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></span><br /><br /></p><div style={{ boxSizing: "border-box", wordBreak: "normal", overflowWrap: "break-word", fontSize: "13px", lineHeight: "18px", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><br /></div><p ><span style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}>Once this is enabled, agents will start seeing the Undo option in the reply panel after they send out replies.</span></p><p ><br /></p><p ><span dir="ltr" style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontSize: "13px", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></span><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><br /><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, system-ui, ", fontWeight: "400", textAlign: "start", textIndent: "0px" }}><strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Note:</strong> The ‘Undo’ option is available only for replies. And, it will not be possible to undo the replies sent using the 'Send and set as' option.</p>

</details>

