---
sidebar_position: 1
---

# 복수 제품 FAQ

복수 제품에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>What do you mean by multiple products?</strong></summary>

Freshdesk lets you support multiple products by creating dedicated portals for each product. Any ticket created from these multiple product portals would come into one central helpdesk and agents could work on these tickets from a single location. If your organisation has various products, this would be the best option for you.To get a detailed overview click this [link](https://support.freshdesk.com/support/solutions/articles/37638-supporting-multiple-products-with-freshdesk).

</details>

<details>
<summary><strong>Why would I need to set up Multiple Products in Freshdesk?</strong></summary>

Multiple products let you set up separate support portals for each of your products, giving each of them a separate platform and a unique URL.Also, you'll gain the ability to restrict solution and forum categories specific to products without additional account charges. When you have different services or products for which you need independent support portals, they all could be integrated within the same account using this feature.

</details>

<details>
<summary><strong>How do I set up multiple products on a portal?</strong></summary>

The Multiple Products feature is available from the Estate Plan onwards in Freshdesk.To set up a new product, please navigate to **Admin > Support Operar > Multiple Products **and then click on New Product. Enter the details related to the product and a new email address for this product is mandatory.Configure separate support emails for each product. They can be automatically queued in a specific group by filling in the details requested under 'Product Support Email'.[This article](https://support.freshdesk.com/support/solutions/articles/37638-supporting-multiple-products-with-freshdesk) provides additional information on this process.

</details>

<details>
<summary><strong>Where do I enter the URL for my new product ?</strong></summary>

Under **Admin > Channels > Portals > Edit(corresponding to the portal name)**, you would have the option to provide the Portal URL. Here, you could provide a vanity URL like **help.yourcompany.com** (help is the subdomain) and associate it with your Product portal.Before using this field please ensure that you have created a CNAME record in your DNS Zone file to point **help.yourcompany.com** to yourcompany.freshdesk.com(your Freshdesk Account URL). Once this is done, you would be able to access the newly created Product Portal using the specified Portal URL.

</details>

<details>
<summary><strong>Is it possible to re­assign a support email address from the main portal to one of the products?</strong></summary>

Yes, please navigate to **Admin > Channels > Email**. Here, you could see the list of support email addresses that could be associated with the products added in **Admin > Support Operations > Multiple products. **Kindly click on edit next to the support address and choose the product under "Link this support email with a product." Note that this product should already be added to the helpdesk.

</details>

<details>
<summary><strong>Is it possible to have product-specific SLA policies?</strong></summary>

Please navigate to **A****dmin > Workflows > SLA Policies > click on Edit** next to a new **SLA policy. **Inside this page, you would find the option called '**Apply this to**' that you could use to associate the policy to any of the products you have created. Kindly note that this option would not be available for the "Default SLA policy."

</details>

<details>
<summary><strong>Can I brand tickets separately for different products?</strong></summary>

While creating multiple products, you could set a distinct branding for tickets created through emails. You could have this done by setting up a dedicated support email addresses for each Product.When you create a new product(under **Admin > Support Operations > Multiple Products > New Product**), you would be asked to provide a separate support email address for that portal. This would be the primary support email address for that product portal and emails sent to this email would get created as tickets and would be updated with the corresponding Product. By default, replies to customers would also be sent through this dedicated email address.

</details>

<details>
<summary><strong>Can I make the Ticket URL sent out with every reply portal-specific?</strong></summary>

Yes, this is possible. Please navigate to **A****dmin > Workflows > Email Notification > Template > Agent Reply Template **and click on "insert placeholder which would give you the placeholders available in the system. Kindly choose the placeholder** "****\{\{ticket.portal_url\}\}” under helpdesk options** to add it in your reply and position it according to your preference.This will insert a product-specific ticket URL inside a ticket rather than the generic ticket URL which would map the customers to the right portal.

</details>

<details>
<summary><strong>Is it possible to restrict the visibility of solution articles with respect to the product portals?</strong></summary>

The visibility of solution articles can be set by entering the necessary solution articles in the "Solutions" tab under the Portal categories of the respective portal. Please navigate to **Admin ­> Channels > Portals > Corresponding portal name **and add these articles in its solutions tab.If you have articles common to more than one or two portals, kindly click on edit in the category to choose the portals the category must be visible in.Further, visibility could be set to logged-in users or all users within the folder where it could be changed according to your requirement. Another alternative is to set user permission for the solutions in **관리자 -> Channels -> Portals -> settings -> User Permissions -> who can view the solution articles. **

</details>

<details>
<summary><strong>How do I set the product in the embeddable widget?</strong></summary>

You would be able to set-up feedback widgets that are dedicated to specific product portal. You will be able to have this done by making modifications to the widget code that you add. The product URL would have to be changed in the respective product in the "src" field of the widget code.

</details>

<details>
<summary><strong>How to transfer solution articles from the main portal to the product portal?</strong></summary>

Please navigate to **solutions **tab of the portal and click on the category which needs to be visible in the product portal as well. Once you are on that page with the category and the list of folders please click on the "pen and paper" icon next to the heading which allows you to edit the category.Kindly choose the product portal in **"visible in portal" **option. This will ensure that the articles under this category will only be visible on the associated product portal.

</details>

<details>
<summary><strong>How do I setup different Kbase for different products?</strong></summary>

You could configure the Solution Articles such that each product has a different KBase. This could be set up under **Admin > Channels > ****Portals > **Select the **Product Porta****l-->**Under **Portal Categories**, select the respective **Solution Category** to be displayed for that product portal.

</details>

<details>
<summary><strong>How do I view the tickets pertaining only to a particular product?</strong></summary>

Please navigate to the **"Tickets" **tab on the global header next to the dashboard where you could see all the tickets in your view or a list of tickets depending on the filters chosen.You could remove all the other filters and choose the "Product" name alone using the **Product **field. If you have access to view all tickets, you will be able to view all tickets for that particular product, under this view. Kindly make sure you have **global** access (in agent profile) to view all tickets.

</details>

<details>
<summary><strong>How to send product-based email notifications?</strong></summary>

With the Multiple Products feature available in Freshdesk, you can create several products, depending on your plan type. If you have set up your Freshdesk account to support multiple products, you must include proper branding in all your outgoing messages.Here are the two stages in setting up product-based email notifications in Freshdesk.- [Disable default email notifications](#Disable-default-email-notifications)[](#Use-product-specific-placeholders-in-automation-rules)
- [Use product-specific placeholders in automation rules](#Use-product-specific-placeholders-in-automation-rules)[](https://docs.google.com/document/d/15hi58ihFIICB9-paFY1pHhlQG1t2xqkO_5P8zUNdeXE/edit#heading=h.mgjnmdxaiyf7)**Disable default email notifications**
Disabling the default email notifications is imperative as they are generic and not entirely product-specific. As an administrator of your Freshdesk account, you can disable them by following the steps below.-
Navigate to Admin from the menu. Select Workflows and click on Email Notifications.-
Click on the active green toggle button next to the email notification to disable them.![Disable default email notification.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008501660/original/35Q5ATEYEbZQeQyC83VvPOt8FFnH6UezXQ.gif?1685598715)**Use product-specific placeholders in automation rules**
Use the automation rules on ticket creation and ticket updates to send product-specific email notifications for new tickets and replies.Make sure to perform the following three key changes while creating the automation rules to customize email updates.-
Choose Condition as 'Product is.'-
Action as send 'Email to Requester'.-
Make use of product-specific placeholders under the Action section.![Key changes for setting up product-specific automation rules.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008578610/original/euv1YQJGn4EK10ktkoYC-HqFM0icAhjzpA.gif?1686307370)

</details>

<details>
<summary><strong>Is there a placeholder for a product-specific activation URL when a new customer signs up?</strong></summary>

The default placeholder '\{\{activation_url\}\}' under **관리자 -> Workflows -> Email notification -> Requester notifications -> User activation** will automatically send a URL based on the product without any prior configuration.

</details>

<details>
<summary><strong>How can I make Facebook pages product-specific?</strong></summary>

Please navigate to **관리자 -> Channels ­-> Facebook -> click on Edit corresponding to a particular page. **Once there, you would be able to edit the page and choose a product in **"link to Product."**Kindly note that one Facebook page could be linked to one product only.

</details>

<details>
<summary><strong>Can I associate separate group for each product?</strong></summary>

Yes, you can allocate a unique group for each product in the portal. While creating a portal under **Admin> Support Operations > Multiple products**, there is an option to choose an email address and a group for that particular product as shown in the image below :![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44751322/original/jJz3zmzoNsb3MuPS3-iWZ_Ut_CO4V7qqBA.png?1554961143)

</details>


## 📋 문제 해결

<details>
<summary><strong>While adding a new product I get the error message "Please enter a valid email address". Why so?</strong></summary>

For each portal on your account, you would have one dedicated primary email address associated with it. The main portal will have a similar primary support email and the product portal will have it's own distinct primary email address.Existing emails cannot be used while creating a new product. You would have to add a new/unique email address and associated it with the New Product which is being created.

</details>


## 📋 사용자 관리

<details>
<summary><strong>How will multiple portals look on the end-user side? Will they have to login with different credentials?</strong></summary>

Multiple portals will look like two different websites from the customers' point of view.Once a customer is signed up on a portal, he/she can use the same credentials to log into the other portal as well, depending on how the URLs are exposed. You would be able to determine the portal access by changing the user permissions in 관리자 -> Portals -> settings.Please navigate to **Admin > Workflows > Email Notifications > Requester Notifications > click on insert placeholder **and include the placeholder for product-specific URL. This would allow customers to navigate to the support of the appropriate product.

</details>

<details>
<summary><strong>Is it possible to use the same agents and SLAs for multiple products?</strong></summary>

Yes, agents can be provided with access to view different products, and SLAs can be shared between different products as well.Please navigate to **Admin > Workflows > SLA policies > click on new policy** and choose "Apply this SLA to" where you could add products for which the SLA is applied.

</details>

<details>
<summary><strong>Is it possible to restrict an agent’s access to tickets from one portal only?</strong></summary>

The scope of an agent can be based on the groups in the portal. Please navigate to **관리자 -> Team -> Agents -> click on edit **to associate groups within the profile.This group could be routed to a product under **Admin­­ -> Support Operations -> Multiple Products­­ -> Edit the product­­ -> Assign to Group** and agents who specifically need to access this product could be added to that Group under **Admin -­­> Team -> Groups**. They are the ones with group access on the portal. This would restrict them to a particular product portal.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How do multiple brand names work under the same account?</strong></summary>

Once multiple products are set up under a single account mycompany.com pointing to (companyname.freshdesk.com), the different products could be identified by a vanity URL.This vanity URL should point to the product's Freshdesk URL; i.e. if product1.companyname.com and product2.company.com are vanity URLs of the portal, then [point the CNAME](https://support.freshdesk.com/en/support/solutions/articles/37590) to companyname.freshdesk.com.This will ensure that you have multiple brands from a customer's perspective, but all under the same Freshdesk account from an agent's point of view which increases the overall productivity.

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
