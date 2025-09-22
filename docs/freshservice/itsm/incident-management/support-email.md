---
sidebar_position: 5
---

# 지원 이메일 주소 설정하기

Freshservice에서 효과적인 티켓 관리를 위해서는 지원 이메일 주소를 올바르게 설정하는 것이 중요합니다. 이를 통해 고객이 이메일로 보낸 요청이 자동으로 티켓으로 변환되어 체계적으로 관리할 수 있습니다.

:::info 기본 이메일 주소
Freshservice 계정 생성 시 기본적으로 `support@{domain}.freshservice.com` 형태의 이메일 주소가 제공됩니다.
:::

## 사용자 정의 이메일 주소 설정

### 1단계: 도메인 설정

자체 도메인을 사용하여 전문적인 지원 이메일 주소를 만들 수 있습니다:

1. **Admin > Channels > Email**로 이동합니다
2. **Add new support email**을 클릭합니다
3. 원하는 이메일 주소를 입력합니다 (예: `support@yourcompany.com`)

### 2단계: DNS 설정

이메일 전달을 위해 DNS 설정이 필요합니다:

#### MX 레코드 설정
```
Type: MX
Host: support (또는 하위 도메인)
Value: mx.freshservice.com
Priority: 10
```

#### CNAME 레코드 설정 (선택사항)
```
Type: CNAME
Host: support
Value: email.freshservice.com
```

### 3단계: SPF 레코드 설정

이메일 전달 신뢰성을 위해 SPF 레코드를 추가합니다:

```
Type: TXT
Host: @ (또는 루트 도메인)
Value: v=spf1 include:email.freshservice.com ~all
```

## 이메일 처리 규칙 설정

### 자동 티켓 생성 규칙

이메일이 티켓으로 변환될 때의 규칙을 설정할 수 있습니다:

#### 기본 설정
- **제목**: 이메일 제목이 티켓 제목이 됩니다
- **설명**: 이메일 본문이 티켓 설명이 됩니다
- **요청자**: 발신자가 요청자로 설정됩니다
- **우선순위**: 기본 우선순위가 적용됩니다

#### 고급 설정
- **키워드 기반 분류**: 이메일 내용에 따른 자동 분류
- **첨부파일 처리**: 이메일 첨부파일의 티켓 첨부
- **서명 제거**: 이메일 서명 자동 제거

### 이메일 템플릿 설정

#### 자동 회신 템플릿
```
안녕하세요 {{ticket.requester.name}}님,

귀하의 요청을 접수했습니다.
티켓 번호: {{ticket.id}}
제목: {{ticket.subject}}

빠른 시일 내에 답변드리겠습니다.

감사합니다.
{{company.name}} 지원팀
```

#### 해결 알림 템플릿
```
안녕하세요 {{ticket.requester.name}}님,

귀하의 요청이 해결되었습니다.
티켓 번호: {{ticket.id}}
해결 내용: {{ticket.resolution_notes}}

추가 문의사항이 있으시면 언제든 연락주세요.

감사합니다.
{{company.name}} 지원팀
```

## 다중 이메일 주소 관리

### 부서별 이메일 주소

다양한 부서나 유형별로 별도의 이메일 주소를 설정할 수 있습니다:

- `it-support@yourcompany.com` - IT 지원
- `hr-support@yourcompany.com` - HR 지원
- `facilities@yourcompany.com` - 시설 관리

### 자동 할당 규칙

이메일 주소별로 자동 할당 규칙을 설정할 수 있습니다:

```
it-support@yourcompany.com → IT 그룹 자동 할당
hr-support@yourcompany.com → HR 그룹 자동 할당
facilities@yourcompany.com → 시설 관리 그룹 자동 할당
```

## 이메일 보안 설정

### DKIM 설정

이메일 인증을 위한 DKIM 설정:

1. Freshservice에서 DKIM 키 생성
2. DNS에 DKIM 레코드 추가
3. 설정 확인 및 활성화

### DMARC 정책

이메일 스푸핑 방지를 위한 DMARC 정책:

```
Type: TXT
Host: _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:admin@yourcompany.com
```

## 이메일 모니터링 및 관리

### 이메일 로그 확인

이메일 처리 상태를 모니터링할 수 있습니다:

- **수신된 이메일**: 성공적으로 처리된 이메일
- **실패한 이메일**: 처리 실패한 이메일과 원인
- **스팸 처리**: 스팸으로 분류된 이메일

### 문제 해결

#### 일반적인 문제들

1. **이메일이 티켓으로 변환되지 않음**
   - DNS 설정 확인
   - 이메일 주소 설정 확인
   - 스팸 필터 확인

2. **중복 티켓 생성**
   - 제목 패턴 설정 확인
   - 이메일 스레드 설정 확인

3. **첨부파일 문제**
   - 파일 크기 제한 확인
   - 지원되는 파일 형식 확인

### 성능 최적화

- **이메일 처리 속도**: 일반적으로 1-2분 내 처리
- **대용량 첨부파일**: 클라우드 링크 사용 권장
- **대량 이메일**: 배치 처리로 성능 최적화

:::warning 주의사항
- 이메일 설정 변경 시 기존 티켓에 영향을 주지 않습니다
- DNS 변경사항은 전파되는 데 최대 24시간이 걸릴 수 있습니다
- 이메일 전달 테스트를 통해 설정을 확인하세요
:::