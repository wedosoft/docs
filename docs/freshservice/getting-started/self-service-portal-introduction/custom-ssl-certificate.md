---
sidebar_position: 2
---

# 사용자 지정 SSL 인증서 설정

:::info 문서 목적
이 문서는 "사용자 지정 SSL 인증서 설정(Custom SSL Certificate Configuration)" 기능의 개념과 설정 방법을 안내합니다.
:::

## 개요

Freshservice는 freshservice.com 도메인에서 지원 포털을 사용하는 모든 사용자에게 기본 와일드카드 SSL을 제공합니다. 이는 가입 시 설정한 기본 Freshservice URL(예: yourcompany.freshservice.com)을 계속 사용하는 한 사용할 수 있습니다.

그러나 헬프데스크 포털에 사용자 지정 도메인 이름(예: helpdesk.yourcompany.com)을 지정한 경우에는 기본 SSL이 작동하지 않습니다. 이 경우 도메인 이름과 함께 Freshservice에서 제공하는 사용자 지정 SSL 인증서를 구성해야 합니다.

## 사전 요구사항

포털 URL을 사용자 지정 도메인으로 구성하기 전에 다음 사항을 확인해야 합니다:

### 1. CNAME 레코드에서 프록시 비활성화

DNS 공급업체/등록 기관이 CNAME 레코드에서 프록시를 자동으로 활성화하는 경우, 사용자 지정 도메인이 대기 상태로 유지될 수 있습니다. CNAME 레코드에서 프록시를 비활성화해야 합니다. Freshworks는 맞춤형 Cloudflare 설정을 사용하여 사용자 지정 호스트명에 대한 요청이 완전히 보호되도록 합니다.

### 2. Cloudflare 사용자를 위한 설정

Cloudflare를 프록시/DNS 공급업체로 사용하는 경우 서브도메인을 일시적으로 차단해야 합니다:

1. **Cloudflare 대시보드에서 설정**
   - `Overview > Quick Actions > Zone Hold`로 이동합니다

2. **서브도메인 차단 해제**
   - **"Also prevent subdomains"** 옵션의 체크를 해제합니다
   - 이미 체크가 해제되어 있다면 Zone Hold를 해제하기 위한 추가 작업은 필요하지 않습니다

3. **사용자 지정 도메인 생성 완료 후**
   - 필요한 경우 옵션을 다시 활성화할 수 있습니다
   - **참고**: 영역 및 서브도메인의 소유권은 변경되지 않습니다

### 3. CAA 레코드 구성

도메인에 CAA 레코드를 추가한 경우, 서브도메인의 레코드에 **pki.goog**와 **letsencrypt.org**를 추가해야 합니다.

## 일반 계정의 사용자 지정 SSL 설정

### 설정 단계

1. **브랜딩 설정 페이지 이동**
   - **일반 계정**: `Admin > Account Settings > Service Desk Rebranding`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Account Settings > Service Desk Rebranding`

2. **포털 정보 입력**
   - **Settings** 섹션에서 **Service Desk 또는 Portal 이름**을 입력합니다
   - **Helpdesk/Portal URL**을 입력합니다

3. **Custom SSL 추가**
   - 포털에 Custom SSL을 아직 설정하지 않은 경우, **Add Custom SSL** 옵션을 클릭하여 보안 연결을 설정할 수 있습니다

![Custom SSL 설정 인터페이스](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002505910/original/Fam64LNNm2ilOcVRXAikpbyyUEdAtb-1ag.png)

4. **CNAME 정보 확인**
   - **"Add Custom SSL"** 옵션을 클릭하면 대화 상자가 나타나며 **CNAME**과 고유한 **Value**가 표시됩니다

![CNAME 값 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002505911/original/nwFE5aWxiozukbM4gwQqeCeYY3ZbyjnZqg.png)

5. **DNS 레코드 생성**
   - 도메인 서비스 공급업체에 로그인합니다
   - DNS 파일 영역에서 CNAME 레코드를 생성하여 새 URL이 서비스 데스크 포털을 가리키도록 설정합니다

6. **DNS 전파 및 활성화**
   - DNS 변경이 전파되면 상태가 **"In progress"**에서 **"Active"**로 변경됩니다 (24~72시간 소요)
   - 지원 포털 방문 시 주소 표시줄에 자물쇠 아이콘이 표시됩니다

7. **설정 검증**
   - CNAME 생성 후 **Verify** 버튼을 클릭하여 Freshservice 측에서 설정을 완료합니다

![검증 완료 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002505909/original/spzmwoKnpzmxNNOgWJWRgc70ybeQqnTYZQ.png)

## MSP 계정의 사용자 지정 SSL 설정

### MSP용 설정 단계

1. **포털 관리 페이지 이동**
   - **일반 계정**: `Admin > Channels > Support portal > New portal/Edit portal`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Channels > Support portal > New portal/Edit portal`

2. **포털 정보 입력**
   - **Service Desk 또는 Portal 이름**을 입력합니다
   - **Helpdesk/Portal URL**을 입력합니다

3. **Custom SSL 추가**
   - 포털에 Custom SSL을 아직 설정하지 않은 경우 **Add Custom SSL** 옵션을 클릭합니다

4. **CNAME 정보 확인**
   - **"Add Custom SSL"** 옵션을 클릭하면 대화 상자가 나타나며 **CNAME**과 고유한 **Value**가 표시됩니다

5. **DNS 레코드 생성**
   - 도메인 서비스 공급업체에 로그인하여 DNS 파일 영역에 CNAME 레코드를 생성합니다

6. **전파 및 활성화**
   - DNS 변경이 전파되면 상태가 **"Active"**로 변경됩니다 (24~72시간 소요)

7. **설정 검증**
   - CNAME 생성 후 **Verify** 버튼을 클릭하여 설정을 완료합니다

## 중요 사항

:::warning 도메인 일관성 유지
사용자 지정 SSL 인증서는 지원 URL과 요청 제출 시 언급된 URL이 동일한 경우에만 작동합니다. Freshservice를 다른 도메인을 가리키도록 재구성하면 연결이 더 이상 안전하지 않습니다.
:::

:::info SSL 제공업체
Freshservice는 Let's Encrypt로 SSL을 제공합니다.
:::

## 주요 기능

:::tip 보안 강화 효과
- **HTTPS 보안**: 모든 데이터 전송이 암호화되어 보안성 확보
- **신뢰성 향상**: 브라우저 주소표시줄의 자물쇠 아이콘으로 사용자 신뢰 구축
- **사용자 지정 도메인**: 조직의 도메인을 사용한 전문적인 포털 운영
- **자동 갱신**: Let's Encrypt를 통한 자동 인증서 갱신
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [사용자 지정 URL 및 CNAME 설정](./vanity-url-setup)
- [서비스 데스크 브랜딩 설정](./service-desk-branding)
- [포털 접속 및 로그인](./portal-access-login)
-->
