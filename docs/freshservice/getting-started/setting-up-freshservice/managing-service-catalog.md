---
sidebar_position: 8
---

# Freshservice 서비스 카탈로그 관리

:::info 문서 목적
이 문서는 "Freshservice 서비스 카탈로그 관리(Managing Service Catalog in Freshservice)" 기능의 설정, 관리, 최적화 방법을 안내하는 문서입니다.
:::

Freshservice 서비스 카탈로그는 조직 내 IT 서비스와 요청을 체계적으로 관리할 수 있는 중앙 집중식 플랫폼이에요. 이 문서는 서비스 아이템 생성부터 고급 관리 기능까지 포괄적인 가이드를 제공해요.

## 개요

서비스 카탈로그는 사용자가 요청할 수 있는 모든 IT 서비스를 구조화된 방식으로 제시하는 디지털 메뉴예요. 올바른 설정과 관리를 통해 사용자 경험을 향상시키고 IT 팀의 효율성을 높일 수 있어요.

:::info 서비스 카탈로그의 핵심 요소
- **Service Items**: 개별 서비스 요청 항목 (하드웨어, 소프트웨어, 액세스 권한 등)
- **Service Categories**: 서비스 분류 체계 (IT Support, HR Services, Facilities 등)
- **Custom Fields**: 서비스별 맞춤 정보 수집 필드
- **Workflow Integration**: 승인 프로세스 및 자동화 워크플로우 연결
- **Visibility Controls**: 사용자 그룹별 서비스 접근 권한 관리
:::

## 서비스 카탈로그 접근 및 설정

### 관리자 접근 경로

1. **Admin** 메뉴로 이동
2. **Service Management** 섹션 → **Service Request Management** 하위 메뉴
3. **Service Catalog** 선택

### 기본 구조 이해

서비스 카탈로그는 다음과 같은 계층 구조로 구성됩니다:

```
Service Catalog
├── Category 1 (예: IT Support)
│   ├── Service Item 1 (예: Software Installation)
│   ├── Service Item 2 (예: Hardware Request)
│   └── Service Item 3 (예: Password Reset)
├── Category 2 (예: HR Services)
│   ├── Service Item 4 (예: Employee Onboarding)
│   └── Service Item 5 (예: Leave Request)
└── Category 3 (예: Facilities)
    ├── Service Item 6 (예: Meeting Room Booking)
    └── Service Item 7 (예: Parking Space Request)
```

## 서비스 아이템 생성 및 관리

### 새 서비스 아이템 생성

#### 1단계: 기본 정보 설정
- **Service Item Name**: 명확하고 이해하기 쉬운 이름
- **Description**: 서비스에 대한 상세 설명
- **Category**: 적절한 서비스 카테고리 선택
- **Icon**: 시각적 식별을 위한 아이콘 설정

#### 2단계: 서비스 상세 구성
- **Delivery Instructions**: 서비스 제공 방법 및 절차
- **Cost**: 서비스 비용 정보 (필요한 경우)
- **SLA**: 서비스 수준 협약 설정
- **Approval Process**: 승인 워크플로우 연결

### 커스텀 필드 추가

서비스 아이템에 특화된 정보를 수집하기 위한 커스텀 필드를 추가할 수 있습니다:

#### 커스텀 필드 추가 단계
1. 원하는 **Service Item** 선택
2. **Custom Fields** 탭 클릭
3. 필드 유형 선택:
   - **Text Field**: 단순 텍스트 입력
   - **Dropdown**: 선택 옵션 목록
   - **Checkbox**: 체크박스 선택
   - **Date**: 날짜 선택기
   - **Number**: 숫자 입력
   - **Multi-line Text**: 긴 텍스트 입력

4. 필드 속성 설정:
   - **Field Name**: 필드 이름 지정
   - **Required**: 필수 입력 여부
   - **Display to Requester**: 요청자에게 표시 여부
   - **Requester can edit**: 요청자 편집 가능 여부

5. **Save** 버튼으로 저장 (Draft 또는 Publish 선택)

:::tip 커스텀 필드 설계 모범 사례
1. **최소한의 필드**: 꼭 필요한 정보만 수집하여 사용자 경험 향상
2. **명확한 라벨**: 사용자가 이해하기 쉬운 필드명 사용
3. **기본값 설정**: 일반적인 선택사항에 기본값 제공
4. **도움말 텍스트**: 복잡한 필드에 대한 설명 추가
5. **논리적 순서**: 정보 입력의 자연스러운 흐름 고려
:::

## 서비스 아이템 가시성 관리

### 기본 가시성 설정

서비스 아이템의 가시성은 **Agent Groups**와 **Requester Groups**를 기반으로 제어됩니다.

#### 가시성 설정 방법
1. Service Item 선택 → **Settings** 탭
2. **"Choose who can view this service item"** 섹션에서:
   - **Agent Groups**: 에이전트 그룹 선택
   - **Requester Groups**: 요청자 그룹 선택

### 고급 가시성 제어

#### 지역별 제한
요청자의 위치에 따른 서비스 제한을 위해:
1. 지역별 요청자 그룹 생성
2. 해당 그룹에 지역 사용자 추가
3. 서비스 아이템 가시성을 특정 그룹으로 제한

#### 모든 요청자로부터 숨기기
특정 서비스를 완전히 숨기는 워크어라운드:
1. **더미 요청자 그룹** 생성
2. 더미 사용자 프로필 추가
3. 해당 그룹에만 가시성 부여

### 요청자 화면 표시 설정

#### "Display to Requester" 옵션 작동 방식
- **Display to Requester** 체크: 요청자 화면에 필드 표시
- **Requester can edit** 체크: 요청자가 편집 가능 (둘 다 체크해야 실제 표시됨)

:::warning 중요한 동작 특성
**Display to Requester**만 체크하고 **Requester can edit**을 체크하지 않으면 요청자 화면에 필드가 표시되지 않습니다. 이는 Freshservice의 기본 동작입니다.
:::

## 특수 서비스 아이템 관리

### Employee Offboarding Bundle
다중 워크스페이스 환경에서:
- Employee offboarding 번들 아이템은 기본적으로 **HR workspace**에만 표시
- 다른 워크스페이스에서 접근하려면 별도 설정 필요

### "Request for someone else" 기능
1. 서비스 아이템에서 **"Place request"** 옵션 활성화
2. 요청자가 다른 사람을 대신하여 요청할 수 있는 기능 제공

## 서비스 카탈로그 최적화

### 사용자 경험 향상

#### 1. 직관적인 카테고리 구성
```
✅ 좋은 예시:
- IT Support
  - Hardware & Equipment
  - Software & Applications
  - Network & Connectivity
- HR Services
  - Employee Services
  - Benefits & Payroll
- Facilities
  - Office Services
  - Meeting & Events

❌ 피해야 할 예시:
- Miscellaneous Items
- Other Requests
- General Support
```

#### 2. 검색 최적화
- **Keywords**: 서비스 설명에 검색 가능한 키워드 포함
- **Synonyms**: 사용자가 사용할 수 있는 다양한 용어 고려
- **Clear Naming**: 기술적 용어보다는 사용자 친화적 명칭 사용

#### 3. 시각적 개선
- **Consistent Icons**: 카테고리별 일관된 아이콘 사용
- **Clear Descriptions**: 간결하면서도 정보가 풍부한 설명
- **Screenshots**: 복잡한 서비스의 경우 스크린샷 활용

### 운영 효율성 향상

#### 자동화 연결
1. **Workflow Automation**: 서비스 요청에 대한 자동 승인/처리
2. **SLA Integration**: 서비스별 처리 시간 목표 설정
3. **Asset Management**: 하드웨어 요청 시 자산 관리 시스템 연동

#### 승인 프로세스 최적화
- **Multi-level Approval**: 고가 항목에 대한 다단계 승인
- **Conditional Approval**: 요청 내용에 따른 조건부 승인
- **Auto-approval**: 저가/일반 항목에 대한 자동 승인

## 보고 및 분석

### 서비스 카탈로그 성과 측정

#### 주요 메트릭
1. **Service Item Usage**: 가장 많이 요청되는 서비스 분석
2. **User Adoption**: 카탈로그 사용률 추적
3. **Request Completion Time**: 서비스별 처리 시간 분석
4. **User Satisfaction**: 서비스별 만족도 점수

#### 개선 지표
- **Catalog Utilization Rate**: 전체 서비스 대비 실제 사용되는 서비스 비율
- **Self-Service Success Rate**: 사용자 자체 해결 성공률
- **Request Accuracy**: 정확한 정보로 제출되는 요청 비율

:::success 성공적인 서비스 카탈로그 운영 팁
1. **정기적 검토**: 월별 사용 현황 분석 및 불필요한 서비스 정리
2. **사용자 피드백**: 정기적인 사용자 설문을 통한 개선사항 파악
3. **지속적 업데이트**: 조직 변화에 따른 서비스 카탈로그 업데이트
4. **교육 및 홍보**: 새로운 서비스나 기능에 대한 사용자 교육
5. **표준화**: 서비스 명명법, 설명 형식, 승인 프로세스 표준화
:::

## 관련 문서
:::

## 문제 해결 (Troubleshooting)

### 일반적인 문제와 해결책

#### 필드가 요청자에게 표시되지 않는 경우
**문제**: "Display to Requester"를 체크했지만 필드가 보이지 않음
**해결**: "Requester can edit" 옵션도 함께 체크

#### 서비스가 특정 사용자에게 보이지 않는 경우
**문제**: 서비스 아이템이 일부 사용자에게만 표시됨
**해결**: 
1. 사용자의 그룹 멤버십 확인
2. 서비스 아이템의 가시성 설정 검토
3. 워크스페이스 설정 확인

#### 커스텀 필드 저장 오류
**문제**: 커스텀 필드 설정이 저장되지 않음
**해결**:
1. 필수 필드 정보 입력 확인
2. 필드명 중복 여부 검토
3. 브라우저 캐시 클리어 후 재시도

### 성능 최적화

#### 로딩 속도 개선
- 불필요한 커스텀 필드 제거
- 이미지 크기 최적화
- 카테고리별 서비스 수량 적절히 분산

#### 검색 성능 향상
- 서비스 이름에 핵심 키워드 포함
- 태그 시스템 적극 활용
- 중복 서비스 정리

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [SLA 정책 관리](./managing-sla-policy)
- [워크플로우 자동화 설정](./workflow-automation-setup)
- [사용자 그룹 관리](./managing-user-groups)
- [승인 프로세스 설정](./approval-process-configuration)
- [에이전트 관리](./managing-agents-freshservice)
-->
