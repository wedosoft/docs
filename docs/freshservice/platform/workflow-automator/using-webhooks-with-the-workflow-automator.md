---
sidebar_position: 12
---

# 워크플로 자동화와 웹훅 사용하기

웹훅은 Freshservice의 워크플로 자동화에서 외부 시스템과의 실시간 통합을 가능하게 하는 강력한 도구입니다. 이 가이드는 웹훅을 효과적으로 활용하는 방법을 안내합니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


## 웹훅이란?

웹훅은 특정 이벤트가 발생했을 때 외부 URL로 HTTP 요청을 보내는 방법입니다. 이를 통해 Freshservice의 데이터를 실시간으로 다른 시스템에 전달하거나 외부 작업을 트리거할 수 있습니다.

## 웹훅의 주요 이점

- **실시간 데이터 동기화**: 이벤트 발생 즉시 데이터 전송
- **시스템 간 연동**: 다양한 도구와 플랫폼 연결
- **자동화 확장**: 외부 로직 실행으로 복잡한 자동화 구현
- **알림 시스템**: 외부 알림 채널로 즉시 전송

## 웹훅 설정 방법

### 1. 워크플로 자동화에서 웹훅 추가

1. **관리자 &gt; 워크플로 자동화**로 이동
2. 새 워크플로를 생성하거나 기존 워크플로 편집
3. **작업** 섹션에서 **웹훅 호출** 선택
4. 다음 정보 입력:
   - **URL**: 대상 엔드포인트 주소
   - **요청 방법**: GET, POST, PUT, PATCH, DELETE 중 선택
   - **헤더**: 필요한 인증 및 콘텐츠 타입 정보
   - **본문**: 전송할 데이터 (JSON 형식 권장)

### 2. 웹훅 본문 구성

```json
{
  "ticket_id": "``{{ticket.id}}``",
  "subject": "``{{ticket.subject}}``",
  "description": "``{{ticket.description}}``",
  "status": "``{{ticket.status}}``",
  "priority": "``{{ticket.priority}}``",
  "requester": {
    "email": "``{{ticket.requester.email}}``",
    "name": "``{{ticket.requester.name}}``"
  },
  "assigned_agent": "``{{ticket.agent.name}}``",
  "created_at": "``{{ticket.created_at}}``",
  "updated_at": "``{{ticket.updated_at}}``"
}
```

## 일반적인 웹훅 사용 사례

### 1. 외부 알림 시스템 연동

**Slack 알림 예시:**
```json
&#123;
  "text": "새 긴급 티켓이 생성되었습니다",
  "attachments": [
    {
      "color": "danger",
      "fields": [
        {
          "title": "티켓 ID",
          "value": "{{ticket.id&#125;}",
          "short": true
        },
        &#123;
          "title": "제목",
          "value": "{{ticket.subject&#125;}",
          "short": true
        },
        &#123;
          "title": "요청자",
          "value": "{{ticket.requester.email&#125;}",
          "short": true
        },
        &#123;
          "title": "우선순위",
          "value": "{{ticket.priority&#125;}",
          "short": true
        }
      ]
    }
  ]
}
```

### 2. CRM 시스템 동기화

고객 정보를 외부 CRM에 자동으로 업데이트:

```json
{
  "customer_email": "``{{ticket.requester.email}}``",
  "last_interaction": "``{{ticket.created_at}}``",
  "issue_type": "``{{ticket.category}}``",
  "priority_level": "``{{ticket.priority}}``",
  "assigned_representative": "``{{ticket.agent.email}}``"
}
```

### 3. 자산 관리 시스템 연동

자산 관련 티켓 정보를 CMDB에 업데이트:

```json
{
  "asset_id": "``{{ticket.asset.tag}}``",
  "incident_reported": "``{{ticket.created_at}}``",
  "issue_description": "``{{ticket.description}}``",
  "reporter": "``{{ticket.requester.name}}``",
  "status": "under_maintenance"
}
```

## 고급 웹훅 기능

### 1. 조건부 웹훅 실행

특정 조건에서만 웹훅을 실행하도록 설정:

- 우선순위가 '긴급'인 경우에만 실행
- 특정 그룹에 할당된 티켓에만 적용
- VIP 고객의 요청인 경우에만 트리거

### 2. 여러 웹훅 체인

순차적으로 여러 웹훅을 실행하여 복잡한 워크플로 구현:

1. 첫 번째 웹훅: 외부 시스템에 티켓 정보 전송
2. 두 번째 웹훅: 승인 시스템에 알림
3. 세 번째 웹훅: 자동 할당 로직 실행

### 3. 오류 처리 및 재시도

웹훅 실패 시 자동 재시도 설정:

- 재시도 횟수 지정
- 재시도 간격 설정
- 실패 시 대체 액션 정의

## 보안 고려사항

### 1. 인증 설정

웹훅 URL에 적절한 인증 메커니즘 구현:

- **API 키**: 헤더에 `Authorization: Bearer YOUR_API_KEY` 추가
- **Basic 인증**: 사용자명과 비밀번호 인코딩
- **서명 검증**: 요청 본문의 HMAC 서명 확인

### 2. HTTPS 사용

모든 웹훅 URL에 HTTPS 프로토콜 사용으로 데이터 암호화

### 3. IP 화이트리스팅

가능한 경우 Freshservice IP 주소만 허용하도록 설정

## 문제 해결

### 일반적인 문제들

**1. 웹훅이 실행되지 않음**
- 워크플로 조건 확인
- URL 유효성 검증
- 대상 서버 상태 확인

**2. 데이터가 제대로 전송되지 않음**
- JSON 형식 검증
- 플레이스홀더 구문 확인
- 대상 서버의 로그 확인

**3. 응답 시간 초과**
- 대상 서버의 응답 시간 개선
- 비동기 처리 구현 고려
- 타임아웃 설정 조정

## 모니터링 및 로깅

### 웹훅 실행 로그 확인

1. **관리자 &gt; 워크플로 자동화 &gt; 실행 로그**에서 웹훅 상태 확인
2. 실패한 웹훅의 오류 메시지 분석
3. 성공률 및 응답 시간 모니터링

### 대상 시스템 로깅

외부 시스템에서도 웹훅 수신 로그를 유지하여 문제 진단에 활용

웹훅을 통해 Freshservice의 자동화 기능을 외부 시스템으로 확장하면 훨씬 더 강력하고 유연한 워크플로를 구축할 수 있습니다.