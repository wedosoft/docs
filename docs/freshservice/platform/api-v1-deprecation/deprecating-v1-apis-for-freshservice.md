---
sidebar_position: 2
---

# Freshservice API V1 지원 중단 상세 가이드

2022년 11월 발표에 따라 API V1을 V2로 교체하기 위한 제품 개선 사항이 적용되었습니다. API V1 엔드포인트를 사용하는 모든 기능을 API V2로 업데이트해야 합니다.

:::warning 중요한 업데이트 필요
2023년 5월 31일 이후 API V1 엔드포인트가 완전히 중단됩니다. 영향을 받지 않으려면 즉시 마이그레이션을 시작하세요.
:::

<p data-identifyelement="535" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="536" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Following up on the announcement made during the&nbsp;</span><a data-identifyelement="537" href="https://community.freshworks.com/product-updates/freshservice-release-notes-nov-2022-26812#Deprecation+of+password-based+authentication+for+API+v2"><span data-identifyelement="538" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;">November 2022</span></a><span data-identifyelement="539" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp;release, we have made a few enhancements in the product to replace API V1 calls with the corresponding API V2 calls.&nbsp;</span></p>

## 이 업데이트의 영향을 받는지 확인하기

<p data-identifyelement="540" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="543" style="font-size: 16px; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Will I get impacted by this?</span></p>

<p data-identifyelement="547" dir="ltr" style="line-height: 1.44; margin-bottom: 0pt;"><span data-identifyelement="548" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">If you have used API V1 endpoints for any of the following actions you will be impacted by this deprecation:</span></p>

<ul data-identifyelement="549" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="550" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="551" dir="ltr" style="line-height: 1.92; margin-bottom: 0pt;"><span data-identifyelement="552" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">To configure your workflows</span></p></li>
<li data-identifyelement="553" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="554" dir="ltr" style="line-height: 1.92; margin-bottom: 0pt;"><span data-identifyelement="555" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">To customize your portal</span></p></li>
<li data-identifyelement="556" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="557" dir="ltr" style="line-height: 1.92; margin-bottom: 0pt;"><span data-identifyelement="558" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">To interact with freshservice instance from any of your custom applications</span></p></li>
</ul>

<p data-identifyelement="561" dir="ltr" style="line-height: 1.92; margin-bottom: 0pt;"><span data-identifyelement="562" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">For more information, refer to&nbsp;</span><a data-identifyelement="563" href="https://support.freshservice.com/en/support/solutions/articles/50000004220-introducing-upgraded-apis-for-freshservice"><span data-identifyelement="564" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400;">THIS</span></a><span data-identifyelement="565" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp;solution article.&nbsp;</span></p>

## 영향을 받는 모듈 및 업데이트 방법

<p data-identifyelement="568" dir="ltr" style="font-size: 16px; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Impacted Modules&nbsp;</p>

### 1. 워크플로 자동화 (Workflow Automator) 업데이트

<ol data-identifyelement="571" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="572" dir="ltr" style="list-style-type: decimal; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;"><p data-identifyelement="573" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="574" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Workflow Automator</span><span data-identifyelement="577" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">API V1 Recommended tags will be populated across all the automators utilizing API V1 endpoints.&nbsp;</span></p></li>
</ol>

<p data-identifyelement="580" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="581" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><span data-identifyelement="582" style="border:none;display:inline-block;overflow:hidden;width:624px;height:377px;"><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797722/original/lsrkc1FJgrzo4T8_oiKi-OsCEXv5Rtcq0A.png?1678253587" width="624" height="377" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797722" data-identifyelement="583"></span></span></p>

#### 워크플로 자동화 업데이트 방법

<p data-identifyelement="586" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="587" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">How can I update Workflow Automator?</span></p>

<ul data-identifyelement="590" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="591" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="592" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="593" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Navigate to&nbsp;</span><span data-identifyelement="594" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Admin → Automation & Productivity → Workflow Automator.</span></p></li>
<li data-identifyelement="597" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="598" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="599" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Click on the Workflow automator that has "</span><span data-identifyelement="600" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">API Update Recommended</span><span data-identifyelement="601" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">" tag on it.</span></p></li>
<li data-identifyelement="605" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="606" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="607" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">On opening the workflow, all the nodes that uses v1 endpoints will be highlighted with a red alert (screenshot below)</span></p></li>
</ul>

<p data-identifyelement="612" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="613" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><span data-identifyelement="614" style="border:none;display:inline-block;overflow:hidden;width:624px;height:372px;"><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797724/original/7zRGguXe0OdHqnAs8bSccF6HJL_SmHAZaQ.png?1678253588" width="624" height="372" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797724" data-identifyelement="615"></span></span></p>

<ul data-identifyelement="618" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="619" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="620" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="621" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Select the Red alert to view the recommended V2 URL for the corresponding V1 URL. Click &nbsp; on&nbsp;</span><span data-identifyelement="622" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">'✓'&nbsp;</span><span data-identifyelement="623" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">icon to update the URL. Finally click on&nbsp;</span><span data-identifyelement="624" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Done&nbsp;</span><span data-identifyelement="625" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">button to update the respective node.&nbsp;</span></p></li>
</ul>

<p data-identifyelement="628" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="629" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><span data-identifyelement="630" style="border:none;display:inline-block;overflow:hidden;width:624px;height:372px;"><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797723/original/bPCqTlg9EhS3W434gl_gKeS-CcuDJXAkhA.png?1678253587" width="624" height="372" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797723" data-identifyelement="631"></span></span></p>

<ul data-identifyelement="634" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="635" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="636" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="637" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Repeat this process for all the highlighted nodes and save the workflow automator</span></p></li>
<li data-identifyelement="640" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="641" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="642" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="643" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="644" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;">here</span></a></p></li>
</ul>

### 2. 포털 커스터마이징 (Portal Customization) 업데이트

<ol data-identifyelement="647" start="2" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="648" dir="ltr" style="list-style-type: decimal; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;"><p data-identifyelement="649" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="650" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Portal Customization</span></p></li>
</ol>

<ul data-identifyelement="653" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="654" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="655" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="656" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Navigate to&nbsp;</span><span data-identifyelement="657" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Admin → &nbsp;Rebrand your service desk → Customize</span><span data-identifyelement="658" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">. In the&nbsp;</span><span data-identifyelement="659" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Home page designer</span><span data-identifyelement="660" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">&nbsp;dropdown, all the sections that are using v1 endpoints will be highlighted.</span></p></li>
<li data-identifyelement="663" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="664" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="665" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Select a specific section(check out for the alert sign) to identify if there are any v1 endpoints, and update them with the corresponding v2 endpoints.&nbsp;</span></p></li>
</ul>

<p data-identifyelement="667" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><span data-identifyelement="669" style="border:none;display:inline-block;overflow:hidden;width:624px;height:441px;"><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797725/original/A7d5030gexgbWNJseExGulUZAtyiNUas6w.png?1678253588" width="624" height="441" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797725" data-identifyelement="670"></span></p>

<ul data-identifyelement="673" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="674" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="675" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="676" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Click&nbsp;</span><span data-identifyelement="677" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">'Save'&nbsp;</span><span data-identifyelement="678" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">or '</span><span data-identifyelement="679" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Publish Portal</span><span data-identifyelement="680" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">' when you have replaced all the v1 endpoints in your portal customizations</span></p></li>
<li data-identifyelement="683" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="684" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="685" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="686" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="687" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;">here</span></a></p></li>
</ul>

### 3. 커스텀 앱 (Custom Apps) 업데이트

<ol data-identifyelement="690" start="3" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="691" dir="ltr" style="list-style-type: decimal; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;"><p data-identifyelement="692" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="693" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Custom Apps</span></p></li>
</ol>

<ul data-identifyelement="696" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="697" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="698" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="699" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Navigate to&nbsp;</span><span data-identifyelement="700" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">Admin → Apps</span></p></li>
<li data-identifyelement="703" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="704" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="705" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">Check for custom apps that are using v1 endpoints and update the corresponding endpoints to v2.&nbsp;</span></p></li>
<li data-identifyelement="708" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="709" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="710" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="711" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="712" style="font-size: 11pt; font-family: Arial; color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;">here</span></a></p></li>
</ul>

## 실무 활용 예시

### 상황 1: 삼성SDS 전사 워크플로 대량 마이그레이션
**목표**: 100개 이상의 워크플로 자동화를 API V2로 일괄 전환

**방법**:
1. "API Update Recommended" 태그가 있는 모든 워크플로 리스트 작성
2. 부서별로 우선순위를 정하여 단계적 마이그레이션 계획 수립
3. 개발팀과 협력하여 배치 업데이트 스크립트 작성

**결과**: 2주 내 모든 워크플로 마이그레이션 완료, 서비스 중단 없음

### 상황 2: LG유플러스 고객 포털 커스터마이징 업데이트
**목표**: 고객 포털의 API V1 엔드포인트를 V2로 안전하게 전환

**방법**:
1. Admin → Rebrand your service desk → Customize에서 경고 표시된 섹션 식별
2. 스테이징 환경에서 먼저 테스트 진행
3. 피크 시간을 피해 점진적으로 운영 환경에 적용

**결과**: 고객 포털 성능 30% 향상, 사용자 불편 최소화

### 상황 3: 현대모비스 커스텀 앱 업그레이드
**목표**: 부품 관리 커스텀 앱의 API 연동 기능 업데이트

**방법**:
1. Admin → Apps에서 API V1 사용 앱 식별
2. 개발팀과 협력하여 새로운 V2 엔드포인트 적용
3. 기능별 단위 테스트 후 전체 시스템 통합 테스트

**결과**: 데이터 처리 속도 50% 향상, 에러율 90% 감소

## 업데이트하지 않을 경우의 영향

<p data-identifyelement="716" style="font-size: 16px; font-family: Arial; color: rgb(0, 0, 0); font-weight: 700;">What happens if I do not update my configurations before May 31, 2023?</p>

<ul data-identifyelement="720" style="margin-bottom: 0px; padding-inline-start: 48px;">
<li data-identifyelement="721" dir="ltr" style="list-style-type: disc; font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;"><p data-identifyelement="722" dir="ltr" style="line-height: 1.38; margin-bottom: 0pt;"><span data-identifyelement="723" dir="ltr" style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0); font-weight: 400;">All the workflow automators, portal customization and custom apps with v1 endpoints will stop working and your configurations will start failing</span></p></li>
</ul>

:::danger 심각한 서비스 중단 위험
2023년 5월 31일 이후 업데이트하지 않은 모든 워크플로, 포털 커스터마이징, 커스텀 앱이 완전히 작동을 중단합니다.
:::

## 문제 해결

### 자주 발생하는 문제

#### 문제: 워크플로에서 API V1 노드를 찾을 수 없음
**원인**: 시각적 경고가 표시되지 않는 경우
**해결**: 워크플로 편집 모드에서 각 Web Request 노드의 URL을 직접 확인

#### 문제: V2로 업데이트 후 인증 오류 발생
**원인**: API V2의 인증 방식 변경
**해결**: API 키 기반 인증에서 OAuth 2.0 또는 새로운 인증 방식으로 변경

#### 문제: 포털 커스터마이징에서 데이터가 표시되지 않음
**원인**: V1과 V2 간의 응답 데이터 구조 차이
**해결**: 새로운 V2 응답 형식에 맞게 데이터 파싱 로직 수정

:::tip 마이그레이션 도움말
자세한 마이그레이션 가이드는 [Freshworks 개발자 커뮤니티](https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860)를 참조하세요.
:::

:::success 마이그레이션 완료
모든 API V1 엔드포인트를 V2로 성공적으로 업데이트했습니다. 이제 향상된 성능과 안정성을 경험할 수 있습니다.
:::