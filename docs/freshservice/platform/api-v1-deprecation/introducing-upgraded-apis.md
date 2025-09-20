---
sidebar_position: 1
---

# API V2 업그레이드 가이드

Freshservice에서 더 나은 API 일관성과 향상된 경험을 제공하기 위해 기존 API V1을 단계적으로 중단하고 업그레이드된 API V2로 전환하고 있습니다. 모든 통합과 커스터마이징이 원활하게 작동하도록 마이그레이션이 필요합니다.

:::info 통합 정보 안내
Freshservice 통합에 대해 자세히 알아보려면 [통합 페이지](https://www.freshworks.com/freshservice/integration/)를 확인하세요.
:::

<div className="fd-callout fd-callout--info"><span dir="ltr" style={{"color": "rgb(0, 0, 0)", "fontFamily": "Arial", "fontSize": "13px", "fontWeight": "normal", "textAlign": "left", "textIndent": "0px", "textDecorationSkipInk": "none"}}>지원 문서에 도착했습니다. Freshservice의 통합에 대해 알아보시려면&nbsp;</span><a className="waffle-rich-text-link" href="https://www.freshworks.com/freshservice/integration/" style={{"color": "rgb(17, 85, 204)", "fontFamily": "Arial", "fontSize": "13px", "fontWeight": "normal", "textAlign": "left", "textIndent": "0px", "textDecorationSkipInk": "none"}}>통합 페이지</a><span dir="ltr" style={{"color": "rgb(0, 0, 0)", "fontFamily": "Arial", "fontSize": "13px", "fontWeight": "normal", "textAlign": "left", "textIndent": "0px", "textDecorationSkipInk": "none"}}>를 확인하세요.</span></div>

<p data-identifyelement="542" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt"}}><span data-identifyelement="543" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>강력한 통합 구축, 최종 사용자 포털 사용자 지정, 여러 애플리케이션 간 데이터 공유 - Freshservice API는 이 모든 것을 지원합니다.</span></p>

## API V1 지원 중단 일정

<p data-identifyelement="546" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="547" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>더 나은 API 일관성과 향상된 경험으로 귀하에게 더 나은 서비스를 제공하기 위해 이전 버전(API V1)을<strong data-identifyelement="535" dir="ltr">&nbsp;2023년 5월 31일</strong></span><span data-identifyelement="548" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}><strong data-identifyelement="536">까지</strong></span><span data-identifyelement="549" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}> 지원 중단하고 업그레이드된 버전(API V2)으로 이전할 예정입니다.</span></p>

<p data-identifyelement="552" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="553" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>이 지원 중단으로 인한 중단을 방지하기 위해</span><span data-identifyelement="554" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "400" }}>&nbsp;</span><span data-identifyelement="555" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>API V1&nbsp;</span><span data-identifyelement="556" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>엔드포인트 사용을 중단하고&nbsp;</span><span data-identifyelement="557" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>API V2</span><span data-identifyelement="558" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}>&nbsp;</span><span data-identifyelement="559" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>로</span><span data-identifyelement="560" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}>&nbsp;2023년 5월 31일</span><span data-identifyelement="561" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>까지</span><span data-identifyelement="562" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}> 완전히</span><span data-identifyelement="563" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>&nbsp;전환해 주시기 바랍니다.</span></p>

:::warning 중요한 마이그레이션 일정
API V1은 2023년 5월 31일부터 사용할 수 없습니다. 서비스 중단을 방지하기 위해 반드시 API V2로 마이그레이션해야 합니다.
:::

## API V2의 새로운 기능

<p data-identifyelement="566" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="567" style={{"fontSize": "13pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>API V2의 새로운 기능</span></p>

### 새롭고 향상된 API
<p data-identifyelement="570" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="571" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>→&nbsp;</span><span data-identifyelement="572" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>새롭고 향상된 API</span></p>

<p data-identifyelement="573" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "16pt" }}><span data-identifyelement="575" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(51, 51, 51)", "fontWeight": "400" }}>커스텀 객체, 직원 온보딩, 프로젝트, 영업시간, 구매 주문, 벤더, 제품, 위치 등을 위한 새로운 API가 이제 API V2에서 제공됩니다. 자세한 정보는&nbsp;</span> <a data-identifyelement="576" href="https://api.freshservice.com/#whats_new"></a><a href="https://api.freshservice.com/#whats_new">여기</a><span data-identifyelement="575" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(51, 51, 51)", "fontWeight": "400" }}>를 확인하세요.</span></p>

### 향상된 속도 제한
<p data-identifyelement="578" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "16pt" }}><span data-identifyelement="579" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>→&nbsp;</span><span data-identifyelement="580" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>더 높은 요청 제한</span></p>

<p data-identifyelement="582" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "16pt" }}><span data-identifyelement="583" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>API 안정성과 확장성을 개선하기 위해 시간 기반에서 분 기반 속도 제한으로 변경하고 있습니다. 호출에 사용되는 에이전트 수나 IP 주소에 관계없이 계정 전체 기준으로 이러한 제한을 계속 적용할 예정입니다. 자세한 정보는&nbsp;</span><span data-identifyelement="585" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(17, 85, 204)", "fontWeight": "400", "textDecorationSkipInk": "none" }}><a href="https://api.freshservice.com/#rate_limit">여기</a></span><span data-identifyelement="583" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>를 확인하세요.</span></p>

### 개선된 오류 처리
<p data-identifyelement="586" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "16pt" }}><span data-identifyelement="587" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>→</span><span data-identifyelement="588" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}>&nbsp;</span><span data-identifyelement="589" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>향상된 오류 처리</span></p>

<p data-identifyelement="586" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "16pt" }}><span data-identifyelement="591" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>오류를 식별할 수 있는 명확한 HTTP 상태 코드로 잘못된 API 요청을 빠르고 정확하게 수정하세요. 자세한 정보는&nbsp;</span><span data-identifyelement="592" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(17, 85, 204)", "fontWeight": "400", "textDecorationSkipInk": "none" }}><a href="https://api.freshservice.com/#error">여기</a></span><span data-identifyelement="591" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>를 확인하세요.</span></p>

## 마이그레이션 가이드

<p data-identifyelement="593" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="594" style={{"fontSize": "13pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>어떻게 해야 할까요?</span></p>

### 영향을 받는 영역
<p data-identifyelement="597" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="598" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>영향을 받는 영역</span></p>

<p data-identifyelement="599" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="600" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "400" }}>다음 기능에서 API V1 호출을 해당하는 API V2 엔드포인트 호출로 교체하세요.&nbsp;</span><span data-identifyelement="601" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>지원 중단 날짜 이후에도 다음 기능에서 API V1을 계속 사용하면 작동이 중단되고 V1에 대한 모든 요청이 실패합니다.&nbsp;</span></p>

<p data-identifyelement="604" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="605" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span data-identifyelement="606" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}>&nbsp;→</span><span data-identifyelement="607" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>&nbsp;워크플로 자동화 (웹 요청 노드 및 "웹훅 트리거" 액션 노드)</span></p>
<p data-identifyelement="608" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="609" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → 커스텀 앱</span></p>
<p data-identifyelement="610" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="611" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → 포털 커스터마이징&nbsp;</span></p>
<p data-identifyelement="612" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="613" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; → Freshservice API를 사용하여 개발된 모든 커스텀 서비스 또는 미들웨어</span></p>

### API V1 식별 및 교체
<p data-identifyelement="616" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="617" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>버전 1 API 식별</span></p>

<p data-identifyelement="618" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="619" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>새로운 엔드포인트를 이해하고&nbsp;</span><span data-identifyelement="622" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "700" }}>2023년 5월 31일</span><span data-identifyelement="623" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>&nbsp;지원 중단 날짜 이전에 기존 API V1 코드베이스를 API V2로 마이그레이션하려면&nbsp;</span><span data-identifyelement="621" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(17, 85, 204)", "fontWeight": "400", "textDecorationSkipInk": "none" }}><a href="https://api.freshservice.com/">API V2&nbsp;문서</a></span><span data-identifyelement="622" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>&nbsp;및 <a href="https://support.freshservice.com/en/support/solutions/articles/50000006003-deprecating-v1-apis-for-freshservice">솔루션 문서</a>를 참조하세요.</span></p>

## 실무 활용 예시

## 마이그레이션하지 않을 경우의 위험

<p data-identifyelement="627" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="628" style={{"fontSize": "13pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>마이그레이션하지 않으면 어떻게 될까요?</span></p>

<p data-identifyelement="629" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="630" dir="ltr" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>API V1 엔드포인트는 <strong dir="ltr">2023년 5월 31일</strong> 이후 접근할 수 없게 되며, 워크플로와 커스터마이징이 중단됩니다.</span></p>

:::danger 서비스 중단 경고
API V1 마이그레이션을 완료하지 않으면 2023년 5월 31일 이후 모든 워크플로와 커스터마이징이 작동하지 않습니다.
:::

## 지원 및 도움

<p data-identifyelement="633" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="634" style={{"fontSize": "13pt", "fontFamily": "Arial", "color": "rgb(67, 67, 67)", "fontWeight": "700" }}>도움이 필요하신가요?</span></p>

<p data-identifyelement="635" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt" }}><span data-identifyelement="636" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400" }}>마이그레이션에 대한 질문이 있거나 API 호출을 V2 엔드포인트로 마이그레이션하는 동안 문제가 발생하면 저희 팀이 도움을 드릴 수 있습니다. 추가 지원을 위해 support@freshservice.com 또는 고객 성공 관리자에게 문의하세요.</span></p>

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