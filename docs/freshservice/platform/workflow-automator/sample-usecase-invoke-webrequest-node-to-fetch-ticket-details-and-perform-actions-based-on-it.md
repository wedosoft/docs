---
sidebar_position: 22
---

# 샘플 사용 사례 - 웹 요청 노드를 호출하여 티켓 세부 정보를 가져오고 이를 기반으로 작업 수행하기

[웹 요청 노드](https://support.freshservice.com/en/support/solutions/articles/50000003705-web-request-node)를 사용하여 Freshservice 티켓 세부 정보를 가져오는 샘플 GET 요청을 호출하고 [JSON 파서 노드](https://support.freshservice.com/en/support/solutions/articles/50000003708-json-parser-node)를 사용하여 응답 본문을 파싱하고 이를 기반으로 작업을 수행합니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


## 1단계

웹 요청 노드를 사용하여 Freshservice 티켓 세부 정보를 가져오는 샘플 GET 요청을 트리거합니다.

**참고:** 오케스트레이션 서버의 도움으로 온프레미스 네트워크로 요청을 라우팅할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573364/original/Ah_bKm1boytWApCwW0Nyl0H2sqJujhCv7A.png?1628853758" width="624" height="319" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573364" />

## 2단계

작업을 테스트하고 샘플 응답 본문을 클립보드에 복사합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573371/original/8ooFoKvS3ybyH2wwLuBmvogoRwqn_FV19g.png?1628853836" width="624" height="293" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573371" />

## 3단계

이 요청이 성공했는지 확인하기 위해 조건 블록에서 **2XX 응답**에 대한 상태 코드를 확인할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573384/original/gqQ66m7a1ka1CG5zp1lqxfN4egFNk6fS8g.png?1628853929" width="624" height="216" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573384" />

## 4단계

**JSON 파서 노드**를 캔버스에 끌어다 놓습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573386/original/q6yXOzQXrjVt1j6u_V8rLKT23S9Q8bfv5w.png?1628853968" width="624" height="249" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573386" />

## 5단계

**소스**를 웹 노드 요청의 출력에 매핑합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573390/original/0ytMaZeZzO4LRHm1m2eXB0XW3tOUe9kqbQ.png?1628854019" width="624" height="328" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573390" />

## 6단계

샘플 응답 본문을 페이로드 섹션에 붙여넣고 **출력 생성 버튼**을 눌러 페이로드 입력의 스키마를 기반으로 출력을 자동으로 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573392/original/XMbiMNRS8J_gn4Y-w3BmZTiHbPzKS04Hag.png?1628854075" width="624" height="367" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573392" />

**선택사항**: 런타임에 스키마의 다른 값이 필요한 경우 [사용자 정의 JSON Path 표현식](https://support.freshservice.com/en/support/solutions/articles/50000003708-json-parser-node)으로 출력을 생성할 수 있습니다.

예시: 1) 아래 페이로드에서 티켓과 연결된 첫 번째 자산만 필터링하려면 **$.ticket.assets[0]** JSON path 표현식을 사용할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573395/original/fko1CmqhOMEuMTUCCrPxMUwZHldMsR4ZMA.png?1628854121" width="608" height="213" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573395" />

예시: 2) 중간 영향도를 가진 티켓의 연결된 자산 이름을 필터링하려면 **$.ticket.assets[?(@.impact&lt;2)].name** JSON path 표현식을 사용할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573397/original/WlBgoqHCqYlV36X2JcQPm8h2j0cLwFZ76w.png?1628854179" width="624" height="184" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573397" />

## 7단계

후속 조건 및 작업에서 파서 노드에 정의된 모든 출력을 참조합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573406/original/91iX5Fg-wK8XFbYbMGYYf68uJAqTE4qDfQ.png?1628854222" width="659" height="261" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573406" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003573416/original/4YgsONc5DGfhuctEhtFvKqAERgLbc6lcWA.png?1628854251" width="624" height="265" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50003573416" />

이 샘플 사용 사례를 통해 웹 요청 노드와 JSON 파서 노드를 효과적으로 결합하여 동적인 워크플로우를 구성할 수 있습니다.