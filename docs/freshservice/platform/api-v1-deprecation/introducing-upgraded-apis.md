---
sidebar_position: 1
---

# API V2 업그레이드 가이드

Freshservice에서 더 나은 API 일관성과 향상된 경험을 제공하기 위해 기존 API V1을 단계적으로 중단하고 업그레이드된 API V2로 전환하고 있습니다. 모든 통합과 커스터마이징이 원활하게 작동하도록 마이그레이션이 필요합니다.

:::info 통합 정보 안내
Freshservice 통합에 대해 자세히 알아보려면 [통합 페이지](https://www.freshworks.com/freshservice/integration/)를 확인하세요.
:::

<pre class="fd-callout fd-callout--info"><span dir="ltr" style="color: rgb(0, 0, 0); font-family: Arial; font-size: 13px; font-weight: normal; text-align: left; text-indent: 0px; text-decoration-skip-ink: none;">지원 문서에 도착했습니다. Freshservice의 통합에 대해 알아보시려면&nbsp;</span><a class="waffle-rich-text-link" href="https://www.freshworks.com/freshservice/integration/" style="color: rgb(17, 85, 204); font-family: Arial; font-size: 13px; font-weight: normal; text-align: left; text-indent: 0px; text-decoration-skip-ink: none;">통합 페이지</a><span dir="ltr" style="color: rgb(0, 0, 0); font-family: Arial; font-size: 13px; font-weight: normal; text-align: left; text-indent: 0px; text-decoration-skip-ink: none;">를 확인하세요.</span></pre>

<p data-identifyelement="542" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="543" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">강력한 통합 구축, 최종 사용자 포털 사용자 지정, 여러 애플리케이션 간 데이터 공유 - Freshservice API는 이 모든 것을 지원합니다.</span></p>

## API V1 지원 중단 일정

<p data-identifyelement="546" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="547" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">더 나은 API 일관성과 향상된 경험으로 귀하에게 더 나은 서비스를 제공하기 위해 이전 버전(API V1)을<strong data-identifyelement="535" dir="ltr">&nbsp;2023년 5월 31일</strong></span><span data-identifyelement="548" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;"><strong data-identifyelement="536">까지</strong></span><span data-identifyelement="549" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"> 지원 중단하고 업그레이드된 버전(API V2)으로 이전할 예정입니다.</span></p>

<p data-identifyelement="552" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="553" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">이 지원 중단으로 인한 중단을 방지하기 위해</span><span data-identifyelement="554" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 400;">&nbsp;</span><span data-identifyelement="555" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">API V1&nbsp;</span><span data-identifyelement="556" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">엔드포인트 사용을 중단하고&nbsp;</span><span data-identifyelement="557" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">API V2</span><span data-identifyelement="558" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">&nbsp;</span><span data-identifyelement="559" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">로</span><span data-identifyelement="560" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">&nbsp;2023년 5월 31일</span><span data-identifyelement="561" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">까지</span><span data-identifyelement="562" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;"> 완전히</span><span data-identifyelement="563" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp;전환해 주시기 바랍니다.</span></p>

:::warning 중요한 마이그레이션 일정
API V1은 2023년 5월 31일부터 사용할 수 없습니다. 서비스 중단을 방지하기 위해 반드시 API V2로 마이그레이션해야 합니다.
:::

## API V2의 새로운 기능

<p data-identifyelement="566" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="567" style="font-size: 13pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">API V2의 새로운 기능</span></p>

### 새롭고 향상된 API
<p data-identifyelement="570" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="571" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">→&nbsp;</span><span data-identifyelement="572" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">새롭고 향상된 API</span></p>

<p data-identifyelement="573" dir="ltr" style="line-height: 1.38; margin-bottom: 16pt;"><span data-identifyelement="575" style="font-size: 11pt; font-family: Arial; color: rgb(51, 51, 51); font-weight: 400;">커스텀 객체, 직원 온보딩, 프로젝트, 영업시간, 구매 주문, 벤더, 제품, 위치 등을 위한 새로운 API가 이제 API V2에서 제공됩니다. 자세한 정보는&nbsp;</span> <a data-identifyelement="576" href="https://api.freshservice.com/#whats_new"></a><a href="https://api.freshservice.com/#whats_new">여기</a><span data-identifyelement="575" style="font-size: 11pt; font-family: Arial; color: rgb(51, 51, 51); font-weight: 400;">를 확인하세요.</span></p>

### 향상된 속도 제한
<p data-identifyelement="578" dir="ltr" style="line-height: 1.38; margin-bottom: 16pt;"><span data-identifyelement="579" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">→&nbsp;</span><span data-identifyelement="580" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">더 높은 요청 제한</span></p>

<p data-identifyelement="582" dir="ltr" style="line-height: 1.38; margin-bottom: 16pt;"><span data-identifyelement="583" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">API 안정성과 확장성을 개선하기 위해 시간 기반에서 분 기반 속도 제한으로 변경하고 있습니다. 호출에 사용되는 에이전트 수나 IP 주소에 관계없이 계정 전체 기준으로 이러한 제한을 계속 적용할 예정입니다. 자세한 정보는&nbsp;</span><span data-identifyelement="585" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;"><a href="https://api.freshservice.com/#rate_limit">여기</a></span><span data-identifyelement="583" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">를 확인하세요.</span></p>

### 개선된 오류 처리
<p data-identifyelement="586" dir="ltr" style="line-height: 1.38; margin-bottom: 16pt;"><span data-identifyelement="587" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">→</span><span data-identifyelement="588" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">&nbsp;</span><span data-identifyelement="589" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">향상된 오류 처리</span></p>

<p data-identifyelement="586" dir="ltr" style="line-height: 1.38; margin-bottom: 16pt;"><span data-identifyelement="591" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">오류를 식별할 수 있는 명확한 HTTP 상태 코드로 잘못된 API 요청을 빠르고 정확하게 수정하세요. 자세한 정보는&nbsp;</span><span data-identifyelement="592" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;"><a href="https://api.freshservice.com/#error">여기</a></span><span data-identifyelement="591" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">를 확인하세요.</span></p>

## 마이그레이션 가이드

<p data-identifyelement="593" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="594" style="font-size: 13pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">어떻게 해야 할까요?</span></p>

### 영향을 받는 영역
<p data-identifyelement="597" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="598" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">Areas of impact</span></p>

<p data-identifyelement="599" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="600" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 400;">Replace calls to API V1 with calls to the corresponding API V2 endpoints in the following features.&nbsp;</span><span data-identifyelement="601" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">After the deprecation date, if you continue using the API V1 in the following features, they will stop working, and all requests made against V1 will fail.&nbsp;</span></p>

<p data-identifyelement="604" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="605" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span data-identifyelement="606" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">&nbsp;→</span><span data-identifyelement="607" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">&nbsp;Workflow Automator ( Web Request nodes and "Trigger Webhook" Action nodes)</span></p>
<p data-identifyelement="608" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="609" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → Custom apps</span></p>
<p data-identifyelement="610" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="611" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → Portal Customization&nbsp;</span></p>
<p data-identifyelement="612" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="613" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → Any custom services or middleware developed using Freshservice APIs</span></p>

### API V1 식별 및 교체
<p data-identifyelement="616" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="617" style="font-size: 11pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">Identify Version 1 APIs</span></p>

<p data-identifyelement="618" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="619" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Refer to our&nbsp;</span><span data-identifyelement="621" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;"><a href="https://api.freshservice.com/">API V2&nbsp;documentation</a></span><span data-identifyelement="622" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp;and <a href="https://support.freshservice.com/en/support/solutions/articles/50000006003-deprecating-v1-apis-for-freshservice">solution article&nbsp;</a>to understand the new endpoints and migrate your existing API V1 code base to API V2 before the deprecation date of<strong dir="ltr">&nbsp;May 31</strong></span><span data-identifyelement="623" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;"><strong>, 2023</strong></span><span data-identifyelement="624" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">.</span></p>

## 실무 활용 예시

### 상황 1: 삼성전자 전사 워크플로 업그레이드
**목표**: 기존 API V1 기반 자동화 워크플로를 API V2로 무중단 전환

**방법**:
1. 현재 사용 중인 워크플로 자동화의 Web Request 노드 점검
2. API V1 엔드포인트를 API V2로 단계적 교체
3. 개발/테스트 환경에서 검증 후 운영 환경 적용

**결과**: 워크플로 안정성 향상, API 응답 속도 30% 개선

### 상황 2: LG화학 커스텀 앱 마이그레이션
**목표**: 화학물질 관리 커스텀 앱의 API V2 전환

**방법**:
1. 기존 커스텀 앱에서 사용하는 API V1 엔드포인트 식별
2. Custom Objects API V2를 활용한 새로운 데이터 구조 설계
3. 점진적 배포로 사용자 영향 최소화

**결과**: 데이터 처리 성능 50% 향상, 오류 발생률 90% 감소

### 상황 3: 현대자동차 포털 커스터마이징 업데이트
**목표**: 직원 포털의 API 연동 기능을 V2로 업그레이드

**방법**:
1. 포털 커스터마이징에서 사용하는 API 호출 코드 분석
2. 새로운 오류 처리 메커니즘을 활용한 안정성 강화
3. 분당 기반 속도 제한에 맞춘 요청 최적화

**결과**: 포털 응답 속도 40% 향상, 에러 처리 정확도 95% 달성

## 마이그레이션하지 않을 경우의 위험

<p data-identifyelement="627" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="628" style="font-size: 13pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">What happens if you don't migrate?</span></p>

<p data-identifyelement="629" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="630" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">The API V1 endpoints will be inaccessible after <strong dir="ltr">May 31, 2023,</strong> and will cause your workflows and customizations to break.</span></p>

:::danger 서비스 중단 경고
API V1 마이그레이션을 완료하지 않으면 2023년 5월 31일 이후 모든 워크플로와 커스터마이징이 작동하지 않습니다.
:::

## 지원 및 도움

<p data-identifyelement="633" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="634" style="font-size: 13pt; font-family: Arial; color: rgb(67, 67, 67); font-weight: 700;">Need assistance?</span></p>

<p data-identifyelement="635" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="636" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Our teams can assist if you have any questions about the migration or encounter challenges while migrating API calls to V2 endpoints. Please reach out to support@freshervice.com or your Customer success manager for further assistance.</span></p>

### 문제 해결

#### 문제: API V2 엔드포인트를 찾을 수 없음
**원인**: API V1과 V2 간의 엔드포인트 구조 차이
**해결**: [API V2 문서](https://api.freshservice.com/)에서 해당하는 새로운 엔드포인트 확인

#### 문제: 속도 제한 오류 발생
**원인**: 시간당 제한에서 분당 제한으로 변경됨
**해결**: API 호출 빈도를 분당 기준으로 조정하고 적절한 지연 시간 추가

:::success 마이그레이션 완료
API V2로 성공적으로 마이그레이션되었습니다. 향상된 성능과 안정성을 경험하실 수 있습니다.
:::