---
sidebar_position: 1
---

# 자동 Ticket 배포 FAQ

자동 Ticket 배포에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Does Round-Robin 기능 work 만 during 비즈니스 시간? 는 무엇인가요?</strong></summary>

round robin 기능 또는 자동 할당 기능 할 것입니다 work whenever icon next 로 profile photo is togged 에서. This is not tied 로 비즈니스 시간. As 의 now, this 기능 할 것입니다 work irrespective 의 portal's 비즈니스 시간. 심지어 if agent turns 에서 auto ticket 할당 during **non-비즈니스 시간**, system 할 것입니다 continue assigning tickets 로 agent. workaround 될 것입니다 로 not give agent permission 로 turn 에서 자동 할당 에 의해 unchecking **"Allow agents 로 change their 가용성 위해 자동 ticket 할당" -**this 할 것입니다 give admins 로 control ticket 할당 및 할 수 있습니다 manually switch 에서 round robin during 비즈니스 시간 에서 **Dashboard -> 사용 가능 agents -> ticket 할당. ** ****

</details>

<details>
<summary><strong>Does Round-Robin assign tickets 에서 alphabetical order? 는 무엇인가요?</strong></summary>

auto-할당 기능 할 것입니다 assign tickets 로 agents as per order 에서 they have been added 로 group. 위해 example, if agents C, A, 및 B are added 로 group 에서 order 및 if they are 모든 online 로 accept tickets, tickets 할 것입니다 또한 be assigned 에서 같은 order. 따라서, if tickets 해야 합니다 be assigned 에서 alphabetical order, please manually rearrange them accordingly 에서 **Admin > Team > Groups > click 에서 edit** 로 achieve this.

</details>

<details>
<summary><strong>What happens 로 ticket caps 위해 모든 agents are met? 는 무엇인가요?</strong></summary>

모든 사용 가능 agents reach their ticket cap you have 자동 할당 turned 에서, 새로운 incoming tickets 될 것입니다 queued 에서 unassigned bucket. Please check cap 에서**Admin > Team > Groups > click 에서 edit**next 로 one you 할 것입니다 하고 싶습니다 check this 위해 및 see number listed 에서 maximum tickets per agent 하위에서 **"부하 Balanced ticket 할당. "** These 될 것입니다 assigned any one 의 agent's ticket count falls 아래에 capped level.

</details>

<details>
<summary><strong>How does 자동 ticket 할당 work after agent logs out는 무엇인가요?</strong></summary>

This depends 에서 whether agent is part 의 groups 위해 가용성 is managed centrally 에 의해 admins ( 될 수 있습니다 configured 하위에서 Admin-> Groups)! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50004910431/original/1q_n2S4M5IxsK9dbrkEcgKKX7lS9K1B7AQ. png? 1646382490) **Case 1- Agents have ability 로 manage statuses****** If agents have access 로 change their 가용성 에서 모든 groups they're part 의, they become unavailable 위해 자동 할당 they log out. **Case 2- Agent's 가용성 is centrally managed. ****** If agent is part 의 one 또는 더 groups 가용성 is managed centrally 에 의해 Admins, agent's 가용성 prior 로 logging out is considered 위해 자동 routing. 위해 example, say Agent 및 Agent B are part 의 groups 가용성 is managed centrally 에 의해 admins. Agent A's status is 사용 가능 they log out. Agent B's status is unavailable they log out. Tickets 할 것입니다 continue being assigned 로 agent since they were 사용 가능 에서 time 의 log out.

</details>

<details>
<summary><strong>What is 자동 ticket 할당? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 automatically assign tickets 로 agents 에서 various groups 에 의해 enabling 자동 할당 option 위해 corresponding group. 아래에 are steps 로 활성화 that; - Login 로 your Freshdesk account as administrator. - Navigate 로 Admin 에서 menu. 하위에서 Team, click 에서 Groups. - Select group 위해 you 하고 싶습니다 활성화 자동 할당 및 click ‘Edit’ icon. - Go 로 Group Properties 및 활성화 ‘자동 ticket 할당. ’ - Choose appropriate 할당 mode 및 agent 가용성 parameter. - Click ‘Save’ 로 업데이트 group settings.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50008552935/original/ZF2Sn-8Si5T2MUCv2a5buA2ddDOS0Rch3A. gif? 1686126546) Please reach out 로 [support@freshdesk. com](mailto: support@freshdesk. com) if you require further assistance.

</details>

<details>
<summary><strong>Is there way 로 prevent 자동 ticket 할당 agent replies 로 unassigned ticket? 는 무엇인가요?</strong></summary>

자동 ticket 할당 될 것입니다 caused 에 의해 action 의 automation rule runs 에서 ticket updates - 'Automatically assign ticket 로 first responder'. You 할 수 있습니다 비활성화 this rule if you'd like 로 have ticket assigned before being responded 로. Go 로 **Admin > Workflows > Automations > Ticket Updates** toggle this off.

</details>

<details>
<summary><strong>Is it possible 로 automatically assign tickets based 에서 agent 워크로드? 는 무엇인가요?</strong></summary>

Yes, Freshdesk has 기능 called **부하-based ticket 할당**, using tickets 될 수 있습니다 assigned within group, based 에서 current ticket 부하 위해 agent. Please navigate 로 **Admin > Team > Groups > click 에서 edit**next 로 group 위해 this 기능 has 로 be enabled 및 choose **"부하 Balanced Ticket 할당"**radio button 하위에서 자동 ticket 할당.

</details>

<details>
<summary><strong>Is there report 에서 total time agent has been 사용 가능 위해 ticket 할당? ?</strong></summary>

Currently, it is not possible 로 report 에서 time duration 위해 agent has been 사용 가능 로 accept tickets 통해 the**"자동 ticket 할당"** 기능. 하지만, please navigate 로 **D****ashboard -> agent 가용성 -> ticket 할당**as Admin you 할 수 있을 것입니다 see number 의 hours since agent has been automatically receiving tickets.

</details>

<details>
<summary><strong>How do I 활성화 Round Robin Ticket 할당 에서 my account? 는 무엇인가요?</strong></summary>

Within Freshdesk, you 할 것입니다 have option 로 automatically assign tickets 로 agents within group, 에서 round-robin. 로 활성화 자동 ticket 할당 위해 group, please navigate 로 **Admin > Team > Groups >** Edit(corresponding 로 group) 및 turn 에서 "**자동 Ticket 할당**". You 할 수 있습니다 choose mode 의 자동 Ticket 할당 as " Round Robin". Note: This 기능 is 사용 가능 만 에서 Estate 및 Forest plans.

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
