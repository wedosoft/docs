---
sidebar_position: 9
---

# 자동화 규칙 완전 가이드

자동화 규칙은 Freshservice의 핵심 기능으로, 조건(Conditions)과 액션(Actions)의 조합을 통해 복잡한 비즈니스 로직을 자동화하여 서비스 데스크 운영 효율성을 극대화합니다.

:::info 자동화 규칙 설계 원칙
- 단계적 접근: 간단한 규칙부터 시작하여 점진적으로 복잡한 로직 구현
- 명확한 조건: 모호하지 않은 구체적인 조건 설정으로 예상치 못한 동작 방지
- 액션 순서: 논리적 순서에 따른 액션 배치로 일관된 결과 보장
- 테스트 필수: 프로덕션 적용 전 충분한 테스트로 안정성 확보
:::

## 자동화 규칙 생성 프로세스

### 1단계: 규칙 계획 수립
자동화 규칙을 생성하기 전에 명확한 계획을 수립해야 합니다.

**계획 수립 체크리스트:**
```
비즈니스 요구사항 분석:
- 해결하고자 하는 문제 정의
- 자동화 대상 프로세스 식별
- 예상 효과 및 성공 지표 설정

기술적 요구사항 정의:
- 필요한 조건 필드 확인
- 실행할 액션 목록 작성
- 예외 상황 처리 방안 수립
```

### 2단계: 조건(Conditions) 설계

#### 기본 조건 유형
**필드 기반 조건:**
- **텍스트 필드**: Subject, Description에서 키워드 검색
- **선택 필드**: Status, Priority, Category 등 드롭다운 값
- **사용자 필드**: Requester, Agent, Group 등 담당자 정보
- **날짜 필드**: Created Date, Updated Date 등 시간 기반 조건

**고급 조건 설정:**
```
단일 조건 예시:
- Subject contains "긴급"
- Priority is "높음"
- Requester Department is "개발팀"

복합 조건 예시 (AND):
- Subject contains "서버" AND
- Priority is "긴급" AND  
- Created Date is "업무 시간 중"

복합 조건 예시 (OR):
- Category is "하드웨어" OR
- Category is "소프트웨어" OR
- Subject contains "설치"
```

#### 조건 최적화 전략
**효율적인 조건 순서:**
1. **가장 제한적인 조건 우선**: 빠른 필터링으로 성능 향상
2. **단순 필드 조건 먼저**: 복잡한 계산이 필요한 조건은 후순위
3. **예외 조건 명시**: 원하지 않는 결과를 방지하는 제외 조건 추가

### 3단계: 액션(Actions) 구성

#### 기본 액션 카테고리

**티켓 속성 변경:**
```
상태 관리:
- Set Status to "진행 중"
- Set Status to "해결됨"
- Set Status to "종료됨"

우선순위 관리:
- Set Priority to "긴급"
- Set Priority to "높음"
- Increase Priority by 1 level

할당 관리:
- Assign to Agent "홍길동"
- Assign to Group "IT 지원팀"
- Auto-assign based on workload
```

**커뮤니케이션 액션:**
```
알림 발송:
- Send email to Requester
- Send email to Agent
- Send SMS to Manager
- Post to Slack channel

노트 추가:
- Add public note
- Add private note
- Add templated response
```

**고급 액션:**
```
외부 시스템 연동:
- Create JIRA issue
- Update ServiceNow record
- Send webhook to external API
- Trigger Lambda function

데이터 처리:
- Update custom fields
- Calculate SLA timers
- Generate reports
- Archive attachments
```

## 복잡한 규칙 조합 패턴

### 패턴 1: 다단계 에스컬레이션 규칙
```
규칙명: "VIP 고객 3단계 에스컬레이션"

조건:
- Requester Custom Field "VIP Status" is "Yes" AND
- Status is "신규" OR "진행 중" AND
- Hours since last update > 2

액션 체인:
1. 1차 액션 (즉시):
   - Send email to assigned agent
   - Add urgent tag
   - Set priority to "높음"

2. 2차 액션 (1시간 후, Supervisor 규칙):
   - Escalate to team leader
   - Send SMS notification
   - Add escalation note

3. 3차 액션 (2시간 후):
   - Escalate to manager
   - Create management report
   - Schedule follow-up call
```

### 패턴 2: 조건부 자동 해결 규칙
```
규칙명: "표준 요청 자동 해결"

복합 조건 (모든 조건 만족):
- Category is "표준 요청" AND
- Sub-category is "비밀번호 재설정" AND
- Requester verified identity is "True" AND
- No manual intervention flag is set

조건부 액션:
IF (Business hours):
  - Execute password reset
  - Send new password via secure email
  - Set status to "해결됨"
  - Add completion note
ELSE:
  - Queue for next business day
  - Send acknowledgment email
  - Set priority to "낮음"
```

### 패턴 3: 인텔리전트 라우팅 규칙
```
규칙명: "스마트 티켓 라우팅"

분기 조건:
SWITCH (Subject + Description analysis):
  CASE contains "네트워크", "연결", "인터넷":
    - Assign to "네트워크팀"
    - Set category to "인프라"
    - Add "네트워크" tag
    
  CASE contains "이메일", "Outlook", "Exchange":
    - Assign to "이메일팀"
    - Set category to "애플리케이션"
    - Check Exchange server status
    
  CASE contains "프린터", "인쇄", "스캔":
    - Assign to "하드웨어팀"
    - Set category to "하드웨어"
    - Auto-order toner if needed
    
  DEFAULT:
    - Assign to "일반 지원팀"
    - Request manual categorization
```

## 실무 활용 예시

### 상황 1: 글로벌 제조기업 24시간 운영 지원
**목표**: 전 세계 3개 지역의 24시간 생산라인 지원 자동화
**방법**: 
1. 지역별 시간대 기반 자동 라우팅 규칙
2. 언어별 자동 번역 및 응답 시스템
3. 생산 중단 위험도 기반 우선순위 자동 할당

**핵심 규칙:**
```
생산 라인 긴급 대응 규칙:
조건:
- Subject contains "생산중단", "라인다운", "설비고장"
- Requester Location matches production facilities
- Time is production hours for that location

액션:
- Set priority to "긴급"
- Assign to local production support team
- Send SMS to production manager
- Create real-time dashboard alert
- Auto-conference call setup if >30min
```

**결과**: 평균 대응 시간 75% 단축, 생산 다운타임 50% 감소

### 상황 2: 금융 서비스 보안 강화 자동화
**목표**: 보안 인시던트의 즉각적인 탐지 및 대응 체계 구축
**방법**: 
1. 보안 키워드 기반 자동 분류 및 에스컬레이션
2. 규정 준수 요구사항 자동 확인 및 처리
3. 감사 추적을 위한 자동 로깅 시스템

**핵심 규칙:**
```
보안 인시던트 자동 대응:
조건:
- Subject OR Description contains security keywords
- Severity assessment > threshold
- Compliance flag is triggered

자동 대응 체인:
1. 즉시 격리 (0분):
   - Disable affected accounts
   - Block suspicious IP addresses
   - Alert security team

2. 조사 시작 (5분):
   - Create investigation ticket
   - Gather initial evidence
   - Notify compliance officer

3. 보고서 생성 (30분):
   - Generate incident report
   - Update risk assessment
   - Schedule management briefing
```

**결과**: 보안 인시던트 평균 탐지 시간 90% 단축, 규정 준수율 100% 달성

### 상황 3: 대학교 통합 학사 지원 시스템
**목표**: 학생, 교수, 직원의 다양한 요청을 자동으로 분류 및 처리
**방법**: 
1. 학번/교번 기반 자동 신원 확인 및 권한 검증
2. 학사 일정 연동 자동 처리 시스템
3. 부서별 승인 워크플로우 자동화

**핵심 규칙:**
```
학사 요청 자동 처리:
조건 분기:
- Student ID pattern match → 학생 요청 프로세스
- Faculty ID pattern match → 교수 요청 프로세스  
- Staff ID pattern match → 직원 요청 프로세스

학생 성적 관련 자동화:
IF (Request type = "성적 정정"):
  - Verify enrollment status
  - Route to course instructor
  - Set deadline = grade submission + 30 days
  - Auto-remind before deadline
  
IF (Request type = "졸업 요건 확인"):
  - Query academic system
  - Generate requirement checklist
  - Auto-schedule advisor meeting
  - Send graduation timeline
```

**결과**: 학사 업무 처리 시간 60% 단축, 학생 만족도 35% 향상

## 규칙 관리 및 거버넌스

### 규칙 라이프사이클 관리
```
개발 단계:
1. 요구사항 분석 및 설계
2. 개발 환경에서 구현
3. 단위 테스트 및 검증

테스트 단계:
1. 통합 테스트 환경 배포
2. 시나리오 기반 테스트
3. 성능 및 안정성 검증

프로덕션 배포:
1. 점진적 롤아웃 (10% → 50% → 100%)
2. 실시간 모니터링
3. 롤백 계획 준비

운영 및 최적화:
1. 성능 지표 모니터링
2. 정기적 규칙 검토
3. 지속적 개선
```

### 규칙 충돌 방지
```
우선순위 매트릭스:
1. 보안 관련 규칙 (최우선)
2. 컴플라이언스 규칙
3. 비즈니스 크리티컬 규칙
4. 일반 자동화 규칙

충돌 해결 전략:
- 배타적 조건 설정
- 실행 순서 정의
- 조건 중복 검사
- 정기적 규칙 감사
```

## 고급 기법 및 최적화

### 동적 조건 활용
```
플레이스홀더 기반 조건:
- "Hours since {{ticket.created_at}} > {{custom_field.sla_hours}}"
- "{{requester.department}} in {{approved_departments_list}}"
- "{{current_time}} between {{business_hours.start}} and {{business_hours.end}}"

계산된 필드 조건:
- Ticket age calculation
- Business hours exclusion
- SLA remaining time
- Workload distribution metrics
```

### 머신러닝 기반 자동화
```
AI 지원 분류:
- 자연어 처리 기반 카테고리 예측
- 과거 패턴 분석을 통한 우선순위 추천
- 해결 시간 예측 기반 자동 에스컬레이션
- 고객 감정 분석 기반 대응 전략
```

## 문제 해결 및 디버깅

### 일반적인 문제들

#### 문제: 규칙이 예상대로 작동하지 않음
**진단 단계:**
1. 조건 로직 검증
2. 테스트 데이터로 단계별 확인
3. 로그 분석을 통한 실행 추적

**해결 방법:**
```
디버깅 체크리스트:
□ 조건 문법 정확성 확인
□ 필드명 및 값 정확성 검증
□ 논리 연산자 (AND/OR) 올바른 사용
□ 괄호를 이용한 우선순위 명확화
□ 예외 케이스 조건 추가
```

#### 문제: 성능 저하 및 처리 지연
**최적화 방법:**
```
성능 튜닝:
1. 조건 순서 최적화 (제한적 조건 우선)
2. 불필요한 조건 제거
3. 복잡한 액션 분리
4. 배치 처리 활용
5. 캐싱 전략 적용
```

:::tip 규칙 설계 모범 사례
효과적인 자동화 규칙은 단순함에서 시작됩니다. 복잡한 로직보다는 이해하기 쉽고 유지보수가 용이한 규칙을 만드는 것이 장기적으로 더 효과적입니다.
:::

:::success 자동화 규칙 완성
포괄적인 자동화 규칙 시스템이 구축되었습니다. 이제 복잡한 비즈니스 로직도 효율적으로 자동화할 수 있습니다.
:::