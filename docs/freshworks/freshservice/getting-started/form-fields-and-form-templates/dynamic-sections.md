---
id: dynamic-sections
title: 동적 섹션 활용 가이드
sidebar_label: 동적 섹션 활용 가이드
sidebar_position: 8
---

<div class="subtitle">
  이 문서는 "동적 섹션(Dynamic Sections)" 기능을 활용하여 사용자 입력에 따라 변화하는 동적 티켓 폼을 구성하는 방법을 안내하는 문서입니다.
</div>

## 개요

동적 섹션 기능을 사용하면 사용자의 입력에 따라 폼의 필드가 동적으로 변화하는 티켓 폼을 만들 수 있습니다. 드롭다운 필드에서 선택한 값에 따라 서로 다른 필드 세트가 표시되어, 상황에 맞는 정보를 효율적으로 수집할 수 있습니다.

## 동적 섹션의 활용 사례

### IT 관련 티켓
- **필요 정보**: 워크스테이션 번호, IP 주소, 디바이스 ID
- **수집 목적**: 기술적 문제 해결을 위한 시스템 정보

### 재무 관련 티켓  
- **필요 정보**: 직원 ID, 입사일, 부서 코드
- **수집 목적**: 급여, 비용 처리를 위한 인사 정보

### 시설 관리 티켓
- **필요 정보**: 건물명, 층수, 좌석 번호
- **수집 목적**: 시설 관련 요청 처리를 위한 위치 정보

![동적 섹션 예시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/32741541/original/8bb4Yp9-S67IyjbdZhtBW6lPwfauRteFdA.gif?1492586911)

## 동적 섹션 설정 방법

### 1단계: 관리자 권한으로 접근

1. **관리자 계정**으로 Freshservice에 로그인합니다
2. **Admin** 탭을 클릭합니다
3. **Account Settings** > **Field Manager**로 이동합니다

:::info 워크스페이스 환경
워크스페이스가 여러 개인 경우: **Admin** > **&#123;워크스페이스명&#125;** > **Account Settings** > **Field Manager** 순으로 접근하세요.
:::

### 2단계: 드롭다운 필드 생성

![필드 매니저 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/44787646/original/Ldu9_InJzupMmrlHJZCqT-yaMm5HpoBRfg.png?1555068933)

1. 티켓 폼에서 **커스텀 드롭다운 필드**를 생성합니다
2. 필드 설정을 완료하고 **저장**합니다
3. 저장 후 해당 필드에 마우스를 올리면 **Add Section** 옵션이 나타납니다

### 3단계: 동적 섹션 추가

![섹션 추가 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35633791/original/c9z0wWHZMzIUWOoulBXP3NTLnZqGGrMqEg.png?1509095528)

1. **Add Section** 버튼을 클릭합니다
2. 팝업창에서 다음을 설정합니다:
   - **섹션 제목**: 섹션의 명칭 입력
   - **연결된 필드 값**: 이 섹션이 표시될 드롭다운 값 선택

![섹션 설정 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/32708917/original/VdiuYs-NRbPMJTPb0zLxDkNmtEoryIjiIA.png?1492436313)

### 4단계: 섹션별 필드 구성

각 섹션에는 다양한 타입의 필드를 추가할 수 있습니다:

| 필드 타입 | 활용 사례 |
|-----------|-----------|
| **Single line text** | 디바이스명, 사용자명 |
| **Multi-Line text** | 문제 상세 설명, 추가 메모 |
| **Checkbox** | BYOD 여부, 긴급 여부 |
| **Number** | 디바이스 ID, 전화번호 |
| **Dropdown** | 디바이스 모델, 부서명 |
| **Date** | 문제 발생일, 요청 희망일 |
| **Decimal** | IP 주소, 버전 정보 |
| **Dependent Fields** | 카테고리와 하위 카테고리 |

![필드 구성 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35633815/original/Ymk-ClO1HWM58oqnUJF_77BJMRc6bytfuQ.png?1509095660)

## 필드 관리 기능

### 필드 재배열
- 섹션 내에서 **드래그 앤 드롭**으로 필드 순서를 변경할 수 있습니다
- 직관적인 인터페이스로 손쉬운 폼 구성이 가능합니다

### 필드 이동 및 복사
- **이동**: 소스 섹션에서 필드를 제거하고 타겟 섹션으로 완전히 이동
- **복사**: 소스 섹션에 필드를 유지하면서 타겟 섹션에 복사본 생성

### 섹션 삭제
- 섹션을 삭제하려면 먼저 **섹션 내 모든 필드를 삭제**해야 합니다
- 섹션명 옆의 **휴지통 아이콘**을 클릭하여 삭제합니다

## 실제 적용 예시

### IT 지원 요청 폼

```
문제 유형: [드롭다운]
├─ 하드웨어 문제 선택 시
│  ├─ 디바이스명 (텍스트)
│  ├─ 시리얼 번호 (텍스트)
│  └─ 구매일 (날짜)
│
├─ 소프트웨어 문제 선택 시
│  ├─ 프로그램명 (텍스트)
│  ├─ 버전 정보 (텍스트)
│  └─ 오류 메시지 (멀티라인 텍스트)
│
└─ 네트워크 문제 선택 시
   ├─ IP 주소 (소수점)
   ├─ 네트워크 위치 (드롭다운)
   └─ 연결 방식 (드롭다운)
```

![완성된 동적 폼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/32708643/original/pcrORIon1BAR_rBLrgfdt3_tDsaKywYLlg.png?1492435146)

## 주요 제한사항 및 주의사항

:::warning 기능 제한사항
- **최대 5개 동적 섹션**까지만 생성 가능합니다
- 제한에 도달하면 "Add Section" 버튼이 비활성화됩니다
- **단일 드롭다운 필드**에만 적용 가능 (멀티 드롭다운 불가)
:::

:::tip 필드명 중복 방지
- 동일한 필드명으로는 새 필드를 생성할 수 없습니다
- 기존 필드를 재사용하려면 **이동** 또는 **복사** 기능을 활용하세요
:::

## 활용 효과

### 에이전트 관점
- **구조화된 정보 수집**으로 티켓 분류가 용이합니다
- **필수 정보 누락 방지**로 빠른 문제 해결이 가능합니다
- **자동화 규칙 설정**에 동적 필드를 활용할 수 있습니다

### 사용자 관점
- **관련 없는 필드 숨김**으로 폼 작성이 간편합니다
- **단계별 안내**로 정확한 정보 입력이 가능합니다
- **상황별 맞춤 필드**로 효율적인 요청 제출이 가능합니다

## 문제 해결

### 섹션이 표시되지 않는 경우
1. 드롭다운 필드가 **저장**되었는지 확인
2. 섹션과 연결된 **필드 값이 정확**한지 점검
3. 브라우저 **캐시를 지우고** 새로고침

### 필드 이동이 안 되는 경우
1. **동일한 필드명**이 이미 존재하는지 확인
2. 타겟 섹션에 **충분한 공간**이 있는지 점검
3. 필드 타입 간 **호환성**을 확인

### 동적 섹션 한도 도달
1. 기존 섹션을 **통합**하여 개수 줄이기
2. **의존 필드** 기능으로 대체 검토
3. 폼 구조 **재설계**를 통한 최적화

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [사용자 정의 필드 생성](./custom-fields-creation)
- [의존 필드 설정](./dependent-fields-setup)
- [자동화 규칙 활용](../automation/automation-rules)
- [티켓 폼 관리](./ticket-form-management)
-->
