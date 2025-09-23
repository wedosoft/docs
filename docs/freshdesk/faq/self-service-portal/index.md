---
sidebar_position: 1
---

# 셀프 서비스 포털 FAQ

셀프 서비스 포털에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>What is Freshdesk?</strong></summary>

Freshdesk, the online customer engagement solution from Freshworks, lets you streamline your company's customer support using the [customer service software](https://www.freshworks.com/products/what-is-freshdesk/) and helps you to efficiently manage your customers as you scale. Here's what you can do with Freshdesk,- Track and manage incoming tickets from multiple channels into one single view
- Support customers across various platforms like email, phone, call, chat, social media, and other messaging apps
- Collaborate with multiple teams within your company to split, assign and resolve queries faster as a team
- Automate redundant tasks like agent assignment based on the skill, workload, and availability
- Empower customers with a comprehensive knowledge base and self-service portal
- Analyze and gather critical insights on agent performances and customer experience with advanced analytics
- Customize Freshdesk completely to suit your business requirements
- Leverage AI and ML capabilities of Freddy, to take some work off your agents and provide faster resolutions to customers, without compromising on the qualityYou can sign up for a free trial [here](https://freshdesk.com/signup).

</details>

<details>
<summary><strong>How do I restrict customers from editing the ticket properties after a ticket is submitted?</strong></summary>

You can use the below-displayed code to restrict the customer from editing the ticket fields after a ticket is submitted.Please navigate to **Admin**--> Channels > **Portals **-->**Customize portal**-->**Layout & pages**-->**Portal pages**-->paste the below code under the **T****icket details** section,jQuery('#portal_ticket_form .controls').each(function() \{jQuery(this).children().attr('disabled','disabled');\});jQuery('#helpdesk_ticket_submit').attr('disabled','disabled')This would be possible only from the **Estate** plan onwards in Freshdesk.

</details>

<details>
<summary><strong>How do I change "Solutions" to "Knowledge base" on the customer portal?</strong></summary>

Please go to **Admin > Channels > Portals > Customize > Edit theme > Layouts & Pages** and make the following changes.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009272014/original/ap5QfPlqW_eiGuKxkdA7ME_9j4PWZphhGA.png?1692892469)**Header:**jQuery('#header-tabs a[href='/support/solutions']').text('Knowledge base');**Footer****:**jQuery('.footer-links a[href='/support/solutions']').text('Knowledge base');**Search results:**jQuery('.nav-filter li a[href^='/support/search/solutions?term']').text('Knowledge Base');**Note**:1)This can only be done on accounts in the **Estate and Forest plan (older plan structure)**.2)If multiple languages are set up on the helpdesk, you would need to specify the languages.For example, if the helpdesk languages are English and French, here is the script for header:jQuery('#header-tabs a[href="/en/support/solutions"]').text("Knowledgebase");
jQuery('#header-tabs a[href="/fr/support/solutions"]').text("Base de connaissances");To learn more about portal customization, click [here](https://support.freshdesk.com/en/support/solutions/articles/50000003754).

</details>

<details>
<summary><strong>How to hide the portal and solution articles from being crawled on a Google search?</strong></summary>

To prevent the portal from being crawled on a Google Search, you can have the following code attached under Portal customizations. This would available only for accounts on the **Estate and Forest plans**, though.To hide the entire portal, please go to **Admin --> Channels --> Portals --> Customize portal --> Layouts & Pages --> Portal Layout --> Head **and add the below mentioned tag:******If you are looking to hide only the Solutions tab from being crawled, please paste the following tag-*********\{% if current_tab == 'solutions' %\}************\{% endif %\}***

</details>

<details>
<summary><strong>How do I hide the login button from the Customer portal?</strong></summary>

If you do not wish your customers to login to your portal, but only to view the content which is made available on it, you could hide the login button from your portal.To hide the login button, you can use the following code under the Stylesheet section:a[href*='login']\{display:none;\}This can be found under **Admin --> Channels --> Portals --> Customize --> Edit theme > Stylesheet **and would be available from the **Garden** plan onwards.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009272512/original/dxG0VA5UwyodHf7CEddVYWq5RqXPtZHfVw.png?1692894916)

</details>

<details>
<summary><strong>Can I change the default landing page on the customer portal?</strong></summary>

The default behavior in Freshdesk is that the users will be redirected to the **Portal Home **page when they access the Customer portal.If you are looking to show the Tickets page or the Solutions page instead of the portal home, below is a small hack to do that.Please add this code under **Admin --> Channels --> Portals --> Customize portal --> Layout & Pages --> Portal pages --> Portal home.**window.location.href = 'https://domain.freshdesk.com/support/solutions';This code will redirect the user to the solutions page when they access the portal home page. Similarly, You could replace the URL with the tickets page URL to redirect users to the tickets page.This is available only from the Estate plan onwards.**Note**: In the code, please replace domain.freshdesk.com with your Freshdesk URL.

</details>

<details>
<summary><strong>How to create a new support ticket to Freshdesk Support?</strong></summary>

Using our Help widget, you can easily search and browse through our FAQs. To create a ticket click **'Get in touch' **option. Alternatively, you could also write to **support@freshdesk.com**. You can also use our chat support if you have subscribed for a plan where you can engage with our bot/agent and have a ticket created.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001783573/original/nheQe3UdUE9lltalTj5Zd037Ry7iw0NRkQ.png?1600943516)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001783617/original/78P40g385cg2E4clSAdNabJ1CfDinFnvUg.png?1600943820)

</details>

<details>
<summary><strong>Why is it best to not overwrite the default style in Freshdesk?</strong></summary>

It is always best to write your own elements since you have access and the space to write your own script, HTML. This way, your elements are independent from the default elements we have provided and would not result in the page breaking. For instance, we could have used the style of the header in more than one place in the website and so overwriting it will automatically reflect it in the other places of the website.

</details>

<details>
<summary><strong>What do I need to do to have different side bars in my support portal?</strong></summary>

To have different side bars, you need to enclose class under a parent element.Example:.custom-homepage \{.sidebar\{//your css code here\}\}.custom-category-page \{.sidebar\{//your css code here\}\}

</details>

<details>
<summary><strong>Can I have colour coding in tickets view based on the priority of the ticket?</strong></summary>

The page is not customisable and so it is not possible to achieve the color coding using a custom script. However, by default, you can see the color coding on the sidebar based on priority as:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009243392/original/_lHH8M3vZlt5vjeJ5MSL5JIfSp4f3_5PRQ.png?1692714098)

</details>

<details>
<summary><strong>How do I customise my profile page?</strong></summary>

If you are looking to customise the profile page, you can style it with the scripts in the header that will be carried to the profile page. The 'Edit' page has Header and Footer.

</details>

<details>
<summary><strong>Is there a liquid object available that would tell the url of any of the pages at the customer portal?</strong></summary>

“Current_page_name” This is a liquid object used to cull out the name of the current page. Through this, you can see the portal homepage, New Ticket Page, Solutions Page, Edit Page etc. As a workaround, you can use jQuery scripts to get the current page URL.

</details>

<details>
<summary><strong>How can I display the first name of the customer in the forum details page?</strong></summary>

Go to **Admin > Channels > Portal > Customize portal > Layouts & Pages > Portal pages >Discussions > Topic View**. Replace user.name as user.firstname in the places where user.name is mentioned in the css code of the topic view page.

</details>

<details>
<summary><strong>How do I create a ticket on behalf of a customer?</strong></summary>

At times, there might be instances where you need to create a ticket on behalf of a customer who reached out to you directly, or for proactive support.You can do this under **'+New' -> New Ticket**. You enter the Requester Information, Ticket Subject, and Description and other mandatory fields to raise a ticket on behalf of the Requester.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009272542/original/4x5_twmzUuSbc9M0lqga43vyCa_fRlrbJQ.png?1692895093)

</details>

<details>
<summary><strong>How do I create a ticket for my own reference?</strong></summary>

At times, an agent might need tickets for his/her own reference.Such a ticket can be created by clicking on **New ticket** icon from the Menu bar. The SLA timers would still be ticking on such tickets.As a workaround, the agent can send in an email ticket (send an email to the support email address) and then reply or can add a public note to the same ticket from Freshdesk, this way the First response SLA would not be violated.

</details>

<details>
<summary><strong>What is the difference between Freshworks URL and Freshdesk URL?</strong></summary>

Freshworks Neo Platform is a flexible, end-to-end, AI-powered enterprise platform that offers a set of services that are leveraged by all the applications in the Freshworks portfolio. It is a centralized console offering customizable security and administration solutions across Freshworks products. Admins can leverage different authentication and authorization solutions, various security controls to customize, and simplified agent and account management.When you first sign up for a Freshworks product, an Organization is created. You can access the Neo Admin Center using the Organization URL or Freshworks URL that looks something like this: [yourcompany@freshworks.com](mailto:yourcompany@freshworks.com). It binds every customer accounts across the Freshworks portfolio together. As an organization admin, you can easily access all the accounts, security settings, and agents under a single glass pane. When you sign up for a standalone Freshdesk account, you will be provided with a Freshdesk URL address or subdomain that your admins and agents will use to log in to your Freshdesk account. Your customers will also use it to access your self-service portal. E.g., [acmesupport.freshdesk.com](https://acmesupport.freshdesk.com/)

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How do I create a new Freshdesk Account?</strong></summary>

You can create one from under freshdesk.com, using the '**Sign up'** option. The website will collect your contact information before creating a new Freshdesk Trial Account for you.Alternatively, you can use the below link to sign up for a new Freshdesk account -
[https://freshdesk.com/signup](https://freshdesk.com/signup)Happy Supporting!

</details>


## 📋 사용자 관리

<details>
<summary><strong>How to ensure that users do not change their email address while submitting a ticket, from the portal?</strong></summary>

You can pre-populate the users' email addresses and grey-out the field so that they will not be able to edit the email address when the user is logged in. This can be done by greying out the 'Requester' field using a jQuery script.The code that you'll have to use is -\{% if portal.has_user_signed_in %\}jQuery('#helpdesk_ticket_email').prop('disabled', true);\{% endif %\}You would have to place this code below the existing code under **Adm****in --> Channels --> Portals --> Customize portal --> Layouts & Pages --> Portal Pages -->** **New Ticket** and then click on **Save & Publish**.This option would be available from the **Estate** plan onwards.

</details>

<details>
<summary><strong>What is the difference between Agents and Collaborators?</strong></summary>

An agent is a user in your helpdesk who takes care of the support activities as a full-time job. An agent can be assigned the role of an admin, supervisor or given a custom role with specified duties.However, a collaborator is a third-party member you invite to be part of a support ticket. These collaborators are not part of your helpdesk but can be added to specific tickets as a one-time activity.A few scenarios where you can add collaborators are to provide approvals on a refund request, provide insights on a business use case or give information related to resolving the ticket.Admins can invite[ ](https://support.freshdesk.com/en/support/solutions/articles/50000003573-how-to-set-up-collaborators-)[Collaborators](https://support.freshdesk.com/en/support/solutions/articles/50000003573-how-to-set-up-collaborators-) from outside the team to your Freshdesk account to collaborate on tickets or give your agents the privilege to invite collaborators.Collaborators will then receive an email inviting them to log into their Freshdesk account. They can then view the ticket and customer details and collaborate by responding to the private note and helping full-time agents resolve the ticket faster.

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
