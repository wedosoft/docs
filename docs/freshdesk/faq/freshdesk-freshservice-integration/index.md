---
sidebar_position: 1
---

# Freshdesk-Freshservice integration

이 섹션에서는 Freshdesk-Freshservice integration와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 고급 기능 및 사용법

<details>
<summary>Will any internal team on Freshservice be able to contact or respond to the customer?</summary>

<p>No. Internal agents on Freshservice are not allowed to respond to customers but can add private notes or responses on the Freshservice incident or service request which will be notified to the customer support agent on Freshdesk. </p>

</details>


## 통합 및 연동

<details>
<summary>Can multiple Freshdesk instances be connected to one Freshservice instance or vice versa?</summary>

<p dir="ltr" style={{ fontSize: "16px" }}>No. Currently, the integration only supports linking between one Freshdesk account and one Freshservice account.</p>

</details>

<details>
<summary>Will the Freshdesk-Freshservice integration use any account API limits?</summary>

<p dir="ltr" style={{ fontSize: "16px" }}>No. Since this is a native integration and not a marketplace app, this will not consume the API limit counts.</p>

</details>

<details>
<summary>Will this integration work if the Freshdesk &amp; Freshservice accounts are located in different data centers?</summary>

<p dir="ltr">No, the integration will work only if the accounts are in the same data center (region).</p>

</details>

<details>
<summary>Is this integration available on the Freshdesk and Freshservice 모바일 앱?</summary>

<p dir="ltr">Currently, it is not available on the mobile app. &nbsp;</p>

</details>

<details>
<summary>Do Freshdesk or Freshservice teams need an additional license to 접근하다 this integration?</summary>

<p dir="ltr">No. No additional costs. It comes free for all paid plans.</p>

</details>

<details>
<summary>Are error logs available for Freshdesk-Freshservice integration?</summary>

<p>No. For audit logs, please reach out to support@freshdesk.com&nbsp;</p><p><br /></p>

</details>


## 관리 및 유지보수

<details>
<summary>Which teams need to be on Freshdesk and Freshservice?</summary>

<p dir="ltr" style={{ fontSize: "16px" }}>Freshdesk is a customer service software (CSS) that helps businesses track, manage, and resolve issues that their customers run into while using their product or service. With Freshdesk, the support teams can provide service across multiple channels, including social, get a complete context from a customer’s timeline of events, assign tickets to agents via Omniroute™, manage shifts, and make use of other customer-support specific capabilities.</p><p dir="ltr" style={{ fontSize: "16px" }}>Freshservice is an internal IT helpdesk and service management platform that helps organizations simplify and automate their internal IT operations.</p><p dir="ltr" style={{ fontSize: "16px" }}><span dir="ltr" style={{ fontSize: "16px" }}>&nbsp;</span></p>

</details>

<details>
<summary>Can a Freshdesk ticket be linked to multiple Freshservice tickets?</summary>

<p>You can achieve this by linking multiple tickets to a tracker in Freshdesk. You can then link the tracker to a Freshservice incident or a service request.</p><p><br /></p>

</details>

<details>
<summary>Can multiple Freshdesk tickets be linked to a Freshservice ticket?</summary>

<p>You can achieve this by linking multiple child tickets to a parent ticket. You can then link the parent ticket to a Freshservice incident or a service request. </p>

</details>

<details>
<summary>Will Freshservice agents be able to change the 상태 of the Freshdesk ticket?</summary>

<p>The Freshservice agent cannot directly change the status of the Freshdesk ticket. However, if the ticket field sync is set up on Freshdesk, whenever the Freshservice agent updates the status of an incident or a service request, it updates the status of the Freshdesk ticket automatically.&nbsp;</p><p><br /></p>

</details>

<details>
<summary>Will the Freshservice agent be able to raise a Freshdesk ticket?</summary>

<p>No. Only agents on Freshdesk will be able to raise incidents and service requests on Freshservice. </p>

</details>

<details>
<summary>Can a ticket be raised from Freshservice to Freshdesk?</summary>

<p>No. Freshservice agents cannot raise Freshdesk tickets using this integration. </p>

</details>

<details>
<summary>Will attachments be available on Freshdesk tickets, Freshservice incidents, and service requests?</summary>

<p>Yes. Agents on Freshdesk and Freshservice will be able to attach files similar to how they do it on normal tickets, incidents, or service requests.&nbsp;</p><p><br /></p>

</details>

<details>
<summary>Will Freshdesk admins be able to draw 분석 for tickets raised on Freshservice?</summary>

<p dir="ltr">Currently, this is not *directly* possible for Freshdesk admins. By adding tags &amp; syncing fields from Freshservice, it is possible to set up reports on Freshdesk. However, Freshservice admins will be able to draw analytics on the tickets raised from Freshdesk using the distinct source ‘Freshdesk’&nbsp;</p><p><br /></p>

</details>

<details>
<summary>Will agents be notified via email for any ticket updates or responses on Freshdesk or Freshservice?</summary>

<p>If the agents are the requesters on the Freshservice ticket, they will receive email notifications.</p><p><br /></p>

</details>

<details>
<summary>Will agents on Freshdesk be notified in-product when an internal team updates their 상태?</summary>

<p dir="ltr">If the ticket field sync has been set up, the status of the Freshdesk ticket will be updated as and when there are updates on Freshservice. However, the Freshdesk agent will not be notified of status updates but for responses on an incident or a service request. &nbsp;</p>

</details>

