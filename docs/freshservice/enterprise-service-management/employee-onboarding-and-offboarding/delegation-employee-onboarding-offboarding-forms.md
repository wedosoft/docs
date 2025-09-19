---
sidebar_position: 13
---

# 온보딩/오프보딩 양식 위임

Freshservice의 온보딩/오프보딩 양식 위임을 통해 효율적인 직원 라이프사이클 관리를 구현할 수 있습니다.

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
<p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-size: 14px; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}>Freshservice allows&nbsp;</span><span style={{font-size: 14px;}}><span style={{font-family: Helvetica,sans-serif;}}><a href="https://support.freshservice.com/en/support/solutions/articles/50000002363"><span style={{color: rgb(17, 85, 204); font-weight: 400; text-decoration-skip-ink: none;}}>stakeholders involved in employee onboarding and offboarding</span></a><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;workflows to delegate the filling of forms that are assigned to them. This functionality is useful if the stakeholders are out of office or on leave and do not want the onboarding or offboarding requests to be stuck because of their absence.&nbsp;</span></span></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p class="fd-toc" style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><strong>TABLE OF CONTENTS</strong></span></p><ul style={{font-family: Helvetica, sans-serif;}}><li><span style={{font-family: Helvetica,sans-serif;}}><a href="#How-can-you-enable-onboarding/offboarding-forms-delegation?"><span style={{font-size: 14px;}}>How can you enable delegation of onboarding/offboarding forms?</span></a></span></li><li><span style={{font-size: 14px;}}><span style={{font-family: Helvetica,sans-serif;}}><a href="#How-does-onboarding/offboarding-form-delegation-work?">How does onboarding/offboarding form delegation work?</a></span></span></li></ul><p style={{font-family: Helvetica, sans-serif;}}><br></p><pre class="fd-callout fd-callout--note"><span style={{font-size: 14px; font-family: Helvetica, sans-serif;}}><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>NOTE: Please note that the&nbsp;</span><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>form assigned to the initiator can NOT be delegated</span><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>. This functionality is available only for the ‘Stakeholder’ as defined in the following articles.</span>
```
```html
<span style={{color: rgb(0, 0, 0); font-weight: 400;}}><a href="https://support.freshservice.com/en/support/solutions/articles/50000002363">Stakeholders in Onboarding</a></span>
```
```html
</span><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}><a href="https://support.freshservice.com/en/support/solutions/articles/50000006198-employee-offboarding"><span style={{font-family: Helvetica,sans-serif;}}>Stakeholders in Offboarding</span></a></span></pre><div align="left" style={{margin-left: 0pt; font-family: Helvetica, sans-serif;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><a href="https://support.freshservice.com/en/support/solutions/articles/50000002363"></a></span></p><br></div><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>There are two personas involved in the delegation process.</span></span></p><p style={{font-family: Helvetica, sans-serif; font-size: 14px;}}><span style={{font-size: 14px;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif; font-size: 14px;}}><span style={{font-size: 14px;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>Delegator:</span><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;The user who turns delegation ON so that incoming approvals and forms can be routed to someone else in the team. This user can be a requester or an agent.</span></span></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px;}}><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>Delegatee</span></span><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>: The user to whom the delegator’s requests are routed while delegation is ON. This user can be a requester or an agent.</span></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><h2 id="How-can-you-enable-onboarding/offboarding-forms-delegation?" style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 13pt; color: rgb(0, 0, 0); font-weight: 700;}}>How can you enable delegation of onboarding/offboarding forms?</span></span></h2><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>Delegation can be performed by any requester/agent. Here are the steps.&nbsp;</span></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 14px; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt; font-size: 14px;}}><span style={{font-size: 14px;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>Click on&nbsp;</span><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>Profile Settings&nbsp;</span><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>by clicking on your profile icon on the top right corner of the screen.&nbsp;</span></span></span></p></li><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>Go to your user profile, and go to “Delegation Settings” on the right side of the screen.</span><span style={{font-size: 11pt; color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;</span></span></p></li></ul><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}><br></span></span></p><pre class="fd-callout fd-callout--note" ><span style={{color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; font-family: Helvetica, sans-serif; display: inline !important; font-size: 14px;}}>NOTE: Please note that the option to delegate onboarding and offboarding forms will be shown only if employee onboarding and offboarding functionalities are enabled in your accounts</span></pre><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>Enter the required details in the</span><span style={{font-size: 14px;}}><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>&nbsp;Delegation Settings</span><span style={{color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;modal that opens up. Select the delegatee and enter the date and time range for which you want the delegation to happen. Click on the&nbsp;</span><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>Delegate</span></span><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;button.</span></span></p></li></ul><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 11pt; color: rgb(0, 0, 0); font-weight: 400;}}><span style={{border:none;display:inline-block;overflow:hidden;width:624px;height:391px;}}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346105/original/BZVYS14KFlcktT6cVSXiSLo5ixqTUH_6BQ.png?1702285996" width="624" height="391" ></span></span></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>The active delegation settings will now show in the right panel of your profile page. The delegation will be active during the date and time range mentioned by you. You can also manually turn off the delegation in the interim period by clicking on the&nbsp;</span><span style={{font-size: 14px;}}><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>Turn off Delegation</span></span><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;button.</span></span></p></li></ul><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 11pt; color: rgb(0, 0, 0); font-weight: 400;}}><span style={{border:none;display:inline-block;overflow:hidden;width:624px;height:351px;}}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346106/original/qYl6h0JiAl1A0Br9YOccqlSVlOMfblmOMQ.png?1702285997" width="624" height="351" ></span></span></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><h2 id="How-does-onboarding/offboarding-form-delegation-work?" style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 13pt; color: rgb(0, 0, 0); font-weight: 700;}}>How does onboarding/offboarding form delegation work?</span></span></h2><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>Once delegation has been activated, every onboarding/offboarding form-filling request that the delegator receives is automatically delegated to the delegatee. &nbsp;The delegator and delegatee both receive email notifications upon the creation of an onboarding/offboarding request. &nbsp;This is to ensure that the required information is filled in a timely manner.&nbsp;</span></span></p></li></ul><p style={{line-height: 1.38; margin-bottom: 0pt;}}><br></p><pre class="fd-callout fd-callout--note" ><span style={{font-size: 14px; font-family: Helvetica, sans-serif;}}>NOTE:&nbsp;</span><span style={{color: rgb(0, 0, 0); font-family: Helvetica, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; float: none; display: inline !important;}}>Requests created only after the activation of delegation are forwarded to the delegatee. Any pending requests with the delegator before the activation of the delegation are not forwarded.</span></pre><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>The delegatee will receive a system-generated email requesting to fill out the form. Below is a sample email for employee onboarding.</span></span></p></li></ul><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 11pt; color: rgb(0, 0, 0); font-weight: 400;}}><span style={{border:none;display:inline-block;overflow:hidden;width:624px;height:341px;}}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346103/original/J9rsBS03e7ifg2oWV7tCTuXygAnBLrTN4A.png?1702285995" width="624" height="341" ></span></span></span></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><pre class="fd-callout fd-callout--note" ><span style={{font-size: 14px; font-family: Helvetica, sans-serif;}}>NOTE:&nbsp;</span><span style={{color: rgb(0, 0, 0); font-family: Helvetica, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal;  text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;}}>Please note that it is not possible to modify the content of this email. However, the subject of the email is picked up from the subject field defined in the onboarding/offboarding module settings. This is the Subject that was set for the email to be sent to the original recipient of the form request. It is recommended to use the new hire/employee’s name in the subject to provide clear context of the request to the delegatee.</span>
```

```html
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346298/original/eMOBvrUVwti1dbmhOqvYcWyDL2MEArAxyw.png?1702287191" width="610" height="339" style={{box-sizing: border-box; border: 0px; vertical-align: bottom; max-width: calc(100% - 10px); position: relative; cursor: pointer; padding: 0px 1px; display: inline-block; float: none; margin-left: 5px; margin-right: 5px; color: rgb(0, 0, 0); font-family: Helvetica, sans-serif; font-size: 14.6667px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal;  text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;}} ></pre><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><ul style={{margin-bottom: 0px; padding-inline-start: 48px; font-family: Helvetica, sans-serif;}}><li style={{list-style-type: disc; font-size: 11pt; font-family: Helvetica, sans-serif; color: rgb(0, 0, 0); font-weight: 400;}}><p style={{line-height: 1.38; margin-bottom: 0pt;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>By clicking on the&nbsp;</span><span style={{font-size: 14px;}}><span style={{color: rgb(0, 0, 0); font-weight: 700;}}>form</span></span><span style={{font-size: 14px; color: rgb(0, 0, 0); font-weight: 400;}}>&nbsp;link in the email, the delegate will be taken to the form where they can fill in the required information for the request.&nbsp;</span></span></p></li></ul><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p style={{line-height: 1.38; margin-bottom: 0pt; font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><span style={{font-size: 11pt; color: rgb(0, 0, 0); font-weight: 400;}}><span style={{border:none;display:inline-block;overflow:hidden;width:624px;height:341px;}}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010346104/original/EqG--PFu_Vhxj8W8roFd4ERxov2kLnEggg.png?1702285995" width="624" height="341" ></span></span></span></p><p style={{font-family: Helvetica, sans-serif;}}><br></p><p style={{font-family: Helvetica, sans-serif;}}><br></p><pre class="fd-callout fd-callout--note" style={{box-sizing: border-box; overflow: visible; font-family: monospace, monospace; font-size: 13px; white-space: pre-wrap; overflow-wrap: break-word;  padding: 12px 16px; display: block; cursor: pointer; word-break: normal; margin: 0px; border-width: 1px 1px 1px 6px; border-style: solid; border-color: rgb(235, 237, 240) rgb(235, 237, 240) rgb(235, 237, 240) rgb(232, 111, 37); border-image: initial; border-radius: 8px 4px 4px 8px; color: rgb(0, 0, 0); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;}}><span style={{font-size: 14px; font-family: Helvetica, sans-serif;}}>NOTE: As long as delegation is active, the delegatee will be able to view the submitted details by clicking on the link in the email. After the expiration of the delegation, the submitted details will not be accessible to the delegatee. The delegator will be able to view the details submitted by the delegatee at all times.</span>
```
```html
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50010362615/original/DXE1JL6QTSbS8Gep1i5RVlUwQHL9jOr3-A.png?1702384852" style={{width: auto;}} ></pre><p><br></p><p style={{font-family: Helvetica, sans-serif;}}><span style={{font-family: Helvetica,sans-serif;}}><br></span></p><p><br></p>
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
