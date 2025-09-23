---
sidebar_position: 1
---

# 고객 만족도 조사 FAQ

고객 만족도 조사에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>have more than a 3 point scale on my 고객 satisfaction surveys하는 방법은 무엇인가요?</strong></summary>

With the new Satisfaction Survey in Freshdesk, you would be able to customize your surveys with more than 3 point scales. This new satisfaction survey is available from the** Pro** (previously **Estate) **요금제 onwards.So, if you are using an 계정 in the **Pro or Enterprise** 요금제 (previously  **Estate or Forest 요금제)**, please do drop in an 이메일 to **지원@freshdesk.com** and we would have this enabled.Please navigate to **관리자 -> Workflows -> 고객 satisfaction -> click**** on edit** to customize this once it is enabled.

</details>

<details>
<summary><strong>change the Survey Pitch하는 방법은 무엇인가요?</strong></summary>

While sending the survey, you could **add your own content**, requesting the 고객 to rate their experience. This could be something like "Please tell us what you think of your 지원 experience".If you wish to change this text, please navigate to **관리자 -> Workflows -> 고객 Satisfaction -> Edit **which would allow you to edit the content available under the **"Survey Question"** field. Hit on **"Save"** to use the edited text for future surveys.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001119968/original/_yNgtfRGIkaybl_DQGnXMO5FDtdripyhTA.png?1589867787)

</details>

<details>
<summary><strong>have a questionnaire after the default survey is sent out하는 방법은 무엇인가요?</strong></summary>

With the new surveys in Freshdesk, you would be able to set up an additional set of questions that you could send out to the customers.Please navigate to **관리자 -> Workflows ** -> 고객 satisfaction -> click on edit next to the survey to be taken to the survey details. Below the thank you page, there is an additional questions section that could be set up and sent out to the 고객.If you are on the **Estate 요금제 or higher**, drop a quick 이메일 to **지원@freshdesk.com** to have this enabled for your 계정.

</details>

<details>
<summary><strong>I haven't sent out the survey to the 고객 but still there seems to a rating on the ticket. How is this possible?</strong></summary>

If you have enabled the satisfaction surveys, the customers would also have the ability to rate the closed ticket from the 고객 포털 itself.Please check whether it is enabled in **관리자 -> Workflows **-> 고객 satisfaction and toggle the survey off if you do not want this to go out to customers.

</details>

<details>
<summary><strong>I have configured the 고객 satisfaction surveys right, but when I run a quick test, I do not get the survey.</strong></summary>

The surveys would not be sent to you if the **requestor of the ticket is the same as an Agent** 이메일 address.Hence, please try sending the survey to a ticket where your agent address isn't the requestor (preferably from your personal address).

</details>

<details>
<summary><strong>왜 the 고객 satisfaction surveys are not being sent인가요?</strong></summary>

If the setting is set to send the survey when the status of a ticket is changed to Resolved or Closed, the satisfaction survey would be sent along with the Requester notifications of **'Agent Solves the Ticket'** and **'Agent Closes the Ticket'** respectively.Please navigate to **관리자 > Workflows** > 이메일 notifications > Requester notifications and toggle on the corresponding 이메일 notification to make sure that the survey is sent. If this is toggled off, then the survey would not be sent.The survey will also not be sent on 티켓 where the **requester of the ticket is also an agent** on the 헬프데스크 as it is not considered ideal for an agent to rate another agent.

</details>

<details>
<summary><strong>have an NPS score using Freshdesk surveys하는 방법은 무엇인가요?</strong></summary>

As of now, we do not have the ability to calculate the **NPS** via the Freshdesk surveys, but you sure could try out the [**Integration with Survey Monkey**](https://지원.freshdesk.com/지원/solutions/articles/119431-the-surveymonkey-app)** **that would help you get this done.Please navigate to **관리자 -> ****지원 Operations**** -> Apps** to bring this into your system.

</details>

<details>
<summary><strong>create a new 고객 Satisfaction Survey하는 방법은 무엇인가요?</strong></summary>

You would have a default 고객 satisfaction survey configured on your 계정. If you are looking to create a new and customized Satisfaction Survey, you could have this set up under **관리자 -> Workflows -> 고객 Satisfaction -> New Survey**.Once this is configured, you would be able to choose from the Survey list on which Survey you would like to associate with your 계정. At any given time, you could have only one Survey turned on.This feature is available from the **Pro** 요금제 (Previously **Garden**) onwards.

</details>

<details>
<summary><strong>send CSAT survey in different languages for different customers할 수 있나요?</strong></summary>

From Estate and above 요금제, you can localize the CSAT survey forms in your Freshdesk 계정 to match the preferred language in the 고객’s profile.Please refer to the article in the [](https://지원.freshdesk.com/지원/solutions/articles/50000000119-localize-your-feedback-forms-with-multilingual-고객-satisfaction-surveys)[link](https://지원.freshdesk.com/지원/solutions/articles/50000000119-localize-your-feedback-forms-with-multilingual-고객-satisfaction-surveys) for detailed information.

</details>

<details>
<summary><strong>The CSAT survey emails are not being translated. What am I missing?</strong></summary>

The CSAT survey 이메일 might not have been translated in the preferred language if any one of the following is true.**1.  **The language associated with the contact seems to be incorrect. The 고객’s preferred language is auto-detected by Freshdesk and saved in contact details based on their first interaction. This can be changed under **Contact > Edit Contact**.2. The survey will be sent in the default language if the translations for the 고객's preferred** language is not uploaded or available** in Freshdesk.3. The **‘secondary languages’** in your 헬프데스크 should be marked as **‘Visible in 포털’** for the surveys to be automatically translated to the corresponding languages

</details>

<details>
<summary><strong>My 고객 is not receiving the survey 이메일 in the correct language. How to fix this?</strong></summary>

The language in which the 이메일 notifications are being sent to the 고객 depends on the language that the particular contact has been associated with.Navigate to the profile of the contact under 연락처 tab > Edit Contact and change the language of the contact to the preferred language.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001150171/original/tML2KJ191fHCxcU8-a7FM9v9zdd6PkrOcg.png?1590496005)

</details>

<details>
<summary><strong>send a satisfaction survey for 티켓 that came through Facebook할 수 있나요?</strong></summary>

Satisfaction surveys would be triggered through 이메일 notification. When a social ticket is created, we just fetch the 사용자명 of the user. So ideally, there is no direct option to send a CSAT survey for social 티켓.
But you could integrate any third party tool and attach a survey link manually.

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
