# Freshservice 레거시 리포트 모듈에서 Analytics 모듈로 마이그레이션

> **참고**: 리포트 지원 중단의 일환으로, 2022년 6월에 레거시 리포트에서 Analytics로 리포트를 마이그레이션했습니다. 레거시 리포트는 2022년 11월부터 완전히 지원 중단됩니다.

## 개요

Analytics와 리포팅은 모든 조직이 팀에서 데이터 기반 의사결정을 내릴 수 있도록 하는 데 중요한 요소가 되었습니다. 고객의 리포팅 기능을 향상시키고 중단 없는 서비스 제공을 위해, 기존의 레거시 리포트 모듈에서 훨씬 더 정교하면서도 사용하기 쉬운 Analytics 모듈로 마이그레이션하고 있습니다.

기존 리포트를 잃을까 걱정되시나요? 걱정하지 마세요. Freshservice가 여러분의 노력 없이도 레거시 리포트 모듈의 모든 리포트를 Analytics 모듈로 마이그레이션해드립니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005444723/original/0J9w7NYZUcSaZ6xIf24kuOgRdD6HUck3AQ.png?1652334518" alt="Migration Overview" width="511" height="336" />

## 영향을 받는 대상

2020년 3월 13일 이전에 생성된 계정이거나 레거시 리포트 모듈을 사용하는 모든 고객이 이 마이그레이션의 영향을 받습니다.

## 마이그레이션 이유

Analytics Pro를 통해 리포트 작성 시간을 줄이고 결과 활용에 더 많은 시간을 투자할 수 있습니다. 이는 고객의 리포팅 요구사항을 위한 단일 솔루션 역할을 하는 강력한 도구입니다. Analytics Pro를 통해 고객은 서비스 데스크에 대한 더 즉각적이고 정확한 인사이트를 쉽게 얻고, 데이터 기반 의사결정을 내려 서비스 데스크 효율성을 개선할 수 있습니다.

### 마이그레이션 전후 비교

**이전: 레거시 리포트 모듈의 리포트**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005444819/original/Cf-XMFaCKlG9sSQJUTtiFieu_9-qUL2Zsg.png?1652335565" alt="Legacy Reports" width="624" height="353" />

**이후: Analytics 모듈의 리포트 (마이그레이션된 리포트)**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005444817/original/4gfZrVajMgGSHSRkXDEO376ByZH5UMbqww.png?1652335564" alt="Analytics Reports" width="624" height="296" />

> **참고**: 마이그레이션으로 인한 약간의 데이터 불일치가 있을 수 있습니다 (문서 후반부에서 상세 설명).

## 마이그레이션의 이점

- **사전 구축된 템플릿**: 위젯용 사전 구축된 템플릿에 액세스하여 빠른 리포트 작성
- **고급 필터링**: 다양한 필터로 메트릭 드릴다운; 다양한 매개변수로 메트릭 그룹화
- **고급 리포팅**: 고급 리포팅 기능으로 데이터 심화 분석
- **AI 기반 검색**: Ask Freddy를 사용한 빠른 AI 기반 검색
- **BI 도구 연동**: BI 도구에 입력할 수 있는 데이터 내보내기 기능
- **사용자 정의**: 스타일 및 형식 옵션을 사용하여 리포트 모양 사용자 정의
- **리포트 공유**: 리포트 공유 기능

## 마이그레이션 타임라인

레거시 리포트에서 Analytics 모듈로의 마이그레이션은 두 단계로 계획되었습니다. 1단계는 2022년 6월, 2단계는 2022년 11월에 예정되어 있습니다.

### 1단계 (2022년 6월)

<div className="table-container">

| 날짜 | 이벤트 |
|-----|-------|
| **2022년 6월** | • 레거시 리포트 모듈에서 리포트 및 스케줄 생성 및 편집 기능 비활성화<br/>• 새로운 리포트, 스케줄, 내보내기는 **Analytics** 모듈을 활용해야 함<br/>• 기존 리포트의 Analytics 모듈로의 단계적 마이그레이션 시작<br/>• 레거시 리포트 모듈에서 생성된 모든 스케줄은 비활성화 상태로 Analytics 모듈로 마이그레이션 |

</div>

### 2단계 (2022년 11월)

<div className="table-container">

| 날짜 | 이벤트 |
|-----|-------|
| **2022년 11월** | • 레거시 리포트 모듈 완전 지원 중단<br/>• 레거시 리포트 모듈에서 마이그레이션된 스케줄이 Analytics 모듈에서 활성화<br/>• 역할이 Analytics로 마이그레이션 |

</div>

> **중요**: 2022년 11월 이후 사용자는 레거시 리포트에 액세스할 수 없습니다.

## 변경 사항

### 주요 변경사항

1. **새 리포트 생성 제한**: 사용자는 레거시 리포트 모듈에서 새 리포트를 생성하거나 기존 리포트를 편집할 수 없습니다. 더 많은 기능을 제공하는 Analytics 모듈로 이동해야 합니다.

2. **마이그레이션된 리포트**: 레거시 리포트 모듈의 마이그레이션된 리포트는 Analytics 모듈에서 사용자 정의 리포트로 제공됩니다.
   - 리포트는 레거시 리포트 모듈과 동일한 이름으로 마이그레이션되며, `'{모듈} Reports:'` 접두사가 추가됩니다
   - 예: "Agent Ticket Summary"라는 티켓 리포트는 "Tickets Report: Agent Ticket Summary"로 마이그레이션됩니다
   - 기본 리포트의 모든 뷰는 Analytics 모듈에서 별도의 리포트로 마이그레이션됩니다

3. **위젯 분리**: 마이그레이션된 사용자 정의 리포트에서 차트와 데이터는 두 개의 다른 위젯으로 마이그레이션됩니다.

4. **그룹화 제한**: 차트와 테이블 데이터의 그룹화 기준이 다를 수 없습니다. Analytics에서는 동일한 속성으로만 그룹화할 수 있습니다.

### 데이터 차이점

두 모듈 간에 데이터 불일치가 있을 수 있습니다:

<div className="table-container">

| 항목 | 설명 |
|-----|------|
| **병합된 티켓** | Analytics 모듈(및 사용자 정의 리포트)에 포함되지 않음 |
| **데이터 새로 고침 빈도** | • 기본 리포트: 1일<br/>• 사용자 정의 리포트: 4시간<br/>• Analytics 모듈: 30분 |

</div>

## 역할 마이그레이션

2022년 11월에 레거시 리포트 모듈에서 Analytics 모듈로 모든 역할과 액세스 권한이 마이그레이션됩니다. 이는 레거시 리포트 모듈에는 액세스할 수 있지만 Analytics 모듈에는 액세스할 수 없는 상담원들이 Analytics에서 리포트를 공유하는 데 어려움을 겪는 상황을 방지하기 위함입니다.

역할 마이그레이션에 대한 자세한 정보는 [여기](https://support.freshservice.com/en/support/solutions/articles/50000004236-roles-migration-from-legacy-reports-modules-to-analytics-module)를 참조하세요.

## 걱정하지 않아도 되는 사항

- **고객 조치 불필요**: 마이그레이션 수행을 위해 고객 측에서 어떤 조치나 확인도 필요하지 않습니다. 모든 과정을 처리해드립니다.
- **서비스 중단 없음**: 전체 마이그레이션 기간 동안 Analytics 모듈의 다운타임이 발생하지 않습니다.

## 마이그레이션 준비사항

### 사전 준비

1. **현재 리포트 목록 확인**: 마이그레이션될 모든 리포트 목록을 확인하세요
2. **중요 리포트 식별**: 비즈니스에 중요한 리포트를 식별하세요
3. **사용자 교육 계획**: Analytics 모듈 사용법에 대한 사용자 교육을 계획하세요

### 마이그레이션 후 확인

1. **마이그레이션된 리포트 검증**: 모든 리포트가 올바르게 마이그레이션되었는지 확인하세요
2. **데이터 정확성 검증**: 중요한 리포트의 데이터가 예상과 일치하는지 확인하세요
3. **스케줄 재활성화**: 필요한 스케줄을 재활성화하세요

## 지원 및 문의

마이그레이션과 관련된 지원이나 문의사항이 있으시면 [support@freshservice.com](mailto:support@freshservice.com)으로 연락해주세요.

## 추가 자료

- [Analytics 시작하기](getting-started-with-analytics-basic.md)
- [역할 마이그레이션 가이드](roles-migration-from-legacy-reports-modules-to-analytics-module.md)
- [Analytics Pro로 직관적인 리포트 생성하기](generate-intuitive-reports-using-analytics-pro.md)

이 마이그레이션을 통해 더 강력하고 유연한 Analytics 플랫폼으로 전환하여 더 나은 인사이트와 의사결정을 지원할 수 있습니다.