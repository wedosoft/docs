---
sidebar_position: 1
---

# API 및 웹훅 FAQ

API 및 웹훅에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>웹훅이란 무엇인가요?</strong></summary>

웹훅은 특정 이벤트가 발생할 때 트리거되는 애플리케이션 또는 웹 서비스에 대한 콜백입니다. means you 할 수 있습니다 set up 웹훅 로 look 위해 특정 업데이트, change 또는 action 로 occur 에서 your Helpdesk 및 it 할 것입니다 automatically push information you specify 로 애플리케이션 you want. 간단히 말해서, 두 애플리케이션이 웹훅을 사용하여 통신합니다. 웹훅 될 수 있습니다 트리거됨 via automation 규칙 run 에서 ticket creation 및 규칙 run 에서 ticket updates 에서 Freshdesk.

</details>

<details>
<summary><strong>앱을 생성하는 방법은 무엇인가요?</strong></summary>

Freshdesk에서 다양한 앱 생성에 대한 정보를 얻으려면 다음 문서를 참조하십시오: [https: //developers. freshdesk. com/v2/docs/빠른-start/](https: //developers. freshdesk. com/v2/docs/빠른-start/)

</details>

<details>
<summary><strong>API 키는 어디서 찾을 수 있나요?</strong></summary>

**Note: **If your account is 에서 **Sprout** plan, API 키 및 API 기능 할 것입니다 NOT be 사용 가능. API 키 is unique 영숫자 식별자, 위해 각 agent 에서 your Freshdesk Account. Irrespective 의 버전 의 **Freshdesk's API** you use, you 할 것입니다 해야 합니다 provide either your 사용자명 및 비밀번호 combination 또는 your API 키 위해 인증 making API 호출 에 의해 triggering 웹훅. API 키를 검색하는 방법은 다음과 같습니다: - Freshdesk 계정에 로그인하십시오 - Click 에서 your 프로필 사진 icon 에서 top right corner 및 select **프로필 설정**! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/43123696/original/zF3n_DLVhON3Bsp8O71jLHmkLl9gs1WFew. png? 1548399480) - 에서 right pane, you 할 것입니다 find **API 키** - 서드파티 솔루션을 인증하는 데 필요에 따라 이를 복사하여 붙여넣으십시오 Please 보장하다 you are administrator/account administrator 로 perform helpdesk 활동 using API. 다음 사항을 기억하십시오: API 키 위해 admin/account admin are based 에서 role capabilities. 위해 example, account admin API is 필수 로 설치 app 에서 마켓플레이스 또는 위해 any 통합, while admin's API 될 수 있습니다 used 위해 any ticketing-related 활동. If you encounter any issues finding your API 키 하위에서 your profile, kindly log 에서 로 your helpdesk 에서 다른 브라우저 또는 clear 캐시 또는 쿠키 에서 your existing 브라우저. Then, log 에서 if needed 및 navigate 통해 your 프로필 설정 로 find your API 키.

</details>

<details>
<summary><strong>API를 사용하여 솔루션 문서에 이미지를 추가할 수 있나요?</strong></summary>

네, API를 사용하여 솔루션 문서에 인라인 이미지를 추가할 수 있습니다. Refer 로 샘플 코드 given 아래에: \{"description": "Test Article *이미지: Smiley face*", "status": 2, "title": "Solutions API", "type": 1\} Note: Please 보장하다 image 되어야 합니다 hosted 에서 공개 위치.

</details>

<details>
<summary><strong>Freshdesk의 API에 대한 문서가 있나요?</strong></summary>

Please visit [http: //developer. freshdesk. com/API](http: //developer. freshdesk. com/API) 위해 API 문서.

</details>

<details>
<summary><strong>Freshdesk API 호출의 속도 제한은 무엇인가요?</strong></summary>

**Note: **per-minute rate limiting is being rolled out 에서 batches. number 의 API 호출 you 할 수 있습니다 make is based 에서 your plan. This limit is applied 로 your account irrespective 의 number 의 agents you have 또는 IP addresses 사용되었습니다 make calls. We're currently moving 모든 Freshdesk accounts 에서 per-hour limit 로 per-minute limit. 에서 this article, we'll give you details 에서 both. **Call limits per minute** **Plan****Calls per minute** **Maximum limit per endpoint** Free00Growth200Ticket 생성하다 - 80Ticket 업데이트 - 80Tickets List - 20Contacts List - 20Pro400Ticket 생성하다 - 160Ticket 업데이트 - 160Tickets List - 100Contacts List - 100Enterprise700Ticket 생성하다 - 280Ticket 업데이트 - 280Tickets List - 200Contacts List - 200 위해 더 details, visit our [developer portal](https: //developers. freshdesk. com/API/). If you are looking 로 increase your API limit, 또는 move 로 per-minute limiting, please drop email 로 support@freshdesk. com 함께 details 에서 your use-case 및 we'll help you sort this out. **** **Please note: 위해 모든 trial period API limit is 50 per minute. **

</details>

<details>
<summary><strong>API를 사용하여 티켓에 고객 만족도 설문조사를 추가할 수 있나요?</strong></summary>

Yes, here is API 문서 위해 creating Satisfaction Survey: [https: //developer. freshdesk. com/API/#create_satisfaction_rating](https: //developer. freshdesk. com/API/#create_satisfaction_rating). endpoint API/v2/tickets/[ticket_id]/satisfaction_ratings is one 위해 creating satisfaction rating using API.

</details>

<details>
<summary><strong>어떤 웹훅이 속도 제한에 영향을 주나요?</strong></summary>

Any 웹훅 you have set up 에서 your Freshdesk - be it 에서 automation rule, 또는 external 웹훅 ( like Zapier 또는 TimeCamp) - 할 것입니다 contribute towards adding 로 API 호출 resulting 에서 meeting 함께 your rate limits.

</details>

<details>
<summary><strong>API를 사용하여 연락처를 생성하는 방법은 무엇인가요?</strong></summary>

Refer this [link](https: //developer. freshdesk. com/API/#create_contact) 로 get detailed information 에서 creating contact using API.

</details>

<details>
<summary><strong>How 로 edit subject line 의 tickets based 에서 certain conditions 또는 특정 keyword 에서 subject? 는 무엇인가요?</strong></summary>

This 될 수 있습니다 done using API. Navigate 로 **Admin > Workflow > Automations > Ticket Creation > 새로운 Rule** 및 set up automation rule as follows: **Condition: **Description contains ". . . . . . . . . . . " **Action: **트리거 웹훅! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50001067860/original/sHUR6bJSwyf2TAO-2XJZ-ly3VGO0HOFrEQ. png? 1588840658) Kindly refer 로 this[link](https: //developers. freshdesk. com/API/#update_ticket) 위해 더 information 에서 updating ticket details via API. Copy code accordingly 위해 changing subject.

</details>

<details>
<summary><strong>How do I apply filters 및 view list 의 tickets using API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 view tickets 에서 custom ticket list view, using API. You 할 수 있습니다 make use 의 v1 의 API 로 have this done. Please refer 로 this [문서](https: //freshdesk. com/API#view_all_ticket) 위해 detailed information 에서 같은.

</details>

<details>
<summary><strong>How 로 생성하다 ticket 함께 dependent field using API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use **생성하다 ticket 함께 custom fields** commands via API as given 에서 this [link](https: //developer. freshdesk. com/API/#create_ticket) 로 생성하다 ticket 함께 dependent field using API.

</details>

<details>
<summary><strong>Is there API 로 list 모든 tickets 및 schedule it 위해 특정 time? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 list 모든 tickets 에서 periodic basis. API 문서 될 것입니다 사용 가능 에서 [http: //developer. freshdesk. com/API/#list_all_tickets](http: //developer. freshdesk. com/API/#list_all_tickets). **Note: ** automated script has 로 be run 에서 your end 로 run this API 호출 에서 ***specified time interval. ***

</details>

<details>
<summary><strong>How 할 수 있습니다 I view Ticket Properties 의 ticket using API? ?</strong></summary>

You 할 수 있습니다 use API 로 "View Ticket" 및 as part 의 response, you 할 수 있을 것입니다 receive Tag added 로 ticket. **Command** **: ** Get **콜백 U****R****L: **/API/v2/tickets/[id] **Sample Curl: **curl -v -u 사용자명: 비밀번호 -H "Content-Type: 애플리케이션/json" -X GET '[https: //domain. freshdesk. com/API/v2/tickets/20](https: //domain. freshdesk. com/API/v2/tickets/20)'

</details>

<details>
<summary><strong>How 로 remove quoted text via API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use this command 아래에 로 remove quoted text 통해 API: client. interface. 트리거("click", \{id: "delete_quoted_text"\})

</details>

<details>
<summary><strong>할 수 있습니다 I use my vanity URL 또는 CNAME 로 make API 호출? ?</strong></summary>

As 의 now, V2 의 Freshdesk's API supports 만 Freshdesk URL 에서 HTTPs. Making calls using vanity URL isn't supported.

</details>

<details>
<summary><strong>Do we have API 및 통합 capabilities 에서 free Sprout plan? 는 무엇인가요?</strong></summary>

No, access 로 Freshdesk API 및 통합 capabilities is not 사용 가능 에서 free Sprout plan. It 될 것입니다 **사용 가능 에서 Blossom plan onwards. ** Please refer [here](https: //freshdesk. com/helpdesk-기능) 위해 detailed 기능 comparison chart.

</details>

<details>
<summary><strong>How do I get list 의 agent ID's? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use our API 로 get list 의 모든 agents 할 것입니다 include Agent's IDs as well. 로 know 더 about 같은 you 할 수 있습니다 make use 의 [https: //developers. freshdesk. com/API/#list_all_agents](https: //developers. freshdesk. com/API/#list_all_agents)

</details>

<details>
<summary><strong>Why have I received email saying 'Please recheck 웹훅 settings 에서 your account'? 는 무엇인가요?</strong></summary>

This is notification email that is auto-generated 웹훅 which is 트리거됨 에서 your account fails. This 웹훅 될 수 있습니다 part 의 automations 또는 에서 your server. you set-up 웹훅, you 할 것입니다 have entered incorrect URL 또는 content 에서 script 위해 웹훅 될 수 있습니다 incorrect. Please 확인하다 you have entered right URL 위해 those 웹훅 및 확인하다 if 규칙 are set correctly.

</details>

<details>
<summary><strong>How 로 handle 및 prevent 웹훅 drops? 는 무엇인가요?</strong></summary>

웹훅 is 콜백 로 애플리케이션 또는 웹 서비스 트리거됨 특정 이벤트 occurs. 에서 case 의 특정 업데이트, change, 또는 action 에서 your helpdesk, you 할 수 있습니다 set up 웹훅 로 automatically push 특정 information 로 애플리케이션 통해 Freshdesk automations - ticket creation 및 ticket 업데이트 규칙. You 할 수 있습니다 구성하다 as 많은 웹훅 위해 이벤트 triggers as you want 하지만 execute them 만 based 에서 [API rate limit](https: //developer. freshdesk. com/API/#ratelimit) 위해 your account. Any 웹훅 beyond limit 될 것입니다 postponed 로 next hour if you schedule 더 than assigned call rate. If system postpones 웹훅 에서 execution 위해 더 than 24 hours, Freshdesk drops 웹훅 및 sends following alert email 로 helpdesk admin.! [이미지](https: //s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50006747944/original/p3DNq-mnBj1zVIbx0Sn1w_qlKw9-92mXEg. png? 1666789883) 또한, 보장하다 로 set-up 웹훅 함께 correct URL 및 follow proper syntax 위해 웹훅 content 로 avoid 웹훅 failures during execution. Please reach out 로 [support@freshdesk. com](mailto: support@freshdesk. com) 로 learn 더 about setting up 웹훅 위해 your business use-case 더 efficiently 및 avoid failures 에 의해 keeping them within API rate limit.

</details>

<details>
<summary><strong>List 모든 tickets 함께 conversations using API는 무엇인가요?</strong></summary>

You 할 수 있습니다 use API [https: //developers. freshdesk. com/API/#list_all_ticket_notes](https: //developers. freshdesk. com/API/#list_all_ticket_notes) 로 list 모든 conversations 의 ticket. You 할 수 있습니다 make use 의 script 로 fetch conversations 의 모든 tickets as 필수. 로 know tickets 에서 there are multiple conversations you 할 수 있습니다 take export 의 tickets 에서 list view page. Choose parameter 'Customer interaction' 및 if this is 더 than 1 it means customer has replied 로 ticket after creating it.

</details>

<details>
<summary><strong>How 할 수 있습니다 I prevent 웹훅 에서 being dropped? ?</strong></summary>

웹훅 될 것입니다 dropped 만 if it exceeds permitted API rate limit 의 your Freshdesk Account. Please write 로 support@freshdesk. com 함께 details regarding 웹훅 및 use-case 위해 you had set it up. One 의 our agents 할 것입니다 get 에서 contact 함께 you 로 discuss 에서 making this 더 efficient 위해 you, after you 할 수 있습니다 트리거 웹훅 및 keep it within rate limit.

</details>

<details>
<summary><strong>Status codes 및 its reasons는 무엇인가요?</strong></summary>

에서 Freshdesk, error codes 할 수 있습니다 appear during various interactions 및 processes, indicating 특정 issues 또는 anomalies need attention. Understanding these error codes 및 their reasons 할 수 있습니다 help diagnose 및 해결하다 underlying problems efficiently. 아래에 are 일부 일반적인 error codes encountered 에서 Freshdesk 및 reasons they 할 수 있습니다 occur: HTTP STATUS CODETEXTDESCRIPTION200 OK request was successful, 및 server responded 함께 requested data. 201 Created request was successful, 및 새로운 resource was created. 204 No Content request was successful, 하지만 there is no content 로 send 에서 response. 400Client 또는 Validation ErrorThe request body/query string is not 에서 correct format. 위해 example, [생성하다 ticket](http: //developer. freshdesk. com/API/#create_ticket) API requires **requester_id** field 로 be sent as part 의 request 및 if it is missing, this status code is returned. 401Authentication FailureIndicates **인증** header is either missing 또는 incorrect. You 할 수 있습니다 learn 더 about 인증 header [here. ](http: //developer. freshdesk. com/API/#인증)403Access DeniedThis indicates agent whose credentials were used 에서 making this request was not authorized 로 perform this API 호출. It 될 수 있습니다 this API 호출 requires admin level credentials 또는 perhaps Freshdesk portal doesn't have corresponding 기능 enabled. It 할 수 있습니다 또한 indicate user has reached maximum number 의 failed login attempts 또는 account has reached maximum number 의 agents404Requested Resource not FoundThis status code is returned request contains invalid ID/Freshdesk domain 에서 URL 또는 invalid URL itself. 위해 example, API 호출 로 검색하다 ticket 함께 invalid ID 할 것입니다 return HTTP 404 status code 로 let you know no 그러한 ticket exists. 405Method not allowedThis API request used wrong HTTP verb/method. 위해 example, API PUT request 에서 /API/v2/tickets endpoint 할 것입니다 return HTTP 405 as /API/v2/tickets allows 만 GET 및 POST requests. 406Unsupported Accept HeaderOnly **애플리케이션/json** 및 ***/*** are supported. uploading files multipart/form-data is supported. 409Inconsistent/Conflicting StateThe resource that is being created/updated is 에서 inconsistent 또는 conflicting state. 위해 example, if you attempt 로 [생성하다 Contact](http: //developer. freshdesk. com/API/#create_user) 함께 email that is 이미 associated 함께 existing user, this code 될 것입니다 returned. 415Unsupported Content-typeContent type **애플리케이션/xml** is not supported. 만 **애플리케이션/json** is supported. 429Rate Limit ExceededThe API rate limit allotted 위해 your Freshdesk domain has been exhausted. 500Unexpected Server ErrorPhew! ! You 할 수 있습니다't do anything 더 here. This indicates error 에서 Freshdesk's side. Please [support@freshdesk. com](mailto: support@freshdesk. com) your API script along 함께 response headers. We 할 것입니다 reach you out 로 you 및 fix this ASAP. 502Bad Gateway server, while acting as gateway 또는 proxy, received invalid response 에서 upstream server. 503 Service Unavailable server is not ready 로 handle request, possibly due 로 maintenance 또는 overload. 504 Gateway Timeout server, while acting as gateway 또는 proxy, did not receive timely response 에서 upstream server.

</details>

<details>
<summary><strong>do I find 문서 위해 API? 는 무엇인가요?</strong></summary>

Freshdesk API 문서 될 수 있습니다 found 하위에서 - [https: //developers. freshdesk. com/API](https: //developers. freshdesk. com/API). Using information 사용 가능 here, you 할 수 있을 것입니다 구축하다 your own account 특정 API based 에서 your business requirements.

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
