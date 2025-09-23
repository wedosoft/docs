---
sidebar_position: 1
---

# 셀프 서비스 포털

이 섹션에서는 셀프 서비스 포털와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 고급 기능 및 사용법

<details>
<summary>어떻게 restrict customers from editing the ticket properties after a ticket is submitted?</summary>

<p><span style={{ fontSize: "16px" }}>You can use the below-displayed code to restrict the customer from editing the ticket fields after a ticket is submitted. </span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span dir="ltr" style={{ fontSize: "16px" }}>Please navigate to <strong>Admin</strong>--&gt; Channels &gt; <strong dir="ltr">Portals </strong>--&gt;<strong dir="ltr">Customize portal</strong>--&gt;<strong>Layout &amp; pages</strong>--&gt;<strong>Portal pages</strong>--&gt;paste the below code under the <strong>T</strong><strong>icket details</strong> section,</span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>&lt;script&gt;</span></p><p><span style={{ fontSize: "16px" }}> jQuery('#portal_ticket_form .controls').each(function() { </span></p><p><span style={{ fontSize: "16px" }}> jQuery(this).children().attr('disabled','disabled'); </span></p><p><span style={{ fontSize: "16px" }}> });</span></p><p><span style={{ fontSize: "16px" }}> jQuery('#helpdesk_ticket_submit').attr('disabled','disabled')</span></p><p><span style={{ fontSize: "16px" }}>&lt;/script&gt;</span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>This would be possible only from the <strong>Estate</strong> plan onwards in Freshdesk. </span></p><p><br /></p>

</details>

<details>
<summary>어떻게 change "Solutions" to "지식 베이스" on the customer portal?</summary>

<p ><span dir="ltr" style={{ fontSize: "16px", fontFamily: "Arial"" }}>Please go to <strong dir="ltr" style={{ fontFamily: "Arial"" }}>Admin &gt; Channels &gt; Portals &gt; Customize &gt; Edit theme &gt; Layouts &amp; Pages</strong> and make the following changes.</span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /><img src="#" style={{ width: "auto", fontFamily: "Arial"" }} class="fr-fic fr-fil fr-dib" /><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><br /></span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><strong style={{ fontFamily: "Arial"" }}>Header:</strong></span></span></p><div><pre contenteditable="false" rel="highlighter">&lt;script&gt; jQuery('#header-tabs a[href='/support/solutions']').text('Knowledge base'); &lt;/script&gt;</pre></div><div style={{ fontFamily: "Arial"" }}><br /></div><div></div><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><strong dir="ltr" style={{ fontFamily: "Arial"" }}>Footer</strong><strong style={{ fontFamily: "Arial"" }}>:</strong></span></span></p><div style={{ fontFamily: "Arial"" }}><pre contenteditable="false" rel="highlighter" style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}>&lt;script&gt; jQuery('.footer-links a[href='/support/solutions']').text('Knowledge base'); &lt;/script&gt;</span></pre></div><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><br /></span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><strong style={{ fontFamily: "Arial"" }}>Search results:</strong></span></span></p><div style={{ fontFamily: "Arial"" }}><pre contenteditable="false" rel="highlighter" style={{ fontFamily: "Arial"" }}>&lt;script&gt; jQuery('.nav-filter li a[href^='/support/search/solutions?term']').text('Knowledge Base'); &lt;/script&gt;</pre></div><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}><strong style={{ fontFamily: "Arial"" }}>Note</strong>:&nbsp;</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}>1)This can only be done on accounts in the <strong dir="ltr" style={{ fontFamily: "Arial"" }}>Estate and Forest plan (older plan structure)</strong>.</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "16px", fontFamily: "Arial"" }}>2)If multiple languages are set up on the helpdesk, you would need to specify the languages.</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "16px", fontFamily: "Arial"" }}>For example, if the helpdesk languages are English and French, here is the script for header:</span></span></p><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><div style={{ fontFamily: "Arial"" }}><pre contenteditable="false" rel="highlighter" style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}>&lt;script&gt; jQuery('#header-tabs a[href="/en/support/solutions"]').text("Knowledgebase"); jQuery('#header-tabs a[href="/fr/support/solutions"]').text("Base de connaissances"); &lt;/script&gt;</span></pre></div><p style={{ fontFamily: "Arial"" }}><span style={{ fontFamily: "Helvetica Neue" }}><span dir="ltr" style={{ fontSize: "16px", fontFamily: "Arial"" }}>To learn more about portal customization, click <a href="https://support.freshdesk.com/en/support/solutions/articles/50000003754">here</a>.</span></span></p><p ><span style={{ fontFamily: "Helvetica Neue" }}><br /></span></p><p ><br /></p>

</details>

<details>
<summary>어떻게 hide the login button from the Customer portal?</summary>

<p ><span style={{ fontSize: "16px" }}>If you do not wish your customers to login to your portal, but only to view the content which is made available on it, you could hide the login button from your portal.&nbsp;</span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>To hide the login button, you can use the following code under the Stylesheet section:</span></p><div><pre contenteditable="false" rel="highlighter">a[href*='login'] {display:none;}</pre></div><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span dir="ltr" style={{ fontSize: "16px" }}>This can be found under <strong dir="ltr">Admin --&gt; Channels --&gt; Portals --&gt; Customize --&gt; Edit theme &gt; Stylesheet&nbsp;</strong>and would be available from the <strong >Garden</strong> plan onwards.</span></p><p ><br /></p><p ><span dir="ltr" style={{ fontSize: "16px" }}><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></span><br /></p>

</details>

<details>
<summary>할 수 있나요 change the default landing page on the customer portal?</summary>

<p ><span style={{ fontSize: "16px" }}>The default behavior in Freshdesk is that the users will be redirected to the <strong >Portal Home </strong>page when they access the Customer portal.</span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>If you are looking to show the Tickets page or the Solutions page instead of the portal home, below is a small hack to do that. </span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>Please add this code under <strong dir="ltr">Admin --&gt; Channels --&gt; Portals --&gt; Customize portal --&gt; Layout &amp; Pages --&gt; Portal pages --&gt; Portal home.</strong></span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><pre contenteditable="false" rel="highlighter"><span style={{ fontSize: "16px" }}><code >&lt;script type='text/javascript'&gt;<br /> window.location.href = 'https://domain.freshdesk.com/support/solutions';<br />&lt;/script&gt;</code></span></pre><p ><span style={{ fontSize: "16px" }}></span></p><p ><span style={{ fontSize: "16px" }}>This code will redirect the user to the solutions page when they access the portal home page. Similarly, You could replace the URL with the tickets page URL to redirect users to the tickets page.</span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}>This is available only from the Estate plan onwards.</span></p><p ><br /></p><p ><span style={{ fontSize: "16px" }}><strong >Note</strong>: In the code, please replace domain.freshdesk.com with your Freshdesk URL.</span></p><p ><br /></p>

</details>

<details>
<summary>어떻게 customise my profile page?</summary>

<p>If you are looking to customise the profile page, you can style it with the scripts in the header that will be carried to the profile page. The 'Edit' page has Header and Footer.</p>

</details>

<details>
<summary>Is there a liquid object available that would tell the url of any of the pages at the customer portal?</summary>

<p>“Current_page_name” This is a liquid object used to cull out the name of the current page. Through this, you can see the portal homepage, New Ticket Page, Solutions Page, Edit Page etc. As a workaround, you can use jQuery scripts to get the current page URL.</p>

</details>

<details>
<summary>어떻게 할 수 있나요 display the first name of the customer in the forum details page?</summary>

<p dir="ltr">Go to <strong>Admin &gt; Channels &gt; Portal &gt; Customize portal &gt; Layouts &amp; Pages &gt; Portal pages &gt;Discussions &gt; Topic View</strong>. Replace user.name as user.firstname in the places where user.name is mentioned in the css code of the topic view page. </p>

</details>

<details>
<summary>어떻게 create a ticket on behalf of a customer?</summary>

<p>At times, there might be instances where you need to create a ticket on behalf of a customer who reached out to you directly, or for proactive support.</p><p><br /></p><p dir="ltr">You can do this under <strong>'+New' -&gt; New Ticket</strong>. You enter the Requester Information, Ticket Subject, and Description and other mandatory fields to raise a ticket on behalf of the Requester.</p><p dir="ltr"><br /></p><p dir="ltr"><img src="#" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" /></p>

</details>


## 관리 및 유지보수

<details>
<summary>무엇인가요 Freshdesk?</summary>

<p >Freshdesk, the online customer engagement solution from Freshworks, lets you streamline your company's customer support using the <a href="https://www.freshworks.com/products/what-is-freshdesk/">customer service software</a> and helps you to efficiently manage your customers as you scale. Here's what you can do with Freshdesk,</p><ul ><li >Track and manage incoming tickets from multiple channels into one single view</li><li >Support customers across various platforms like email, phone, call, chat, social media, and other messaging apps</li><li >Collaborate with multiple teams within your company to split, assign and resolve queries faster as a team</li><li >Automate redundant tasks like agent assignment based on the skill, workload, and availability</li><li >Empower customers with a comprehensive knowledge base and self-service portal&nbsp;</li><li >Analyze and gather critical insights on agent performances and customer experience with advanced analytics</li><li >Customize Freshdesk completely to suit your business requirements</li><li dir="ltr">Leverage AI and ML capabilities of Freddy, to take some work off your agents and provide faster resolutions to customers, without compromising on the quality<br /><br />You can sign up for a free trial <a href="https://freshdesk.com/signup" rel="noopener noreferrer" target="_blank">here</a>.</li></ul>

</details>

<details>
<summary>어떻게 create a new Freshdesk Account?</summary>

<p>You can create one from under freshdesk.com, using the '<strong>Sign up'</strong> option. The website will collect your contact information before creating a new Freshdesk Trial Account for you.<br /><br />Alternatively, you can use the below link to sign up for a new Freshdesk account -<br /><a href="https://freshdesk.com/signup">https://freshdesk.com/signup</a><br /><br />Happy Supporting!</p>

</details>

<details>
<summary>방법 ensure that users do not change their email address while submitting a ticket, from the portal?</summary>

<p><span rel="tempredactor" style={{ fontSize: "16px" }}>You can pre-populate the users' email addresses and grey-out the field so that they will not be able to edit the email address when the user is logged in. This can be done by greying out the 'Requester' field using a jQuery script.</span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">The code that you'll have to use is - </span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor"><br /></span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">{% if portal.has_user_signed_in %}</span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">&lt;script type='text/javascript'&gt;</span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">jQuery('#helpdesk_ticket_email').prop('disabled', true);</span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">&lt;/script&gt;</span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">{% endif %}</span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor"><br /></span></span></p><p><span style={{ fontSize: "16px" }}><span rel="tempredactor">You would have to place this code below the existing code under <strong>Adm</strong><strong dir="ltr">in --&gt; Channels --&gt; Portals --&gt; Customize portal --&gt; Layouts &amp; Pages --&gt; Portal Pages --&gt;</strong><strong>New Ticket</strong> and then click on <strong>Save &amp; Publish</strong>.</span></span></p><p><span style={{ fontSize: "16px" }}><br /></span></p><p><span style={{ fontSize: "16px" }}>This option would be available from the <strong>Estate</strong> plan onwards.</span></p>

</details>

<details>
<summary>방법 hide the portal and solution articles from being crawled on a Google 검색?</summary>

<p ><span style={{ fontSize: "16px" }}>To prevent the portal from being crawled on a Google Search, you can have the following code attached under Portal customizations. This would available only for accounts on the <strong >Estate and Forest plans</strong>, though. </span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p dir="ltr"><span style={{ fontSize: "16px" }}>To hide the entire portal, please go to <strong dir="ltr">Admin --&gt; Channels --&gt; Portals --&gt; Customize portal --&gt; Layouts &amp; Pages --&gt; Portal Layout --&gt; Head </strong>and add the below mentioned tag:</span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}><strong ><em >&lt;META NAME='ROBOTS' CONTENT='NOINDEX, NOFOLLOW'&gt;</em></strong></span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}>If you are looking to hide only the Solutions tab from being crawled, please paste the following tag- </span></p><p ><span style={{ fontSize: "16px" }}><strong ><em ><br /></em></strong></span></p><p ><span style={{ fontSize: "16px" }}><em ><strong >{% if current_tab == 'solutions' %}</strong></em></span></p><p ><span style={{ fontSize: "16px" }}><em ><strong >&lt;meta name='robots' content='noindex, nofollow'&gt;</strong></em></span></p><p ><span style={{ fontSize: "16px" }}><strong ><em >{% endif %}</em></strong></span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><span style={{ fontSize: "16px" }}><br /></span></p><p ><br /></p>

</details>

<details>
<summary>방법 create a new support ticket to Freshdesk Support?</summary>

<p dir="ltr" style={{ textAlign: "left" }}>Using our Help widget, you can easily search and browse through our FAQs. To create a ticket click <strong>'Get in touch'&nbsp;</strong>option. Alternatively, you could also write to <strong>support@freshdesk.com</strong>. You can also use our chat support if you have subscribed for a plan where you can engage with our bot/agent and have a ticket created.</p><p style={{ textAlign: "left" }}><br /></p><p style={{ textAlign: "center" }}><br /><span style={{ caretColor: "rgb(0, 0, 0)", color: "rgb(0, 0, 0)" }}><img width="232px;" height="407px;" src="#" class="fr-fic fr-dii fr-bordered" /><span style={{ caretColor: "rgb(0, 0, 0)", color: "rgb(0, 0, 0)" }}><img width="232px;" height="406px;" src="#" class="fr-fic fr-dii fr-bordered" /></span></span></p><p style={{ textAlign: "center" }}><br /></p><p style={{ textAlign: "center" }}><br /></p><p style={{ textAlign: "left" }}><br /></p>

</details>

<details>
<summary>왜인가요 it best to not overwrite the default style in Freshdesk?</summary>

<p>It is always best to write your own elements since you have access and the space to write your own script, HTML. This way, your elements are independent from the default elements we have provided and would not result in the page breaking. For instance, we could have used the style of the header in more than one place in the website and so overwriting it will automatically reflect it in the other places of the website.</p>

</details>

<details>
<summary>What 필요한가요 to do to have different side bars in my support portal?</summary>

<p>To have different side bars, you need to enclose class under a parent element. </p><p><br /></p><p>Example:</p><p>.custom-homepage {</p><p> .sidebar{</p><p> //your css code here</p><p> }</p><p>}</p><p>.custom-category-page {</p><p> .sidebar{</p><p> //your css code here</p><p> }</p><p>}</p>

</details>

<details>
<summary>할 수 있나요 have colour coding in tickets view based on the 우선순위 of the ticket?</summary>

<p>The page is not customisable and so it is not possible to achieve the color coding using a custom script. However, by default, you can see the color coding on the sidebar based on priority as:</p><p dir="ltr"><br /></p><p dir="ltr"><img src="#" style={{ width: "237px" }} class="fr-fic fr-fil fr-dib" /></p><p><br /></p>

</details>

<details>
<summary>어떻게 create a ticket for my own reference?</summary>

<p>At times, an agent might need tickets for his/her own reference.</p><p><br /></p><p>Such a ticket can be created by clicking on <strong>New ticket</strong> icon from the Menu bar. The SLA timers would still be ticking on such tickets.</p><p><br /></p><p>As a workaround, the agent can send in an email ticket (send an email to the support email address) and then reply or can add a public note to the same ticket from Freshdesk, this way the First response SLA would not be violated.</p><p><br /></p>

</details>

<details>
<summary>무엇인가요 the difference between Agents and Collaborators?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "16px", fontFamily: "Arial, Helvetica, sans-serif", color: "rgb(14, 16, 26)", fontWeight: "400" }}>An agent is a user in your helpdesk who takes care of the support activities as a full-time job. An agent can be assigned the role of an admin, supervisor or given a custom role with specified duties.&nbsp;</span></p><p style={{ fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><br /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><span style={{ color: "rgb(14, 16, 26)", fontWeight: "400" }}>However, a collaborator is a third-party member you invite to be part of a support ticket. These collaborators are not part of your helpdesk but can be added to specific tickets as a one-time activity.&nbsp;</span></span></span></p><p style={{ fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><br /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><span style={{ color: "rgb(14, 16, 26)", fontWeight: "400" }}>A few scenarios where you can add collaborators are to provide approvals on a refund request, provide insights on a business use case or give information related to resolving the ticket.</span></span></span></p><p style={{ fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><br /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt", fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><span style={{ color: "rgb(14, 16, 26)", fontWeight: "400" }}>Admins can invite</span><a href="https://support.freshdesk.com/en/support/solutions/articles/50000003573-how-to-set-up-collaborators-"><span style={{ color: "rgb(74, 110, 224)", fontWeight: "400", textDecorationSkipInk: "none" }}>&nbsp;</span></a><a href="https://support.freshdesk.com/en/support/solutions/articles/50000003573-how-to-set-up-collaborators-">Collaborators</a></span><span style={{ color: "rgb(14, 16, 26)", fontWeight: "400" }}>&nbsp;from outside the team to your Freshdesk account to collaborate on tickets or give your agents the privilege to invite collaborators.</span></span></p><p style={{ fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontFamily: "Arial,Helvetica,sans-serif" }}><br /></span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px" }}><span style={{ color: "rgb(14, 16, 26)", fontWeight: "400" }}>Collaborators will then receive an email inviting them to log into their Freshdesk account. They can then view the ticket and customer details and collaborate by responding to the private note and helping full-time agents resolve the ticket faster.</span></span></p><p><br /></p>

</details>

<details>
<summary>무엇인가요 the difference between Freshworks URL and Freshdesk URL?</summary>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Freshworks Neo Platform</span><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;is a flexible, end-to-end, AI-powered enterprise platform that offers a set of services that are leveraged by all the applications in the Freshworks portfolio. It is a&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>centralized console</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;offering customizable security and administration solutions across Freshworks products. Admins can leverage different authentication and authorization solutions, various security controls to customize, and simplified agent and account management. <br />&nbsp;</span></span></p><p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontFamily: "Helvetica Neue" }}><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>When you first sign up for a Freshworks product, an Organization is created. You can access the Neo Admin Center using the&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Organization URL or Freshworks URL</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>&nbsp;that looks something like this:&nbsp;</span><a href="mailto:yourcompany@freshworks.com" style={{ fontFamily: "Arial"" }}><span style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none", fontFamily: "Arial"" }}>yourcompany@freshworks.com</span></a><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>. It binds every customer accounts across the Freshworks portfolio together. As an organization admin, you can easily access all the accounts, security settings, and agents under a single glass pane. <br /><br />When you sign up for a&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>standalone Freshdesk account</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>, you will be provided with a&nbsp;</span><span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "700", fontFamily: "Arial"" }}>Freshdesk URL</span></span><span style={{ fontSize: "12pt", fontFamily: "Arial"", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;address or subdomain that your admins and agents will use to log in to your Freshdesk account. <span style={{ fontSize: "12pt", color: "rgb(0, 0, 0)", fontWeight: "400", fontFamily: "Arial"" }}>Your customers will also use it to access your self-service portal. E.g.,&nbsp;</span><a href="https://acmesupport.freshdesk.com/"><span dir="ltr" style={{ fontSize: "12pt", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none" }}>acmesupport.freshdesk.com</span></a></span></p>

</details>

