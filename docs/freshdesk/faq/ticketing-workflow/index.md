---
sidebar_position: 1
---

# 티켓 워크플로우 FAQ

티켓 워크플로우에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>How do I create a custom ticket view?</strong></summary>

You can create a view from the **Tickets tab,** where you have to filter out the fields that is required and at the top of the page you would see the **Save as** option.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/39634555/original/7K5hBnV1Osn-7GCFBROXuqDf2219byXgew.png?1531285257)Once that is clicked you can save the new view under a different name.

</details>

<details>
<summary><strong>Where is the option to forward a ticket ?</strong></summary>

The **Forward** option for a ticket will be inside the **Ticket details page** as shown below:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/39864946/original/r69YoGytSM3eMce1zbAkDEtffdKw9js-2Q.png?1532494295)

</details>

<details>
<summary><strong>What is the maximum size of a file that can be attached to a ticket ?</strong></summary>

You will only be able to attach a maximum size of 20MB when receiving an email and for replies sent out of Freshdesk.

</details>

<details>
<summary><strong>What is the size limit for attachments to a ticket reply?</strong></summary>

Freshdesk lets you send and receive emails with an attachment size limit of **20 MB**/conversation for accounts on the Blossom and above plans. For Sprout and trial accounts, the attachment size limit is 15 MB.By default, the content of the email (excluding attachments) has a 15 MB limit per conversation.However, if you are looking to attach bigger files, you can use **Dropbox** as a workaround. Once you integrate Freshdesk with Dropbox, you can hotlink any file from your Dropbox account (with unlimited file size), and use it as an attachment inside Freshdesk. This file can be directly opened from Dropbox whenever someone clicks on it, and will not be stored anywhere on our end. Another alternative is **OneDrive** which could also help you add files with a greater MB value.**참고:** We do not recommend that you use heavy HTML content inside your tickets. Instead, you can attach them as separate files inside the ticket just like any other attachment.

</details>

<details>
<summary><strong>What are tags? How can I add/merge tags?</strong></summary>

As an agent when you are working on tickets or accessing articles, characterizing them by adding a tag would help to track and segregate them with respect to issues or requests.Go to **Admin > Agent Productivity > Tags > Add tag** and add the required tags for the helpdesk. Each tag has a **character limit of 32**.Once a tag is created, you can associate it with Tickets, Contact, and Articles. You can merge two tags by editing one of the tags and giving it the same name as the other.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/45887725/original/UIQLz8DDhc97PUr-WGyIj4c3hejTjVJtxA.png?1560315549)Upon adding a tag:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/45887734/original/CIPpey0qHA45opF28OJxiBdEwDRrykpgVg.png?1560315603)

</details>

<details>
<summary><strong>How do I add a tag to a ticket?</strong></summary>

The '**Tag**' field will be available under the '**Ticket Properties**' panel on the right hand side of the ticket details page. You can either manually type out and create new tags or add existing ones to tickets.If you are using Freshdesk on Mint, the '**Add tag**' option will be available above the main message/description of the ticket, in the ticket details page:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/39866627/original/lpPe5SvkQJ19Ib2NYdAssdp_7hmnb2TWhQ.png?1532500753)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009244120/original/HADEO8kuQpmRLFbJv9yzfGovgid9AO83Cw.png?1692717064)

</details>

<details>
<summary><strong>Can I add tags automatically?</strong></summary>

You can add tags manually and/or automatically. Add them manually inside a ticket or go to **Admin > Agent Productivity > Tags** to add/see the list of tags and the corresponding ticket count.[Add tags automatically using automations rules](https://support.freshdesk.com/en/support/solutions/articles/207276). Note that in a Supervisor rule, the tag will be added only after an hour if there is no other time-related condition.

</details>

<details>
<summary><strong>Can I attach multiple files while replying to a ticket?</strong></summary>

You can attach multiple files from your system while replying to a ticket. However, for trial accounts and accounts that are on the Sprout plan, the total file size of all the attachments together should not exceed 15 MB. For accounts that are on the Blossom and above plans, the attachment size limit is 20 MB.

</details>

<details>
<summary><strong>Would it be possible to add attachments that are more than 20 MB in size?</strong></summary>

The attachment size limit in Freshdesk is 20 MB per email for accounts on the Blossom and above plans and 15 MB for Sprout and accounts that are on Trial.This can be extended by making use of third party integration tools such as [](https://support.freshdesk.com/support/solutions/articles/210996-the-google-drive-app-part-1-developer-console-settings)[Dropbox](https://support.freshdesk.com/support/solutions/articles/55359-the-dropbox-app) and [OneDrive](https://support.freshdesk.com/support/solutions/articles/213938-the-onedrive-app).

</details>

<details>
<summary><strong>I want to insert a footer into all my replies. How do I do this?</strong></summary>

You can insert **footers **into all the ticket replies going out of your helpdesk, by adding them in the Agent Reply Template. This template is automatically included in all agent replies, whenever they respond to tickets. To do this- Please log in to your Freshdesk account as an Administrator
- Go to **Admin > Workflows > Email Notifications**
- Click on the** Templates** tab **>** **Agent Reply Template** and add the footer message to the content of the template

</details>

<details>
<summary><strong>How to close a ticket without sending an email notification to the customer?</strong></summary>

When you are working on tickets, we extend an option to **close **the ticket without an email notification sent out for this.This can be achieved by clicking on the **"closed"** button inside a ticket (details page) or on the list view which is basically "shift+close" and a notification would not be sent in this case.When you are completely affirmative that you do not want to send this out at all for any of the tickets, kindly navigate to**Admin > Workflows > Email Notifications > Requester Notifications > Turn OFF "Agent Closes the Ticket."**

</details>

<details>
<summary><strong>Is it possible to forward the ticket to an email address whenever a new ticket is created ?</strong></summary>

Yes, you could either set up a new rule under **Admin > Workflows > Automations > Ticket Creation** to add a CC whenever a new ticket is created, or you could add the user's email address under **Admin > Channels > Email > Advanced Settings > Set automatic Bcc email.**This email address would be automatically included in all helpdesk communications.

</details>

<details>
<summary><strong>How do I view the updates made to a ticket?</strong></summary>

After clicking on a ticket, please click on the Activities option to the top-right of the ticket details page. This would display the list of activities performed on the ticket in chronological order, which would contain information on updates made by each of these activities.

</details>

<details>
<summary><strong>How to exclude the full email thread in each customer reply to a ticket?</strong></summary>

When you are replying to a customer from inside a ticket, you can remove the quoted text manually and the customer will not receive the whole thread. Also, you can make use of the [Marketplace app](https://apps.freshdesk.com/remove_quoted_text/) to have the quoted text removed when the reply is added in Freshdesk.

</details>

<details>
<summary><strong>While merging tickets, is it possible to change the content of the auto response?</strong></summary>

Although the text that is added as a private note when two or more tickets are merged cannot be modified automatically, it still can be modified by the agent manually, by using the "Edit Note" option, while merging the tickets.The Agent will also be provided with the option to add it as a **public note** that would be visible to the requester.

</details>

<details>
<summary><strong>Is there a limit in the number of tickets you can have?</strong></summary>

There is no limit on the number of tickets that can be present inside your Freshdesk Account, under any plan.

</details>

<details>
<summary><strong>What is a Requester Widget?</strong></summary>

Requester Widget is a part of the ticket details page. This section would contain Requester Information such as Requester Name, Email Address, Company Name and any custom field which could be associated with this section.The Requester Widget gives more context about the requester to any agent working on the ticket. This functionality is available only from the Blossom plan onwards in Freshdesk.

</details>

<details>
<summary><strong>How do I add/remove the fields to be displayed on the requester widget?</strong></summary>

You can add or remove the fields being displayed as part of the requester widget, from under **Admin > Support Operations > Customer Fields >****Customize Requester Widget** option. You can also add company fields to be displayed within the Requester Widget.For more details, please refer to this article on setting up the [Requester Widget](https://support.freshdesk.com/support/solutions/articles/37586-driving-additional-context-with-requester-info).

</details>

<details>
<summary><strong>Can I edit the requester details directly from the requester widget?</strong></summary>

Except the **Email**, all the requester details can directly be edited from the widget. To edit the contact field values from within the Requester Widget, click on the "Edit" option within the Requester Info section. This would open a pop-up with the fields on the Requester Widget, from where you could edit the values of those Contact/Company Fields.

</details>

<details>
<summary><strong>Can a public note be changed to private?</strong></summary>

No, there is no option to change a public note that is already added into a private note. However, you would be able to delete the public note and add a private note from inside the ticket.

</details>

<details>
<summary><strong>How to change the requester’s email address in a ticket?</strong></summary>

Inside the Ticket details page, click on the **More button -> choose**** Edit **to find the option to edit the requester's email address.The **Edit **option would not be available for the tickets with Source as **Outbound email. **To edit the requester of an Outbound email ticket, you would have to change the Source of the ticket first under ticket properties.If you are using **Freshdesk on Mint**, you will find the 'More' option against the subject of the ticket. Clicking here will give you an option to 'Edit' the details of the ticket.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/45723483/original/8Es7--hzOkdywxmiiQUXQcHlNdAvOk_qKQ.png?1559542511)

</details>

<details>
<summary><strong>I am not able to add more custom fields to the requester widget?</strong></summary>

The upper limit to number of fields that could be added to the requester widget is 15. So, it would not be currently possible to add more than 15 fields to the Requester Widget.

</details>

<details>
<summary><strong>Is it possible to check the ticket history of a particular customer?</strong></summary>

In Freshdesk, you could view the most recent tickets raised by a requester, from within any of the the requester's tickets. To view this list, please click on the **Recent Tickets** option present within the requester widget. This would bring up all the past tickets from a particular customer.

</details>

<details>
<summary><strong>Can I see an email after its deleted from trash?</strong></summary>

A ticket will remain in the trash folder inside Freshdesk for 30 days and post which it will be permanently deleted automatically from the database. Once a ticket is deleted from the trash folder manually or automatically there is no option to restore the ticket.

</details>

<details>
<summary><strong>How can I create a view to see only the tickets I am working on?</strong></summary>

Once you start working with the product and develop a workflow where you are assigned tickets on a regular basis, you require an organized queue of the ones that need your attention. This is called a "view" - when you get tickets assigned to you, a filter can be applied by choosing "me" in the agent field and other properties could be changed to see your prioritized list.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008971548/original/7upAZZmXo-bpQ_MHYq5Oa9_mYR7m8mgsSQ.png?1690199186)Say, for instance, you are an agent who works on social tickets on a high priority - please choose the filters accordingly from the filters pane. You can also save the view if needed as **"Tickets I'm working on"**.

</details>

<details>
<summary><strong>How to sort my tickets such that the oldest tickets are on the top of the tickets queue?</strong></summary>

You have a good volume of tickets to handle on a daily basis and according to you, the tickets that have been sitting in the queue for a greater period of time would need your immediate attention. In this case, please explore the option of sorting in the tickets list view where the option that needs to be chosen is "date created" and in order to have the oldest tickets on top - please choose "ascending" along with this in the dropdown.Please note that this has many other options such as last modified, status, priority and due by date. Within that, you could choose ascending or descending.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008970943/original/vZzg_u5hRyoTmzpQKRmIfglef_jlcxttEw.png?1690196459)

</details>

<details>
<summary><strong>How does a ticket get marked as spam?</strong></summary>

There are three ways in which a ticket can end up in the Spam folder -1. Manually marked as Spam by an Agent.2. Ticket marked as Spam by an Automation rule such as the **Ticket creation** or the **Ticket Update **rule.3. Any ticket raised from a **deleted user in Freshdesk **would go to Spam automatically.

</details>

<details>
<summary><strong>How do I view deleted tickets?</strong></summary>

To access the deleted tickets on the helpdesk, navigate to the **Tickets** section and click on the hamburger icon and in there, Choose **Trash** (under the "List View Names" dropdown). You can also find the conversations from a deleted user in the **Spam** folder.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42281994/original/mIF1kqJdy0OZ1mgXrFfHPn5o7XgchlEQSA.png?1544602357)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42281997/original/Z-CujD_qFVlRst1x7A3fT86Ni6eDEPeIgA.png?1544602379)You can **Restore, Not spam** or **Delete Forever** those listed tickets, under these ticket views.Also, tickets in the **trash** folder for more than 30 days will be permanently removed from the portal.

</details>

<details>
<summary><strong>How to filter tickets by creation date?</strong></summary>

Ticket List Views enable you to group tickets based on a defined set of criteria. You can filter out tickets by source, type, status, assigned agents, tags, products, and even the custom fields (dropdown and dependent fields only) you have created. This way, agents can set their priorities and stay customer-centric. Besides these, agents can use the Ticket List Views for changing ticket owners, deleting tickets in bulk, or export the ticket list to a CSV file.If you wish to filter tickets based on their date of creation follow the steps below,-
Navigate to Tickets tab from the menu.-
Navigate to the Filters panel on the right, and choose the Select time period option from the Created dropdown.-
Under the Time period option, select the from and to dates and click on Update.-
Now click on Apply button to filter tickets.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006768417/original/0VH28kwpn6xAbep0RsHDd2hyLWLXkdc_Jg.png?1666956321)**Note :** Filtering tickets based on a custom date field is not possible.

</details>

<details>
<summary><strong>Is there an option to add more than one email address in 'TO' when replying?</strong></summary>

Since we map the 'To' address based on the requester of the ticket and because there can only be one requester for a ticket, you will not be able to add more than one email address in the 'To' field. You can however add the email addresses in the CC field.

</details>

<details>
<summary><strong>How to respond to multiple tickets with a common reply?</strong></summary>

Freshdesk offers the following features to respond to multiple tickets with a common reply.-
Bulk Update option from Ticket list views-
Canned ResponsesThe 'Bulk Update’ option from the Ticket list view page enables you to assign a selected set of tickets (maximum of 30 tickets per page) to an Internal group and agent. Please follow the steps below to make bulk updates on tickets in Freshdesk,-
Navigate to Tickets tab from the menu.-
Select the tickets you want to perform bulk actions on the Ticket List View page.-
Click on Bulk Update option from the top menu bar.-
Provide a reply message and update the respective ticket status, internal group, and agent.-
Click on Update to execute this action.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008515849/original/7Azi2gqWCIemEjP5HkxRqP2SpOvncJMzSw.gif?1685703522)With [Canned Responses](https://support.freshdesk.com/en/support/solutions/articles/37579-using-canned-responses-in-ticket-replies), your agents can create a predefined set of reply templates they can send out with a single click.[Using dynamic content placeholders](https://support.freshdesk.com/en/support/solutions/articles/52630-understanding-dynamic-content-and), agents can ensure customization of each response with the requester's name, agent's signature, and ticket details.Here is a detailed demonstration of Video: using canned responses in ticket replies on youtube for your reference.

</details>

<details>
<summary><strong>Can I customise the fields under the Tickets tab?</strong></summary>

When you are familiar with the tickets tab, sometimes there will be requirements to alter the arrangement of fields on "The Tickets list view" page. Unfortunately, it is not customizable as the design of the page is set by default and is common for all accounts.Please note that the custom ticket fields within **Admin > Workflows > Ticket Fields** could be altered in terms of the values and label. These changes would reflect within the filters on the left of the tickets list.

</details>

<details>
<summary><strong>Is there a possibility for a customer to check the status of their ticket without logging in?</strong></summary>

As a customer, it is understandable that they sometimes want to do a quick peruse through the ticket and not log in to the portal. In this scenario, the best recommendation would be to use a **"public ticket URL"** which leads to the ticket and does not require the customer to sign in.This has a placeholder which when included in the description of the ticket will ensure that the customer can view the ticket status without logging into the portal upon clicking this URL.To have the Public Ticket URL available in all replies, please navigate to **Admin > Workflows > Email Notifications > Templates > ****Agent Reply Template** ->** insert placeholder **and include the Public Ticket URL placeholder (please find this under the tickets section within the "insert placeholder" window).

</details>

<details>
<summary><strong>How can the customer change the priority and type of a ticket?</strong></summary>

When customers raise tickets, you would like to extend the ability for them to choose the priority and type of tickets so that you could plan the assignment and tracking of them.Please navigate to **Admin > Workflows > Ticket fields** > double click on these fields and verify if the priority field is displayed to the customer. If not, kindly choose the option 'Display to the customer' under customers end in ticket properties and the customer will then be able to edit it.

</details>

<details>
<summary><strong>How can customers view their previous conversations after a ticket is closed?</strong></summary>

Customers can view the history of tickets if they have access to your customer portal.They could log into your portal using the email address used to raise the tickets and view the status of all the tickets raised. You would be able to determine who could view the tickets by changing the permission to **"Logged in Users"** or to **"Everyone"** with a public ticket URL in **관리자 -> Channels -> Portals -> Settings. **Customers would also receive an email notification with the ticket details if you have enabled the Requester notifications under **관리자 -> Workflows -> Email Notifications.**

</details>

<details>
<summary><strong>How many tickets can I link to a tracker?</strong></summary>

You can associate upto 300 tickets to a single tracker.

</details>

<details>
<summary><strong>Can I download attachments using a Public Ticket URL without being logged in?</strong></summary>

Kindly note that only logged in users would be able to download attachments, even while using the Public Ticket URL. This would be the default behavior of the system to ensure data security and confidentiality.

</details>

<details>
<summary><strong>Can details apart from the contact details in Freshdesk be retrieved for a particular requester?</strong></summary>

Third party tools such as Salesforce.com or Zoho CRM can be integrated into Freshdesk, using which contact information from those CRM tools could be brought into Freshdesk. This contact information would be made visible as part of the Requester Info section as well.

</details>

<details>
<summary><strong>Can I receive a sound notification when a new ticket comes in?</strong></summary>

There is a feature called smart notifications for agents within the portal itself which would give real-time audible** notifications **about new tickets and updates on the ones you are working on. You can open the Notification Center by clicking on the bell icon from the navigation bar next to search.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008982964/original/Mcfm7grDSI0GYQIHt3vQRgj2_rwUjOlvww.png?1690278791)You could choose the ones you want to get these alerts for by clicking on the desktop icon in the notification center. You could enable **desktop notifications **in this window.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008983050/original/p9SJbYc1NxTX7MwYLtnQDKsCUI3N7WhZbA.png?1690279080)Muting is possible by turning on the "silent notifications" within the Preferences tab.For detailed information please refer to this article.

</details>

<details>
<summary><strong>Can I schedule a recurring ticket in Freshdesk ?</strong></summary>

As of now, we do not have the ability to schedule recurring tickets. However, as a workaround, you could make use of any third party event scheduler like [Google Calendar](https://support.freshdesk.com/support/solutions/articles/77059-the-google-calendar-app) to trigger an email to the support email address whenever an event is due.In that way, you wouldn't miss out on any notification as they would all come in as new tickets on your portal.

</details>

<details>
<summary><strong>How to remove ticket number that appears in the subject?</strong></summary>

Ticket numbers appear in the subject of email notifications because of the inclusion of ticket ID.In order to remove this, please navigate to** 관리자 -> Workflows -> Email notifications** ->to modify the "Subject" of the email notification by removing the placeholder for "Ticket ID" - \{\{ticket.id\}\}.

</details>

<details>
<summary><strong>How to undo ticket merging?</strong></summary>

Merging is an irreversible process. Once two tickets are merged it cannot be split.

</details>

<details>
<summary><strong>How to automatically stop the Time Tracker?</strong></summary>

The time tracker would automatically **stop** under the following instances:- When the status of the ticket is moved to Resolved/Closed.- When the agent starts replying on another ticket.- When the agent does an update to another ticket.

</details>

<details>
<summary><strong>On what time zone are the ticket counting timers based?</strong></summary>

The timers are based on the Helpdesk time zone that can be configured according to your location. Please navigate to **관리자 -> 계정 -> Helpdesk Settings** to change the timezone.

</details>

<details>
<summary><strong>Ticket field that I created is not present in the filters</strong></summary>

The Single line text fields, Multi line text fields, Number fields and check boxes will not be available in the filters of the ticket list view page.

</details>

<details>
<summary><strong>How do I split a customer response into a new ticket?</strong></summary>

If your customers respond with a new or unrelated query on an existing ticket, you can deal with it separately using the **S****plit**** Ticket **option. You can split **only a** **customer response** into a new ticket.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40878756/original/NYMQmKHUQQ7hJA2spVUrNuFTGefk8Ru1pQ?1537464067)This would facilitate better tracking metrics and help regulate your SLA compliance.

</details>

<details>
<summary><strong>How to include ticket thread when forwarding conversation?</strong></summary>

You can make sure that the entire ticket thread is visible to the person you forward it to by,-
enabling the 'Public ticket URL' option and-
inserting '**Public ticket URL**' placeholder in **Agent Forward Template**.Once done, when an agent clicks on the 'Forward' option, the public ticket URL will be visible to the person you forward it to, and they can view the complete ticket thread.As an administrator, you can enable the 'Public ticket URL' option by following the steps below.-
Navigate to Admin from the menu. Click on Channels. Select Portals.-
Under the Settings tab, navigate to the 'Who can view tickets on portal' section.-
Select the option 'Anyone with public ticket URL.'-
Click Save.![Changing portal settings to ](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008501559/original/TAZh1lotmgAGzEleU3u5A4VBHUgRTwmGvA.gif?1685598092)Users can now view tickets without logging in to your portal using the public ticket URLs.After enabling the 'Public ticket URL' option, you should now enable the corresponding placeholder in the Agent Forward Template. As an administrator of your Freshdesk account, here is how you can do it.-
Navigate to Admin from the menu. Click on Workflows. Select Email Notifications.-
Under the Templates tab, click on the Edit button next to the Agent Forward Template.-
Place your cursor on the reply editor where you wish to position the Public ticket URL.-
Click on the ‘Insert Placeholder’ button. Under the Tickets tab, click on the ‘Public Ticket URL’ placeholder.-
Click Save.
![Enabling the placeholder in the Agent Forward Template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008501568/original/jBBTVdgN8Hc84xkP8uBDXK-ozHAhxHQssA.gif?1685598145)

</details>

<details>
<summary><strong>How can I link an article to the reply of a ticket?</strong></summary>

Please navigate to the "**Tickets**" tab and open the ticket you would like to work on. Kindly click on the "Reply" button within the "**Ticket Details**" page, which will allow you to type your response. Among the various formatting options, you will find a "**book**" symbol that leads to the solution articles. You can either search for the relevant article or choose from the ones listed here.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009243700/original/ZL9Q4cQHkvpo9kbuLWueh5XNiVieZfGW0Q.png?1692715227)Ensure the article is visible in the customer portal when sharing an article link.  Articles can also be inserted as a link or the complete content by clicking the "**Insert** **Content**" or "**Insert link**" within the article suggestion.

</details>

<details>
<summary><strong>How to change due by date of a ticket ?</strong></summary>

In the ticket details page, above the subject of the ticket, there is an option to manually edit the 'Due Date' of the ticket as shown below :![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000625224/original/2_3uaQnxgU_0Rn2fQTKTLknrOFIOauz1BA.png?1579675067)You can also change the SLA applied to this ticket under **Admin > Workflows > SLA Policies.** Once the changes are done, you can update some properties for that ticket so that the new SLA will get applied and the due by date will be changed accordingly.**참고:**1) The option to change the due date will only show up when the ticket is assigned to statuses that have the **SLA timer ON** (example: Open).You can check which statuses have their SLA timers ON or OFF under **Admin > Workflows > Ticket Fields > Status** field. Once a manual change is done to the Due Time of a ticket, it will not change again when the ticket properties (for example, a change in priority) are updated.2) The due by date and time can always be updated only to a value greater than the First response time, that is the 'Response due' time on the ticket.

</details>

<details>
<summary><strong>What is the E-commerce channel?</strong></summary>

When you are hosted on an online e-commerce store and would like the customer queries from those stores to create tickets within your Freshdesk account, you can make use of the E-commerce channel. You will have the option to [integrate with your eBay account](https://support.freshdesk.com/support/solutions/folders/270315) and tickets will get created inside Freshdesk via your eBay shops.

</details>

<details>
<summary><strong>What are flags ? How can I fliter using flags?</strong></summary>

Flags are default labels in Freshdesk. They appear in the ticket list view and inside the ticket details page when certain activities occur:**New**: This flag shows on a ticket when an agent's response to the customer is pending. It remains until the first response/resolution isn't overdue.**Customer Responded: **This flag displays when a customer responds to a ticket.**Overdue**: This occurs when the ticket surpasses its resolution time without being resolved.**Response due:** This flag appears when the agent's first response isn't sent within a specific time based on the SLA.These flags are default and hardcoded, unalterable or removable. Ticket filtering using these flags isn't an option as of now

</details>

<details>
<summary><strong>What is a ticket?</strong></summary>

Each customer query - be it an email, or a phone call that comes into your account is a ticket. The agent would then be able to click on the ticket to respond to the customer about their query.Tickets raised on your account could be viewed under the Tickets tab, from where you could access them.

</details>

<details>
<summary><strong>Why is an Outbound email set to Close Status automatically?</strong></summary>

An Outbound email in Freshdesk is to be used for pro-active external communication directed at the customer. Only when the customer replies, the ticket created from this Outbound email would be considered as an active ticket and set to Open Status. In the meanwhile, the ticket created from this Outbound email would be marked Closed.

</details>

<details>
<summary><strong>When does a Tickets tab auto-refresh?</strong></summary>

In Freshdesk, the auto-refresh notification gives you non-invasive live updates on the ticket. This notification would show up when there is a property update within the ticket or when there is a reply/note added to the ticket.

</details>

<details>
<summary><strong>How to change the 'From' email address of a ticket?</strong></summary>

While replying, you can use the drop-down arrow mark to choose the 'From' email address as shown in the image below:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/40638603/original/pSgyY0zg3LGGhP44V-y-LfvPOAczWaePlw.png?1536310105)If you want to have a common email from which the replies are sent out, you can make use of the App '[Common From email address](https://www.freshworks.com/apps/freshdesk/customize_from_email_address/)'

</details>

<details>
<summary><strong>What happens when the attachment size limit goes beyond the threshold?</strong></summary>

Freshdesk will allow tickets to be created even when the attachments are exceeding the limit - from the email service, we now allow tickets which have attachments upto 50MB to come in, however, all attachments above 20 MB limit will be dropped and this alert will be shown in the ticket - '**Attachment(s) that exceed 20 MB limit have been dropped. Please reach out to the sender.**'This way, the tickets get created and the agents are also notified about the status of the attachment(s).**참고:** The limit is 20 MB for Blossom and above accounts. For Sprout and trial accounts, the threshold is 15 MB.

</details>

<details>
<summary><strong>Can I send bulk emails to customers using Freshdesk?</strong></summary>

No, there isn't an option to send out bulk emails to customers from inside Freshdesk. However, an integration with MailChimp can help you perform this action.Please refer to [this article](https://support.freshdesk.com/support/solutions/articles/41745-the-mailchimp-app) on how you can integrate MailChimp with Freshdesk.

</details>

<details>
<summary><strong>How many child tickets can I add to a parent ticket?</strong></summary>

You can add up to a maximum of 10 child tickets to a parent ticket.

</details>

<details>
<summary><strong>How can I delete an archived ticket?</strong></summary>

In order to delete an archived ticket, please go to the corresponding ticket page (either by performing a Search or hitting the ticket ID directly in the URL). Here, you will find the '**Delete forever**' button. Clicking on this button will **permanently delete** the ticket from the helpdesk.This option is only available on Freshdesk Mint.

</details>

<details>
<summary><strong>How to change the subject of a ticket?</strong></summary>

Inside the ticket details page, click on the three-dotted icon->select the '**Edit ticket details**' option to edit the subject of the ticket as shown below:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002700818/original/KDCFzZoq1EGoXsL5UpDWWTIY6kQlNg4_4w.png?1616499572)

</details>

<details>
<summary><strong>My ticket shows 'Response Due' though it has a response already</strong></summary>

Please check if the ticket has a private note/ Forward (Check for a lock symbol next to the note) or if it has a public note/ reply. If the reply is private then it would not be considered as a response by Freshdesk, because it is not displayed to the customer.

</details>

<details>
<summary><strong>How do I delete multiple tickets from same person?</strong></summary>

Using Search bar, search for the Requester email address and navigate to **Contacts** tab and click **Show tickets from **.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008947488/original/tXcWZ6fVzb-F_kFr5Ir-XtDEpCRV66c0sQ.png?1689856866)
You can use bulk actions to delete the tickets (30 tickets at a time) to delete all the tickets associated to the requester email address.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008947493/original/jCO06QajGuoZ2BdIMnITu7gSGEjb8yqWBg.png?1689856910)

</details>

<details>
<summary><strong>How to remove CC from a ticket?</strong></summary>

To remove the CC from a ticket you need click on the Reply option > select the addresses in the cc bar and click on the 'x' mark next to it and send the reply. Once removed, the CC address would not appear in the next replies unless added again by the requester or one of the agents manually.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008947706/original/jtMDRJ0JdhwZnMBSScRhxCgKnaqxXqKaKw.png?1689857992)

</details>

<details>
<summary><strong>What will be the impact on existing tickets if we update some dropdown fields?</strong></summary>

When you remove an item or option from the Dropdown field, this would automatically remove the value from the tickets and reports as well. The same happens when you rename or make any changes to the values of the field.The process that needs to be followed would be to create a new value in the same Dropdown field and Bulk change the values in all the tickets that you need. Once this is done, you can remove the value from **Admin > Workflows > Ticket fields**.

</details>

<details>
<summary><strong>Automatically track the time spent on tickets</strong></summary>

You can make use of the **Auto Start Timer** App to calculate the time spent on tickets based on the statuses you set. To know more about this check out the [link](https://www.freshworks.com/apps/freshdesk/auto_start_timer/).

</details>

<details>
<summary><strong>Can I re-open an archived ticket?</strong></summary>

No, you will not be able to change the status or reopen an Archived ticket.

</details>

<details>
<summary><strong>Can I unsplit a ticket?</strong></summary>

Make use of the [merge feature](https://support.freshdesk.com/en/support/solutions/articles/80180) in Freshdesk to merge the conversations from a secondary ticket to the primary ticket. If once split, you can merge the reply into the original ticket using this feature.

</details>

<details>
<summary><strong>When opening ticket the page scrolls down to latest reply</strong></summary>

If a ticket is assigned to you, then when you access that ticket you will be taken to the latest response automatically. However, this would not be the case when you are viewing a different agent's ticket.

</details>

<details>
<summary><strong>Tickets page keeps loading in Freshdesk</strong></summary>

Please follow the steps below so that we could identify the reason for the same.- Try accessing the account in the 'Incognito' window of your browser. If this works clear the cache and cookies of the browser and that should do the trick.
- Try in different browsers. This will help us identify if this is a browser specific issue.
- If both the above steps do not work then check the issue on a different network and let us know if that helps (A mobile hotspot should help with this).
- Check out our status page which is [https://updates.freshdesk.com/](https://updates.freshdesk.com/) to know if there are currently any issues.If none of the above works, please raise a ticket with us so that we could have this checked for you.

</details>

<details>
<summary><strong>Where is the Spam folder?</strong></summary>

You can access the 'Spam' folder by clicking on the hamburger menu in the Ticket list page.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000931217/original/sdZHJSyG8mWo7CUXwtULRGjNewcmEvUKCw.png?1586146473)You'll be able to see all the default and custom ticket views of your helpdesk here. Click on 'Spam' to go to the Spam view.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000931220/original/SRcoW-AeZSZAQmvO15wscfzc4R1FFAl7LQ.png?1586146590)

</details>

<details>
<summary><strong>How did a ticket land in the spam folder?</strong></summary>

**G****iven below are the ways in which a ticket gets spammed** :1) An agent can mark the ticket as spam manually.2) An automation rule would have acted upon the ticket.3) The contact of the ticket would have been deleted or blocked. Restore the ticket > click on the **Activities** at the top right corner and check as to why the ticket has been spammed. Once you restore the contact, all future emails from the contact will come through as tickets.If none of these were the reasons when checking the Activities please reach out to support@freshdesk.com and we would be glad to help you out.

</details>

<details>
<summary><strong>Is there a way to send a notification to all customer at once?</strong></summary>

We do not have an option to bulk email all your customers at once. You can make use of [**Mailchimp**](https://apps.freshdesk.com/mailchimp/) to send out these emails.However, if you are wanting to notify customers who have raised tickets then you can make use of the Bulk Actions present in the **Ticket list view** and send out the emails to 30 tickets at a time.

</details>

<details>
<summary><strong>I am not able to merge a ticket to a child ticket</strong></summary>

When the ticket has an association such as Parent/Child, you will not be able to add another association to it such as linking the ticket to a tracker or merging.

</details>

<details>
<summary><strong>Can I unarchive a ticket?</strong></summary>

Once the ticket is archived you will not be able to make any changes to the ticket. The archiving with take place only on tickets that has been in the Closed status for more than 120 days with no activity on the ticket.If you have tickets that need to be reopened in future then set them in a different status other than Closed.

</details>

<details>
<summary><strong>How to modify a parent child association ?</strong></summary>

It would not be possible to unlink a child ticket or link it with another parent. Child tickets are created with the association to the parent ticket and the only option would be to have it closed once it is done. You would have to create a new child ticket to be associated with the other parent ticket.

</details>

<details>
<summary><strong>Where can I find the customer fields in ticket page?</strong></summary>

You will not be able to filter the tickets using the Customer fields. However, if you want to view the Contact details in the Ticket details page you can make use of the Requester widget available under **Admin > Support Operations > Customer fields > Customize Requester widget**. This is a feature available from the Estate plan.

</details>

<details>
<summary><strong>If I resolve a tracker ticket, do all the tickets linked to it will become resolved?</strong></summary>

No, resolving the tracker ticket would not resolve the linked tickets by default. You have to manually resolve this as you might need to update your customers before resolving the tickets.

</details>

<details>
<summary><strong>How to protect your helpdesk from spam attack?</strong></summary>

In Freshdesk, we provide few options to protect your helpdesk from any possible spam tickets coming from sources like Portal and Email.For spam tickets created via Portal,  enable CAPTCHA on your customer support portal. Navigate to **Admin > Channels > Portals > Edit > Manage sections** and select the **'Enable CAPTCHA to help avoid spam'** option.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009297840/original/486-e4ikj4rbeucc4fPJU2vh8SykaIxaWA.png?1693235821)For spam tickets coming via Email, we enable Proactive Spam Filter from the backend. This spam filter will check all the tickets coming through the Email channel and based on certain pre-defined conditions, a spam score will be associated with each incoming email ticket. If the spam score of the email is 6 and above, the tickets will be marked as a spam automatically.The purpose of this feature is to ensure that you have optimum spam deflection. However, please note that there are chances that some valid emails can be marked as spam, if in case these emails arrive via a Spam reporting IP or with a high spam score. You could keep track of those tickets in the Spam folder inside the Tickets tab in Freshdesk and restore them if you deem that they are valid.If you would like this feature to be enabled for your account, please drop an email to [support@freshdesk.com](mailto:support@freshdesk.com). We'd be glad to assist.

</details>

<details>
<summary><strong>What each default SLA flag means on the ticket page</strong></summary>

Freshdesk, by default, classifies tickets with 4 specific flags. These flags help agents quickly take notice of the ticket in question and perform necessary actions.**Flag****Description**
![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44096793/original/9TtGfJrq8OZRsX2cl1LOCfdVYlWKqIQWBg.png?1552391023)
Represents all new tickets created on the helpdesk
![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44096809/original/Sp8823RTqD876IGZdoKGv8hdp0sH9furpA.png?1552391057)
Represents tickets the customer has responded to
![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44096964/original/C_686OnX-gx2hjkq7bNKum2WcddS2u4gbQ.png?1552391326)
Represents tickets for which the first response SLA has been violated
![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44097007/original/KNuoMJYa_TqeLwF3A5b32irpha5azGhCjQ.png?1552391407)
Represents tickets for which the resolution SLA has been violated**참고:** These flag values are hardcoded and cannot be edited. You will not be able to filter tickets based on these flags.

</details>

<details>
<summary><strong>Receiving spam emails to support@domain.freshdesk.com, Please help!</strong></summary>

We have been reported of multiple cases where the Russian Spammers usually create spam tickets by sending an email to the generic forwarding address. And this issue is not just specific to Freshdesk and it has been prevalent across all the helpdesk softwares like Zendesk, HelpScout as well.The spammers identify the generic forwarding address [like support@domain.freshdesk.com or info@domain.freshdesk.com or help@domain.freshdesk.com] and they create these spam tickets. So, using a generic forwarding address makes an account vulnerable to spam influx.To mitigate such spams, there is a feature called **'Prevent Wildcard Ticket Create'** where only emails directly sent to the email address configured under the Email config page in Freshdesk will be converted into tickets. Please go to **Admin > Channels > Email > Advanced Settings** and disable **'Allow emails to be sent to the wildcard support address'**Also, we would recommend using domain-specific email addresses like support@domain.com or help@domain.com [emails having your company's domain name] to avoid such issues. Using a domain-specific email address is going to be more advantageous for your business for the following reasons- It will help you brand the emails and replies sent by your organization from Freshdesk.
- It will allow you to have greater flexibility and control as to which emails need to be converted as tickets and so.
- It will be of help if you would like to use your own mail server to relay emails from and to Freshdesk through our Custom mail server feature.
- Your stakeholders will be able to receive emails authenticated by your own domain using the [DKIM](https://support.freshdesk.com/en/support/solutions/articles/223779) feature which ensures proper end-to-end email delivery.If you have any further queries, please drop us an email at support@freshdesk.com.

</details>

<details>
<summary><strong>How to stop tickets from being redirected to Ticket List View every time a ticket is closed?</strong></summary>

When the agent sends a reply and resolves or closes the ticket using the 'Send and set as resolved' or 'Send and set as closed' options, the page will be automatically redirected to the Ticket List View.This is the default behavior of the system designed to help the agents to view the other tickets in their queue without any additional clicks.If you do not want the page to be redirected to the Ticket List View upon closing the tickets, you can update the status of the ticket from the Ticket Properties section instead of using the 'Send and set as Resolved/Closed' options.

</details>

<details>
<summary><strong>Is there an option to undo a sent reply?</strong></summary>

Clicked on ‘**Send**’ even before the email was ready to go out to the customer? If you’re on the **Blossom or above plan**, you can use the ‘**Undo Send**’ button **within 10 seconds** of replying to stop it from going out.Agents will have to enable this option by clicking on their **profile picture icon on the top right corner > Profile settings** and then toggle the feature **ON**:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007619641/original/mK3EXgATc7y91oWtsqBm3kH8lxUN8rXSyg.png?1676458701)Once this is enabled, agents will start seeing the Undo option in the reply panel after they send out replies.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007619660/original/AOQ3H9_UJKqU0EtZpOh9XBjLFiTiVwfIJA.png?1676458923)**참고:** The ‘Undo’ option is available only for replies. And, it will not be possible to undo the replies sent using the 'Send and set as' option.

</details>


## 📋 데이터 관리

<details>
<summary><strong>How do I specify time range for export?</strong></summary>

After filtering the tickets that you need to export from the Tickets List view page, you would be able to click on the Export icon at the top of the page. In the popup that appears you would be able to enter the date range for which you want to export the tickets.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/39634632/original/0f8MK4nlPiBQetPVECn5XyXwM6HEHPcM5w.png?1531285433)

</details>

<details>
<summary><strong>How do I export my tickets from Freshdesk?</strong></summary>

Agents can export tickets, contacts, companies, or granular account data easily, and quickly download it anytime, from a centralized window.To export the tickets from your helpdesk, please navigate to the **Tickets** tab and choose the pre-existing '**All tickets**' view from the ticket list page.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41727962/original/Hr1KWJMUdP3-Z9BD3VXuTzRCVDHHSvYkog.png?1542003634)You can then choose and apply all the necessary filters such as the created time, agents, groups, type, status etc on the right and set up your filter to display the exact set of tickets you want to export then click on **Export** from the top right corner.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41727969/original/o5tA-Po2Nmxnl5onsP0ebYb7o0dtowTS1w.png?1542003706)When you click '**Export**', a slider opens out. Here, you can choose the format of the file (**CSV or Excel**) along with desired ticket fields that should be included in the ticket export. Expand the '**Show multiline text fields**' option on this slider to choose to export the '**Description**' or any other custom multiline text field.**Note**: The time frame set on the ticket list page has to be greater than the time frame set in the Export window. It is recommended to set the Created time field as '**Any time**' on the list page and apply the desired time in the export window. You'll notice that the export function now fetches tickets based on the filter you've applied, ensuring you get precisely the data you're looking for.This export will NOT give you the entire conversation from the ticket or historical data (archived tickets) - for that, you will have to perform an [account export](https://support.freshdesk.com/support/solutions/articles/225487-how-do-i-export-my-helpdesk-data-).![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41727385/original/0eCkQaLvmeMHswPOi-iyaqgVslAuxJjRKg.png?1542000319)To view previously exported data from your helpdesk, please navigate to Admin > Accounts exports. From here, you can see the export history.You can also see the progress of downloads and directly download the file from this page.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007809956/original/Ra68fvQhzU8PUTdBBlPc4HD8KIsAlfAJ9w.png?1678339723)A window pops up when you click on the Details button which provides details about the export. The agent can easily see information like the selected time period, ticket fields, contact fields, company fields, and other information from here.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007809972/original/RDacW3Db1xj9hFNxKNAvGtc8QRONaVaKSA.png?1678339822)**참고: **If the '**Export**' option is missing for you, it is possible that your Admin has restricted it by setting up a custom role. This setting can be changed under **Admin > Roles** by an Admin.

</details>

<details>
<summary><strong>When I export the tickets for a certain period of time, why don't I get the full count in export?</strong></summary>

The ideal way to export tickets is to set the time range under the '**Filter Tickets By**' section in the '**Export Tickets**' section. First, choose the preferred file format, set the desired range select the required fields to export and click '**Ex****port**'. Ensure that the **FILTERS** section in the Tickets list view does not have any date range specified (or) set as **Any time**. If any date range is set there, the export will only include tickets from that specified range.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011876874/original/XmsMnQj7vffq7poV3McOlSq0AQ443C8Lcw.png?1716134421)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011916937/original/YKlL5StwjZ_rOz91BAeP0pDfng8i0kQEdw.png?1716389787)

</details>

<details>
<summary><strong>How can I export tickets including the content of the ticket?</strong></summary>

There are multiple ways you can export the tickets with its content.- You can print the ticket and save it as a PDF on your system. (OR)
- The Account Admin can export all the data within your account (including tickets, solution articles, etc.) from the Admin section:- Navigate to Admin > Account > Account Details.
- Click Export
- The data will be exported to the account administrator's email in XML format. You can then convert the XML data into your preferred format.Watch Video: this video for steps to export the account data.

</details>


## 📋 사용자 관리

<details>
<summary><strong>Is it possible to add another agent to a ticket?</strong></summary>

You have a workflow set up where tickets are assigned to a particular agent depending upon the job description, the group this concerned agent belongs to and the expertise as well. Sometimes an agent would need another agent to look into something in the thread or receive notifications to go through the discussion.In this case, an agent could be added as a **"watcher" **who would receive all the notifications about the thread from the time when the agent is added as a watcher. You could have multiple agents added to a ticket as watchers.Only the one added as a watcher could remove oneself from the thread. An occasional agent without a day pass could still follow the ticket in the email thread when added as a watcher on tickets.

</details>

<details>
<summary><strong>How do you check if an agent is looking at the same ticket ?</strong></summary>

When an agent is looking into the same ticket, you could be notified regarding this within the ticket. This would help in preventing multiple agents working on the same ticket and to improve internal communication, using Freshdesk.At the top-left, within a ticket, you would find an "Eye" icon. While hovering upon it, the number of agents viewing the ticket would be displayed. You could also click on the icon to view a list of Agent Names of those agents currently viewing the ticket.This functionality is called as [Agent Collision detection](https://support.freshdesk.com/en/support/solutions/articles/218073) and is available from the Growth Plan onwards in Freshdesk.

</details>

<details>
<summary><strong>How do we check if an agent is answering/replying to your ticket ?</strong></summary>

If there are multiple agents replying to a ticket, you could be notified regarding that within the ticket as well. There would be a "Pen" icon on the top-left side within a ticket. If the symbol displays a number, it would mean that those many agents are currently replying to the ticket and you could click on the icon to view the agents' names.

</details>

<details>
<summary><strong>How do I notify my team members about the proceedings of the tickets?</strong></summary>

You can add the agents as watchers to the ticket so that all the members will receive email notifications about all the activities happening on a ticket.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41891454/original/AcIgqPZ7mxVrUpOGxMNy_83nIUGcGugg0g.png?1542784473)

</details>

<details>
<summary><strong>Every ticket for a particular user goes to Spam. Is there a place where we can “clear” the user's email?</strong></summary>

There are three ways by which a ticket leads to the Spam folder -- Manually marked as Spam by an Agent.
- A ticket marked as Spam by an Automation rule such as the Ticket Creation or Ticket Updates.
- Any ticket raised by a "deleted contact" in Freshdesk would go to Spam automatically.To have this resolved, kindly ensure that there are no automation rules that would mark tickets as Spam automatically and also make sure that the contact is restored from the Deleted list under the Customers tab.If you believe that a ticket was not marked as spam from the customer end, you can navigate to your spam folder, unspam it, and check how the ticket was marked as spam in the "Show activities" option in the top right corner.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008957818/original/ZdjkesiFiU-Hc26qEv95oez9wCxbQrQBQg.png?1689936042)

</details>

<details>
<summary><strong>Will agents be able to respond to tickets on their smartphones using Freshdesk?</strong></summary>

Yes, we do have an Agent specific Freshdesk Mobile app for IOS and Android. You can download the App from the App store/ Play store respectively.

</details>

<details>
<summary><strong>Is there a possibility to lock a ticket while one agent is answering and working on that?</strong></summary>

The primary step that needs to be taken in such a case would be to assign the ticket to the agent working on the ticket or he/she can pick it up from the list view itself. Each of your agents can have filters to view the tickets that are their names. The Agent collision feature would notify anyone if a different agent is view or replying to that ticket currently.

</details>

<details>
<summary><strong>How can I see drafts by another agent?</strong></summary>

The draft feature is for each agent; the draft saved by one of the agents cannot be viewed by another.**참고:** The drafts on the ticket reply editor will be available only for **24 hours**. They will not be available if the agents are drafting the response as a public/private note.Using the [Agent Collision](https://support.freshdesk.com/en/support/solutions/articles/218073) feature, you can see if another agent is already viewing or replying to a ticket in real-time. This feature is particularly useful for teams working on urgent or complex tickets, as it allows multiple agents to work on the same ticket simultaneously.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>Can the Admin and Agents view the same system activities in automations?</strong></summary>

The view for both the Admin and Agents would be different. When Activities is toggled 'ON', Admins would be able to view the automation along with the name of the rule and a hyperlink redirecting to it. However, Agents and Supervisors can only view the name of the automation rule which was executed.

</details>

<details>
<summary><strong>Where can I view the tickets in my account - how can I sort my queue?</strong></summary>

We have a '**Tickets'** section represented by a ticket icon and this presents all the tickets in your helpdesk. All these tickets from various 'sources' like phone, chat, social, feedback form and such (internally these channels are called sources) are all available on this list within the tickets section and we generally address it as the **tickets list view**.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008947864/original/i1cgCDDau7obGMMWPC6W_UmmwWdHlnPeZg.png?1689858492)To achieve an organized structure for accessing tickets, we have filters such as date created, last modified, due by time and other ticket properties such as status or priority. Please refer to this [**article**](https://support.freshdesk.com/support/solutions/articles/37559-working-with-the-ticket-list-view) on how efficiently the filters could be used.Further, they can be sorted as well in an ascending or descending order. This can be seen when you click on the header of the tickets queue (for example, it would say '**All tickets'**). You can use the available sorting options that is depicted in the image below.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008947882/original/PQkZKlgmj8JwTmhrNc0C8MV2mzDpNMUoyQ.png?1689858565)

</details>

<details>
<summary><strong>How do I view the Archived Tickets on my account?</strong></summary>

Any closed ticket with no updates for the past 120 days would be marked as **Archived**. These tickets would be part of the archived tickets list on your helpdesk.Please go to the Tickets tab and click on the view list > choose **Archive** (under the 'List View Names' dropdown) to see all the archived tickets in the portal.Alternatively, you can access the archived tickets by performing a search in your helpdesk or by directly hitting the ticket ID in the URL. ****Under the Global search, if you want the Archived tickets to show up, you have to manually change the search settings to include the archived tickets if required. By default, this option will be turned off.If you are using Freshdesk on Mint, clicking on the Archive view will take you to a page where you can apply the required filters and then export the file to your agent mailbox.

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
