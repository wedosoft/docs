---
sidebar_position: 1
---

# API 및 웹훅 FAQ

API 및 웹훅에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>What are Webhooks?</strong></summary>

A Webhook is a callback to an application or web service that is triggered when a specific event occurs. That means you can set up a Webhook to look for a specific update, change or action to occur in your Helpdesk and it will automatically push the information you specify to the application you want. In simple words, two applications communicate using Webhooks.Webhooks can be triggered via the automation rules that run on ticket creation and rules that run on ticket updates in Freshdesk.

</details>

<details>
<summary><strong>How do I create an app?</strong></summary>

To get information about creating different apps in Freshdesk you can refer to this documentation: [https://developers.freshdesk.com/v2/docs/quick-start/](https://developers.freshdesk.com/v2/docs/quick-start/)

</details>

<details>
<summary><strong>Where can I find my API key?</strong></summary>

**참고: **If your account is on the **Sprout** plan, the API key and the API functionality will NOT be available.An API key is a unique alphanumeric identifier, for each agent on your Freshdesk Account. Irrespective of which version of **Freshdesk's APIs** you use, you will need to provide either your username and password combination or your API key for authorization when making API calls by triggering webhooks. Here's how you can retrieve your API key:- Login to your Freshdesk Account
- Click on your profile picture icon on the top right corner and select **Profile Settings**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/43123696/original/zF3n_DLVhON3Bsp8O71jLHmkLl9gs1WFew.png?1548399480)- On the right pane, you will find the **API Key**
- Copy-paste this as required to authenticate third-party solutionsPlease ensure that you are the administrator/account administrator to perform helpdesk activities using the API. Keep in mind that the API keys for admin/account admin are based on role capabilities. For example, the account admin API is required to install an app from the marketplace or for any integration, while the admin's API can be used for any ticketing-related activities. If you encounter any issues finding your API key under your profile, kindly log in to your helpdesk from a different browser or clear the cache or cookies from your existing browser. Then, log in if needed and navigate through your profile settings to find your API key.

</details>

<details>
<summary><strong>Can I add images to solution articles using API?</strong></summary>

Yes, you can add inline images to your solution articles using API. Refer to the sample code given below :\{"description":"Test Article *Image: Smiley face*","status":2,"title":"Solutions API","type":1\}참고: Please ensure that the image should be hosted in a public location.

</details>

<details>
<summary><strong>Is there any documentation for the APIs on Freshdesk?</strong></summary>

Please visit [http://developer.freshdesk.com/api](http://developer.freshdesk.com/api) for API documentation.

</details>

<details>
<summary><strong>What are the rate limits for the API calls to Freshdesk?</strong></summary>

**참고: **The per-minute rate limiting is being rolled out in batches.The number of API calls you can make is based on your plan. This limit is applied to your account irrespective of the number of agents you have or IP addresses used to make the calls.We're currently moving all Freshdesk accounts from a per-hour limit to a per-minute limit. In this article, we'll give you details on both.**Call limits per minute**** Plan****     Calls per minute **
**Maximum limit per endpoint**
Free00Growth200Ticket Create - 80Ticket Update - 80Tickets List - 20Contacts List - 20Pro400Ticket Create - 160Ticket Update - 160Tickets List - 100Contacts List - 100Enterprise700Ticket Create - 280Ticket Update - 280Tickets List - 200Contacts List - 200For more details, visit our [developer portal](https://developers.freshdesk.com/api/).If you are looking to increase your API limit, or move to the per-minute limiting, please drop an email to support@freshdesk.com with details on your use-case and we'll help you sort this out.******Please note: For every trial period the API limit is 50 per minute.**

</details>

<details>
<summary><strong>Can I add a customer satisfaction survey for a ticket using API?</strong></summary>

Yes, here is the the API documentation for creating a Satisfaction Survey: [https://developer.freshdesk.com/api/#create_satisfaction_rating](https://developer.freshdesk.com/api/#create_satisfaction_rating).The endpoint api/v2/tickets/[ticket_id]/satisfaction_ratings is the one for creating a satisfaction rating using APIs.

</details>

<details>
<summary><strong>What webhooks will contribute to my rate limit?</strong></summary>

Any webhook you have set up on your Freshdesk - be it in an automation rule, or an external webhooks  ( like Zapier or TimeCamp) - will contribute towards adding to the API calls resulting in meeting with your rate limits.

</details>

<details>
<summary><strong>How to create a contact using API?</strong></summary>

Refer this [link](https://developer.freshdesk.com/api/#create_contact) to get detailed information on creating a contact using API.

</details>

<details>
<summary><strong>How to edit the subject line of the tickets based on certain conditions or specific keyword in the subject?</strong></summary>

This can be done using the API. Navigate to **Admin > Workflow > Automations > Ticket Creation > New Rule** and set up an automation rule as follows:**Condition: **Description contains "..........."**Action: **Trigger a webhook![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001067860/original/sHUR6bJSwyf2TAO-2XJZ-ly3VGO0HOFrEQ.png?1588840658)Kindly refer to this[ link](https://developers.freshdesk.com/api/#update_ticket) for more information on updating ticket details via API. Copy the code accordingly for changing the subject.

</details>

<details>
<summary><strong>How do I apply filters and view a list of tickets using API?</strong></summary>

You can view the tickets from a custom ticket list view, using API. You could make use of v1 of API to have this done. Please refer to this [documentation](https://freshdesk.com/api#view_all_ticket) for detailed information on the same.

</details>

<details>
<summary><strong>How to create a ticket with dependent field using API?</strong></summary>

You can use **Create ticket with custom fields** commands via API as given in this [link](https://developer.freshdesk.com/api/#create_ticket) to create a ticket with dependent field using API.

</details>

<details>
<summary><strong>Is there an API to list all the tickets and schedule it for a particular time?</strong></summary>

You could list all tickets on a periodic basis. The API documentation would be available at [http://developer.freshdesk.com/api/#list_all_tickets](http://developer.freshdesk.com/api/#list_all_tickets).**참고:** An automated script has to be run at your end to run this API call at a ***specified time interval.***

</details>

<details>
<summary><strong>How can I view the Ticket Properties of a ticket using API?</strong></summary>

You could use the API to "View a Ticket" and as part of the response, you would be able to receive the Tag added to the ticket.**Command** **:** Get**Callback U****R****L : **/api/v2/tickets/[id]**Sample Curl : **curl -v -u username:password -H "Content-Type: application/json" -X GET '[https://domain.freshdesk.com/api/v2/tickets/20](https://domain.freshdesk.com/api/v2/tickets/20)'

</details>

<details>
<summary><strong>How to remove quoted text via API?</strong></summary>

You can use this command below to remove the quoted text through API:client.interface.trigger("click", \{id: "delete_quoted_text"\})

</details>

<details>
<summary><strong>Can I use my vanity URL or CNAME to make an API call?</strong></summary>

As of now, the V2 of Freshdesk's API supports only the Freshdesk URL on HTTPs. Making calls using the vanity URL isn't supported.

</details>

<details>
<summary><strong>How to handle and prevent webhook drops?</strong></summary>

A Webhook is a callback to an application or web service triggered when a specific event occurs. In case of a particular update, change, or action in your helpdesk, you can set up a Webhook to automatically push specific information to an application through Freshdesk automations - ticket creation and ticket update rules.You can configure as many Webhooks for event triggers as you want but execute them only based on the [API rate limit](https://developer.freshdesk.com/api/#ratelimit) for your account. Any webhooks beyond that limit will be postponed to the next hour if you schedule more than the assigned call rate.If the system postpones a webhook from execution for more than 24 hours, Freshdesk drops the webhook and sends the following alert email to the helpdesk admin.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006747944/original/p3DNq-mnBj1zVIbx0Sn1w_qlKw9-92mXEg.png?1666789883)Also, ensure to set-up webhooks with the correct URL and follow the proper syntax for the webhook content to avoid webhook failures during execution.Please reach out to [support@freshdesk.com](mailto:support@freshdesk.com) to learn more about setting up webhooks for your business use-case more efficiently and avoid failures by keeping them within the API rate limit.

</details>

<details>
<summary><strong>List all tickets with conversations using API</strong></summary>

You can use the API [https://developers.freshdesk.com/api/#list_all_ticket_notes](https://developers.freshdesk.com/api/#list_all_ticket_notes) to list all the conversations of a ticket. You can make use of a script to fetch the conversations of all the tickets as required.To know the tickets in which there are multiple conversations you can take an export of the tickets from the list view page. Choose the parameter 'Customer interaction' and if this is more than 1 it means the customer has replied to the ticket after creating it.

</details>

<details>
<summary><strong>How can I prevent a webhook from being dropped?</strong></summary>

A webhook would be dropped only if it exceeds the permitted API rate limit of your Freshdesk Account. Please write to support@freshdesk.com with details regarding the webhook and use-case for which you had set it up. One of our agents would get in contact with you to discuss on making this more efficient for you, after which you could trigger the webhooks and keep it within the rate limit.

</details>

<details>
<summary><strong>Status codes and its reasons</strong></summary>

In Freshdesk, error codes may appear during various interactions and processes, indicating specific issues or anomalies that need attention. Understanding these error codes and their reasons can help diagnose and resolve the underlying problems efficiently. Below are some common error codes encountered in Freshdesk and the reasons they may occur:HTTP STATUS CODETEXTDESCRIPTION200
OKThe request was successful, and the server responded with the requested data.
201
CreatedThe request was successful, and a new resource was created.
204
No Content
The request was successful, but there is no content to send in the response.
400Client or Validation ErrorThe request body/query string is not in the correct format. For example, the [Create a ticket](http://developer.freshdesk.com/api/#create_ticket) API requires the **requester_id** field to be sent as part of the request and if it is missing, this status code is returned.401Authentication FailureIndicates that the **Authorization** header is either missing or incorrect. You can learn more about the Authorization header [here.](http://developer.freshdesk.com/api/#authentication)403Access DeniedThis indicates that the agent whose credentials were used in making this request was not authorized to perform this API call. It could be that this API call requires admin level credentials or perhaps the Freshdesk portal doesn't have the corresponding feature enabled. It could also indicate that the user has reached the maximum number of failed login attempts or that the account has reached the maximum number of agents404Requested Resource not FoundThis status code is returned when the request contains invalid ID/Freshdesk domain in the URL or an invalid URL itself. For example, an API call to retrieve a ticket with an invalid ID will return a HTTP 404 status code to let you know that no such ticket exists.405Method not allowedThis API request used the wrong HTTP verb/method. For example, an API PUT request on /api/v2/tickets endpoint will return a HTTP 405 as /api/v2/tickets allows only GET and POST requests.406Unsupported Accept HeaderOnly **application/json** and ***/*** are supported.When uploading files multipart/form-data is supported.409Inconsistent/Conflicting StateThe resource that is being created/updated is in an inconsistent or conflicting state. For example, if you attempt to [Create a Contact](http://developer.freshdesk.com/api/#create_user) with an email that is already associated with an existing user, this code will be returned.415Unsupported Content-typeContent type **application/xml** is not supported. Only **application/json** is supported.429Rate Limit ExceededThe API rate limit allotted for your Freshdesk domain has been exhausted.500Unexpected Server ErrorPhew!! You can't do anything more here. This indicates an error at Freshdesk's side. Please [email us](mailto:support@freshdesk.com) your API script along with the response headers. We will reach you out to you and fix this ASAP.502Bad Gateway
The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
503
Service UnavailableThe server is not ready to handle the request, possibly due to maintenance or overload.
504
Gateway Timeout
The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.

</details>

<details>
<summary><strong>Where do I find the documentation for API?</strong></summary>

Freshdesk API documentation could be found under - [https://developers.freshdesk.com/api](https://developers.freshdesk.com/api). Using the information available here, you would be able to build your own account specific API based on your business requirements.

</details>


## 📋 요금제 및 결제

<details>
<summary><strong>Do we have API and integration capabilities in the free Sprout plan?</strong></summary>

No, the access to Freshdesk APIs and the integration capabilities is not available in the free Sprout plan. It will be **available from the Blossom plan onwards.**Please refer [here](https://freshdesk.com/helpdesk-features) for the detailed feature comparison chart.

</details>


## 📋 사용자 관리

<details>
<summary><strong>How do I get a list of agent ID's?</strong></summary>

You can use our API to get a list of all the agents which would include the Agent's IDs as well. To know more about the same you can make use of [https://developers.freshdesk.com/api/#list_all_agents](https://developers.freshdesk.com/api/#list_all_agents)

</details>


## 📋 계정 및 관리

<details>
<summary><strong>Why have I received an email saying 'Please recheck the webhook settings in your account'?</strong></summary>

This is a notification email that is auto-generated when a Webhook which is triggered from your account fails. This Webhook might be a part of the automations or from your server.When you set-up webhooks, you would have entered an incorrect URL or the content in the script for webhooks might be incorrect. Please confirm that you have entered the right URL for those webhooks and verify if the rules are set correctly.

</details>


---

## 🔗 관련 자료

추가적인 도움이 필요하시면 다음 자료들을 참고해 주세요:

- [Freshdesk 도움말 센터](https://support.freshdesk.com)
- [커뮤니티 포럼](https://community.freshworks.com)
- [비디오 튜토리얼](https://freshdesk.com/resources/videos)

:::tip 도움말
더 자세한 정보나 개별 상담이 필요하시면 고객지원팀(support@freshdesk.com)으로 연락해 주세요.
:::
