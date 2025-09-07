---
sidebar_position: 3
---

# 사용자 정의 메일박스 설정

:::info 문서 목적
이 문서는 "사용자 정의 메일박스 설정(Setting up a Custom mailbox)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
:::

Freshservice의 서비스 데스크는 매일 수많은 이메일을 송수신하며, Freshservice의 이메일 서버가 모든 수신 및 발신 메일을 처리합니다. 필요에 따라 고객의 자체 메일 서버를 사용할 수도 있습니다.

## 개요

Freshservice에서는 다음과 같은 메일 서버 옵션을 제공합니다:

- **기본 Freshworks 메일 서버**: Freshservice에서 제공하는 표준 메일 서비스
- **사용자 정의 메일 서버**: Google, Microsoft, 기타 IMAP/SMTP 서버

## 설정 단계

### 1. 이메일 설정 페이지 접근

1. Freshservice 계정에 관리자로 로그인합니다.
2. **Admin > Channels > Email > Email Settings and Mailboxes**로 이동합니다.

:::info 멀티 워크스페이스 환경
계정에 여러 워크스페이스가 있는 경우, **Admin > &#123;Workspace name&#125; > Channels > Email > Email Settings and Mailboxes**로 이동하세요.
:::

![이메일 설정 페이지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010035546/original/E_ewQqrPnuhtYjhHPw104MKxz3hztCqNnA.png?1699856659)

### 2. 메일박스 설정 선택

현재 지원 이메일(기본값: `support@yourcompany.freshservice.com`)이 표시됩니다.

- 기존 설정을 변경하려면: **Edit** 클릭
- 새 이메일 설정을 추가하려면: **New Email Settings** 클릭

:::info 멀티 워크스페이스 참조
멀티 워크스페이스 환경에서 이메일 설정과 메일박스 관리에 대한 자세한 내용은 [managing multiple workspaces](https://support.freshservice.com/en/support/solutions/articles/50000005585) 문서를 참조하세요.
:::

![메일박스 목록](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806182/original/mg3iCTGDRDAiaz9Wh6yyl6wg8MKIPsnmag.png?1601389799)

### 3. 기본 정보 입력

다음 정보를 입력합니다:

- **헬프데스크 이름(Name)**: 헬프데스크 표시 이름
- **이메일 주소(Email Address)**: 지원 이메일 주소
- **기본 그룹(Default Group)**: 이 이메일을 통해 들어오는 티켓의 기본 그룹
- **회사(Company)**: MSP 계정인 경우 회사 선택

### 4. 메일 서버 선택

다음 옵션 중 하나를 선택합니다:

- **기본 메일 서버**: Freshworks 이메일 서비스 사용
- **사용자 정의 메일 서버**: Google, Microsoft, 또는 기타 서버

:::tip 기본 메일 서버
기본 메일 서버를 선택하면 Freshworks 이메일 서비스를 사용할 수 있습니다. 포워딩 주소 작동 방식에 대한 자세한 내용은 [이메일 설정 가이드](https://support.freshservice.com/support/solutions/articles/154123-setting-up-your-support-email)를 참조하세요.
:::

## Microsoft 메일 서버 설정

### 설정 과정

1. **Sign in with Microsoft** 버튼을 클릭합니다.

![Microsoft 로그인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942827/original/riVgMQ2Xu5_KVKi2q7GvAdhQGcM_6Zq3Hg.png?1620206065)

2. 사용할 Microsoft 계정을 선택합니다.

![Microsoft 계정 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003385204/original/WheMQNGBol6lhYa6mijD6j3_SvDnAVVQDg.png?1626416433)

3. Freshservice에서 헬프데스크 이메일 설정에 필요한 권한을 **Accept**를 클릭하여 허용합니다.

![권한 승인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806197/original/PvoHxQOcUMHUYvAUdStpWTWIOfV7qN4wMA.png?1601389932)

4. 수신 및 발신 메일 서버 구성을 확인한 후 **Save**를 클릭합니다.

![서버 구성 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806212/original/BGgagyZZWD1Asx51KFmNACGz6JthySf93g.png?1601389994)

5. 이메일 설정을 저장하면 헬프데스크 이메일로 계정 확인을 위한 활성화 이메일이 발송됩니다.

![활성화 이메일](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806213/original/YzKShfp_wOSKQnPRsXo6XsUSLxf-Iyv-pg.png?1601390014)

6. 확인이 완료되면 Microsoft를 사용한 사용자 정의 메일박스 설정이 완료됩니다.

## Google 메일 서버 설정

### 설정 과정

1. **Sign in with Google** 버튼을 클릭하여 Google 메일 서비스를 사용합니다.

![Google 로그인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942786/original/hn44sKeGNxKQk2YTojZWcBgRxnItv76k-g.png?1620205873)

2. 사용할 Google 계정을 선택합니다.

![Google 계정 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942793/original/9npXaXxnOH1_LoauSygpFOxGkSZybr5dSA.png?1620205909)

3. Freshservice에서 헬프데스크 이메일 설정에 필요한 권한을 **Accept**를 클릭하여 허용합니다.

![Google 권한 승인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942801/original/O94AlyXGFB7SQ7PjMkHWpb8USx6vvpzANA.png?1620205934)

4. 수신 및 발신 메일 서버 구성을 확인한 후 **Save**를 클릭합니다.

![Google 서버 구성](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942815/original/RbufGSJMyfmwhVWv1Vb-wriT1Dw4flbiIQ.png?1620206022)

5. 이메일 설정을 저장하면 헬프데스크 이메일로 계정 확인을 위한 활성화 이메일이 발송됩니다.

![Google 활성화 이메일](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002942811/original/ieWnH8Pb_GfYXjXmWHC93ssgCE4oxRaSGw.png?1620205987)

6. 확인이 완료되면 Google을 사용한 사용자 정의 메일박스 설정이 완료됩니다.

## 기타 메일 서버 설정

### 수신 메일 서버 (IMAP) 설정

![IMAP 서버 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806214/original/DZJ2SJCiG7ynZdNYo12oM6p897N4ln1fYg.png?1601390046)

다음 정보를 입력합니다:

- **IMAP 서버 이름**: 이메일 서버의 IMAP 서버 주소
- **포트**: IMAP 서버 포트 번호
- **SSL/TLS 인증**: 이메일 서비스에서 SSL/TLS를 사용하는 경우 체크박스 활성화
- **인증 방식**: Plain 또는 Login Authentication 선택
- **이메일 주소**: 이메일 서버의 이메일 주소
- **비밀번호**: 이메일 서버의 비밀번호

설정 완료 후 **Save**를 클릭합니다.

### 발신 메일 서버 (SMTP) 설정

![SMTP 서버 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001806217/original/RyhZAnpHZxLhF7iFINoD5cyn9Um_It-HZQ.png?1601390079)

다음 정보를 입력합니다:

- **SMTP 서버 이름**: 이메일 서버의 SMTP 서버 주소
- **포트**: SMTP 서버 포트 번호
- **SSL/TLS 인증**: 이메일 서비스에서 SSL/TLS를 사용하는 경우 체크박스 활성화
- **인증 방식**: Plain 또는 Login Authentication 선택
- **이메일 주소**: 이메일 서버의 이메일 주소
- **비밀번호**: 이메일 서버의 비밀번호

설정 완료 후 **Save**를 클릭합니다.

## 문제 해결

### SMTP/IMAP 오류 해결 방법

#### Microsoft 메일박스

메일박스가 연결되지 않는 경우 다음 단계를 따르세요:

1. O365 관리자 자격 증명으로 O365 Admin Center에 로그인합니다.
2. **Users → Active Users**로 이동하여 사용자 정의 메일박스가 구성된 **이메일 주소**를 클릭합니다.
3. 팝업 창에서 **Mail > Manage email apps**로 이동합니다.
4. **IMAP, Authenticated SMTP** 및 아래 언급된 모든 항목이 활성화되어 있는지 확인합니다.

![O365 설정 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011854879/original/xZ5d9rWtknM9DhUHamv6cDrK1qlSPHjxTQ.png?1715863735)

#### Google 및 기타 메일박스

Google 또는 기타 메일박스 계정을 사용하는 경우, POP3, IMAP, SMTP 설정이 활성화되어 있는지 확인하세요.

### 지속적인 문제 해결

문제가 계속 관찰되는 경우 다음 지침에 따라 메일박스를 재구성하세요:

:::warning 재구성 단계
1. Org 포털에서 Default Freshworks 로그인이 활성화되어 있지 않은 경우 활성화합니다.
2. **시크릿 창**에서 Freshservice에 접근하고 **SSO를 사용하지 않고** 로그인하여 브라우저가 활성 세션을 인식하지 않도록 합니다. 필요한 경우 비밀번호 찾기를 사용하세요.
3. 로그인한 후, Sign in with Microsoft / Google / Other를 선택하여 문제를 해결하도록 재구성합니다.
:::

## 주요 포인트

:::success 설정 완료 체크리스트
- [ ] 적절한 메일 서버 유형 선택 (기본, Microsoft, Google, 기타)
- [ ] 필요한 인증 정보 입력
- [ ] SSL/TLS 설정 확인
- [ ] 활성화 이메일 확인
- [ ] 메일 서버 연결 테스트
:::

:::tip 권장사항
- 설정 전 현재 이메일 서버의 IMAP/SMTP 설정을 미리 확인하세요.
- 방화벽이나 보안 설정이 Freshservice 접근을 차단하지 않는지 확인하세요.
- 테스트 이메일을 보내어 설정이 올바르게 작동하는지 확인하세요.
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [이메일 채널 관리](./email-channel-management)
- [메일 템플릿 설정](./email-template-setup)
- [다중 워크스페이스 관리](./multi-workspace-management)
-->
