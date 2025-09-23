---
sidebar_position: 1
---

# 셀프 서비스 포털 FAQ

셀프 서비스 포털에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Freshdesk은 무엇인가요?</strong></summary>

Freshdesk, the online 고객 engagement 해결책 from Freshworks, lets you streamline your company's 고객 지원 using the [고객 서비스 software](https://www.freshworks.com/products/what-is-freshdesk/) and helps you to efficiently manage your customers as you scale. Here's what you can do with Freshdesk,- Track and manage incoming 티켓 from multiple channels into one single view
- 지원 customers across various platforms like 이메일, phone, call, chat, social media, and other messaging apps
- Collaborate with multiple teams within your company to split, assign and resolve queries faster as a 팀
- Automate redundant tasks like agent assignment based on the skill, workload, and availability
- Empower customers with a comprehensive knowledge base and self-서비스 포털
- Analyze and gather critical insights on agent performances and 고객 experience with advanced 분석
- Customize Freshdesk completely to suit your business requirements
- Leverage AI and ML capabilities of Freddy, to take some work off your 상담원 and provide faster resolutions to customers, without compromising on the qualityYou can sign up for a free trial [here](https://freshdesk.com/signup).

</details>

<details>
<summary><strong>create a new Freshdesk 계정하는 방법은 무엇인가요?</strong></summary>

You can create one from under freshdesk.com, using the '**Sign up'** option. The website will collect your contact information before creating a new Freshdesk Trial 계정 for you.Alternatively, you can use the below link to sign up for a new Freshdesk 계정 -
[https://freshdesk.com/signup](https://freshdesk.com/signup)Happy Supporting!

</details>

<details>
<summary><strong>restrict customers from editing the ticket properties after a ticket is submitted하는 방법은 무엇인가요?</strong></summary>

You can use the below-displayed code to restrict the 고객 from editing the ticket fields after a ticket is submitted.Please navigate to **관리자**--> Channels > **Portals **-->**Customize 포털**-->**Layout & pages**-->**포털 pages**-->paste the below code under the **T****icket details** section,jQuery('#portal_ticket_form .controls').each(function() \{jQuery(this).children().attr('disabled','disabled');\});jQuery('#helpdesk_ticket_submit').attr('disabled','disabled')This would be possible only from the **Estate** 요금제 onwards in Freshdesk.

</details>

<details>
<summary><strong>ensure that users do not change their 이메일 address while submitting a ticket, from the 포털하는 방법은 무엇인가요?</strong></summary>

You can pre-populate the users' 이메일 addresses and grey-out the field so that they will not be able to edit the 이메일 address when the user is logged in. This can be done by greying out the 'Requester' field using a jQuery script.The code that you'll have to use is -\{% if 포털.has_user_signed_in %\}jQuery('#helpdesk_ticket_email').prop('disabled', true);\{% endif %\}You would have to place this code below the existing code under **Adm****in --> Channels --> Portals --> Customize 포털 --> Layouts & Pages --> 포털 Pages -->** **New Ticket** and then click on **Save & Publish**.This option would be available from the **Estate** 요금제 onwards.

</details>

<details>
<summary><strong>change "Solutions" to "Knowledge base" on the 고객 포털하는 방법은 무엇인가요?</strong></summary>

Please go to **관리자 > Channels > Portals > Customize > Edit theme > Layouts & Pages** and make the following changes.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009272014/original/ap5QfPlqW_eiGuKxkdA7ME_9j4PWZphhGA.png?1692892469)**Header:**jQuery('#header-tabs a[href='/지원/solutions']').text('Knowledge base');**Footer****:**jQuery('.footer-links a[href='/지원/solutions']').text('Knowledge base');**Search results:**jQuery('.nav-filter li a[href^='/지원/search/solutions?term']').text('Knowledge Base');**참고**:1)This can only be done on accounts in the **Estate and Forest 요금제 (older 요금제 structure)**.2)If multiple languages are set up on the 헬프데스크, you would need to specify the languages.For example, if the 헬프데스크 languages are English and French, here is the script for header:jQuery('#header-tabs a[href="/en/지원/solutions"]').text("Knowledgebase");
jQuery('#header-tabs a[href="/fr/지원/solutions"]').text("Base de connaissances");To learn more about 포털 customization, click [here](https://지원.freshdesk.com/en/지원/solutions/articles/50000003754).

</details>

<details>
<summary><strong>hide the 포털 and 해결책 articles from being crawled on a Google search하는 방법은 무엇인가요?</strong></summary>

To prevent the 포털 from being crawled on a Google Search, you can have the following code attached under 포털 customizations. This would available only for accounts on the **Estate and Forest 요금제**, though.To hide the entire 포털, please go to **관리자 --> Channels --> Portals --> Customize 포털 --> Layouts & Pages --> 포털 Layout --> Head **and add the below mentioned tag:******If you are looking to hide only the Solutions tab from being crawled, please paste the following tag-*********\{% if current_tab == 'solutions' %\}************\{% endif %\}***

</details>

<details>
<summary><strong>hide the 로그인 button from the 고객 포털하는 방법은 무엇인가요?</strong></summary>

If you do not wish your customers to 로그인 to your 포털, but only to view the content which is made available on it, you could hide the 로그인 button from your 포털.To hide the 로그인 button, you can use the following code under the Stylesheet section:a[href*='로그인']\{display:none;\}This can be found under **관리자 --> Channels --> Portals --> Customize --> Edit theme > Stylesheet **and would be available from the **Garden** 요금제 onwards.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009272512/original/dxG0VA5UwyodHf7CEddVYWq5RqXPtZHfVw.png?1692894916)

</details>

<details>
<summary><strong>change the default landing page on the 고객 포털할 수 있나요?</strong></summary>

The default behavior in Freshdesk is that the users will be redirected to the **포털 Home **page when they access the 고객 포털.If you are looking to show the 티켓 page or the Solutions page instead of the 포털 home, below is a small hack to do that.Please add this code under **관리자 --> Channels --> Portals --> Customize 포털 --> Layout & Pages --> 포털 pages --> 포털 home.**window.location.href = 'https://domain.freshdesk.com/지원/solutions';This code will redirect the user to the solutions page when they access the 포털 home page. Similarly, You could replace the URL with the 티켓 page URL to redirect users to the 티켓 page.This is available only from the Estate 요금제 onwards.**참고**: In the code, please replace domain.freshdesk.com with your Freshdesk URL.

</details>

<details>
<summary><strong>create a new 지원 ticket to Freshdesk 지원하는 방법은 무엇인가요?</strong></summary>

Using our Help widget, you can easily search and browse through our FAQs. To create a ticket click **'Get in touch' **option. Alternatively, you could also write to **지원@freshdesk.com**. You can also use our chat 지원 if you have subscribed for a 요금제 where you can engage with our bot/agent and have a ticket created.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001783573/original/nheQe3UdUE9lltalTj5Zd037Ry7iw0NRkQ.png?1600943516)![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001783617/original/78P40g385cg2E4clSAdNabJ1CfDinFnvUg.png?1600943820)

</details>

<details>
<summary><strong>왜 is it best to not overwrite the default style in Freshdesk인가요?</strong></summary>

It is always best to write your own elements since you have access and the space to write your own script, HTML. This way, your elements are independent from the default elements we have provided and would not result in the page breaking. For instance, we could have used the style of the header in more than one place in the website and so overwriting it will automatically reflect it in the other places of the website.

</details>

<details>
<summary><strong>What do I need to do to have different side bars in my 지원 포털?</strong></summary>

To have different side bars, you need to enclose class under a parent element.Example:.custom-homepage \{.sidebar\{//your css code here\}\}.custom-category-page \{.sidebar\{//your css code here\}\}

</details>

<details>
<summary><strong>have colour coding in 티켓 view based on the priority of the ticket할 수 있나요?</strong></summary>

The page is not customisable and so it is not possible to achieve the color coding using a custom script. However, by default, you can see the color coding on the sidebar based on priority as:![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009243392/original/_lHH8M3vZlt5vjeJ5MSL5JIfSp4f3_5PRQ.png?1692714098)

</details>

<details>
<summary><strong>customise my profile page하는 방법은 무엇인가요?</strong></summary>

If you are looking to customise the profile page, you can style it with the scripts in the header that will be carried to the profile page. The 'Edit' page has Header and Footer.

</details>

<details>
<summary><strong>Is there a liquid object available that would tell the url of any of the pages at the 고객 포털?</strong></summary>

“Current_page_name” This is a liquid object used to cull out the name of the current page. Through this, you can see the 포털 homepage, New Ticket Page, Solutions Page, Edit Page etc. As a workaround, you can use jQuery scripts to get the current page URL.

</details>

<details>
<summary><strong>display the first name of the 고객 in the forum details page하는 방법은 무엇인가요?</strong></summary>

Go to **관리자 > Channels > 포털 > Customize 포털 > Layouts & Pages > 포털 pages >Discussions > Topic View**. Replace user.name as user.firstname in the places where user.name is mentioned in the css code of the topic view page.

</details>

<details>
<summary><strong>create a ticket on behalf of a 고객하는 방법은 무엇인가요?</strong></summary>

At times, there might be instances where you need to create a ticket on behalf of a 고객 who reached out to you directly, or for proactive 지원.You can do this under **'+New' -> New Ticket**. You enter the Requester Information, Ticket Subject, and Description and other mandatory fields to raise a ticket on behalf of the Requester.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009272542/original/4x5_twmzUuSbc9M0lqga43vyCa_fRlrbJQ.png?1692895093)

</details>

<details>
<summary><strong>create a ticket for my own reference하는 방법은 무엇인가요?</strong></summary>

At times, an agent might need 티켓 for his/her own reference.Such a ticket can be created by clicking on **New ticket** icon from the Menu bar. The SLA timers would still be ticking on such 티켓.As a workaround, the agent can send in an 이메일 ticket (send an 이메일 to the 지원 이메일 address) and then reply or can add a public 참고 to the same ticket from Freshdesk, this way the First response SLA would not be violated.

</details>

<details>
<summary><strong>the difference between 상담원 and Collaborators은 무엇인가요?</strong></summary>

An agent is a user in your 헬프데스크 who takes care of the 지원 activities as a full-time job. An agent can be assigned the role of an 관리자, supervisor or given a custom role with specified duties.However, a collaborator is a third-party member you invite to be part of a 지원 ticket. These collaborators are not part of your 헬프데스크 but can be added to specific 티켓 as a one-time activity.A few scenarios where you can add collaborators are to provide approvals on a refund request, provide insights on a business use case or give information related to resolving the ticket.Admins can invite[ ](https://지원.freshdesk.com/en/지원/solutions/articles/50000003573-how-to-set-up-collaborators-)[Collaborators](https://지원.freshdesk.com/en/지원/solutions/articles/50000003573-how-to-set-up-collaborators-) from outside the 팀 to your Freshdesk 계정 to collaborate on 티켓 or give your 상담원 the privilege to invite collaborators.Collaborators will then receive an 이메일 inviting them to log into their Freshdesk 계정. They can then view the ticket and 고객 details and collaborate by responding to the private 참고 and helping full-time 상담원 resolve the ticket faster.

</details>

<details>
<summary><strong>the difference between Freshworks URL and Freshdesk URL은 무엇인가요?</strong></summary>

Freshworks Neo Platform is a flexible, end-to-end, AI-powered enterprise platform that offers a set of services that are leveraged by all the applications in the Freshworks portfolio. It is a centralized console offering customizable security and administration solutions across Freshworks products. Admins can leverage different authentication and authorization solutions, various security controls to customize, and simplified agent and 계정 management.When you first sign up for a Freshworks product, an Organization is created. You can access the Neo 관리자 Center using the Organization URL or Freshworks URL that looks something like this: [yourcompany@freshworks.com](mailto:yourcompany@freshworks.com). It binds every 고객 accounts across the Freshworks portfolio together. As an organization 관리자, you can easily access all the accounts, security 설정, and 상담원 under a single glass pane. When you sign up for a standalone Freshdesk 계정, you will be provided with a Freshdesk URL address or subdomain that your admins and 상담원 will use to log in to your Freshdesk 계정. Your customers will also use it to access your self-서비스 포털. E.g., [acmesupport.freshdesk.com](https://acmesupport.freshdesk.com/)

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
