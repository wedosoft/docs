---
sidebar_position: 1
---

# 이메일 지원 채널 설정

이메일을 통해 티켓을 자동 생성하고 관리할 수 있는 이메일 지원 채널 설정 방법입니다.

:::info 이메일 지원 채널 개요
고객이 이메일을 보내면 자동으로 티켓이 생성되어 체계적인 고객 지원이 가능합니다.
다양한 이메일 서버와 연동하여 안정적인 티켓 생성 환경을 구축할 수 있습니다.
:::

## 이메일 전달 규칙 설정

### 서비스 데스크 이메일 전달 구성

### 서비스 데스크 이메일 전달 구성

서비스 데스크 이메일 주소에 전송된 이메일이 Freshservice로 적절히 라우팅되어 티켓 생성 및 관리가 이루어지도록 전달 규칙을 설정합니다.

**1단계: 이메일 설정 접근**
1. 관리자로 Freshservice 계정에 로그인
2. **Admin > Email Settings > Support Email**로 이동

**2단계: 전달 규칙 구성**
1. 이메일 제공업체 선택 (Office 365, Gmail, Exchange 등)
2. 해당 이메일 시스템의 특정 설정 지침 따르기
3. 제공된 Freshservice 전달 주소로 자동 전달 설정

**3단계: 구성 테스트**
1. 서비스 데스크 주소로 테스트 이메일 발송
2. Freshservice에서 티켓 생성 확인
3. 모든 이메일 형식과 첨부 파일이 보존되는지 확인

:::warning 중요 고려사항
- 이메일 전달이 원본 발신자 정보를 보존하는지 확인
- Freshservice 이메일을 허용하도록 스팸 필터 구성
- 이메일 전송을 위한 적절한 인증(SPF, DKIM) 설정
:::

:::tip 제공업체별 설정
상세한 제공업체별 지침은 해당 이메일 시스템 문서를 참조하거나 Freshservice 지원팀에 문의하세요.
:::

## 고객 이메일 주소 추가

### 티켓 생성용 이메일 주소 설정

고객이 이메일을 보내서 티켓을 생성할 수 있는 이메일 주소를 추가하는 전체 과정입니다.

**1단계: 이메일 설정으로 이동**
1. **Admin > Email Settings > Support Email** 이동
2. **Add Email Address** 또는 **New Support Email** 클릭

**2단계: 이메일 주소 구성**
- **이메일 주소**: 고객이 사용할 이메일 주소 입력 (예: support@yourcompany.com)
- **부서**: 이 이메일에서 오는 티켓을 처리할 부서 선택
- **그룹 할당**: 티켓의 기본 그룹 선택
- **우선순위**: 들어오는 티켓의 기본 우선순위 수준 설정

**3단계: 이메일 서버 구성**

설정 방법을 선택하세요:

| 옵션 | 설명 | 적합한 상황 |
|------|------|-------------|
| **이메일 전달** | Freshservice 전달 주소로 이메일 전달 | 기존 이메일 서버 유지 |
| **IMAP/POP3** | 직접 이메일 서버 접근 구성 | 고급 제어가 필요한 경우 |
| **OAuth 통합** | Office 365/Google Workspace 연동 | 클라우드 이메일 서비스 사용 |

**4단계: 활성화 프로세스**
1. Freshservice가 지원 주소로 활성화 이메일 발송
2. 이메일의 활성화 링크 클릭
3. Freshservice 관리자 패널에 활성화 코드 입력
4. 이메일 주소가 "Active"로 표시되는지 확인

**5단계: 티켓 생성 테스트**
1. 새 지원 주소로 테스트 이메일 발송
2. 올바른 정보로 티켓이 생성되는지 확인
3. 고객에게 자동 응답이 발송되는지 확인

:::tip 모범 사례
- 전문적이고 기억하기 쉬운 이메일 주소 사용
- 이메일 서명 및 자동 응답 설정
- 제목이나 내용 기반의 이메일 라우팅 규칙 구성
- 적절한 이메일 인증(SPF, DKIM, DMARC) 확인
:::

## 이메일 주소 활성화

### 서비스 데스크 이메일 활성화 절차

설정된 서비스 데스크 이메일 주소를 활성화하여 실제 티켓 생성이 가능하도록 하는 과정입니다.

**1단계: 활성화 이메일 확인**
1. Freshservice에서 지원 이메일 주소로 발송한 활성화 이메일 확인
2. 스팸 폴더 포함하여 이메일 수신함 전체 검색
3. 발신자: noreply@freshservice.com 또는 유사한 주소

**2단계: 활성화 링크 클릭**
1. 활성화 이메일 내의 **"Activate Email"** 링크 클릭
2. 새 브라우저 창에서 Freshservice 활성화 페이지 열림
3. 로그인이 필요한 경우 관리자 계정으로 로그인

**3단계: 활성화 코드 입력**
1. 이메일에 포함된 활성화 코드 복사
2. Freshservice 관리자 패널의 이메일 설정으로 이동
3. 해당 이메일 주소 옆의 활성화 코드 입력 필드에 붙여넣기
4. **"Verify"** 또는 **"Activate"** 버튼 클릭

**4단계: 활성화 상태 확인**
1. 이메일 주소 목록에서 상태가 **"Active"**로 표시되는지 확인
2. 녹색 체크 표시 또는 "활성화됨" 레이블 확인
3. 필요시 페이지 새로고침

:::success 활성화 완료
이메일 주소가 성공적으로 활성화되어 고객 이메일로부터 티켓 생성이 가능합니다.
:::

## 실무 활용 예시

### 상황 1: 다부서 지원 체계 구축
**목표**: 부서별로 다른 이메일 주소를 통한 티켓 분류
**방법**:
1. 부서별 이메일 주소 설정 (it@company.com, hr@company.com)
2. 각 이메일별 담당 그룹 자동 할당
3. 부서별 특화된 자동 응답 메시지 설정
4. 우선순위 및 SLA 규칙 차별화

**결과**: 효율적인 업무 분산 및 전문화된 지원

### 상황 2: 글로벌 고객 지원
**목표**: 지역별 시간대를 고려한 이메일 지원 체계
**방법**:
1. 지역별 이메일 주소 설정 (asia@company.com, europe@company.com)
2. 지역별 언어 설정 및 자동 응답
3. 시간대별 에이전트 그룹 할당
4. 이메일 서명에 현지 연락처 포함

**결과**: 24시간 글로벌 고객 지원 체계 완성

## 문제 해결

### 자주 발생하는 문제

#### 문제: 활성화 이메일이 도착하지 않음
**원인**: 스팸 필터 또는 이메일 전달 설정 문제
**해결**:
1. 스팸/정크 메일 폴더 확인
2. Freshservice 도메인을 화이트리스트에 추가
3. 이메일 전달 규칙 재확인
4. 관리자 패널에서 활성화 이메일 재발송

:::success 해결 완료
화이트리스트 등록 후 활성화 이메일이 정상 수신됩니다.
:::

#### 문제: 이메일로 티켓이 생성되지 않음
**원인**: 전달 규칙 설정 오류 또는 인증 문제
**해결**:
1. 이메일 전달 설정 재확인
2. SPF, DKIM 레코드 확인
3. 방화벽 설정에서 Freshservice IP 허용
4. 테스트 이메일로 단계별 확인

#### 문제: 첨부 파일이 누락됨
**원인**: 첨부 파일 크기 제한 또는 형식 제한
**해결**:
1. 첨부 파일 크기 제한 확인 (일반적으로 20MB)
2. 허용된 파일 형식 확인
3. 바이러스 검사 통과 여부 확인
4. 압축 파일로 변환하여 재전송

<p>Activating your service desk email address is crucial for enabling email-to-ticket functionality. Follow this step-by-step process:</p><p><br /></p><p><strong>Step 1: Initial Setup</strong></p><ul><li>Complete the email address configuration in <strong>Admin &gt; Email Settings</strong></li><li>Ensure your email forwarding or server settings are correct</li><li>Save the configuration</li></ul><p><br /></p><p><strong>Step 2: Activation Email</strong></p><ul><li>Freshservice automatically sends an activation email to your support address</li><li>Check your email inbox (and spam folder) for the activation message</li><li>The email will come from <strong>noreply@freshservice.com</strong></li></ul><p><br /></p><p><strong>Step 3: Complete Activation</strong></p><ul><li>Click the <strong>Activate Email Address</strong> link in the email</li><li>This redirects you to a Freshservice activation page</li><li>Enter the activation code shown in the email</li><li>Click <strong>Activate</strong> to complete the process</li></ul><p><br /></p><p><strong>Step 4: Verify Activation</strong></p><ul><li>Return to <strong>Admin &gt; Email Settings &gt; Support Email</strong></li><li>Check that your email address shows as <strong>"Active"</strong></li><li>Send a test email to verify ticket creation</li></ul><p><br /></p><p><strong>Troubleshooting Activation Issues:</strong></p><ul><li><strong>No activation email received:</strong> Check spam folders and email forwarding settings</li><li><strong>Activation link expired:</strong> Request a new activation email from the settings page</li><li><strong>Invalid activation code:</strong> Ensure you're using the latest activation email</li></ul><p><br /></p><p><strong>Manual Activation Alternative:</strong></p><p>If automated activation fails:</p><ul><li>Contact Freshservice support with your domain and email details</li><li>Provide proof of email ownership (DNS records or admin access)</li><li>Support team can manually activate your email address</li></ul>

---

## Freshservice에서 활성화 이메일을 받지 못하는 이유는?

<p>Not receiving activation emails from Freshservice can occur due to several reasons. Here's a comprehensive troubleshooting guide:</p><p><br /></p><p><strong>Common Reasons and Solutions:</strong></p><p><br /></p><p><strong>1. Email Filtering and Spam</strong></p><ul><li><strong>Check spam/junk folders</strong> in your email client</li><li><strong>Add freshservice.com to your safe senders list</strong></li><li><strong>Check email rules</strong> that might filter or redirect emails</li><li><strong>Review corporate email security</strong> settings that may block automated emails</li></ul><p><br /></p><p><strong>2. Email Forwarding Issues</strong></p><ul><li><strong>Verify forwarding is working</strong> by sending a test email</li><li><strong>Check forwarding rules</strong> aren't blocking system emails</li><li><strong>Ensure forwarding preserves</strong> original recipient information</li><li><strong>Test direct email delivery</strong> without forwarding</li></ul><p><br /></p><p><strong>3. DNS and Domain Configuration</strong></p><ul><li><strong>Verify MX records</strong> are correctly configured</li><li><strong>Check SPF records</strong> include Freshservice domains</li><li><strong>Ensure DMARC policy</strong> doesn't block Freshservice emails</li><li><strong>Validate domain ownership</strong> in your DNS settings</li></ul><p><br /></p><p><strong>4. Email Server Configuration</strong></p><ul><li><strong>IMAP/POP3 settings:</strong> Verify server details and credentials</li><li><strong>OAuth connections:</strong> Check if authentication has expired</li><li><strong>Firewall settings:</strong> Ensure Freshservice IPs aren't blocked</li></ul><p><br /></p><p><strong>Step-by-Step Resolution:</strong></p><p><br /></p><p><strong>Step 1: Immediate Checks</strong></p><ul><li>Search all email folders for emails from freshservice.com</li><li>Check quarantine or security folders</li><li>Contact your IT team about email filtering</li></ul><p><br /></p><p><strong>Step 2: Request New Activation Email</strong></p><ul><li>Go to <strong>Admin &gt; Email Settings</strong></li><li>Find your email address and click <strong>Resend Activation</strong></li><li>Wait 10-15 minutes for delivery</li></ul><p><br /></p><p><strong>Step 3: Contact Support</strong></p><p>If issues persist:</p><ul><li>Email support@freshservice.com with your domain details</li><li>Include error messages or screenshots</li><li>Provide your email configuration details</li><li>Request manual activation if necessary</li></ul><p><br /></p><p><strong>Prevention for Future:</strong></p><ul><li>Whitelist all Freshservice email domains</li><li>Set up proper email authentication</li><li>Test email delivery before going live</li><li>Document your email configuration for troubleshooting</li></ul>

---

## 지원 이메일 주소 활성화 시 '활성화 코드가 유효하지 않음' 오류가 발생하는 이유는?

<p>The "Activation code invalid" error occurs when there's a mismatch or issue with the activation process. Here's how to resolve this common issue:</p><p><br /></p><p><strong>Common Causes and Solutions:</strong></p><p><br /></p><p><strong>1. Timing Issues</strong></p><ul><li><strong>Activation code expired:</strong> Codes typically expire after 24-48 hours</li><li><strong>Solution:</strong> Request a new activation email from the admin panel</li><li><strong>Multiple activation attempts:</strong> Previous codes become invalid when new ones are generated</li><li><strong>Solution:</strong> Always use the most recent activation email</li></ul><p><br /></p><p><strong>2. Copy-Paste Errors</strong></p><ul><li><strong>Extra spaces or characters:</strong> Common when copying codes manually</li><li><strong>Solution:</strong> Click the activation link directly instead of copying the code</li><li><strong>Character encoding issues:</strong> Some email clients may alter special characters</li><li><strong>Solution:</strong> Try opening the email in a different client or browser</li></ul><p><br /></p><p><strong>3. Email Configuration Changes</strong></p><ul><li><strong>Modified email settings:</strong> Changes after activation email was sent</li><li><strong>Solution:</strong> Complete current activation before making setting changes</li><li><strong>DNS or domain changes:</strong> Domain modifications can invalidate codes</li><li><strong>Solution:</strong> Wait for DNS propagation and request new activation</li></ul><p><br /></p><p><strong>Step-by-Step Resolution:</strong></p><p><br /></p><p><strong>Step 1: Verify Current Status</strong></p><ul><li>Check if the email address shows as "Pending Activation" in admin panel</li><li>Confirm you're using the latest activation email received</li><li>Check email timestamp to ensure code hasn't expired</li></ul><p><br /></p><p><strong>Step 2: Request Fresh Activation</strong></p><ul><li>Go to <strong>Admin &gt; Email Settings &gt; Support Email</strong></li><li>Find the email address and click <strong>Resend Activation</strong></li><li>Check both inbox and spam folders for the new email</li></ul><p><br /></p><p><strong>Step 3: Use Direct Link Method</strong></p><ul><li>Don't manually enter the activation code</li><li>Click the <strong>"Activate Email Address"</strong> link directly in the email</li><li>Ensure you're logged into the correct Freshservice account</li></ul><p><br /></p><p><strong>Step 4: Clear Browser Issues</strong></p><ul><li>Clear browser cache and cookies</li><li>Try activation in an incognito/private browser window</li><li>Use a different browser if issues persist</li></ul><p><br /></p><p><strong>Alternative Activation Methods:</strong></p><p><br /></p><p><strong>Method 1: Manual Code Entry</strong></p><ul><li>Go to the activation page manually</li><li>Enter the code exactly as shown in email</li><li>Ensure no extra spaces or line breaks</li></ul><p><br /></p><p><strong>Method 2: Contact Support</strong></p><p>If all else fails:</p><ul><li>Email support@freshservice.com</li><li>Include screenshots of the error</li><li>Provide your domain and email address details</li><li>Request manual activation assistance</li></ul><p><br /></p><p><strong>Prevention Tips:</strong></p><ul><li>Complete activation immediately after receiving the email</li><li>Don't make email configuration changes during activation process</li><li>Keep activation emails until process is complete</li><li>Test email delivery before attempting activation</li></ul>

---

## Freshservice에서 자체 메일 서버를 사용해서 이메일을 송수신할 수 있나요?

<p>Yes, Freshservice supports using your own mail servers for sending and receiving emails. This gives you more control over email delivery and branding. Here's how to set it up:</p><p><br /></p><p><strong>Benefits of Using Your Own Mail Server:</strong></p><ul><li><strong>Brand consistency:</strong> Emails appear to come from your domain</li><li><strong>Better deliverability:</strong> Established domain reputation helps avoid spam filters</li><li><strong>Enhanced security:</strong> Direct control over email security policies</li><li><strong>Compliance:</strong> Meet specific industry email requirements</li></ul><p><br /></p><p><strong>Setup Requirements:</strong></p><p><br /></p><p><strong>1. Incoming Email (IMAP/POP3)</strong></p><ul><li><strong>Email server details:</strong> Server address, port, encryption settings</li><li><strong>Authentication:</strong> Username and password for the support mailbox</li><li><strong>SSL/TLS support:</strong> Secure connection to your email server</li><li><strong>Folder configuration:</strong> Specify folders for processed emails</li></ul><p><br /></p><p><strong>2. Outgoing Email (SMTP)</strong></p><ul><li><strong>SMTP server settings:</strong> Server, port, authentication method</li><li><strong>Security protocols:</strong> SSL/TLS encryption support</li><li><strong>From address:</strong> Configure sender email addresses</li><li><strong>Rate limiting:</strong> Ensure compliance with server sending limits</li></ul><p><br /></p><p><strong>Configuration Steps:</strong></p><p><br /></p><p><strong>Step 1: Prepare Email Infrastructure</strong></p><ul><li>Set up dedicated mailboxes for support emails</li><li>Configure IMAP access and SMTP sending</li><li>Ensure proper DNS records (MX, SPF, DKIM, DMARC)</li><li>Test email server connectivity and authentication</li></ul><p><br /></p><p><strong>Step 2: Configure Incoming Email</strong></p><ul><li>Navigate to <strong>Admin &gt; Email Settings &gt; Support Email</strong></li><li>Choose <strong>Add Email Address &gt; Use your own email server</strong></li><li>Enter IMAP/POP3 server details:
<ul><li>Server address and port</li><li>Username and password</li><li>Encryption method (SSL/TLS)</li><li>Polling frequency</li></ul></li><li>Test connection and save settings</li></ul><p><br /></p><p><strong>Step 3: Configure Outgoing Email</strong></p><ul><li>Go to <strong>Admin &gt; Email Settings &gt; Outbound Email</strong></li><li>Select <strong>Use your own SMTP server</strong></li><li>Enter SMTP configuration:
<ul><li>SMTP server and port</li><li>Authentication credentials</li><li>Security settings</li><li>From address configuration</li></ul></li><li>Test email sending functionality</li></ul><p><br /></p><p><strong>Advanced Configuration Options:</strong></p><p><br /></p><p><strong>1. Email Routing Rules</strong></p><ul><li>Set up department-specific email addresses</li><li>Configure routing based on subject line or sender</li><li>Implement priority-based email processing</li></ul><p><br /></p><p><strong>2. Security Settings</strong></p><ul><li>Configure email encryption requirements</li><li>Set up email archiving and retention</li><li>Implement additional spam filtering</li></ul><p><br /></p><p><strong>3. Integration Features</strong></p><ul><li>Email signature management</li><li>Auto-responder configuration</li><li>Email template customization</li></ul><p><br /></p><p><strong>Troubleshooting Common Issues:</strong></p><ul><li><strong>Connection timeouts:</strong> Check firewall settings and port accessibility</li><li><strong>Authentication errors:</strong> Verify credentials and authentication methods</li><li><strong>SSL/TLS issues:</strong> Ensure certificate validity and protocol compatibility</li><li><strong>Delivery problems:</strong> Check DNS records and email server configuration</li></ul><p><br /></p><p><strong>Best Practices:</strong></p><ul><li>Use dedicated support email addresses</li><li>Implement proper email authentication</li><li>Monitor email server performance and capacity</li><li>Regular backup of email configurations</li><li>Test failover procedures for email continuity</li></ul>

---

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [자동화 설정](./automation-rules)
- [워크플로 설정](./workflow-automator)  
- [에이전트 관리](./agent-management)
-->
