---
sidebar_position: 1
---

# PCI-DSS 규정 준수 FAQ

PCI-DSS 규정 준수에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>PCI Compliance?이란은 무엇인가요?</strong></summary>

PCI compliance refers 로 technical 그리고 operational standards as defined 에 의해 결제 Card Industry 데이터 보안 Standard (PCI-DSS) 로 secure 그리고 protect 신용카드 데이터. standards defined under PCI-DSS is developed 그리고 managed 에 의해 PCI 보안 Standards Council (PCI SSC).

</details>

<details>
<summary><strong>왜 is PCI compliance 중요?</strong></summary>

Adhering 로 PCI compliance standards ensures cardholder 데이터 is handled 에서 secure manner that helps reduce likelihood 의 sensitive financial 계정 information stolen 또는 hacked. It helps 에서 avoiding fraudulent activity 그리고 mitigate 데이터 breaches which is critical 위해 gaining 고객 confidence 그리고 trust. 에서 addition, any vendor working 와 함께 서비스 provider using their products 또는 services 위해 accepting card payments 또는 storing/processing/transmitting cardholder 데이터 will need 로 be PCI compliant.

</details>

<details>
<summary><strong>cardholder 데이터 (CHD)?이란은 무엇인가요?</strong></summary>

에서 minimum, cardholder 데이터 consists 의 full Permanent 계정 Number (PAN). Cardholder 데이터 may also appear 에서 form 의 full PAN plus any 의 following: cardholder name, expiration date, 그리고/또는 서비스 code 위해 additional 데이터 elements that may be transmitted 또는 processed (하지만 not stored) as part 의 결제 transaction.

</details>

<details>
<summary><strong>Are Freshdesk (standalone version) 그리고 Freshdesk Omnichannel PCI compliant?</strong></summary>

No. Only Freshdesk (standalone version) via vault 서비스 is PCI compliant, whereas Freshdesk Omnichannel is not. Although Freshdesk isn’t intended 로 be used as 결제 platform, cardholder 데이터 as per PCI-DSS can be stored. information is encrypted 그리고 is made 사용 가능한 에-demand only 로 users who have privilege 로 access 데이터.

</details>

<details>
<summary><strong>Who provided PCI-DSS certification 위해 Freshdesk?</strong></summary>

Freshdesk’s workflows have been audited 그리고 approved 에 의해 third-party **Qualified 보안 Assessor** (QSA).

</details>

<details>
<summary><strong>How does PCI-DSS encryption work 에서 Freshdesk?</strong></summary>

information entered 에서 PCI 필드 is stored 에서 secure environment outside 의 Freshdesk. Virtual Private Cloud (VPC) used 로 store encrypted PCI 데이터 is 서비스 에 its own 그리고 does not have any peering 로 any 의 Freshdesk’s VPCs. stored 데이터 will not be read/written directly 에서 Freshdesk 또는 any 의 its subsystems. 언제 상담원/admins wish 로 입력 또는 unmask 데이터 에서 PCI 필드, they will be hitting secure environment's API directly 로 store 또는 retrieve encrypted information.

</details>

<details>
<summary><strong>활성화 PCI 필드?하는 방법은 무엇인가요?</strong></summary>

This is 에-demand feature. Drop 이메일 로 us 로 지원@freshdesk.com 그리고 we will 확인하다 necessary features/설정 (like idle session timeout 에서 15 mins, IP whitelisting, 비밀번호 policy that adheres 로 PCI DSS, etc.) are 에서 place 그리고 그러면 활성화 PCI 필드 위해 that 계정. Post this, 계정 Admins can see option 로 생성 PCI 필드 (namely ‘secure 필드’) 에서 **관리자 > Workflows > Ticket Fields** page. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001619282/original/u0XDdXPVqiXmiKa6IUZbjcIIrCu8UyhU6g.png?1598009580) **참고:** - secure 필드 section will be disabled 에 의해 기본값. - secure 필드 will be enabled only 언제 IP whitelisting, idle session, 그리고 concurrent session are enabled 그리고 에서-least one IP range should be present. - 만약 secure fields are enabled 그리고 later 만약 you try 로 비활성화 any 의 mandatory sections secure fields toggle will automatically be turned off. - Once secure fields are enabled IP whitelisting toggle 그리고 session preferences section will be disabled. - You will see banner stating that idle sessions will 기본값 로 15 mins 만약 secure fields are enabled. 만약 you do not set 15 mins 에서 UI, it will be automatically be set 에서 backend. This will not 기본값 로 15 mins 에서 UI 에 enabling. - Session replay will be turned off 언제 PCI is enabled.

</details>

<details>
<summary><strong>Is PCI 필드 기본값 필드 또는 사용자 정의 필드?</strong></summary>

PCI 필드 is 사용 가능한 as 사용자 정의 필드 에서 Freshdesk. It is 사용 가능한 에서 drag-그리고-drop section under **관리자 > Workflows > Ticket Fields**.

</details>

<details>
<summary><strong>Who enters 데이터 에서 PCI 필드?</strong></summary>

There are two ways 에서 which 데이터 can be entered into PCI 필드. - Customers can fill 에서 their card number 에서 ticket form directly, 또는 - 상담원 와 함께 access 로 필드 can fill it 에서.

</details>

<details>
<summary><strong>How can admins restrict 또는 제공하다 access 로 상담원 위해 PCI-DSS?</strong></summary>

에 의해 기본값, access 로 PCI 필드 is restricted 위해 all 상담원 그리고 admins alike. 에 creating 사용자 정의 role, admins can 선택 로 제공하다 read-only 또는 read 그리고 write access 로 PCI 필드. This 사용자 정의 role can 그러면 be applied 로 agent profiles who need access 로 PCI 필드.

</details>

<details>
<summary><strong>Who can view contents 의 PCI 필드?</strong></summary>

Admins 그리고 상담원 와 함께 following roles can view contents 의 PCI 필드 - Admins who have access 로 PCI 필드 - 상담원 who have access 로 편집 PCI 필드 - 상담원 who have access 로 view PCI 필드

</details>

<details>
<summary><strong>Which product lines 에서 지원 BU are PCI Compliant?</strong></summary>

Freshdesk (standalone version) is PCI compliant. As part 의 integrated 해결책, Freshworks has built isolated air-gap environment that is invoked 위해 collecting, storing, 그리고 processing Card Holder 데이터 (CHD).

</details>

<details>
<summary><strong>Are standalone Freshchat 그리고 standalone Freshcaller PCI compliant?</strong></summary>

Categorically, answer is 'Not Applicable' as per PCI DSS v.3.2.1 - Clause 4.2 - Never send unprotected PANs 에 의해 end-user messaging technologies (위해 example, e-mail, instant messaging, SMS, chat, etc.). As per PCI DSS, cardholder 데이터 (CHD) is not recommended 로 be exchanged over end-user communication channels such as chat, emails, 그리고 calls. Further, 에서 case 의 chat 그리고 emails, customers can sanitize their conversations through our 데이터 Redaction app. 상담원 can invoke our secure form through interaction 에서 chat 그리고 제공하다 their card information. Likewise, our Caller system can be invoked within 지원 system 그리고 can be used 에 의해 상담원 로 제공하다 any card-based transaction 지원. Having said that, 에서 both standalone Freshchat 그리고 standalone Freshcaller, 데이터 stores are encrypted 에서 transit 그리고 에서 rest. We have also implemented multi-tiered 보안 controls that are also audited as part 의 SOC 2, ISO 27001, ISO 27701 그리고 Cyber Essentials Plus certifications.

</details>

<details>
<summary><strong>Can you 내보내기 all sensitive 데이터 에서 Freshdesk (Vault)?</strong></summary>

No. We will not provision exporting 데이터 에서 Freshdesk Vault. 에 other hand, sensitive 데이터 can be cleared off 에 의해 different means. (Deleting ticket, deleting 계정, deleting 필드, etc.)

</details>

<details>
<summary><strong>How is HIPAA compliant encrypted 필드 different 에서 PCI 필드?</strong></summary>

- 데이터 entered 에서 PCI 필드 is stored 에서 Virtual Private Cloud (VPC) that is not connected 로 any 의 Freshdesk’s subsystems. 데이터, conversations, 그리고 histories entered 에서 encrypted 필드 are stored securely 에 Amazon’s AWS servers. However, 데이터 inside encrypted 필드 (HIPAA) is stored within Freshdesk’s systems. - There is no cap 에 number 의 HIPAA compliant encrypted fields that can be added. 에 other hand, only one PCI 필드 can be added. - HIPAA compliant encrypted fields have 특정한 features that allow administrators 로 control access privileges, 하지만 they cannot be hidden 위해 상담원. Whereas, PCI 필드 can be accessed only 에 의해 상담원/admins who have read 그리고 편집 access 로 perform functions respectively. 위해 other 상담원, PCI 필드 will not be visible.

</details>

<details>
<summary><strong>Does PCI 필드 follow Primary 계정 Number (PAN) format?</strong></summary>

PCI 필드 is not restricted 로 PAN format. It is single-line text 필드 에 Freshdesk 그리고 hence can accept any UTF-8 character.

</details>

<details>
<summary><strong>Can we store Social 보안 Number (SSN) 에서 PCI 필드?</strong></summary>

PCI 필드 can accept any single line text - this includes any UTF-8 character. Thus, any sensitive 또는 confidential information 의 customers can be stored 에서 this 필드.

</details>

<details>
<summary><strong>Will last 4-digits 의 PCI 필드 be visible 위해 all 상담원?</strong></summary>

All digits 에서 PCI 필드 are masked. This means only 상담원/admins who have access 로 unmask/편집 PCI 필드 can view content 에서 필드. Partial masking is not enabled as we don’t want 로 restrict you 로 use this 필드 only 로 store/handle card information 그리고 be able 로 use it 로 their edge-case requirements. Also, storing last 4 digits 의 primary 계정 number (PAN) can be done 에 separate 필드 그리고 does not violate any PCI DSS compliance rules.

</details>

<details>
<summary><strong>validity 의 our Freshdesk’s PCI compliance certification?이란은 무엇인가요?</strong></summary>

It is valid 위해 1 year 에서 time 의 certification 그리고 needs 로 be renewed every year after assessment 에 의해 QSA.

</details>

<details>
<summary><strong>Will PCI compliance certification mean that there will be no breaches 의 데이터 또는 cardholder information would not be 에서 risk?</strong></summary>

PCI DSS is not completely secure 또는 hacker-proof. However, they are standard set 의 fundamental 보안 controls framed 로 deal 와 함께 most 일반적인 risk scenarios 그리고 known attack vectors identified 에 의해 PCI SSC. It’s practically impossible 위해 PCI DSS 로 anticipate every possible attack scenario. Nonetheless, PCI SSC continues 로 keep protocol updated. While PCI SSC is constantly working 로 모니터링하다 threats 그리고 improve industry’s means 의 dealing 와 함께 them, ultimately, it’s each organization’s responsibility 로 제공하다 신용카드 데이터 보안.

</details>

<details>
<summary><strong>Is Freshdesk Level 1 PCI Compliant? What do these levels mean?</strong></summary>

PCI compliance levels, 또는 tiers, refer 로 card transaction volume (credit, debit, 그리고 prepaid) over 12-month period. - **PCI Compliance Level 1** - greater than 6M Mastercard 또는 Visa transactions annually, 또는, merchant that has experienced attack resulting 에서 compromised card 데이터, 또는, merchant deemed level 1 에 의해 card association. - **PCI Compliance Level 2** - between 1M 그리고 6M Mastercard 또는 Visa transactions annually. - **PCI Compliance Level 3** - between 20,000 그리고 1M e-commerce Mastercard 또는 Visa transactions annually. - **PCI Compliance Level 4** - less than 20,000 card Mastercard 또는 Visa e-commerce transactions annually, 또는 up 로 1M Mastercard 또는 Visa transactions annually. Levels 2, 3, 그리고 4 all have same validation requirements - yearly self-assessment using PCI SSC self-assessment questionnaire, quarterly network scan 에 의해 approved scanning vendor (also 사용 가능한 through PCI SSC), 그리고 attestation 의 compliance form. 위해 PCI level 1 compliance, merchant is 필수 로 have yearly assessments 의 compliance 에 의해 Qualified 보안 Assessor (QSA), 에서 addition 로 requirements 위해 levels 2, 3, 그리고 4. Since Freshdesk’s PCI compliance is audited 에 yearly basis 에 의해 external QSA, we’re level 1 PCI compliant, 그리고 those who make over 6 million transactions can use our platform.

</details>

<details>
<summary><strong>Is our PCI compliance better than Zendesk?</strong></summary>

Yes. Freshdesk’s approach 로 PCI compliance is more comprehensive 그리고 allows 위해 additional use cases, unlike Zendesk. Zendesk's approach 로 PCI compliance is 에 의해 redaction - i.e, 15-19 digit primary 계정 number (또는 PAN) entered into Zendesk’s PCI Compliant Ticket 필드 is redacted 로 last 4 digits prior 로 데이터 being submitted 그리고 stored 에 Zendesk. 에 contrary, 에서 our approach - we store PAN 에서 its entirety 에서 secure vault. 계정 owners 에서 Freshdesk have authority 로 define who can unmask 그리고 view 또는 편집 this information - which is not possible 에서 Zendesk. Further, as part 의 our 보안 에 의해 design approach, we employ 데이터 minimization principles 로 securely purge cardholder 데이터 after 30-days.

</details>

<details>
<summary><strong>inadvertent exposure?이란은 무엇인가요?</strong></summary>

There will always be incidents where irrespective 의 measures 에서 place 고객 또는 agent inputs full PAN into locations outside 의 dedicated PCI 필드 에 Freshdesk. This is termed as inadvertent exposure.

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
