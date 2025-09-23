---
sidebar_position: 1
---

# API 및 웹훅 FAQ

API 및 웹훅에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Webhooks?이란은 무엇인가요?</strong></summary>

웹훅 is callback 로 application 또는 web 서비스 that is triggered 언제 특정한 event occurs. That means you can set up 웹훅 로 look 위해 특정한 업데이트, change 또는 action 로 occur 에서 your 헬프데스크 그리고 it will automatically push information you specify 로 application you want. 에서 simple words, two applications communicate using Webhooks.Webhooks can be triggered via automation rules that run 에 ticket creation 그리고 rules that run 에 ticket updates 에서 Freshdesk.

</details>

<details>
<summary><strong>생성 app?하는 방법은 무엇인가요?</strong></summary>

로 get information about creating different apps 에서 Freshdesk you can refer 로 this documentation: [https://developers.freshdesk.com/v2/docs/quick-start/](https://developers.freshdesk.com/v2/docs/quick-start/)

</details>

<details>
<summary><strong>find my API key?는 어디서은 무엇인가요?</strong></summary>

**참고:**만약 your 계정 is 에 **Sprout** 요금제, API key 그리고 API functionality will NOT be 사용 가능한. API key is unique alphanumeric identifier, 위해 each agent 에 your Freshdesk 계정. Irrespective 의 which version 의 **Freshdesk's APIs** you use, you will need 로 제공하다 either your 사용자명 그리고 비밀번호 combination 또는 your API key 위해 authorization 언제 making API calls 에 의해 triggering webhooks. Here's how you can retrieve your API key: - 로그인 로 your Freshdesk 계정 - 클릭 에 your profile picture icon 에 top right corner 그리고 선택 **Profile 설정** ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/43123696/original/zF3n_DLVhON3Bsp8O71jLHmkLl9gs1WFew.png?1548399480) - 에 right pane, you will find **API Key** - Copy-paste this as 필수 로 authenticate third-party solutions Please 확인하다 that you are 관리자/계정 관리자 로 perform 헬프데스크 activities using API. Keep 에서 mind that API keys 위해 관리자/계정 관리자 are based 에 role capabilities. 위해 example, 계정 관리자 API is 필수 로 install app 에서 marketplace 또는 위해 any 연동, while 관리자's API can be used 위해 any ticketing-related activities. 만약 you encounter any issues finding your API key under your profile, kindly log 에서 로 your 헬프데스크 에서 different browser 또는 clear cache 또는 cookies 에서 your existing browser. 그러면, log 에서 만약 needed 그리고 이동 through your profile 설정 로 find your API key.

</details>

<details>
<summary><strong>추가 images 로 해결책 articles using API?할 수 있나요은 무엇인가요?</strong></summary>

Yes, you can 추가 inline images 로 your 해결책 articles using API. Refer 로 sample code given below :\{"description":"Test Article *이미지: Smiley face*","status":2,"title":"Solutions API","입력":1\} 참고: Please 확인하다 that image should be hosted 에서 public location.

</details>

<details>
<summary><strong>Is there any documentation 위해 APIs 에 Freshdesk?</strong></summary>

Please visit [http://developer.freshdesk.com/API](http://developer.freshdesk.com/API) 위해 API documentation.

</details>

<details>
<summary><strong>rate limits 위해 API calls 로 Freshdesk?이란은 무엇인가요?</strong></summary>

**참고: ** per-minute rate limiting is being rolled out 에서 batches. number 의 API calls you can make is based 에 your 요금제. This limit is applied 로 your 계정 irrespective 의 number 의 상담원 you have 또는 IP addresses used 로 make calls. We're currently moving all Freshdesk accounts 에서 per-hour limit 로 per-minute limit. 에서 this article, we'll give you details 에 both. **Call limits per minute** **요금제****Calls per minute** **Maximum limit per endpoint** Free00Growth200Ticket 생성 - 80Ticket 업데이트 - 80Tickets List - 20Contacts List - 20Pro400Ticket 생성 - 160Ticket 업데이트 - 160Tickets List - 100Contacts List - 100Enterprise700Ticket 생성 - 280Ticket 업데이트 - 280Tickets List - 200Contacts List - 200 위해 more details, visit our [developer 포털](https://developers.freshdesk.com/API/). 만약 you are looking 로 increase your API limit, 또는 move 로 per-minute limiting, please drop 이메일 로 지원@freshdesk.com 와 함께 details 에 your use-case 그리고 we'll help you sort this out. **** **Please 참고: 위해 every trial period API limit is 50 per minute.**

</details>

<details>
<summary><strong>추가 고객 satisfaction survey 위해 ticket using API?할 수 있나요은 무엇인가요?</strong></summary>

Yes, here is API documentation 위해 creating Satisfaction Survey: [https://developer.freshdesk.com/API/#create_satisfaction_rating](https://developer.freshdesk.com/API/#create_satisfaction_rating). endpoint API/v2/티켓/[ticket_id]/satisfaction_ratings is one 위해 creating satisfaction rating using APIs.

</details>

<details>
<summary><strong>What webhooks will contribute 로 my rate limit?</strong></summary>

Any 웹훅 you have set up 에 your Freshdesk - be it 에서 automation rule, 또는 external webhooks ( like Zapier 또는 TimeCamp) - will contribute towards adding 로 API calls resulting 에서 meeting 와 함께 your rate limits.

</details>

<details>
<summary><strong>생성 연락하다 using API?하는 방법은 무엇인가요?</strong></summary>

Refer this [link](https://developer.freshdesk.com/API/#create_contact) 로 get detailed information 에 creating 연락하다 using API.

</details>

<details>
<summary><strong>편집 subject line 의 티켓 based 에 certain conditions 또는 특정한 keyword 에서 subject?하는 방법은 무엇인가요?</strong></summary>

This can be done using API. 이동 로 **관리자 > Workflow > Automations > Ticket Creation > New Rule** 그리고 set up automation rule as follows: **Condition:**Description contains "..........." **Action:**Trigger 웹훅 ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001067860/original/sHUR6bJSwyf2TAO-2XJZ-ly3VGO0HOFrEQ.png?1588840658) Kindly refer 로 this[link](https://developers.freshdesk.com/API/#update_ticket) 위해 more information 에 updating ticket details via API. Copy code accordingly 위해 changing subject.

</details>

<details>
<summary><strong>apply filters 그리고 view list 의 티켓 using API?하는 방법은 무엇인가요?</strong></summary>

You can view 티켓 에서 사용자 정의 ticket list view, using API. You could make use 의 v1 의 API 로 have this done. Please refer 로 this [documentation](https://freshdesk.com/API#view_all_ticket) 위해 detailed information 에 same.

</details>

<details>
<summary><strong>생성 ticket 와 함께 dependent 필드 using API?하는 방법은 무엇인가요?</strong></summary>

You can use **생성 ticket 와 함께 사용자 정의 fields** commands via API as given 에서 this [link](https://developer.freshdesk.com/API/#create_ticket) 로 생성 ticket 와 함께 dependent 필드 using API.

</details>

<details>
<summary><strong>Is there API 로 list all 티켓 그리고 schedule it 위해 particular time?</strong></summary>

You could list all 티켓 에 periodic basis. API documentation would be 사용 가능한 에서 [http://developer.freshdesk.com/API/#list_all_tickets](http://developer.freshdesk.com/API/#list_all_tickets). **참고:** automated script has 로 be run 에서 your end 로 run this API call 에서 ***specified time interval.***

</details>

<details>
<summary><strong>view Ticket Properties 의 ticket using API?하는 방법은 무엇인가요?</strong></summary>

You could use API 로 "View Ticket" 그리고 as part 의 response, you would be able 로 receive Tag added 로 ticket. **Command** **:** Get **Callback U****R****L :**/API/v2/티켓/[id] **Sample Curl :**curl -v -u 사용자명:비밀번호 -H "Content-입력: application/json" -X GET '[https://domain.freshdesk.com/API/v2/티켓/20](https://domain.freshdesk.com/API/v2/티켓/20)'

</details>

<details>
<summary><strong>제거 quoted text via API?하는 방법은 무엇인가요?</strong></summary>

You can use this command below 로 제거 quoted text through API: client.interface.trigger("클릭", \{id: "delete_quoted_text"\})

</details>

<details>
<summary><strong>use my vanity URL 또는 CNAME 로 make API call?할 수 있나요은 무엇인가요?</strong></summary>

As 의 now, V2 의 Freshdesk's API supports only Freshdesk URL 에 HTTPs. Making calls using vanity URL isn't supported.

</details>

<details>
<summary><strong>Do we have API 그리고 연동 capabilities 에서 free Sprout 요금제?</strong></summary>

No, access 로 Freshdesk APIs 그리고 연동 capabilities is not 사용 가능한 에서 free Sprout 요금제. It will be **사용 가능한 에서 Blossom 요금제 onwards.** Please refer [here](https://freshdesk.com/헬프데스크-features) 위해 detailed feature comparison 차트.

</details>

<details>
<summary><strong>get list 의 agent ID's?하는 방법은 무엇인가요?</strong></summary>

You can use our API 로 get list 의 all 상담원 which would include Agent's IDs as well. 로 know more about same you can make use 의 [https://developers.freshdesk.com/API/#list_all_agents](https://developers.freshdesk.com/API/#list_all_agents)

</details>

<details>
<summary><strong>왜 have I received 이메일 saying 'Please recheck 웹훅 설정 에서 your 계정'?</strong></summary>

This is notification 이메일 that is auto-generated 언제 웹훅 which is triggered 에서 your 계정 fails. This 웹훅 might be part 의 automations 또는 에서 your server. 언제 you set-up webhooks, you would have entered incorrect URL 또는 content 에서 script 위해 webhooks might be incorrect. Please confirm that you have entered right URL 위해 those webhooks 그리고 확인하다 만약 rules are set correctly.

</details>

<details>
<summary><strong>handle 그리고 prevent 웹훅 drops?하는 방법은 무엇인가요?</strong></summary>

웹훅 is callback 로 application 또는 web 서비스 triggered 언제 특정한 event occurs. 에서 case 의 particular 업데이트, change, 또는 action 에서 your 헬프데스크, you can set up 웹훅 로 automatically push 특정한 information 로 application through Freshdesk automations - ticket creation 그리고 ticket 업데이트 rules. You can configure as many Webhooks 위해 event triggers as you want 하지만 execute them only based 에 [API rate limit](https://developer.freshdesk.com/API/#ratelimit) 위해 your 계정. Any webhooks beyond that limit will be postponed 로 next hour 만약 you schedule more than assigned call rate. 만약 system postpones 웹훅 에서 execution 위해 more than 24 hours, Freshdesk drops 웹훅 그리고 sends following alert 이메일 로 헬프데스크 관리자. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50006747944/original/p3DNq-mnBj1zVIbx0Sn1w_qlKw9-92mXEg.png?1666789883) Also, 확인하다 로 set-up webhooks 와 함께 correct URL 그리고 follow proper syntax 위해 웹훅 content 로 avoid 웹훅 failures during execution. Please 문의하다 로 [지원@freshdesk.com](mailto:지원@freshdesk.com) 로 learn more about setting up webhooks 위해 your business use-case more efficiently 그리고 avoid failures 에 의해 keeping them within API rate limit.

</details>

<details>
<summary><strong>List all 티켓 와 함께 conversations using API은 무엇인가요?</strong></summary>

You can use API [https://developers.freshdesk.com/API/#list_all_ticket_notes](https://developers.freshdesk.com/API/#list_all_ticket_notes) 로 list all conversations 의 ticket. You can make use 의 script 로 fetch conversations 의 all 티켓 as 필수. 로 know 티켓 에서 which there are 다수의 conversations you can take 내보내기 의 티켓 에서 list view page. 선택 parameter '고객 interaction' 그리고 만약 this is more than 1 it means 고객 has replied 로 ticket after creating it.

</details>

<details>
<summary><strong>prevent 웹훅 에서 being dropped?하는 방법은 무엇인가요?</strong></summary>

웹훅 would be dropped only 만약 it exceeds permitted API rate limit 의 your Freshdesk 계정. Please write 로 지원@freshdesk.com 와 함께 details regarding 웹훅 그리고 use-case 위해 which you had set it up. One 의 our 상담원 would get 에서 연락하다 와 함께 you 로 discuss 에 making this more efficient 위해 you, after which you could trigger webhooks 그리고 keep it within rate limit.

</details>

<details>
<summary><strong>Status codes 그리고 its reasons은 무엇인가요?</strong></summary>

에서 Freshdesk, 오류 codes may appear during 다양한 interactions 그리고 processes, indicating 특정한 issues 또는 anomalies that need attention. Understanding these 오류 codes 그리고 their reasons can help diagnose 그리고 resolve underlying problems efficiently. Below are some 일반적인 오류 codes encountered 에서 Freshdesk 그리고 reasons they may occur: HTTP STATUS CODETEXTDESCRIPTION200 OK request was successful, 그리고 server responded 와 함께 requested 데이터. 201 Created request was successful, 그리고 new resource was created. 204 No Content request was successful, 하지만 there is no content 로 send 에서 response. 400Client 또는 Validation ErrorThe request body/query string is not 에서 correct format. 위해 example, [생성 ticket](http://developer.freshdesk.com/API/#create_ticket) API requires **requester_id** 필드 로 be sent as part 의 request 그리고 만약 it is missing, this status code is returned.401Authentication FailureIndicates that **Authorization** header is either missing 또는 incorrect. You can learn more about Authorization header [here.](http://developer.freshdesk.com/API/#authentication)403Access DeniedThis indicates that agent whose credentials were used 에서 making this request was not authorized 로 perform this API call. It could be that this API call requires 관리자 level credentials 또는 perhaps Freshdesk 포털 doesn't have corresponding feature enabled. It could also indicate that user has reached maximum number 의 failed 로그인 attempts 또는 that 계정 has reached maximum number 의 agents404Requested Resource not FoundThis status code is returned 언제 request contains invalid ID/Freshdesk domain 에서 URL 또는 invalid URL itself. 위해 example, API call 로 retrieve ticket 와 함께 invalid ID will return HTTP 404 status code 로 let you know that no such ticket exists.405Method not allowedThis API request used wrong HTTP verb/method. 위해 example, API PUT request 에 /API/v2/티켓 endpoint will return HTTP 405 as /API/v2/티켓 allows only GET 그리고 POST requests.406Unsupported Accept HeaderOnly **application/json** 그리고 ***/*** are supported.When uploading files multipart/form-데이터 is supported.409Inconsistent/Conflicting StateThe resource that is being created/updated is 에서 inconsistent 또는 conflicting state. 위해 example, 만약 you attempt 로 [생성 연락하다](http://developer.freshdesk.com/API/#create_user) 와 함께 이메일 that is already associated 와 함께 existing user, this code will be returned.415Unsupported Content-typeContent 입력 **application/xml** is not supported. Only **application/json** is supported.429Rate Limit ExceededThe API rate limit allotted 위해 your Freshdesk domain has been exhausted.500Unexpected Server ErrorPhew!! You can't do anything more here. This indicates 오류 에서 Freshdesk's side. Please [이메일 us](mailto:지원@freshdesk.com) your API script along 와 함께 response headers. We will reach you out 로 you 그리고 fix this ASAP.502Bad Gateway server, while acting as gateway 또는 proxy, received invalid response 에서 upstream server. 503 서비스 Unavailable server is not ready 로 handle request, possibly due 로 maintenance 또는 overload. 504 Gateway Timeout server, while acting as gateway 또는 proxy, did not receive timely response 에서 upstream server.

</details>

<details>
<summary><strong>Where do I find documentation 위해 API?</strong></summary>

Freshdesk API documentation could be found under - [https://developers.freshdesk.com/API](https://developers.freshdesk.com/API). Using information 사용 가능한 here, you would be able 로 build your own 계정 특정한 API based 에 your business requirements.

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
