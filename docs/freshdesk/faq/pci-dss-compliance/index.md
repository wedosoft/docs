---
sidebar_position: 1
---

# PCI-DSS 규정 준수 FAQ

PCI-DSS 규정 준수에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>PCI Compliance은 무엇인가요?</strong></summary>

PCI compliance refers to the technical and operational standards as defined by the 결제 Card Industry Data Security Standard (PCI-DSS) to secure and protect 신용카드 data. The standards defined under PCI-DSS is developed and managed by the PCI Security Standards Council (PCI SSC).

</details>

<details>
<summary><strong>왜 is PCI compliance 중요인가요?</strong></summary>

Adhering to PCI compliance standards ensures the cardholder data is handled in a secure manner that helps reduce the likelihood of sensitive financial 계정 information stolen or hacked. It helps in avoiding fraudulent activity and mitigate data breaches which is critical for gaining 고객 confidence and trust.In addition, any vendor working with a 서비스 provider using their products or services for accepting card payments or storing/processing/transmitting cardholder data will need to be PCI compliant.

</details>

<details>
<summary><strong>cardholder data (CHD)은 무엇인가요?</strong></summary>

At a minimum, cardholder data consists of the full Permanent 계정 Number (PAN). Cardholder data may also appear in the form of the full PAN plus any of the following: cardholder name, expiration date, and/or 서비스 code for additional data elements that may be transmitted or processed (but not stored) as part of a 결제 transaction.

</details>

<details>
<summary><strong>Are Freshdesk (standalone version) and Freshdesk Omnichannel PCI compliant?</strong></summary>

No. Only Freshdesk (standalone version) via the vault 서비스 is PCI compliant, whereas Freshdesk Omnichannel is not. Although Freshdesk isn’t intended to be used as a 결제 platform, cardholder data as per the PCI-DSS can be stored. The information is encrypted and is made available on-demand only to users who have the privilege to access the data.

</details>

<details>
<summary><strong>Who provided the PCI-DSS certification for Freshdesk?</strong></summary>

Freshdesk’s workflows have been audited and approved by a third-party **Qualified Security Assessor** (QSA).

</details>

<details>
<summary><strong>How does the PCI-DSS encryption work in Freshdesk?</strong></summary>

The information entered in the PCI field is stored in a secure environment outside of Freshdesk.
The Virtual Private Cloud (VPC) used to store the encrypted PCI data is a 서비스 on its own and does not have any peering to any of the Freshdesk’s VPCs. The stored data will not be read/written directly from Freshdesk or any of its subsystems.
When 상담원/admins wish to enter or unmask the data in the PCI field, they will be hitting the secure environment's API directly to store or retrieve encrypted information.

</details>

<details>
<summary><strong>enable the PCI field하는 방법은 무엇인가요?</strong></summary>

This is an on-demand feature. Drop an 이메일 to us to 지원@freshdesk.com and we will ensure the necessary features/설정 (like idle session timeout in 15 mins, IP whitelisting, 비밀번호 policy that adheres to PCI DSS, etc.) are in place and then enable the PCI field for that 계정.Post this, the 계정 Admins can see an option to create a PCI field (namely ‘secure field’)  in the **관리자 > Workflows > Ticket Fields** page.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50001619282/original/u0XDdXPVqiXmiKa6IUZbjcIIrCu8UyhU6g.png?1598009580)
**참고:**- The secure field section will be disabled by default.
- The secure field will be enabled only when IP whitelisting, an idle session, and a concurrent session are enabled and at-least one IP range should be present.
- If the secure fields are enabled and later if you try to disable any of the mandatory sections the secure fields toggle will automatically be turned off.
- Once the secure fields are enabled the IP whitelisting toggle and session preferences section will be disabled.
- You will see a banner stating that idle sessions will default to 15 mins if secure fields are enabled. If you do not set 15 mins in UI, it will be automatically be set from the backend. This will not default to 15 mins in UI on enabling.
- Session replay will be turned off when PCI is enabled.

</details>

<details>
<summary><strong>Is the PCI field a default field or custom field?</strong></summary>

The PCI field is available as a Custom field in Freshdesk. It is available in the drag-and-drop section under **관리자 > Workflows > Ticket Fields**.

</details>

<details>
<summary><strong>Who enters the data in the PCI field?</strong></summary>

There are two ways in which data can be entered into the PCI field.- Customers can fill in their card number in the ticket form directly, or
- 상담원 with access to the field can fill it in.

</details>

<details>
<summary><strong>How can admins restrict or provide access to 상담원 for PCI-DSS?</strong></summary>

By default, access to the PCI field is restricted for all 상담원 and admins alike. On creating a custom role, admins can choose to provide read-only or read and write access to the PCI  field. This custom role can then be applied to agent profiles who need access to the PCI field.

</details>

<details>
<summary><strong>Who can view the contents of the PCI field?</strong></summary>

Admins and 상담원 with the following roles can view the contents of the PCI field- Admins who have access to the PCI field
- 상담원 who have access to edit the PCI field
- 상담원 who have access to view the PCI field

</details>

<details>
<summary><strong>Which product lines in the 지원 BU are PCI Compliant?</strong></summary>

Freshdesk (standalone version) is PCI compliant. As part of the integrated 해결책, Freshworks has built an isolated air-gap environment that is invoked for collecting, storing, and processing Card Holder Data (CHD).

</details>

<details>
<summary><strong>Are standalone Freshchat and standalone Freshcaller PCI compliant?</strong></summary>

Categorically, the answer is 'Not Applicable' as per PCI DSS v.3.2.1 - Clause 4.2 - Never send unprotected PANs by end-user messaging technologies (for example, e-mail, instant messaging, SMS, chat, etc.).
As per PCI DSS, cardholder data (CHD) is not recommended to be exchanged over end-user communication channels such as chat, emails, and calls.Further, in the case of chat and emails, customers can sanitize their conversations through our Data Redaction app. 상담원 can invoke our secure form through interaction in the chat and provide their card information. Likewise, our Caller system can be invoked within the 지원 system and can be used by 상담원 to provide any card-based transaction 지원.Having said that, in both standalone Freshchat and standalone Freshcaller, the data stores are encrypted in transit and at rest. We have also implemented multi-tiered security controls that are also audited as part of SOC 2, ISO 27001, ISO 27701 and Cyber Essentials Plus certifications.

</details>

<details>
<summary><strong>Can you export all sensitive data from Freshdesk (Vault)?</strong></summary>

No. We will not provision exporting data from Freshdesk Vault. On the other hand, the sensitive data can be cleared off by different means. (Deleting a ticket, deleting the 계정, deleting the field, etc.)

</details>

<details>
<summary><strong>How is HIPAA compliant encrypted field different from PCI field?</strong></summary>

- The data entered in the PCI field is stored in a Virtual Private Cloud (VPC) that is not connected to any of Freshdesk’s subsystems. The data, conversations, and histories entered in the encrypted field are stored securely on Amazon’s AWS servers. However, the data inside the encrypted field (HIPAA) is stored within Freshdesk’s systems.
- There is no cap on the number of HIPAA compliant encrypted fields that can be added. On the other hand, only one PCI field can be added.
- HIPAA compliant encrypted fields have specific features that allow administrators to control access privileges, but they cannot be hidden for 상담원. Whereas, the PCI field can be accessed only by 상담원/admins who have read and edit access to perform the functions respectively. For other 상담원, the PCI field will not be visible.

</details>

<details>
<summary><strong>Does the PCI field follow the Primary 계정 Number (PAN) format?</strong></summary>

The PCI field is not restricted to the PAN format. It is a single-line text field on Freshdesk and hence can accept any UTF-8 character.

</details>

<details>
<summary><strong>Can we store Social Security Number (SSN) in the PCI field?</strong></summary>

The PCI field can accept any single line text - this includes any UTF-8 character. Thus, any sensitive or confidential information of customers can be stored in this field.

</details>

<details>
<summary><strong>Will the last 4-digits of the PCI field be visible for all 상담원?</strong></summary>

All digits in the PCI field are masked. This means only 상담원/admins who have access to unmask/edit the PCI field can view the content in the field. Partial masking is not enabled as we don’t want to restrict you to use this field only to store/handle card information and be able to use it to their edge-case requirements.
Also, storing the last 4 digits of the primary 계정 number (PAN) can be done on a separate field and does not violate any PCI DSS compliance rules.

</details>

<details>
<summary><strong>the validity of our Freshdesk’s PCI compliance certification은 무엇인가요?</strong></summary>

It is valid for 1 year from the time of certification and needs to be renewed every year after assessment by a QSA.

</details>

<details>
<summary><strong>Will PCI compliance certification mean that there will be no breaches of data or cardholder information would not be at risk?</strong></summary>

The PCI DSS is not completely secure or hacker-proof. However, they are a standard set of fundamental security controls framed to deal with the most common risk scenarios and known attack vectors identified by the PCI SSC. It’s practically impossible for PCI DSS to anticipate every possible attack scenario. Nonetheless, PCI SSC continues to keep the protocol updated. While PCI SSC is constantly working to monitor threats and improve the industry’s means of dealing with them, ultimately, it’s each organization’s responsibility to provide 신용카드 data security.

</details>

<details>
<summary><strong>Is Freshdesk Level 1 PCI Compliant? What do these levels mean?</strong></summary>

The PCI compliance levels, or tiers, refer to card transaction volume (credit, debit, and prepaid) over a 12-month period.- **PCI Compliance Level 1** - greater than 6M Mastercard or Visa transactions annually, or, a merchant that has experienced an attack resulting in compromised card data, or, a merchant deemed level 1 by a card association.
- **PCI Compliance Level 2** - between 1M and 6M Mastercard or Visa transactions annually.
- **PCI Compliance Level 3** - between 20,000 and 1M e-commerce Mastercard or Visa transactions annually.
- **PCI Compliance Level 4** - less than 20,000 card Mastercard or Visa e-commerce transactions annually, OR up to 1M Mastercard or Visa transactions annually.Levels 2, 3, and 4 all have the same validation requirements - yearly self-assessment using the PCI SSC self-assessment questionnaire, a quarterly network scan by an approved scanning vendor (also available through PCI SSC), and an attestation of compliance form.
For PCI level 1 compliance, the merchant is required to have yearly assessments of compliance by a Qualified Security Assessor (QSA), in addition to the requirements for levels 2, 3, and 4.
Since Freshdesk’s PCI compliance is audited on a yearly basis by an external QSA, we’re level 1 PCI compliant, and those who make over 6 million transactions can use our platform.

</details>

<details>
<summary><strong>Is our PCI compliance better than Zendesk?</strong></summary>

Yes. Freshdesk’s approach to PCI compliance is more comprehensive and allows for additional use cases, unlike Zendesk.
Zendesk's approach to PCI compliance is by redaction - i.e, the 15-19 digit primary 계정 number (or PAN) entered into the Zendesk’s PCI Compliant Ticket Field is redacted to the last 4 digits prior to the data being submitted and stored on Zendesk.
On the contrary, in our approach - we store the PAN in its entirety in a secure vault. 계정 owners in Freshdesk have the authority to define who can unmask and view or edit this information - which is not possible in Zendesk.
Further, as part of our security by design approach, we employ data minimization principles to securely purge cardholder data after 30-days.

</details>

<details>
<summary><strong>inadvertent exposure은 무엇인가요?</strong></summary>

There will always be incidents where irrespective of the measures in place a 고객 or agent inputs a full PAN into locations outside of the dedicated PCI Field on Freshdesk. This is termed as inadvertent exposure.

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
