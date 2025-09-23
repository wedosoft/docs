---
sidebar_position: 1
---

# 헬프데스크 리브랜딩

이 섹션에서는 헬프데스크 리브랜딩와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 고급 기능 및 사용법

<details>
<summary>방법 communicate with a third party from a Freshdesk ticket without involving the customer?</summary>

<p><span style="font-size: 16px;">If you are looking to initiating a private conversation with a third party vendor who isn't a part of your Freshdesk Account, you could use the <strong>Forward</strong> option on the Ticket details page. </span></p><p><br /></p><p><span style="font-size: 16px;">Please navigate to the <strong>Tickets</strong> tab -&gt; click on the ticket on which you would want to perform this action -&gt; and click on "<strong>forward" </strong>next to the reply option. </span></p><p><span style="font-size: 16px;"><br /></span></p><p><span style="font-size: 16px;">This sends the entire thread or individual reply (depending on which Forward is used) to the third party and it would not be visible to the customer. A reply to this email will be added as a private note to the ticket, which would also not be visible to the customer.</span></p>

</details>

<details>
<summary>Customers are not able to open the ticket URL in the response. 어떻게 할 수 있나요 rectify this?</summary>

<p>When you send out responses to your customers - the ticket URL would be available to the users depending on the user permission which can be understood by navigating to <strong dir="ltr">Admin -&gt; Channels -&gt; Portals -&gt; Settings</strong>. So there are two options - logged-in users or anyone with a <strong>public ticket </strong>URL. </p><p><br /></p><p dir="ltr">Considering the question, the option in your settings is "logged in users" who would need to be verified to have an account in your portal so that they could log in and check. There are two options to do this - make sure you send out an activation URL manually from the customers' tab or automate it in <strong dir="ltr">Adnin &gt; Workflows &gt; Email notifications &gt; Requester notifications &gt; User activation</strong>. Finally, if you would want a quicker alternative, you could guide them to do a password reset on the portal. </p>

</details>


## 관리 및 유지보수

<details>
<summary>무엇인가요 the difference between the New > Ticket and the New > Email option?</summary>

<p>The option to raise a <strong>new ticket</strong> or send a <strong>new email</strong> is available as part of the '<strong>+ New</strong>' quick access dropdown on the top right corner near the Search icon. You will also find '<strong>New contact</strong>', and '<strong>New Company</strong>' options as part of the dropdown for quick access. </p><p><br /></p><div ><span dir="ltr"><strong dir="ltr">+ New Ticket: </strong>This option can be used by the agents to create a new ticket on behalf of the requester, ideally after a phone call. The source of this ticket will be set as <strong>Phone</strong>. Also, on this page, you will be able to add a new contact. The 'Create another' option will open another new ticket page with the same properties as the previous ticket you just raised.</span></div><div ><span dir="ltr"></span></div><div dir="ltr"><span dir="ltr"><strong dir="ltr">+ New Email: </strong>This option can be used by agents to send outbound emails to customers from Freshdesk, for any intimation. This email will also be converted into a ticket. Here, you will not have an option to add a contact like the one available in the new ticket page. The 'Send another' option will open <span dir="ltr">another new email page with the same properties as the previous email you just sent.</span></span></div><div dir="ltr"><span dir="ltr"><span dir="ltr"></span></span></div><div dir="ltr"><span dir="ltr"><span dir="ltr">If you would like to create a ticket on behalf of the customer then you can use the 'New Ticket' option and if you would like to send an outbound email to one of your customers then you can use the 'New Email' option.</span></span></div><p><br /></p>

</details>

<details>
<summary>어떻게 auto-fill fields when I'm creating a new ticket as an Agent?</summary>

<p><span style="font-size: 14px;">You have agents with a busy schedule who are on calls and creating tickets for customers as you believe in first-hand support. When your agents are creating a new ticket or sending an outbound email, you can use the Ticket Templates feature to pre-fill regularly used fields. </span></p><p><span style="font-size: 14px;"><br /></span></p><p><span style="font-size: 14px;">Under <strong dir="ltr">Admin &gt; Agent Productivity &gt; Ticket templates</strong>, you can set up a template that your agents can select with one click. This solution article walks you through the process.</span></p><p><span style="font-size: 14px;"><br /></span></p><p><span style="font-size: 14px;">The Ticket templates feature is available from the Garden plan onwards.</span></p>

</details>

<details>
<summary>어떻게 save the filters I apply under the Tickets tab?</summary>

<p><span style="font-size: 16px;">After applying the filters under the Filter Tickets section of the Ticket view page, please click on the <strong>Tick mark </strong>next to the list view name (All tickets). </span></p><p><br /></p><p><span style="font-size: 16px;">This will allow you to save these filters and give it a relevant heading as well which you could use later. </span></p><p><span style="font-size: 16px;"><br /></span></p><p><span style="font-size: 16px;">Here's a<a href="https://support.freshdesk.com/support/solutions/articles/37559-filtering-tickets-using-views" target="_blank"> detailed article</a> that will help you set it up.</span></p>

</details>

<details>
<summary>왜인가요 a different language being displayed when I 로그 in to the portal?</summary>

<div dir="ltr"><p style=""><span rel="tempredactor"><span style="font-size: medium;">Please check the language options which is applied to your profile - you could check this under Agent Avatar--&gt;Profile Settings.</span></span></p></div>

</details>

<details>
<summary>어떻게 할 수 있나요 비활성화하다 the option for requesters to sign up to our helpdesk?</summary>

<p ><span style="font-size: 16px;">Please navigate to <strong dir="ltr">Admin -&gt; Channels -&gt; Portals -&gt; Settings </strong>and choose the option "<strong >No" </strong>under </span><strong ><span style="font-size: 16px;">Allow users to Sign Up from the customer portal</span></strong><span style="font-size: 16px;">. </span></p><p ><br /></p><p ><span style="font-size: 16px;">This <strong >would not allow</strong> users to sign up from the portal - you would have to send them an activation email to create an account with your system. </span></p>

</details>

<details>
<summary>어떻게 remove the Forums tab from the portal entirely?</summary>

<p><span style="font-size: 16px;">Please navigate to <strong dir="ltr">Admin -&gt; Account -&gt; Helpdesk Settings </strong>where you would be able to find a toggle button next to forums. Disabling this would hide the forums tab for all users on every product portal of your system.</span></p><p><br /></p><p><span style="font-size: 16px;">In order to hide this only for your customers, please get in touch with us <strong>(support@freshdesk.com)</strong> where we could give you a CSS code to hide the tab on the user end. </span></p>

</details>

<details>
<summary>어떻게 change the Helpdesk name in the left corner on the Agent portal?</summary>

<div style="box-sizing: border-box; color: rgb(24, 50, 71); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-size: 14px; font-weight: 400; text-align: start; text-indent: 0px;">Please navigate to Admin -&gt; Account -&gt; Helpdesk Settings to change the portal name displayed on the left side of the navigation bar.</div><div style="box-sizing: border-box; color: rgb(24, 50, 71); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-size: 14px; font-weight: 400; text-align: start; text-indent: 0px;"><br style="box-sizing: border-box;"></div><div dir="ltr" style="box-sizing: border-box; color: rgb(24, 50, 71); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-size: 14px; font-weight: 400; text-align: start; text-indent: 0px;">You will find a field called <strong>Helpdesk name</strong> in the Helpdesk settings, where you can enter the desired helpdesk name.</div><p><br /></p><p><span dir="ltr" style="font-size: 16px;"><img src="#" style="width: auto;" class="fr-fic fr-fil fr-dib" /></span><br /></p>

</details>

<details>
<summary>어떻게 rebrand the Agent side of the portal and change its colors?</summary>

<p><span style="font-size: 16px;">To change the colors of the Agent side of the portal, please go to <strong dir="ltr">Admin &gt; Account &gt; Helpdesk Settings &gt;&nbsp;</strong>Click on<strong dir="ltr">&nbsp;Edit Branding&nbsp;</strong>and make the necessary changes to&nbsp;</span><strong><span dir="ltr" style="font-size: 16px;">Helpdesk colors</span></strong><span style="font-size: 16px;">.</span></p><p><br /></p><p><span dir="ltr" style="font-size: 16px;"><img src="#" style="width: auto;" class="fr-fic fr-fil fr-dib" /></span><br /></p>

</details>

<details>
<summary>방법 cancel my Freshdesk Account?</summary>

<p >We, at Freshdesk, are always available to assist you with any issues that you are facing and will be happy to make your experience better. If there is anything we can help you with, feel free to write to us at <strong >support@freshdesk.com</strong>.</p><p ><br /></p><p >However, if you're certain that you'd like to delete your account, please click on <strong >Admin</strong> (represented by a gear icon from the navigation panel on the left)<strong dir="ltr">&nbsp;&gt; Account &gt; Account Details&nbsp;</strong>and click on '<strong >Cancel Account</strong>'.&nbsp;</p><p ><br /></p><p ><strong >Note that you will have to be an 'Account Administrator' on the portal to find this section.</strong></p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style="width: 224px; height: 113.806px;" /></p><p ><br /></p><p ><br /></p><p >It would be really helpful if you share your feedback and the reason behind canceling your account with us. You can then hit the '<strong >Request Cancellation</strong>' button on the next page and confirm the action on the following pop-up window.&nbsp;</p><p ><br /></p><p >You will have <strong >24 hours before your account gets suspended</strong>, and <strong >14 days (2 weeks) before we delete your account and account data permanently</strong>.</p><p ><br /></p><p ><img class="fr-dib fr-bordered" src="#" style="width: 214px; height: 238.141px;" /></p><p ><br /></p><p >Furthermore, we would advise you to export your account data by using the '<strong >Export Now</strong>' option on the same page before canceling your Freshdesk Account.</p><p ><br /></p><p ><strong >Note</strong>: If you're getting an error while deleting your account, please reach out to our support team at support@freshdesk.com</p>

</details>

