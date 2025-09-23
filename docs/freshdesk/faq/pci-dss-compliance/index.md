---
sidebar_position: 1
---

# PCI-DSS 규정 준수

이 섹션에서는 PCI-DSS 규정 준수와 관련된 자주 묻는 질문들을 다룹니다.

:::info
각 질문을 클릭하면 상세한 답변을 확인할 수 있습니다.
:::


## 기본 설정 및 구성

<details>
<summary>방법 활성화하다 the PCI field?</summary>

<p><span style={{ fontSize: "16px" }}>This is an on-demand feature. Drop an email to us to support@freshdesk.com and we will ensure the necessary features/settings (like idle session timeout in 15 mins, IP whitelisting, password policy that adheres to PCI DSS, etc.) are in place and then enable the PCI field for that account.</span></p><p dir="ltr" style={{ fontSize: "16px" }}><span dir="ltr" style={{ fontSize: "16px" }}>Post this, the Account Admins can see an option to create a PCI field (namely ‘secure field’) in the <strong>Admin &gt; Workflows &gt; Ticket Fields</strong> page.</span><br /><br /><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><img src="#" width="637" height="352" class="fr-fic fr-dii" /></span></span></span></p><blockquote dir="ltr" style={{ fontSize: "16px" }}><strong><span style={{ fontSize: "16px" }}>Note:</span></strong><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><br /></span></span></span></blockquote><ol><li class="p1"><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>The secure field section will be disabled by default.</span></span></span></li><li class="p1"><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>The secure field will be enabled only when IP whitelisting, an idle session, and a concurrent session are enabled and at-least one IP range should be present.</span></span></span></li><li class="p1"><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>If the secure fields are enabled and later if you try to disable any of the mandatory sections the secure fields toggle will automatically be turned off.</span></span></span></li><li class="p1"><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Once the secure fields are enabled the IP whitelisting toggle and session preferences section will be disabled.</span></span></span></li><li class="p1"><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>You will see a banner stating that idle sessions will default to 15 mins if secure fields are enabled. If you do not set 15 mins in UI, it will be automatically be set from the backend. This will not default to 15 mins in UI on enabling.</span></span></span></li><li class="p1"><span style={{ fontSize: "16px" }}>Session replay will be turned off when PCI is enabled.</span></li></ol>

</details>


## 고급 기능 및 사용법

<details>
<summary>Is the PCI field a default field or custom field?</summary>

<p><span dir="ltr" style={{ fontSize: "16px" }}>The PCI field is available as a Custom field in Freshdesk. It is available in the drag-and-drop section under <strong>Admin &gt; Workflows &gt; Ticket Fields</strong>. </span></p>

</details>


## 관리 및 유지보수

<details>
<summary>무엇인가요 PCI 규정 준수?</summary>

<p><span style={{ fontSize: "16px" }}>PCI compliance refers to the technical and operational standards as defined by the Payment Card Industry Data Security Standard (PCI-DSS) to secure and protect credit card data. The standards defined under PCI-DSS is developed and managed by the PCI Security Standards Council (PCI SSC).</span></p>

</details>

<details>
<summary>왜인가요 PCI 규정 준수 important?</summary>

<p><span style={{ fontSize: "16px" }}>Adhering to PCI compliance standards ensures the cardholder data is handled in a secure manner that helps reduce the likelihood of sensitive financial account information stolen or hacked. It helps in avoiding fraudulent activity and mitigate data breaches which is critical for gaining customer confidence and trust.</span></p><p><span style={{ fontSize: "16px" }}>In addition, any vendor working with a service provider using their products or services for accepting card payments or storing/processing/transmitting cardholder data will need to be PCI compliant.</span></p>

</details>

<details>
<summary>무엇인가요 cardholder data (CHD)?</summary>

<p><span style={{ fontSize: "16px" }}>At a minimum, cardholder data consists of the full Permanent Account Number (PAN). Cardholder data may also appear in the form of the full PAN plus any of the following: cardholder name, expiration date, and/or service code for additional data elements that may be transmitted or processed (but not stored) as part of a payment transaction.</span></p>

</details>

<details>
<summary>Are Freshdesk (standalone version) and Freshdesk Omnichannel PCI compliant?</summary>

<p dir="ltr"><span dir="ltr" style={{ fontSize: "16px" }}>No.&nbsp;</span><span style={{ fontSize: "16px" }}>Only Freshdesk (standalone version) via the vault service is PCI compliant, whereas Freshdesk Omnichannel is not. Although Freshdesk isn’t intended to be used as a billing platform, cardholder data as per the PCI-DSS can be stored. The information is encrypted and is made available on-demand only to users who have the privilege to access the data.</span></p>

</details>

<details>
<summary>Who provided the PCI-DSS certification for Freshdesk?</summary>

<p><span style={{ fontSize: "16px" }}>Freshdesk’s workflows have been audited and approved by a third-party </span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><strong>Qualified Security Assessor</strong></span></span></span><span style={{ fontSize: "16px" }}> (QSA).</span></p>

</details>

<details>
<summary>How does the PCI-DSS encryption work in Freshdesk?</summary>

<p><span style={{ fontSize: "16px" }}>The information entered in the PCI field is stored in a secure environment outside of Freshdesk.</span><br /><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>The Virtual Private Cloud (VPC) used to store the encrypted PCI data is a service on its own and does not have any peering to any of the Freshdesk’s VPCs. The stored data will not be read/written directly from Freshdesk or any of its subsystems.</span></span></span><br /><span style={{ fontSize: "16px" }}>When agents/admins wish to enter or unmask the data in the PCI field, they will be hitting the secure environment's API directly to store or retrieve encrypted information.</span></p>

</details>

<details>
<summary>Who enters the data in the PCI field?</summary>

<p><span style={{ fontSize: "16px" }}>There are two ways in which data can be entered into the PCI field. </span></p><ul><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Customers can fill in their card number in the ticket form directly, or</span></span></span></li><li><span style={{ fontSize: "16px" }}>Agents with access to the field can fill it in. </span></li></ul>

</details>

<details>
<summary>How can admins restrict or provide 접근하다 to agents for PCI-DSS?</summary>

<p><span style={{ fontSize: "16px" }}>By default, access to the PCI field is restricted for all agents and admins alike. On creating a custom role, admins can choose to provide read-only or read and write access to the PCI &nbsp;field. This custom role can then be applied to agent profiles who need access to the PCI field.</span></p>

</details>

<details>
<summary>Who can view the contents of the PCI field?</summary>

<p><span style={{ fontSize: "16px" }}>Admins and agents with the following roles can view the contents of the PCI field</span></p><ul><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Admins who have access to the PCI field</span></span></span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Agents who have access to edit the PCI field</span></span></span></li><li><span style={{ fontSize: "16px" }}>Agents who have access to view the PCI field</span></li></ul>

</details>

<details>
<summary>Which product lines in the Support BU are PCI Compliant?</summary>

<p><span dir="ltr" style={{ fontSize: "16px" }}>Freshdesk (standalone version) is PCI compliant. As part of the integrated solution, Freshworks has built an isolated air-gap environment that is invoked for collecting, storing, and processing Card Holder Data (CHD).</span></p>

</details>

<details>
<summary>Are standalone Freshchat and standalone Freshcaller PCI compliant?</summary>

<p><span dir="ltr" style={{ fontSize: "16px" }}>Categorically, the answer is 'Not Applicable' as per PCI DSS v.3.2.1 - Clause 4.2 - Never send unprotected PANs by end-user messaging technologies (for example, e-mail, instant messaging, SMS, chat, etc.).</span><br /><span dir="ltr" style={{ fontSize: "16px" }}>&nbsp;<br /></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span dir="ltr" style={{ fontSize: "16px" }}>As per PCI DSS, cardholder data (CHD) is not recommended to be exchanged over end-user communication channels such as chat, emails, and calls. &nbsp;</span></span></span><br /><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span dir="ltr" style={{ fontSize: "16px" }}><br /></span></span></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Further, in the case of chat and emails, customers can sanitize their conversations through our Data Redaction app. Agents can invoke our secure form through interaction in the chat and provide their card information. Likewise, our Caller system can be invoked within the Support system and can be used by agents to provide any card-based transaction support.</span></span></span><br /><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><br /></span></span></span><span dir="ltr" style={{ fontSize: "16px" }}>Having said that, in both standalone Freshchat and standalone Freshcaller, the data stores are encrypted in transit and at rest. We have also implemented multi-tiered security controls that are also audited as part of SOC 2, ISO 27001, ISO 27701 and Cyber Essentials Plus certifications.</span></p>

</details>

<details>
<summary>Can you 내보내기 all sensitive data from Freshdesk (Vault)?</summary>

<p><span style={{ fontSize: "16px" }}>No. We will not provision exporting data from Freshdesk Vault. On the other hand, the sensitive data can be cleared off by different means. (Deleting a ticket, deleting the account, deleting the field, etc.)</span></p>

</details>

<details>
<summary>How is HIPAA compliant encrypted field different from PCI field?</summary>

<ul><li><span style={{ fontSize: "16px" }}>The data entered in the PCI field is stored in a Virtual Private Cloud (VPC) that is not connected to any of Freshdesk’s subsystems. The data, conversations, and histories entered in the encrypted field are stored securely on Amazon’s AWS servers. However, the data inside the encrypted field (HIPAA) is stored within Freshdesk’s systems. </span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>There is no cap on the number of HIPAA compliant encrypted fields that can be added. On the other hand, only one PCI field can be added.</span></span></span></li><li><span style={{ fontSize: "16px" }}>HIPAA compliant encrypted fields have specific features that allow administrators to control access privileges, but they cannot be hidden for agents. Whereas, the PCI field can be accessed only by agents/admins who have read and edit access to perform the functions respectively. For other agents, the PCI field will not be visible.</span></li></ul>

</details>

<details>
<summary>Does the PCI field follow the Primary Account Number (PAN) format?</summary>

<p><span style={{ fontSize: "16px" }}>The PCI field is not restricted to the PAN format. It is a single-line text field on Freshdesk and hence can accept any UTF-8 character.</span></p>

</details>

<details>
<summary>Can we store 소셜 보안 Number (SSN) in the PCI field?</summary>

<p><span style={{ fontSize: "16px" }}>The PCI field can accept any single line text - this includes any UTF-8 character. Thus, any sensitive or confidential information of customers can be stored in this field.</span></p>

</details>

<details>
<summary>Will the last 4-digits of the PCI field be visible for all agents?</summary>

<p><span style={{ fontSize: "16px" }}>All digits in the PCI field are masked. This means only agents/admins who have access to unmask/edit the PCI field can view the content in the field. Partial masking is not enabled as we don’t want to restrict you to use this field only to store/handle card information and be able to use it to their edge-case requirements.<br /></span><span style={{ fontSize: "16px" }}>Also, storing the last 4 digits of the primary account number (PAN) can be done on a separate field and does not violate any PCI DSS compliance rules.</span></p>

</details>

<details>
<summary>무엇인가요 the validity of our Freshdesk’s PCI 규정 준수 certification?</summary>

<p><span style={{ fontSize: "16px" }}>It is valid for 1 year from the time of certification and needs to be renewed every year after assessment by a QSA.</span></p>

</details>

<details>
<summary>Will PCI 규정 준수 certification mean that there will be no breaches of data or cardholder information would not be at risk?</summary>

<p><span style={{ fontSize: "16px" }}>The PCI DSS is not completely secure or hacker-proof. However, they are a standard set of fundamental security controls framed to deal with the most common risk scenarios and known attack vectors identified by the PCI SSC. It’s practically impossible for PCI DSS to anticipate every possible attack scenario. Nonetheless, PCI SSC continues to keep the protocol updated. While PCI SSC is constantly working to monitor threats and improve the industry’s means of dealing with them, ultimately, it’s each organization’s responsibility to provide credit card data security.</span></p>

</details>

<details>
<summary>Is Freshdesk Level 1 PCI Compliant? What do these levels mean?</summary>

<p><span style={{ fontSize: "16px" }}>The PCI compliance levels, or tiers, refer to card transaction volume (credit, debit, and prepaid) over a 12-month period. </span></p><ul><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><strong>PCI Compliance Level 1</strong> - greater than 6M Mastercard or Visa transactions annually, or, a merchant that has experienced an attack resulting in compromised card data, or, a merchant deemed level 1 by a card association.</span></span></span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><strong>PCI Compliance Level 2</strong> - between 1M and 6M Mastercard or Visa transactions annually.</span></span></span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><strong>PCI Compliance Level 3</strong> - between 20,000 and 1M e-commerce Mastercard or Visa transactions annually.</span></span></span></li><li><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><strong>PCI Compliance Level 4</strong> - less than 20,000 card Mastercard or Visa e-commerce transactions annually, OR up to 1M Mastercard or Visa transactions annually.</span></span></span></li></ul><p><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Levels 2, 3, and 4 all have the same validation requirements - yearly self-assessment using the PCI SSC self-assessment questionnaire, a quarterly network scan by an approved scanning vendor (also available through PCI SSC), and an attestation of compliance form.<br /></span></span></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>For PCI level 1 compliance, the merchant is required to have yearly assessments of compliance by a Qualified Security Assessor (QSA), in addition to the requirements for levels 2, 3, and 4.<br /></span></span></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Since Freshdesk’s PCI compliance is audited on a yearly basis by an external QSA, we’re level 1 PCI compliant, and those who make over 6 million transactions can use our platform.</span></span></p>

</details>

<details>
<summary>Is our PCI 규정 준수 better than Zendesk?</summary>

<p><span style={{ fontSize: "16px" }}>Yes. Freshdesk’s approach to PCI compliance is more comprehensive and allows for additional use cases, unlike Zendesk. <br /></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Zendesk's approach to PCI compliance is by redaction - i.e, the 15-19 digit primary account number (or PAN) entered into the Zendesk’s PCI Compliant Ticket Field is redacted to the last 4 digits prior to the data being submitted and stored on Zendesk. <br /></span></span></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>On the contrary, in our approach - we store the PAN in its entirety in a secure vault. Account owners in Freshdesk have the authority to define who can unmask and view or edit this information - which is not possible in Zendesk.<br /></span></span></span><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}><span style={{ fontSize: "16px" }}>Further, as part of our security by design approach, we employ data minimization principles to securely purge cardholder data after 30-days.</span></span></span></p><p><br /></p>

</details>

<details>
<summary>무엇인가요 inadvertent exposure?</summary>

<p><span style={{ fontSize: "16px" }}>There will always be incidents where irrespective of the measures in place a customer or agent inputs a full PAN into locations outside of the dedicated PCI Field on Freshdesk. This is termed as inadvertent exposure.</span></p>

</details>

