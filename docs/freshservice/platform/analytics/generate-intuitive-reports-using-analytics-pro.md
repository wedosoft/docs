# Analytics Pro를 사용한 직관적인 리포트 생성

Freshservice의 Analytics는 서비스 데스크를 위한 직관적인 리포트를 생성할 수 있게 해주며, 서비스 요청 및 서비스 아이템에 대한 지속적인 추적과 측정을 지원합니다.

## 소개

이 문서는 Analytics 모듈의 기본 사항과 리포트를 생성하고 맞춤 설정하는 방법에 대해 설명합니다.

## 용어 정리

Analytics 모듈을 사용하기 전에 다음 중요한 용어들을 이해해야 합니다:

**Analytics Home** - 본인이나 다른 사용자가 생성한 모든 리포트가 포함된 공간입니다.

**위젯(Widget)** - 특정 시각적 형식(파이 차트, 막대 그래프 등)으로 데이터를 표시하는 분석 차트입니다.

**리포트(Report)** - 다양한 위젯을 포함하는 대시보드입니다. 예를 들어 "티켓 개요" 리포트를 생성하여 모든 티켓 관련 위젯을 포함시킬 수 있습니다. 이 리포트는 티켓 상황에 대한 완전한 개요를 제공합니다.

## Analytics 접근하기

Analytics에 접근하려면 좌측 사이드바의 Reports 아이콘에 마우스를 올리고 Analytics를 클릭합니다.

**참고사항**: 이 기능은 **Admin → Roles → Reports**에서 찾을 수 있는 "view analytics" 권한이 있는 사용자만 접근할 수 있습니다. 또한 이 권한에는 글로벌 범위가 적용됩니다.

## 리포트 생성하기

### 리포트에 위젯 추가하기

리포트를 생성하려면:

1. **Reports > Analytics**로 이동하여 오른쪽 상단의 **New Report**를 클릭합니다.
2. 사용 가능한 위젯 목록이 표시됩니다. **Untitled Report**를 클릭하여 위젯 이름을 추가합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006241417/original/DWP6xFI_QM7-sk1ysk9V-2mFrj78kIIAOA.png?1661243942" style={{ width: "606px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006241417" />

3. 다음 방법으로 위젯을 찾을 수 있습니다:

**처음부터 생성하기** - 중앙 창에 필요한 위젯을 드래그 앤 드롭합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242905/original/VZRqnykAobXXMlQ-4LeZAV8wThoWtlS8Ug.png?1661250485" style={{ width: "207px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006242905" />

**검색 바** - 사용 가능한 매개변수를 기반으로 시스템이 자동 생성한 위젯을 검색할 수 있습니다. 원하는 위젯을 찾으면 리포트에 드래그하여 배치합니다.

**갤러리** - 기존 위젯에서 선택할 수 있습니다. 왼쪽의 **GALLERY** 옵션을 클릭하고 드롭다운에서 **Tickets** 또는 **Changes** 등 원하는 모듈을 선택합니다. 원하는 위젯을 드래그하여 리포트에 배치합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006241558/original/mZHgv0KY339kl6XATw7hTaDk7DxIFn3lPQ.png?1661244735" style={{ width: "591px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006241558" />

위젯을 추가한 후에는 리포트가 준비됩니다. **Analytics Home**에서 접근할 수 있습니다.

### 리포트 관리하기

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242220/original/akf0wdClT4T6nuyFmsCdS5yWuK00EZx3Hg.png?1661247460" style={{ width: "663px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006242220" />

- **Help** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242658/original/9B6Aqcz4kdiXaoMmN8sX8NOhFvJgeAwtZQ.png?1661249464" style={{ width: "29px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242658" /> 에는 모듈 탐색을 쉽게 도와주는 특별 투어와 FAQ가 포함되어 있습니다.

- **Share** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242709/original/L9RFwKhXWHlgj1_sP4T54yC7DZISE0zgLw.png?1661249649" style={{ width: "29px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242709" /> 는 analytics에 접근 권한이 있는 다른 사용자와 리포트를 공유하는 데 사용됩니다.

- **Export, Schedule, Subscribe** <img data-id="50000505239" className="fr-fic fr-dii" height="21" width="24" src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000505239/original/FNm9Z_9533lDOq3OerU8Oe3lvq5M4QV97A.png?1576646972" /> 는 현재 리포트를 PDF 파일로 이메일로 내보내거나, 정기적으로 본인이나 다른 사람의 이메일로 전송하도록 예약하거나 구독하는 데 사용됩니다.

- **Present** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242727/original/fg54ltp7Giw_jcBObHFnNodGPUilah76qg.png?1661249729" style={{ width: "23px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242727" /> 는 리포트를 발표하기 위한 전체 화면 프레젠테이션 모드를 활성화합니다. Exit 아이콘을 클릭하여 전체 화면 모드에서 나올 수 있습니다.

#### 리포트 구성 옵션

- 위젯을 더 추가하려면 화면 오른쪽 상단의 **+ADD WIDGET** 버튼을 클릭합니다.

- **Configure** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242953/original/AoFAka14RbaNX-EVul2L1OQloQpZL-tfVw.png?1661250776" style={{ width: "19px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242953" /> 는 리포트의 레이아웃과 그리드 설정을 구성하는 데 사용됩니다. 기본적으로 리포트와 위젯의 레이아웃은 16 X 9입니다.

- **Filter** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242778/original/1D1CBWDiWPUVPUBvJ4u-FVmg8XsKY032pg.png?1661249953" style={{ width: "20px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242778" /> 는 기준에 따라 위젯 필터, 페이지 필터 또는 리포트 필터를 추가하는 데 사용됩니다.

- **Style** <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242840/original/rDs6e3qvaNBD6gmBhPgqZ4cHqcVAHreKJw.png?1661250245" style={{ width: "20px" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006242840" /> 는 위젯에 스타일과 설명을 추가하는 데 사용됩니다. 개별 위젯에 스타일을 추가하면서 위젯 설명도 여기서 추가할 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006242607/original/hZdR-0vnRzgLwJB3U3YlbZ-msHpuhNX5SQ.png?1661249164" style={{ width: "662px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006242607" />

### Ask Freddy로 빠른 인사이트 얻기

Freshservice는 ML 기반의 **Ask Freddy** 기능을 제공합니다. 이는 자연어 처리 알고리즘을 사용하여 Freddy에게 간단히 질문을 던지는 것만으로 위젯을 생성합니다. 예를 들어, "상담원별 티켓 평균 해결 시간은 얼마인가요?"라고 질문할 수 있습니다. Freddy는 적절한 기준을 적용하여 질문을 처리하고 즉시 결과를 반환합니다.

**어디서 찾을 수 있나요?**

1. Analytics 탭으로 이동하여 상단의 **Ask Freddy** 바를 찾습니다.
2. Ask Freddy 바를 클릭하면 드롭다운 메뉴에서 최근 검색 쿼리와 FAQ를 찾을 수 있습니다. Ask 바에 질문을 입력하고 **Ask**를 클릭하거나 Enter를 눌러 위젯을 생성합니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008613609/original/3THTeb2WGS3Un3oPClrgekQjgxHdGep8zw.png?1686729824" style={{ width: "auto" }} class="fr-fil fr-dib" data-attachment="[object Object]" data-id="50008613609" />

Ask Freddy에 대한 자세한 내용은 [여기](https://support.freshservice.com/en/support/solutions/articles/50000000062-get-quick-service-desk-metrics-with-freddy)를 클릭하세요.

## 즉석 리포트 생성

Analytics 모듈에서 지원하는 다양한 위젯을 사용하여 과거 데이터로부터 유연하고 즉석적인 관리 리포트를 생성할 수 있습니다.

<img data-id="50000505314" class="fr-fic fr-dib fr-bordered" height="319" width="624" src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000505314/original/DkOtzU21ZCMlqW9okhLu1dYUwm_S1LVpRg.png?1576647669" />

## 위젯 편집하기

모든 위젯은 서비스 데스크 데이터의 시각적 표현입니다. 데이터를 자세히 보거나 위젯을 변경하려면 위젯을 클릭해야 합니다.

리포트에서 위젯을 클릭하면 위젯을 확장하거나, 필터를 추가/수정하거나, 내보내기, 구독 또는 기반 데이터를 확인할 수 있는 몇 가지 옵션이 나타납니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006243004/original/YBCvOrWVuu6loYsuXPhgN_HKcaAuLXBoFA.png?1661251112" style={{ width: "355px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50006243004" />

위젯을 편집하거나 수정하려면 **expand** 아이콘 <img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006243033/original/jlR6gHnrPT7LTpIUP7vhPg_V3tAMC9Ry7g.png?1661251233" style={{ width: "auto" }} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50006243033" /> 를 클릭합니다.

### 차트 유형 변경하기

차트 유형을 변경하려면:

1. 차트 유형을 변경하려는 위젯을 클릭하고 확장 옵션을 선택합니다.
2. 다음 페이지로 이동하면 오른쪽 상단에서 다양한 차트 유형을 볼 수 있습니다.

<img src="https:/s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005794248/original/5IOmRZUPShfBHyBc_SWGj9r8x-beUStaDw.png?1656393770" style={{ width: "621px" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50005794248" />

다음 차트 유형 중에서 선택할 수 있습니다: **막대 그래프, 누적 막대 그래프, 파이 차트, 히트맵**.

원하는 차트를 클릭하면 위젯이 해당 차트 유형으로 정보를 표시합니다.

## 자주 묻는 질문

### 1. 리포트의 기반 데이터나 필드 컬럼을 어떻게 볼 수 있나요?

Analytics 모듈로 이동하여 해당 **Analytics 리포트 &gt; 기반 데이터가 필요한 위젯 확장 > Summary Table 옆의 Underlying Data**를 선택합니다. 리포트 편집 옵션을 클릭하여 기반 데이터에 추가 필드를 추가할 수도 있습니다.

### 2. 특정 서비스 카탈로그 아이템의 모든 사용자 정의 필드 정보가 포함된 리포트를 생성하려면?

Analytics 모듈로 이동하여 **Add Widgets > 메트릭 추가**를 통해 새 위젯을 생성합니다. 기반 데이터를 활용하여 **"add column"**을 선택하여 추가 사용자 정의 필드를 포함시킵니다.

### 3. Analytics에서 총 티켓 수/자산 수가 다른 이유는?

필터 적용, 시간 범위 선택의 차이 때문일 수 있습니다. **메트릭 내 설정된 날짜 범위의 충돌**을 확인하고, Filter 아이콘을 클릭하여 **Basic, Page, Report 필터**를 검토하세요.

### 4. Analytics 리포트를 대시보드에 추가할 수 있나요?

아니요, Freshservice에서는 이것들이 별도의 모듈이므로 Analytics 리포트를 대시보드에 추가할 수 없습니다. Analytics 리포트는 Analytics 모듈 내에서만 볼 수 있습니다.

### 5. SLA 위반 티켓을 Analytics 리포트에서 어떻게 조회하나요?

Analytics 리포트로 이동하여 메트릭을 **"Resolution SLA Violated Tickets"**로 설정한 새 위젯을 생성합니다. 필요에 따라 추가 필터와 그룹핑을 선택적으로 추가할 수 있습니다.

이 가이드를 통해 Freshservice Analytics Pro의 강력한 기능을 활용하여 조직의 서비스 데스크 성과를 체계적으로 분석하고 개선할 수 있습니다.