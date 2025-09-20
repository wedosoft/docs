---
sidebar_position: 8
---

# 예약된 워크플로우 소개

서비스 데스크를 관리하는 동안 반복되는 작업을 기억하고 주기적으로 수행하는 것은 에이전트가 다가오는 작업을 잊어버리거나 제시간에 실행하지 못할 수 있어 어려울 수 있습니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


## 예약된 워크플로우란?

예약된 워크플로우를 통해 에이전트는 워크플로우 자동화에서 특정 **시간대**와 **주기**를 지정하여 워크플로우가 **언제** 트리거될 수 있는지 제어할 수 있습니다.

예를 들어, 지금부터 2일 후 회사에 입사하는 모든 직원에 대해 매일 오전 9시에 내부 리마인더를 보내도록 워크플로우를 설정할 수 있습니다.

## 일반적인 사용 사례

→ 직원 입사/퇴사 날짜를 기반으로 직원 온보딩/오프보딩 작업 자동화  
→ 지난 30일 동안 스캔되지 않은 자산의 상태 업데이트  
→ 자산의 보증 만료일 전에 이메일 알림 발송

## 예약된 워크플로우 사용 방법

예약된 워크플로우는 **예약된 이벤트**를 기반으로 구성되고 **필수** **예약된 조건**을 가진다는 점을 제외하고는 일반 이벤트 기반 워크플로우와 모든 동일한 기능을 갖습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155146/original/uEuNg-HvbGPTBqJUhr6rabfC7cGNZ3KyTQ.gif?1660160332" style={{ width: "auto" }} class="fr-fil fr-dib" data-attachment="[object Object]" data-id="50006155146" />

### 1. 예약된 이벤트

→ 지정된 **일정**, **시간**, **시간대**를 기반으로 워크플로우가 언제 실행되어야 하는지 정의합니다  
→ 일정은 **한 번**, **매일**, **매월** 또는 **매주** 기준으로 설정할 수 있습니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155038/original/PkE5IVd2DAlr9YE5L-Z1foJ2YuCtc-Yhww.png?1660159272" width="437" height="309" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006155038" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155039/original/9Dkla9__wR5VOohC12L5GHJdxxKlBgon6Q.png?1660159272" width="455" height="306" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006155039" />

### 2. 예약된 조건

워크플로우가 실행되어야 하는 레코드를 필터링할 수 있습니다. 예: 마감일이 정확히 2일 남은 티켓만 처리

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155037/original/h_YTFd9YtJxaQ-HMWvzdbGUDoajUSLe-Fg.png?1660159269" width="624" height="340" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006155037" />

## 예약된 조건 실행

예약된 워크플로우를 실행하기 전에 다음 조건을 검토하는 것이 좋습니다.

<table style={{ border: "none", borderCollapse: "collapse", width: "100%" }}>
<tbody>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word", width: "36%" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt", textAlign: "center" }}><strong>모듈</strong></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word", width: "64%" }}>
<p style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><strong>조건 평가 기준</strong></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>티켓, 작업</p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>예약된 워크플로우는 지난 6개월 내에 생성된 <strong>미완료 티켓</strong>에서 실행되며, <strong>완료 및 해결된 티켓은 제외</strong>하고 최대 10,000개의 매칭 레코드로 제한됩니다.</p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>변경</p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>지난 6개월 내에 생성된 <strong>미완료 변경</strong>에서 평가되며 최대 10,000개의 매칭 레코드로 제한됩니다.</p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>문제</p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>지난 6개월 내에 생성된 <strong>미완료 문제</strong>에서 평가되며 최대 10,000개의 매칭 레코드로 제한됩니다.</p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>릴리스</p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>지난 6개월 내에 생성된 <strong>미완료 릴리스</strong>에서 평가되며 최대 10,000개의 매칭 레코드로 제한됩니다.</p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>자산</p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p style={{ lineHeight: "1.2", marginBottom: "0pt" }}>휴지통을 제외한 인벤토리의 <strong>모든 자산</strong>에서 평가됩니다.</p>
</td>
</tr>
</tbody>
</table>

**참고**: 티켓의 승인 상태와 관계없이 예약된 워크플로우는 이제 '승인 상태: 요청됨'으로 라벨이 지정된 모든 티켓에 대해 실행됩니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009988613/original/wBVH1CXdVvBhIWhVM47xAPdyoWOqBsASeg.png?1699449908" width="624" height="156" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50009988613" />

예약된 워크플로우에서 승인 대기 중인 티켓을 제외하려면 워크플로우에서 다음 조건을 사용하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009988626/original/AssFpQ7_-uDPmTehVtIQ0i7DUuTGHMgP1w.png?1699449959" width="602" height="273" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50009988626" />

## 예약된 워크플로우 실행 가이드라인

1. 예약된 워크플로우는 완료된 티켓에서 실행되지 않습니다.
2. 예약된 워크플로우는 6개월 이전에 생성된 티켓에서 실행되지 않습니다.
3. 6개월 기간 계산 시 고려되는 시간대는 계정의 시간대입니다.
   - 예시: 계정이 영국에 있고 티켓이 5월 1일 12:00 GMT에 생성된 경우, 워크플로우 실행 마지막 날짜는 5월 1일 12:00 GMT로부터 6개월 이내여야 합니다.
4. 참고:
   - 날짜 필드를 사용하면 시간을 제거하고 날짜로 변환하므로 일부 경우에 조건이 일치하지 않을 수 있습니다.
   - 해결 방법으로 날짜-시간 필드를 사용하고 하루 끝으로 설정하여 시간이 하루 끝으로 설정되도록 하여 전체 날짜가 기간 내에서 고려되도록 하세요.

## 사용 사례 예시

### 사례 1: 자산 보증 만료 10일 전 리마인더 알림

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155124/original/HYLgZkNv4I3SuzUQ6rjn4IV94Qoc6gJ8hw.png?1660160144" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006155124" />

1. **Admin → 자동화 및 생산성 → 자동화 → 워크플로우 자동화**로 이동합니다.
2. **새 워크플로우**를 클릭하고 사이드바 창에서 **예약된 워크플로우**를 선택합니다.
3. **제목**을 입력하고 워크플로우가 실행될 **모듈**을 선택합니다.
4. **예약된 이벤트**를 끌어다 놓아 워크플로우가 트리거되는 시기를 예약합니다.
5. **조건 블록**을 사용하여 보증 만료일이 정확히 10일 남은 자산만 필터링합니다.
6. **액션 블록**을 추가하여 에이전트 그룹/자산 관리자에게 자산 보증 갱신에 대한 리마인더 이메일을 보냅니다.

### 사례 2: 직원 입사일 2일 전 작업 자동화

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006155082/original/XamL0vXr-cIDXKRpx7B01SrhgaIT_YdH8A.png?1660159468" width="624" height="245" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006155082" />

1. **Admin → 자동화 및 생산성 → 자동화 → 워크플로우 자동화**로 이동합니다.
2. **새 워크플로우**를 클릭하고 **예약된 워크플로우**를 선택합니다.
3. **제목**을 입력하고 모듈로 **티켓**을 선택합니다.
4. **예약된 이벤트**를 끌어다 놓아 특정 시간과 주기에 워크플로우를 트리거합니다.
5. **조건 블록**을 추가하여 소스 필드를 사용해 온보딩 요청만 필터링합니다.
6. **표현식 빌더** 노드를 끌어서 직원의 입사일을 가져옵니다.
7. 입사일이 정확히 2일 남은 온보딩 티켓만 필터링하는 조건 블록을 구성합니다.
8. **액션 블록**을 끌어서 티켓에 작업과 리마인더를 추가합니다.

### 사례 3: 직원 퇴사일에 오프보딩 작업 자동화

1. **Admin → 자동화 및 생산성 → 자동화 → 워크플로우 자동화**로 이동합니다.
2. **새 워크플로우**를 클릭하고 **예약된 워크플로우**를 선택합니다.
3. **제목**을 입력하고 모듈로 **티켓**을 선택합니다.
4. **예약된 이벤트**를 끌어다 놓아 특정 시간대, 주기, 시간대에 워크플로우를 트리거합니다.
5. **조건 블록**을 추가하여 **직원 오프보딩 요청**인지 확인하고 **퇴사일이 현재 날짜와 같은지** 검증합니다.
6. 오프보딩 작업을 실행하기 위해 **액션 블록**을 추가합니다.

예약된 워크플로우를 통해 반복적인 작업을 자동화하고 시간 기반 프로세스를 효율적으로 관리할 수 있습니다.