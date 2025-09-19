---
sidebar_position: 9
---

# 하위 티켓 간 정보 전달

Freshservice의 하위 티켓 간 정보 전달을 통해 효율적인 직원 라이프사이클 관리를 구현할 수 있습니다.

:::info 주요 특징
- 자동화된 프로세스로 업무 효율성 극대화
- 실시간 진행 상황 추적 및 모니터링
- 역할 기반 권한 관리 및 승인 워크플로
:::

## 기능 설정 방법

### 1단계: 기본 설정 구성

1. **관리자 → 서비스 관리 → 직원 온보딩**으로 이동
2. **'새 설정'** 버튼 클릭
3. 필요한 권한 및 역할 설정

### 2단계: 상세 옵션 구성

1. 워크플로 규칙 정의
2. 알림 및 에스컬레이션 설정
3. 테스트 실행으로 동작 확인

:::warning 중요 사항
설정 변경 시 기존 진행 중인 프로세스에 영향을 줄 수 있으니 주의하세요.
:::

## 원본 기능 상세 정보

```html
<p ><br></p><p >Once you have configured the child tickets in your employee onboarding settings and defined which one is a predecessor and which one is a successor, you can use the Workflow Automator to pass information from a predecessor ticket to a successor ticket.</p><p ><br></p><p >Here's how you can do it:</p><p ><br></p><p >1. Identify the predecessor ticket with the help of Event and Condition blocks. In this case, we've defined them as follows:</p><p ><br></p><p >Event: Service Request is updated</p><p ><br></p><p >Condition 1: Source is Employee Onboarding</p><p >Condition 2: Subject includes the keyword: Workstation Allocation</p><p >Condition 3: Status is changed to Resolved</p><p ><br></p><p ><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004667270/original/kxH4nO4SAcxs2lpEj5CL1x22jEgOGq0E9g.png?1643816584" style={{width: auto;}} ></p><p ><br></p><p ><br></p><p ><br></p><p >2. Add an action block and choose the desired action. In the example below, as we wish to update successor tickets with the details of workspace allocation, we're updating their workspace location field with the help of a placeholder from the predecessor ticket. We're applying this action by choosing "Associated Successor Tickets" from the dropdown at the top.</p><p ><br></p><p ><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004667286/original/NorK4BzikiLanJ90Q5BJ7I78fziMlt-5TA.png?1643816688" style={{width: auto;}} ></p><p ><br></p><p ><br></p><p >And that's how you can apply any action on a predecessor ticket's successor tickets.</p><p ><br></p><p ><br></p>
```

:::tip 효율적인 활용
- 테스트 환경에서 먼저 검증 후 운영 환경 적용
- 사용자 그룹별로 단계적 배포 권장
- 정기적인 프로세스 검토 및 개선
:::

## 실무 활용 예시

### 상황 1: 대기업 신입사원 온보딩
**목표**: 대규모 조직에서의 체계적인 신입사원 적응 지원
**방법**: 
1. 부서별 맞춤형 온보딩 키트 준비
2. 단계별 체크리스트와 진행 상황 추적
3. 멘토링 시스템과 연계한 지속적 지원

**결과**: 신입사원 만족도 향상 및 조기 적응 달성

### 상황 2: 원격 근무 환경에서의 온보딩
**목표**: 비대면 환경에서도 효과적인 온보딩 실현
**방법**:
1. 디지털 온보딩 키트 및 가상 오리엔테이션
2. 온라인 협업 도구 교육 및 계정 설정
3. 정기적인 화상 체크인 및 피드백 수집

**결과**: 물리적 거리를 극복한 성공적인 팀 통합

### 상황 3: 계약직 및 임시직 빠른 온보딩
**목표**: 단기 근무자를 위한 효율적 온보딩 프로세스
**방법**:
1. 필수 정보만 포함된 간소화된 온보딩 키트
2. 자동화된 시스템 접근 권한 부여
3. 업무 시작 즉시 필요한 도구 및 정보 제공

**결과**: 빠른 업무 투입과 생산성 확보

## 문제 해결

### 자주 발생하는 문제

#### 문제: 프로세스 진행 지연
**원인**: 승인 단계의 병목 현상 또는 필수 정보 누락
**해결**: 
1. 자동 에스컬레이션 규칙 설정으로 지연 방지
2. 체크리스트 기반 진행 상황 실시간 모니터링
3. 백업 승인자 지정으로 프로세스 연속성 보장

:::success 해결 완료
프로세스가 정상적으로 진행됩니다.
:::

#### 문제: 권한 설정 오류
**원인**: 역할별 권한 매핑 설정 미흡
**해결**:
1. 표준 역할 템플릿 사전 정의
2. 권한 검증 프로세스 자동화
3. 오류 발생 시 즉시 알림 시스템 구축

## 관련 기능 연계

이 기능은 다음과 같은 Freshservice 모듈과 연계하여 사용할 수 있습니다:

- **사용자 관리**: 신규 사용자 계정 생성 및 권한 할당
- **자산 관리**: 업무용 장비 및 소프트웨어 라이선스 배정
- **서비스 카탈로그**: 역할별 필요 서비스 자동 신청
- **워크플로 자동화**: 반복 업무 자동화로 효율성 극대화
