---
sidebar_position: 10
---

# 순차 티켓 처리

<div className="subtitle">
  이 문서는 "Sequential ticketing for child tickets" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

Do you get frustrated when you don’t have the necessary pre-requisites to resolve an open ticket? We heard you! Support your agents with all the information needed to resolve a ticket without causing delays and negatively impacting SLAs.

What is Sequential ticketing?

Sequential Ticketing enables admins to define dependencies between the child tickets of an employee onboarding request and have them become available for action when their prerequisites are completed. Each child ticket can be associated with a ticket dependent on information during the setup. The dependent tickets are called ‘successor tickets,’ and the ticket they depend upon is called the ‘predecessor ticket.’

For instance, background verification is a prerequisite for creating an email address in the case of a new employee. Email address is a prerequisite for enabling software access or issuing an ID card.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707286/original/E-ShmocW4lD4gWD609ooxHuYs1uZOgw0Og.png?1644316846)

With sequential ticketing, the admin can ensure the ‘Email ID creation’ ticket for the IT agent is assigned as an open ticket with SLA ON only after the HRBP resolves the ‘background verification’ ticket. Similarly, the ‘Software access’ and ‘ID card’ tickets are assigned as open tickets only after the IT team has created the email ID and the respective agent resolves the ticket. The successor tickets can remain created in a status with its SLA timer OFF so that the agents don’t breach the SLA when they are not actively working on them.

Setting up sequential ticketing:

1. While configuring the new employee onboarding module, create all the child tickets that have to be associated with the parent employee onboarding ticket.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707289/original/BLO_uI0JSimpoSph9KJmWgitpB8wJSxTTA.png?1644316852)
2. Edit the child tickets that have prerequisites needed for resolution of the ticket![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707287/original/fzjc_7wWfmQOHAqwt93ymDq8hN3gzluRyA.png?1644316848)
3. Select the predecessor ticket that needs to be resolved for the successor ticket to be open for action by the agent. A ticket can be associated with only one predecessor ticket.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707294/original/4EQ3-wavwEab1dV49RO_HaMoESWTbNj5MA.png?1644316853)

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707291/original/9XizNo2gn2vcpeAEN6946DSLQOCK6hE7Tg.png?1644316853)

1. Once the predecessor ticket is associated, the status of the child ticket will by default be ‘Pending’ upon creation until the predecessor ticket is closed/resolved. You can also choose to change it to any other status that has SLA turned OFF. On the resolution of the predecessor ticket, the successor child ticket’s status will be auto-changed to ‘Open.’

However, if the successor ticket’s status is changed manually or via a workflow rule after it is created, it will not auto-change to “Open” as it is assumed an agent is actively working on the successor ticket.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707288/original/U3xca2WgK4AaQt8P6X6z1AmeN0lNCAHEiQ.png?1644316850)![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707297/original/EZCkti8dURojk0djwDb8KZXj5dj2X3irjw.png?1644316853)

1. Once the child ticket is associated with the predecessor ticket, it can further be associated as a predecessor ticket to the consecutive child tickets.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707298/original/TlXJZoTW2-kIuKpEY-CXgtbCz04n6Ew-kw.png?1644316854)![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707296/original/P2AljcwsC2JrDN7XeAjXY9v5xDpcyRl00w.png?1644316853)
2. Once the request is successfully created, the ticket details page of each child ticket will display related ticket information like the parent onboarding request, predecessor ticket, and successor tickets.

Passing Information from Predecessor ticket to Successor Tickets

While associating child tickets with a predecessor ticket, you can also set up workflow automation to pass information from the predecessor ticket to the immediate successor child tickets. You can learn how to pass information between these tickets here.

The tickets that are further linked to the successor of a predecessor ticket are not considered as successor tickets of the predecessor ticket. Therefore you cannot pass information directly to them. Learn[more](https://support.freshservice.com/support/solutions/articles/50000003959-passing-information-between-employee-onboarding-child-tickets).

Please note:You can have only 25 levels of child tickets associated with each other in a hierarchy. For example: ‘Provide Software Access’ and ‘Provide ID Card’ belong to the same level, i.e., the 3rd level. Similarly, you can have a total of 25 levels linked to each other.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004707295/original/3dT05rasSZ_hm5leAcjksMr4OrRJVWWrqg.png?1644316853)

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

#### 문제: 온보딩 프로세스 지연
**원인**: 승인 단계의 병목 현상 또는 문서 누락
**해결**: 
1. 자동 에스컬레이션 규칙 설정으로 지연 방지
2. 체크리스트 기반 진행 상황 실시간 모니터링
3. 백업 승인자 지정으로 프로세스 연속성 보장

:::warning 주의사항
승인자가 부재 중일 때를 대비해 반드시 백업 승인자를 설정하세요.
:::

#### 문제: 시스템 접근 권한 설정 오류
**원인**: 역할별 권한 매핑 설정 미흡
**해결**:
1. 표준 역할 템플릿 사전 정의
2. 권한 검증 프로세스 자동화
3. 오류 발생 시 즉시 알림 시스템 구축

:::success 해결 완료
권한 설정이 정상적으로 완료되었습니다.
:::

## 모범 사례

### 효율적인 온보딩을 위한 체크리스트

:::tip 온보딩 성공 요소
- **사전 준비**: 입사 전 필요한 모든 자료와 계정 준비
- **개인화**: 역할과 부서에 맞는 맞춤형 온보딩 경험 제공
- **피드백**: 정기적인 진행 상황 점검 및 개선사항 수집
- **문서화**: 모든 과정을 문서화하여 향후 참조 및 개선에 활용
:::

## 관련 기능 연계

이 기능은 다음과 같은 Freshservice 모듈과 연계하여 사용할 수 있습니다:

- **사용자 관리**: 신규 사용자 계정 생성 및 권한 할당
- **자산 관리**: 업무용 장비 및 소프트웨어 라이선스 배정
- **서비스 카탈로그**: 역할별 필요 서비스 자동 신청
- **워크플로 자동화**: 반복 업무 자동화로 효율성 극대화
