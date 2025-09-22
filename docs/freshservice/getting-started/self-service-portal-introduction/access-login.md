---
sidebar_position: 3
---

# 서비스 데스크 로그인 및 접근 설정

:::info 문서 목적
이 문서는 "서비스 데스크 로그인 및 접근 설정(Service Desk Login & Access)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
:::

## 개요

고객이 티켓을 생성하고 서비스 데스크 지원 포털을 통해 연락하기 쉽게 만들 수 있어요. 예를 들어, 새 계정을 생성하도록 하는 대신 기존 Google 계정을 사용해서 셀프 서비스 지원 포털에 로그인할 수 있도록 허용할 수 있어요. 또한 기존 Active Directory 자격 증명을 사용해서 로그인하도록 인증할 수도 있어요.

다음은 고객이 지원 포털에 로그인하고 접근하기 쉽게 만드는 3가지 일반 설정 방법이에요.

## 1. 로그인 없이 티켓 제출

### 개념

고객이 긴급한 문제에 직면했을 때 즉시 도움을 받고 싶어해요. 포털에 와서 티켓을 생성하려고 할 때 로그인을 요구하면 고객이 짜증을 낼 수 있어요. 대신 홈 화면에 새 티켓 탭을 표시해서 이메일 주소를 지정해서 바로 티켓을 제출할 수 있도록 할 수 있어요.

### 설정 방법

1. **설정 페이지 이동**
   - **일반 계정**: `Admin > Channel > Other Channel > Support Portal`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Channel > Other Channel > Support Portal`
   - **MSP 모드**: Settings 탭으로 이동

2. **사용자 권한 설정**
   - **User Permissions** 섹션에서 **"Who can submit a new ticket on the portal"** 옵션을 **"Everyone"**으로 선택해요
   - 이 섹션에서 지원 포털의 솔루션을 볼 수 있는 사용자도 정의할 수 있어요

## 2. Google 로그인 사용

### 개념

누군가 지원에 와서 티켓을 생성하려고 할 때 먼저 가입하라는 요청을 받을 수 있어요. 이는 상당히 짜증스러울 수 있으며 좌절감을 줄 수 있어요. 이를 방지하기 위해 기존 Google 계정을 사용해서 로그인할 수 있는 옵션을 제공할 수 있어요.

### 설정 방법

1. **설정 페이지 이동**
   - **일반 계정**: `Admin > Channel > Other Channel > Support Portal`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Channel > Other Channel > Support Portal`
   - **MSP 모드**: Settings 탭으로 이동

2. **Google 로그인 활성화**
   - 사용자가 Google을 사용해서 로그인할 수 있도록 하는 옵션을 선택해요

![Google 로그인 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44786239/original/5JPJh5-EaXtMDB0Yj4ZGuTrs9njGtZkmKw.png)

:::info 2020년 2월 이후 가입자
2020년 2월부터 Freshworks 제품군에 가입한 경우, 추가적인 Google 로그인 설정이 가능합니다.
:::

## 3. Single Sign-On (SSO) 구성

### 개념

고객이 이미 웹사이트나 앱에 로그인한 상태에서 지원 포털에 와서 티켓을 생성하려고 할 때, 다시 로그인하도록 요구하는 것은 매우 불편합니다. 이를 방지하기 위해 SSO(Single Sign-On)을 활성화하여 고객이 다시 로그인하지 않고도 지원에 접근할 수 있도록 할 수 있습니다.

### 설정 방법

1. **보안 설정 페이지 이동**
   - **일반 계정**: `Admin > Account Settings > Helpdesk Security`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Account Settings > Helpdesk Security`

2. **SSO 활성화**
   - **Single Sign-On** 옵션을 ON으로 토글합니다
   - 다음 중 하나를 선택합니다:
     - **SAML SSO**
     - **Simple SSO**

![SSO 설정 인터페이스](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44786355/original/9Q_gBFT5M_BEulS-petEbLfJlTIps2mlRQ.png)

### Freshworks Organization 계정 사용자

:::tip Freshworks Organization 계정
**Freshworks Organization 계정**을 사용하여 Freshservice에 접근하는 경우, Org Security 페이지에서 SSO를 구성할 수 있습니다.
:::

#### Org Security 설정 접근 방법

1. **Freshservice 계정에 로그인**

2. **보안 설정 페이지 이동**
   - **일반 계정**: `Admin > Account Settings > Helpdesk Security`
   - **다중 워크스페이스 계정**: `Admin > Global Settings > Account Settings > Helpdesk Security`

3. **Organization 보안 페이지 접근**
   - **"Manage Helpdesk Security from Freshworks 360 Security"** 링크를 클릭합니다
   - 새 탭에서 Org Security 페이지가 열립니다

![Organization Security 페이지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000624610/original/O8tEqTYT1YcA995z4yuJ0DPxnaim5oWpVA.png)

## 추가 고려사항

:::warning 계정별 설정 차이
- **2020년 2월 이후 가입자**: Freshworks 제품군 사용자는 **SAML 2.0 Single Sign-On**을 구성할 수 있습니다
- **Organization 계정 사용자**: Freshworks Organization 계정으로 SSO 설정을 별도로 관리할 수 있습니다
:::

## 주요 기능

:::info 사용자 편의성 향상
- **즉시 접근**: 로그인 없이 긴급 티켓 제출 가능
- **간편 로그인**: 기존 Google 계정으로 빠른 접근
- **통합 인증**: SSO를 통한 끊김 없는 사용자 경험
- **보안 강화**: 기존 인증 시스템과의 통합으로 보안성 확보
:::

