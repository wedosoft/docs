---
sidebar_position: 14
---

# 비즈니스 규칙 사용 사례

:::info 문서 목적
이 문서는 "비즈니스 규칙 사용 사례(Business Rules Usecases)" 기능을 통해 실제 업무에서 활용할 수 있는 다양한 규칙 설정 방법을 안내하는 문서입니다.
:::

비즈니스 규칙을 통해 구현할 수 있는 일반적인 사용 사례들을 안내합니다. 이러한 규칙들은 업무 프로세스를 자동화하고 일관성을 유지하는 데 도움이 됩니다.

:::tip 규칙 설정 가이드
비즈니스 규칙을 구성하는 방법에 대한 자세한 내용은 [동적 폼 생성 가이드](https://support.freshservice.com/en/support/solutions/articles/50000002728-create-no-code-dynamic-forms-with-business-rules)를 참조하세요.
:::

## 권한 및 실행 순서

### 관리자 권한
- **글로벌 비즈니스 규칙**: 워크스페이스 관리자만 조회 가능
- **워크스페이스 수준 규칙**: 워크스페이스 관리자가 생성 가능

### 실행 순서
글로벌 규칙이 먼저 실행된 후 워크스페이스 수준 규칙이 실행되어, 워크스페이스 규칙이 글로벌 규칙보다 우선적용됩니다.

## 주요 사용 사례

### 1. 티켓 유형에 따른 필드 표시/숨김

특정 필드를 인시던트와 서비스 요청에 따라 다르게 표시할 수 있습니다.

:::info 티켓 유형 필드 제한사항
티켓 유형 필드는 티켓 편집 시에만 사용할 수 있으므로, **편집 폼 전용 규칙**으로 설정해야 합니다.
:::

**설정 예시:**
- **조건**: 티켓 유형이 "인시던트"인 경우
- **동작**: 인시던트 관련 필드만 표시
- **적용 폼**: 편집 폼

![티켓 유형별 필드 표시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714488/original/E0lyGD4NglKzdR2kAYKdL4FYdjjlr8OJNQ.png?1616649638)

### 2. 특정 요청 항목에 따른 조건부 동작

특정 서비스 항목이 포함된 서비스 요청에서만 특정 필드를 필수로 만들 수 있습니다.

**활용 예시: 직원 온보딩 요약 필수 입력**
- **조건**: 현재 티켓에 "직원 온보딩" 서비스 항목 포함
- **동작**: 티켓 해결 전 "온보딩 요약" 필드 필수 입력
- **대상**: 상담원

![서비스 항목별 필드 조건](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714490/original/Vb7LjSR1HyNPVNkH_lLa2nlC1miPLcvGKg.png?1616649638)

### 3. 종속 필드의 특정 수준 필수 입력

카테고리와 같은 종속 필드에서 특정 수준을 필수로 만들 수 있습니다.

**하위 카테고리 필수 설정:**
- **조건**: "Is Empty" 연산자 사용
- **대상 필드**: 하위 카테고리
- **동작**: 하위 카테고리가 비어있으면 유효성 검사 실패

![종속 필드 유효성 검사](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714487/original/RL40ipMjVsi2AP_crKhLWWFZixy46V0lGw.png?1616649637)

### 4. 티켓 직접 종료 방지

상담원이 티켓을 직접 종료하지 못하도록 제한하여, 해결 후 자동 종료 프로세스를 강제할 수 있습니다.

**설정 방법:**
- **조건**: 상태가 "종료"로 변경되는 경우
- **동작**: 유효성 검사 실패 및 오류 메시지 표시
- **목적**: 해결 → 자동 종료 워크플로우 준수

![티켓 직접 종료 방지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714486/original/W1PDR8dHe3Ujj321mY7Do0j9UCKQ4B3Amw.png?1616649637)

### 5. 대기 상태 전환 시 추가 정보 필수 입력

티켓을 대기 상태로 변경할 때 추가 세부사항을 필수로 입력하도록 설정할 수 있습니다.

**구성 요소:**
- **조건**: 티켓 상태가 "대기"로 변경
- **필수 필드**: 추가 세부사항 필드
- **적용 대상**: 상담원

![대기 상태 필수 정보](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714491/original/riQdkYSOkpZywYoSU11AD1UyQzXr6Awa1g.png?1616649638)

### 6. 승인 대기 중 티켓 종료 방지

승인을 기다리는 티켓이 종료되지 않도록 제한할 수 있습니다.

**티켓 상태 구분:**
- **현재 티켓 상태**: 티켓의 현재 상태
- **티켓 폼 상태**: 상담원이 변경하려는 상태

![승인 대기 중 종료 방지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714489/original/1x5sE1zzEdbfJCshGq3gaVY_Q2v6CfUZvg.png?1616649638)

### 7. 종료된 티켓 속성 변경 방지

티켓이 종료된 후에는 티켓 속성을 업데이트할 수 없도록 제한할 수 있습니다.

**적용 범위:**
- **대상**: 종료된 티켓의 모든 속성
- **제한 동작**: 필드 값 변경, 상태 수정 등
- **목적**: 티켓 무결성 보장

![종료 티켓 수정 방지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002714485/original/B7E_-gUHIA0WFCvQ0_drmOW8Z_KHl1Ibqg.png?1616649636)

## 옵션 설정 및 제거 기능

### 드롭다운 선택 제한

Set 및 Remove 옵션 기능을 사용하여 특정 조건에서 드롭다운 선택지를 제한할 수 있습니다.

**적용 가능한 필드:**
- 기본 드롭다운
- 사용자 정의 드롭다운
- 종속 필드
- 룩업 필드 (상담원, 부서, 그룹 등)

### 8. 위치/부서/그룹별 카테고리 제한 (Set Options)

요청자의 위치, 부서, 그룹에 따라 관련 카테고리만 표시할 수 있습니다.

**설정 방법:**
- **조건**: 요청자의 위치/부서/그룹
- **동작**: Set Options로 해당 카테고리만 표시
- **효과**: 업무 영역에 맞는 카테고리만 선택 가능

![카테고리 제한 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002920008/original/Scb7vYOKJlv0A7QSfTrdQEgCdHy7uJ9MCw.jpg?1619794916)

### 9. 승인 대기 중 상태 옵션 제거 (Remove Options)

승인을 기다리는 티켓에서 "해결됨" 및 "종료됨" 상태를 선택할 수 없도록 제한합니다.

**구성:**
- **조건**: 티켓이 승인 대기 상태
- **동작**: Remove Options로 특정 상태 숨김
- **제거 대상**: 해결됨, 종료됨 상태

![상태 옵션 제거](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002920182/original/Bz_7pKKkup8i4L3OFddd0j1PiswuMyZVCg.jpg?1619795932)

### 10. 조건부 자산 연결 필수/선택 설정

카테고리, 상태 등에 따라 자산 연결을 조건부로 필수 또는 선택사항으로 만들 수 있습니다.

**활용 사례:**
- **하드웨어 관련 카테고리**: 자산 연결 필수
- **소프트웨어 문의**: 자산 연결 선택사항
- **일반 문의**: 자산 연결 불필요

![조건부 자산 연결](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002921178/original/8Ol7-WIol2VuG0H1WV6s2O80ApIRGrC2gw.jpg?1619805583)

:::tip 사용 사례 활용 팁
- 규칙 설정 전에 업무 프로세스를 명확히 정의하세요
- 복잡한 규칙은 여러 개의 간단한 규칙으로 나누어 관리하세요
- 테스트 환경에서 충분히 검증한 후 운영 환경에 적용하세요
- 규칙 간의 충돌을 방지하기 위해 실행 순서를 고려하세요
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [비즈니스 규칙 설정 가이드](./business-rules-configuration)
- [비즈니스 규칙 문제 해결](./business-rules-troubleshooting-guide)
- [동적 폼 생성](./dynamic-forms)
- [필드 관리](./field-management)
-->
