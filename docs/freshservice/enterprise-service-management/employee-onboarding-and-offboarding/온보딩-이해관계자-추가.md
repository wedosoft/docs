---
sidebar_position: 3
---

# 온보딩 이해관계자 추가

<div className="subtitle">
  이 문서는 "Adding Stakeholders to the Onboarding Module" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 기능 개요

In your organisation, there might be multiple stakeholders involved in your onboarding process. The first step in setting up your onboarding process is adding your key stakeholders to the onboarding module. In Freshservice's Onboarding Module you can add your stakeholders in the following hierarchy.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001296481/original/a2w52is0TEkX18RzT8PtjHUFQuiV3yQuTA.png?1592504762)

Who is an Initiator?

An initiator initiates the onboarding process in your organization and can raise onboarding requests from the end-user portal. To facilitate the flow of approvals and information, the stakeholders can be added in the following hierarchy.

Note:You can add only 3 stakeholders in the onboarding process including the initiator.

To add an Initiator,

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284356/original/DoVS_oLxljVaQFBXqtbirCi-odu23uPOOw.gif?1592396207)

- Click onAdd Stakeholder.Enter the Stakeholder’s role or the team’s name.
- Next, map the Freshservice agent/ requester groups with the Stakeholders Role. For example, if the stakeholder is the HR Manager, you can associate with Freshservice agent or requester groups in which HR Managers belong.
- Next set up the form that you would want your initiator to fill to kick start the onboarding process for a hire. You can drag and drop the required fields to set it up.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284350/original/aNFe07_QLzyAsflzuJ7oSBJxcIdd1PQWtw.png?1592396191)

- Click onSave and Continueto add more stakeholders.

To add Subsequent Stakeholders,

- Click onAdd stakeholder.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284349/original/sJWu2WN-VMeHpq84Nt1yUOjoaK8K57RrbA.png?1592396191)

- You’ll be redirected to theAdd Stakeholderpage where you can add your next stakeholder and associate the Freshservice agent groups.
- Next, set up the form you would want your stakeholder to fill and email that has to be sent out for their approvals/information.

Routing the Right Context to Stakeholders

- When you add stakeholders, keep in mind these two simple steps to route the right context.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001296486/original/ao3Sa-AUFt0WwMx6uMQt7pfOw36KabxD3A.png?1592504791)

- Email Field in Initiator’s form:When the initiator raises an onboarding request, they will need an email field to forward the request to the next stakeholder in the onboarding process. To enable this, whenever subsequent stakeholders are added after the initiator, an email ID field for the added stakeholder is automatically added to the initiator’s form

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284353/original/gyiZuYwNEX8BHW9tnSSNUJ28t8k329bp3g.png?1592396192)

For example, let’s say the second stakeholder is the reporting manager. When you add this stakeholder, the HR Manager’s form will be updated with a field “Reporting Manager’s Email” to enable the HR Manager to route the request to the right person.

Note: You can define this email field to be a text field or a drop-down field. You can use a text field if the stakeholder you’re addressing is not a user in Freshservice. If they are a Freshservice user, you can enable a drop-down populated with emails from the Freshservice User Database.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284352/original/8RP6ASPtRN1pRkc61A_HpX1EMaMIoqI0tQ.png?1592396192)

- Adding Fields from the Initiator’s form:Once the HR Manager routes the onboarding request, the reporting manager needs to know which hire this request is about. To facilitate this, you can add fields from the initiator’s form which would add more context about the hire to this stakeholder. For example, you can add fields like Hire’s name and Department from the initiator’s form.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284351/original/h5skHCPKq9-kIchsAuB71t-P6LwxDRaHaw.png?1592396192)

- Click onSave and Continue.
- Define anemail templatethat has to be sent by Freshservice to the stakeholder you’re adding.
- Click onSave and Continueto add more stakeholders.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001284354/original/Ke8scxOCfeyy-AOosrjiw6hmDMIbi-R1Fg.png?1592396192)

Now that you're done with Step 1, go on and find out how to[Build Onboarding Kits](https://support.freshservice.com/en/support/solutions/articles/50000002364)in Step 2.

Faq's:

1. The onboarding button is not visible on our customer portal for any users who are listed as stakeholders,

how to initiate an employee onboarding request from the self-service portal?

Kindly navigate to theGlobal Settings / Admin > Employee Onboarding >UnderStakeholdersselect the initiator and see if the respective user group is added under "Which groups does the HR Manager belong to?".

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011882217/original/-lnPYb4VrNmuXHW0FvPJ46hD9ysd7-Fw4A.png?1716197754)

2. I have added a field to a stakeholder in employee onboarding but cannot add it to a ticket.

Go toGlobal Settings / Admin > Employee Onboarding >UnderCreate Ticketsselect the respective ticket > Click on thepencil icon >Click on theAdd Fieldsto add the stakeholder fields.

3.How to customize the onboarding notification that is sent to the reporting manager and other stakeholders?

Go toAdmin > Employee Onboarding > Add Stakeholder. Choose the appropriate stakeholder, and all the fields will be visible. ClickContinueto edit the employee onboarding email notification.

4. How do I add a checklist or checkbox to the parent ticket for onboarding?

InGlobal Settings/Admin, navigate toEmployee Onboarding > Add Stakeholder.Any form field added to the initiator form can be included in the parent ticket. Add the checkbox field in the initiator form andfrom the 'Create ticket' sectionadd it to the parent ticket.

![기능 스크린샷](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012343064/original/0XNjVWcTN8AUjTarBvrIp95nh0Me1chXqg.png?1719997319)

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
