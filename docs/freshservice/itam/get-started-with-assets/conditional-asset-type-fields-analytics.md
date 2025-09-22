---
sidebar_position: 20
---

# 분석에서 조건부 자산 유형 필드를 활용하여 주요 사용 사례 충족

## 목차

- [소개](#소개)
- [사용 사례 1. 시리얼 번호가 없는 하드웨어 자산 식별](#사용-사례-1-시리얼-번호가-없는-하드웨어-자산-식별)
- [사용 사례 2. 시리얼 번호와 함께 자산 유형별 하드웨어 하위 모든 자산 나열](#사용-사례-2-시리얼-번호와-함께-자산-유형별-하드웨어-하위-모든-자산-나열)
- [사용 사례 3. 유형별 특정 필드와 함께 여러 자산 유형을 내보내도록 데이터 내보내기 구성](#사용-사례-3-유형별-특정-필드와-함께-여러-자산-유형을-내보내도록-데이터-내보내기-구성)

## 소개

자산 필드는 각 유형에 특정하며 특정 필터가 적용될 때 분석에서 조건부로 나타납니다. 이 개념을 명확히 하는 데 도움이 되는 몇 가지 예시는 다음과 같습니다:

## 사용 사례 1. 시리얼 번호가 없는 하드웨어 자산 식별

1. **Admin → Reporting → Analytics**로 이동하여 사용자 정의 보고서를 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312683/original/N6ntcCq1rfn7IK0AbzZVWOpdqGT5cQ3apw.png?1719813802"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312683" />

2. 오른쪽 상단 모서리에서 **New Report**를 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312692/original/F1tW2pD5VPp3TYN55vTmYmcEwN9yuyvSMw.png?1719813803"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312692" />

3. 위젯을 끌어다 놓아 보고서를 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312686/original/ChmP133X685m3RzPhbDJnnJ0BBhIBvUVKw.png?1719813802"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312686" />

4. 드롭다운 필드에서 자산 메트릭을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312682/original/ZqFbNzUKUZkXVCwflvJAeqsxfZgFLdTijA.png?1719813800"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312682" />

5. 필터 아이콘을 클릭하고 아래 조건을 사용하여 시리얼 번호가 없는 하드웨어 자산을 보고합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312693/original/yHs6DJVF60eJHnJJOviH0jI9PoX8YCZp4w.png?1719813803"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312693" />

**필터 조건 참고사항:**

- **CI type is Hardware** - 시리얼 번호와 같은 모든 하드웨어 특정 속성이 표 형식 보기, 필터 및 그룹화에서 보고서에 사용할 수 있도록 보장합니다.

- **Asset Family list includes Hardware** - Computer, Laptop 등과 같은 관련 하위 유형과 함께 Hardware 유형의 자산 목록을 제공합니다.

- **2개 필터 그룹 간 Match Any** - 첫 번째 그룹은 하드웨어 속성이 보고서 내에서 사용 가능하도록 보장하고 두 번째 필터 그룹은 빈 시리얼 번호가 있는 하드웨어 하위의 모든 자산을 표시합니다.

**자산 유형 필드의 조건부 특성**: 특정 자산 유형을 기반으로 사용자 정의 필드를 필터링하려면 다음 조건을 지정해야 합니다: "CI type is &lt;자산 유형&gt;". 예를 들어, 노트북 자산의 사용자 정의 필드를 필터링하려면 "CI type is Laptop" 조건을 지정하여 노트북과 관련된 특정 필드에 액세스합니다.

5. 마지막으로 시리얼 번호를 기준으로 자산을 그룹화합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312691/original/UC0ZbXMfNF4rwGRl2ScJpJ2JYSoFz7Y5uQ.png?1719813803"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312691" />

## 사용 사례 2. 시리얼 번호와 함께 자산 유형별 하드웨어 하위 모든 자산 나열

1. Assets를 메트릭으로 사용하여 아래 스크린샷과 같이 고급 필터를 설정합니다:

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312681/original/h_mpz2gDEyOWmvFXzV47jjWpYU3jUuxheQ.png?1719813800"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312681" />

2. 이제 CI type으로 그룹화합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312677/original/kUYfK9E5rh6VMn0K8I3iNzDKvCW9BOWegQ.png?1719813798"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312677" />

3. 기본 데이터에서 시리얼 번호와 같은 하드웨어 특정 속성에 액세스합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312688/original/YEsl96r0zb6Xe6DxSTPx0VixdFyfysK3iQ.png?1719813803"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312688" />

## 사용 사례 3. 유형별 특정 필드와 함께 여러 자산 유형을 내보내도록 데이터 내보내기 구성

1. 다음 필터로 자산에 대한 데이터 내보내기를 설정합니다. 아래 예시에서는 Hardware와 Cloud 유형 하위의 모든 자산을 내보내려고 하지만 OS name, IMEI number, Serial Number, Instance ID와 같은 특정 속성도 추출합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312678/original/xFdf1mE5yBN2JnVou-Xfl0ZadSOwu-WQnA.png?1719813799"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312678" />

2. **내보내기에 필요한 유형별 특정 필드를 선택합니다.**

1단계에서 필터를 설정하고 적용한 후 자산 유형과 해당 유형별 특정 필드가 어떻게 사용 가능한지 확인하세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312687/original/lKEDnPrywl6_U1F0wadJJRABn8_bmVT5ZQ.png?1719813803"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312687" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012312680/original/wshX8v1BbBBuMsxm7xcB39mCewYQzNFyWw.png?1719813800"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012312680" />