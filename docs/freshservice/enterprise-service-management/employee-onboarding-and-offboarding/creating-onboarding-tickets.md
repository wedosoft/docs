---
sidebar_position: 5
---

# 온보딩 티켓 생성

<div className="subtitle">
  이 문서는 "Creating Onboarding Tickets" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

When an onboarding request is raised, you might want to split and assign tasks between various teams. For example, if there are IT services and HR services that have to be provided as a part of an onboarding request, you will have to assign these subtasks to respective teams.

To enable this, you can create the parent and child tickets which will be created as a part of the onboarding request.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284479/original/6BR2rg6J6_GIIthPGmfAUrtu3Ch3xV7Zog.png?1592397029)

Creating Child Tickets

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284484/original/gagwT2jcMnA85J-EWeLXH0kTTGH0pIX5TQ.gif?1592397051)

- Click onCreate Child Ticket.
- InAssign to, choose which Agent group you want to assign this ticket to.
- Add fields from the Onboarding form to include information about the hires in your ticket.
- Now add the onboarding items that have to be provided as a part of this child ticket. You can choose items from the service items you’ve added to the onboarding kits in the previous steps.
- Click onCreateto create the child ticket.

Editing the Parent Ticket

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001295553/original/3dBshTmyBEDAI_oOX6RoeHiDHUl-YQrOpg.png?1592496070)

- Click on![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284474/original/RAB8j2jIsO-rfByw05vE-8ut1v28ZPVUzg.png?1592397025)on the parent ticket to the edit.
- InAssign to, choose which Agent group you want to assign this ticket to.
- Add fields from the Onboarding form to include information about the hires in your ticket.
- Now add the onboarding items that have to be provided as a part of this child ticket. All service items you’ve added to the onboarding kits in the previous steps will be automatically included to this ticket. Click onSaveto create the child ticket.

Your onboarding tickets are good to go! Now, go ahead and[Modify Approvals](https://support.freshservice.com/en/support/solutions/articles/50000002366)in Step 4.

Faq:

1. Where can I find the onboarding ticket fields of the stakeholders?

Navigate toAdmin / Global Settings > Employee Onboarding >UnderAdd Stakeholdersafter clicking on the respective stakeholder you will be able to view their fields.

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
