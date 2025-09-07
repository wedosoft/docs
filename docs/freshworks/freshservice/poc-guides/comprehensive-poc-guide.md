---
sidebar_position: 1
---

# Freshservice PoC 가이드

이 가이드는 Freshservice의 핵심 기능을 체계적으로 검증하고, IT 운영 효율성을 극대화할 수 있는 방법을 확인하기 위한 3주간의 PoC 진행 가이드입니다.

:::info PoC 진행 개요
이 가이드는 3주간의 체계적인 Freshservice PoC 진행을 위한 단계별 로드맵을 제공합니다. 각 주차별로 핵심 기능을 순차적으로 체험하며 실무 적용 가능성을 검증할 수 있습니다.
:::

## PoC 진행 로드맵

| 주차 | 핵심 영역 | 주요 활동 |
|------|-----------|-----------|
| **1주차** | 서비스 데스크 설정 | 유저/에이전트 포털, 티켓 필드 설정 |
| **2주차** | 핵심 연동 설정 | AD 연동, ITAM(자산관리) 구성 |
| **3주차** | 심화 기능 및 데이터 관리 | 워크플로 자동화, ITIL, KPI 분석, 보안 |

## 1주차: 서비스 데스크 설정

### 목표
서비스 데스크의 기본 환경을 구성하고 엔드 유저와 에이전트 모두가 Freshservice에 쉽게 적응할 수 있도록 포털 설정을 완료합니다.

:::warning 1주차 핵심 포인트
포털 디자인, 티켓 템플릿, 에이전트 권한 설정 등을 꼼꼼히 확인하여 사용자 경험을 최적화하세요.
:::

### 1. 유저 포털 서비스 데스크 설정

엔드 유저가 직접 사용하는 서비스 데스크 포털의 기본 설정을 구성합니다.

#### 주요 설정 항목

**유저 서비스 요청 플로우**
- 엔드 유저의 서비스 요청 전체 과정 이해
- [서비스 요청 프로세스 문서](https://support.freshservice.com/support/solutions/articles/234484-raising-a-service-request)

**서비스 브랜드 포털 설정**
- 포털 로고, 색상, 레이아웃 사용자 정의
- [서비스 데스크 기본 설정](https://support.freshservice.com/support/solutions/articles/224440-service-desk-basics)
- [No-code 포털 구축](https://support.freshservice.com/support/solutions/articles/50000005515-build-portals-on-the-fly-the-no-code-way)

**고객 문의 템플릿 설정**
- 자주 발생하는 문의 유형별 티켓 템플릿 생성
- [티켓 템플릿 생성 가이드](https://support.freshservice.com/support/solutions/articles/229834-creating-ticket-and-change-template)

**요청자 정보 관리**
- 요청자 프로필 관리 및 티켓 이력 추적 설정
- [사용자 관리 문서](https://support.freshservice.com/support/solutions/articles/233754-user-management)

**서비스 카탈로그 설정**
- 자주 요청되는 서비스/물품 카탈로그 구성
- [서비스 카탈로그 설정](https://support.freshservice.com/support/solutions/articles/199643-configure-the-service-catalog)

### 2. 에이전트 포털 서비스 데스크 설정

상담원이 티켓을 관리하고 ITIL 프로세스를 실행하는 에이전트 포털을 설정합니다.

#### 에이전트 포털 구성

**포털 둘러보기**
- 에이전트 포털의 주요 기능과 레이아웃 이해
- [에이전트 시작 가이드](https://support.freshservice.com/support/solutions/161457-getting-started-with-freshservice-for-agents)

**티켓 응답 관리**
- 티켓 답변 추가, 파일 첨부, 상태 변경 프로세스
- [티켓 응답 가이드](https://support.freshservice.com/support/solutions/articles/234443-replying-to-tickets)

**작업 할당 시스템**
- 티켓을 담당자/팀에 할당하고 마감일 설정
- [작업 추가](https://support.freshservice.com/support/solutions/articles/234439-adding-tasks)
- [작업 관리 뷰](https://support.freshservice.com/support/solutions/articles/50000007401-optimized-task-management-with-enhanced-task-list-view)

**권한 및 그룹 관리**
- 에이전트 역할과 권한 정의, 담당 부서 설정
- [에이전트 역할 설정](https://support.freshservice.com/support/solutions/articles/154760-setting-agent-roles-and-permissions)
- [에이전트 그룹 관리](https://support.freshservice.com/support/solutions/articles/50000005578-managing-agent-groups)

**승인 절차 설정**
- 특정 요청에 대한 승인 워크플로 자동화
- [승인 그룹 및 체인](https://support.freshservice.com/support/solutions/articles/50000010315-introducing-groups-and-chains-in-approvals-intervention-required)
- [승인 할당 방법](https://support.freshservice.com/support/solutions/articles/50000011144-how-to-create-and-assign-approvals-in-freshservice-)
- [서비스 요청 승인 자동화](https://support.freshservice.com/support/solutions/articles/191018-service-request-approvals-requesting-an-approval-manually-automate-and-approving-a-service-request)

### 3. 티켓 필드 설정

고객 문의가 티켓 형태로 효율적으로 관리될 수 있도록 필드를 구성합니다.

#### 티켓 구성 요소

**기본 티켓 필드**
- 기본 및 사용자 정의 필드 정의
- [티켓 속성 관리](https://support.freshservice.com/support/solutions/articles/155559-managing-ticket-properties)
- [티켓 뷰 이해](https://support.freshservice.com/support/solutions/articles/50000000126-understanding-ticket-views)
- [티켓 필터링](https://support.freshservice.com/support/solutions/articles/50000009636-enhancements-to-ticket-list-view)

**티켓 템플릿**
- 특정 유형 티켓의 필드 미리 설정으로 반복 작업 감소
- [폼 필드 설정](https://support.freshservice.com/support/solutions/articles/156449-setting-up-form-fields-for-tickets-problems-changes-and-releases)

**양식 사용자 정의**
- 티켓 제출 양식 커스터마이징으로 효율적 정보 수집
- [동적 섹션 활용](https://support.freshservice.com/support/solutions/articles/226005-using-dynamic-sections-in-ticket-forms)

**티켓 고급 기능**
- 티켓 연결, 하위 티켓 등 고급 관리 기능
- [티켓 연결](https://support.freshservice.com/support/solutions/articles/50000005640-why-can-i-not-link-a-child-ticket-to-a-parent-ticket-in-freshservice-)
- [하위 티켓 추가](https://support.freshservice.com/support/solutions/articles/50000009857-adding-child-tickets-to-a-ticket-in-freshservice)

---

## 2주차: 핵심 연동 설정

### 목표
Freshservice의 핵심 자동화 기능을 연동하여 사용자 정보 동기화와 자산 정보 자동 관리를 구현합니다.

:::warning 2주차 핵심 포인트
Active Directory 연동과 ITAM 기능을 활용해 자동화된 IT 자산 관리 체계를 구축하세요. 이 단계에서 Freshservice의 진정한 효율성을 경험할 수 있습니다.
:::

### 1. AD 연동 설정

Active Directory와 Freshservice를 연동하여 사용자 정보를 자동으로 동기화하고 프로비저닝합니다.

#### AD 통합 프로세스

**AD 동기화 에이전트 설치**
- AD와의 동기화를 위한 에이전트 설치 및 구성
- [Azure 통합 가이드](https://support.freshservice.com/support/solutions/articles/50000003289-integrating-with-azure-)

**클라우드 디스커버리**
- AD에서 Freshservice로 사용자 자동 가져오기
- [Azure 클라우드 디스커버리](https://support.freshservice.com/support/solutions/articles/50000003721-freshservice-cloud-discovery-azure-cloud)

**SSO 활성화**
- AD 사용자를 위한 Single Sign-On 설정
- [Azure AD SSO 설정](https://support.freshservice.com/support/solutions/articles/203501-setting-up-microsoft-azure-ad-single-sign-on-in-freshservice)

**LDAP 연동**
- LDAP을 통한 사용자 정보 동기화
- [SSO 마이그레이션](https://support.freshservice.com/support/solutions/articles/50000003339-migrating-freshservice-sso-to-freshworks-organization)

**그룹 및 사용자 매핑**
- Freshservice와 AD 간 사용자 및 그룹 정보 매핑
- [에이전트 그룹 관리](https://support.freshservice.com/support/solutions/articles/50000005578-managing-agent-groups)

**오케스트레이션 기능**
- AD에서 사용자 생성, 비활성화 등 고급 자동화
- [Azure AD 온보딩 사례](https://support.freshservice.com/support/solutions/articles/50000003329-sample-use-case-for-azure-ad-orchestration-app-employee-onboarding)

### 2. ITAM 연동

IT 자산 자동 발견(Discovery) 설정을 통해 조직 내 모든 하드웨어 및 소프트웨어 자산을 자동으로 수집하고 관리합니다.

#### 자산 디스커버리

**자산 관리 개념**
- Freshservice에서 자산의 의미와 관리 방법 이해
- [Basic vs Advanced ITAM](https://support.freshservice.com/support/solutions/articles/50000010385-what-are-the-impacts-of-switching-from-basic-itam-to-advanced-itam-on-freshservice-)

**Discovery Probe 설치**
- Probe를 통한 자산 정보 자동 수집
- [Discovery Probe 가이드](https://support.freshservice.com/support/solutions/articles/158679-freshservice-discovery-probe)

**Discovery Agent 방식**
- Agent 기반 자산 정보 수집
- [Discovery Agent 문서](https://support.freshservice.com/support/solutions/articles/200393-freshservice-discovery-agent)

#### 자산 관리 및 활용

**자산 정보 관리**
- Freshservice에 등록된 자산의 정보와 이력 확인
- [자산 할당 이력](https://support.freshservice.com/support/solutions/articles/50000009774-asset-assignment-history)

**티켓과 자산 연결**
- 인시던트 및 서비스 요청 티켓에 자산 연결
- [자산-인시던트 연결](https://support.freshservice.com/support/solutions/articles/234440-associating-assets-to-incidents)

**CMDB 설정**
- 구성 관리 데이터베이스를 통한 자산 관계 시각화
- [CMDB 소개](https://support.freshservice.com/support/solutions/articles/233758-introduction-to-configuration-management-database-cmdb-)

**자산 보고서 및 대시보드**
- 자산 데이터 기반 보고서 생성 및 대시보드 구성
- [자산 활동 보고](https://support.freshservice.com/support/solutions/articles/50000010140-asset-activity-reporting)

---

## 3주차: 심화 기능 및 데이터 관리

### 목표
Freshservice의 고급 기능을 체험하며 운영 효율을 극대화하는 방법을 익힙니다. 워크플로 자동화, ITIL 기반 프로세스, 데이터 분석을 통해 전략적 IT 관리를 구현합니다.

:::warning 3주차 핵심 포인트
고급 자동화 기능과 ITIL 프로세스를 통해 복잡한 IT 환경을 체계적으로 관리하고 데이터 기반의 전략적 의사결정을 내릴 수 있습니다.
:::

### 1. 워크플로 자동화

반복적인 IT 업무 프로세스를 자동화하여 운영 효율성을 극대화합니다.

#### 자동화 구성 요소

**티켓 자동화 규칙**
- 티켓 상태 변경, 알림 전송 등 자동화 규칙 설정
- [자동 할당 시스템](https://support.freshservice.com/support/solutions/articles/157134-auto-assigning-tickets-to-agents-in-a-group-round-robin-)

**자동 분류 및 라우팅**
- 조건에 따른 티켓 자동 분류 및 담당 부서 할당
- [라운드 로빈 할당](https://support.freshservice.com/support/solutions/articles/157134-auto-assigning-tickets-to-agents-in-a-group-round-robin-)

**서비스 요청 워크플로**
- 복잡한 서비스 요청 워크플로 설계 및 구현
- [서비스 요청 승인](https://support.freshservice.com/support/solutions/articles/191018-service-request-approvals-requesting-an-approval-manually-automate-and-approving-a-service-request)

**승인 프로세스 자동화**
- 특정 요청에 대한 승인 워크플로 자동화
- [승인 그룹 및 체인](https://support.freshservice.com/support/solutions/articles/50000010315-introducing-groups-and-chains-in-approvals-intervention-required)

#### 고급 자동화 기능

**온보딩 프로세스**
- 자동화된 직원 온보딩 템플릿 및 워크플로
- [온보딩 템플릿](https://support.freshservice.com/support/solutions/articles/50000011383-create-a-journey-using-a-template)
- [온보딩 요청](https://support.freshservice.com/support/solutions/articles/50000011377-initiate-a-journey-request-from-the-support-portal)

**커스텀 오브젝트**
- 자동화 워크플로 내 커스텀 데이터 및 비즈니스 로직 활용
- [M365 라이선스 할당](https://support.freshservice.com/support/solutions/articles/50000003387-sample-use-case-for-azure-ad-orchestration-app-m365-license-assignment-during-onboarding)

**외부 시스템 연동**
- AD, Teams 등 외부 시스템과의 자동화 워크플로 확장
- [Azure AD 온보딩 사례](https://support.freshservice.com/support/solutions/articles/50000003329-sample-use-case-for-azure-ad-orchestration-app-employee-onboarding)

### 2. ITIL 기반 프로세스 관리

ITILv3 프레임워크를 따른 체계적인 서비스 관리를 구현합니다.

#### 핵심 ITIL 프로세스

**인시던트 관리**
- 인시던트 기록, 관리 및 해결 프로세스
- [인시던트 관리](https://support.freshservice.com/support/solutions/articles/232991-incident-management)
- [주요 인시던트 관리](https://support.freshservice.com/support/solutions/articles/50000006167-working-with-major-incidents-in-freshservice)
- [인시던트-변경관리 연결](https://support.freshservice.com/support/solutions/articles/50000000038-linking-incidents-to-existing-or-new-changes)

**문제 관리**
- 반복 인시던트의 근본 원인 파악 및 해결
- [문제 관리 프로세스](https://support.freshservice.com/support/solutions/articles/233755-problem-management)

**변경 관리**
- IT 환경 변경사항의 체계적 관리
- [변경 관리](https://support.freshservice.com/support/solutions/articles/233756-change-management)
- [CAB 구성 및 관리](https://support.freshservice.com/support/solutions/articles/155582-understanding-change-approvals-and-cabs)
- [변경 라이프사이클](https://support.freshservice.com/support/solutions/articles/236100-manage-your-change-processes-with-change-lifecycle)

**릴리즈 관리**
- IT 서비스 릴리즈 계획 및 관리
- [릴리즈 관리](https://support.freshservice.com/support/solutions/articles/234458-working-with-releases)

**DevOps 통합**
- DevOps 파이프라인과 통합된 서비스 관리 자동화
- [DevOps 변경관리](https://support.freshservice.com/support/solutions/articles/50000010034-change-management-for-devops-enhancing-governance-and-compliance)

### 3. 성과 지표(KPI) 분석

PoC 데이터를 기반으로 맞춤형 리포트와 대시보드를 구성하여 IT 서비스의 핵심 성과 지표를 측정합니다.

#### 분석 및 보고 시스템

**기본 리포트 활용**
- 기본 제공 리포트를 통한 성과 분석
- [공통 리포트](https://support.freshservice.com/support/solutions/articles/50000003515-common-reports-using-analytics)
- [리포트 공유](https://support.freshservice.com/support/solutions/articles/50000005508-report-sharing-in-freshservice-analytics)

**맞춤형 대시보드**
- 핵심 지표 중심의 맞춤형 대시보드 구성
- [팀 대시보드](https://support.freshservice.com/support/solutions/articles/50000003682-team-dashboard-is-now-more-inclusive)
- [분석 기능 개선](https://support.freshservice.com/support/solutions/articles/50000004791-what-s-changing-in-analytics-)

**KPI 설정 및 추적**
- 핵심 성과 지표 정의 및 주기적 추적
- [팀 정렬 개선](https://support.freshservice.com/support/solutions/articles/50000002980-improve-team-alignment-with-team-dashboards)

### 4. 보안 및 연동

Freshservice의 보안 기능과 외부 시스템 연동을 통해 안전하고 효율적인 IT 환경을 구축합니다.

#### 보안 관리

**감사 로그 관리**
- Freshservice 내 모든 활동에 대한 감사 로그 추적
- [감사 로그 접근](https://support.freshservice.com/support/solutions/articles/232444-how-to-access-audit-log-in-freshservice-)

**IP 접근 제어**
- 특정 IP 주소에서만 Freshservice 접근 허용
- [IP 주소 제한](https://support.freshservice.com/support/solutions/articles/195168-restrict-access-to-your-support-portal-using-ip-address)

**SSO 통합**
- 단일 로그인(Single Sign-On) 설정으로 사용자 인증 통합
- [SSO 마이그레이션](https://support.freshservice.com/support/solutions/articles/50000003339-migrating-freshservice-sso-to-freshworks-organization)

#### 오케스트레이션 및 앱 연동

**오케스트레이션 시스템**
- Freshservice 워크플로를 통한 외부 시스템 작업 자동화
- [오케스트레이션 FAQ](https://support.freshservice.com/support/solutions/articles/50000003144-orchestration-faqs)
- [오케스트레이션 서버 설정](https://support.freshservice.com/support/solutions/articles/50000003259-setting-up-the-orchestration-server)

**외부 앱 연동**
- Microsoft Teams, Slack, Jira, G Suite, GitHub, Zoom 등 다양한 앱 지원
- [Teams 통합](https://support.freshservice.com/support/solutions/articles/50000000656-integrating-servicebot-with-microsoft-teams)

## 실무 활용 예시

### 상황 1: 신규 직원 온보딩 자동화
**목표**: 신규 직원 입사 시 필요한 모든 IT 자원을 자동으로 프로비저닝
**방법**: 
1. AD 연동을 통한 사용자 계정 자동 생성
2. 서비스 카탈로그를 통한 필수 소프트웨어/하드웨어 신청
3. 승인 워크플로를 통한 자동 승인 및 할당
4. 온보딩 체크리스트 자동 생성 및 진행 상황 추적

**결과**: 수동 업무 80% 감소, 온보딩 시간 단축

### 상황 2: 인시던트 대응 체계 구축
**목표**: 시스템 장애 발생 시 신속하고 체계적인 대응 체계 마련
**방법**:
1. 자동 티켓 분류 및 우선순위 설정
2. 주요 인시던트 자동 식별 및 에스컬레이션
3. ITIL 기반 문제 관리 프로세스 적용
4. 실시간 대시보드를 통한 현황 모니터링

**결과**: 평균 해결 시간 50% 단축, 고객 만족도 향상

### 상황 3: IT 자산 통합 관리
**목표**: 조직 내 모든 IT 자산의 통합 관리 및 최적화
**방법**:
1. Discovery Agent/Probe를 통한 자동 자산 발견
2. CMDB를 활용한 자산 간 관계 매핑
3. 자산 라이프사이클 관리 자동화
4. 자산 활용도 분석 및 최적화 권고

**결과**: 자산 가시성 100% 확보, 라이선스 비용 20% 절감

## 문제 해결

### 자주 발생하는 설정 문제

#### 문제: AD 연동 시 사용자 동기화 실패
**원인**: 네트워크 연결 문제 또는 권한 설정 오류
**해결**: 
1. 방화벽 설정 확인 (필요한 포트 오픈)
2. AD 서비스 계정 권한 검증
3. Discovery Agent 로그 확인
4. 테스트 사용자로 단계별 확인

#### 문제: 자산 발견이 제대로 되지 않음
**원인**: Discovery Probe 설정 문제 또는 네트워크 스캔 범위 제한
**해결**:
1. Probe 설치 상태 및 네트워크 연결 확인
2. 스캔 범위 및 스케줄 설정 검토
3. 방화벽 및 보안 정책 확인
4. 단계적 스캔 범위 확대

#### 문제: 워크플로 자동화가 작동하지 않음
**원인**: 조건 설정 오류 또는 권한 부족
**해결**:
1. 자동화 규칙의 조건문 검토
2. 실행 권한 및 역할 확인
3. 테스트 케이스로 단계별 검증
4. 로그 분석을 통한 오류 지점 파악

:::success PoC 완료
3주간의 체계적인 PoC를 통해 Freshservice의 핵심 기능을 모두 체험했습니다. 이제 조직의 IT 서비스 관리 효율성을 크게 향상시킬 수 있는 준비가 완료되었습니다.
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [Freshservice 시작 가이드](../getting-started)
- [사용자 관리](../getting-started/user-management)
- [자산 관리](../it-asset-management)
- [워크플로 자동화](../it-service-management)
- [ITIL 프로세스](../it-service-management)
-->

---

**PoC 진행 중 궁금한 점이나 추가적인 문의사항이 있으시면 언제든지 말씀해 주세요. 성공적인 PoC 진행을 위해 최선을 다해 지원하겠습니다.**
