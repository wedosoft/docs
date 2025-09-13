---
sidebar_position: 5
---

# 사용자 지정 URL 및 CNAME 설정

:::info 문서 목적
이 문서는 "사용자 지정 URL 및 CNAME 설정(Vanity URL & CNAME Setup)" 기능의 개념과 설정 방법을 안내해요.
:::

## 개요

Freshservice 계정 설정 후 `helpdesk.mycompany.com`과 같은 자체 도메인으로 지원 포털의 URL을 맞춤 설정할 수 있어요. 이 기능을 통해 요청자와 지원 상담원이 브랜드화된 URL을 사용해서 지원 포털에 접근할 수 있어, 브랜드 정체성을 강화하고 고객과의 신뢰를 구축할 수 있어요.

이를 위해 DNS 영역 파일에서 CNAME 레코드를 생성해서 사용자 지정 URL을 Freshservice 도메인(mycompany.freshservice.com)으로 가리키도록 설정하면 돼요.

## 일반 계정의 CNAME 설정

### 설정 단계

1. **브랜딩 설정 페이지 이동**
   - **Admin > Account Settings > Service Desk Rebranding**으로 이동해요

2. **포털 정보 입력**
   - **Settings** 섹션에서 원하는 **Service Desk 또는 Portal 이름**을 입력해요
   - 선택한 **Helpdesk 또는 Portal URL**을 입력해요 (예: helpdesk.mycompany.com)

3. **Custom SSL 옵션 활성화**
   - 포털에 Custom SSL이 필요한 경우 **Add Custom SSL** 옵션을 클릭해서 보안 연결을 설정해요

![CNAME 설정 인터페이스](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008956514/original/7KLKtheGFr_x-_DYq7RAg6v6IV3j_FSY2A.png)

4. **CNAME 정보 확인**
   - **Add Custom SSL** 옵션을 클릭하면 사용자 지정 URL 설정에 필요한 **CNAME**과 고유한 **Value**가 표시됩니다

![CNAME 값 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008956521/original/bNXX_1kCjqSvauFmebE38FIK_qOSNiwk-A.png)

5. **DNS 설정**
   - **도메인 서비스 제공업체**에 로그인합니다
   - DNS 영역 파일에서 CNAME 레코드를 생성하여 새 URL이 서비스 데스크 포털을 가리키도록 설정합니다

6. **CNAME 검증**
   - Google의 DNS 검증 도구를 사용하여 사용자 지정 도메인이 올바른 CNAME으로 가리키는지 확인할 수 있습니다
   - 검증 URL: https://toolbox.googleapps.com/apps/dig/#A/

7. **DNS 전파 대기**
   - DNS 변경사항이 전파될 때까지 기다립니다 (24~72시간 소요 가능)
   - 상태가 **In progress**에서 **Active**로 변경됩니다

8. **보안 연결 확인**
   - 지원 포털 방문 시 주소표시줄에 자물쇠 아이콘이 표시되어 보안 연결을 나타냅니다

9. **설정 완료**
   - CNAME 생성 후 **Verify** 버튼을 클릭하여 Freshservice 측에서 설정을 완료합니다

![검증 완료 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008956061/original/YPbXq4CkaDCXOXZ2GERW9-F0ZV1pXtHxEw.png)

## MSP 계정의 CNAME 설정

### MSP용 설정 단계

1. **포털 관리 페이지 이동**
   - **Admin > Channels > Support portal > New portal/Edit portal**로 이동합니다

2. **포털 정보 입력**
   - 원하는 **Service Desk 또는 Portal 이름**을 입력합니다
   - 선택한 **Helpdesk 또는 Portal URL**을 입력합니다

3. **Custom SSL 설정**
   - 포털에 Custom SSL이 필요한 경우 **Add Custom SSL** 옵션을 클릭합니다

4. **CNAME 정보 확인**
   - **Add Custom SSL** 옵션을 클릭하면 사용자 지정 URL에 필요한 **CNAME**과 고유한 **Value**가 표시됩니다

5. **DNS 레코드 생성**
   - 도메인 서비스 제공업체에 로그인하여 DNS 영역 파일에 CNAME 레코드를 생성합니다

6. **전파 및 활성화**
   - DNS 변경사항 전파 후 상태가 **Active**로 변경됩니다

7. **설정 검증**
   - **Verify** 버튼을 클릭하여 설정을 완료합니다

## 중요 고려사항

:::warning CNAME 수정 금지
포털에 제공된 URL의 CNAME은 Freshservice가 SSL 인증서를 특정 URL에 태그하는 식별자 역할을 합니다. 이 CNAME은 어떤 상황에서도 수정해서는 안 됩니다. 수정할 경우 프록시 URL(예: Cloudflare 프록시)이 사용되는 것으로 인식되어 SSL 인증서 갱신이 실패할 수 있습니다.
:::

:::info SSL 인증서 조건
- 사용자 지정 SSL 인증서는 지원 URL과 요청 제출 시 언급된 URL이 동일한 경우에만 작동합니다
- Freshservice 도메인을 변경하면 연결 보안에 영향을 줄 수 있습니다
- Freshservice는 Let's Encrypt로 SSL을 제공하여 보안 통신을 보장합니다
:::

## 추가 지원

### 서브도메인 변경 요청

Freshservice.com 도메인으로 URL의 서브도메인을 변경하려면 다음 정보를 포함하여 support@freshservice.com으로 문의하세요:
- 현재 URL
- 새로운 URL

### 주요 기능

:::tip 브랜드 강화 효과
- **브랜드 일관성**: 조직의 도메인을 사용한 통합된 브랜드 경험
- **신뢰도 향상**: 사용자 친숙한 도메인으로 고객 신뢰 구축
- **보안 연결**: SSL 인증서를 통한 안전한 HTTPS 연결
- **DNS 검증**: 실시간 도메인 설정 상태 확인 가능
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [서비스 데스크 브랜딩 설정](./service-desk-branding)
- [Custom SSL 인증서 설정](./custom-ssl-certificate)
- [포털 접속 및 로그인](./portal-access-login)
-->
