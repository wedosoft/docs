---
sidebar_position: 4
---

# ITSM 서비스 아이템 설정 및 구성

ITSM 환경에서 서비스 아이템은 IT 서비스 제공의 핵심 요소로, 표준화된 서비스 요청 프로세스를 통해 조직의 IT 서비스 품질과 효율성을 향상시킵니다.

:::info ITSM 서비스 아이템 핵심 원칙
- **ITIL 프레임워크 준수**: 서비스 포트폴리오와 카탈로그 관리 표준 적용
- **표준화된 분류**: IT 서비스 카테고리별 체계적 분류 (Infrastructure, Application, Security 등)
- **SLA 연동**: 각 서비스 아이템별 서비스 수준 협약 자동 적용
- **변경 관리 통합**: 서비스 변경 시 Change Management 프로세스 연동
:::

## ITSM 서비스 카테고리 구조

### 표준 ITSM 서비스 분류

```
🔧 Infrastructure Services
├── Server & Storage
├── Network & Connectivity  
├── Backup & Recovery
└── Cloud Services

💻 Application Services
├── Business Applications
├── Development Tools
├── Database Services
└── Monitoring & Analytics

🛡️ Security Services
├── Access Management
├── Security Tools
├── Compliance & Audit
└── Incident Response

👥 End User Services
├── Desktop Support
├── Mobile Device Management
├── Software Installation
└── Account Management
```

### 서비스 아이템 생성 프로세스

#### 1단계: 서비스 정의 및 분류
1. **Admin** → **Service Management** → **Service Catalog** 접근
2. **Add New** → **Service Item** 선택
3. ITSM 카테고리 선택 및 서비스명 정의

#### 2단계: ITIL 속성 설정
- **Service Owner**: 서비스 책임자 지정
- **Service Type**: Core, Supporting, Enhancing 분류
- **Service Level**: Gold, Silver, Bronze 등급 설정
- **Business Criticality**: Critical, High, Medium, Low 분류

:::warning ITSM 준수사항
- 모든 서비스 아이템은 승인된 서비스 포트폴리오에 포함되어야 함
- 서비스 카탈로그 변경 시 Change Advisory Board(CAB) 승인 필요
- 비즈니스 영향도에 따른 적절한 승인 워크플로우 설정 필수
:::

## 커스텀 필드 설계

### ITSM 필수 필드

#### 비즈니스 정보
- **Business Unit**: 요청 부서
- **Cost Center**: 비용 센터 코드
- **Business Justification**: 비즈니스 타당성
- **Expected ROI**: 기대 투자 수익률

#### 기술 정보
- **Technical Requirements**: 기술적 요구사항
- **Dependencies**: 의존성 분석
- **Risk Assessment**: 위험도 평가
- **Implementation Timeline**: 구현 일정

#### 규정 준수
- **Compliance Requirements**: 규정 준수 요구사항
- **Security Classification**: 보안 등급
- **Data Classification**: 데이터 분류
- **Audit Requirements**: 감사 요구사항

:::tip ITSM 모범 사례
- **자동화 우선**: 반복적인 요청은 자동화 워크플로우 적용
- **표준화**: 동일한 서비스에 대해 일관된 프로세스 제공
- **측정 가능**: 서비스 성과 측정을 위한 KPI 설정
- **지속적 개선**: 정기적인 서비스 검토 및 개선
:::

## 승인 워크플로우 설계

### 비즈니스 영향도 기반 승인 매트릭스

| 영향도 | 비용 범위 | 승인 단계 | 승인자 |
|--------|-----------|-----------|--------|
| **Critical** | 1억원 이상 | 3단계 | 팀장 → 부서장 → CIO |
| **High** | 1천만원-1억원 | 2단계 | 팀장 → 부서장 |
| **Medium** | 100만원-1천만원 | 1단계 | 팀장 승인 |
| **Low** | 100만원 미만 | 자동승인 | 시스템 자동처리 |

### 승인 프로세스 자동화

#### Emergency Request 처리
```
조건: 업무 중단 관련 긴급 요청
프로세스: 
1. 즉시 임시 승인
2. 사후 정식 승인 절차 진행
3. 24시간 내 CAB 검토
```

#### Standard Request 처리
```
조건: 사전 승인된 표준 서비스
프로세스:
1. 자동 승인
2. 이행 팀 자동 배정
3. 표준 SLA 적용
```

## 서비스 수준 관리

### SLA 통합 설정

#### 서비스별 SLA 매트릭스
- **P1 (Critical)**: 15분 이내 응답, 4시간 이내 해결
- **P2 (High)**: 1시간 이내 응답, 1일 이내 해결
- **P3 (Medium)**: 4시간 이내 응답, 3일 이내 해결
- **P4 (Low)**: 1일 이내 응답, 1주일 이내 해결

#### SLA 자동 적용 규칙
1. 서비스 아이템 카테고리별 기본 SLA 설정
2. 요청자 그룹별 차등 SLA 적용
3. 비즈니스 시간/업무 외 시간 구분 적용

:::success ITSM 통합 성과
- **서비스 표준화**: 일관된 서비스 제공 프로세스 구축
- **가시성 향상**: 서비스 포트폴리오 전체 현황 파악 가능
- **비용 최적화**: 서비스별 비용 투명성 확보
- **규정 준수**: ITIL/ISO 20000 표준 준수 체계 구축
:::

## 실무 활용 예시

### 상황 1: 글로벌 제조업체의 ERP 시스템 업그레이드 요청
**목표**: 다국가 ERP 시스템 업그레이드를 체계적으로 관리

**방법**:
1. **서비스 아이템 생성**: "ERP System Upgrade" 서비스 아이템 설정
2. **국가별 승인 워크플로우**: 각 국가의 현지 법규 및 비즈니스 요구사항 반영
3. **위험도 평가 필드**: 업그레이드 영향도, 롤백 계획, 테스트 결과 등
4. **다단계 승인**: 현지 IT 팀 → 지역 본부 → 글로벌 IT → CEO 승인

**결과**: 6개국 동시 ERP 업그레이드 성공, 다운타임 최소화, 규정 준수 100% 달성

### 상황 2: 금융기관의 보안 강화 서비스 체계 구축
**목표**: 금융 규정 준수를 위한 보안 서비스 카탈로그 구축

**방법**:
1. **보안 등급별 서비스 분류**: 
   - Level 1: 일반 사용자 보안 도구
   - Level 2: 관리자 권한 보안 솔루션  
   - Level 3: 핵심 시스템 보안 서비스
2. **규정 준수 체크리스트**: 금융감독원, PCI-DSS, ISO 27001 요구사항 자동 검증
3. **감사 추적**: 모든 보안 서비스 요청 및 승인 과정 자동 로깅

**결과**: 금융감독원 검사 통과, 보안 서비스 요청 처리 시간 50% 단축, 컴플라이언스 위반 0건