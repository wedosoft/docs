# 서비스 카탈로그 FAQ

Freshservice의 서비스 카탈로그 설정, 관리, 사용자 정의에 대한 자주 묻는 질문들입니다. 서비스 항목 생성, 사용자 그룹 관리, 가시성 제어 등 다양한 기능을 다룹니다.

<details>
<summary><strong>서비스 카탈로그에서 서비스 카테고리를 추가하는 방법은?</strong></summary>

**질문:** 서비스 카탈로그에서 서비스 카테고리를 추가하는 방법은?

**답변:** 서비스 카테고리는 관련 서비스 항목들을 체계적으로 분류하고 구성하는 데 사용됩니다. 사용자가 필요한 서비스를 쉽게 찾을 수 있도록 구조화된 서비스 카탈로그를 제공합니다.

## 서비스 카테고리 추가 절차

### 1. 관리자 접근
```
경로: Admin → Service Management → Service Request Management → Service Catalog

다중 워크스페이스인 경우:
Admin → {워크스페이스명} → Service Management → Service Request Management → Service Catalog
```

### 2. 새 카테고리 생성
```
단계:
1. "Add New" 드롭다운 클릭
2. "Service Category" 선택
3. 카테고리명과 설명 입력
4. "Create" 클릭하여 생성 완료
```

## 카테고리 구성 모범 사례

### 추천 카테고리 구조
```
✅ IT Support
  - Hardware & Equipment
  - Software & Applications
  - Network & Connectivity

✅ HR Services
  - Employee Services
  - Benefits & Payroll
  - Training & Development

✅ Facilities
  - Office Services
  - Meeting & Events
  - Security & Access

✅ Business Applications
  - ERP Systems
  - CRM Tools
  - Financial Systems
```

### 피해야 할 카테고리명
```
❌ Miscellaneous Items
❌ Other Requests
❌ General Support
```

## 카테고리 관리 팁

### 계층 구조 설계
- **최대 3-4레벨 깊이** 권장
- **카테고리당 5-10개 항목** 적정
- **논리적 그룹핑** 중심으로 구성

### 네이밍 규칙
- **사용자 친화적** 명칭 사용
- **일관된 형식** 유지
- **검색 가능한 키워드** 포함

### 정기적 검토
- **월별 사용 현황** 분석
- **불필요한 카테고리** 정리
- **사용자 피드백** 반영

## 워크스페이스별 관리

### 다중 워크스페이스 환경
- **각 워크스페이스마다** 독립적인 서비스 항목 목록 관리
- **워크스페이스 생성 순서**에 따라 포털 표시 순서 결정
- **워크스페이스 레벨**에서 카테고리 및 항목 순서 설정 가능

효과적인 서비스 카테고리 구성을 통해 사용자 경험을 향상시키고 IT 서비스 관리의 효율성을 높일 수 있습니다.

</details>

<details>
<summary><strong>서비스 카탈로그에 새 서비스 항목을 추가하는 방법은?</strong></summary>

**질문:** 서비스 카탈로그에 새 서비스 항목을 추가하는 방법은?

**답변:** 서비스 항목은 사용자가 요청할 수 있는 개별 서비스나 리소스를 의미합니다. 체계적인 설정을 통해 효율적인 서비스 요청 프로세스를 구축할 수 있습니다.

## 서비스 항목 추가 단계

### 1. 기본 설정 단계
```
접근 경로:
Admin → Service Management → Service Request Management → Service Catalog

실행:
1. "Add New" 드롭다운에서 "Service Item" 선택
2. 기본 정보 섹션 작성
```

### 2. 일반 정보 설정
```
필수 정보:
✅ Item Name: 명확하고 이해하기 쉬운 이름
✅ Service Category: 적절한 카테고리 선택
✅ Short Description: 간단한 서비스 설명
✅ Detailed Description: 상세한 서비스 정보

선택 정보:
- Cost (USD): 서비스 비용
- Estimated Delivery (시간): 예상 배송 시간
- Requested for: 요청 대상 설정
- Visible in portal: 포털 표시 여부
```

### 3. 커스텀 필드 구성
```
사용 가능한 필드 유형:
- Text: 단순 텍스트 입력
- Paragraph Text: 긴 텍스트 입력
- Checkbox: 체크박스 선택
- Dropdown: 드롭다운 선택
- Date: 날짜 선택
- Number: 숫자 입력
- Lookup Fields: 계층적 관계 설정
- Content Fields: 리치 텍스트 섹션
```

### 4. 커스텀 필드 설정 방법
```
단계:
1. Custom Fields 섹션에서 필요한 필드 유형 선택
2. "Drag and drop fields here" 영역으로 드래그
3. 필드 속성 정의:
   - Field Label: 필드명
   - Placeholder Text: 안내 텍스트
   - Required: 필수 입력 여부
   - Default Value: 기본값 설정
4. 접근 권한 및 동작 설정:
   - Display to Requester: 요청자 표시 여부
   - Requester can edit: 요청자 편집 가능 여부
```

## 고급 기능 설정

### 추가 항목 (Additional Items)
```
기능:
- 메인 서비스와 함께 요청할 수 있는 관련 서비스 검색 및 포함
- 보조 항목 선택으로 서비스 요청 효율성 향상
- 여러 요청 생성 필요성 제거

설정 옵션:
✅ 필수 추가 항목 지정
✅ 항목 삭제 기능
✅ 개별 하위 티켓 생성 옵션
✅ 단일 서비스 요청으로 통합 처리 옵션
```

### 서비스 항목 설정
```
이행 옵션:
- Asset Type: 자산 유형 선택
- Product: 제품 선택 (하드웨어/소프트웨어 요청 시)

가시성 옵션:
- 특정 요청자 그룹으로 제한
- Agent Groups/Requester Groups 기반 접근 제어

커스터마이징:
- 서비스 요청 제목 형식 정의
- 자동 할당 규칙 연결
```

## 저장 및 게시

### 저장 옵션
```
Save & Publish: 즉시 활성화하여 사용자에게 제공
Save as Draft: 나중에 검토하고 수정하기 위해 임시 저장
```

### 품질 검증 체크리스트
```
게시 전 확인사항:
✅ 서비스명이 명확하고 이해하기 쉬운가?
✅ 필수 필드가 적절히 설정되었는가?
✅ 가시성 설정이 올바른가?
✅ 예상 처리 시간이 합리적인가?
✅ 승인 프로세스가 필요한가?
✅ 연관 서비스가 적절히 연결되었는가?
```

## 모범 사례

### 서비스 설계 원칙
```
사용자 중심:
- 기술 용어보다 사용자 친화적 명칭 사용
- 최소한의 필드로 필요한 정보만 수집
- 명확한 라벨과 도움말 텍스트 제공

효율성 향상:
- 일반적인 선택사항에 기본값 제공
- 논리적 정보 입력 흐름 고려
- 자동화 가능 부분 식별 및 연결
```

체계적인 서비스 항목 설정을 통해 사용자 만족도를 높이고 IT 서비스 제공의 효율성을 극대화할 수 있습니다.

</details>

<details>
<summary><strong>서비스 요청 시 요청자가 시간 정보를 볼 수 있도록 하는 방법은?</strong></summary>

**질문:** 서비스 요청 시 요청자가 시간 정보를 볼 수 있도록 하는 방법은?

**답변:** 서비스 요청 양식에서 시간 정보가 표시되지 않는 문제는 주로 카탈로그 항목 필드의 "Request time information" 옵션 설정과 관련이 있습니다.

## 문제 상황 및 원인

### 일반적인 문제
```
증상: 요청자가 서비스 요청 시 시간 관련 필드를 볼 수 없음
원인: "Request time information" 옵션이 활성화되지 않음
제약: 기존 카탈로그 항목 필드에서는 이 설정을 수정할 수 없음
```

### 해결 방법 개요
```
해결책: 새로운 Date 필드 생성 필요
접근법: "Request time information" 옵션이 활성화된 새 필드 추가
```

## 단계별 해결 방법

### 1. 워크스페이스 관리자 접근
```
다중 워크스페이스 환경:
경로: Admin → {워크스페이스명} → Service Catalog

단일 워크스페이스 환경:
경로: Admin → Service Catalog
```

### 2. 카탈로그 항목 선택
```
단계:
1. 문제가 발생한 서비스 항목 선택
2. 편집 모드로 전환
3. Custom Fields 섹션으로 이동
```

### 3. 새 날짜 필드 생성
```
필드 생성:
1. Date 필드 유형 선택
2. 필드를 양식으로 드래그 앤 드롭
3. 필드 속성 설정
```

### 4. 시간 정보 옵션 활성화
```
중요 설정:
✅ Field Type: Date
✅ "Request time information" 체크박스 선택
✅ Display to Requester: 활성화
✅ Required: 필요에 따라 설정

추가 설정:
- Field Label: 명확한 레이블 설정
- Help Text: 사용자 안내 텍스트
- Default Value: 기본값 (필요시)
```

## 필드 설정 세부사항

### 시간 정보 필드 유형
```
Time Only: 시간만 입력 (HH:MM)
Date Only: 날짜만 입력 (YYYY-MM-DD)
Date and Time: 날짜와 시간 모두 입력
```

### 사용자 경험 최적화
```
레이블 예시:
✅ "서비스 제공 희망 시간"
✅ "설치 예약 일시"
✅ "점검 희망 날짜"

도움말 텍스트 예시:
- "업무 시간 내 서비스 제공을 위해 선택해 주세요"
- "평일 09:00-18:00 시간대를 권장합니다"
- "긴급 상황시 즉시 연락 가능한 시간을 입력하세요"
```

## 검증 및 테스트

### 설정 확인 방법
```
테스트 절차:
1. 서비스 항목 저장 및 게시
2. 요청자 계정으로 포털 접속
3. 해당 서비스 요청 페이지 확인
4. 시간 정보 필드 표시 여부 검증
```

### 문제 해결 체크리스트
```
확인 항목:
✅ "Request time information" 옵션이 체크되어 있는가?
✅ "Display to Requester"가 활성화되어 있는가?
✅ 필드가 올바른 위치에 배치되어 있는가?
✅ 필드 권한 설정이 적절한가?
✅ 캐시가 지워졌는가?
```

## 고급 활용 방안

### 시간 기반 자동화
```
워크플로우 연계:
- 요청 시간에 따른 자동 할당
- 업무 시간 외 요청의 다음 날 처리
- 긴급 요청의 즉시 알림 설정
```

### SLA 연동
```
시간 기반 SLA:
- 요청 시간에 따른 처리 목표 시간 조정
- 업무 시간 계산 적용
- 휴일/주말 제외 처리
```

### 보고 및 분석
```
시간 데이터 활용:
- 서비스 요청 패턴 분석
- 피크 시간대 식별
- 리소스 배치 최적화
```

이러한 설정을 통해 사용자는 서비스 요청 시 원하는 시간 정보를 명확히 전달할 수 있으며, IT 팀은 더욱 효율적인 서비스 제공이 가능해집니다.

</details>

<details>
<summary><strong>티켓 생성 후 요청 항목 섹션에서 Content 필드가 보이지 않는 이유는?</strong></summary>

**질문:** 티켓 생성 후 요청 항목 섹션에서 Content 필드가 보이지 않는 이유는?

**답변:** Content 필드는 기본적으로 요청 제출 시에만 표시되며, 티켓의 요청 항목(Requested Item) 섹션에는 표시되지 않도록 설계되어 있습니다.

## Content 필드 표시 동작

### 기본 동작 방식
```
요청 제출 시: ✅ Content 필드 표시됨
티켓 생성 후: ❌ Requested Item 섹션에서 숨김
```

### 설계 의도
```
목적:
- 요청 시점의 정보 수집에 집중
- 티켓 관리 화면의 간소화
- 중요 정보와 상세 정보의 분리
```

## Content 필드의 역할

### 요청 단계에서의 기능
```
사용 용도:
- 상세한 요청 사항 설명
- 특별 지시사항 입력
- 추가 컨텍스트 제공
- 첨부 파일 설명
```

### 정보 보존 방식
```
데이터 저장:
- 입력된 내용은 티켓 내부에 저장됨
- 티켓 설명이나 초기 메모로 통합
- 에이전트는 티켓 상세에서 확인 가능
```

## 대안 솔루션

### 1. 커스텀 필드 활용
```
해결 방법:
1. Admin → Service Catalog → 해당 서비스 항목 편집
2. Custom Fields에서 "Paragraph Text" 필드 추가
3. 필드 속성 설정:
   - Display to Requester: 활성화
   - Show in Requested Item: 활성화 (가능한 경우)
```

### 2. 필드 가시성 설정
```
설정 옵션:
✅ "Display to Requester": 요청자 화면 표시
✅ "Display to Agent": 에이전트 화면 표시
✅ "Show in Summary": 요약 섹션 표시
✅ "Required Field": 필수 입력 설정
```

### 3. 티켓 템플릿 활용
```
템플릿 구성:
- 중요 정보를 티켓 설명으로 자동 이동
- 표준화된 정보 구조 적용
- 에이전트 작업 효율성 향상
```

## 정보 접근 방법

### 에이전트 관점
```
Content 정보 확인 위치:
1. 티켓 Description 섹션
2. Initial Notes 영역
3. Request Details 탭
4. Activity Timeline의 초기 항목
```

### 요청자 관점
```
제출 후 확인 방법:
1. 티켓 상세 페이지 접속
2. Request Summary 섹션
3. 이메일 확인서의 내용 요약
```

## 모범 사례

### 필드 설계 전략
```
권장 방법:
1. 핵심 정보는 별도 필수 필드로 분리
2. Content는 보조 설명용으로 활용
3. 구조화된 정보 수집을 위한 드롭다운 활용
4. 에이전트 작업에 필수적인 정보는 항상 표시되도록 설정
```

### 사용자 경험 향상
```
개선 방안:
- 요청 양식에 명확한 안내 제공
- 필수 정보와 선택 정보의 구분
- 미리보기 기능으로 제출 전 확인 가능
- 도움말 텍스트로 각 필드의 용도 설명
```

### 내부 프로세스 최적화
```
에이전트 교육:
- Content 정보 위치 안내
- 중요 정보 추출 방법 교육
- 티켓 분류 시 참고 사항 활용
- 고객 소통 시 초기 요청 내용 참조
```

## 시스템 제한사항

### 현재 제약
```
기본 동작:
- Content 필드의 Requested Item 섹션 표시 불가
- 필드별 표시 위치 커스터마이징 제한
- 레거시 필드의 동작 방식 변경 불가
```

### 대안 접근법
```
우회 방법:
1. 새로운 커스텀 필드 생성
2. 워크플로우를 통한 정보 재배치
3. API를 활용한 정보 표시 커스터마이징
4. 티켓 템플릿 최적화
```

이러한 제약 사항을 이해하고 적절한 대안을 활용하면, 사용자와 에이전트 모두에게 최적화된 서비스 요청 경험을 제공할 수 있습니다.

</details>

<details>
<summary><strong>모든 워크스페이스의 서비스 카탈로그를 내보내는 방법은?</strong></summary>

**질문:** 모든 워크스페이스의 서비스 카탈로그를 내보내는 방법은?

**답변:** Freshservice에서는 서비스 카탈로그 항목을 직접 내보내는 기본 기능이 제공되지 않습니다. 하지만 API를 활용한 대안 방법으로 모든 워크스페이스의 서비스 카탈로그 정보를 추출할 수 있습니다.

## 내보내기 제한사항

### 현재 시스템 제약
```
제공되지 않는 기능:
❌ Service Catalog에서 직접 Export 옵션 없음
❌ UI 기반 일괄 다운로드 불가
❌ CSV/Excel 형식 자동 생성 기능 없음
❌ 워크스페이스 간 일괄 export 기능 없음
```

### 사용 가능한 대안
```
권장 해결책:
✅ Freshservice API 활용
✅ 프로그래밍 기반 데이터 추출
✅ 사용자 정의 export 스크립트 개발
```

## API 기반 해결 방법

### 1. Service Catalog API 활용
```
API 엔드포인트:
GET /api/v2/service_catalog

기본 정보:
- 모든 서비스 카탈로그 항목 조회
- JSON 형식으로 데이터 반환
- 페이지네이션 지원
```

### 2. API 호출 예시
```bash
# 기본 API 호출
curl -u 'API_KEY:X' \
  -H 'Content-Type: application/json' \
  'https://domain.freshservice.com/api/v2/service_catalog'

# 특정 워크스페이스 API 호출
curl -u 'API_KEY:X' \
  -H 'Content-Type: application/json' \
  'https://domain.freshservice.com/api/v2/service_catalog?workspace_id=123'
```

### 3. API 응답 데이터 구조
```json
{
  "service_items": [
    {
      "id": 1,
      "name": "Laptop Request",
      "description": "Request for new laptop",
      "category_id": 1,
      "cost": 1000.00,
      "delivery_time": 48,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z",
      "workspace_id": 1
    }
  ]
}
```

## 실용적인 Export 솔루션

### 1. Python 스크립트 예시
```python
import requests
import csv
import json

def export_service_catalog(domain, api_key):
    url = f"https://{domain}.freshservice.com/api/v2/service_catalog"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url, auth=(api_key, 'X'), headers=headers)
    data = response.json()
    
    # CSV 파일로 저장
    with open('service_catalog.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Description', 'Category', 'Cost', 'Delivery Time'])
        
        for item in data['service_items']:
            writer.writerow([
                item['id'],
                item['name'],
                item['description'],
                item.get('category_id', ''),
                item.get('cost', ''),
                item.get('delivery_time', '')
            ])

# 사용법
export_service_catalog('your-domain', 'your-api-key')
```

### 2. 다중 워크스페이스 처리
```python
def export_all_workspaces(domain, api_key, workspace_ids):
    all_items = []
    
    for workspace_id in workspace_ids:
        url = f"https://{domain}.freshservice.com/api/v2/service_catalog"
        params = {'workspace_id': workspace_id}
        
        response = requests.get(url, auth=(api_key, 'X'), params=params)
        data = response.json()
        
        for item in data['service_items']:
            item['workspace_id'] = workspace_id
            all_items.append(item)
    
    return all_items
```

## API 설정 및 준비

### 1. API 키 생성
```
단계:
1. Freshservice Admin → API 설정
2. 새 API 키 생성
3. 적절한 권한 부여 (Service Catalog 읽기)
4. 키 보안 관리
```

### 2. 워크스페이스 ID 확인
```
방법:
1. Admin → Workspaces에서 각 워크스페이스 확인
2. URL에서 workspace_id 추출
3. API 호출로 워크스페이스 목록 조회
```

### 3. 권한 요구사항
```
필요 권한:
✅ Service Catalog 읽기 권한
✅ Workspace 접근 권한
✅ API 사용 권한
```

## 데이터 처리 및 분석

### 1. 추출 가능한 정보
```
서비스 항목 기본 정보:
- 서비스 ID 및 이름
- 설명 및 카테고리
- 비용 및 배송 시간
- 생성/수정 날짜
- 워크스페이스 연결 정보

상세 설정:
- 커스텀 필드 구성
- 가시성 설정
- 승인 워크플로우
- 관련 서비스 연결
```

### 2. 데이터 변환 옵션
```
출력 형식:
- CSV: 스프레드시트 분석용
- JSON: 시스템 통합용
- Excel: 고급 분석 및 보고서용
- XML: 다른 시스템 이관용
```

## 모범 사례

### 정기적 백업 전략
```
권장 방법:
1. 월별 정기 export 실행
2. 변경 이력 추적 및 비교
3. 서비스 항목 사용률 분석
4. 불필요한 서비스 정리
```

### 데이터 품질 관리
```
검증 항목:
- 누락된 필수 정보 확인
- 중복 서비스 항목 식별
- 비활성 서비스 정리
- 카테고리 구조 최적화
```

### 보안 고려사항
```
보안 조치:
- API 키 안전한 저장
- 접근 로그 모니터링
- 데이터 암호화 전송
- 정기적 키 갱신
```

API를 활용한 이러한 방법을 통해 모든 워크스페이스의 서비스 카탈로그를 효과적으로 관리하고 분석할 수 있습니다.

</details>

<details>
<summary><strong>사용자 그룹별로 서비스 카탈로그를 사용자 정의하는 방법은?</strong></summary>

**질문:** 사용자 그룹별로 서비스 카탈로그를 사용자 정의하는 방법은?

**답변:** 부서나 직무에 따라 서비스 카탈로그를 맞춤화하면 사용자 경험이 크게 향상됩니다. 예를 들어, 디자이너에게는 Photoshop이 표시되지만 운영팀에는 표시되지 않도록 설정할 수 있습니다.

## 사용자 정의 프로세스 개요

### 3단계 설정 프로세스
```
1단계: 사용자(요청자)의 부서 및 직책 지정
2단계: 부서/직책을 포함하는 사용자 그룹 생성
3단계: 특정 서비스를 특정 사용자 그룹에 제공 설정
```

## 1단계: 사용자 정보 설정

### 사용자 부서 및 직책 지정
```
접근 경로:
Admin → User Management → Requesters

다중 워크스페이스:
Admin → {워크스페이스명} → User Management → Requesters
```

### 사용자 정보 편집
```
단계:
1. 해당 요청자 위에 마우스 호버
2. "Edit" 버튼 클릭
3. Department/Job Title 추가
4. "Update" 버튼으로 저장
```

### 부서 관리
```
부서 추가 경로:
Admin → User Management → Departments

기능:
- 새 부서 생성
- 기존 부서 수정
- 부서 계층 구조 설정
- 부서별 권한 관리
```

## 2단계: 사용자 그룹 생성

### 요청자 그룹 설정
```
접근 경로:
Admin → User Management → Requester Groups

기능:
- 기존 그룹 확인 및 편집
- 새 요청자 그룹 생성
```

### 새 그룹 생성 과정
```
단계:
1. "Create New" → "Requester Group" 선택
2. 그룹명 및 설명 입력
3. 멤버 추가 방법 선택:
   - Manual Addition: 수동으로 멤버 추가
   - Rule-based: 규칙 기반 자동 추가
4. 멤버 선택 완료 후 "Save"
```

### 규칙 기반 그룹 멤버십
```
조건 설정 예시:
- Department = "IT"
- Job Title = "Developer"
- Location = "Seoul"
- Language = "Korean"
- Time Zone = "Asia/Seoul"
- Reporting Manager = "특정 관리자"
```

## 3단계: 서비스 가시성 설정

### 서비스 항목 접근
```
경로:
Admin → Service Management → Service Catalog

단계:
1. 편집할 서비스 선택
2. "Service Item settings" 섹션으로 이동
```

### 가시성 옵션 설정
```
Agent Visibility:
- All Agents: 모든 에이전트
- Agent Groups: 특정 에이전트 그룹

Requester Visibility:
- All Requesters: 모든 요청자
- Requester Groups: 특정 요청자 그룹
```

### 그룹별 서비스 할당
```
설정 방법:
1. "Agent Visibility" 드롭다운에서 "Agent Groups" 선택
2. 서비스를 제공할 그룹 지정
3. "Save"로 설정 저장
```

## 실용적인 사용 사례

### 부서별 서비스 분리
```
IT 부서:
- 서버 액세스 권한
- 개발 도구 라이선스
- 네트워크 장비 요청

HR 부서:
- 직원 온보딩 서비스
- 교육 프로그램 등록
- 휴가 승인 프로세스

디자인 팀:
- 그래픽 소프트웨어 라이선스
- 고성능 워크스테이션
- 디자인 리소스 접근
```

### 지역별 맞춤화
```
서울 오피스:
- 한국어 지원 서비스
- 로컬 장비 대여
- 현지 규정 준수 서비스

해외 지사:
- 다국어 지원 서비스
- 국제 배송 옵션
- 현지 법규 대응 서비스
```

### 직급별 권한 분리
```
관리자급:
- 고가 장비 승인 권한
- 팀 리소스 요청
- 예산 관련 서비스

일반 직원:
- 표준 장비 요청
- 기본 소프트웨어 라이선스
- 일반 지원 서비스
```

## 고급 사용자 정의 기능

### 복합 조건 설정
```
예시: 아랍어 키보드 서비스
조건:
- Language = "Arabic"
- Location = "Dubai"
→ 아랍어 사용자이면서 두바이 근무자만 접근 가능
```

### 동적 그룹 관리
```
자동 업데이트:
- 신규 직원 자동 그룹 할당
- 부서 이동 시 자동 권한 변경
- 퇴사 시 자동 권한 제거
```

### 시간 기반 제한
```
설정 가능 조건:
- 업무 시간 내 서비스만 제공
- 특정 요일에만 요청 가능
- 계절별 서비스 제공
```

## 모니터링 및 최적화

### 사용 패턴 분석
```
추적 지표:
- 그룹별 서비스 사용률
- 가장 인기 있는 서비스
- 사용하지 않는 서비스 식별
- 요청 승인률 분석
```

### 지속적 개선
```
정기 검토 사항:
1. 그룹 구성의 적절성
2. 서비스 분류의 정확성
3. 사용자 피드백 반영
4. 새로운 요구사항 식별
```

### 성능 모니터링
```
확인 항목:
- 서비스 카탈로그 로딩 속도
- 검색 성능
- 사용자 만족도
- 지원팀 효율성
```

이러한 체계적인 사용자 정의를 통해 각 사용자 그룹에 최적화된 서비스 카탈로그를 제공할 수 있으며, 이는 사용자 만족도 향상과 IT 운영 효율성 증대로 이어집니다.

</details>

<details>
<summary><strong>특정 카탈로그 항목에 대한 사용자 접근을 제한하는 방법은?</strong></summary>

**질문:** 특정 카탈로그 항목에 대한 사용자 접근을 제한하는 방법은?

**답변:** Freshservice에서는 세밀한 가시성 제어를 통해 특정 사용자나 그룹만 특정 서비스에 접근할 수 있도록 제한할 수 있습니다. 이는 보안, 비용 관리, 그리고 업무 효율성을 높이는 데 중요한 기능입니다.

## 접근 제한 설정 방법

### 기본 접근 경로
```
관리자 경로:
Admin → Global Settings Admin (다중 워크스페이스의 경우)
또는
Admin → Service Management → Service Catalog

워크스페이스별:
Admin → {워크스페이스명} → Service Catalog
```

### 서비스 항목 가시성 설정
```
단계:
1. 제한하려는 특정 서비스 항목 선택
2. "Service Item Settings" 섹션으로 이동
3. "Choose who can view this service item" 옵션 확인
4. 에이전트 및 요청자 그룹별 접근 권한 설정
```

## 가시성 제어 옵션

### 에이전트(Agents) 접근 제어
```
설정 옵션:
✅ All Agents: 모든 에이전트 접근 가능
✅ Specific Agent Groups: 지정된 에이전트 그룹만 접근
✅ No Agents: 에이전트 접근 차단

실용 예시:
- 고급 네트워크 장비: 네트워크 팀만 접근
- 보안 도구: 보안팀만 접근
- 관리자 도구: 시니어 에이전트만 접근
```

### 요청자(Requesters) 접근 제어
```
설정 옵션:
✅ All Requesters: 모든 요청자 접근 가능
✅ Specific Requester Groups: 지정된 요청자 그룹만 접근
✅ No Requesters: 요청자 접근 차단

실용 예시:
- 개발 도구: 개발팀만 접근
- 디자인 소프트웨어: 디자인팀만 접근
- 관리자 서비스: 관리자급만 접근
```

## 세부 설정 방법

### 1. 요청자 그룹 기반 제한
```
그룹 생성 기준:
- 부서별 (IT, HR, Finance, Marketing)
- 직급별 (Manager, Senior, Junior)
- 위치별 (Seoul, Busan, Overseas)
- 프로젝트별 (Project A, Project B)
```

### 2. 복합 조건 설정
```python
# 예시: 고가 장비 요청 제한
조건 설정:
- Requester Group: "Senior Staff" 
- Department: "IT" 또는 "Engineering"
- Job Title: "Manager" 이상
→ 시니어급 IT/엔지니어링 직원만 접근 가능
```

### 3. 시간 기반 제한 (고급)
```
조건부 가시성:
- 업무 시간 내에만 표시
- 특정 요일에만 제공
- 프로젝트 기간 중에만 활성화
- 예산 승인 후에만 표시
```

## 실제 사용 사례

### 보안 관련 제한
```
높은 보안 등급 서비스:
- VPN 접근 권한: 보안팀 + 승인된 원격 근무자
- 서버 루트 액세스: 시스템 관리자만
- 민감 데이터 접근: 데이터 보호 담당자만

설정 방법:
1. "Security Clearance" 요청자 그룹 생성
2. 해당 그룹에 인증된 사용자만 포함
3. 보안 서비스를 이 그룹에만 제한
```

### 비용 관리 제한
```
고가 서비스 제한:
- 고성능 워크스테이션: 부서장 승인 필요 그룹
- 소프트웨어 라이선스: 예산 승인된 그룹
- 외부 교육: 매니저급 이상

예산 그룹 설정:
1. "Budget Approved" 그룹 생성
2. 예산 승인받은 직원만 포함
3. 고가 서비스를 이 그룹에만 제한
```

### 지역별 제한
```
지역 특화 서비스:
- 현지 장비 대여: 해당 지역 직원만
- 지역별 규정 서비스: 해당 국가 직원만
- 언어 특화 지원: 해당 언어 사용자만

지역 그룹 예시:
- "Seoul Office": 서울 근무자
- "US Branch": 미국 지사 직원
- "Remote Workers": 원격 근무자
```

## 고급 제한 전략

### 계층적 접근 제어
```
접근 레벨 설계:
Level 1 (Basic): 모든 직원 접근 가능
Level 2 (Standard): 정규직만 접근
Level 3 (Advanced): 시니어급 이상
Level 4 (Executive): 임원진만 접근

구현:
1. 각 레벨별 요청자 그룹 생성
2. 서비스별 적절한 레벨 할당
3. 정기적 권한 검토 실시
```

### 동적 권한 관리
```
자동 권한 부여/해제:
- 신입사원: 3개월 후 고급 서비스 접근
- 부서 이동: 자동 권한 재할당
- 프로젝트 종료: 관련 서비스 접근 제거
- 휴직/퇴사: 즉시 모든 접근 차단
```

### 임시 접근 권한
```
한시적 접근 설정:
- 프로젝트 기간 중에만 특정 도구 접근
- 출장 기간 중 특별 서비스 제공
- 긴급 상황 시 임시 권한 부여
- 교육 기간 중 실습 환경 접근
```

## 모니터링 및 감사

### 접근 로그 추적
```
모니터링 항목:
- 서비스별 접근 시도 현황
- 거부된 접근 요청 분석
- 사용 패턴 변화 추적
- 비정상적 접근 탐지
```

### 정기적 권한 검토
```
검토 주기 및 항목:
월별: 신규 서비스 권한 설정
분기별: 그룹 멤버십 적정성 검토
반기별: 전체 권한 구조 재검토
연간: 보안 정책 준수 감사
```

### 규정 준수 관리
```
컴플라이언스 요구사항:
- SOX 규정: 재무 관련 서비스 접근 통제
- GDPR: 개인정보 처리 서비스 제한
- ISO 27001: 정보보안 관련 서비스 제어
- 내부 보안 정책: 회사별 맞춤 제한
```

## 사용자 경험 최적화

### 명확한 안내 제공
```
사용자 알림:
- 접근 불가 서비스에 대한 명확한 설명
- 접근 권한 신청 절차 안내
- 승인 담당자 연락처 제공
- 대안 서비스 추천
```

### 셀프서비스 권한 요청
```
자동화된 권한 요청:
1. 접근 불가 서비스 클릭 시 권한 요청 양식 표시
2. 요청 사유 및 기간 입력
3. 자동으로 승인자에게 전달
4. 승인 시 자동 권한 부여
```

이러한 체계적인 접근 제한 설정을 통해 보안을 강화하고, 비용을 효율적으로 관리하며, 사용자에게는 필요한 서비스만 제공하는 최적화된 서비스 카탈로그를 운영할 수 있습니다.

</details>

---

*이 가이드는 Freshservice의 서비스 카탈로그를 효과적으로 활용하는 데 도움이 됩니다.*
