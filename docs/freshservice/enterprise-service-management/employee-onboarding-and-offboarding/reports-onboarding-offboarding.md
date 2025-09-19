---
sidebar_position: 12
---

# 온보딩 및 오프보딩 리포트

<div className="subtitle">
  이 문서는 "Reports for Onboarding and Offboarding" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

With Onboarding and Offboarding reports you now get a bird’s eye view of your onboarding and offboarding operations in a matter of a few clicks. Get actionable insights on the entire onboarding/offboarding operations, and identify gaps and bottlenecks to further streamline your workflows.

Freshservice provides curated reports to get an overall glimpse of your onboarding or offboarding operations. You can also create custom reports to stay on top of the metrics that matter to your business.

TABLE OF CONTENTS

- [Curated report for onboarding](#Curated-report-for-onboarding)[Overview](#Overview-)[Onboarding child tickets](#Onboarding-child-tickets)
- [Overview](#Overview-)
- [Onboarding child tickets](#Onboarding-child-tickets)
- [Curated report for offboarding](#Curated-report-for-offboarding)[Overview](#Overview--1)[Offboarding child tickets](#Offboarding-child-tickets)
- [Overview](#Overview--1)
- [Offboarding child tickets](#Offboarding-child-tickets)
- [Custom reports on Onboarding / Offboarding](#Custom-reports-on-Onboarding-/-Offboarding)
- [Impact on Onboarding APIs](#Impact-on-Onboarding-APIs)

## Curated report for onboarding

- From the left panel, go toReporting > Analytics > Curated reports.Click on theOnboarding requests overviewreport.
- You will be able to see data under two tabs accessible from the bottom of the screen:

### Overview

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346652/original/znMlqWU96VC64quKkXRCkXIv3F-9gOWMCQ.png?1702288663)

Here are the key data metrics you can review in theOverviewtab of the curated report.

- Total requests
- Open requests
- Closed requests
- Average time to close onboarding requests (calculated in business hours defined in Global Settings)
- Open requests - older than 15 days
- Top request initiators
- Average time taken - by status

NOTE: An onboarding request goes through 3 status values
- Awaiting Information: After the Initiator triggers the onboarding request, if the stakeholders are yet to fill the forms assigned to them, the request will be in the Awaiting Information status.
- In-process: After all stakeholders have filled out the form, the tickets get automatically created and the request moves to In-process status. 
- Closed: After the parent ticket has been moved to ‘Closed’ or ‘Resolved’ status, the request automatically moves to Closed status.

- Onboarding Request - Trend

NOTE: You can apply filters for Location, Department, and Date Range to fetch deeper insights and trends across different available metrics.

### Onboarding child tickets

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346695/original/qS4V2y7pDP556SgxRb5ebTBIgp8KJjxGSw.png?1702288807)

Here are the key data metrics you can review in theOnboarding Child TIcketstab of the curated report.

- Total child tickets
- Open child tickets
- Closed child tickets
- Average resolution time - child tickets
- Time spent by agent group

NOTE: You can apply filters for Date range, Agent group, and Agent to fetch deeper insights and trends across different available metrics.

## Curated report for offboarding

- From the left panel, go toReporting > Analytics > Curated reports.Click on theOffboarding requests overviewreport.
- You will be able to see data under two tabs accessible from the bottom of the screen:

### Overview

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346710/original/rMx5r3mxiJ0QQ2_rnKH5zKufR7_bRjameA.png?1702288845)

Here are the key data metrics you can review in theOverviewtab of the curated report.

- Total requests
- Open requests
- Closed requests
- Average time to close (calculated in business hours defined in Global Settings)
- Open requests - older than 15 days
- Top request initiators
- Average time taken by status

NOTE: An offboarding request goes through 3 status values
- Awaiting Information: After the Initiator triggers the offboarding request, if the stakeholders are yet to fill the forms assigned to them, the request will be in the Awaiting Information status.
- In-process: After all stakeholders have filled out the form, the tickets get automatically created and the request moves to In-process status.
- Closed: After the parent ticket has been moved to ‘Closed’ or ‘Resolved’ status, the request automatically moves to Closed status.

- Offboarding Request - Trend

NOTE: You can apply filters for Location, Department, and Date Range to fetch deeper insights and trends across different available metrics.

### Offboarding child tickets

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346746/original/LuUSOCAkUOkIXZAXYS1N9lntbRcIvQeiww.png?1702288964)

Here are the key data metrics you can review in theOffboarding Child Ticketstab of the curated report.

- Total child tickets
- Open child tickets
- Total closed child tickets
- Average resolution time - child tickets
- Time spent by agent group

NOTE: You can apply filters for Date range, Agent group, and Agent to fetch deeper insights and trends across different available metrics.

## Custom reports on Onboarding / Offboarding

Apart from using the curated reports for onboarding and offboarding, you can also create custom reports as per your needs to create a customized dashboard for the metrics that you want to stay updated about.

- Go toReporting > Analytics > All Reportsand click on theNew Reportbutton at the top right part of the screen.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010343796/original/bbyCh__80Q73_hJGfmKHBVzxrhmYdQoUaQ.png?1702273043)

- Drag and drop the required widgets and use ‘Onboarding request’ or ‘Offboarding request’ as a metric to build charts and graphs as per your needs. Please note that all the attributes of the following forms will be available as filters for you to create widgets based on your needs.Onboarding: Initiator and Stakeholder formsOffboarding: Initiator form
- Onboarding: Initiator and Stakeholder forms
- Offboarding: Initiator form

Check out our collection of[solution articles on reporting](https://support.freshservice.com/en/support/solutions/folders/260393/page/1?url_locale=en)to get a complete glimpse of how to create custom reports.

## Impact on Onboarding APIs

With the introduction of Onboarding reports an additional value (Request Closed = 4) for Status of Onboarding Request is being added to the API definition.

Status

Value

Awaiting Information

1

Request Cancelled

2

Request In Progress

3

Request Closed

4

Please make the required changes to your API implementation to leverage the newly added status code. Refer to[this section in the API documentation](https://api.freshservice.com/#view_onboarding_request)for more details.

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
