# Analytics 데이터를 Power BI로 내보내기

## 개요

Freshservice의 Analytics 모듈을 사용하면 서비스 데스크를 위한 직관적인 리포트를 생성할 수 있습니다. Power BI와 Freshservice를 통합하면 실행 가능한 인사이트를 사용하여 비즈니스 결과를 도출하는 광범위한 대시보드와 리포트로 분석을 확장할 수 있습니다.

## Freshservice Analytics에서 내보내기 예약하는 방법

데이터 내보내기를 예약하려면 다음 단계를 따르세요:

### 1. Analytics 접근
1. Freshservice 계정에 로그인하고 왼쪽 사이드바에서 **Analytics**를 클릭합니다.

### 2. 데이터 내보내기 설정
1. Analytics 내에서 왼쪽 하단 모서리의 설정 아이콘 <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284854/original/m_iFCyxeM38St8cNXdgJxCjvhs0gUSUVYg.png?1661765075" style="width: auto; font-family: 'Helvetica Neue';" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006284854">을 클릭하고 **데이터 내보내기**를 선택합니다.

2. 오른쪽 상단 모서리에 있는 **내보내기 생성** 옵션을 클릭하여 데이터 내보내기를 예약합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007170062/original/YJ0dSeZowduudEAuK7kRhj4vSJAIYd1yow.png?1671172887" style="width: 619px; font-family: 'Helvetica Neue';" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50007170062">

### 3. 내보내기 구성
1. **내보내기 이름과 모듈 이름**을 추가합니다. 예를 들어 **변경** 모듈에 대한 데이터 내보내기를 예약하려면 **모듈 이름**에서 변경을 선택합니다.

2. **예약 간격**을 선택합니다. **시간별**, **일별**, **주별** 또는 **월별**로 설정할 수 있습니다.

3. **보기**와 **기본 필터** 옵션을 사용하여 내보낼 데이터를 필터링합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284933/original/64WjnHKu0_CBmslkbup_0H_44XHuqCiQ1g.png?1661765436" style="width: 644px; font-family: 'Helvetica Neue';" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006284933">

### 4. 필드 및 전송 방법 선택
1. **내보낼 필드**를 선택할 수 있습니다.

2. 내보내기를 **이메일**로 받을지 **API 링크**로 받을지 선택합니다. **API URL**은 내보내기 파일에 대한 링크를 보관합니다. API URL을 BI 도구에 입력하면 Freshservice에서 자동으로 데이터를 가져올 수 있습니다.

3. 완료되면 **저장**을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284965/original/eU__A1mF-EgM2jV_4jTdY9BwDRcdwNHJ_w.png?1661765542" style="width: 670px; font-family: 'Helvetica Neue';" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006284965">

## Power BI와 Freshservice Analytics 통합 방법

### 1단계: API URL 복사
Freshservice의 Analytics 모듈에서 파일을 내보내는 링크가 포함된 API URL을 복사합니다.

> **중요 사항**: API URL에서 "https"와 기본 Freshservice URL을 사용하세요. API URL에 cname이나 'http'가 포함되어 있으면 Power BI에서 인증되지 않습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000539163/original/qvW8_ZgEBCSwpkjVVLWithiP83c4eeiKww.png?1578032999" width="600" height="338" class="fr-fic fr-bordered fr-dib" data-id="50000539163" style="font-family: 'Helvetica Neue';">

### 2단계: Power BI에서 데이터 가져오기
1. Power BI Desktop에 로그인하고 <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000535728/original/o9ljnQo-mFgPiDT6bvoQwJqc31lLKp-wbQ.png?1577959575" width="24" class="fr-fic fr-dii" data-id="50000535728" style="width: 20px; height: 20.8333px; font-family: 'Helvetica Neue';"> **데이터 가져오기**를 클릭합니다.

2. 데이터 가져오기 창에서 <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000535729/original/j83FkGfv7qPFRjsHclgF5m53XmxeG4wL8g.png?1577959575" width="21" class="fr-fic fr-dii" data-id="50000535729" style="width: 16px; height: 17.5238px; font-family: 'Helvetica Neue';"> **웹**을 선택하고 **연결**을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000539166/original/lZvaZWIr0RvlN0WWim2LvvT_epuBFIEI6Q.png?1578033008" width="624" height="351" class="fr-fic fr-bordered fr-dib" data-id="50000539166" style="font-family: 'Helvetica Neue';">

### 3단계: API URL 입력
**웹에서** 창에서 **URL** 필드에 Freshservice API URL을 붙여넣고 **확인**을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000539170/original/pJ3K3-j0ycBDAS1jwi3Tn704suaVN5jebg.png?1578033019" width="624" height="351" class="fr-fic fr-bordered fr-dib" data-id="50000539170" style="font-family: 'Helvetica Neue';">

### 4단계: 인증
사용자 이름 필드에 **FS 사용자의 API 키**를 사용하고(비밀번호는 비워둠) **연결**을 클릭합니다.

> **API 키 찾기**: Freshservice에서 오른쪽 상단의 프로필을 클릭하고 **프로필 설정**을 클릭합니다. 오른쪽 패널에서 API 키를 찾을 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000539172/original/xguVtRArS0ZINNLvqRA7UB_ZdOBL4ORnGw.png?1578033041" width="624" height="351" class="fr-fic fr-bordered fr-dib" data-id="50000539172" style="font-family: 'Helvetica Neue';">

### 5단계: 데이터 사용
이제 Freshservice 데이터 내보내기 파일을 받게 됩니다. 이 파일을 데이터 소스로 사용하여 Power BI에서 리포트 작성을 시작할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000539173/original/lRGVtpVuV8XFlKE0tnCzXVd9j6MC1-26qg.png?1578033060" width="643" height="361" class="fr-fic fr-bordered fr-dib" data-id="50000539173" style="font-family: 'Helvetica Neue';">

## 리포트 내보내기 방법

리포트를 내보내려면 제공된 "API URL"을 브라우저에 복사하여 붙여넣으세요. API URL에 Cname이 포함되어 있는 경우(yourdomain.freshservice.com이 포함되지 않은 경우) Freshservice URL로 교체하세요. 이렇게 하면 CSV 파일의 다운로드가 시작됩니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011767368/original/_JQ2VjLstGR3ukd0oW0adlFHou-s5PY_jQ.png?1715160676" style="width: 684px;" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50011767368">

## 활용 방안

Power BI와의 통합을 통해 다음과 같은 이점을 얻을 수 있습니다:

- **고급 시각화**: Power BI의 강력한 시각화 도구 활용
- **실시간 대시보드**: 자동 데이터 새로고침으로 실시간 인사이트 제공
- **고급 분석**: 복잡한 데이터 분석 및 예측 모델링
- **협업**: 팀 간 리포트 및 대시보드 공유