---
sidebar_position: 1
---

# Advanced Ticketing features

이 섹션에서는 Advanced Ticketing features와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 기본 설정 및 구성

<details>
<summary>방법 setup Shared Ownership for existing tickets?</summary>

<div rel="clipboard_data"><p>On the ticket details page select and<span></span><u>update</u><span></span>following:</p><ol><li>Internal Groups</li><li>Internal Agent</li></ol></div><p><br /></p>

</details>

<details>
<summary>어떻게 활성화하다 the Linked Ticket feature on my account?</summary>

<p dir="ltr">To enable Linked Tickets,</p><p dir="ltr"><br /></p><p dir="ltr">Go to <strong dir="ltr">Admin&gt;Support operation&gt;Advanced ticketing&gt;&nbsp;</strong>toggle on<strong dir="ltr">&nbsp;Linked tickets</strong></p><p dir="ltr"><br /></p><p dir="ltr"><strong dir="ltr"><img src="#" style={{ width: "684px" }} class="fr-fic fr-dib fr-bordered" /></strong><br /></p>

</details>


## 고급 기능 및 사용법

<details>
<summary>가능한가요 to link tickets using automations ?</summary>

No. Tickets cannot be linked to trackers by using any of the four automations.

</details>

<details>
<summary>Can internal 그룹 or agents be included in 자동화 rules?</summary>

<p >Internal groups or agents can be set in the Conditions and Actions in automation rules that run on ticket creation or ticket updates.</p><p ><br /></p>

</details>

<details>
<summary>가능한가요 to trigger an action using the Ticket 업데이트하다 자동화 if the Internal 그룹 is changed?</summary>

<p dir="ltr"><span style={{ fontSize: "16px", fontFamily: "Arial", color: "rgb(0, 0, 0)" }}><span dir="ltr" style={{ fontWeight: "400", textAlign: "left", textIndent: "0px", display: "inline !important" }}>Within the Ticket Update automation rule, the Internal group can be included in the Conditions and Actions sections, but it is not possible to trigger an Event specifically when the internal group is changed.</span></span></p><p><br /></p>

</details>


## 관리 및 유지보수

<details>
<summary>Can a related ticket be unlinked ?</summary>

<p dir="ltr">Yes it is possible. To unlink the ticket from the Tracker, Go to <strong>Linked Tickets</strong> and click<strong dir="ltr">&nbsp;Unlink</strong>. <span style={{ color: "rgb(0, 0, 0)", fontFamily: "-apple-system, BlinkMacSystemFont, ", fontSize: "13px", fontStyle: "normal", fontVariantLigatures: "normal", fontVariantCaps: "normal", fontWeight: "400", letterSpacing: "normal", orphans: "2", textAlign: "left", textIndent: "0px", textTransform: "none", whiteSpace: "normal", widows: "2", wordSpacing: "0px", WebkitTextStrokeWidth: "0px", textDecorationThickness: "initial", textDecorationStyle: "initial", textDecorationColor: "initial", display: "inline !important", float: "none" }}>This permanently unlinks the ticket from that tracker and CANNOT be undone.</span>&nbsp;</p><p dir="ltr"><br /></p><p dir="ltr"><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p>

</details>

<details>
<summary>방법 create parent and child tickets?</summary>

<p>You may open a ticket, click on ‘Add Child’ and choose between "Using a Template" and "New Child Ticket". The original ticket will become the parent ticket and the child ticket will be created as a new ticket. This feature is available from the Estate Plan onwards on Freshdesk.</p><p><br /></p>

</details>

<details>
<summary>가능한가요 to link tickets in Freshdesk?</summary>

Yes, it is possible. By using trackers ,tickets can be linked in Freshdesk.

</details>

<details>
<summary>When does Shared Ownership come into play?</summary>

When there are multiple agents involved in a single ticket, we could make use of Shared Ownership. Whether it is a customer facing agent or an internal agent, all are kept in the loop on any action done within the ticket.<p><br /></p>

</details>

<details>
<summary>방법 view all the related tickets to a specific tracker?</summary>

<p>Yes, it would be possible to view all the tickets linked to a tracker. </p><p><br /></p><p>Here are the steps: </p><p>Step 1: Filter the tickets of tracker type in the Association Type field. </p><p>Step 2: Select the tracker, the one you wish to view all the related tickets.</p><p>Step 3: Click on X Related tickets on the right hand side of the page.The list of all the related tickets is shown.Here X= Number of related tickets.</p><p><br /></p><p>However as of now, this information is not available as a metrics with Reports.</p>

</details>

<details>
<summary>Sample scenario for Shared Ownership?</summary>

<p>A ticket comes from an e-commerce company which has issues relating to a bug as well a query regarding a feature. </p><p>Query is solved by the customer facing agent(Primary agent).</p><p>Bug is solved by the internal agent(Developer).</p><p><br /></p><p>Shared Ownership helps in dynamically checking the status of work on a single ticket, keeping both the agents in the loop.</p><p><br /></p>

</details>

<details>
<summary>When can we close the parent ticket?</summary>

<p>A Child Ticket is essentially a subdivision of the Parent Ticket. The Parent Ticket can be closed only if all of its Child Tickets are either Closed or Resolved.</p><p><br /></p>

</details>

<details>
<summary>Where/How do you link tickets ?</summary>

<p>Go to the <strong>Tickets Tab &gt; Click on the required ticket &gt; Expand the 'Linked Tickets' panel on the extreme right &gt; Create a new tracker or choose to link it to an existing tracker.</strong></p><p><br /></p><p dir="ltr">This feature is available only from the<strong dir="ltr">&nbsp;Pro/Garden Plan&nbsp;</strong>onwards in Freshdesk.</p><p dir="ltr"><br /></p><p dir="ltr"><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p><p>Click <a href="https://support.freshdesk.com/support/solutions/articles/224695-setting-up-linked-tickets" rel="noreferrer noopener" target="_blank">here</a> to know more about Linked tickets.</p>

</details>

<details>
<summary>할 수 있나요 필터 tickets according to a specific tracker ?</summary>

No, it is not possible to do so. In order to view all the related tickets of that tracker, go to the tracker itself and click on related tickets.

</details>

<details>
<summary>방법 add multiple child tickets to a parent ticket?</summary>

<p> After creating a new child ticket, click on ’Save and New Child’ to add a new child. You could also click on "Add Child" option within a Parent Ticket to create a new child ticket.</p>

</details>

<details>
<summary>방법 설정하다 Shared Ownership?</summary>

<p >You would have to install the Shared Ownership App on your account as shown in this <a href="https://support.freshdesk.com/support/solutions/articles/224194-enabling-shared-ownership" rel="noopener noreferrer" target="_blank">solution article</a>.</p><p ><br /></p><p >After this is done, there are two steps involved.</p><p ><br /></p><p ><strong >1. Map internal groups to a ticket status:</strong></p><p ><br /></p><p dir="ltr">Go to <strong>Admin &gt; Workflows &gt; Ticket fields </strong></p><p >Excluding the 4 basic statuses of ticket, map the custom statuses under<span ></span><u >Mapped Internal Groups</u>.</p><p >NOTE: Don't forget to include<span ></span><u >Customer responded</u>.</p><p ><br /></p><p ><strong >2. Set up automation rules to make sure everyone's in the loop:</strong></p><p ><br /></p><p dir="ltr">Go to <strong dir="ltr">Admin &gt; Workflows &gt; Automations &gt; Ticket updates &gt; New rule</strong></p><p ><br /><strong ><u >Set up a new automation rule as below:</u></strong></p><p ><br /></p><p ><strong >When an action is performed by</strong></p><p >Requester</p><p ><br /></p><p ><strong >Involves any of these events</strong></p><p >Reply IS sent</p><p ><br /></p><p ><strong >On tickets with these properties</strong></p><p >Status is NOT &gt; Open OR Waiting on Third party OR Waiting on Sellers team</p><p ><br /></p><p ><strong >Perform these actions:</strong></p><p >Set status as &gt; OPEN</p><p >Send email to Agent &gt; Assigned Agent</p><p ><br /></p>

</details>

<details>
<summary>방법 view all related tickets?</summary>

<p dir="ltr">In the tickets list page, the ticket with the separate tag that indicates <strong>Tracker</strong> is the main tracker ticket. Also, it is possible to filter all the tracker tickets in the helpdesk. This can be done by choosing <strong>T</strong><strong dir="ltr">racker</strong> in the<strong>&nbsp;Association Type dropdown field</strong>.</p><p><br /></p><p><img src="#" style={{ width: "700px" }} class="fr-fic fr-dib fr-bordered" /></p><p dir="ltr">To view related tickets,</p><p dir="ltr"><br /></p><p dir="ltr">Go to <strong dir="ltr">Tickets&nbsp;</strong>&gt;select the<strong >&nbsp;Tracker ticket</strong> &gt; click on <strong >Related</strong><strong dir="ltr">&nbsp;Tickets.</strong></p><p dir="ltr"><br /></p><p dir="ltr"><strong dir="ltr"><img src="#" style={{ width: "684px" }} class="fr-fic fr-dib" /></strong><br /></p>

</details>

<details>
<summary>Can we edit the the related ticket 위젯 ? i.e show more details of the tracker?</summary>

No it is not possible to show more details of the tracker in the widget. In order to get more details of the tracker , the agent can view it separately.

</details>

<details>
<summary>어떻게 know which is the tracker ticket ?</summary>

<p dir="ltr">In the tickets list page, the ticket with the separate tag that indicates <strong>Tracker</strong> is the main tracker ticket. Also, it is possible to filter all the tracker tickets in the helpdesk. This can be done by choosing <strong>T</strong><strong dir="ltr">racker</strong> in the<strong>&nbsp;Association Type dropdown field</strong>.</p><p><br /></p><p><img src="#" style={{ width: "700px" }} class="fr-fic fr-dib fr-bordered" /></p>

</details>

<details>
<summary>어떻게 view all related tickets?</summary>

In the tickets tab, the tickets having the tag Related Ticket are related/linked to a ticket.

</details>

<details>
<summary>방법 create templates for child tickets?</summary>

<p dir="ltr">Under <strong>Admin &gt; Agent Productivity &gt; Ticket Templates &gt; New Template</strong>, you could add a new ticket template and choose "Save and Add Child" to create a template for Parent Ticket. Once this is done, you would be able to add Child Ticket Templates under this Parent Ticket Template.</p><p><br /></p><p>To apply a template to the child ticket click on ‘<strong>Use existing template</strong>’ while creating a new child ticket.</p><p><br /></p>

</details>

<details>
<summary>Is the Linked tickets tracker same as that of the time tracker ? Are they related ?</summary>

No, both the trackers are completely different. The first one is used to link tickets which creates a separate tracker ticket.Whereas the latter is used to calculate the amount of time spent on a particular ticket.

</details>

<details>
<summary>What would be the source of a child ticket?</summary>

<p>Since the ticket is created by an agent, the source of the ticket would be phone.</p><p><br /></p>

</details>

<details>
<summary>Does the Linked Ticket Actions appear in the activities tab?</summary>

All the activities that are carried out with respect to the ticket are shown in the activities tab. In this case, even when tickets are linked to a tracker is shown in the activities tab,

</details>

<details>
<summary>어떻게 할 수 있나요 assign large number of groups and agents for Shared Ownership?</summary>

<div rel="clipboard_data"><p>There are 2 ways to do it.</p><p><br /></p><p>-<span></span><strong>Bulk Mode</strong></p><p>Select the necessary tickets to perform bulk actions.</p><p><br /></p><p><font>-<span></span><strong>Using Scenario Automation</strong></font></p><p><font>Option to execute a scenario is directly available in the drop down menu.</font></p></div><p><br /></p>

</details>

<details>
<summary>How many child tickets can be added to a parent ticket?</summary>

<p dir="ltr">We can add a maximum of 50 child tickets to a parent ticket.</p><p><br /></p>

</details>

<details>
<summary>Is there a bulk action to unlink multiple tickets at once ?</summary>

No. It is only possible to unlink a ticket in the ticket details page. Multiple unlinks are not available as of now.

</details>

<details>
<summary>An agent is able to view all the related tickets but not view it separately? Why ?</summary>

<div style={{ margin: "15px 0px", padding: "0px", fontSize: "13px", fontFamily: "Arial", border: "0px", overflowX: "auto", textAlign: "initial", color: "rgb(51, 51, 51)", textIndent: "0px", textDecorationStyle: "initial", textDecorationColor: "initial" }}><p style={{ margin: "0px", padding: "0px", fontSize: "13px", border: "0px", lineHeight: "1.4", wordBreak: "normal", wordWrap: "break-word" }}><span style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}>That agent would be having restricted or group access and hence the related tickets are out of the agent's scope.</span></p><p style={{ margin: "0px", padding: "0px", fontSize: "13px", border: "0px", lineHeight: "1.4", wordBreak: "normal", wordWrap: "break-word" }}><br /></p><p style={{ margin: "0px", padding: "0px", fontSize: "13px", border: "0px", lineHeight: "1.4", wordBreak: "normal", wordWrap: "break-word" }}><span dir="ltr" style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}>To can give the agent access to view tickets,</span></p><ul><li style={{ marginTop: "0px", marginRight: "0px", marginBottom: "0px", padding: "0px", fontSize: "13px", border: "0px", lineHeight: "1.4", wordBreak: "normal", overflowWrap: "break-word" }}><span dir="ltr" style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}>Go to <strong dir="ltr">Admin &gt; Teams &gt; Agents &gt; Edit Agent</strong></span></li><li style={{ marginTop: "0px", marginRight: "0px", marginBottom: "0px", padding: "0px", fontSize: "13px", border: "0px", lineHeight: "1.4", wordBreak: "normal", overflowWrap: "break-word" }}><span dir="ltr" style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}>Scroll down to Scope and edit the scope of the agent.</span></li></ul><p><span dir="ltr" style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}><img src="#" style={{ width: "500px" }} class="fr-fic fr-dib fr-bordered" /></span></p><p><br /></p><p><span dir="ltr" style={{ margin: "0px", padding: "0px", fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", border: "0px" }}>Learn more about agent scope <a href="https://support.freshdesk.com/en/support/solutions/articles/50000002804" rel="noreferrer" target="_blank">here</a>.</span></p></div><p><br /></p>

</details>

<details>
<summary>Can we delete a tracker ? Even if there are tickets related to it ?</summary>

<p dir="ltr">Yes it is possible to delete a tracker.&nbsp;</p><p dir="ltr"><br /></p><ul><li dir="ltr">Go to the <strong>Tracker.</strong></li><li dir="ltr">Click on the three dots for <strong dir="ltr">More options</strong> and select <strong dir="ltr">Delete.</strong></li><li dir="ltr">Once you delete a tracker, its related tickets will be permanently unlinked which <strong>cannot</strong> be restored.</li></ul><p><img src="#" style={{ width: "684px" }} class="fr-fic fr-dib fr-bordered" /></p>

</details>

<details>
<summary>방법 create a parent ticket ?</summary>

<p style={{ boxSizing: "border-box", margin: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, BlinkMacSystemFont, ", fontStyle: "normal", fontVariantLigatures: "normal", fontVariantCaps: "normal", fontWeight: "400", letterSpacing: "normal", orphans: "2", textAlign: "start", textIndent: "0px", textTransform: "none", whiteSpace: "normal", widows: "2", wordSpacing: "0px", WebkitTextStrokeWidth: "0px", textDecorationThickness: "initial", textDecorationStyle: "initial", textDecorationColor: "initial" }}><strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Quick guide to set up Parent Child Ticketing:</strong></p><ol style={{ boxSizing: "border-box", margin: "8px 0px 4px", padding: "0px 0px 0px 40px", lineHeight: "17px", listStylePosition: "initial", listStyleImage: "initial", color: "rgb(24, 50, 71)", fontFamily: "-apple-system, BlinkMacSystemFont, ", fontSize: "13px", fontStyle: "normal", fontVariantLigatures: "normal", fontVariantCaps: "normal", fontWeight: "400", letterSpacing: "normal", orphans: "2", textAlign: "start", textIndent: "0px", textTransform: "none", whiteSpace: "normal", widows: "2", wordSpacing: "0px", WebkitTextStrokeWidth: "0px", textDecorationThickness: "initial", textDecorationStyle: "initial", textDecorationColor: "initial" }}><li dir="ltr" style={{ boxSizing: "border-box", fontSize: "13px", lineHeight: "18px", margin: "0px", wordBreak: "normal", overflowWrap: "break-word" }}>Log in to your Freshdesk portal as an Administrator.</li><li style={{ boxSizing: "border-box", fontSize: "13px", lineHeight: "18px", margin: "0px", wordBreak: "normal", overflowWrap: "break-word" }}>Go to <strong style={{ boxSizing: "border-box", fontWeight: "700" }}>Admin</strong><strong dir="ltr" style={{ boxSizing: "border-box", fontWeight: "700" }}>&nbsp;&gt; Support Operations &gt; Advanced Ticketing</strong>.</li><li style={{ boxSizing: "border-box", fontSize: "13px", lineHeight: "18px", margin: "0px", wordBreak: "normal", overflowWrap: "break-word" }}>Enable the toggle for <strong dir="ltr" style={{ boxSizing: "border-box", fontWeight: "700" }}>Parent-Child Ticketing</strong>.<br /><strong dir="ltr" style={{ boxSizing: "border-box", fontWeight: "700" }}><img src="#" class="fr-fic fr-fil fr-dib fr-bordered" style={{ boxSizing: "border-box", border: "0px", maxWidth: "100%", cursor: "pointer", padding: "0px 1px", marginBottom: "5px", marginLeft: "0px", display: "block", textAlign: "left", color: "rgb(226, 80, 65)", fontFamily: "-apple-system, ", fontSize: "13px", fontWeight: "400", textIndent: "0px", width: "auto" }} /></strong></li></ol><p><br /></p><p><span dir="ltr" style={{ color: "rgb(24, 50, 71)", fontFamily: "-apple-system, BlinkMacSystemFont, ", fontSize: "13px", fontStyle: "normal", fontVariantLigatures: "normal", fontVariantCaps: "normal", fontWeight: "400", letterSpacing: "normal", orphans: "2", textAlign: "start", textIndent: "0px", textTransform: "none", whiteSpace: "normal", widows: "2", wordSpacing: "0px", WebkitTextStrokeWidth: "0px", textDecorationThickness: "initial", textDecorationStyle: "initial", textDecorationColor: "initial", display: "inline !important", float: "none" }}>Parent-Child Ticketing will now be enabled in your account.</span></p><p dir="ltr"><br /></p><p dir="ltr">To create a parent-child relationship, add a child ticket to any existing or new ticket.</p><p dir="ltr"><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p>

</details>

<details>
<summary>What happens when you delete a parent ticket?</summary>

<div rel="clipboard_data"><p>The parent ticket will be deleted and the associated child tickets will be unlinked from the parent ticket.</p></div><p><br /></p>

</details>

<details>
<summary>무엇인가요 the use of the Broadcast button?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontFamily: "Arial", fontSize: "14px" }}>With all the related tickets linked to the Tracker, the team working on it can notify the agents on the progress by using an internal broadcast message.</span></p><p dir="ltr" style={{ fontFamily: "Arial", fontSize: "14px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "14px", fontFamily: "Arial" }}>Once the message is broadcasted on the Tracker ticket, it would be relayed on all the related tickets automatically. This broadcast message would be visible only to agents on the account.</span></span></p><ul style={{ fontFamily: "Arial", fontSize: "14px" }}><li dir="ltr" style={{ fontFamily: "Arial", fontSize: "14px" }}><p style={{ fontFamily: "Arial", fontSize: "14px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "14px", fontFamily: "Arial" }}>To broadcast an internal message to agents who are assigned to related tickets, click on <strong style={{ fontFamily: "Arial" }}>Broadcast</strong>.&nbsp;</span></span></p></li></ul><p class="article_note" style={{ fontFamily: "Arial", fontSize: "14px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "14px", fontFamily: "Arial" }}><strong dir="ltr" style={{ fontFamily: "Arial" }}>Note:</strong> Only agents who have access to the Tracker ticket will be able to send a broadcast message.</span></span></p><ul ><li dir="ltr"><span style={{ fontSize: "14px", fontFamily: "Arial" }}>Enter the message and click Broadcast. The message will be sent to all the related tickets that are linked with the Tracker.</span></li></ul><p><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p><p ><span style={{ fontFamily: "Arial", fontSize: "14px" }}>The broadcast message will be added to any new tickets linked to the Tracker. At any point of time, any related ticket will only have the last broadcasted message. That is, if a new message is broadcasted, it will replace the existing message with the new one. The agents can include the message in their replies on the related tickets using the <strong style={{ fontFamily: "Arial" }}>Insert this message into reply</strong> option</span></p><p style={{ fontFamily: "Arial", fontSize: "14px" }}><span style={{ fontSize: "14px" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></span></p><p class="article_note" ><span style={{ fontSize: "14px" }}><span style={{ fontFamily: "Helvetica Neue" }}><strong style={{ fontFamily: "Arial" }}>Note:</strong>&nbsp;</span></span><span dir="ltr" style={{ fontFamily: "Arial", fontSize: "14px" }}>When a message is broadcasted from the Tracker ticket, a hardcoded email notification will be sent to the assigned agent and the <a href="https://support.freshdesk.com/support/solutions/articles/37560-monitoring-important-tickets-by-becoming-a-watcher-" rel="noreferrer noopener" style={{ fontFamily: "Arial" }} target="_blank">watcher(s)</a> added on the related tickets. &nbsp;</span></p><p dir="ltr"><br /></p>

</details>

<details>
<summary>Does updating the 상태 of parent ticket affect the child ticket?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontFamily: "Arial", fontSize: "16px" }}>No, changing the status of the parent ticket will not impact the status of the child tickets. However, if you wish to achieve this, you can utilize an automation rule. Here is a sample automation rule summary -<br /><br /><img src="#" style={{ width: "690px", fontFamily: "Arial", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-fic fr-dib fr-bordered fr-shadow" /><br /></span></p><p ><br /></p>

</details>

<details>
<summary>How many number of tickets can be linked to a tracker ?</summary>

To a single tracker, a maximum of 300 tickets can be linked to it.

</details>

<details>
<summary>가능한가요 to link multiple tickets at once?</summary>

To link multiple tickets, we have to goto the ticket details page separately of each ticket and link them individually to a tracker. As of now there is no option under Bulk Actions to carry out this function.

</details>

<details>
<summary>What happens when you mark a parent ticket as spam?</summary>

<p>The child tickets associated with the parent ticket will be unlinked and the changes<span> cannot</span><span></span>be restored. However, the child tickets would not be marked as spam.</p><p><br /></p>

</details>

<details>
<summary>Can we 필터 out tickets based on parent and child tickets?</summary>

<p dir="ltr">Yes, we can filter out tickets based on parent and child tickets.&nbsp;</p><ul><li dir="ltr">Go to<strong>&nbsp;Tickets</strong>.</li><li dir="ltr">Under the <strong>Filters section</strong> on the left hand side, click on <strong>Association Type</strong>.</li><li dir="ltr">Select the type of association as <strong>Parent or Child</strong> to filter out the corresponding tickets.&nbsp;</li></ul><p><br /></p><p><img src="#" style={{ width: "700px" }} class="fr-fic fr-dib fr-bordered" /></p><p><br /></p><p><br /></p><p><br /></p>

</details>

<details>
<summary>Can a linked ticket also be a child/parent ticket ?</summary>

<p>No, tickets can be associated via trackers or the parent-child method, but not both.</p>

</details>

<details>
<summary>Can we 필터 out child tickets based on parent ticket?</summary>

<p>No, you cannot filter out child tickets based on the parent ticket. However, you can go to the parent ticket and view the child tickets associated with it.</p>

</details>

<details>
<summary>What are the mandatory fields while creating a new tracker?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontFamily: "Arial", fontSize: "16px" }}>Two fields are mandatory while creating a new tracker :<br /><br />1. <strong>Requester field</strong> -&nbsp;</span><br /><span dir="ltr" style={{ fontFamily: "Arial", fontSize: "16px" }}>The agent creating the tracker ticket is also the requester.<br />There is an option for the agent to create the tracker under their name or the name of one of their colleagues.<br /><br /><img src="#" style={{ width: "511px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center", fontFamily: "Arial" }} class="fr-fic fr-dib fr-bordered fr-shadow" /><br />2. <strong>Subject field</strong> - This defines the name/<span dir="ltr" style={{ color: "rgb(0, 0, 0)", fontStyle: "normal", fontVariantLigatures: "normal", fontVariantCaps: "normal", fontWeight: "400", letterSpacing: "normal", orphans: "2", textAlign: "left", textIndent: "0px", textTransform: "none", widows: "2", wordSpacing: "0px", WebkitTextStrokeWidth: "0px", whiteSpace: "normal", textDecorationThickness: "initial", textDecorationStyle: "initial", textDecorationColor: "initial", float: "none", fontFamily: "Arial", display: "inline !important" }}>description o</span>f the tracker.<br /><br />If there are any additional fields designated as mandatory under the Admin &gt; Ticket fields section, those fields should also be filled in to create a tracker.<br /></span></p>

</details>

<details>
<summary>Is there a way to 비활성화하다 the 'link to a tracker' option for specific groups/agents?</summary>

<div rel="clipboard_data"><span dir="ltr" style={{ color: "rgb(51, 51, 51)", fontFamily: "Arial", fontSize: "16px", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial" }}>You can create a custom role and manage the <strong style={{ fontFamily: "Arial" }}>Ticket</strong> access for the agents assigned to the role under <strong dir="ltr" style={{ fontFamily: "Arial" }}>Permissions.</strong>&nbsp;</span></div><p style={{ fontFamily: "Arial", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></span></p><p style={{ fontFamily: "Arial", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ color: "rgb(51, 51, 51)", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial", fontFamily: "Arial" }}>To disable the option for agents to link tickets,</span></span></span></p><ul><li style={{ fontFamily: "Arial", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ color: "rgb(51, 51, 51)", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial", fontFamily: "Arial" }}>Go to <strong dir="ltr" style={{ fontFamily: "Arial" }}>Admin &gt; Teams &gt; Roles&nbsp;</strong></span></span></span></li><li style={{ fontFamily: "Arial", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ color: "rgb(51, 51, 51)", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial", fontFamily: "Arial" }}>Create a <strong dir="ltr" style={{ fontFamily: "Arial" }}>New Role&nbsp;</strong>or click <strong dir="ltr" style={{ fontFamily: "Arial" }}>Edit&nbsp;</strong>next to an existing custom role.</span></span></span></li><li style={{ fontFamily: "Arial", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ color: "rgb(51, 51, 51)", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial", fontFamily: "Arial" }}>Scroll down to <strong dir="ltr" style={{ fontFamily: "Arial" }}>Permissions.</strong></span></span></span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ color: "rgb(51, 51, 51)", textAlign: "start", textIndent: "0px", backgroundColor: "rgb(255, 255, 255)", textDecorationStyle: "initial", textDecorationColor: "initial" }}>Under the Tickets tab, uncheck the box next to <strong dir="ltr">Create a linked ticket.</strong></span></span></span></li></ul><p><br /></p><p><img src="#" style={{ width: "684px" }} class="fr-fic fr-dib fr-bordered" /></p><p><br /></p><p dir="ltr"><span style={{ fontFamily: "Arial", fontSize: "16px" }}>You can now, assign this role to all the agents who should not have access to create linked tickets.</span></p><p><br /></p>

</details>

<details>
<summary>Can an agent link a ticket to any tracker?</summary>

An agent can only link tickets to a tracker that are present in his/her scope. So, if an agent has group/restricted access he/she wont be able to view all the trackers that are present in the helpdesk.

</details>

<details>
<summary>Would an agent with Restricted 접근하다 be able to view Shared Ownership tickets?</summary>

<div rel="clipboard_data">When the agent has restricted access, still he would be able to see tickets assigned to him as an internal agent even if he is not the assigned agent on the ticket.</div><p><br /></p>

</details>

<details>
<summary>Would an agent with 그룹 접근하다 be able to view Shared Ownership tickets?</summary>

When an agent has group access, he will have access to the tickets which have the internal group assigned as the agent’s group even though the ticket belongs to a different group.<p><br /></p>

</details>

<details>
<summary>할 수 있나요 use a 템플릿 to create a new ticket?</summary>

<p>We understand that you might want to create tickets on-the-go.<br />Freshdesk allows you to create templates from <strong dir="ltr">Admin &gt; Agent Productivity &gt; Ticket Templates</strong>. These templates can be used while creating a ticket from the <strong>“Select a template”</strong> option.</p><p><br /></p><p><a href="https://support.freshdesk.com/support/solutions/articles/220141-creating-and-using-ticket-templates" rel="noreferrer noopener" target="_blank">This</a> article will give you more details on its usage.</p>

</details>

<details>
<summary>Can a linked ticket be merged with another ticket?</summary>

<p dir="ltr">Yes, you can merge tickets to a ticket linked to a tracker.</p>

</details>

<details>
<summary>Why am I not able to link tickets to a tracker?</summary>

<p>A ticket cannot be linked to a tracker when any of the following is true :</p><ul><li>When the <strong>mandatory or required ticket fields are not filled</strong> in for a ticket, the ticket cannot be linked to a tracker. Make sure all the mandatory ticket fields are filled in for a ticket before linking it to a tracker ticket.<br /><br /></li><li>When the ticket is <strong>already associated with a parent or a child ticket</strong>, it will not be possible to link such tickets to a tracker.<br /><br /></li><li>When a ticket is <strong>merged with another ticket</strong>. The primary ticket which is closed will not have the Linked tickets option. In those cases, please use the secondary ticket for linking it to a tracker.</li></ul>

</details>

