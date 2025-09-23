---
sidebar_position: 1
---

# Freshdesk Freshservice 연동 FAQ

Freshdesk Freshservice 연동에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Which teams need to be on Freshdesk and Freshservice?</strong></summary>

Freshdesk is a 고객 서비스 software (CSS) that helps businesses track, manage, and resolve issues that their customers run into while using their product or 서비스. With Freshdesk, the 지원 teams can provide 서비스 across multiple channels, including social, get a complete context from a 고객’s timeline of events, assign 티켓 to 상담원 via Omniroute™, manage shifts, and make use of other 고객-지원 specific capabilities.Freshservice is an internal IT 헬프데스크 and 서비스 management platform that helps organizations simplify and automate their internal IT operations.

</details>

<details>
<summary><strong>Can multiple Freshdesk instances be connected to one Freshservice instance or vice versa?</strong></summary>

No. Currently, the integration only supports linking between one Freshdesk 계정 and one Freshservice 계정.

</details>

<details>
<summary><strong>Will the Freshdesk-Freshservice integration use any 계정 API limits?</strong></summary>

No. Since this is a native integration and not a marketplace app, this will not consume the API limit counts.

</details>

<details>
<summary><strong>Can a Freshdesk ticket be linked to multiple Freshservice 티켓?</strong></summary>

You can achieve this by linking multiple 티켓 to a tracker in Freshdesk. You can then link the tracker to a Freshservice incident or a 서비스 request.

</details>

<details>
<summary><strong>Can multiple Freshdesk 티켓 be linked to a Freshservice ticket?</strong></summary>

You can achieve this by linking multiple child 티켓 to a parent ticket. You can then link the parent ticket to a Freshservice incident or a 서비스 request.

</details>

<details>
<summary><strong>Will this integration work if the Freshdesk & Freshservice accounts are located in different data centers?</strong></summary>

No, the integration will work only if the accounts are in the same data center (region).

</details>

<details>
<summary><strong>Is this integration available on the Freshdesk and Freshservice mobile apps?</strong></summary>

Currently, it is not available on the mobile app.

</details>

<details>
<summary><strong>Will any internal 팀 on Freshservice be able to contact or respond to the 고객?</strong></summary>

No. Internal 상담원 on Freshservice are not allowed to respond to customers but can add private notes or responses on the Freshservice incident or 서비스 request which will be notified to the 고객 지원 agent on Freshdesk.

</details>

<details>
<summary><strong>Do Freshdesk or Freshservice teams need an additional license to access this integration?</strong></summary>

No. No additional costs. It comes free for all paid 요금제.

</details>

<details>
<summary><strong>Will Freshservice 상담원 be able to change the status of the Freshdesk ticket?</strong></summary>

The Freshservice agent cannot directly change the status of the Freshdesk ticket. However, if the ticket field sync is set up on Freshdesk, whenever the Freshservice agent updates the status of an incident or a 서비스 request, it updates the status of the Freshdesk ticket automatically.

</details>

<details>
<summary><strong>Will the Freshservice agent be able to raise a Freshdesk ticket?</strong></summary>

No. Only 상담원 on Freshdesk will be able to raise incidents and 서비스 requests on Freshservice.

</details>

<details>
<summary><strong>Can a ticket be raised from Freshservice to Freshdesk?</strong></summary>

No. Freshservice 상담원 cannot raise Freshdesk 티켓 using this integration.

</details>

<details>
<summary><strong>Will attachments be available on Freshdesk 티켓, Freshservice incidents, and 서비스 requests?</strong></summary>

Yes. 상담원 on Freshdesk and Freshservice will be able to attach files similar to how they do it on normal 티켓, incidents, or 서비스 requests.

</details>

<details>
<summary><strong>Are 오류 logs available for Freshdesk-Freshservice integration?</strong></summary>

No. For audit logs, please reach out to 지원@freshdesk.com

</details>

<details>
<summary><strong>Will Freshdesk admins be able to draw 분석 for 티켓 raised on Freshservice?</strong></summary>

Currently, this is not *directly* possible for Freshdesk admins. By adding tags & syncing fields from Freshservice, it is possible to set up 보고서 on Freshdesk. However, Freshservice admins will be able to draw 분석 on the 티켓 raised from Freshdesk using the distinct source ‘Freshdesk’

</details>

<details>
<summary><strong>Will 상담원 be notified via 이메일 for any ticket updates or responses on Freshdesk or Freshservice?</strong></summary>

If the 상담원 are the requesters on the Freshservice ticket, they will receive 이메일 notifications.

</details>

<details>
<summary><strong>Will 상담원 on Freshdesk be notified in-product when an internal 팀 updates their status?</strong></summary>

If the ticket field sync has been set up, the status of the Freshdesk ticket will be updated as and when there are updates on Freshservice. However, the Freshdesk agent will not be notified of status updates but for responses on an incident or a 서비스 request.

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
