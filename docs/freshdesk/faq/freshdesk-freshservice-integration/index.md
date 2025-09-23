---
sidebar_position: 1
---

# Freshdesk Freshservice 연동 FAQ

Freshdesk Freshservice 연동에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Which teams need 로 be 에 Freshdesk 그리고 Freshservice?</strong></summary>

Freshdesk is 고객 서비스 software (CSS) that helps businesses track, manage, 그리고 resolve issues that their customers run into while using their product 또는 서비스. 와 함께 Freshdesk, 지원 teams can 제공하다 서비스 across 다수의 channels, including social, get complete context 에서 고객’s timeline 의 events, assign 티켓 로 상담원 via Omniroute™, manage shifts, 그리고 make use 의 other 고객-지원 특정한 capabilities. Freshservice is internal IT 헬프데스크 그리고 서비스 management platform that helps organizations simplify 그리고 automate their internal IT operations.

</details>

<details>
<summary><strong>Can 다수의 Freshdesk instances be connected 로 one Freshservice instance 또는 vice versa?</strong></summary>

No. Currently, 연동 only supports linking between one Freshdesk 계정 그리고 one Freshservice 계정.

</details>

<details>
<summary><strong>Will Freshdesk-Freshservice 연동 use any 계정 API limits?</strong></summary>

No. Since this is native 연동 그리고 not marketplace app, this will not consume API limit counts.

</details>

<details>
<summary><strong>Can Freshdesk ticket be linked 로 다수의 Freshservice 티켓?</strong></summary>

You can achieve this 에 의해 linking 다수의 티켓 로 tracker 에서 Freshdesk. You can 그러면 link tracker 로 Freshservice incident 또는 서비스 request.

</details>

<details>
<summary><strong>Can 다수의 Freshdesk 티켓 be linked 로 Freshservice ticket?</strong></summary>

You can achieve this 에 의해 linking 다수의 child 티켓 로 parent ticket. You can 그러면 link parent ticket 로 Freshservice incident 또는 서비스 request.

</details>

<details>
<summary><strong>Will this 연동 work 만약 Freshdesk & Freshservice accounts are located 에서 different 데이터 centers?</strong></summary>

No, 연동 will work only 만약 accounts are 에서 same 데이터 center (region).

</details>

<details>
<summary><strong>Is this 연동 사용 가능한 에 Freshdesk 그리고 Freshservice mobile apps?</strong></summary>

Currently, it is not 사용 가능한 에 mobile app.

</details>

<details>
<summary><strong>Will any internal 팀 에 Freshservice be able 로 연락하다 또는 respond 로 고객?</strong></summary>

No. Internal 상담원 에 Freshservice are not allowed 로 respond 로 customers 하지만 can 추가 private notes 또는 responses 에 Freshservice incident 또는 서비스 request which will be notified 로 고객 지원 agent 에 Freshdesk.

</details>

<details>
<summary><strong>Do Freshdesk 또는 Freshservice teams need additional license 로 access this 연동?</strong></summary>

No. No additional costs. It comes free 위해 all paid 요금제.

</details>

<details>
<summary><strong>Will Freshservice 상담원 be able 로 change status 의 Freshdesk ticket?</strong></summary>

Freshservice agent cannot directly change status 의 Freshdesk ticket. However, 만약 ticket 필드 sync is set up 에 Freshdesk, whenever Freshservice agent updates status 의 incident 또는 서비스 request, it updates status 의 Freshdesk ticket automatically.

</details>

<details>
<summary><strong>Will Freshservice agent be able 로 raise Freshdesk ticket?</strong></summary>

No. Only 상담원 에 Freshdesk will be able 로 raise incidents 그리고 서비스 requests 에 Freshservice.

</details>

<details>
<summary><strong>Can ticket be raised 에서 Freshservice 로 Freshdesk?</strong></summary>

No. Freshservice 상담원 cannot raise Freshdesk 티켓 using this 연동.

</details>

<details>
<summary><strong>Will attachments be 사용 가능한 에 Freshdesk 티켓, Freshservice incidents, 그리고 서비스 requests?</strong></summary>

Yes. 상담원 에 Freshdesk 그리고 Freshservice will be able 로 attach files similar 로 how they do it 에 normal 티켓, incidents, 또는 서비스 requests.

</details>

<details>
<summary><strong>Are 오류 logs 사용 가능한 위해 Freshdesk-Freshservice 연동?</strong></summary>

No. 위해 audit logs, please 문의하다 로 지원@freshdesk.com

</details>

<details>
<summary><strong>Will Freshdesk admins be able 로 draw 분석 위해 티켓 raised 에 Freshservice?</strong></summary>

Currently, this is not *directly* possible 위해 Freshdesk admins. 에 의해 adding tags & syncing fields 에서 Freshservice, it is possible 로 set up 보고서 에 Freshdesk. However, Freshservice admins will be able 로 draw 분석 에 티켓 raised 에서 Freshdesk using distinct source ‘Freshdesk’

</details>

<details>
<summary><strong>Will 상담원 be notified via 이메일 위해 any ticket updates 또는 responses 에 Freshdesk 또는 Freshservice?</strong></summary>

만약 상담원 are requesters 에 Freshservice ticket, they will receive 이메일 notifications.

</details>

<details>
<summary><strong>Will 상담원 에 Freshdesk be notified 에서-product 언제 internal 팀 updates their status?</strong></summary>

만약 ticket 필드 sync has been set up, status 의 Freshdesk ticket will be updated as 그리고 언제 there are updates 에 Freshservice. However, Freshdesk agent will not be notified 의 status updates 하지만 위해 responses 에 incident 또는 서비스 request.

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
