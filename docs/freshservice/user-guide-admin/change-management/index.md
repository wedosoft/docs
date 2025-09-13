---
title: 변경 관리
description: Freshservice 변경 관리 프로세스 및 변경 제어 가이드
sidebar_position: 1
---

# 변경 관리

## 📋 개요

변경 관리는 변경 사항의 생명주기를 제어하는 역할을 담당합니다. 주요 목적은 IT 서비스에 대한 최소한의 중단으로 유익한 변경이 이루어질 수 있도록 하는 것입니다.

:::info ITIL 베스트 프랙티스
Freshservice의 변경 관리는 ITIL 4 프레임워크를 기반으로 설계되어, 조직의 변경 승인 프로세스와 리스크 관리를 체계적으로 지원합니다.
:::

<h2 data-identifyelement="440" dir="ltr">Change Management</h2><p data-identifyelement="441"><br></p><p data-identifyelement="443" dir="ltr">Okay, so now you've got the root cause of the incident figured out and documented. Time to bring about the change that will fix the problem, ideally, for good.&nbsp;</p><p data-identifyelement="444"><br></p><p data-identifyelement="446" dir="ltr"><strong>Change Management</strong> is responsible for controlling the lifecycle of changes. Its primary objective is to enable beneficial Changes to be made, with minimum disruption to IT Services.</p><h3 data-identifyelement="448" dir="ltr"><br></h3><h3 data-identifyelement="450" dir="ltr"><strong>Change Management in Freshservice</strong></h3><p data-identifyelement="451" dir="ltr"><br></p><p data-identifyelement="453" dir="ltr">The Changes module in Freshservice also provides custom filter options to help you view Changes<br>that match specific conditions.</p><p data-identifyelement="457" dir="ltr">&nbsp; &nbsp; &nbsp; &nbsp; ● Your Changes<br>● New and Your Open Changes<br>● Your Closed Changes<br>● Your Approved Changes<br>● Your Unapproved Changes<br>● Unassigned Changes<br>● Closed Changes<br>● Changes Awaiting Release<br>● Trash<br>● All Changes</p><p data-identifyelement="469" dir="ltr">Changes can also be sorted by the date created, last modified, priority, status and in ascending<br>or descending order.</p><p data-identifyelement="471"><br></p><p data-identifyelement="473" dir="ltr">You can select multiple Changes and perform these bulk actions:</p><ul data-identifyelement="476"><li dir="ltr"><p dir="ltr"><strong>Delete</strong> - Select the Change(s) you don't need anymore and click Delete.</p></li><li dir="ltr"><p dir="ltr"><strong>Pick Up</strong> - This option assigns the selected Change to you.</p></li><li dir="ltr"><p dir="ltr"><strong>Assign to Agent</strong> - In case you need to assign a Change to another agent, click on this option and then select the agent's name from the drop-down-menu.</p></li></ul><h3 data-identifyelement="488" dir="ltr"><strong>Information and modification options available on the Change view page</strong></h3><p><br></p><p>You could add more details or modify the existing<strong>&nbsp;c</strong>hange properties such as Priority, Impact, Risk and Change Type<strong>&nbsp;</strong>right from the ticket's detail page,&nbsp;</p><p data-identifyelement="491" dir="ltr"><br></p><p data-identifyelement="491" dir="ltr"><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000041163/original/S_UonUA8JqUiuwVqZLLehVOwnXOKBf_1Kw.png?1563939851" style="width: 713px;" class="fr-fil fr-dii fr-bordered" data-id="50000041163"></p><p data-identifyelement="491" dir="ltr"><br></p><p data-identifyelement="493" dir="ltr">Under Planning, you could fill up the following options required to fulfil the change request.</p><p data-identifyelement="496"><br></p><ul data-identifyelement="498"><li dir="ltr"><p dir="ltr">Reason for Change</p></li><li dir="ltr"><p dir="ltr">Impact</p></li><li dir="ltr"><p dir="ltr">Rollout Plan</p></li><li dir="ltr"><p dir="ltr">Backout Plan</p></li></ul><p data-identifyelement="509" dir="ltr">In case any of the details are already added, you get the option to edit them.</p><p data-identifyelement="512" dir="ltr">2. <strong>Associate</strong>- This option lets you associate the Change with a new or existing Release (Release Management aims at implementing Changes in a planned manner. We'll get to it in a bit).</p><p data-identifyelement="514" dir="ltr"><br>3. <strong>More</strong> - You can change properties like Status, Priority, Impact, Risk, Change Type, Category, Cost, Group and Agent right from the Change view page.&nbsp;</p><p data-identifyelement="517"><br></p><ul data-identifyelement="519"><li dir="ltr"><p dir="ltr">If you'd like to change the Requester, Subject line or Description, click on <strong>More</strong> and click <strong>Edit</strong>.&nbsp;</p></li><li dir="ltr"><p dir="ltr">You can also attach a CI to the problem if need be.</p></li><li dir="ltr"><p dir="ltr">To Delete or Close the Change, click on <strong>More</strong> and then click the respective option.</p></li></ul><p data-identifyelement="535" dir="ltr">4 . In case the Change requires the CAB's approval, you can request for it right from the Change view page. Click on the <strong>Request for CAB Approval</strong> option to send the request.</p><p data-identifyelement="539" dir="ltr">5. Need to track the elapsed time for the Change? Scroll all the way down and click on <strong>Time tracked → Add time</strong>, and click on <strong>Start timer</strong> to start the auto-timer. You can also specify the amount of time elapsed since the Change was created to start the timer at that point.</p><p data-identifyelement="544" dir="ltr">6. You can find options to add notes and tasks, link Incidents, Problems and CIs and view all activities performed on the Change, right below the description on the Change view page.</p><p data-identifyelement="545"><br></p><p data-identifyelement="547"><br></p><p data-identifyelement="549"><br></p>

## 🎯 한국 기업 활용 시나리오

### 시나리오 1: 금융권 시스템 변경
**회사**: 신한은행 IT본부
- **Normal Change**: 정기 패치 및 기능 개선
- **Emergency Change**: 보안 취약점 긴급 패치
- **Standard Change**: 사전 승인된 계정 생성/삭제 작업
- **CAB 승인**: 핵심 뱅킹 시스템 변경 시 리스크위원회 검토

### 시나리오 2: 제조업 시스템 업그레이드
**회사**: 삼성전자 반도체사업부
- **계획된 변경**: 생산 시스템 업그레이드 (야간/주말 작업)
- **리스크 관리**: 생산 중단 최소화를 위한 단계적 적용
- **백아웃 계획**: 문제 발생 시 즉시 원복 가능한 절차 수립

### 시나리오 3: 통신사 네트워크 확장
**회사**: SK텔레콤 네트워크운영센터
- **인프라 변경**: 5G 장비 추가 설치
- **서비스 영향**: 고객 서비스 중단 없는 변경 절차
- **모니터링**: 변경 후 성능 지표 실시간 모니터링

## 💡 변경 관리 모범사례

### 변경 유형별 처리 프로세스

#### 📋 Normal Change (일반 변경)
```markdown
1. 변경 요청서 작성
2. 영향도 및 리스크 분석
3. CAB 검토 및 승인
4. 구현 계획 수립
5. 변경 실행
6. 검증 및 완료
```

#### ⚡ Emergency Change (긴급 변경)
```markdown
1. 긴급상황 확인
2. 즉시 승인 절차
3. 신속한 구현
4. 사후 문서화
5. 사후 검토 및 개선
```

#### 🔄 Standard Change (표준 변경)
```markdown
1. 사전 승인된 절차 확인
2. 표준 템플릿 적용
3. 자동화된 실행
4. 결과 검증
5. 로그 기록
```

### CAB (Change Advisory Board) 운영

#### 🏛️ CAB 구성원
- **CAB 의장**: IT 서비스 관리자
- **기술 전문가**: 시스템 아키텍트, 보안 전문가
- **업무 담당자**: 사업부 대표, 프로세스 오너
- **외부 전문가**: 벤더, 컨설턴트 (필요시)

#### 📅 CAB 운영 주기
```
주간 정기 CAB: 일반 변경 검토
긴급 CAB: 긴급 변경 시 즉시 소집
월간 CAB 리뷰: 변경 성과 및 개선사항 검토
```

## 🔍 변경 관리 프로세스 세부사항

### 1단계: 변경 요청 및 기록
- **RFC (Request for Change)** 작성
- 변경 이유 및 목적 명시
- 영향 범위 및 리스크 분석
- 구현 일정 및 리소스 계획

### 2단계: 변경 평가 및 승인
- **영향도 분석**: 비즈니스, 기술, 보안 측면
- **리스크 평가**: 장애 가능성 및 대응 방안
- **CAB 검토**: 다각도 검토 및 승인 결정
- **우선순위 결정**: 비즈니스 임팩트 기반

### 3단계: 변경 구현 및 검증
- **구현 전 체크리스트** 확인
- **단계별 실행**: 롤아웃 계획에 따른 순차 진행
- **실시간 모니터링**: 시스템 상태 및 성능 확인
- **백아웃 준비**: 문제 발생 시 즉시 원복 가능

### 4단계: 변경 완료 및 사후관리
- **변경 결과 검증**: 목표 달성 여부 확인
- **사용자 피드백**: 서비스 품질 만족도 조사
- **문서화**: 변경 과정 및 결과 기록
- **교훈 학습**: 개선사항 도출 및 적용

## 📊 변경 성과 측정 지표

### 핵심 KPI
- **변경 성공률**: 95% 이상 목표
- **계획 준수율**: 일정 및 예산 준수 정도
- **장애 발생률**: 변경으로 인한 인시던트 비율
- **고객 만족도**: 변경 후 서비스 만족도

### 모니터링 대시보드
```markdown
실시간 변경 현황:
✅ 진행 중인 변경: 15건
🕒 승인 대기: 8건
✅ 완료된 변경: 127건
⚠️ 실패한 변경: 2건
```

## 🛠️ 변경 관리 도구 활용

### Freshservice 고급 기능
- **변경 템플릿**: 표준 변경을 위한 사전 정의된 양식
- **승인 워크플로**: 자동화된 다단계 승인 프로세스
- **변경 캘린더**: 전체 변경 일정을 한눈에 확인
- **충돌 감지**: 동시 변경으로 인한 리스크 사전 감지

### 통합 연동
- **CMDB 연동**: 변경 대상 CI의 종속성 자동 확인
- **모니터링 연동**: 변경 후 시스템 상태 자동 수집
- **알림 시스템**: 변경 진행 상황 실시간 알림
- **보고서 자동화**: 변경 성과 리포트 자동 생성

이러한 체계적인 변경 관리를 통해 한국 기업들은 디지털 전환 과정에서 안정적인 IT 서비스를 유지하면서도 혁신을 지속할 수 있습니다.

## 🎯 한국 기업 활용 시나리오

### 시나리오 1: 금융권 시스템 변경
**회사**: 신한은행 IT본부
- **Normal Change**: 정기 패치 및 기능 개선
- **Emergency Change**: 보안 취약점 긴급 패치
- **Standard Change**: 사전 승인된 계정 생성/삭제 작업
- **CAB 승인**: 핵심 뱅킹 시스템 변경 시 리스크위원회 검토

### 시나리오 2: 제조업 시스템 업그레이드
**회사**: 삼성전자 반도체사업부
- **계획된 변경**: 생산 시스템 업그레이드 (야간/주말 작업)
- **리스크 관리**: 생산 중단 최소화를 위한 단계적 적용
- **백아웃 계획**: 문제 발생 시 즉시 원복 가능한 절차 수립

### 시나리오 3: 통신사 네트워크 확장
**회사**: SK텔레콤 네트워크운영센터
- **인프라 변경**: 5G 장비 추가 설치
- **서비스 영향**: 고객 서비스 중단 없는 변경 절차
- **모니터링**: 변경 후 성능 지표 실시간 모니터링

## 💡 변경 관리 모범사례

### 변경 유형별 처리 프로세스

#### 📋 Normal Change (일반 변경)
```markdown
1. 변경 요청서 작성
2. 영향도 및 리스크 분석
3. CAB 검토 및 승인
4. 구현 계획 수립
5. 변경 실행
6. 검증 및 완료
```

#### ⚡ Emergency Change (긴급 변경)
```markdown
1. 긴급 상황 확인
2. 간소화된 승인 절차
3. 즉시 구현
4. 사후 CAB 보고
5. 문서화 완료
```

#### ✅ Standard Change (표준 변경)
```markdown
1. 사전 승인된 절차 확인
2. 체크리스트 기반 실행
3. 자동화된 검증
4. 완료 보고
```

### 변경 계획 수립 가이드
```markdown
필수 포함 항목:
✅ 변경 사유 (Reason for Change)
✅ 영향 분석 (Impact Analysis)
✅ 구현 계획 (Rollout Plan)
✅ 백아웃 계획 (Backout Plan)
✅ 테스트 시나리오
✅ 의사소통 계획
```

## ⚠️ 리스크 관리

:::warning 주요 위험 요소
- **서비스 중단**: 비즈니스 운영에 미치는 영향 최소화
- **데이터 손실**: 백업 및 복구 계획 필수
- **보안 취약점**: 변경으로 인한 새로운 보안 위험 검토
- **성능 저하**: 변경 후 시스템 성능 모니터링
:::

### 리스크 평가 매트릭스

| 영향도 \ 확률 | 낮음 | 중간 | 높음 |
|---------------|------|------|------|
| **높음** | 중간 | 높음 | 매우높음 |
| **중간** | 낮음 | 중간 | 높음 |
| **낮음** | 매우낮음 | 낮음 | 중간 |

## 📊 변경 관리 지표

| KPI | 목표 수치 | 설명 |
|-----|-----------|------|
| **Change Success Rate** | > 95% | 성공한 변경 / 전체 변경 |
| **Emergency Change Ratio** | < 10% | 긴급 변경 / 전체 변경 |
| **Change Lead Time** | < 14일 | 요청부터 구현까지 소요시간 |
| **Failed Change Recovery** | < 4시간 | 실패한 변경의 복구 시간 |

## 🔄 CAB (Change Advisory Board) 운영

### CAB 구성원
```markdown
필수 구성원:
- Change Manager (의장)
- 기술 전문가 (시스템별)
- 비즈니스 대표
- 보안 담당자
- 운영 담당자

선택 구성원:
- 외부 업체 담당자
- 법무팀 (규제 관련)
- 품질보증팀
```

### 승인 기준
```markdown
고려사항:
✅ 비즈니스 가치
✅ 기술적 위험도
✅ 자원 가용성
✅ 다른 변경과의 충돌
✅ 규정 준수 여부
```

## 🔗 관련 문서

- [Problem Management](../problem-management/)
- [Release Management](../release-management/)
- [Incident Management](../incident-management/)
- [User Management](../admin-settings/user-management)