---
sidebar_position: 1
---

# 복수 제품 FAQ

복수 제품에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>What do you mean by multiple products?</strong></summary>

Freshdesk lets you 지원 multiple products by creating dedicated portals for each product. Any ticket created from these multiple product portals would come into one central 헬프데스크 and 상담원 could work on these 티켓 from a single location. If your organisation has various products, this would be the best option for you.To get a detailed overview click this [link](https://지원.freshdesk.com/지원/solutions/articles/37638-supporting-multiple-products-with-freshdesk).

</details>

<details>
<summary><strong>왜 would I need to set up Multiple Products in Freshdesk인가요?</strong></summary>

Multiple products let you set up separate 지원 portals for each of your products, giving each of them a separate platform and a unique URL.Also, you'll gain the ability to restrict 해결책 and forum categories specific to products without additional 계정 charges. When you have different services or products for which you need independent 지원 portals, they all could be integrated within the same 계정 using this feature.

</details>

<details>
<summary><strong>set up multiple products on a 포털하는 방법은 무엇인가요?</strong></summary>

The Multiple Products feature is available from the Estate 요금제 onwards in Freshdesk.To set up a new product, please navigate to **관리자 > 지원 Operar > Multiple Products **and then click on New Product. Enter the details related to the product and a new 이메일 address for this product is mandatory.Configure separate 지원 emails for each product. They can be automatically queued in a specific group by filling in the details requested under 'Product 지원 이메일'.[This article](https://지원.freshdesk.com/지원/solutions/articles/37638-supporting-multiple-products-with-freshdesk) provides additional information on this process.

</details>

<details>
<summary><strong>Where do I enter the URL for my new product ?</strong></summary>

Under **관리자 > Channels > Portals > Edit(corresponding to the 포털 name)**, you would have the option to provide the 포털 URL. Here, you could provide a vanity URL like **help.yourcompany.com** (help is the subdomain) and associate it with your Product 포털.Before using this field please ensure that you have created a CNAME record in your DNS Zone file to point **help.yourcompany.com** to yourcompany.freshdesk.com(your Freshdesk 계정 URL). Once this is done, you would be able to access the newly created Product 포털 using the specified 포털 URL.

</details>

<details>
<summary><strong>re­assign a 지원 이메일 address from the main 포털 to one of the products할 수 있나요?</strong></summary>

Yes, please navigate to **관리자 > Channels > 이메일**. Here, you could see the list of 지원 이메일 addresses that could be associated with the products added in **관리자 > 지원 Operations > Multiple products. **Kindly click on edit next to the 지원 address and choose the product under "Link this 지원 이메일 with a product." 참고 that this product should already be added to the 헬프데스크.

</details>

<details>
<summary><strong>While adding a new product I get the 오류 message "Please enter a valid 이메일 address". Why so?</strong></summary>

For each 포털 on your 계정, you would have one dedicated primary 이메일 address associated with it. The main 포털 will have a similar primary 지원 이메일 and the product 포털 will have it's own distinct primary 이메일 address.Existing emails cannot be used while creating a new product. You would have to add a new/unique 이메일 address and associated it with the New Product which is being created.

</details>

<details>
<summary><strong>How will multiple portals look on the end-user side? Will they have to 로그인 with different credentials?</strong></summary>

Multiple portals will look like two different websites from the customers' point of view.Once a 고객 is signed up on a 포털, he/she can use the same credentials to log into the other 포털 as well, depending on how the URLs are exposed. You would be able to determine the 포털 access by changing the user permissions in 관리자 -> Portals -> 설정.Please navigate to **관리자 > Workflows > 이메일 Notifications > Requester Notifications > click on insert placeholder **and include the placeholder for product-specific URL. This would allow customers to navigate to the 지원 of the appropriate product.

</details>

<details>
<summary><strong>use the same 상담원 and SLAs for multiple products할 수 있나요?</strong></summary>

Yes, 상담원 can be provided with access to view different products, and SLAs can be shared between different products as well.Please navigate to **관리자 > Workflows > SLA policies > click on new policy** and choose "Apply this SLA to" where you could add products for which the SLA is applied.

</details>

<details>
<summary><strong>have product-specific SLA policies할 수 있나요?</strong></summary>

Please navigate to **A****dmin > Workflows > SLA Policies > click on Edit** next to a new **SLA policy. **Inside this page, you would find the option called '**Apply this to**' that you could use to associate the policy to any of the products you have created. Kindly 참고 that this option would not be available for the "Default SLA policy."

</details>

<details>
<summary><strong>brand 티켓 separately for different products할 수 있나요?</strong></summary>

While creating multiple products, you could set a distinct branding for 티켓 created through emails. You could have this done by setting up a dedicated 지원 이메일 addresses for each Product.When you create a new product(under **관리자 > 지원 Operations > Multiple Products > New Product**), you would be asked to provide a separate 지원 이메일 address for that 포털. This would be the primary 지원 이메일 address for that product 포털 and emails sent to this 이메일 would get created as 티켓 and would be updated with the corresponding Product. By default, replies to customers would also be sent through this dedicated 이메일 address.

</details>

<details>
<summary><strong>make the Ticket URL sent out with every reply 포털-specific할 수 있나요?</strong></summary>

Yes, this is possible. Please navigate to **A****dmin > Workflows > 이메일 Notification > Template > Agent Reply Template **and click on "insert placeholder which would give you the placeholders available in the system. Kindly choose the placeholder** "****\{\{ticket.portal_url\}\}” under 헬프데스크 options** to add it in your reply and position it according to your preference.This will insert a product-specific ticket URL inside a ticket rather than the generic ticket URL which would map the customers to the right 포털.

</details>

<details>
<summary><strong>restrict the visibility of 해결책 articles with respect to the product portals할 수 있나요?</strong></summary>

The visibility of 해결책 articles can be set by entering the necessary 해결책 articles in the "Solutions" tab under the 포털 categories of the respective 포털. Please navigate to **관리자 ­> Channels > Portals > Corresponding 포털 name **and add these articles in its solutions tab.If you have articles common to more than one or two portals, kindly click on edit in the category to choose the portals the category must be visible in.Further, visibility could be set to logged-in users or all users within the folder where it could be changed according to your requirement. Another alternative is to set user permission for the solutions in **관리자 -> Channels -> Portals -> 설정 -> User Permissions -> who can view the 해결책 articles. **

</details>

<details>
<summary><strong>set the product in the embeddable widget하는 방법은 무엇인가요?</strong></summary>

You would be able to set-up feedback widgets that are dedicated to specific product 포털. You will be able to have this done by making modifications to the widget code that you add. The product URL would have to be changed in the respective product in the "src" field of the widget code.

</details>

<details>
<summary><strong>How do multiple brand names work under the same 계정?</strong></summary>

Once multiple products are set up under a single 계정 mycompany.com pointing to (companyname.freshdesk.com), the different products could be identified by a vanity URL.This vanity URL should point to the product's Freshdesk URL; i.e. if product1.companyname.com and product2.company.com are vanity URLs of the 포털, then [point the CNAME](https://지원.freshdesk.com/en/지원/solutions/articles/37590) to companyname.freshdesk.com.This will ensure that you have multiple brands from a 고객's perspective, but all under the same Freshdesk 계정 from an agent's point of view which increases the overall productivity.

</details>

<details>
<summary><strong>transfer 해결책 articles from the main 포털 to the product 포털하는 방법은 무엇인가요?</strong></summary>

Please navigate to **solutions **tab of the 포털 and click on the category which needs to be visible in the product 포털 as well. Once you are on that page with the category and the list of folders please click on the "pen and paper" icon next to the heading which allows you to edit the category.Kindly choose the product 포털 in **"visible in 포털" **option. This will ensure that the articles under this category will only be visible on the associated product 포털.

</details>

<details>
<summary><strong>setup different Kbase for different products하는 방법은 무엇인가요?</strong></summary>

You could configure the 해결책 Articles such that each product has a different KBase. This could be set up under **관리자 > Channels > ****Portals > **Select the **Product Porta****l-->**Under **포털 Categories**, select the respective **해결책 Category** to be displayed for that product 포털.

</details>

<details>
<summary><strong>view the 티켓 pertaining only to a particular product하는 방법은 무엇인가요?</strong></summary>

Please navigate to the **"티켓" **tab on the global header next to the 대시보드 where you could see all the 티켓 in your view or a list of 티켓 depending on the filters chosen.You could remove all the other filters and choose the "Product" name alone using the **Product **field. If you have access to view all 티켓, you will be able to view all 티켓 for that particular product, under this view. Kindly make sure you have **global** access (in agent profile) to view all 티켓.

</details>

<details>
<summary><strong>restrict an agent’s access to 티켓 from one 포털 only할 수 있나요?</strong></summary>

The scope of an agent can be based on the groups in the 포털. Please navigate to **관리자 -> 팀 -> 상담원 -> click on edit **to associate groups within the profile.This group could be routed to a product under **관리자­­ -> 지원 Operations -> Multiple Products­­ -> Edit the product­­ -> Assign to Group** and 상담원 who specifically need to access this product could be added to that Group under **관리자 -­­> 팀 -> Groups**. They are the ones with group access on the 포털. This would restrict them to a particular product 포털.

</details>

<details>
<summary><strong>send product-based 이메일 notifications하는 방법은 무엇인가요?</strong></summary>

With the Multiple Products feature available in Freshdesk, you can create several products, depending on your 요금제 type. If you have set up your Freshdesk 계정 to 지원 multiple products, you must include proper branding in all your outgoing messages.Here are the two stages in setting up product-based 이메일 notifications in Freshdesk.- [Disable default 이메일 notifications](#Disable-default-이메일-notifications)[](#Use-product-specific-placeholders-in-automation-rules)
- [Use product-specific placeholders in automation rules](#Use-product-specific-placeholders-in-automation-rules)[](https://docs.google.com/document/d/15hi58ihFIICB9-paFY1pHhlQG1t2xqkO_5P8zUNdeXE/edit#heading=h.mgjnmdxaiyf7)**Disable default 이메일 notifications**
Disabling the default 이메일 notifications is imperative as they are generic and not entirely product-specific. As an 관리자 of your Freshdesk 계정, you can disable them by following the steps below.-
Navigate to 관리자 from the menu. Select Workflows and click on 이메일 Notifications.-
Click on the active green toggle button next to the 이메일 notification to disable them.![Disable default 이메일 notification.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008501660/original/35Q5ATEYEbZQeQyC83VvPOt8FFnH6UezXQ.gif?1685598715)**Use product-specific placeholders in automation rules**
Use the automation rules on ticket creation and ticket updates to send product-specific 이메일 notifications for new 티켓 and replies.Make sure to perform the following three key changes while creating the automation rules to customize 이메일 updates.-
Choose Condition as 'Product is.'-
Action as send '이메일 to Requester'.-
Make use of product-specific placeholders under the Action section.![Key changes for setting up product-specific automation rules.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008578610/original/euv1YQJGn4EK10ktkoYC-HqFM0icAhjzpA.gif?1686307370)

</details>

<details>
<summary><strong>Is there a placeholder for a product-specific activation URL when a new 고객 signs up?</strong></summary>

The default placeholder '\{\{activation_url\}\}' under **관리자 -> Workflows -> 이메일 notification -> Requester notifications -> User activation** will automatically send a URL based on the product without any prior configuration.

</details>

<details>
<summary><strong>make Facebook pages product-specific하는 방법은 무엇인가요?</strong></summary>

Please navigate to **관리자 -> Channels ­-> Facebook -> click on Edit corresponding to a particular page. **Once there, you would be able to edit the page and choose a product in **"link to Product."**Kindly 참고 that one Facebook page could be linked to one product only.

</details>

<details>
<summary><strong>associate separate group for each product할 수 있나요?</strong></summary>

Yes, you can allocate a unique group for each product in the 포털. While creating a 포털 under **관리자> 지원 Operations > Multiple products**, there is an option to choose an 이메일 address and a group for that particular product as shown in the image below :![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/44751322/original/jJz3zmzoNsb3MuPS3-iWZ_Ut_CO4V7qqBA.png?1554961143)

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
