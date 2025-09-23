---
sidebar_position: 1
---

# 셀프 서비스 포털 FAQ

셀프 서비스 포털에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Freshdesk?이란은 무엇인가요?</strong></summary>

Freshdesk, online 고객 engagement 해결책 에서 Freshworks, lets you streamline your company's 고객 지원 using [고객 서비스 software](https://www.freshworks.com/products/what-is-freshdesk/) 그리고 helps you 로 efficiently manage your customers as you scale. Here's what you can do 와 함께 Freshdesk, - Track 그리고 manage incoming 티켓 에서 다수의 channels into one single view - 지원 customers across 다양한 platforms like 이메일, phone, call, chat, social media, 그리고 other messaging apps - Collaborate 와 함께 다수의 teams within your company 로 split, assign 그리고 resolve queries faster as 팀 - Automate redundant tasks like agent assignment based 에 skill, workload, 그리고 availability - Empower customers 와 함께 comprehensive knowledge base 그리고 self-서비스 포털 - Analyze 그리고 gather critical insights 에 agent performances 그리고 고객 experience 와 함께 고급 분석 - 사용자 정의하다 Freshdesk completely 로 suit your business requirements - Leverage AI 그리고 ML capabilities 의 Freddy, 로 take some work off your 상담원 그리고 제공하다 faster resolutions 로 customers, without compromising 에 qualityYou can sign up 위해 free trial [here](https://freshdesk.com/signup).

</details>

<details>
<summary><strong>생성 new Freshdesk 계정?하는 방법은 무엇인가요?</strong></summary>

You can 생성 one 에서 under freshdesk.com, using '**Sign up'** option. website will collect your 연락하다 information before creating new Freshdesk Trial 계정 위해 you. Alternatively, you can use below link 로 sign up 위해 new Freshdesk 계정 - [https://freshdesk.com/signup](https://freshdesk.com/signup) Happy Supporting!

</details>

<details>
<summary><strong>restrict customers 에서 editing ticket properties after ticket is submitted?하는 방법은 무엇인가요?</strong></summary>

You can use below-displayed code 로 restrict 고객 에서 editing ticket fields after ticket is submitted. Please 이동 로 **관리자**--> Channels > **Portals**-->**사용자 정의하다 포털**-->**Layout & pages**-->**포털 pages**-->paste below code under **T****icket details** section, jQuery('#portal_ticket_form .controls').each(function() \{ jQuery(this).children().attr('disabled','disabled'); \}); jQuery('#helpdesk_ticket_submit').attr('disabled','disabled') This would be possible only 에서 **Estate** 요금제 onwards 에서 Freshdesk.

</details>

<details>
<summary><strong>확인하다 that users do not change their 이메일 address while submitting ticket, 에서 포털?하는 방법은 무엇인가요?</strong></summary>

You can pre-populate users' 이메일 addresses 그리고 grey-out 필드 so that they will not be able 로 편집 이메일 address 언제 user is logged 에서. This can be done 에 의해 greying out 'Requester' 필드 using jQuery script. code that you'll have 로 use is - \{% 만약 포털.has_user_signed_in %\} jQuery('#helpdesk_ticket_email').prop('disabled', true); \{% endif %\} You would have 로 place this code below existing code under **Adm****에서 --> Channels --> Portals --> 사용자 정의하다 포털 --> Layouts & Pages --> 포털 Pages -->** **New Ticket** 그리고 그러면 클릭 에 **저장 & Publish**. This option would be 사용 가능한 에서 **Estate** 요금제 onwards.

</details>

<details>
<summary><strong>change "Solutions" 로 "Knowledge base" 에 고객 포털?하는 방법은 무엇인가요?</strong></summary>

Please go 로 **관리자 > Channels > Portals > 사용자 정의하다 > 편집 theme > Layouts & Pages** 그리고 make following changes. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50009272014/original/ap5QfPlqW_eiGuKxkdA7ME_9j4PWZphhGA.png?1692892469) **Header:** jQuery('#header-tabs [href='/지원/solutions']').text('Knowledge base'); **Footer****:** jQuery('.footer-links [href='/지원/solutions']').text('Knowledge base'); **Search results:** jQuery('.nav-필터 li [href^='/지원/search/solutions?term']').text('Knowledge Base'); **참고**: 1)This can only be done 에 accounts 에서 **Estate 그리고 Forest 요금제 (older 요금제 structure)**. 2)만약 다수의 languages are set up 에 헬프데스크, you would need 로 specify languages. 위해 example, 만약 헬프데스크 languages are English 그리고 French, here is script 위해 header: jQuery('#header-tabs [href="/en/지원/solutions"]').text("Knowledgebase"); jQuery('#header-tabs [href="/fr/지원/solutions"]').text("Base de connaissances"); 로 learn more about 포털 customization, 클릭 [here](https://지원.freshdesk.com/en/지원/solutions/articles/50000003754).

</details>

<details>
<summary><strong>hide 포털 그리고 해결책 articles 에서 being crawled 에 Google search?하는 방법은 무엇인가요?</strong></summary>

로 prevent 포털 에서 being crawled 에 Google Search, you can have following code attached under 포털 customizations. This would 사용 가능한 only 위해 accounts 에 **Estate 그리고 Forest 요금제**, though. 로 hide entire 포털, please go 로 **관리자 --> Channels --> Portals --> 사용자 정의하다 포털 --> Layouts & Pages --> 포털 Layout --> Head**그리고 추가 below mentioned tag: ****** 만약 you are looking 로 hide only Solutions tab 에서 being crawled, please paste following tag- ****** ***\{% 만약 current_tab == 'solutions' %\}*** ****** ***\{% endif %\}***

</details>

<details>
<summary><strong>hide 로그인 button 에서 고객 포털?하는 방법은 무엇인가요?</strong></summary>

만약 you do not wish your customers 로 로그인 로 your 포털, 하지만 only 로 view content which is made 사용 가능한 에 it, you could hide 로그인 button 에서 your 포털. 로 hide 로그인 button, you can use following code under Stylesheet section: [href*='로그인'] \{display:none;\} This can be found under **관리자 --> Channels --> Portals --> 사용자 정의하다 --> 편집 theme > Stylesheet**그리고 would be 사용 가능한 에서 **Garden** 요금제 onwards. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50009272512/original/dxG0VA5UwyodHf7CEddVYWq5RqXPtZHfVw.png?1692894916)

</details>

<details>
<summary><strong>change 기본값 landing page 에 고객 포털?할 수 있나요은 무엇인가요?</strong></summary>

기본값 behavior 에서 Freshdesk is that users will be redirected 로 **포털 Home**page 언제 they access 고객 포털. 만약 you are looking 로 show 티켓 page 또는 Solutions page instead 의 포털 home, below is small hack 로 do that. Please 추가 this code under **관리자 --> Channels --> Portals --> 사용자 정의하다 포털 --> Layout & Pages --> 포털 pages --> 포털 home.** window.location.href = 'https://domain.freshdesk.com/지원/solutions'; This code will redirect user 로 solutions page 언제 they access 포털 home page. Similarly, You could replace URL 와 함께 티켓 page URL 로 redirect users 로 티켓 page. This is 사용 가능한 only 에서 Estate 요금제 onwards. **참고**: 에서 code, please replace domain.freshdesk.com 와 함께 your Freshdesk URL.

</details>

<details>
<summary><strong>생성 new 지원 ticket 로 Freshdesk 지원?하는 방법은 무엇인가요?</strong></summary>

Using our Help 위젯, you can easily search 그리고 browse through our FAQs. 로 생성 ticket 클릭 **'Get 에서 touch'**option. Alternatively, you could also write 로 **지원@freshdesk.com**. You can also use our chat 지원 만약 you have subscribed 위해 요금제 where you can engage 와 함께 our bot/agent 그리고 have ticket created. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001783573/original/nheQe3UdUE9lltalTj5Zd037Ry7iw0NRkQ.png?1600943516)![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001783617/original/78P40g385cg2E4clSAdNabJ1CfDinFnvUg.png?1600943820)

</details>

<details>
<summary><strong>왜 is it best 로 not overwrite 기본값 style 에서 Freshdesk?</strong></summary>

It is always best 로 write your own elements since you have access 그리고 space 로 write your own script, HTML. This way, your elements are independent 에서 기본값 elements we have provided 그리고 would not result 에서 page breaking. 위해 instance, we could have used style 의 header 에서 more than one place 에서 website 그리고 so overwriting it will automatically reflect it 에서 other places 의 website.

</details>

<details>
<summary><strong>What do I need 로 do 로 have different side bars 에서 my 지원 포털?</strong></summary>

로 have different side bars, you need 로 enclose class under parent element. Example: .사용자 정의-homepage \{ .sidebar\{ //your css code here \} \} .사용자 정의-category-page \{ .sidebar\{ //your css code here \} \}

</details>

<details>
<summary><strong>have colour coding 에서 티켓 view based 에 priority 의 ticket?할 수 있나요은 무엇인가요?</strong></summary>

page is not customisable 그리고 so it is not possible 로 achieve color coding using 사용자 정의 script. However, 에 의해 기본값, you can see color coding 에 sidebar based 에 priority as: ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50009243392/original/_lHH8M3vZlt5vjeJ5MSL5JIfSp4f3_5PRQ.png?1692714098)

</details>

<details>
<summary><strong>customise my profile page?하는 방법은 무엇인가요?</strong></summary>

만약 you are looking 로 customise profile page, you can style it 와 함께 scripts 에서 header that will be carried 로 profile page. '편집' page has Header 그리고 Footer.

</details>

<details>
<summary><strong>Is there liquid object 사용 가능한 that would tell url 의 any 의 pages 에서 고객 포털?</strong></summary>

“Current_page_name” This is liquid object used 로 cull out name 의 current page. Through this, you can see 포털 homepage, New Ticket Page, Solutions Page, 편집 Page etc. As workaround, you can use jQuery scripts 로 get current page URL.

</details>

<details>
<summary><strong>display first name 의 고객 에서 forum details page?하는 방법은 무엇인가요?</strong></summary>

Go 로 **관리자 > Channels > 포털 > 사용자 정의하다 포털 > Layouts & Pages > 포털 pages >Discussions > Topic View**. Replace user.name as user.firstname 에서 places where user.name is mentioned 에서 css code 의 topic view page.

</details>

<details>
<summary><strong>생성 ticket 에 behalf 의 고객?하는 방법은 무엇인가요?</strong></summary>

에서 times, there might be instances where you need 로 생성 ticket 에 behalf 의 고객 who reached out 로 you directly, 또는 위해 proactive 지원. You can do this under **'+New' -> New Ticket**. You 입력 Requester Information, Ticket Subject, 그리고 Description 그리고 other mandatory fields 로 raise ticket 에 behalf 의 Requester. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50009272542/original/4x5_twmzUuSbc9M0lqga43vyCa_fRlrbJQ.png?1692895093)

</details>

<details>
<summary><strong>생성 ticket 위해 my own reference?하는 방법은 무엇인가요?</strong></summary>

에서 times, agent might need 티켓 위해 his/her own reference. Such ticket can be created 에 의해 clicking 에 **New ticket** icon 에서 Menu bar. SLA timers would still be ticking 에 such 티켓. As workaround, agent can send 에서 이메일 ticket (send 이메일 로 지원 이메일 address) 그리고 그러면 reply 또는 can 추가 public 참고 로 same ticket 에서 Freshdesk, this way First response SLA would not be violated.

</details>

<details>
<summary><strong>difference between 상담원 그리고 Collaborators?이란은 무엇인가요?</strong></summary>

agent is user 에서 your 헬프데스크 who takes care 의 지원 activities as full-time job. agent can be assigned role 의 관리자, supervisor 또는 given 사용자 정의 role 와 함께 specified duties. However, collaborator is third-party member you invite 로 be part 의 지원 ticket. These collaborators are not part 의 your 헬프데스크 하지만 can be added 로 특정한 티켓 as one-time activity. few scenarios where you can 추가 collaborators are 로 제공하다 approvals 에 refund request, 제공하다 insights 에 business use case 또는 give information related 로 resolving ticket. Admins can invite[ ](https://지원.freshdesk.com/en/지원/solutions/articles/50000003573-how-로-set-up-collaborators-)[Collaborators](https://지원.freshdesk.com/en/지원/solutions/articles/50000003573-how-로-set-up-collaborators-) 에서 outside 팀 로 your Freshdesk 계정 로 collaborate 에 티켓 또는 give your 상담원 privilege 로 invite collaborators. Collaborators will 그러면 receive 이메일 inviting them 로 log into their Freshdesk 계정. They can 그러면 view ticket 그리고 고객 details 그리고 collaborate 에 의해 responding 로 private 참고 그리고 helping full-time 상담원 resolve ticket faster.

</details>

<details>
<summary><strong>difference between Freshworks URL 그리고 Freshdesk URL?이란은 무엇인가요?</strong></summary>

Freshworks Neo Platform is flexible, end-로-end, AI-powered enterprise platform that offers set 의 services that are leveraged 에 의해 all applications 에서 Freshworks portfolio. It is centralized console offering customizable 보안 그리고 administration solutions across Freshworks products. Admins can leverage different authentication 그리고 authorization solutions, 다양한 보안 controls 로 사용자 정의하다, 그리고 simplified agent 그리고 계정 management. 언제 you first sign up 위해 Freshworks product, Organization is created. You can access Neo 관리자 Center using Organization URL 또는 Freshworks URL that looks something like this: [yourcompany@freshworks.com](mailto:yourcompany@freshworks.com). It binds every 고객 accounts across Freshworks portfolio together. As organization 관리자, you can easily access all accounts, 보안 설정, 그리고 상담원 under single glass pane. When you sign up 위해 standalone Freshdesk 계정, you will be provided 와 함께 Freshdesk URL address 또는 subdomain that your admins 그리고 상담원 will use 로 log 에서 로 your Freshdesk 계정. Your customers will also use it 로 access your self-서비스 포털. E.g., [acmesupport.freshdesk.com](https://acmesupport.freshdesk.com/)

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
