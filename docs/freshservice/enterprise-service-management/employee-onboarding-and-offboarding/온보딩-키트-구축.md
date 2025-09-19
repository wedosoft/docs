---
sidebar_position: 4
---

# 온보딩 키트 구축

<div className="subtitle">
  이 문서는 "Building Onboarding Kits" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

You would want to provide your hires with the right onboarding items based on their roles. To do so, you can bundle these items into onboarding kits. You can build tailor-made kits to suit every role in your organization.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001714689/original/426ndfRfu9ONw2JxGSw3JvGDp0_nz7t_TA.png?1599746952)

- Choose the existing kit if it suits your needs. You can edit the name of the existing kit if needed. Or click onBuild a Kitif you want to build one from scratch.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284417/original/WctyNtMPJE3zagYxgotLEEIukfPABQGdGw.png?1592396522)

- To build role-specific kits, you can define who needs your kits by setting upconditions. For example, if you’re building a kit for Visual Designers, you can define a condition,Job Role includes DesignandDevelopment.
- Next, add items that have to be provided as a part of this kit. You can select items that you have populated in your service catalog.
- Additionally, it might be possible that some of the form fields in the service catalog items would remain the same for every employee belonging to a particular location, department, etc. To minimize the time taken while filling the forms out, you can prefill those fields. For instance, if you have a kit for all developers in your firm, the value for a field called “department” in an ID card service item can be prefilled as “Technology.” Similarly, for a software access service item, the value of purpose can be prefilled as “Employee Onboarding.”and To do so, click on the prefill fields option below the service catalog item, enter the field name and the value as per the required conditions.Note for Bulk Onboarding:If a mandatory dropdown field is added in 'Prefill fields' and the value chosen to be prefilled is deleted later in the Service Item's page, the requester will receive an error on submitting the form unless you enter a value that is present in the dropdown. It is advised that a new value be updated in the corresponding Prefill field after you delete the old one.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004160115/original/wNF7d0FNfpaQn7xKbHj5ZQKPwGQE98bYWA.png?1637061301)
- You can choose who can view items selected by the initiator from the visibility settings in the top right corner.The chosen stakeholder(s) can view items selected by the initiator in their onboarding form.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001714699/original/2g-FXY74QAvnxiea4IyAX5gtdlZGTg248A.png?1599747066)

Note:Items chosen by an initiator is visible to all stakeholders in the process if they are Freshservice Users. If a stakeholder is not a Freshservice user, they cannot view the items selected by the initiator in an onboarding request.

Is there a way to pick different build kits during the onboarding process using the portal, and if so, how?

The visibility of build kits during an onboarding request depends on the configured conditions found in

Admin --> Employee Onboarding --> Build Kits.![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011396496/original/tDKQAAmLwdpM_-jn1Esd-bLKltee9v316Q.png?1711730991)

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
