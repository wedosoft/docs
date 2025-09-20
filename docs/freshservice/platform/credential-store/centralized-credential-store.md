---
sidebar_position: 1
---

# 중앙화된 자격 증명 저장소

조직이 성장함에 따라 IT 팀이 타사 도구에 대한 인증 요청을 위해 액세스 자격 증명을 관리하는 것이 생산성을 저해하는 요인이 되고 있습니다. 중앙화된 자격 증명 저장소를 통해 자격 증명을 효율적으로 관리하고 워크플로 전반에서 쉽게 참조할 수 있습니다.

:::info 지원되는 인증 방식
- Basic Auth (기본 인증)
- API Key (API 키)
- OAuth 2.0 (OAuth 2.0)
- No Auth (인증 없음)
:::

## 중앙화된 자격 증명 저장소의 주요 기능

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>조직이 지속적으로 성장함에 따라 IT 팀이 타사 도구에 대한 인증 요청을 위해 액세스 자격 증명을 관리하는 것이 생산성을 저해하는 요인이 되고 있습니다. IT 팀은 토큰 변경사항을 지속적으로 확인하고 모든 워크플로에서 수동으로 업데이트해야 하므로 시간이 많이 소요됩니다.</span></p>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(34, 34, 34)", fontWeight: "400" }}>중앙화된 자격 증명 저장소를 통해 다음과 같은 작업이 가능합니다:</span></p>

- <p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(34, 34, 34)", fontWeight: "400" }}>웹훅 트리거나 웹 요청 노드 호출 시 자격 증명을 쉽게 관리하고 참조할 수 있습니다.</span></p>
- <p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(34, 34, 34)", fontWeight: "400" }}>자격 증명 저장소에서 변경사항을 업데이트하면 모든 워크플로에 자동으로 반영됩니다.</span></p>
- <p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(34, 34, 34)", fontWeight: "400" }}>OAuth 2.0, API 키 등 인증 메커니즘에 관계없이 모든 타사 호출을 수행할 수 있습니다.</span></p>

![중앙 집중식 자격 증명 저장소](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004107965/original/A3Jr7tV_bglq3JtA8AtMYyLa9Ntakna19g.png?1636380532)

## 새 자격 증명 생성 방법

### 1단계: 자격 증명 메뉴 접근
<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;1. 다음 경로로 이동하세요:&nbsp;</span><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>관리자 → 자동화 및 생산성 → 자격 증명</span></p>

<p><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007041296/original/VV9sTzUr0p2a4609QIMi6BqQa01eU1E-dA.jpeg?1669799653" style={{ width: "638px" }} className="fr-fil fr-dib" data-id="50007041296" data-attachment="[object Object]" /></p>

### 2단계: 새 자격 증명 생성
<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>&nbsp;2. &nbsp;</span><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>새 자격 증명</span><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>을 클릭하세요.</span></p>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}><span style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "169px" }}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004108065/original/rQIsXHzex3aVKhY4sJH-YJesiTnv0vy1KA.png?1636381035" className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50004108065" width="624" height="169" /></span></span></p>

### 3단계: 자격 증명 정보 입력
<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>3. &nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>이름</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>을 입력하고 자격 증명에 해당하는&nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>인증 유형</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>을 선택하세요.</span></p>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}><span style={{ border: "none", display: "inline-block", overflow: "hidden", width: "624px", height: "223px" }}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004108077/original/y-8y0FFv3DblHg9sAl2Kx9TC2SxevqyO8Q.png?1636381132" className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50004108077" width="624" height="223" /></span></span></p>

## 인증 방식별 설정 가이드

| 인증 유형 | 입력 항목 | 설명 |
| --- | --- | --- |
| Basic Auth | 사용자명: 이메일 주소 / 비밀번호: 비밀번호 | 요청에 검증된 사용자명과 비밀번호를 포함하여 전송할 때 사용합니다. 참고: Freshservice API 키 인증은 Basic Auth로 설정할 수 있으며, 사용자명=API 키, 비밀번호=x 를 사용합니다. |
| API key | 키: 타사 서비스 전용 인증 키 / 값: API 키 | 인증에 API 키가 필요한 애플리케이션 작업 시 사용합니다. |
| No Auth | - | 요청에 인증이 필요하지 않은 경우 사용합니다. |
| OAuth 2.0 | 권한 부여 유형(인증 코드, 클라이언트 자격 증명 등), 인증 URL, 액세스 토큰 URL, 클라이언트 ID/시크릿, 범위, 클라이언트 인증 방법 | 안전한 위임 액세스가 필요한 경우 사용합니다. 리디렉션 URL 예: `https://<yourdomain.freshservice.com>/api/_/credentials/oauth_callback` |

### 4단계: 자격 증명 저장 및 활용
<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>4. 필요한 세부 정보를 모두 입력한 후&nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>저장</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>을 클릭하세요.</span></p>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>5. 이제 워크플로에서&nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>웹훅 트리거</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>나&nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>웹 요청 노드</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>에서&nbsp;</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>저장된 자격 증명을 참조</span><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>할 수 있습니다.</span></p>

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span dir="ltr" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004108268/original/-ThscpPUKu-LSrjSeYXJtCpzaljzZsLd1w.png?1636382056" style={{ width: "500px" }} className="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50004108268" /></span></p>

:::tip 워크플로에서 자격 증명 참조
저장된 자격 증명은 워크플로 자동화에서 웹훅 트리거나 웹 요청 노드 실행 시 쉽게 참조할 수 있습니다.
:::

## 실무 활용 예시

## 문제 해결

### 자주 발생하는 문제

#### 문제: OAuth 2.0 인증 실패
**원인**: Redirect URL 설정 오류 또는 토큰 만료
**해결**: 
1. Redirect URL 형식 확인: `https://<yourdomain.freshservice.com>/api/_/credentials/oauth_callback`
2. 토큰 갱신 주기 점검
3. 클라이언트 ID/Secret 재확인

:::warning OAuth 설정 주의사항
OAuth 2.0 설정 시 API 제공업체의 정확한 인증 정보와 스코프를 확인해야 합니다.
:::

#### 문제: API 키 인증 오류
**원인**: 잘못된 키 값 또는 권한 부족
**해결**:
1. API 키 형식과 값 재확인
2. 해당 API의 권한 범위 점검
3. 키 만료일 확인

:::success 자격 증명 설정 완료
모든 자격 증명이 올바르게 설정되었습니다. 이제 워크플로에서 안전하게 외부 시스템과 연동할 수 있습니다.
:::