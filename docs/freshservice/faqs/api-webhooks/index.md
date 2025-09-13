# API & Webhooks

API와 웹훅을 활용한 시스템 통합부터 문제 해결까지, 실무에서 자주 발생하는 질문들과 해결 방법을 정리했습니다.

<details>
<summary>Microsoft Teams용 Servicebot의 업그레이드된 API로 업데이트 출시</summary>

업데이트를 통해 얻을 수 있는 기능들을 소개합니다.

## 새로운 기능

### 1. 전체 직장인을 위한 Servicebot 자동 설치

직원들이 Microsoft Teams에 봇을 수동으로 설치할 필요가 없어졌습니다. 조직에서 Servicebot을 활성화하면 모든 직원의 Teams에 자동으로 봇이 설치됩니다.

[자세히 알아보기](https://support.freshservice.com/en/support/solutions/articles/50000005624-bring-richer-ticket-context-into-your-collaboration-tools)

**참고:** MS Teams에서 Servicebot 앱을 차단하지 않았는지 확인하세요. 차단되어 있으면 자동 설치가 실패합니다.

### 2. 승인 및 티켓 대화 관리 개선

앱 간 전환을 줄이고 에이전트와 승인자가 Microsoft Teams 내에서 티켓을 효율적으로 관리할 수 있도록 개선되었습니다.

향상된 티켓 및 서비스 요청 컨텍스트:

- 승인 관리 시 동료 승인자의 조치 내역 확인 가능
- 티켓에 첨부된 최신 대화를 빠르게 파악

[자세히 알아보기](https://support.freshservice.com/en/support/solutions/articles/50000005624-bring-richer-ticket-context-into-your-collaboration-tools)

### 3. 에이전트에게 온콜 관리 알림 전달 (곧 출시)

온콜 에이전트는 MS Teams에서 바로 인시던트를 확인, 에스컬레이션, 해결하고 메모를 추가할 수 있습니다. 온콜 에이전트가 인시던트 처리 시 전체 그룹과 이해관계자가 자동으로 업데이트됩니다. 원활한 협업을 통해 더 빠른 인시던트 해결이 가능합니다.

[지금 앱 업데이트](https://www.freshworks.com/apps/freshservice/msteams-freshservice/)

**참고:** 앞으로 모든 Servicebot과 Virtual Agent 기능은 v2 API 기반으로 구축됩니다. 위의 기능들과 향후 추가될 기능을 사용하려면 Microsoft Teams, Freshservice 관리자 설정, 또는 온콜 관리 모듈의 알림 탭에서 앱 업데이트를 승인해야 합니다.

## 앱 업데이트 방법

**참고:** Freshservice 관리자이면서 Azure 관리자인 경우에만 업데이트를 실행할 수 있습니다.

### 모든 플랜

관리자는 MS Teams 앱을 통해 Servicebot 알림으로 전달되는 "승인" 버튼을 볼 수 있습니다. 버튼을 클릭하여 업데이트하세요.

### 엔터프라이즈 플랜

1. Freshservice > 설정 > Virtual Agent ("채널" 섹션 하위)로 이동
2. Microsoft Teams 하위의 "더 많은 채널 연결" 패널에서 "승인" 버튼을 확인할 수 있습니다
3. 버튼을 클릭하여 업데이트

### 비엔터프라이즈 플랜

1. Freshservice > 설정 > 앱 ("자동화 및 생산성" 섹션 하위) > 앱 관리로 이동
2. 알림 구성이 나열된 섹션에서 "승인" 버튼을 확인할 수 있습니다
3. 버튼을 클릭하여 업데이트

### 온콜 관리 모듈 사용자

1. Freshservice > 관리자 > 온콜 일정 > 알림 규칙으로 이동
2. MS Teams 테넌트의 관리자는 알림을 받기 위해 MS Teams 계정을 승인해야 합니다

</details>

<details>
<summary>워크플로 자동화와 웹훅 사용</summary>

## 웹훅이란 무엇인가요?

웹훅은 특정 이벤트가 발생할 때 트리거되는 애플리케이션 또는 웹 서비스에 대한 "콜백"입니다. 특정 업데이트, 변경 또는 작업이 발생하면 웹훅을 사용하여 외부 애플리케이션으로 데이터를 푸시할 수 있습니다.

워크플로 자동화를 사용하여 특정 이벤트가 발생할 때 웹훅을 트리거하는 워크플로를 만들 수 있습니다.

## 웹훅 호출로 할 수 있는 일

자동화를 사용하여 티켓에서 특정 이벤트가 발생할 때 특정 작업을 실행하는 워크플로를 만들 수 있습니다. 자동화를 사용하여 Freshservice 내에서 업데이트, 수정, 알림 전송 및 작업 실행이 가능합니다. 예를 들어, 티켓 우선순위를 업데이트하거나 에스컬레이션 이메일을 보낼 수 있습니다.

웹훅은 외부 애플리케이션이나 도구에서 작업을 트리거하려는 경우에 유용합니다. 웹훅을 사용할 수 있는 예시 시나리오:

| 수행하려는 작업 | 찾아야 할 조건 | 웹훅이 호출해야 할 대상 |
|---|---|---|
| 고객이 티켓에 응답할 때 SMS/문자 메시지 전송 | 고객이 티켓에 응답 (또는 댓글 추가) | 타사 SMS 도구로 댓글 내용 전송 |
| 제품 반품 요청이 업데이트될 때 재고 업데이트 | 티켓 카테고리(사용자 정의 필드)가 "제품 반품"으로 업데이트 | 매장 재고에서 제품 정보 업데이트 |
| 내부 제품 관리 도구와 기능 요청 상태 동기화 | "기능 요청" 유형 티켓의 상태 업데이트 | 티켓 정보로 제품 관리 도구 업데이트 |
| 나쁜 고객 만족도 평점을 받을 때 경보음 및 사이렌 울리기 | 고객 피드백 수신, 평점이 "좋지 않음" | 이 웹훅으로 트리거되는 스마트 전구와 사이렌 음향 보드 커스터마이징 |

## 자동화로 웹훅 요청 설정하는 방법

다음 사용 사례를 고려해 보겠습니다:
"티켓이 변경 요청일 때 자동으로 변경을 생성"

1. 워크플로 자동화를 사용하여 새 워크플로를 생성합니다. 웹훅을 트리거해야 하는 이벤트와 조건을 드래그 앤 드롭합니다.
2. 작업에서 드롭다운에서 "웹훅 트리거" 옵션을 선택합니다.

### 콜백 요청 유형 선택

각 타사 앱이 다른 방식으로 요청 유형을 사용할 수 있지만, 대부분의 애플리케이션은 표준 방법을 따릅니다:

- **GET** 요청: 일반적으로 하나 또는 모든 리소스를 검색하는 데 사용
- **POST** 요청: 보통 새 리소스를 생성
- **PUT 및 PATCH** 요청: 리소스를 업데이트하는 데 사용
- **DELETE** 요청: 보통 리소스를 삭제하는 데 사용

이 예시에서는 변경 모듈에 새 변경을 생성해야 하므로 POST 요청을 생성합니다.

### 콜백 URL 지정

웹훅에 구성된 애플리케이션의 콜백 URL을 지정합니다. [동적 플레이스홀더](https://support.freshservice.com/support/solutions/articles/157150-using-dynamic-placeholders-in-your-canned-responses)를 사용하여 URL을 동적으로 만들 수 있습니다.

예를 들어, `http://yourapp.com/yourInfo?email=[user email]` 형태의 콜백 URL을 전달하려면 사용자 이메일 부분을 `{{"{{requestor.email}}"}}` 플레이스홀더로 대체할 수 있습니다.

## 웹훅 테스트

복잡한 웹훅 호출이 있는 대규모 워크플로가 있는 경우 테스트가 필수입니다. 웹훅을 테스트하기 위해 워크플로를 활성화하는 것은 최적의 테스트 방법이 아닙니다. 대신 워크플로 자동화 내에서 웹훅을 직접 테스트할 수 있습니다.

예를 들어, 변경 모듈에서 변경 티켓을 생성하는 웹훅을 설정하고 웹훅 테스트 버튼을 누르면 테스트가 성공할 경우 변경 모듈에 테스트 티켓이 생성됩니다.

오류가 발생하는 API 요청은 오류 유형을 식별하는 데 도움이 되는 적절한 HTTP 상태 코드를 반환합니다. 각 코드의 의미를 이해하려면 [이 표](https://api.freshservice.com/v2/#error)를 사용할 수 있습니다.

**참고:** 플레이스홀더는 웹훅 테스트에서 지원되지 않습니다.

### 인증 및 인코딩

1. 인증이 필요한 경우 **인증 필요** 체크박스를 활성화할 수 있습니다. 사용자명/비밀번호 또는 API 키를 인증에 사용할 수 있습니다.
2. 리소스 애플리케이션이 지원하는 요청 인코딩(JSON, XML 또는 XML-Encoded)을 선택합니다.

### 콘텐츠 옵션

- **간단한 콘텐츠**: 이 웹훅에서 원하는 티켓 속성 목록을 단순히 전송하려면 간단한 콘텐츠 옵션을 선택합니다.
- **고급**: 전송되는 콘텐츠를 사용자 정의하려면 고급을 선택합니다.
  - 고급 옵션을 사용하면 사용자 정의 API 요청을 작성할 수 있습니다. 이러한 요청은 이전 단계에서 선택한 형식으로 인코딩되어야 합니다.
  - requestb.in 또는 postman - REST 클라이언트(Google Chrome 확장 프로그램)를 사용하여 API를 테스트할 수 있습니다.

- `{{"{{Triggered event}}"}}` 플레이스홀더는 웹훅에서만 사용할 수 있으며 규칙을 트리거한 이벤트의 이름을 반환합니다.

### 웹훅 콜백 요청 제한

시간당 사용할 수 있는 웹훅 요청 수는 1000건으로 제한됩니다. 상태 코드가 200-299 사이이면 콜백이 성공이고, 300-399 사이의 상태 코드는 콜백 리디렉션으로 간주됩니다.

콜백이 실패하거나(2xx 및 3xx 이외의 상태 코드) 15초 내에 응답을 받지 못하면 웹훅이 3, 5, 9, 17분 간격으로 최대 4번 자동으로 재시도됩니다.

위 자동화가 활성화되면 "변경 요청" 유형으로 들어오는 모든 티켓이 변경 모듈에서 자동으로 변경을 생성합니다.

</details>

<details>
<summary>업그레이드된 API 소개 - Freshservice 지원</summary>

강력한 통합 구축, 최종 사용자 포털 사용자 정의, 여러 애플리케이션 간 데이터 공유 - Freshservice API는 이 모든 것과 그 이상을 가능하게 합니다.

향상된 API 일관성과 개선된 경험으로 더 나은 지원을 제공하기 위해, **2023년 5월 31일**까지 이전 버전(API V1)을 사용 중단하고 업그레이드된 버전(API V2)으로 이전합니다.

**2023년 5월 31일**까지 **API V1** 엔드포인트 사용을 중단하고 **API V2**로 완전히 전환하여 이 사용 중단으로 인한 중단을 방지하세요.

## API V2의 새로운 기능

### → 새롭고 향상된 API

사용자 정의 객체, 직원 온보딩, 프로젝트, 비즈니스 시간, 구매 주문, 공급업체, 제품, 위치 등을 위한 새로운 API가 이제 API V2에서 사용할 수 있습니다. [자세한 정보](https://api.freshservice.com/#whats_new)

### → 더 높은 속도 제한

API 안정성과 확장성을 개선하기 위해 시간 기반에서 분 기반 속도 제한으로 이동하고 있습니다. 호출을 하는 데 사용되는 에이전트 수나 IP 주소 수에 관계없이 계정 전체 기준으로 이러한 제한을 계속 적용할 예정입니다. [자세한 정보](https://api.freshservice.com/#rate_limit)

### → 개선된 오류 처리

명확한 HTTP 상태 코드로 오류를 식별하여 잘못된 API 요청을 빠르고 정확하게 수정하세요. [자세한 정보](https://api.freshservice.com/#error)

## 무엇을 해야 하나요?

### 영향을 받는 영역

다음 기능에서 해당 API V2 엔드포인트로 API V1 호출을 대체하세요. 사용 중단 날짜 이후에 다음 기능에서 API V1을 계속 사용하면 작동이 중단되고 V1에 대한 모든 요청이 실패합니다.

- → 워크플로 자동화 (웹 요청 노드 및 "웹훅 트리거" 작업 노드)
- → 사용자 정의 앱
- → 포털 사용자 정의
- → Freshservice API를 사용하여 개발된 모든 사용자 정의 서비스 또는 미들웨어

### 버전 1 API 식별

[API V2 문서](https://api.freshservice.com/)와 [솔루션 문서](https://support.freshservice.com/en/support/solutions/articles/50000006003-deprecating-v1-apis-for-freshservice)를 참조하여 새로운 엔드포인트를 이해하고 **2023년 5월 31일** 사용 중단 날짜 이전에 기존 API V1 코드베이스를 API V2로 마이그레이션하세요.

## 마이그레이션하지 않으면 어떻게 되나요?

**2023년 5월 31일** 이후 API V1 엔드포인트에 액세스할 수 없게 되어 워크플로와 사용자 정의가 중단될 수 있습니다.

## 도움이 필요하신가요?

마이그레이션에 대한 질문이 있거나 API 호출을 V2 엔드포인트로 마이그레이션하는 동안 문제가 발생하면 저희 팀에서 도움을 드릴 수 있습니다. 추가 지원이 필요하시면 support@freshservice.com 또는 고객 성공 관리자에게 문의하세요.

</details>

<details>
<summary>Freshservice의 v1 API 사용 중단</summary>

[2022년 11월](https://community.freshworks.com/product-updates/freshservice-release-notes-nov-2022-26812#Deprecation+of+password-based+authentication+for+API+v2) 릴리스 중 발표한 내용에 따라, API V1 호출을 해당 API V2 호출로 대체하기 위한 몇 가지 제품 개선 사항을 적용했습니다.

## 이 변경사항이 나에게 영향을 미치나요?

다음 작업 중 하나에 API V1 엔드포인트를 사용한 경우 이 사용 중단의 영향을 받습니다:

- 워크플로 구성
- 포털 사용자 정의
- Freshservice 인스턴스와 사용자 정의 애플리케이션 간 상호작용

자세한 정보는 [이 솔루션 문서](https://support.freshservice.com/en/support/solutions/articles/50000004220-introducing-upgraded-apis-for-freshservice)를 참조하세요.

## 영향을 받는 모듈

### 1. 워크플로 자동화

API V1 권장 태그가 API V1 엔드포인트를 사용하는 모든 자동화에 표시됩니다.

#### 워크플로 자동화를 업데이트하는 방법

1. **관리자 → 자동화 및 생산성 → 워크플로 자동화**로 이동
2. "API 업데이트 권장" 태그가 있는 워크플로 자동화를 클릭
3. 워크플로를 열면 v1 엔드포인트를 사용하는 모든 노드가 빨간색 알림으로 강조 표시됩니다
4. 빨간색 알림을 선택하여 해당 V1 URL에 대한 권장 V2 URL을 확인합니다. '✓' 아이콘을 클릭하여 URL을 업데이트합니다. 마지막으로 **완료** 버튼을 클릭하여 해당 노드를 업데이트합니다
5. 강조 표시된 모든 노드에 대해 이 과정을 반복하고 워크플로 자동화를 저장합니다

자세한 정보는 [여기](https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860) 상세 마이그레이션 가이드를 참조하세요.

### 2. 포털 사용자 정의

1. **관리자 → 서비스 데스크 리브랜딩 → 사용자 정의**로 이동합니다. **홈페이지 디자이너** 드롭다운에서 v1 엔드포인트를 사용하는 모든 섹션이 강조 표시됩니다.
2. 특정 섹션(알림 표시 확인)을 선택하여 v1 엔드포인트가 있는지 식별하고 해당 v2 엔드포인트로 업데이트합니다.
3. 포털 사용자 정의에서 모든 v1 엔드포인트를 교체한 후 **저장** 또는 **포털 게시**를 클릭합니다

자세한 정보는 [여기](https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860) 상세 마이그레이션 가이드를 참조하세요.

### 3. 사용자 정의 앱

1. **관리자 → 앱**으로 이동
2. v1 엔드포인트를 사용하는 사용자 정의 앱을 확인하고 해당 엔드포인트를 v2로 업데이트합니다
3. 자세한 정보는 [여기](https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860) 상세 마이그레이션 가이드를 참조하세요

## 2023년 5월 31일 이전에 구성을 업데이트하지 않으면 어떻게 되나요?

v1 엔드포인트가 있는 모든 워크플로 자동화, 포털 사용자 정의 및 사용자 정의 앱이 작동을 중단하고 구성이 실패하기 시작합니다.

</details>

<details>
<summary>Freshservice의 Zapier 통합을 사용하여 300개 이상의 앱과 통합</summary>

Zapier는 웹 애플리케이션 간의 격차를 해소하고 애플리케이션 간 작업을 쉽게 자동화할 수 있는 강력한 통합 플랫폼입니다.

## Freshservice-Zapier 통합 작동 방식

Zapier 계정을 생성하여 Freshservice-Zapier 통합을 활성화할 수 있습니다. 이제 Zap을 생성하여 Freshservice를 수백 개의 사용 가능한 애플리케이션과 통합할 수 있습니다. Zap의 규칙(트리거)이 '앱 A'에서 충족될 때마다 원하는 작업이 '앱 B'에서 자동으로 수행됩니다.

## Zapier 통합 설정 빠른 가이드

1. [https://zapier.com/](https://zapier.com/)을 방문하여 계정에 가입합니다.
2. 계정을 생성하고 확인한 후 화면 상단의 "Make a Zap" 탭을 클릭합니다.
3. Freshservice를 앱 중 하나로 포함하는 Zap을 생성할 때 Zapier에 Freshservice 계정을 추가해야 합니다.
4. "Freshservice 계정 연결"을 클릭합니다.
5. 계정 이름을 제공합니다. 이는 Zapier에서 Freshservice 계정을 식별하는 데 도움이 됩니다.
6. Freshservice 계정의 하위 도메인을 입력합니다.
7. 계정의 API 키를 입력합니다. API 키를 가져오려면:
   - Freshservice 계정에 로그인합니다.
   - 오른쪽 상단 모서리의 프로필 사진을 클릭하고 "프로필 설정"을 선택합니다.
   - API 키는 오른쪽 창에 표시됩니다.
8. '계속'을 클릭합니다.
9. Zapier가 정보를 확인하고 "계정이 작동 중입니다" 메시지를 표시합니다. '계속'을 클릭하여 Zap을 진행합니다.

</details>

<details>
<summary>모든 플랜에서 API의 속도 제한은 무엇인가요?</summary>

## v1의 경우:

시간당 API 호출 수는 1000건으로 제한됩니다. 제한에 도달한 후 API 요청이 수신되면 Freshservice는 오류 응답을 제공합니다. 응답 헤더의 "retry-after" 값은 다른 API 요청을 보내기 전에 기다려야 하는 시간을 알려줍니다.

자세한 내용은 API v1 문서를 참조하세요: [https://api.freshservice.com/](https://api.freshservice.com/)

## v2의 경우:

2020년 9월 1일 이후에 생성된 Freshservice 계정은 분 단위 속도 제한을 사용합니다. 제한은 Freshservice 플랜에 따라 다릅니다. 특정 API 작업에는 전체 제한 내에서 하위 제한도 있습니다. 이 제한은 호출을 하는 데 사용되는 에이전트 수나 IP 주소와 같은 요소에 관계없이 계정 전체 기준으로 적용됩니다.

시간 기반에서 분 기반 속도 제한으로 이동하여 API 안정성과 확장성을 개선합니다. 호출을 하는 데 사용되는 에이전트 수나 IP 주소 수에 관계없이 계정 전체 기준으로 이러한 제한을 계속 적용할 예정입니다.

**플랜별 속도 제한:**
- **Starter**: 분당 100건
- **Growth**: 분당 200건  
- **Pro**: 분당 400건
- **Enterprise**: 분당 700건

2020년 9월 1일 이전에 생성된 계정은 결국 분 단위 속도 제한으로 마이그레이션됩니다. 마이그레이션이 완료될 때까지 이전 제한이 계속 적용됩니다.

자세한 내용은 API v2 문서를 참조하세요: [https://api.freshservice.com/v2/](https://api.freshservice.com/v2/)

</details>

<details>
<summary>API를 사용하여 티켓 필드를 가져오는 방법은?</summary>

다음 curl 명령을 사용하여 필요한 티켓 필드를 가져올 수 있습니다:

```bash
curl -v -u user@yourcompany.com:test -X GET 'https://domain.freshservice.com/api/v2/ticket_fields'
```

curl 명령에서 이메일 주소와 비밀번호를 사용하고 싶지 않다면 아래와 같이 이메일 주소 대신 API 키를, 비밀번호로 X를 사용할 수도 있습니다:

```bash
curl -v -u API키:X -X GET 'https://domain.freshservice.com/api/v2/ticket_fields'
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/v2/#get_all_ticket_fields](https://api.freshservice.com/v2/#get_all_ticket_fields)

</details>

<details>
<summary>Freshservice API에서 사용되는 날짜-시간 형식은 무엇인가요?</summary>

날짜 필드의 입력은 다음 형식 중 하나일 것으로 예상됩니다:

- YYYY-MM-DD
- YYYY-MM-DDTHH:MM
- YYYY-MM-DDTHH:MMZ
- YYYY-MM-DDTHH:MM:SS
- YYYY-MM-DDTHH:MM:SSZ
- YYYY-MM-DDTHH:MM:SS±hh:mm
- YYYY-MM-DDTHH:MM:SS±hh
- YYYY-MM-DDTHH:MM:SS±hhmm

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/v2/#schema](https://api.freshservice.com/v2/#schema)

</details>

<details>
<summary>API를 사용하여 사용자 정보를 가져오는 방법은?</summary>

다음 curl 명령을 사용할 수 있습니다:

```bash
curl -v -u user@yourcompany.com:test -X GET 'https://domain.freshservice.com/api/v2/requesters/777'
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/v2/#view_a_requester](https://api.freshservice.com/v2/#view_a_requester)

</details>

<details>
<summary>API를 사용하여 첨부 파일이 있는 티켓을 생성하는 방법은?</summary>

다음 curl 명령을 사용할 수 있습니다:

```bash
curl -v -u user@yourcompany.com:test \
  -F "helpdesk_ticket[attachments][][resource]=@/path/to/attachment1.ext" \
  -F "helpdesk_ticket[attachments][][resource]=@/path/to/attachment2.ext" \
  -F "helpdesk_ticket[email]=example@example.com" \
  -F "helpdesk_ticket[subject]=Ticket Title" \
  -F "helpdesk_ticket[description]=this is a sample ticket" \
  -X POST https://domain.freshservice.com/helpdesk/tickets.json
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/#create_ticket_with_attachment](https://api.freshservice.com/#create_ticket_with_attachment)

</details>

<details>
<summary>API를 사용하여 모든 서비스 항목을 볼 수 있나요?</summary>

다음 curl 명령을 사용할 수 있습니다:

```bash
curl -u user@yourcompany.com:test \
  -H "Content-Type: application/json" \
  -X GET https://domain.freshservice.com/catalog/items.json?page=2
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/#view_all_service_items](https://api.freshservice.com/#view_all_service_items)

</details>

<details>
<summary>API를 사용하여 솔루션 카테고리를 생성하는 방법은?</summary>

다음 curl 명령을 사용할 수 있습니다:

```bash
curl -u user@yourcompany.com:test \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{ "solution_category": { "name":"API", "description":"API related documents" }}' \
  https://domain.freshservice.com/solution/categories.json
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/#create_solution_category](https://api.freshservice.com/#create_solution_category)

</details>

<details>
<summary>API로 생성할 때 우선순위 값을 "4"로 설정해도 티켓이 낮은 우선순위로 생성되는 이유는?</summary>

계정에서 우선순위 매트릭스가 활성화되어 있으면 API에서 전달된 값이 무시되고 우선순위 매트릭스가 티켓의 우선순위를 설정합니다. 이를 원하지 않는 경우 **관리자 > 우선순위 매트릭스**로 이동하여 비활성화할 수 있습니다.

</details>

<details>
<summary>API를 사용하여 티켓의 사용자 정의 필드를 업데이트할 수 있나요?</summary>

예, 가능합니다. 자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/v2/#update_ticket_priority](https://api.freshservice.com/v2/#update_ticket_priority)

</details>

<details>
<summary>API를 사용하여 티켓에 자산을 연결할 수 있나요?</summary>

다음 curl 명령을 사용할 수 있습니다:

```bash
curl -u (credentials) \
  -H "Content-Type:application/json" \
  -d '{"helpdesk_ticket": {}, "associate_ci": {"serial_no":"99RSH32","name":"SALES-SERV","user": "tom@outerspace.com"}}' \
  -X PUT https://domain.freshservice.com/helpdesk/tickets/123.json
```

자세한 정보는 다음을 참조하세요: [https://api.freshservice.com/#associate_a_ci_to_a_ticket](https://api.freshservice.com/#associate_a_ci_to_a_ticket)

</details>

<details>
<summary>웹훅이란 무엇인가요?</summary>

웹훅은 특정 이벤트가 발생할 때 트리거되는 애플리케이션 또는 웹 서비스에 대한 콜백입니다. 이는 워크플로 자동화를 사용하여 구성됩니다. 즉, 서비스 데스크에서 특정 업데이트, 변경 또는 작업이 발생하도록 웹훅을 설정할 수 있으며, 지정한 정보를 원하는 애플리케이션으로 자동으로 푸시합니다.

</details>

<details>
<summary>부모-자식 연결을 위한 API가 있나요?</summary>

예, 이 링크([https://api.freshservice.com/v2/#create_child_ticket](https://api.freshservice.com/v2/#create_child_ticket))에서 언급된 API를 사용하여 기존 인시던트 티켓에 대한 자식 티켓을 생성할 수 있습니다.

</details>

<details>
<summary>API를 사용하여 변경과 티켓을 연결하는 방법은?</summary>

티켓을 생성하면서 API를 통해 변경을 티켓에 연결하는 것이 가능합니다. 아래의 Curl 명령을 참조하세요:

```bash
curl -u user@yourcompany.com:password \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"helpdesk_ticket": {"subject": "Test Ticket", "description": "Test Description", "change": 123}}' \
  https://domain.freshservice.com/api/v2/tickets
```

이 [링크](https://api.freshservice.com/#create_ticket)를 사용하여 티켓을 생성하고 변경과 연결하세요.

</details>

<details>
<summary>API 키는 어디에서 찾을 수 있나요?</summary>

1. 지원 포털에 로그인합니다
2. 포털 오른쪽 상단 모서리의 프로필 사진을 클릭합니다
3. 프로필 설정 페이지로 이동합니다
4. 오른쪽의 위임 승인 섹션 아래에 API 키가 표시됩니다

</details>

<details>
<summary>앱을 활성화하면 API 호출이 소비되나요?</summary>

예, 특정 마켓플레이스 앱은 API를 소비합니다. 사용하는 앱이 API 호출을 소비하는지에 대한 자세한 정보가 필요하면 support@freshservice로 지원팀에 문의하세요. 사용하는 앱이 API 호출을 소비하는지 확인하여 알려드릴 수 있습니다.

</details>

<details>
<summary>사용 가능한 API 제한을 확인하는 방법은?</summary>

API V1을 사용하는 경우 제한에 도달한 후 Freshservice는 오류 응답을 제공합니다. 응답 헤더의 "retry-after" 값은 다른 API 요청을 보내기 전에 기다려야 하는 시간을 알려줍니다.

V2를 사용하여 API 제한을 확인하려면 모든 API 요청에 대한 응답으로 반환되는 다음 HTTP 헤더를 확인하여 현재 속도 제한 상태를 확인할 수 있습니다.

</details>

<details>
<summary>포털 대신 이메일이나 API를 통해 CAB에 승인을 제출할 수 있나요?</summary>

Freshservice에서는 특히 서비스 요청과 변경 요청에 관한 승인 알림이 일반적으로 이메일을 통해 전송됩니다. 그러나 API를 사용하여 변경 요청을 승인하는 것은 불가능합니다. CAB 구성원은 이메일로 전송된 승인 링크를 클릭하여 변경을 승인할 수 있습니다.

## 현재 프로세스:

현재 Freshservice에서 변경 요청을 승인하는 유일한 방법은 공개 승인 링크를 공유하는 것입니다. 링크는 이메일을 통해 승인자에게 전송되며, 승인 또는 거부하기 전에 요청의 세부 사항을 검토하기 위해 클릭해야 합니다. 그러나 이는 여러 화면을 탐색하고 로그인해야 하는 추가 단계를 추가합니다. 또한 일부 승인자는 공개 승인 링크 공유에 불편함을 느낄 수 있습니다.

## 새로운 개선사항:

Freshservice는 이러한 문제를 해결하고 승인 프로세스를 간소화하기 위한 새로운 개선사항을 도입했습니다. 이 개선사항을 통해 변경 및 서비스 요청 승인자가 이메일 받은편지함에서 직접 요청에 응답할 수 있습니다. 공개 승인 링크를 공유하는 대신 Freshservice는 승인 수신자에게 이메일을 보내며, 여기서 특정 키워드로 회신하여 요청을 승인하거나 거부할 수 있습니다. 이렇게 하면 승인 프로세스가 간소화되고 승인자에게 더 편리해집니다.

## 이메일 승인의 이점:

이메일 승인의 중요한 장점 중 하나는 Freshservice에 로그인하지 않고도 이해관계자가 요청을 승인하거나 거부할 수 있다는 것입니다. 이 기능은 승인자가 조직 외부에 있거나 시스템에 액세스할 수 없는 경우에 특히 유용합니다. 또한 요청을 승인하거나 거부하기 위해 여러 화면을 탐색할 필요가 없어 프로세스가 더 효율적입니다.

자세한 내용은 [이메일을 통한 서비스 요청 및 변경 승인 : Freshservice](https://support.freshservice.com/en/support/solutions/articles/50000004955)를 참조하세요.

</details>

<details>
<summary>임시 에이전트가 로그인하지 않고 API에 액세스할 수 있나요?</summary>

임시 에이전트는 API에 액세스하기 전에 인스턴스에 로그인해야 합니다. 사용자가 로그인하지 않고 시스템에 액세스하려고 하면 시스템에 로그인하라는 메시지가 표시됩니다.

</details>

<details>
<summary>문제 자동화에서 웹훅을 트리거하는 옵션이 있나요?</summary>

예, 웹훅은 문제 자동화에서 지원됩니다.

</details>

<details>
<summary>Freshservice에서 티켓에 추가된 마지막 공개 메모에 액세스하여 웹훅을 통해 전송하는 방법은?</summary>

웹훅을 사용하여 티켓에 추가된 마지막 공개 메모에 액세스하려면 웹훅 페이로드에서 **`{{ticket.latest_public_comment}}`** 플레이스홀더를 사용할 수 있습니다. 웹훅이 트리거되면 이 플레이스홀더가 티켓에 추가된 마지막 공개 메모로 대체되며, 결과 페이로드에 이 정보가 포함됩니다.

예를 들어, 티켓에 공개 메모가 추가될 때마다 Slack 채널로 알림을 보내는 웹훅을 사용하는 경우, 페이로드에 `{{ticket.latest_public_comment}}` 플레이스홀더를 포함하여 마지막 공개 메모가 알림에 포함되도록 할 수 있습니다.

이렇게 하면 팀이 시스템 간 전환 없이 Freshservice의 최신 개발 상황을 파악할 수 있습니다.

</details>

<details>
<summary>다중 작업공간 설정에서 Freshservice API와 마켓플레이스 앱은 어떻게 작동하나요?</summary>

*(2022년 12월 12일 이전에 가입한 계정에만 해당)*

## Freshservice API

각 작업공간은 고유한 다음 항목을 가질 수 있습니다:

- 티켓
- 문제
- 변경
- 릴리스
- 에이전트 그룹
- 자산
- 소프트웨어
- 계약
- 구매 주문
- 비즈니스 시간
- 솔루션
- 서비스 카탈로그
- SLA 정책
- 사용자 정의 객체
- 미리 작성된 응답
- 공지사항
- 감사 로그

단일 작업공간 계정에서는 작업공간 ID를 전달하지 않고도 위 모듈을 기반으로 하는 API가 예상대로 계속 작동합니다. 그러나 여러 작업공간을 추가했고 다음 영역에서 위 모듈에 대해 Freshservice API를 사용하는 경우:

- → 워크플로 자동화 (웹 요청 노드 및 "웹훅 트리거" 작업 노드)
- → 사용자 정의 앱
- → 포털 사용자 정의
- → Freshservice API를 사용하여 개발된 모든 사용자 정의 서비스 또는 미들웨어

다음을 시도하는 경우 API 요청에 작업공간 ID를 추가로 전달해야 할 수 있습니다:

- 작업공간 내에서 새 데이터 생성 (예: 티켓 생성)
- 특정 작업공간에서 항목 목록 검색 (예: 작업공간의 모든 에이전트 그룹 나열)

작업공간 ID가 전달되지 않으면 새 데이터가 기본 작업공간 또는 계정의 첫 번째 작업공간에서 생성되거나 검색됩니다.

작업공간을 알 필요가 없는 작업(예: ID를 전달하여 티켓 가져오기, 편집 또는 삭제)의 경우 다중 작업공간 계정에서도 API가 예상대로 계속 작동합니다.

## 마켓플레이스 앱

### 공개 앱

이제 작업공간 내에 상주할 데이터를 기반으로 하고 다음 중 하나 이상을 수행하는 공개 앱:

- 계정에서 새 데이터를 생성합니다. 예: 티켓 생성
- 티켓/문제/변경/릴리스 양식과 타사 도구 간에 필드가 매핑되어 있기 때문에 타사 도구와 데이터를 동기화합니다
- 계정에서 데이터 목록을 검색합니다. 예: 계정의 모든 티켓 가져오기

이러한 앱은 계정의 기본/첫 번째 작업공간에서 예상대로 계속 작동합니다. 그러나 두 번째 작업공간을 추가하면 첫 번째 작업공간에서만 위의 작업을 계속 수행합니다.

Freshservice 팀은 현재 다중 작업공간 지원을 추가하여 이러한 앱을 업그레이드하는 과정에 있습니다. 앱의 우선순위를 지정하려면 support@freshservice.com으로 문의하세요.

### 개인 앱

"Freshservice API" 섹션에서 언급된 모듈에 대해 Freshservice API를 사용하고 계정에서 여러 작업공간을 생성하는 경우, 앱이 예상대로 계속 작동하도록 올바른 작업공간 ID를 전달하여 앱을 업데이트해야 할 수 있습니다.

</details>
