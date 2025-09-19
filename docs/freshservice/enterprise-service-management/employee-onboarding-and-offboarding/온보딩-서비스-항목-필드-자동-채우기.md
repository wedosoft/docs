---
sidebar_position: 7
---

# 온보딩 서비스 항목 필드 자동 채우기

<div className="subtitle">
  이 문서는 "Autofill Service Item Fields in Employee Onboarding" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

The process of employee onboarding contains a series of forms that require multiple stakeholders to input the relevant information for the new employee. This would mean that service item fields like department, location, role, etc would be repetitive across multiple child forms. The autofill feature allows the child forms with the exact field name to capture the data from the parent form and autofill for text, dropdowns, and paragraph fields.

Note: This feature is automatically enabled in your Freshservice instance.  The fields that have to be auto-filled should be added to the ‘Add fields from the initiator’s form’ field for it to work. 

Parent form filled by the initiator:

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004347852/original/2XMj4wlQWNfgIsj6BgRNDRgZtgVTe54Qrw.png?1639556256)

Child form to be filled by reporting manager with auto-populated value for the location in the form and service item field:

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004348005/original/62Wh9g8WUWZHv0_4GZU7IEyz3yDH3Cu_fQ.png?1639557366)

Child form to be filled by a new employee with auto-populated value for the location:

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004348122/original/Zf_WODerhRzaajRDNgEYvjQQd-eHAwznWg.png?1639558265)

Some of the exceptions the feature does not support:

1. All auto-fills from text, custom dropdown, and paragraph to a list-view dropdown are case-sensitive.
2. Fields such as date, number, decimal, URL, checkbox, nested field, multi-select field, and dependent field are unsupported by autofill.
3. Any field type to auto-complete dropdown* is not auto-filled.
4. Auto-complete dropdown* to custom dropdown is not auto-filled.
5. All dropdowns with input as the data source except location.

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
