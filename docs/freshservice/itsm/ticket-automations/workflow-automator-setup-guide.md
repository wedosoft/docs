---
sidebar_position: 2
---

# Workflow Automator 설정 및 관리

Workflow Automator는 티켓 생성, 업데이트 등 특정 이벤트 발생 시 즉시 동작하는 자동화 규칙을 설정하여 반복적인 업무를 효율화하는 핵심 기능입니다.

:::info Workflow Automator 접근 및 권한
- 관리자 권한 필요: Admin > Automation & Productivity > Automation > Workflow Automator
- 규칙 생성 및 수정 권한은 관리자 및 권한이 부여된 사용자만 가능
- 활성화된 규칙은 즉시 적용되므로 테스트 환경에서 먼저 검증 권장
:::

## Workflow Automator 설정 방법

### 1단계: Workflow Automator 접근
1. **Admin** > **Automation & Productivity** > **Automation** > **Workflow Automator**로 이동
2. **New Rule** 클릭하여 새 규칙 생성
3. 규칙 이름과 설명 입력

### 2단계: 이벤트 설정
워크플로우가 실행될 트리거 이벤트를 선택합니다.

**주요 이벤트 유형:**
- **Ticket is Raised**: 새 티켓 생성 시
- **Ticket is Updated**: 티켓 업데이트 시
- **Priority is changed**: 우선순위 변경 시
- **Status is changed**: 상태 변경 시
- **Agent is assigned**: 담당자 할당 시

### 3단계: 조건 설정
자동화가 실행될 구체적인 조건을 정의합니다.

**조건 설정 예시:**
```
조건 1: Subject contains "긴급"
조건 2: Priority is "높음" OR "긴급"
조건 3: Category is "인프라"
```

### 4단계: 액션 설정
조건이 충족될 때 실행할 액션을 선택합니다.

**사용 가능한 액션:**
- **상태 변경**: 열림, 진행중, 해결됨 등
- **우선순위 설정**: 낮음, 보통, 높음, 긴급
- **담당자 지정**: 특정 에이전트나 그룹에 할당
- **카테고리 설정**: 사전 정의된 카테고리로 분류
- **태그 추가**: 식별 및 필터링용 태그
- **노트 추가**: 공개 또는 비공개 노트
- **이메일 알림 발송**: 관련자에게 알림

## 조건 필드 활용

### 티켓 관련 필드
- **Subject** (제목): 티켓 제목 키워드 검색
- **Description** (설명): 티켓 내용 키워드 검색
- **Status** (상태): 현재 티켓 상태
- **Priority** (우선순위): 티켓 우선순위 레벨
- **Category** (카테고리): 사전 정의된 카테고리
- **Sub-category** (하위 카테고리): 세부 분류
- **Source** (소스): 티켓 생성 경로
- **Tags** (태그): 할당된 태그

### 요청자 관련 필드
- **Requester Email** (요청자 이메일): 요청자 이메일 주소
- **Requester Department** (요청자 부서): 요청자 소속 부서
- **Requester Location** (요청자 위치): 요청자 근무지

### 에이전트 관련 필드
- **Agent** (담당 에이전트): 현재 할당된 담당자
- **Agent Group** (에이전트 그룹): 담당 그룹

### 시간 관련 필드
- **Created Date** (생성일): 티켓 생성 일시
- **Updated Date** (업데이트일): 마지막 업데이트 일시
- **Hours since last update** (마지막 업데이트 이후 시간): 경과 시간

## 실무 활용 예시

### 상황 1: VIP 고객 자동 우선순위 설정
**목표**: 중요 고객의 티켓을 자동으로 높은 우선순위로 설정
**방법**: 
1. 이벤트: "Ticket is Raised"
2. 조건: "Requester Email contains @vip-company.com"
3. 액션: Priority를 "높음"으로 설정, VIP 담당 그룹에 할당

**결과**: VIP 고객 만족도 향상 및 신속한 대응 체계 구축

### 상황 2: 스팸 티켓 자동 필터링
**목표**: 특정 키워드가 포함된 스팸 티켓 자동 처리
**방법**: 
1. 이벤트: "Ticket is Raised"
2. 조건: "Subject or Description contains 광고 OR 홍보 OR 마케팅"
3. 액션: "Mark ticket as Spam" 실행

**결과**: 수동 스팸 처리 시간 90% 절약

### 상황 3: 업무 시간 외 자동 응답
**목표**: 업무 시간 외 생성된 티켓에 자동 응답 발송
**방법**: 
1. 이벤트: "Ticket is Raised"
2. 조건: "Created outside business hours"
3. 액션: 요청자에게 "업무 시간 중 처리 예정" 이메일 발송

**결과**: 고객 안심 효과 및 브랜드 신뢰도 향상

## 고급 설정 옵션

### 복합 조건 설정
```
조건 그룹 1 (AND):
- Subject contains "서버"
- Priority is "긴급"

조건 그룹 2 (OR):
- Requester Department is "개발팀"
- Requester Department is "인프라팀"
```

### 시간 기반 조건
```
조건:
- Created Date is "업무 시간 외"
- Hours since creation is "greater than 2"
```

:::warning 대소문자 구분 주의
"Subject/Description contains" 조건을 사용할 때 입력한 텍스트는 대소문자를 구분합니다. "Password"와 "password"는 서로 다른 것으로 인식되므로 주의하세요.
:::

## 문제 해결

### 자주 발생하는 문제

#### 문제: 자동화 규칙이 실행되지 않음
**원인**: 조건 설정이 너무 제한적이거나 대소문자 불일치
**해결**: 
1. 조건을 단순화하여 테스트
2. 대소문자 정확성 확인
3. 테스트 티켓으로 조건 검증

#### 문제: 중복 액션 실행
**원인**: 여러 자동화 규칙이 동시에 적용됨
**해결**: 
1. 규칙 우선순위 조정
2. 조건 범위 명확화
3. 규칙 간 충돌 검토

:::success 설정 완료
Workflow Automator 설정이 완료되었습니다. 이제 지정한 조건에 따라 자동으로 티켓이 처리됩니다. 정기적으로 자동화 로그를 확인하여 올바르게 작동하는지 모니터링하세요.
:::