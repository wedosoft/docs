---
sidebar_position: 1
---

# 연동 및 통합 FAQ

연동 및 통합에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>추가 Apps 로 my Freshdesk 계정?하는 방법은 무엇인가요?</strong></summary>

You can 추가 apps 로 your Freshdesk 계정 에서 Freshdesk Apps Gallery. Based 에 app's complexity 그리고 availability 의 its features, it is either free 또는 comes 와 함께 charge. 로 install app, - Go 로 **관리자**>**지원 Operations**>**Apps** >**Marketplace** - Search 위해 app you wish 로 추가 그리고 클릭 **Install.** - Under **설정,**configure your **Freshdesk** **Domain URL**그리고 **API Key.** **![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50007628783/original/pMz9X4pdeCCFrZ4wyYlta7V3-IvIf9FvVQ.png?1676533180)** Your Freshdesk URL will be 에서 format .freshdesk.com](//yourcompanyname.freshdesk.com). You can fetch URL 에서 your address bar. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50007628830/original/CcsUKVd840Usk8roJ8IU6ULrLWSrl5myjQ.png?1676533556) 로 fetch your API Key, Go 로 **Profile icon**>**Profile 설정** >**Your API Key** **![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50007629119/original/6bq626_T7G56iz8v-gHm89_whV5YUSki2g.png?1676535429)**

</details>

<details>
<summary><strong>왜 is it that comment 에서 JIRA is added 에서 Freshdesk under different 사용자명?</strong></summary>

언제 user posts comment 에서 JIRA, equivalent 계정 is created 에서 Freshdesk 와 함께 one's JIRA 이메일 그리고 참고 is added 로 Freshdesk ticket. 만약 이메일 address 의 user is **hidden** 에서 JIRA 설정, JIRA 연동 에서 your 헬프데스크 will not be able 로 fetch it, 그리고 so generic one will be used.

</details>

<details>
<summary><strong>왜 is ticket created 에서 Freshdesk whenever comment is added 에서 JIRA?</strong></summary>

This usually happens 언제 you configure notifications 에서 JIRA 그리고 it is linked 로 one 의 지원 addresses configured 에서 Freshdesk. You can just 제거 지원 이메일 address 에서 **notification 설정**within JIRA 로 prevent this.

</details>

<details>
<summary><strong>왜 isn't status mapping 에서 JIRA working 위해 me?</strong></summary>

로 understand 왜 status mapping 에서 JIRA is not working, 1. 이동 로 **관리자 -> 지원 Operations -> Apps -> JIRA Plus app 설정 -> 일반적인 설정** 로 확인하다 how status sync between JIRA 그리고 Freshdesk is 설정. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001119719/original/wgC0wmSBYKHKKy14EF0Y2DXHM7Xc2bW7Sg.png?1589863092) 2. Also, 확인하다 how your 사용자 정의 statuses 에 Freshdesk is mapped 로 문제 status 에 Jira ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001119735/original/KiZtcKRsdYB9Qju8c9TNDMTn3Pzm7gqo-g.png?1589863423)

</details>

<details>
<summary><strong>attach files which are larger than 20 MB?하는 방법은 무엇인가요?</strong></summary>

Freshdesk has many 3rd party integrations like Dropbox 또는 OneDrive 와 함께 which 상담원/customers can use 로 send files larger than 20 MB. 로 set up integrations 와 함께 Google Drive, refer 로 [this article](https://지원.freshdesk.com/해결책/articles/232355--google-drive-app) 그리고 위해 Dropbox, you can 클릭 [here](https://지원.freshdesk.com/지원/solutions/articles/55359--dropbox-app).

</details>

<details>
<summary><strong>왜 aren't messages being pushed 로 Slack?</strong></summary>

Please 확인하다 만약 corresponding channel is configured under **관리자 -> 지원 Operations -> Apps -> Slack -> 편집.** 만약 channel has been**deleted**, messages will not be pushed 로 Slack channel.

</details>

<details>
<summary><strong>avoid entire HTML code that comes out 언제 comment section is included 에서 message sent 로 Slack?하는 방법은 무엇인가요?</strong></summary>

언제 you are using dynamic variables 로 configure 사용자 정의 messages 위해 Slack, please use following variables 위해**ticket description, last public 참고, 그리고 last private 참고** so that only text content 의 description 그리고 notes is sent 로 Slack. Otherwise, **HTML** tags will get pushed 로 slack as well. You can replace placeholder 와 함께 **\{\{ticket.description_text\}\} 또는 \{\{ticket.description | strip_html\}\} instead 의 \{\{ticket.description\}\}** 그리고 this will just have text portion included 에서 notification.

</details>

<details>
<summary><strong>왜 am I unable 로 execute Slash Commands?</strong></summary>

Please 확인하다 following 에서 Slack app: 1. Make sure **"****Allow Slash Commands"**is checked 에서 app 구성 page. Please 이동 로 **관리자 -> 지원 Operations -> Apps ->** 클릭 에 slash 연동 로 see 설정 (gear icon) where you could see this 구성. 2. Make sure that **correct Slash command token** (obtainable 언제 you 생성 slash command) is copied 로 Freshdesk-Slack app 설정 page. 3. Make sure **** entered along 와 함께 /fd_ticket command is right one.

</details>

<details>
<summary><strong>Do we have any limit 로 number 의 Public 그리고 Private channels?</strong></summary>

Yes, 연동 allows only **20 private 그리고 public channels**. 의 these, 에서 least one channel should be 사용 가능한 as Public (independent 의 private channels).

</details>

<details>
<summary><strong>hide certain ticket fields 로 certain 상담원?할 수 있나요은 무엇인가요?</strong></summary>

You can integrate Freshdesk 와 함께 app called 'Hide/비활성화 Ticket Fields'. 언제 there are several irrelevant 기본값 그리고 사용자 정의 Ticket fields it is time-consuming 위해 agent 로 scroll through these fields while creating/updating ticket. All Ticket fields except mandatory fields will be 사용 가능한 로 Hide 그리고/또는 비활성화. - Ability 로 display 티켓 fields 관련된 로 상담원 - Useful 언제 ticket 필드 is used 로 hold background information that is 의 no relevance 의 value 로 agent - Reduce unnecessary clutter 에 상담원’ interface - Improve 상담원’ productivity Refer this [link](https://apps.freshdesk.com/hidedisable_ticket_fields/) 위해 more details.

</details>

<details>
<summary><strong>왜 is only part 의 conversation 에서 Slack being converted into ticket 에서 Freshdesk?</strong></summary>

As per 연동, latest **200 messages** would only be included 에서 text 의 ticket. **text content** only 에서 conversations will be included 에서 ticket. All files attached 그리고 snippets will be 사용 가능한 as clickable Slack link 에서 your ticket.

</details>

<details>
<summary><strong>use dynamic variables 언제 setting up user-defined Slack messages?할 수 있나요은 무엇인가요?</strong></summary>

Yes, this is possible- however, please use following variables 위해 ticket description, last public 참고, 그리고 last private 참고 so that only text content 의 description 그리고 notes is sent 로 Slack; otherwise, **HTML tags**will get pushed 로 slack as well. - Use \{\{ticket.description_text\}\} 에서 place 의 \{\{ticket.description\} - Use \{\{ticket.latest_public_comment_text\}\} 에서 place 의 \{\{ticket.latest_public_comment\}\} - Use \{\{ticket.latest_private_comment_text\}\} 에서 place 의 \{\{ticket.latest_private_comment\}\}

</details>

<details>
<summary><strong>I want 로 know what customers are viewing 에서 website?</strong></summary>

와 함께 Freshmarketer 연동, you can now view 고객 sessions 에 every ticket generated 에서 Freshdesk. session replay is recording 의 고객’s journey 에 website 또는 within web application. Benefits 의 this Session replay 연동: - Get context about 문제 that 고객 has been facing, without having 로 ask them 로 elaborate 문제. 위해 e.g. 만약 고객 has been facing trouble 와 함께 routing emails, you can look 에서 session replay 그리고 understand what went wrong. - Lesser 이메일 threads leading 로 decrease 에서 resolution time. - Understand which part 의 your website/product is confusing 로 고객. - Reduces need 로 ask customers 위해 screenshots. Instead replay sessions. - Identify 해결책 articles visited 에 의해 고객 로 make sure that 지원 agent does not suggest same. Please refer this [link](https://지원.freshdesk.com/지원/solutions/articles/235353-how-로-integrate-freshmarketer-s-session-replay-와 함께-freshdesk-) 위해 more details.

</details>

<details>
<summary><strong>I typed my auth token incorrectly while calling “/fd_ticket” - what do?할 수 있나요은 무엇인가요?</strong></summary>

You may call **slash command** again 와 함께 correct token, 그리고 app will override previously-stored incorrect one. Please 이동 로 **관리자 -> 지원 Operations -> Apps -> Slack** where this could be checked 그리고 modified.

</details>

<details>
<summary><strong>왜 am I getting failure message 에서 time 의 ticket creation, 그리고 being asked 로 연락하다 지원@freshdesk.com?</strong></summary>

This could happen due 로 following reasons: - ticket **format 또는 description** is incorrect. - Ticket creation is done without **mandatory** fields (priority, source etc). - Slack is not able 로 process certain details 로 Freshdesk.

</details>

<details>
<summary><strong>생성 mailing lists 언제 writing emails?할 수 있나요은 무엇인가요?</strong></summary>

You cannot 생성 mailing lists 에서 Freshdesk. However, you can make use 의 Mailchimp 연동 와 함께 Freshdesk 로 생성 mailing lists 에서 Mailchimp 그리고 로 send out emails 에서 bulk. Please refer this[link](https://지원.freshdesk.com/지원/solutions/articles/41745--mailchimp-app)위해 more details about Mailchimp.

</details>

<details>
<summary><strong>Where is Mailchimp 위젯 located please?</strong></summary>

Please 이동 로 **"apps.freshdesk.com"** 그리고 search 위해 MailChimp 로 install this. Kindly make sure you have MailChimp 계정 로 integrate 와 함께 Freshdesk. Once this is successfully added 로 your 헬프데스크, **MailChimp 위젯**would be 사용 가능한 inside 연락처 under customers' tab. 위해 instance, you 클릭 에 that 위젯 inside 연락하다 say, Alex - window 와 함께 two tabs namely,**campaigns 그리고 mailing lists** would open 와 함께 several options underneath that would allow you 로 선택 which 로 subscribe 그리고 unsubscribe appropriately.

</details>

<details>
<summary><strong>I do not have e-commerce option even though I am 에서 Estate 요금제. Please help me 와 함께 this!은 무엇인가요?</strong></summary>

E-commerce is recently developed platform 에 Freshdesk which would 활성화 you 로 bring Ebay channel into 헬프데스크. This is feature enabled upon request 그리고 so kindly 연락하다 us 에**지원@freshdesk.com** 에서 order 로 bring this as option 에 관리자 tab. Once this is enabled, you could see this 에서 **관리자 -> Channels -> E-commerce** where you can 추가 new 계정. This new 계정 would need your eBay site information 그리고 you would be able 로 assign product, group 그리고 such.

</details>

<details>
<summary><strong>integrate Xero 와 함께 Freshdesk?하는 방법은 무엇인가요?</strong></summary>

Xero is **Invoicing Tool**which you could integrate 와 함께 Freshdesk. Using this 연동, you would be able 로 view information about invoices sent 로 requester 의 ticket, within that **ticket's details page**. You could **track time 위해 티켓**에서 Freshdesk 그리고 **send invoices**위해 지원, using Xero 연동. You could integrate Xero 와 함께 your Freshdesk 계정, 에 의해 navigating 로 **관리자 -> Su -> Apps -> Get More Apps-->Time Tracking & 결제-->Xero-->Install**. You would be asked 로 로그인 로 your Xero 계정 로 authorize 연동.

</details>

<details>
<summary><strong>SugarCRM? integrate 와 함께 my SugarCRM 계정?하는 방법이란은 무엇인가요?</strong></summary>

SugarCRM is 고객 Relationship Management tool, which is used 로 track 그리고 keep record 의 your 고객 profiles. 로 제공하다 better context 의 고객 information 로 상담원 working 에 your Freshdesk 계정, you could integrate SugarCRM 와 함께 Freshdesk. 로 integrate SugarCRM, 이동 로 **관리자 > 지원 Operations > Apps > Get More Apps > CRM > SugarCRM > Install**. This would install app 에 your 계정. You could 그러면 configure app 에 의해 entering SugarCRM 계정 URL 그리고 credentials.

</details>

<details>
<summary><strong>integrate Zoho CRM 와 함께 Freshdesk?하는 방법은 무엇인가요?</strong></summary>

Zoho CRM is web-based 고객 relationship management application that has native 연동 에서 Freshdesk. This 연동 would allow you 로 fetch requester information 에서 this tool which is 사용 가능한 에서 연락하다 details as well as 티켓 detail page. Please 이동 로 **관리자 -> 지원 Operations -> Apps -> Get more apps -> 선택 로 install Zoho CRM.** 연동 will ask 위해 Auth Token which can be taken 에서 your Zoho CRM 계정. 위해 more information, please 이동 로 this [link](https://지원.freshdesk.com/지원/solutions/articles/42657--zoho-crm-app) 로 set this up.

</details>

<details>
<summary><strong>integrate Freshdesk 와 함께 my Shopify store?하는 방법은 무엇인가요?</strong></summary>

에서 times, you would want 로 integrate your 헬프데스크 와 함께 Shopify so that you can bring your customers' details into 헬프데스크. 이동 로 **관리자 > 지원 Operations > Apps > Get more apps** 그리고 search 위해 Shopify. 위해 further instructions 에 설치 그리고 app's capabilities, please refer [this](https://지원.freshdesk.com/지원/solutions/articles/195382--shopify-app) article.

</details>

<details>
<summary><strong>convert WordPress comments 로 Freshdesk 티켓?하는 방법은 무엇인가요?</strong></summary>

You can 생성 티켓 위해 comments 에 your WordPress website using Freshdesk plugin 위해 WordPress. You can 생성 ticket 위해 every comment user writes 에 your WordPress site users 로 log 에서 로 Freshdesk. 로 do so, you first need 로 install [Freshdesk WordPress plugin](https://wordpress.org/plugins/freshdesk-지원/). You can install plugin 에서 plugins directory 만약 your site runs 에 self-hosted WordPress. 만약 you use WordPress.com, you need 로 be 에 [Business 요금제 또는 above](https://wordpress.com/pricing/) 로 install this plugin. [클릭 here](https://지원.freshdesk.com/지원/solutions/articles/50000001054-converting-wordpress-comments-로-freshdesk-티켓) 로 read step-에 의해-step guide 에 embedding 해결책 articles 그리고 연락하다 form 에 Shopify 에서 more detail.

</details>

<details>
<summary><strong>기본적인 Freshdesk - Freshcaller 연동?이란은 무엇인가요?</strong></summary>

기본적인 Freshdesk - Freshcaller 연동 helps you convert calls you manage within your Freshcaller 계정 as 티켓 에서 Freshdesk. You can follow-up 에 your calls, i.e, 제공하다 post-call 지원 via Freshdesk 그리고 also document them 위해 future context.

</details>

<details>
<summary><strong>고급 Freshdesk - Freshcaller 연동이란은 무엇인가요?</strong></summary>

Apart 에서 attending your calls, providing post-call 지원 에 의해 converting calls into 티켓 within Freshdesk, 고급 Freshdesk - Freshcaller 연동 also helps you **manage your calls within your Freshdesk 계정**without having 로 switch tabs 로 go 로 your Freshcaller 계정.

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
