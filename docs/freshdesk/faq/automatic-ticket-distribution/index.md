---
sidebar_position: 1
---

# 자동 티켓 배포 FAQ

자동 티켓 배포에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Does Round-Robin functionality work only during business hours?</strong></summary>

round robin feature 또는 자동 assignment functionality would work whenever icon next 로 profile photo is togged 에. This is not tied 로 business hours. As 의 now, this feature will work irrespective 의 포털's business hours. Even 만약 agent turns 에 auto ticket assignment during **non-business hours**, system will continue assigning 티켓 로 that agent. workaround would be 로 not give agent permission 로 turn 에 자동 assignment 에 의해 unchecking **"Allow 상담원 로 change their availability 위해 자동 ticket assignment" -**this would give admins 로 control ticket assignment 그리고 could manually switch 에 round robin during business hours 에서 **대시보드 -> 사용 가능한 상담원 -> ticket assignment.** ****

</details>

<details>
<summary><strong>Does Round-Robin assign 티켓 에서 alphabetical order?</strong></summary>

auto-assignment feature will assign 티켓 로 상담원 as per order 에서 which they have been added 로 group. 위해 example, 만약 상담원 C, , 그리고 B are added 로 group 에서 that order 그리고 만약 they are all online 로 accept 티켓, 티켓 will also be assigned 에서 same order. Therefore, 만약 티켓 have 로 be assigned 에서 alphabetical order, please manually rearrange them accordingly 에서 **관리자 > 팀 > Groups > 클릭 에 편집** 로 achieve this.

</details>

<details>
<summary><strong>What happens 로 ticket 언제 caps 위해 all 상담원 are met?</strong></summary>

언제 all 사용 가능한 상담원 reach their ticket cap when you have 자동 assignment turned 에, new incoming 티켓 will be queued 에서 unassigned bucket. Please 확인하다 cap 에서**관리자 > 팀 > Groups > 클릭 에 편집**next 로 one you would want 로 확인하다 this 위해 그리고 see number listed 에서 maximum 티켓 per agent under **"Load Balanced ticket assignment."** These will be assigned 언제 any one 의 agent's ticket count falls below capped level.

</details>

<details>
<summary><strong>How does 자동 ticket assignment work after agent logs out은 무엇인가요?</strong></summary>

This depends 에 whether agent is part 의 groups 위해 which availability is managed centrally 에 의해 admins ( can be configured under 관리자-> Groups) ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50004910431/original/1q_n2S4M5IxsK9dbrkEcgKKX7lS9K1B7AQ.png?1646382490) **Case 1- 상담원 have ability 로 manage statuses****** 만약 상담원 have access 로 change their availability 에서 all groups that they're part 의, they become unavailable 위해 자동 assignment 언제 they log out. **Case 2- Agent's availability is centrally managed.****** 만약 agent is part 의 one 또는 more groups where availability is managed centrally 에 의해 Admins, agent's availability prior 로 logging out is considered 위해 자동 routing. 위해 example, say Agent 그리고 Agent B are part 의 groups where availability is managed centrally 에 의해 admins. Agent 's status is 사용 가능한 언제 they log out. Agent B's status is unavailable when they log out. 티켓 will continue being assigned 로 agent since they were 사용 가능한 에서 time 의 log out.

</details>

<details>
<summary><strong>자동 ticket assignment?이란은 무엇인가요?</strong></summary>

You can automatically assign 티켓 로 상담원 에서 다양한 groups 에 의해 enabling 자동 assignment option 위해 corresponding group. Below are steps 로 활성화 that; - 로그인 로 your Freshdesk 계정 as 관리자. - 이동 로 관리자 에서 menu. Under 팀, 클릭 에 Groups. - 선택 group 위해 which you want 로 활성화 자동 assignment 그리고 클릭 ‘편집’ icon. - Go 로 Group Properties 그리고 활성화 ‘자동 ticket assignment.’ - 선택 appropriate assignment mode 그리고 agent availability parameter. - 클릭 ‘저장’ 로 업데이트 group 설정. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008552935/original/ZF2Sn-8Si5T2MUCv2a5buA2ddDOS0Rch3A.gif?1686126546) Please 문의하다 로 [지원@freshdesk.com](mailto:지원@freshdesk.com) 만약 you require further assistance.

</details>

<details>
<summary><strong>Is there way 로 prevent 자동 ticket assignment 언제 agent replies 로 unassigned ticket?</strong></summary>

자동 ticket assignment would be caused 에 의해 action 의 automation rule that runs 에 ticket updates - 'Automatically assign ticket 로 first responder'. You could 비활성화 this rule 만약 you'd like 로 have ticket assigned before being responded 로. Go 로 **관리자 > Workflows > Automations > Ticket Updates** toggle this off.

</details>

<details>
<summary><strong>automatically assign 티켓 based 에 agent workload?할 수 있나요은 무엇인가요?</strong></summary>

Yes, Freshdesk has feature called **Load-based ticket assignment**, using which 티켓 could be assigned within group, based 에 current ticket load 위해 agent. Please 이동 로 **관리자 > 팀 > Groups > 클릭 에 편집**next 로 group 위해 which this feature has 로 be enabled 그리고 선택 **"Load Balanced Ticket Assignment"**radio button under 자동 ticket assignment.

</details>

<details>
<summary><strong>Is there report 에 total time that agent has been 사용 가능한 위해 ticket assignment?</strong></summary>

Currently, it is not possible 로 report 에 time duration 위해 which agent has been 사용 가능한 로 accept 티켓 through **"자동 ticket assignment"** feature. However, please 이동 로 **D****ashboard -> agent availability -> ticket assignment**where as 관리자 you would be able 로 see number 의 hours since 언제 agent has been automatically receiving 티켓.

</details>

<details>
<summary><strong>활성화 Round Robin Ticket Assignment 에서 my 계정?하는 방법은 무엇인가요?</strong></summary>

Within Freshdesk, you would have option 로 automatically assign 티켓 로 상담원 within group, 에서 round-robin. 로 활성화 자동 ticket assignment 위해 group, please 이동 로 **관리자 > 팀 > Groups >** 편집(corresponding 로 group) 그리고 turn 에 "**자동 Ticket Assignment**". You could 선택 mode 의 자동 Ticket assignment as " Round Robin". 참고: This feature is 사용 가능한 only 에서 Estate 그리고 Forest 요금제.

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
