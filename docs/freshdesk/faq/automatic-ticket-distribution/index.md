---
sidebar_position: 1
---

# Automatic Ticket Distribution

이 섹션에서는 Automatic Ticket Distribution와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 기본 설정 및 구성

<details>
<summary>어떻게 활성화하다 Round Robin Ticket 할당 in my account?</summary>

<p dir="ltr">Within Freshdesk, you would have the option to automatically assign tickets to agents within a group, in round-robin. To enable automatic ticket assignment for a group, please navigate to <strong>Admin &gt; Team &gt; Groups &gt;</strong> Edit(corresponding to the group) and turn on "<strong>Automatic Ticket Assignment</strong>". You could choose the mode of Automatic Ticket assignment as " Round Robin".</p><p><br /></p><p>Note: This feature is available only in the Estate and Forest plans.</p>

</details>


## 관리 및 유지보수

<details>
<summary>Does the Round-Robin functionality work only during business hours?</summary>

<p ><span style={{ fontSize: "16px" }}>The round robin feature or the automatic assignment functionality would work whenever the icon next to the profile photo is togged on. This is not tied to the business hours. </span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>As of now, this feature will work irrespective of the portal's business hours. Even if the agent turns on auto ticket assignment during <strong>non-business hours</strong>, the system will continue assigning the tickets to that agent. </span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>A workaround would be to not give the agent the permission to turn on the automatic assignment by unchecking <strong>"Allow agents to change their availability for automatic ticket assignment" - </strong>this would give the admins to control the ticket assignment and could manually switch on round robin during business hours in <strong>Dashboard -&gt; Available agents -&gt; ticket assignment.</strong></span></p><p ><strong><span style={{ fontSize: "16px" }}></span></strong></p><p></p><p><br /></p><p></p><p ><span style={{ fontSize: "16px" }}></span></p><p><br /></p>

</details>

<details>
<summary>Does the Round-Robin assign tickets in alphabetical order?</summary>

<p><span style={{ fontSize: "16px" }}>The auto-assignment feature will assign the tickets to the agents as per the order in which they have been added to the group. For example, if agents C, A, and B are added to a group in that order and if they are all online to accept tickets, the tickets will also be assigned in the same order. </span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>Therefore, if the tickets have to be assigned in alphabetical order, please manually rearrange them accordingly in <strong dir="ltr">Admin &gt; Team &gt; Groups &gt; click on edit</strong> to achieve this.</span></p>

</details>

<details>
<summary>What happens to a ticket when the caps for all agents are met?</summary>

<p><span style={{ fontSize: "16px" }}>When all available agents reach their ticket cap when you have automatic assignment turned on, new incoming tickets will be queued in the unassigned bucket. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>Please check the cap in<strong dir="ltr"> Admin &gt; Team &gt; Groups &gt; click on edit </strong>next to the one you would want to check this for and see the number listed in maximum tickets per agent under <strong>"Load Balanced ticket assignment."</strong></span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>These will be assigned when any one of the agent's ticket count falls below the capped level.</span></p>

</details>

<details>
<summary>How does Automatic ticket 할당 work after an agent logs out</summary>

<p ><span dir="ltr" style={{ fontSize: "16px" }}>This depends on whether an agent is a part of groups for which availability is managed centrally by admins ( can be configured under Admin-&gt; Groups)</span></p><p ><br /></p><p ><span dir="ltr" style={{ fontSize: "16px" }}><img src="#" style={{ width: "auto" }} class="fr-fil fr-dib fr-bordered" /></span><br /></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(0, 0, 0)", fontFamily: "-apple-system, ", fontWeight: "400", textAlign: "left", textIndent: "0px" }}><span dir="ltr" style={{ boxSizing: "border-box", fontSize: "16px" }}><strong dir="ltr" style={{ boxSizing: "border-box", fontWeight: "700" }}>Case 1- Agents have the ability to manage statuses&nbsp;</strong></span><strong style={{ boxSizing: "border-box", fontWeight: "700" }}><br /></strong></p><p style={{ boxSizing: "border-box", marginBottom: "0px", marginLeft: "0px", fontSize: "13px", lineHeight: "18px", wordBreak: "normal", overflowWrap: "break-word", color: "rgb(0, 0, 0)", fontFamily: "-apple-system, ", fontWeight: "400", textAlign: "left", textIndent: "0px" }}><span dir="ltr" style={{ boxSizing: "border-box", fontSize: "16px" }}>If agents have access to change their availability in all the groups that they're a part of, they become unavailable for automatic assignment when they log out.</span></p><p ><br /></p><p ><span dir="ltr" style={{ fontSize: "16px" }}><strong dir="ltr">Case 2- Agent's availability is centrally managed.</strong></span><strong ><br /></strong></p><p ><span dir="ltr" style={{ fontSize: "16px" }}>If an agent is a part of one or more groups where availability is managed centrally by Admins, the agent's availability prior to logging out is considered for automatic routing.&nbsp;</span></p><p ><br /></p><p ><span dir="ltr" style={{ fontSize: "16px" }}>For example, say Agent A and Agent B are part of groups where availability is managed centrally by admins. Agent A's status is available when they log out. Agent B's status is unavailable when they log out. Tickets will continue being assigned to agent A since they were available at the time of log out.</span></p><p ><br /></p><p ><br /></p><p ><br /></p>

</details>

<details>
<summary>무엇인가요 automatic ticket 할당?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}>You can automatically assign tickets to agents in various groups by enabling the automatic assignment option for the corresponding group. Below are the steps to enable that;</span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><ol style={{ marginBottom: "0px", paddingInlineStart: "48px", fontFamily: "Arial"" }}><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Login to your Freshdesk account as an&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>administrator</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Navigate to&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Admin</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;from the menu. Under&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Team</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>, click on&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Groups</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Select the group for which you want to enable automatic assignment and click the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>‘Edit’</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;icon.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Go to Group Properties and enable ‘</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Automatic ticket assignment.</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>’</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Choose the appropriate assignment mode and agent availability parameter.</span></span></p></li><li dir="ltr" style={{ listStyleType: "decimal", fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Click&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>‘Save’</span><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;to update the group settings.</span></span><br /><br /></p></li></ol><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}><img src="#" style={{ width: "702px", display: "block", float: "none", verticalAlign: "top", margin: "5px auto", textAlign: "center" }} class="fr-dib fr-bordered fr-shadow" /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><br /><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Please reach out to&nbsp;</span><a href="mailto:support@freshdesk.com" style={{ fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none", fontFamily: "Arial"" }}>support@freshdesk.com</span></a></span><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;if you require further assistance.</span></p>

</details>

<details>
<summary>Is there a way to prevent automatic ticket 할당 when an agent replies to an unassigned ticket?</summary>

<p>The automatic ticket assignment would be caused by the action of the automation rule that runs on ticket updates - 'Automatically assign the ticket to the first responder'. </p><p><br /></p><p dir="ltr">You could disable this rule if you'd like to have the ticket assigned before being responded to. Go to <strong>Admin &gt; Workflows &gt; Automations &gt; Ticket Updates</strong> toggle this off.</p>

</details>

<details>
<summary>가능한가요 to automatically assign tickets based on agent workload?</summary>

<p><span style={{ fontSize: "16px" }}>Yes, Freshdesk has a feature called <strong>Load-based ticket assignment</strong>, using which tickets could be assigned within a group, based on the current ticket load for an agent. </span></p><p><br /></p><p><span style={{ fontSize: "16px" }}>Please navigate to <strong dir="ltr">Admin &gt; Team &gt; Groups &gt; click on edit </strong>next to the group for which this feature has to be enabled and choose the <strong>"Load Balanced Ticket Assignment" </strong>radio button under automatic ticket assignment. </span></p><p><br /></p><p><br /></p>

</details>

<details>
<summary>Is there a 보고서 on the total time that an agent has been available for ticket 할당?</summary>

<p dir="ltr"><span class="" style={{ fontSize: "16px" }}>Currently,</span><span style={{ fontSize: "16px" }}> it is not possible to report on the time duration for which the agent has been available to accept tickets through the<strong> "Automatic ticket assignment"</strong> feature. </span></p><p dir="ltr" ><br /></p><p dir="ltr" ><span style={{ fontSize: "16px" }}>However, please navigate to the <strong>D</strong><strong>ashboard -&gt; agent availability -&gt; ticket assignment </strong>where as an Admin you would be able to see the number of hours since when the agent has been automatically receiving tickets.</span></p>

</details>

