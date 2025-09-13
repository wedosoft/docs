---
sidebar_position: 10
---

# 비즈니스 규칙을 통한 노코드 동적 폼 생성

:::info 문서 목적
비즈니스 규칙을 사용해서 코딩 없이 동적 폼을 구현하는 방법을 안내해요.
:::

비즈니스 규칙을 활용하면 코딩 없이도 동적이고 지능적인 폼을 생성할 수 있어요. 사용자 입력에 따라 필드가 나타나거나 사라지고, 조건에 따라 필수 필드가 변경되며, 데이터 검증을 자동으로 수행하는 고급 폼을 만들 수 있어요.

## 비즈니스 규칙의 핵심 기능

### 동적 필드 제어
- **필드 표시/숨김**: 조건에 따른 필드 가시성 제어
- **필드 활성화/비활성화**: 사용자 상호작용 제한
- **필드 필수/선택**: 동적 검증 규칙 적용
- **드롭다운 옵션 관리**: 조건에 따른 선택 항목 변경

### 폼 검증 및 제출 제어
- **폼 제출 방지**: 사용자 정의 검증 메시지와 함께 제출 차단
- **실시간 검증**: 사용자 입력 중 즉시 피드백 제공
- **조건부 필수 필드**: 상황에 맞는 필수 입력 항목 설정

## 티켓 폼용 비즈니스 규칙 설정

### 1단계: 비즈니스 규칙 생성 시작

**Admin > Business rules for Forms > Create New Rule**로 이동해요.

### 2단계: 규칙 유형 선택

다음 중에서 적용할 폼 유형을 선택해요:
- **Ticket** - 티켓 폼
- **Service Item** - 서비스 아이템 폼

### 3단계: 조건 설정

티켓 폼의 경우 다음 필드를 기반으로 조건을 구성할 수 있어요:

#### 기본 조건 필드
- **Logged-in user** - 로그인한 사용자
- **Requester/Requested for** - 요청자/대상자
- **Ticket properties** - 티켓 속성들

#### 고급 조건 활용
:::info 현재 티켓 조건
현재 티켓 조건은 편집 폼에서만 적용되며, 티켓 유형과 기본 티켓의 요청 항목을 기반으로 조건을 생성할 수 있어요.
:::

### 4단계: 액션 정의

조건이 충족될 때 수행할 액션을 선택해요:

#### 필드 가시성 제어
- **Show and Hide field** - 필드 표시/숨김
- **Enable and Disable fields** - 필드 활성화/비활성화

#### 필드 검증 제어
- **Mandate and Non-mandate fields** - 필드 필수/선택 설정
- **Prevent form submission** - 사용자 정의 검증 메시지로 폼 제출 방지

#### 드롭다운 관리
- **Set and Remove Dropdown Options** - 드롭다운 옵션 설정/제거

#### 추가 검증 옵션
**Validate the form on submission**을 통해 폼 제출 시 사용자 정의 오류 메시지로 검증할 수 있어요.

![비즈니스 규칙 액션 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001424852/original/r4d51zA5m1i9tWoB9ZiRLNTQunNmzRtpGg.png?1594396245)

## 서비스 아이템용 비즈니스 규칙

### 설정 방법

1. **Admin > Business rules for Forms > Create New Rule**로 이동해요
2. **Service Item** 옵션을 선택하세요

![서비스 아이템 규칙 생성](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013933330/original/Q64gTXBKTDjwUhEYyS15N3eRG68g1BolbA.png?1733387871)

### 조건 필드 구성

다음 필드를 기반으로 조건을 설정해요:

| 조건 필드 | 설명 |
|-----------|------|
| **Service Item** | 특정 서비스 아이템 선택 |
| **Logged-in user** | 현재 로그인한 사용자 |
| **Requester/Requested for** | 요청자 또는 요청 대상자 |

![서비스 아이템 조건 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013933352/original/J6ZiuAo1RVInDGzzidXWx1dmRF8Jx-AevA.png?1733387989)

### 동적 날짜 조건 활용

상대적이고 동적인 날짜 기반 조건을 서비스 요청에 구성할 수 있어요.

![동적 날짜 조건 예시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003377108/original/EhZ1veFfPqUlSJm1KuLUtX9wxdUiyELo_g.png?1626333813)

**실제 활용 예시**: 여행 신청 폼에서 시작 날짜가 종료 날짜보다 이전이고 현재 날짜보다 이후가 되도록 설정해서 소급 신청을 방지할 수 있어요.

![여행 신청 폼 예시](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50003377155/original/FWBjI00tXh7xhfCqokHlrkH5iFZd9rTasw.png?1626334043)

## 특수 기능 구현

### "다른 사람을 위한 요청" 옵션 비활성화

관리자는 비즈니스 규칙을 통해 **"Request for someone else"** 체크박스를 비활성화할 수 있어요.

#### 설정 방법
**Actions > Disable > Search Requester**를 선택해서 특정 서비스 아이템에 적용해요.

#### 규칙 동작
- **서비스 아이템**: 사용자가 다른 사용자를 위해 서비스를 요청할 수 없음
- **티켓 및 서비스 아이템**: 로그인한 사용자의 이메일이 요청자 필드에 자동으로 입력됨

![요청자 필드 자동 입력](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013973540/original/eD0hhudJf_VFTYkCwKveIXXi9K0csCOkVg.png?1733812849)

### CC 추가 기능 차단

서비스 아이템과 티켓 요청 생성 시 다른 사용자를 CC에 추가하는 것을 차단할 수 있어요.

#### 적용 범위
- **티켓**: 티켓 생성 및 편집 시 CC 추가 옵션 비활성화
- **서비스 아이템**: 새 서비스 요청 제출 시 CC 추가 옵션 비활성화

![CC 차단 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013973370/original/_pKgiALehmZJWsO36aLSHJW39KaspK3wlA.png?1733811945)

## 고급 설정 옵션

![고급 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001424848/original/X8kSmNnoP8Swg9VFCDN9sfSsc6qXWn-f9w.png?1594396240)

### 1. Auto-Reverse If False (자동 역순 처리)

조건이 충족되지 않을 때 액션을 자동으로 역순 처리해요.

**예시**: 상태가 "해결됨"으로 변경될 때 특정 필드를 필수로 설정한 경우, 상태가 "해결됨"이 아닐 때 자동으로 해당 필드를 선택사항으로 변경해요.

:::tip 권장 설정
추가 규칙 작성의 수고를 덜어주므로 모든 비즈니스 규칙에서 기본적으로 활성화하는 것을 권해요.
:::

### 2. Enforce System-Wide (시스템 전체 적용)

비즈니스 규칙을 모든 폼과 다음 작업에 적용해요:
- 일괄 작업을 통한 티켓 업데이트
- 목록 보기 편집
- 시나리오 자동화
- API 요청

## 규칙 관리 및 운영

### 규칙 목록 관리

![규칙 목록](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001424866/original/25cIKkAH39ajHnTv9kuefUhpdAy05i-7Uw.png?1594396395)

- **활성화/비활성화**: 개별 규칙을 토글로 제어
- **편집/삭제/복제**: 기존 규칙 관리 기능

### 규칙 실행 순서

여러 비즈니스 규칙이 동일한 필드에 적용될 때 마지막에 실행되는 규칙이 우선돼요. **Reorder** 기능을 사용해서 실행 순서를 변경할 수 있어요.

## 제한사항 및 규모

### 비즈니스 규칙 제한

#### 서비스 아이템당 제한
- **25개 미만 사용 계정**: 서비스 아이템당 최대 25개 규칙
- **25개 이상 사용 계정**: 기존 규칙 수에서 최대 5개 추가 가능
- **대량 사용자**: 제품 및 엔지니어링 팀 검토 필요

#### 기타 엔티티 제한
- **티켓 및 변경**: 계정당 250개 규칙 (기존 제한 유지)

### 적용 범위

#### 적용되는 경우
- 새 티켓/편집 티켓 폼
- 자식 티켓 폼
- 자산 세부 정보 페이지에서 생성된 티켓
- Freshcaller 통합을 통해 생성된 티켓
- 시스템 전체 적용 규칙: 일괄 작업, 시나리오 자동화, 목록 보기 편집, API 요청

#### 적용되지 않는 경우
- 이메일을 통해 생성/수정된 티켓
- 워크플로우 자동화
- 수퍼바이저 기능
- 대화형 UI
- 타사 앱
- 티켓 병합
- 서비스 봇 통합

## 모범 사례

### 설계 원칙

1. **테스트 우선**: 샌드박스 계정에서 먼저 규칙을 테스트
2. **단순성 추구**: 복잡한 규칙보다는 여러 개의 간단한 규칙 사용
3. **사용자 경험 고려**: 필드 표시/숨김이 사용자를 혼란스럽게 하지 않도록 주의
4. **성능 최적화**: 필요한 규칙만 활성화하여 폼 성능 유지

### 검증 및 오류 메시지

:::tip Pro Tip
"Validate form on submission" 옵션에서 오류 메시지를 미리 테스트해서 시스템 내에서 어떻게 표시되는지 확인한 후 저장하세요.
:::

### 필드 설정 권장사항

요청자용 비즈니스 규칙이 최적으로 작동하려면 필드가 폼 필드에서 표시 가능하고 편집 가능하도록 구성되어야 해요.

