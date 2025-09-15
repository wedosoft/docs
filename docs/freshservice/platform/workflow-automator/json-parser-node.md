# JSON 파서 노드

JSON 파서 노드를 사용하면 워크플로우 컨텍스트 내에서 모든 JSON 페이로드를 파싱하고 후속 조건 및 작업에서 출력을 사용할 수 있습니다.

지금 바로 JSON 파서 노드를 사용하여 GSuite, Okta 및 JIRA에서 사용자 정의 속성을 가져오는 앱 작업의 JSON 출력을 작업할 수 있으며, 향후에는 워크플로우 자동화 내에서 REST API 응답을 파싱하는 데도 사용할 수 있습니다.

## JSON 파서 노드 사용 방법

### 1. 워크플로우에 JSON 파서 노드 추가

워크플로우 캔버스에 JSON 파서 노드를 끌어다 놓으면 다음과 같은 구성 옵션이 표시됩니다:

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003121855/original/GPtnYkIg7iO8k9LTu_kDs76egq9LozU8vA.png?1622699360" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50003121855" />

**왼쪽:** 페이로드의 소스와 샘플 JSON 페이로드가 구성됩니다  
**오른쪽:** 출력을 자동으로 생성하거나 JSON path 표현식을 사용하여 수동으로 구성할 수 있습니다

### 2. 소스 매핑

JSON 파서 노드의 **소스**를 이전 노드(예: 앱 작업, 웹 요청 노드)의 출력에 매핑합니다.

### 3. 샘플 JSON 페이로드 제공

파싱할 JSON의 구조를 정의하기 위해 샘플 JSON 페이로드를 제공합니다. 이는 출력 스키마를 자동으로 생성하는 데 사용됩니다.

### 4. 출력 생성

두 가지 방법으로 출력을 생성할 수 있습니다:

#### 자동 출력 생성
**출력 생성** 버튼을 클릭하여 제공된 샘플 JSON 페이로드를 기반으로 출력을 자동으로 생성합니다.

#### 사용자 정의 JSON Path 표현식
특정 값이 필요한 경우 사용자 정의 JSON Path 표현식을 사용하여 출력을 생성할 수 있습니다.

**예시:**
- 첫 번째 자산만 필터링: `$.ticket.assets[0]`
- 중간 영향도를 가진 자산 이름 필터링: `$.ticket.assets[?(@.impact&lt;2)].name`

### 5. 후속 노드에서 출력 사용

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003121877/original/litu3FyYnd1r0iwnY_UxQb5M4vnKpU7P_g.png?1622699488" style={{ width: "auto" }} class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50003121877" />

JSON 파서 노드에서 구성된 출력을 후속 노드에서 참조하고 사용할 수 있습니다.

## 사용 사례

### 앱 작업 JSON 출력 파싱
GSuite, Okta, JIRA 등의 앱 작업에서 반환되는 사용자 정의 속성을 포함한 JSON 응답을 파싱하여 워크플로우에서 활용할 수 있습니다.

### 웹 요청 응답 파싱
웹 요청 노드에서 받은 API 응답을 파싱하여 특정 데이터를 추출하고 후속 작업에서 사용할 수 있습니다.

### 복잡한 데이터 구조 처리
중첩된 JSON 구조에서 특정 값을 추출하여 조건부 로직이나 데이터 변환에 활용할 수 있습니다.

## JSON Path 표현식 예시

### 기본 필드 접근
```json
&#123;
  "user": &#123;
    "name": "홍길동",
    "email": "hong@example.com"
  &#125;
&#125;
```
- 사용자 이름: `$.user.name`
- 이메일: `$.user.email`

### 배열 요소 접근
```json
{
  "tickets": [
    {"id": 1, "priority": "high"},
    {"id": 2, "priority": "low"}
  ]
}
```
- 첫 번째 티켓: `$.tickets[0]`
- 모든 티켓 ID: `$.tickets[*].id`

### 조건부 필터링
```json
&#123;
  "assets": [
    &#123;"name": "서버A", "status": "active"&#125;,
    &#123;"name": "서버B", "status": "inactive"&#125;
  ]
&#125;
```
- 활성 자산만: `$.assets[?(@.status=='active')]`
- 활성 자산의 이름: `$.assets[?(@.status=='active')].name`

## 모범 사례

1. **샘플 데이터 사용**: 정확한 출력 생성을 위해 실제 예상 JSON 구조와 유사한 샘플 데이터를 제공하세요.

2. **명확한 출력 이름**: 후속 노드에서 쉽게 식별할 수 있도록 출력에 명확하고 설명적인 이름을 사용하세요.

3. **오류 처리**: JSON 구조가 예상과 다를 수 있으므로 조건 노드를 사용하여 출력 값의 존재 여부를 확인하세요.

4. **성능 고려**: 큰 JSON 페이로드의 경우 필요한 데이터만 추출하는 특정 JSON Path를 사용하세요.

JSON 파서 노드를 효과적으로 활용하면 워크플로우에서 복잡한 JSON 데이터를 처리하고 동적인 자동화를 구현할 수 있습니다.