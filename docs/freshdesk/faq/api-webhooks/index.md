---
sidebar_position: 1
---

# API 및 웹훅 FAQ

API 및 웹훅에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>What are Webhooks? 는 무엇인가요?</strong></summary>

Webhook is callback 로 application 또는 web service is triggered when specific event occurs. means you 할 수 있습니다 set up Webhook 로 look 위해 specific 업데이트하다, 변경하다 또는 작업 로 occur 에서 your Helpdesk 및 it 할 것입니다 automatically push information you specify 로 application you want. 에서 simple words, two applications communicate using Webhooks. Webhooks 할 수 있습니다 triggered via automation rules run 에서 ticket creation 및 rules run 에서 ticket updates 에서 Freshdesk.

</details>

<details>
<summary><strong>How do I 생성하다 app? 는 무엇인가요?</strong></summary>

로 get information about creating different apps 에서 Freshdesk you 할 수 있습니다 refer 로 this documentation: [https://developers. freshdesk. com/v2/docs/quick-start/](https://developers. freshdesk. com/v2/docs/quick-start/)

</details>

<details>
<summary><strong>할 수 있습니다 I find my API key? ?</strong></summary>

**Note:**If your account is 에서 **Sprout** plan, API key 및 API functionality 할 것입니다 NOT be 사용 가능. API key is unique alphanumeric identifier, 위해 each agent 에서 your Freshdesk Account. Irrespective 의 version 의 **Freshdesk's APIs** you use, you 할 것입니다 need 로 provide either your username 및 password combination 또는 your API key 위해 authorization when making API calls 에 의해 triggering webhooks. Here's how you 할 수 있습니다 retrieve your API key: - Login 로 your Freshdesk Account - 클릭하다 your 프로필 picture icon 에서 top right corner 및 선택하다 **프로필 설정**! [이미지](https://s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/43123696/original/zF3n_DLVhON3Bsp8O71jLHmkLl9gs1WFew. png? 1548399480) - 에서 right pane, you 할 것입니다 find **API Key** - Copy-paste this as 필수 로 authenticate third-party solutions 다음을 확인하십시오: you are administrator/account administrator 로 perform helpdesk 활동 using API. Keep 에서 mind API keys 위해 admin/account admin are based 에서 역할 capabilities. 위해 example, account admin API is 필수 로 설치하다 app 에서 marketplace 또는 위해 any integration, while admin's API 할 수 있습니다 used 위해 any ticketing-related 활동. If you encounter any issues finding your API key 하위에서 your 프로필, kindly log 에서 로 your helpdesk 에서 different browser 또는 clear cache 또는 cookies 에서 your existing browser. Then, log 에서 if needed 및 navigate through your 프로필 설정 로 find your API key.

</details>

<details>
<summary><strong>할 수 있습니다 I 추가하다 images 로 solution articles using API? ?</strong></summary>

Yes, you 할 수 있습니다 추가하다 inline images 로 your solution articles using API. Refer 로 sample code given below :\{"description":"Test Article *이미지: Smiley face*", "status":2, "title":"Solutions API", "type":1\} Note: 다음을 확인하십시오: image 해야 합니다 be hosted 에서 public location.

</details>

<details>
<summary><strong>Is there any documentation 위해 APIs 에서 Freshdesk? 는 무엇인가요?</strong></summary>

Please visit [http://developer. freshdesk. com/api](http://developer. freshdesk. com/api) 위해 API documentation.

</details>

<details>
<summary><strong>What are rate limits 위해 API calls 로 Freshdesk? 는 무엇인가요?</strong></summary>

**Note:**per-minute rate limiting is being rolled out 에서 batches. number 의 API calls you 할 수 있습니다 make is based 에서 your plan. This limit is applied 로 your account irrespective 의 number 의 agents you have 또는 IP addresses used 로 make calls. We're currently moving 모든 Freshdesk accounts 에서 per-hour limit 로 per-minute limit. 에서 this article, we'll give you details 에서 both. **Call limits per minute** **Plan****Calls per minute** **Maximum limit per endpoint** Free00Growth200Ticket 생성하다 - 80Ticket 업데이트하다 - 80Tickets List - 20Contacts List - 20Pro400Ticket 생성하다 - 160Ticket 업데이트하다 - 160Tickets List - 100Contacts List - 100Enterprise700Ticket 생성하다 - 280Ticket 업데이트하다 - 280Tickets List - 200Contacts List - 200 위해 더 details, visit our [developer portal](https://developers. freshdesk. com/api/). If you are looking 로 increase your API limit, 또는 move 로 per-minute limiting, please drop email 로 support@freshdesk. com 함께 details 에서 your use-case 및 we'll help you sort this out. **** **Please note: 위해 every trial period API limit is 50 per minute. **

</details>

<details>
<summary><strong>할 수 있습니다 I 추가하다 customer satisfaction survey 위해 ticket using API? ?</strong></summary>

Yes, here is API documentation 위해 creating Satisfaction Survey: [https://developer. freshdesk. com/api/#create_satisfaction_rating](https://developer. freshdesk. com/api/#create_satisfaction_rating). endpoint api/v2/tickets/[ticket_id]/satisfaction_ratings is one 위해 creating satisfaction rating using APIs.

</details>

<details>
<summary><strong>What webhooks 할 것입니다 contribute 로 my rate limit? 는 무엇인가요?</strong></summary>

Any webhook you have set up 에서 your Freshdesk - be it 에서 automation rule, 또는 external webhooks ( like Zapier 또는 TimeCamp) - 할 것입니다 contribute towards adding 로 API calls resulting 에서 meeting 함께 your rate limits.

</details>

<details>
<summary><strong>How 로 생성하다 contact using API? 는 무엇인가요?</strong></summary>

Refer this [연결](https://developer. freshdesk. com/api/#create_contact) 로 get detailed information 에서 creating contact using API.

</details>

<details>
<summary><strong>How 로 편집하다 subject line 의 tickets based 에서 certain conditions 또는 specific keyword 에서 subject? 는 무엇인가요?</strong></summary>

This 할 수 있습니다 done using API. 이동하다 **Admin > Workflow > Automations > Ticket Creation > New Rule** 및 set up automation rule as follows: **Condition:**Description contains ". . . . . . . . . . . " **작업:**Trigger webhook! [이미지](https://s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50001067860/original/sHUR6bJSwyf2TAO-2XJZ-ly3VGO0HOFrEQ. png? 1588840658) Kindly refer 로 this[연결](https://developers. freshdesk. com/api/#update_ticket) 위해 더 information 에서 updating ticket details via API. Copy code accordingly 위해 changing subject.

</details>

<details>
<summary><strong>How do I apply filters 및 보다 list 의 tickets using API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 보다 tickets 에서 custom ticket list 보다, using API. You 할 수 있습니다 make use 의 v1 의 API 로 have this done. Please refer 로 this [documentation](https://freshdesk. com/api#view_all_ticket) 위해 detailed information 에서 same.

</details>

<details>
<summary><strong>How 로 생성하다 ticket 함께 dependent field using API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use **생성하다 ticket 함께 custom fields** commands via API as given 에서 this [연결](https://developer. freshdesk. com/api/#create_ticket) 로 생성하다 ticket 함께 dependent field using API.

</details>

<details>
<summary><strong>Is there API 로 list 모든 tickets 및 schedule it 위해 particular time? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 list 모든 tickets 에서 periodic basis. API documentation 될 것입니다 사용 가능 에서 [http://developer. freshdesk. com/api/#list_all_tickets](http://developer. freshdesk. com/api/#list_all_tickets). **Note:** automated script has 로 be run 에서 your end 로 run this API call 에서 ***specified time interval. ***

</details>

<details>
<summary><strong>How 할 수 있습니다 I 보다 Ticket Properties 의 ticket using API? ?</strong></summary>

You 할 수 있습니다 use API 로 "보다 Ticket" 및 as part 의 response, you 될 것입니다 able 로 receive Tag added 로 ticket. **Command** **:** Get **Callback U****R****L :**/api/v2/tickets/[id] **Sample Curl :**curl -v -u username:password -H "Content-Type: application/json" -X GET '[https://domain. freshdesk. com/api/v2/tickets/20](https://domain. freshdesk. com/api/v2/tickets/20)'

</details>

<details>
<summary><strong>How 로 제거하다 quoted text via API? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use this command below 로 제거하다 quoted text through API: client. interface. trigger("클릭하다", \{id: "delete_quoted_text"\})

</details>

<details>
<summary><strong>할 수 있습니다 I use my vanity URL 또는 CNAME 로 make API call? ?</strong></summary>

As 의 now, V2 의 Freshdesk's API supports 만 Freshdesk URL 에서 HTTPs. Making calls using vanity URL isn't supported.

</details>

<details>
<summary><strong>Do we have API 및 integration capabilities 에서 free Sprout plan? 는 무엇인가요?</strong></summary>

No, 접근 로 Freshdesk APIs 및 integration capabilities is not 사용 가능 에서 free Sprout plan. It 될 것입니다 **사용 가능 에서 Blossom plan onwards. ** Please refer [here](https://freshdesk. com/helpdesk-기능) 위해 detailed 기능 comparison chart.

</details>

<details>
<summary><strong>How do I get list 의 agent ID's? 는 무엇인가요?</strong></summary>

You 할 수 있습니다 use our API 로 get list 의 모든 agents 할 것입니다 include Agent's IDs as well. 로 know 더 about same you 할 수 있습니다 make use 의 [https://developers. freshdesk. com/api/#list_all_agents](https://developers. freshdesk. com/api/#list_all_agents)

</details>

<details>
<summary><strong>Why have I received email saying 'Please recheck webhook 설정 에서 your account'? 는 무엇인가요?</strong></summary>

This is notification email is auto-generated when Webhook is triggered 에서 your account fails. This Webhook 할 수 있습니다 be part 의 automations 또는 에서 your server. When you set-up webhooks, you 할 것입니다 have entered incorrect URL 또는 content 에서 script 위해 webhooks 할 수 있습니다 be incorrect. Please confirm you have entered right URL 위해 those webhooks 및 확인하다 if rules are set correctly.

</details>

<details>
<summary><strong>How 로 handle 및 prevent webhook drops? 는 무엇인가요?</strong></summary>

Webhook is callback 로 application 또는 web service triggered when specific event occurs. 에서 case 의 particular 업데이트하다, 변경하다, 또는 작업 에서 your helpdesk, you 할 수 있습니다 set up Webhook 로 automatically push specific information 로 application through Freshdesk automations - ticket creation 및 ticket 업데이트하다 rules. You 할 수 있습니다 configure as 많은 Webhooks 위해 event triggers as you want 하지만 execute them 만 based 에서 [API rate limit](https://developer. freshdesk. com/api/#ratelimit) 위해 your account. Any webhooks beyond limit 될 것입니다 postponed 로 next hour if you schedule 더 than assigned call rate. If system postpones webhook 에서 execution 위해 더 than 24 hours, Freshdesk drops webhook 및 sends following alert email 로 helpdesk admin.! [이미지](https://s3. amazonaws. com/cdn. freshdesk. com/data/helpdesk/attachments/production/50006747944/original/p3DNq-mnBj1zVIbx0Sn1w_qlKw9-92mXEg. png? 1666789883) 또한, 확인하다 로 set-up webhooks 함께 correct URL 및 follow proper syntax 위해 webhook content 로 avoid webhook failures during execution. Please reach out 로 [support@freshdesk. com](mailto:support@freshdesk. com) 로 learn 더 about 설정 up webhooks 위해 your business use-case 더 efficiently 및 avoid failures 에 의해 keeping them within API rate limit.

</details>

<details>
<summary><strong>List 모든 tickets 함께 conversations using API는 무엇인가요?</strong></summary>

You 할 수 있습니다 use API [https://developers. freshdesk. com/api/#list_all_ticket_notes](https://developers. freshdesk. com/api/#list_all_ticket_notes) 로 list 모든 conversations 의 ticket. You 할 수 있습니다 make use 의 script 로 fetch conversations 의 모든 tickets as 필수. 로 know tickets 에서 there are multiple conversations you 할 수 있습니다 take export 의 tickets 에서 list 보다 page. 선택하다 parameter 'Customer interaction' 및 if this is 더 than 1 it means customer has replied 로 ticket after creating it.

</details>

<details>
<summary><strong>How 할 수 있습니다 I prevent webhook 에서 being dropped? ?</strong></summary>

webhook 될 것입니다 dropped 만 if it exceeds permitted API rate limit 의 your Freshdesk Account. Please write 로 support@freshdesk. com 함께 details regarding webhook 및 use-case 위해 you had set it up. One 의 our agents 할 것입니다 get 에서 contact 함께 you 로 discuss 에서 making this 더 efficient 위해 you, after you 할 수 있습니다 trigger webhooks 및 keep it within rate limit.

</details>

<details>
<summary><strong>Status codes 및 its reasons는 무엇인가요?</strong></summary>

에서 Freshdesk, error codes 할 수 있습니다 appear during various interactions 및 processes, indicating specific issues 또는 anomalies need attention. Understanding these error codes 및 their reasons 할 수 있습니다 help diagnose 및 resolve underlying problems efficiently. Below are 일부 common error codes encountered 에서 Freshdesk 및 reasons they 할 수 있습니다 occur: HTTP STATUS CODETEXTDESCRIPTION200 OK request was successful, 및 server responded 함께 requested data. 201 Created request was successful, 및 new resource was created. 204 No Content request was successful, 하지만 there is no content 로 send 에서 response. 400Client 또는 Validation ErrorThe request body/query string is not 에서 correct format. 위해 example, [생성하다 ticket](http://developer. freshdesk. com/api/#create_ticket) API requires **requester_id** field 로 be sent as part 의 request 및 if it is missing, this status code is returned. 401Authentication FailureIndicates **Authorization** header is either missing 또는 incorrect. You 할 수 있습니다 learn 더 about Authorization header [here. ](http://developer. freshdesk. com/api/#authentication)403Access DeniedThis indicates agent whose credentials were used 에서 making this request was not authorized 로 perform this API call. It 할 수 있습니다 this API call requires admin level credentials 또는 perhaps Freshdesk portal doesn't have corresponding 기능 활성화됨. It 할 수 있습니다 또한 indicate user has reached maximum number 의 failed login attempts 또는 account has reached maximum number 의 agents404Requested Resource not FoundThis status code is returned when request contains invalid ID/Freshdesk domain 에서 URL 또는 invalid URL itself. 위해 example, API call 로 retrieve ticket 함께 invalid ID 할 것입니다 return HTTP 404 status code 로 let you know no such ticket exists. 405Method not allowedThis API request used wrong HTTP verb/method. 위해 example, API PUT request 에서 /api/v2/tickets endpoint 할 것입니다 return HTTP 405 as /api/v2/tickets allows 만 GET 및 POST requests. 406Unsupported Accept HeaderOnly **application/json** 및 ***/*** are supported. When uploading files multipart/form-data is supported. 409Inconsistent/Conflicting StateThe resource is being created/updated is 에서 inconsistent 또는 conflicting state. 위해 example, if you attempt 로 [생성하다 Contact](http://developer. freshdesk. com/api/#create_user) 함께 email is 이미 associated 함께 existing user, this code 될 것입니다 returned. 415Unsupported Content-typeContent type **application/xml** is not supported. 만 **application/json** is supported. 429Rate Limit ExceededThe API rate limit allotted 위해 your Freshdesk domain has been exhausted. 500Unexpected Server ErrorPhew! ! You 할 수 있습니다't do anything 더 here. This indicates error 에서 Freshdesk's side. Please [support@freshdesk. com](mailto:support@freshdesk. com) your API script along 함께 response headers. We 할 것입니다 reach you out 로 you 및 fix this ASAP. 502Bad Gateway server, while acting as gateway 또는 proxy, received invalid response 에서 upstream server. 503 Service Unavailable server is not ready 로 handle request, possibly due 로 maintenance 또는 overload. 504 Gateway Timeout server, while acting as gateway 또는 proxy, did not receive timely response 에서 upstream server.

</details>

<details>
<summary><strong>do I find documentation 위해 API? 는 무엇인가요?</strong></summary>

Freshdesk API documentation 할 수 있습니다 found 하위에서 - [https://developers. freshdesk. com/api](https://developers. freshdesk. com/api). Using information 사용 가능 here, you 될 것입니다 able 로 build your own account specific API based 에서 your business requirements.

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
