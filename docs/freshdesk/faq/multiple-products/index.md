---
sidebar_position: 1
---

# 복수 제품 FAQ

복수 제품에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>What do you mean 에 의해 다수의 products?</strong></summary>

Freshdesk lets you 지원 다수의 products 에 의해 creating dedicated portals 위해 each product. Any ticket created 에서 these 다수의 product portals would come into one central 헬프데스크 그리고 상담원 could work 에 these 티켓 에서 single location. 만약 your organisation has 다양한 products, this would be best option 위해 you. 로 get detailed overview 클릭 this [link](https://지원.freshdesk.com/지원/solutions/articles/37638-supporting-다수의-products-와 함께-freshdesk).

</details>

<details>
<summary><strong>왜 would I need 로 set up 다수의 Products 에서 Freshdesk?</strong></summary>

다수의 products let you set up separate 지원 portals 위해 each 의 your products, giving each 의 them separate platform 그리고 unique URL. Also, you'll gain ability 로 restrict 해결책 그리고 forum categories 특정한 로 products without additional 계정 charges. 언제 you have different services 또는 products 위해 which you need independent 지원 portals, they all could be integrated within same 계정 using this feature.

</details>

<details>
<summary><strong>set up 다수의 products 에 포털?하는 방법은 무엇인가요?</strong></summary>

다수의 Products feature is 사용 가능한 에서 Estate 요금제 onwards 에서 Freshdesk. 로 set up new product, please 이동 로 **관리자 > 지원 Operar > 다수의 Products**그리고 그러면 클릭 에 New Product. 입력 details related 로 product 그리고 new 이메일 address 위해 this product is mandatory. Configure separate 지원 emails 위해 each product. They can be automatically queued 에서 특정한 group 에 의해 filling 에서 details requested under 'Product 지원 이메일'. [This article](https://지원.freshdesk.com/지원/solutions/articles/37638-supporting-다수의-products-와 함께-freshdesk) provides additional information 에 this process.

</details>

<details>
<summary><strong>Where do I 입력 URL 위해 my new product ?</strong></summary>

Under **관리자 > Channels > Portals > 편집(corresponding 로 포털 name)**, you would have option 로 제공하다 포털 URL. Here, you could 제공하다 vanity URL like **help.yourcompany.com** (help is subdomain) 그리고 associate it 와 함께 your Product 포털. Before using this 필드 please 확인하다 that you have created CNAME record 에서 your DNS Zone file 로 point **help.yourcompany.com** 로 yourcompany.freshdesk.com(your Freshdesk 계정 URL). Once this is done, you would be able 로 access newly created Product 포털 using specified 포털 URL.

</details>

<details>
<summary><strong>re­assign 지원 이메일 address 에서 main 포털 로 one 의 products?할 수 있나요은 무엇인가요?</strong></summary>

Yes, please 이동 로 **관리자 > Channels > 이메일**. Here, you could see list 의 지원 이메일 addresses that could be associated 와 함께 products added 에서 **관리자 > 지원 Operations > 다수의 products.** Kindly 클릭 에 편집 next 로 지원 address 그리고 선택 product under "Link this 지원 이메일 와 함께 product." 참고 that this product should already be added 로 헬프데스크.

</details>

<details>
<summary><strong>While adding new product I get 오류 message "Please 입력 valid 이메일 address". 왜 so?</strong></summary>

위해 each 포털 에 your 계정, you would have one dedicated primary 이메일 address associated 와 함께 it. main 포털 will have similar primary 지원 이메일 그리고 product 포털 will have it's own distinct primary 이메일 address. Existing emails cannot be used while creating new product. You would have 로 추가 new/unique 이메일 address 그리고 associated it 와 함께 New Product which is being created.

</details>

<details>
<summary><strong>How will 다수의 portals look 에 end-user side? Will they have 로 로그인 와 함께 different credentials?</strong></summary>

다수의 portals will look like two different websites 에서 customers' point 의 view. Once 고객 is signed up 에 포털, he/she can use same credentials 로 log into other 포털 as well, depending 에 how URLs are exposed. You would be able 로 determine 포털 access 에 의해 changing user permissions 에서 관리자 -> Portals -> 설정. Please 이동 로 **관리자 > Workflows > 이메일 Notifications > Requester Notifications > 클릭 에 insert placeholder**그리고 include placeholder 위해 product-특정한 URL. This would allow customers 로 이동 로 지원 의 appropriate product.

</details>

<details>
<summary><strong>use same 상담원 그리고 SLAs 위해 다수의 products?할 수 있나요은 무엇인가요?</strong></summary>

Yes, 상담원 can be provided 와 함께 access 로 view different products, 그리고 SLAs can be shared between different products as well. Please 이동 로 **관리자 > Workflows > SLA policies > 클릭 에 new policy** 그리고 선택 "Apply this SLA 로" where you could 추가 products 위해 which SLA is applied.

</details>

<details>
<summary><strong>have product-특정한 SLA policies?할 수 있나요은 무엇인가요?</strong></summary>

Please 이동 로 ******dmin > Workflows > SLA Policies > 클릭 에 편집** next 로 new **SLA policy.** Inside this page, you would find option called '**Apply this 로**' that you could use 로 associate policy 로 any 의 products you have created. Kindly 참고 that this option would not be 사용 가능한 위해 "기본값 SLA policy."

</details>

<details>
<summary><strong>brand 티켓 separately 위해 different products?할 수 있나요은 무엇인가요?</strong></summary>

While creating 다수의 products, you could set distinct branding 위해 티켓 created through emails. You could have this done 에 의해 setting up dedicated 지원 이메일 addresses 위해 each Product. 언제 you 생성 new product(under **관리자 > 지원 Operations > 다수의 Products > New Product**), you would be asked 로 제공하다 separate 지원 이메일 address 위해 that 포털. This would be primary 지원 이메일 address 위해 that product 포털 그리고 emails sent 로 this 이메일 would get created as 티켓 그리고 would be updated 와 함께 corresponding Product. 에 의해 기본값, replies 로 customers would also be sent through this dedicated 이메일 address.

</details>

<details>
<summary><strong>make Ticket URL sent out 와 함께 every reply 포털-특정한?할 수 있나요은 무엇인가요?</strong></summary>

Yes, this is possible. Please 이동 로 ******dmin > Workflows > 이메일 Notification > Template > Agent Reply Template**그리고 클릭 에 "insert placeholder which would give you placeholders 사용 가능한 에서 system. Kindly 선택 placeholder**"****\{\{ticket.portal_url\}\}” under 헬프데스크 options** 로 추가 it 에서 your reply 그리고 position it according 로 your preference. This will insert product-특정한 ticket URL inside ticket rather than generic ticket URL which would map customers 로 right 포털.

</details>

<details>
<summary><strong>restrict visibility 의 해결책 articles 와 함께 respect 로 product portals?할 수 있나요은 무엇인가요?</strong></summary>

visibility 의 해결책 articles can be set 에 의해 entering necessary 해결책 articles 에서 "Solutions" tab under 포털 categories 의 respective 포털. Please 이동 로 **관리자 ­> Channels > Portals > Corresponding 포털 name**그리고 추가 these articles 에서 its solutions tab. 만약 you have articles 일반적인 로 more than one 또는 two portals, kindly 클릭 에 편집 에서 category 로 선택 portals category must be visible 에서. Further, visibility could be set 로 logged-에서 users 또는 all users within folder where it could be changed according 로 your requirement. Another alternative is 로 set user permission 위해 solutions 에서 **관리자 -> Channels -> Portals -> 설정 -> User Permissions -> who can view 해결책 articles.**

</details>

<details>
<summary><strong>set product 에서 embeddable 위젯?하는 방법은 무엇인가요?</strong></summary>

You would be able 로 set-up feedback widgets that are dedicated 로 특정한 product 포털. You will be able 로 have this done 에 의해 making modifications 로 위젯 code that you 추가. product URL would have 로 be changed 에서 respective product 에서 "src" 필드 의 위젯 code.

</details>

<details>
<summary><strong>How do 다수의 brand names work under same 계정?</strong></summary>

Once 다수의 products are set up under single 계정 mycompany.com pointing 로 (companyname.freshdesk.com), different products could be identified 에 의해 vanity URL. This vanity URL should point 로 product's Freshdesk URL; i.e. 만약 product1.companyname.com 그리고 product2.company.com are vanity URLs 의 포털, 그러면 [point CNAME](https://지원.freshdesk.com/en/지원/solutions/articles/37590) 로 companyname.freshdesk.com. This will 확인하다 that you have 다수의 brands 에서 고객's perspective, 하지만 all under same Freshdesk 계정 에서 agent's point 의 view which increases overall productivity.

</details>

<details>
<summary><strong>transfer 해결책 articles 에서 main 포털 로 product 포털?하는 방법은 무엇인가요?</strong></summary>

Please 이동 로 **solutions**tab 의 포털 그리고 클릭 에 category which needs 로 be visible 에서 product 포털 as well. Once you are 에 that page 와 함께 category 그리고 list 의 folders please 클릭 에 "pen 그리고 paper" icon next 로 heading which allows you 로 편집 category. Kindly 선택 product 포털 에서 **"visible 에서 포털"**option. This will 확인하다 that articles under this category will only be visible 에 associated product 포털.

</details>

<details>
<summary><strong>설정 different Kbase 위해 different products?하는 방법은 무엇인가요?</strong></summary>

You could configure 해결책 Articles such that each product has different KBase. This could be set up under **관리자 > Channels >****Portals >**선택 **Product Porta****l-->**Under **포털 Categories**, 선택 respective **해결책 Category** 로 be displayed 위해 that product 포털.

</details>

<details>
<summary><strong>view 티켓 pertaining only 로 particular product?하는 방법은 무엇인가요?</strong></summary>

Please 이동 로 **"티켓"**tab 에 global header next 로 대시보드 where you could see all 티켓 에서 your view 또는 list 의 티켓 depending 에 filters chosen. You could 제거 all other filters 그리고 선택 "Product" name alone using **Product**필드. 만약 you have access 로 view all 티켓, you will be able 로 view all 티켓 위해 that particular product, under this view. Kindly make sure you have **global** access (에서 agent profile) 로 view all 티켓.

</details>

<details>
<summary><strong>restrict agent’s access 로 티켓 에서 one 포털 only?할 수 있나요은 무엇인가요?</strong></summary>

scope 의 agent can be based 에 groups 에서 포털. Please 이동 로 **관리자 -> 팀 -> 상담원 -> 클릭 에 편집**로 associate groups within profile. This group could be routed 로 product under **관리자­­ -> 지원 Operations -> 다수의 Products­­ -> 편집 product­­ -> Assign 로 Group** 그리고 상담원 who specifically need 로 access this product could be added 로 that Group under **관리자 -­­> 팀 -> Groups**. They are ones 와 함께 group access 에 포털. This would restrict them 로 particular product 포털.

</details>

<details>
<summary><strong>send product-based 이메일 notifications?하는 방법은 무엇인가요?</strong></summary>

와 함께 다수의 Products feature 사용 가능한 에서 Freshdesk, you can 생성 several products, depending 에 your 요금제 입력. 만약 you have set up your Freshdesk 계정 로 지원 다수의 products, you must include proper branding 에서 all your outgoing messages. Here are two stages 에서 setting up product-based 이메일 notifications 에서 Freshdesk. - [비활성화 기본값 이메일 notifications](#비활성화-기본값-이메일-notifications)[](#Use-product-특정한-placeholders-에서-automation-rules) - [Use product-특정한 placeholders 에서 automation rules](#Use-product-특정한-placeholders-에서-automation-rules)[](https://docs.google.com/document/d/15hi58ihFIICB9-paFY1pHhlQG1t2xqkO_5P8zUNdeXE/편집#heading=h.mgjnmdxaiyf7) **비활성화 기본값 이메일 notifications** Disabling 기본값 이메일 notifications is imperative as they are generic 그리고 not entirely product-특정한. As 관리자 의 your Freshdesk 계정, you can 비활성화 them 에 의해 following steps below. - 이동 로 관리자 에서 menu. 선택 Workflows 그리고 클릭 에 이메일 Notifications. - 클릭 에 active green toggle button next 로 이메일 notification 로 비활성화 them. ![비활성화 기본값 이메일 notification.](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008501660/original/35Q5ATEYEbZQeQyC83VvPOt8FFnH6UezXQ.gif?1685598715) **Use product-특정한 placeholders 에서 automation rules** Use automation rules 에 ticket creation 그리고 ticket updates 로 send product-특정한 이메일 notifications 위해 new 티켓 그리고 replies. Make sure 로 perform following three key changes while creating automation rules 로 사용자 정의하다 이메일 updates. - 선택 Condition as 'Product is.' - Action as send '이메일 로 Requester'. - Make use 의 product-특정한 placeholders under Action section. ![Key changes 위해 setting up product-특정한 automation rules.](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008578610/original/euv1YQJGn4EK10ktkoYC-HqFM0icAhjzpA.gif?1686307370)

</details>

<details>
<summary><strong>Is there placeholder 위해 product-특정한 activation URL 언제 new 고객 signs up?</strong></summary>

기본값 placeholder '\{\{activation_url\}\}' under **관리자 -> Workflows -> 이메일 notification -> Requester notifications -> User activation** will automatically send URL based 에 product without any prior 구성.

</details>

<details>
<summary><strong>make Facebook pages product-특정한?하는 방법은 무엇인가요?</strong></summary>

Please 이동 로 **관리자 -> Channels ­-> Facebook -> 클릭 에 편집 corresponding 로 particular page.**Once there, you would be able 로 편집 page 그리고 선택 product 에서 **"link 로 Product."** Kindly 참고 that one Facebook page could be linked 로 one product only.

</details>

<details>
<summary><strong>associate separate group 위해 each product?할 수 있나요은 무엇인가요?</strong></summary>

Yes, you can allocate unique group 위해 each product 에서 포털. While creating 포털 under **관리자> 지원 Operations > 다수의 products**, there is option 로 선택 이메일 address 그리고 group 위해 that particular product as shown 에서 image below : ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/44751322/original/jJz3zmzoNsb3MuPS3-iWZ_Ut_CO4V7qqBA.png?1554961143)

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
