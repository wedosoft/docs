---
sidebar_position: 2
---

# Freshservice API V1 지원 중단 상세 가이드

2022년 11월 발표에 따라 API V1을 V2로 교체하기 위한 제품 개선 사항이 적용되었습니다. API V1 엔드포인트를 사용하는 모든 기능을 API V2로 업데이트해야 합니다.

:::warning 중요한 업데이트 필요
2023년 5월 31일 이후 API V1 엔드포인트가 완전히 중단됩니다. 영향을 받지 않으려면 즉시 마이그레이션을 시작하세요.
:::

<p data-identifyelement="535" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt"}}><span data-identifyelement="536" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>2022년 11월&nbsp;</span><a data-identifyelement="537" href="https://community.freshworks.com/product-updates/freshservice-release-notes-nov-2022-26812#Deprecation+of+password-based+authentication+for+API+v2"><span data-identifyelement="538" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(17, 85, 204)", "fontWeight": "400", "textDecorationSkipInk": "none"}}>릴리스</span></a><span data-identifyelement="539" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>&nbsp;기간 중 발표에 이어, API V1 호출을 해당하는 API V2 호출로 교체하기 위한 몇 가지 제품 개선 사항을 적용했습니다.&nbsp;</span></p>

## 이 업데이트의 영향을 받는지 확인하기

<p data-identifyelement="540" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt"}}><span data-identifyelement="543" style={{"fontSize": "16px", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700"}}>이 업데이트가 나에게 영향을 미칠까요?</span></p>

<p data-identifyelement="547" dir="ltr" style={{"lineHeight": "1.44", "marginBottom": "0pt"}}><span data-identifyelement="548" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>다음 작업 중 하나라도 API V1 엔드포인트를 사용한 적이 있다면 이 지원 중단의 영향을 받게 됩니다:</span></p>

- <p data-identifyelement="551" dir="ltr" style={{"lineHeight": "1.92", "marginBottom": "0pt"}}><span data-identifyelement="552" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>워크플로 구성</span></p>
- <p data-identifyelement="554" dir="ltr" style={{"lineHeight": "1.92", "marginBottom": "0pt"}}><span data-identifyelement="555" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>포털 사용자 지정</span></p>
- <p data-identifyelement="557" dir="ltr" style={{"lineHeight": "1.92", "marginBottom": "0pt"}}><span data-identifyelement="558" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>커스텀 애플리케이션에서 Freshservice 인스턴스와 상호 작용</span></p>

<p data-identifyelement="561" dir="ltr" style={{"lineHeight": "1.92", "marginBottom": "0pt"}}><span data-identifyelement="562" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>자세한 정보는&nbsp;</span><a data-identifyelement="563" href="https://support.freshservice.com/en/support/solutions/articles/50000004220-introducing-upgraded-apis-for-freshservice"><span data-identifyelement="564" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(17, 85, 204)", "fontWeight": "400"}}>이 솔루션 문서</span></a><span data-identifyelement="565" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>를 참조하세요.&nbsp;</span></p>

## 영향을 받는 모듈 및 업데이트 방법

<p data-identifyelement="568" dir="ltr" style={{ fontSize: "16px", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>영향을 받는 모듈&nbsp;</p>

### 1. 워크플로 자동화 (Workflow Automator) 업데이트

- <p data-identifyelement="573" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="574" dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>워크플로 자동화</span><span data-identifyelement="577" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}> API V1 권장 업데이트 태그가 API V1 엔드포인트를 사용하는 모든 자동화에 표시됩니다.&nbsp;</span></p>

![API v1 단계별 사용 중단 프로세스](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797722/original/lsrkc1FJgrzo4T8_oiKi-OsCEXv5Rtcq0A.png?1678253587)

#### 워크플로 자동화 업데이트 방법

<p data-identifyelement="586" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="587" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>워크플로 자동화를 어떻게 업데이트할 수 있나요?</span></p>

- <p data-identifyelement="592" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="593" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>다음 경로로 이동하세요:&nbsp;</span><span data-identifyelement="594" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>관리자 → 자동화 및 생산성 → 워크플로 자동화.</span></p>
- <p data-identifyelement="598" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="599" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>"</span><span data-identifyelement="600" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>API 업데이트 권장</span><span data-identifyelement="601" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>" 태그가 있는 워크플로 자동화를 클릭하세요.</span></p>
- <p data-identifyelement="606" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="607" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>워크플로를 열면 v1 엔드포인트를 사용하는 모든 노드가 빨간색 알림으로 강조 표시됩니다 (아래 스크린샷 참조)</span></p>

<p data-identifyelement="612" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="613" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}><span data-identifyelement="614" style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "372px" }}><img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797724/original/7zRGguXe0OdHqnAs8bSccF6HJL_SmHAZaQ.png?1678253588" width="624" height="372" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797724" data-identifyelement="615" /></span></span></p>

- <p data-identifyelement="620" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="621" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Select the Red alert to view the recommended V2 URL for the corresponding V1 URL. Click &nbsp; on&nbsp;</span><span data-identifyelement="622" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>'✓'&nbsp;</span><span data-identifyelement="623" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>icon to update the URL. Finally click on&nbsp;</span><span data-identifyelement="624" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Done&nbsp;</span><span data-identifyelement="625" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>button to update the respective node.&nbsp;</span></p>

<p data-identifyelement="628" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="629" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}><span data-identifyelement="630" style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "372px" }}><img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797723/original/bPCqTlg9EhS3W434gl_gKeS-CcuDJXAkhA.png?1678253587" width="624" height="372" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797723" data-identifyelement="631" /></span></span></p>

- <p data-identifyelement="636" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="637" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Repeat this process for all the highlighted nodes and save the workflow automator</span></p>
- <p data-identifyelement="641" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="642" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="643" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="644" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none" }}>here</span></a></p>

### 2. 포털 커스터마이징 (Portal Customization) 업데이트

- <p data-identifyelement="649" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="650" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Portal Customization</span></p>

- <p data-identifyelement="655" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="656" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Navigate to&nbsp;</span><span data-identifyelement="657" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Admin → &nbsp;Rebrand your service desk → Customize</span><span data-identifyelement="658" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>. In the&nbsp;</span><span data-identifyelement="659" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Home page designer</span><span data-identifyelement="660" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;dropdown, all the sections that are using v1 endpoints will be highlighted.</span></p>
- <p data-identifyelement="664" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="665" dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Select a specific section(check out for the alert sign) to identify if there are any v1 endpoints, and update them with the corresponding v2 endpoints.&nbsp;</span></p>

<p data-identifyelement="667" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}><span data-identifyelement="669" style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "441px" }}><img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007797725/original/A7d5030gexgbWNJseExGulUZAtyiNUas6w.png?1678253588" width="624" height="441" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50007797725" data-identifyelement="670" /></span></p>

- <p data-identifyelement="675" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="676" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Click&nbsp;</span><span data-identifyelement="677" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>'Save'&nbsp;</span><span data-identifyelement="678" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>or '</span><span data-identifyelement="679" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Publish Portal</span><span data-identifyelement="680" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>' when you have replaced all the v1 endpoints in your portal customizations</span></p>
- <p data-identifyelement="684" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="685" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="686" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="687" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none" }}>here</span></a></p>

### 3. 커스텀 앱 (Custom Apps) 업데이트

- <p data-identifyelement="692" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="693" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Custom Apps</span></p>

- <p data-identifyelement="698" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="699" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Navigate to&nbsp;</span><span data-identifyelement="700" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Admin → Apps</span></p>
- <p data-identifyelement="704" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="705" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Check for custom apps that are using v1 endpoints and update the corresponding endpoints to v2.&nbsp;</span></p>
- <p data-identifyelement="709" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="710" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>For more info refer to the detailed migration guide&nbsp;</span><a data-identifyelement="711" href="https://community.freshworks.dev/t/migration-guide-for-freshservice-api-v1-to-freshservice-api-v2/5860"><span data-identifyelement="712" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(17, 85, 204)", fontWeight: "400", textDecorationSkipInk: "none" }}>here</span></a></p>

## 실무 활용 예시

## 업데이트하지 않을 경우의 영향

<p data-identifyelement="716" style={{ fontSize: "16px", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>What happens if I do not update my configurations before May 31, 2023?</p>

- <p data-identifyelement="722" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="723" dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>All the workflow automators, portal customization and custom apps with v1 endpoints will stop working and your configurations will start failing</span></p>

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