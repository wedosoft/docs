---
sidebar_position: 1
---

# Freshdesk-Freshservice 연동 FAQ

Freshdesk-Freshservice 연동에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 사용자 관리

<details>
<summary><strong>Which teams need to be on Freshdesk and Freshservice?</strong></summary>

Freshdesk is a customer service software (CSS) that helps businesses track, manage, and resolve issues that their customers run into while using their product or service. With Freshdesk, the support teams can provide service across multiple channels, including social, get a complete context from a customer’s timeline of events, assign tickets to agents via Omniroute™, manage shifts, and make use of other customer-support specific capabilities.Freshservice is an internal IT helpdesk and service management platform that helps organizations simplify and automate their internal IT operations.

</details>

<details>
<summary><strong>Will any internal team on Freshservice be able to contact or respond to the customer?</strong></summary>

No. Internal agents on Freshservice are not allowed to respond to customers but can add private notes or responses on the Freshservice incident or service request which will be notified to the customer support agent on Freshdesk.

</details>

<details>
<summary><strong>Do Freshdesk or Freshservice teams need an additional license to access this integration?</strong></summary>

No. No additional costs. It comes free for all paid plans.

</details>

<details>
<summary><strong>Will Freshservice agents be able to change the status of the Freshdesk ticket?</strong></summary>

The Freshservice agent cannot directly change the status of the Freshdesk ticket. However, if the ticket field sync is set up on Freshdesk, whenever the Freshservice agent updates the status of an incident or a service request, it updates the status of the Freshdesk ticket automatically.

</details>

<details>
<summary><strong>Will the Freshservice agent be able to raise a Freshdesk ticket?</strong></summary>

No. Only agents on Freshdesk will be able to raise incidents and service requests on Freshservice.

</details>

<details>
<summary><strong>Will agents be notified via email for any ticket updates or responses on Freshdesk or Freshservice?</strong></summary>

If the agents are the requesters on the Freshservice ticket, they will receive email notifications.

</details>

<details>
<summary><strong>Will agents on Freshdesk be notified in-product when an internal team updates their status?</strong></summary>

If the ticket field sync has been set up, the status of the Freshdesk ticket will be updated as and when there are updates on Freshservice. However, the Freshdesk agent will not be notified of status updates but for responses on an incident or a service request.

</details>


## 📋 일반 질문

<details>
<summary><strong>Can multiple Freshdesk instances be connected to one Freshservice instance or vice versa?</strong></summary>

No. Currently, the integration only supports linking between one Freshdesk account and one Freshservice account.

</details>

<details>
<summary><strong>Can a Freshdesk ticket be linked to multiple Freshservice tickets?</strong></summary>

You can achieve this by linking multiple tickets to a tracker in Freshdesk. You can then link the tracker to a Freshservice incident or a service request.

</details>

<details>
<summary><strong>Can multiple Freshdesk tickets be linked to a Freshservice ticket?</strong></summary>

You can achieve this by linking multiple child tickets to a parent ticket. You can then link the parent ticket to a Freshservice incident or a service request.

</details>

<details>
<summary><strong>Is this integration available on the Freshdesk and Freshservice mobile apps?</strong></summary>

Currently, it is not available on the mobile app.

</details>

<details>
<summary><strong>Can a ticket be raised from Freshservice to Freshdesk?</strong></summary>

No. Freshservice agents cannot raise Freshdesk tickets using this integration.

</details>

<details>
<summary><strong>Will attachments be available on Freshdesk tickets, Freshservice incidents, and service requests?</strong></summary>

Yes. Agents on Freshdesk and Freshservice will be able to attach files similar to how they do it on normal tickets, incidents, or service requests.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>Will the Freshdesk-Freshservice integration use any account API limits?</strong></summary>

No. Since this is a native integration and not a marketplace app, this will not consume the API limit counts.

</details>

<details>
<summary><strong>Will this integration work if the Freshdesk & Freshservice accounts are located in different data centers?</strong></summary>

No, the integration will work only if the accounts are in the same data center (region).

</details>

<details>
<summary><strong>Will Freshdesk admins be able to draw analytics for tickets raised on Freshservice?</strong></summary>

Currently, this is not *directly* possible for Freshdesk admins. By adding tags & syncing fields from Freshservice, it is possible to set up reports on Freshdesk. However, Freshservice admins will be able to draw analytics on the tickets raised from Freshdesk using the distinct source ‘Freshdesk’

</details>


## 📋 문제 해결

<details>
<summary><strong>Are error logs available for Freshdesk-Freshservice integration?</strong></summary>

No. For audit logs, please reach out to support@freshdesk.com

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
