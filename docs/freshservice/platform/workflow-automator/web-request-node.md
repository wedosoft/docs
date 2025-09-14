# 웹 요청 노드

서비스 데스크가 조직에서 사용되는 여러 도구 중 운영의 중심이 되면서, 서비스 데스크를 에코시스템과 원활하게 통합하는 것이 필수적입니다. **웹 요청 노드**를 통해 이제 [오케스트레이션 센터](https://support.freshservice.com/en/support/solutions/articles/50000002961-introducing-orchestration-center)에서 통합할 수 없는 시스템을 포함하여 모든 종류의 타사 시스템과 통합할 수 있습니다.

## 웹 요청 노드란 무엇인가요?

웹 요청 노드를 사용하면 워크플로우 자동화에서 REST API를 사용하는 모든 타사 시스템으로 API 요청을 발생시킬 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565309/original/3jX6xAWgi06hqS7PCcJgUVyZcXCAmVJqZg.png?1628764803" width="324" height="336" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565309" />

요청에서 반환된 상태 코드를 후속 조건 노드에서 참조하여 요청의 성공 또는 실패에 따라 분기할 수도 있습니다.

## 웹 요청 vs 웹훅

<div align="left" dir="ltr" style="margin-left: 0pt;">
<table style="border: none; border-collapse: collapse; table-layout: fixed; width: 468pt;">
<colgroup>
<col />
<col />
</colgroup>
<tbody>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style={{"lineHeight": "1.38", "textAlign": "center", "marginBottom": "0pt"}}>
<span>**웹 요청 노드**</span> 
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>웹훅</strong></span>
</p>
</td>
</tr>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
JSON 파서로 요청의 응답 본문을 파싱하고 후속 노드에서 응답 출력을 참조합니다.</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
웹훅에서 받은 응답을 기반으로 작업을 수행할 수 없습니다.</span>
</p>
</td>
</tr>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
응답을 받은 후에만 다음 노드로 진행합니다.</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
응답을 받지 못해도 후속 작업을 수행합니다.</span>
</p>
</td>
</tr>
</tbody>
</table>
</div>

## 인증 유형

<div align="left" dir="ltr" style="margin-left: 0pt;">
<table style="border: none; border-collapse: collapse;">
<colgroup >
<col width="157" />
<col width="234" />
<col width="261" />
</colgroup>
<tbody>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong dir="ltr">인증 유형</strong></span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 34.5001%;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong>입력</strong></span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 41.1756%;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong>설명</strong></span>
</p>
</td>
</tr>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
Basic Auth</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 34.5001%;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong>사용자명</strong></span><span style="color: rgb(0, 0, 0); font-weight: 400;">: 이메일 주소</span>
</p>
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong>비밀번호</strong></span><span style="color: rgb(0, 0, 0); font-weight: 400;">: 비밀번호</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 41.1756%;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
요청에 검증된 </span> <span style="color: rgb(0, 0, 0); font-weight: 700;"> <strong> 사용자명</strong> </span> <span dir="ltr" style="color: rgb(0, 0, 0); font-weight: 400;"> 과 </span> <span style="color: rgb(0, 0, 0); font-weight: 700;"> <strong> 비밀번호</strong> </span> <span style="color: rgb(0, 0, 0); font-weight: 400;"> 를 보내는 경우 <strong> Basic Auth</strong> 유형을 사용합니다.</span> 
</p>
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
<strong>참고</strong>: Freshservice API 키 인증은 다음 값으로 기본 인증을 사용하여 수행할 수 있습니다.</span>
</p>
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
사용자명: <strong> <API 키></strong> </span> <br /> 
비밀번호: <strong> x</strong> </span> 
</p>
</td>
</tr>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
API 키</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 34.5001%;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
<strong>키</strong></span><span style="color: rgb(0, 0, 0); font-weight: 400;">: Authorization</span><br />
<strong>값</strong></span><span style="color: rgb(0, 0, 0); font-weight: 400;">: API 키</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 41.1756%;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
인증을 위해 </span> <span style="color: rgb(0, 0, 0); font-weight: 700;"> <strong> API 키</strong> </span> <span dir="ltr" style="color: rgb(0, 0, 0); font-weight: 400;"> 가 필요한 애플리케이션에서 작업을 수행할 때 </span> <span style="color: rgb(0, 0, 0); font-weight: 700;"> <strong> API 키</strong> </span> <span style="color: rgb(0, 0, 0); font-weight: 400;"> 유형을 사용합니다.</span> 
</p>
</td>
</tr>
<tr style="height: 0pt;">
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
No Auth</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 34.5001%;">
<p dir="ltr" style="line-height: 1.2; text-align: center; margin-bottom: 0pt;">
-</span>
</p>
</td>
<td style="border-width: 1pt; border-style: solid; border-color: rgb(0, 0, 0); padding: 5pt; overflow: hidden; overflow-wrap: break-word; width: 41.1756%;">
<p dir="ltr" style="line-height: 1.2; margin-bottom: 0pt;">
요청에 인증이 필요하지 않은 경우 </span> <span style="color: rgb(0, 0, 0); font-weight: 700;"> <strong> No Auth</strong> </span> <span style="color: rgb(0, 0, 0); font-weight: 400;"> 유형을 사용합니다.</span> 
</p>
</td>
</tr>
</tbody>
</table>
</div>

사설 엔드포인트에 웹 요청 노드를 통해 액세스하려면 방화벽 제한을 우회하고 신뢰할 수 있는 요청만 처리할 수 있도록 아래 IP를 화이트리스트에 추가해 주세요.

### IP 주소 화이트리스트

<div align="left" dir="ltr" style="margin-left: 0pt;">
<table style="border: none; border-collapse: collapse; margin-right: calc(-4%); width: 104%;">
<colgroup >
<col width="112" />
<col width="134" />
<col width="112" />
<col width="111" />
<col width="119" />
<col width="37" />
</colgroup>
<tbody>
<tr style="height: 16.5pt;">
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>지역</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 23.3226%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>US</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 18.4799%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>EUC</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 22.1216%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>AU</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 17.8505%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>IND</strong></span>
</p>
</td>
</tr>
<tr style="height: 16.5pt;">
<td rowspan="4" style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
IP 주소</span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 23.3226%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
34.229.27.241</span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 18.4799%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
3.64.157.0</span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 22.1216%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
52.65.121.133</span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 17.8505%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
13.233.211.108</span>
</p>
</td>
</tr>
</tbody>
</table>
</div>

### 온프레미스 오케스트레이션 서버용 도메인 화이트리스트

<div align="left" dir="ltr" style="margin-left: 0pt;">
<table style="border: none; border-collapse: collapse;">
<colgroup >
<col width="119" />
<col width="142" />
<col width="119" />
<col width="117" />
<col width="126" />
</colgroup>
<tbody>
<tr style="height: 16.5pt;">
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>지역</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(204, 204, 204) rgb(193, 199, 208) rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 20.9748%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>US</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(204, 204, 204) rgb(193, 199, 208) rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 23.6324%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>EUC</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(204, 204, 204) rgb(193, 199, 208) rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>AU</strong></span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(204, 204, 204) rgb(193, 199, 208) rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<strong>IND</strong></span>
</p>
</td>
</tr>
<tr style="height: 16.5pt;">
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208) rgb(204, 204, 204) rgb(204, 204, 204); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
화이트리스트할 도메인명</span>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208) rgb(193, 199, 208) rgb(193, 199, 208) rgb(204, 204, 204); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 20.9748%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<a href="http://freshservice-us.freshorchestrator.com/">freshservice-us.freshorchestrator.com</a>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word; width: 23.6324%;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<a href="http://freshservice-eu.freshorchestrator.com">freshservice-eu.freshorchestrator.com</a>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<a href="http://freshservice-au.freshorchestrator.com">freshservice-au.freshorchestrator.com</a>
</p>
</td>
<td style="border-width: 0.5pt; border-style: solid; border-color: rgb(193, 199, 208); padding: 2pt; overflow: hidden; overflow-wrap: break-word;">
<p dir="ltr" style="line-height: 1.38; text-align: center; margin-bottom: 0pt;">
<a href="http://freshservice-ind.freshorchestrator.com">freshservice-ind.freshorchestrator.com</a>
</p>
</td>
</tr>
</tbody>
</table>
</div>

워크플로우에서 웹 요청 노드를 사용하는 방법을 보여주는 예시를 살펴보겠습니다.

## 샘플 사용 사례

이 예시에서는 **비밀번호 재설정** 서비스 요청을 위해 강력한 임시 비밀번호를 생성하는 웹 요청을 호출하겠습니다.

### 1단계

**이벤트 블록**에서 **티켓 생성됨**을 선택하고 **조건 블록**에서 **비밀번호 재설정**을 위한 서비스 항목을 선택합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565316/original/1F3JpcxyPmkNJS3pKgcC3KGjdGfqwX1E2A.png?1628764879" width="624" height="251" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565316" />

웹 요청 노드를 캔버스에 끌어다 놓아 사용자 정의 API 요청을 트리거하고 **인증 유형**을 **No Auth**로 설정합니다.

**참고**: [오케스트레이션 서버](https://support.freshservice.com/en/support/solutions/articles/50000003259-setting-up-the-orchestration-server)의 도움으로 온프레미스 네트워크로 요청을 라우팅할 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565321/original/W8j1fKHjNDHTmxkjHwcv5BD4PCX2nJzr5g.png?1628764971" width="624" height="269" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565321" />

### 2단계

상태 코드는 조건 블록에서 **2XX 응답**에 대해 확인하여 이 요청이 성공했는지 확인할 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565326/original/Y8v2Y-2Xvpgdy5mag28WUEhCjgky_N98dw.png?1628765037" width="624" height="225" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565326" />

### 3단계

**웹 요청 테스트** 작업을 수행하고 샘플 응답 본문을 클립보드에 복사합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003572964/original/ou6Uc6eTNqyZZnUXBZEZENfwBGcjCrq7IQ.gif?1628850387" style="width: auto;" class="fr-fil fr-dib" data-attachment="[object Object]" data-id="50003572964" />

### 4단계

**JSON 파서 노드**를 캔버스에 끌어다 놓습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565330/original/OvBiw7cqZ4kss_dMlUIlaE48hQe_a4211A.png?1628765122" width="624" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565330" style="width: 574px; height: 268.303px;" />

### 5단계

**소스**를 웹 노드 요청의 출력에 매핑합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565332/original/LLYBwVJrgwZrOnIL9j1DLoOOFGTAxNv0gg.png?1628765159" width="562" height="296" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565332" />

### 6단계

샘플 응답 본문을 페이로드 섹션에 붙여넣고 **출력 생성** 버튼을 눌러 페이로드 입력의 스키마를 기반으로 출력을 자동으로 생성합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565368/original/MWQz75U0ZtSbbUTmp9Oa3ABe11-Mxe_APA.png?1628765426" width="507" height="262" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565368" />

### 7단계

Microsoft AD에서 작업을 수행하려면 **앱 노드**를 캔버스에 끌어다 놓고 Microsoft AD에서 **비밀번호 재설정** 작업을 실행합니다.

**이름** 페이로드 전체에 각각의 사용자 정의 사용자 필드 플레이스홀더(**SamAccountName**)를 사용합니다. 새 비밀번호는 파서 필드에 정의된 출력에서 가져올 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003572946/original/6C-Y4bJwdrjAHrvwo6y_0BQKIoG4ta3Lxg.gif?1628850215" style="width: auto;" class="fr-fil fr-dib" data-attachment="[object Object]" data-id="50003572946" />

**팁**: [Discovery Probe](https://support.freshservice.com/support/solutions/articles/221819-mapping-active-directory-fields-while-importing-requesters-through-freshservice-probe)를 사용하여 SamAccountName을 Freshservice의 사용자 정의 사용자 필드와 동기화할 수 있습니다.

### 8단계

마지막으로 **계정 잠금 해제**하고 새 비밀번호와 함께 요청자에게 이메일을 보냅니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565405/original/KMii1zZJDLWYRkazY-Paqz4HTg6DL5YRHQ.png?1628765646" width="624" height="257" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565405" />

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003565407/original/FN-0UlWmbcqEnvLteACeCcBTp_YSQGnqOA.png?1628765659" width="624" height="264" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003565407" />

웹 요청 노드를 사용하여 더 많은 것을 설정할 수 있습니다.

[웹 요청 노드를 호출하여 티켓 세부 정보를 가져오고 이를 기반으로 작업을 수행하는 샘플 사용 사례](https://support.freshservice.com/en/support/solutions/articles/50000003706-sample-usecase-invoke-webrequest-node-to-fetch-ticket-details-and-perform-actions-based-on-it-)

## 자주 묻는 질문

**1. 닫힌 티켓에 누군가 답글을 달거나 공개 메모를 추가할 때마다 새 티켓을 만드는 방법은 무엇인가요?**

새 티켓을 생성하는 자동화를 만들려면 다음 단계를 따르세요:

1. **전역 설정** 또는 특정 **워크스페이스 관리자**로 이동합니다.
2. **워크플로우 자동화**로 이동하여 **새 워크플로우**를 클릭합니다.
3. 답글이 전송될 때 트리거하도록 **이벤트**를 설정합니다.
4. 상태가 **닫힘** 또는 **해결됨**인지 확인하는 **조건** 노드를 추가합니다.
5. **웹 요청** 노드를 끌어다 놓고 **POST** 호출을 사용하도록 구성합니다.
6. 다음 링크를 사용하여 API를 통해 티켓을 생성합니다: `https://api.freshservice.com/v2/#create_ticket`
7. API URL은 다음과 같아야 합니다: `your_domain.freshservice.com/api/v2/tickets`
8. 인증의 경우 관리자 API 키를 사용자명으로, 단일 알파벳(예: 'a', 'x')을 비밀번호로 사용하여 **Basic Auth**를 사용합니다.
9. 요청 본문에 모든 필수 필드가 포함되어 있는지 확인합니다. 기존 티켓이 다시 열리지 않도록 하려면 티켓 재오픈을 담당하는 워크플로우를 비활성화해 주세요.