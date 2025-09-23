---
sidebar_position: 1
---

# SSL 및 보안 FAQ

SSL 및 보안에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Data storage and data security in Freshdesk</strong></summary>

**How can I be sure that my data is safe with Freshdesk? Where is the data hosted?**We take matters of data security very seriously at Freshdesk. We are hosted on the highly reliable Amazon AWS servers, that promise optimal uptime, and data security for all our customers and ticket data.Our hosting partner is AWS and our servers are hosted in a world-class AWS data center, that is protected by biometric locks and 24-hour surveillance. We ensure that our application is always up to date with the latest security patches. All Freshdesk 요금제 include SSL encryption to keep your data safe.**How is the data stored?**The product is built on multi-tenant cloud architecture and every 고객's data is logically segregated with a unique tenant ID so that one 고객 cannot access another 고객 data.**What information security controls are available / deployed?****Data Segregation:**Freshworks uses a multi-tenant data model to host all its applications. Each application is serviced from an individual virtual private cloud and each 고객 is uniquely identified by a tenant ID. The application is engineered and verified to ensure that it always fetches data only for the logged-in tenant. Per this design, no 고객 has access to another 고객’s data.**Access control:**Freshworks has an in-built authentication module where it provides the ability for customers to define user names and assign access roles. Users can be authenticated either using the authentication module within Freshworks products or via the 고객’s SSO. In case customers are using our own authentication module (SSO, AD, etc..), the 비밀번호 rules for authentication & 비밀번호 policy configured by them will be applied. In addition, customers can restrict 지원 상담원 and customers who can log in to their 지원 포털 to certain IP addresses.**Encryption:**All data at rest is encrypted using AES-256-bit standards with the keys being managed using AWS Key Management 서비스. All data in transit is encrypted. We 지원 only TLS 1.2 and lower versions are deprecated.**Logs:**All the events and activities are logged and monitored on a monthly basis. Application Audit Logs within the 관리자 console (**관리자 >계정 > Audit Log**) captures the user activities and configuration changes or all 상담원. These logs are read-only and also encrypted for protection.**Can the data hosting region be moved? How long will the process take?**The hosting region can only be selected at the time of 계정 creation, and if the data center needs to be moved to a different , you can raise a 지원 ticket to 지원@freshdesk.com. The duration of the migration process depends on the amount of data that needs to be transferred.**Where is the data backed up? Will we lose any data?**All data stored and handled in Freshdesk can be backed up in two ways:1. A continuous backup is maintained in different data centers to 지원 a system failover if it were to occur in the primary data center.2. Data is backed up to persistent storage every day and retained for the last seven days.Application logs are backed up and are maintained for a duration of one year.All backups are encrypted using AES 256-bit encryption and keys being managed through AWS Key Management Services (KMS).**What is the encryption type used in FD?**All data at rest is encrypted using AES-256-bit standards with the keys being managed using AWS Key Management 서비스. All data in transit is encrypted using HTTPS with TLS 1.2 and above.**What data does Freshdesk have access to? What data of ours does Freshdesk Analyze?**By Default, Freshdesk does not have access to any of the 고객's data. In case a 고객 wants a Freshdesk representative to work on their 계정, they have to add them as an occasional agent.Freshdesk stores and processes 고객 data, where data refers to all electronic data, messages, or other material submitted to Freshdesk by the 고객 through the 고객’s 계정 in connection with the 고객’s use of Freshdesk’s 서비스(s). This data is processed in compliance with applicable laws and regulations for the purpose of providing services in the Freshworks product suite. As a data processor, Freshdesk performs operations or set of operations on this data in relation to services offered.‘Data hosted’ means data stored for the delivery of services we provide as a data processor and includes data stored for backup. ‘Data’ stated hereby is with reference to definitions specified in the provided [link](https://www.freshworks.com/privacy/data-hosting/).**How do I erase all the data in my 헬프데스크?**Data Deletion post 계정 termination: Any data deleted will be erased 90 days post date of [termination](https://지원.freshdesk.com/지원/solutions/articles/227558-can-i-completely-delete-a-contact-from-freshdesk-/).**Do you process personal data/PII?**Being the data controller, the 고객 gets to decide what data to host/process in Freshdesk. Freshdesk processes data in accordance with your terms of 서비스**What is Freshdesk’s Data Retention Policy**Data is retained as long as the 고객 is active and using our products. If any delete is performed by the users (상담원, 관리자, etc…) - then the delete is immediate. However, logs will be retained. These logs would be retained for 3 months and then archived in a secure environment with no access unless explicitly approved by the senior management to comply with applicable laws. These archived logs would also be purged automatically after 21 days. The log will just contain only information about the action or event and associated details. Logs will not have any data including PII.Upon 계정 Termination, all 계정 data will be deleted after 90 days from the date of termination. Logs will be retained as mentioned above.To know about Freshworks’ Data Retention Policies, refer these pages:- [Freshworks Terms of 서비스 ](https://www.freshworks.com/terms/)
- [Freshworks Data Processing Addendum ](https://www.freshworks.com/data-processing-addendum/)You can also refer to these links for more details: [Third party data sharing](https://지원.freshdesk.com/지원/solutions/articles/50000002360-third-party-data-sharing-in-freshdesk), [Freshworks Security](https://www.freshworks.com/security/), [Freshworks Data Hosting](https://www.freshworks.com/privacy/data-hosting/) and [Freshworks on GDPR](https://www.freshworks.com/privacy/gdpr/company/).

</details>

<details>
<summary><strong>왜 are we getting a 'connection insecure' 오류 when we try to access our 지원 URL인가요?</strong></summary>

This 오류 generally stems from improper SSL certificate configuration, leading to an unencrypted connection. To address this, ensure your SSL certificate is both up-to-date and correctly installed on your server. Additionally, verify that the URL begins with "https" instead of "http." If complications persist, consider engaging your IT 팀 or hosting provider to rectify the SSL configuration.This 오류 may also arise due to an insecure custom/vanity URL. To rectify this, you can secure your custom URL by [acquiring an SSL certificate](https://지원.freshdesk.com/en/지원/solutions/articles/50000005469) from us. Connect with us at 지원@freshdesk.com to obtain the SSL certificate, thereby resolving the 'connection insecure' 오류 associated with your custom URL.Here are additional troubleshooting steps to troubleshoot SSL issues:- Verify CNAME Record Values: Ensure that the CNAME record values for your custom domain are correctly configured in both your DNS provider and Freshdesk. Use tools like MX Toolbox to cross-check the records and confirm they match.- Check Existing CNAME Values in Freshdesk: Navigate to your Freshdesk 설정 and confirm the existing CNAME values to which your custom domain should be pointed. If you can't locate these values, it might be necessary to remove and re-add your custom domain to regenerate accurate CNAME records.- Regenerate CNAME Records: In cases where CNAME records appear incorrect or mismatched, removing the custom domain from the 포털 and adding it back can generate fresh CNAME records. This step is especially useful if you suspect discrepancies in the records.- Align Domain with New CNAME Value: Once new CNAME records are generated, ensure your custom domain is correctly pointed to the newly provided CNAME value within Freshdesk 설정.- Apply for SSL Certificate: With accurate CNAME records in place, reapply for an SSL certificate from within Freshdesk. This step should proceed without errors, and you'll likely see an "Awaiting Activation" message.- Activation Waiting Period: After applying for the SSL certificate, be patient as it may take up to 24 hours for the SSL certificate to activate. During this time, ensure your domain 설정 remain unchanged for successful activation.By incorporating these additional troubleshooting steps, users will have a comprehensive guide to resolving SSL issues related to custom domains in Freshdesk.

</details>

<details>
<summary><strong>the pricing for SSL certificates? Does it differ with respect to 요금제은 무엇인가요?</strong></summary>

SSL certificates are free for all Freshdesk accounts, across all applicable 요금제.

</details>

<details>
<summary><strong>request a new SSL certificate하는 방법은 무엇인가요?</strong></summary>

SSL is a form of encryption protocol that secures data between browsers and servers. SSL certificates are issued to websites & web portals to ensure a safer experience for businesses & customers.When you sign-up for a Freshdesk 계정, the default 계정 URL, which is usually in the format - [yourcompanyname.freshdesk.com](//yourcompanyname.freshdesk.com) is enabled with a default SSL provided by Freshdesk.**When do you need an SSL Certificate? **Any custom 포털 URL that you create for your 헬프데스크 needs an SSL certificate to load securely (in HTTPS)**How do you get an SSL certificate?**- Go to **관리자>Channels>Portals>Select** the required 포털
- Type your custom domain under the '포털 URL' and add the CNAME record generated by Freshdesk to your domain's DNS. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008479339/original/zmvfh0xJp_SBb2-hQ290J_12X1iRi7phLA.png?1685435298)
- Ensure that the CNAME record is successfully published and hit **Save.**
- The Freshworks SSL certificate will **automatically be approved and enabled **for your domain within 24 hours.
- Once the SSL certificate is enabled, the icon next to the 포털 URL will turn **green,** indicating that your custom 포털 is secured.Before SSL Certificate is enabled:![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008083898/original/_SwD1sMIEQ8OsB12Ex5eR1K-FqZclapO8g.png?1681221195)After SSL Certificate is enabled:![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008083919/original/ypcTn2MDDbxLlgzTgBVKgPumzni8MpcQHA.png?1681221269)****

</details>

<details>
<summary><strong>Can we use a wildcard SSL certificate with Freshdesk?</strong></summary>

No, Freshdesk would only 지원 SSL certificates provided by **Let's encrypt**, specific for your custom URL - wildcard SSL certificates are not supported. This is because all Freshdesk Accounts use the Freshdesk domain. So, we will not be able to share the public and private keys for the domain.

</details>

<details>
<summary><strong>왜 is the Feedback Form not loading on my website after I added an SSL certificate인가요?</strong></summary>

When HTTPS is not used for the Feedback widget, its content would not load in a 포털/website where an SSL certificate is enabled. To overcome this, please navigate to **관리자 > Channels > Feedback Form >Toggle On the option to "Use HTTPS"**.You would have to then replace the widget code on your website with the updated widget code.

</details>

<details>
<summary><strong>TLS 1.0 지원 Deprecation</strong></summary>

From 30th November 2016 (PST), Freshdesk will be moving away from the TLS 1.0 version and will disable the encryption protocol across all its services. The deprecation will have effects on all Freshdesk customers currently using TLS 1.0, and it is advised that you check if you're going to be affected. This 해결책 article will walk you through steps on how you can check if this change affects your business.Described below are the compatibilities across Desktop Browsers and Mobile Operating Systems.
**Desktop browser compatibility**1. Internet Explorer: Desktop versions of IE 8,9 and 10 are TLS compatible if you are running Windows 7 or higher, but not by default. Future versions of Internet Explorer are compatible by default. Achieve compatibility by following the [guide here](https://지원.freshdesk.com/해결책/articles/222861-enabling-tls-1-1-and-tls-1-2-in-internet-explorer)[.](https://지원.freshdesk.com/해결책/articles/222861-enabling-tls-1-1-and-tls-1-2-in-internet-explorer)2. Mozilla Firefox: Versions 23 through 26 are compatible, but not by default. Use about:config to enable TLS 1.1 or TLS 1.2 by updating the security.tls.version.max config value to 2 for TLS 1.1, or 3 for TLS 1.2. All future versions of Mozilla Firefox are TLS 1.0+ compatible by default.3. Google Chrome: All versions of Google Chrome above version 38 are compatible by default.4. Safari: Desktop Safari versions 7 and higher for OS X 10.9 (Mavericks) and higher are, compatible with TLS 1.1 and higher, by default.**Verify your browser compatibility**To verify compatibility for TLS 1.1/TLS 1.2 for your browser, go to [this link](https://www.howsmyssl.com/) and if you are able to view a webpage shown below with the message TLS1.1/TLS1.2 Upgrade Test Passed, then your browser is compatible with Freshdesk. **Internet Explorer **users can achieve compatibility by following the [guide here](https://지원.freshdesk.com/해결책/articles/222861-enabling-tls-1-1-and-tls-1-2-in-internet-explorer)[.](https://지원.freshdesk.com/해결책/articles/222861-enabling-tls-1-1-and-tls-1-2-in-internet-explorer)![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/39061493/original/0jEUfpwrZ01rkwepTJO4D6DKTHtnWbqkFA?1528262963)**Mobile compatibility**Devices running Android OS versions lower than 4.1 are not compatible with TLS versions higher than 1.0. Therefore, the Freshdesk Android app will stop working on devices running these versions of the operating system. Users are advised to upgrade their operating systems to continue using the app.Devices running Android 4.1 to 4.4 need to be on version 3.5 or higher of the Android app to continue using Freshdesk. Users running Android versions 5.0 or higher will not face any issues and can continue using the existing version of the app installed on their device or upgrade to version 3.5 of the app.The iOS app will continue to work seamlessly on compatible iOS versions (iOS 8 and above).Once you have ensured that your Browser/OS will not be affected by the eventual deprecation of TLS, you can follow the steps below to run a compatibility test on your Integrations/API clients (if applicable)
**Steps to check for API compatibility**
-
Set up an API client in a test environment. This could be any software that you are using to integrate to Freshdesk or any custom integration code that you have written.-
In that test environment, change the API client's endpoint hostname from yourdomain.freshdesk.com to tlstest.freshdesk.com.-
If you see a '401 Unauthorized' 오류, then this test passed. This response means that the underlying TLS connection was successful, despite the '401 Unauthorized' 오류.-
If you instead see an 오류 message that involves TLS or https, then the test has failed. Your API client will require adjustments or upgrades. Please check with your client's documentation on how to upgrade to TLS 1.1 or TLS 1.2 지원.**Example using cURL**
This is how the output would look when connected from cURL.(The following test cases were run on cURL version 7.50.0)
Failure case
curl -v  -XGET [https://tlstest.freshdesk.com/api/v2/티켓](https://tlstest.freshdesk.com/api/v2/티켓) --tlsv1.0Output* Server aborted the SSL handshake* Closing connection 0curl: (35) Server aborted the SSL handshakeSuccessful case
curl -v  -XGET [https://tlstest.freshdesk.com/api/v2/티켓](https://tlstest.freshdesk.com/api/v2/티켓) --tlsv1.1OutputHTTP/1.1 401 Unauthorized….….* Connection #0 to host tlstest.freshdesk.com left intact\{"code":"invalid_credentials","message":"You have to be logged in to perform this action."\}If you've got any additional queries, just drop a mail to 지원@freshdesk.com

</details>

<details>
<summary><strong>Enabling TLS 1.2 in Internet Explorer</strong></summary>

If you use Internet Explorer to access Freshdesk, then you can use the following steps to make your browser compatible with TLS 1.2. To change the 설정 in IE 8, 9 or 10:- Go to Tools and select Internet Options
- Select the Advanced tab in Internet Options
- Enable (check) TLS 1.2 and also disable (uncheck) SSL 3.0 for additional security- Click on Apply and OK to complete the procedure![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50000903116/original/pBoGVUlY7Sf26-nfnSVW6NR88a5eLGOwmw.png?1585562186)

</details>

<details>
<summary><strong>Third-party data sharing in Freshdesk</strong></summary>

**Apart from freshworks are there any other parties involved in data storage or processing?**Freshdesk partners with organizations that adhere to global standards and regulations. These organizations include sub-processors or third-parties that Freshworks utilizes to assist in providing its products.List of sub-processors along with their role in processing and their processing location are disclosed in the following [link ](https://www.freshworks.com/privacy/sub-processor/)**Do third party platforms have access to our data?**Third parties only have access to data that is absolutely necessary for them to deliver their services. Further, depending on the services they avail from us, the customers have the option to opt-out of availing services from certain sub-processors. Details of the same can be discussed and mutually agreed upon.

</details>

<details>
<summary><strong>Signing DPA, NDA, and data compliance with Freshdesk:</strong></summary>

**Does a DPA have to be signed?**If you have agreed to freshworks [terms of 서비스](https://www.freshworks.com/terms/), which is available online on our website, it also covers the [data processing addendum](https://www.freshworks.com/data-processing-addendum/) and does not require to be signed additionally. You can find the documentation on the [Freshworks security page](https://www.freshworks.com/data-processing-addendum/).**Do I need to execute a signed copy of the DPA for legal/audit records?**In case you want an e-version (instead of online terms) to be executed, contact us at 지원@freshdesk.com**Need to sign an NDA, details?**If you are an existing 고객 of Freshworks, by using our products,  Freshworks terms of 서비스 available online on our website applies by default. In case you want a physical signed copy with special terms included from your side, contact us at 지원@freshdesk.com**What is the audit and compliance process in Freshdesk?**Freshdesk is audited annually by independent audit firms for ISO 27001, ISO 27701, SOC 2 Type 2, and VAPT. One of the objectives of getting these certifications or attestations is to be able to provide the necessary information to our customers through the audits 보고서 by reputed and independent auditors.Therefore, we will only be able to 지원 security evaluations by means of Security questionnaires, 3rd party audit 보고서, certification requests, and evaluation calls.Further, On a case to case basis where it's mandated by the law/regulations, audits and assessments shall be discussed and agreed in the contract**Is Freshdesk PCI Compliant?**Yes, Freshdesk is PCI Compliant. Freshworks has data security controls in line with the ISO 27001 standards and is audited as per the SOC 2 Type II framework covering the security, confidentiality, and availability of trust 서비스 principles.Further, for running PCI compliant workloads, we work with our customers to satisfy specific use cases where we obfuscate card data that is structured in nature. Examples such as a card data on an 이메일 title( using card data masker integration), or providing encrypted fields over a form.**What is CCPA Compliance? Is Freshdesk CCPA Compliant?**To an extent, Freshdesk 계정 holders are ‘consumers’ as defined under the California Consumer Privacy Act of 2018 (“CCPA”) and Freshdesk is a ‘business’ as defined under CCPA. Thus, the following applies to every Freshdesk 계정 holder:Subject to the provisions of the CCPA, you have the right to request in the manner provided herein, for the following:a. Right to request for information about the:- Categories of Personal Data Freshworks has collected about you.- Specific pieces of Personal Data Freshworks has collected about you.- Categories of sources from which the Personal Data is collected.- Business or commercial purpose for collecting Personal Data.- Categories of third parties with whom the business shares Personal Data.b. Right to request for deletion of any Personal Data collected about you by Freshdesk.If you seek to exercise the foregoing rights to access or delete Personal Data which constitutes ‘personal information’ as defined in CCPA, please contact us at privacy@freshworks.com or write to us here. We respond to all requests we receive from you wishing to exercise your data protection rights within a reasonable timeframe in accordance with applicable data protection laws.By writing to us, you agree to receive communication from us seeking information from you in order to verify you to be the consumer from whom we have collected the Personal Data from and such other information as reasonably required to enable us to honor your request.The list of categories of Personal Data collected and disclosed about consumers are enlisted under the head ‘What Personal Data does Freshworks collect and why?’ and the list of categories of third parties to whom the Personal Data was or maybe made disclosed are enlisted under the head ‘Sharing of Personal Data’. Separately, Freshworks does not sell your Personal Data

</details>

<details>
<summary><strong>delete user data하는 방법은 무엇인가요?</strong></summary>

In Freshdesk, a ‘delete’ or ‘export’ request from a 고객 must be routed via the 관리자, who validates if the requestor is genuine.As an 관리자 of your 헬프데스크 계정, you can- [Soft delete a contact](#Soft-delete-a-contact)
- [Hard delete a contact](#Hard-delete-a-contact)
- [Permanently delete the PII of a deleted contact who was previously an agent](#Permanently-delete-the-PII-of-a-deleted-contact-who-was-previously-an-agent)**Soft delete a contact**
To soft delete a contact in Freshdesk,-
Navigate to the left Menu bar, click on the People icon() and select the 연락처 tab.-
Select one or more 연락처 you wish to delete by clicking on the checkboxes adjacent to their name.-
Click on the Delete button on the top bar.-
Click Confirm on the prompt that appears.![How to soft delete 연락처 in Freshdesk](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538742/original/6VPFlYUHOQ3SMxAsUrBSVbL39cRT4BYSHw.gif?1686031928)In case of accidental deletion, you can [restore the contact](https://지원.freshdesk.com/en/지원/solutions/articles/238096-can-i-restore-a-deleted-contact-how-) back from the Deleted 연락처 list.**Hard delete a contact**
To permanently delete 연락처 data - 티켓, forums, calls & profiles from Freshdesk,-
Navigate to the left Menu bar, click on the People icon() and select the 연락처 tab.-
Click on the Filter icon () on the All 연락처 page and select the Deleted 연락처 view.-
Click on the Contact’s name you wish to delete permanently.-
Click the Delete forever button from the top bar.-
Click DELETE FOREVER on the prompt that appears.![How to hard delete/permanently delete 연락처 in Freshdesk](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538752/original/-bHEixfynbsV9ISgOaz3SXA6uSZzDVvg7g.gif?1686031971)**Permanently delete the PII of a deleted contact who was previously an agent**
If the deleted contact was previously an agent with the 계정, Freshdesk permanently deletes their PII(Personally Identifiable Information) such that the individual is not identifiable thereafter.For business continuity, Freshdesk retains their contributions to the business, such as ticket responses, notes, knowledge base articles, forum topics/comments, 지원 calls, surveys, automation rules, ticket templates, 연락처, companies, tags, etc.For any further information or clarifications, please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com).

</details>

<details>
<summary><strong>export user data하는 방법은 무엇인가요?</strong></summary>

In Freshdesk, a ‘delete’ or ‘export’ request from a 고객 must be routed via the 관리자, who validates if the requestor is genuine.As an 관리자 of your Freshdesk 계정, here’s how you can export 고객 data:- [고객 details export  ](#고객-details-export-%C2%A0)
- [고객 ticket export ](#고객-ticket-export%C2%A0)[](https://docs.google.com/document/d/1adJHEohBmto1hSsCHJUy0r9-Mh9M7yXRjsKqFF2Zx14/edit#heading=h.lbvvr63n1n1n)**고객 details export  **
-
Navigate to the People icon and click on 연락처.-
Select the Export button towards your right.-
Click on the required fields to extract 고객 data.-
Select the Export button to receive an 이메일 with the export.Additionally, you may use the [Freshdesk API call](https://developers.freshdesk.com/api/#view_contact) to pull all the customers’ profile information.![How to export 고객 details from Freshdesk?](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538673/original/lYZ8G7iTk15NZrJ3-QiBqCXK-fhi4O7W-w.gif?1686031214)**고객 ticket export**-
Navigate to 티켓 tab from the menu.-
Navigate to the Filters panel on the right, and choose the required option from the 연락처 dropdown.-
Now click on Apply button to filter 티켓.-
Click on Export button above the Filter page.-
Select the export format, time interval, and click on the required fields to extract 고객 data.-
Select the Export button to receive an 이메일 with the export.![How to export 고객 ticket details from Freshdesk?](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538677/original/2YgbgNPy9G2Cea0kaDdK8DYrZIp3NfDTKg.gif?1686031260)Alternatively, you can also use the [Freshdesk API call](https://developers.freshdesk.com/api/#list_all_tickets) to export all the 티켓 of a 고객.

</details>

<details>
<summary><strong>consent for data share and privacy policy하는 방법은 무엇인가요?</strong></summary>

As a data controller, you need to assess the data you’re collecting in ticket fields or contact fields - you must ensure this is kept to a minimum just enough to provide the necessary 서비스 or 지원.As a data processor, Freshworks performs operations or a set of functions on this data only on your authorization and in compliance with applicable regulations. If you use ‘consent’ as the basis for processing personal data and you’d like to make it more explicit, you can add a checkbox-type mandatory field to your ‘New ticket’ form.For those on 요금제 other than Estate and Forest, manually display the checkbox: I consent to ABC collecting my 이메일 id, phone number, location, and IP.If you are on Estate or Forest 요금제, you can use the 포털 Customization feature to state - ‘I consent to such data being shared with third parties and link it to your Terms of 서비스’![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008410720/original/q8HcaPh4XdLgPDgO-bLIzrmoY0hjk2QfjA.png?1684735157)For any further information or clarifications, please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com).

</details>

<details>
<summary><strong>delete old 티켓 in a given period of time하는 방법은 무엇인가요?</strong></summary>

GDPR mandates that personal data should not be retained for periods longer than necessary for the purposes it was collected. Additionally, we must comply if a 고객 decides to exercise their right to be forgotten/erased. Freshdesk provides the following options to delete 고객 data,- [Delete forever option](https://지원.freshdesk.com/a/solutions/articles/50000005499/edit?lang=en&portalId=74847#Delete-forever-option)
- [Delete 티켓 option](https://지원.freshdesk.com/a/solutions/articles/50000005499/edit?lang=en&portalId=74847#Delete-티켓-option)[](https://docs.google.com/document/d/1JkYHSTVmGAnLvUSgE2p2DELnf5GKQJfPY1Rn4C14zU8/edit#heading=h.i04nl6f0xx0z)**Delete forever option**
As an 관리자 of your Freshdesk 계정, you can use the ‘Delete forever’ option under a contact’s profile to delete the contact once you receive a request for data erasure. This action will permanently delete 고객 information in the system and 티켓/chats/calls they were part of.
**Delete 티켓 option**
Based on your data retention policies, if you wish to automate the deletion of 티켓 in the system, please use our [‘Delete ticket’ API](https://developers.freshdesk.com/api/#delete_a_ticket). This API moves 티켓 to Trash, and Freshdesk will permanently delete the 티켓 after 30 days. You can also periodically go to the ticket list view, filter by date, and perform a bulk-delete action.For any further information or clarifications, please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com).

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
