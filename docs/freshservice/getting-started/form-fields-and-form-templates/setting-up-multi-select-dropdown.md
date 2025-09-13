---
sidebar_position: 6
---

# 다중 선택 드롭다운 설정

:::info 문서 목적
이 문서는 "Multi-select Dropdown(멀티 셀렉트 드롭다운)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
:::

멀티 셀렉트 드롭다운 필드는 사용자가 드롭다운에서 여러 옵션을 동시에 선택할 수 있는 기능을 제공합니다. Freshservice에서 티켓, 문제, 변경, 릴리스에 모두 사용할 수 있으며, 서비스 카탈로그의 사용자 정의 필드를 만들 때도 활용할 수 있습니다.

## 멀티 셀렉트 드롭다운의 특징

### 단일 필드에서 다중 선택
일반적인 드롭다운 필드는 하나의 값만 선택할 수 있지만, 멀티 셀렉트 드롭다운은 여러 값을 동시에 선택할 수 있습니다.

### 실용적인 활용 예시
:::info 액세스 요청 폼 예시
사용자가 액세스 요청 폼에서 여러 애플리케이션을 선택해야 하는 경우, 체크박스 필드 대신 모든 애플리케이션 옵션이 포함된 멀티 셀렉트 드롭다운을 생성할 수 있습니다. 이를 통해 사용자는 사용자 정의 드롭다운에서 제공되는 옵션 중에서 단일 필드에 대해 여러 값을 선택할 수 있습니다.
:::

![멀티 셀렉트 드롭다운 동작 예시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002199717/original/ytebJfqtBz0VQs-43r5RKKBx56qbyL60-A.gif?1608112792)

## 멀티 셀렉트 드롭다운 설정 방법

### 1단계: Field Manager 접근

**Admin Settings > Global Settings > Field Manager**로 이동합니다.

:::info 특별한 경우의 접근 경로
- **서비스 카탈로그**: Admin Settings > Global Settings > Service Catalog > Catalog Item
- **개별 워크스페이스**: Admin Settings > Global Settings > Workspace Settings > Field Manager
:::

### 2단계: 티켓 필드 선택

**Ticket Fields** 섹션을 선택합니다.

### 3단계: 멀티 셀렉트 드롭다운 필드 추가

드래그 앤 드롭 필드 박스에서 **Multi-select dropdown**을 클릭하여 필드를 추가합니다.

![멀티 셀렉트 드롭다운 필드 추가](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013332289/original/PjgCDFCHRFScYphq5xYxOFTwaXSxu51TVg.png?1728467614)

![필드 설정 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013332265/original/WPxTIHpw6JquDPK-edoA3GplsMTz7Zqtrg.png?1728467534)

### 4단계: 필드 속성 설정

다음 항목들을 설정합니다:

#### 기본 속성
- **필드 가시성**: 어떤 사용자에게 표시될지 결정
- **편집 가능 여부**: 사용자가 값을 수정할 수 있는지 설정
- **필수 필드 여부**: 티켓 제출 시 반드시 입력해야 하는지 설정

#### 필드 이름 사용자 정의
상담원과 요청자를 위한 필드 이름을 각각 설정합니다.

### 5단계: 드롭다운 유형 선택

두 가지 옵션 중 하나를 선택합니다:

#### Custom Dropdown (사용자 정의 드롭다운)
드롭다운에 표시될 선택 항목을 직접 추가합니다.

#### Select from Data Source (데이터 소스에서 선택)
기존 데이터 소스에서 옵션을 가져옵니다.

![드롭다운 유형 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013332311/original/gxmECycE_9vfZAASpCDYj-OiKCie0K76sA.png?1728467661)

:::warning 데이터 소스 제한사항
**Select from Data Source** 옵션은 서비스 카탈로그 멀티 셀렉트 필드에만 적용됩니다.
:::

### 6단계: 선택 항목 추가

드롭다운에 표시될 선택 항목을 추가합니다.

![선택 항목 추가](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013332557/original/pWBG9sAklYRX8SSBVqfz2tkPskYptS5Bog.png?1728468450)

#### 일괄 선택 항목 추가 (Bulk Add Choices)

![일괄 선택 항목 추가](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013332477/original/Nk_0nCtOjWdlbPeLu_j97yHyQGklJw3Wdg.png?1728468261)

:::tip 효율적인 대량 입력
- 선택 항목을 일괄적으로 입력 가능
- Enter 키를 사용하여 새 선택 항목 추가
- 중복된 선택 항목은 자동으로 건너뜀
- 메모장이나 CSV 파일에서 필요한 선택 항목을 복사하여 텍스트 영역에 붙여넣기
- 기존 선택 항목을 새로운 항목으로 일괄 대체 가능
:::

### 7단계: 설정 저장

1. **Done** 클릭하여 필드 설정 저장
2. **Save** 클릭하여 전체 폼 저장

## 설정 팁 및 주의사항

## 실무 활용 시나리오

### 시나리오 1: 소프트웨어 액세스 요청
**목표**: 사용자가 필요한 여러 소프트웨어를 한 번에 요청

**멀티 셀렉트 옵션:**
- Microsoft Office 365
- Adobe Creative Suite
- Slack
- Zoom
- Tableau
- Salesforce
- Jira
- GitHub Desktop

**효과:**
- 체크박스 필드 대신 깔끔한 드롭다운 인터페이스
- 사용자 경험 개선 및 폼 공간 절약
- 표준화된 소프트웨어 목록 관리

### 시나리오 2: 시설 이용 신청
**목표**: 회의실 및 장비 예약을 위한 다중 선택

**멀티 셀렉트 옵션:**
- 대회의실
- 소회의실
- 프로젝터
- 화이트보드
- 화상회의 장비
- 무선 마이크
- 플립차트
- 노트북

### 시나리오 3: IT 지원 범위 선택
**목표**: 기술 지원이 필요한 여러 영역 선택

**멀티 셀렉트 옵션:**
- 하드웨어 설치
- 소프트웨어 설치
- 네트워크 설정
- 프린터 설정
- 이메일 설정
- VPN 설정
- 백업 설정
- 보안 소프트웨어 설치

## 고급 기능 및 제한사항

### 지원되는 모듈
- **티켓 (Tickets)**
- **문제 (Problems)**
- **변경 (Changes)**
- **릴리스 (Releases)**
- **서비스 카탈로그 (Service Catalog)**

### 제한사항 및 고려사항

:::warning 중요한 제한사항
1. **Asset Type 및 Fields 제외**: 일괄 선택 항목 추가는 Asset Type 및 Fields 모듈을 제외한 모든 모듈에서 지원됩니다.
2. **서비스 아이템 필드 수 제한**: Freshservice는 서비스 아이템 폼에 추가할 수 있는 필드 수를 제한합니다. [자세한 내용은 이 문서를 참조하세요](https://support.freshservice.com/en/support/solutions/articles/50000000600-do-we-have-limitations-on-the-number-of-custom-fields-that-can-be-created-in-a-service-item-).
:::

### 워크플로우 실행 순서
워크스페이스 관리자는 해당 워크스페이스에 적용되는 글로벌 및 로컬 워크플로우 목록을 확인할 수 있습니다. 글로벌 워크플로우가 먼저 실행된 후 워크스페이스 수준 워크플로우가 실행됩니다.

## 모범 사례

### 옵션 설계 원칙
1. **명확한 옵션명**: 사용자가 쉽게 이해할 수 있는 명확한 이름 사용
2. **적절한 옵션 수**: 너무 많은 옵션은 오히려 사용자 혼란 야기
3. **논리적 그룹화**: 관련된 옵션들을 함께 배치

### 사용자 경험 최적화
- **검색 기능 활용**: 옵션이 많을 경우 검색 기능으로 빠른 선택 지원
- **기본값 설정**: 자주 사용되는 옵션을 기본값으로 설정
- **도움말 텍스트**: 필요시 필드 설명 추가

### 데이터 관리
- **정기적 검토**: 사용되지 않는 옵션 정리
- **표준화**: 조직 전체에서 일관된 옵션 사용
- **버전 관리**: 옵션 변경 이력 관리

## 트러블슈팅

### 자주 발생하는 문제

#### 문제: 선택된 값이 저장되지 않음
**원인**: 필드 권한 설정 오류
**해결**: 사용자 그룹에 대한 편집 권한 확인

#### 문제: 드롭다운 옵션이 표시되지 않음
**원인**: 데이터 소스 연결 문제 또는 빈 옵션 목록
**해결**: 옵션 목록 재확인 및 데이터 소스 상태 점검

#### 문제: 다중 선택이 작동하지 않음
**원인**: 일반 드롭다운으로 잘못 설정
**해결**: 필드 유형을 멀티 셀렉트 드롭다운으로 변경

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [드롭다운 필드 설정](./setting-up-dropdown-fields)
- [사용자 정의 필드 생성](./creating-custom-fields-ticket-problem-change-release-task-form)
- [종속 필드 이해](./understanding-dependent-fields)
- [폼 필드 기본 설정](./setting-up-form-fields-tickets-problems-changes-releases)
-->
