# 리포트 지원 중단: 마이그레이션된 리포트가 Analytics 모듈에서 어떻게 보이는가

## 개요

레거시 리포트 모듈에서 Analytics 모듈로 마이그레이션된 리포트가 어떻게 변환되고 표시되는지 시각적 예시를 통해 설명합니다.

## 마이그레이션 전후 비교

### 1. 기본 리포트 구조 변화

#### 마이그레이션 전 (레거시 리포트)

```text
단일 리포트 구조:
├── 리포트 이름: "Agent Performance Report"
├── 차트 섹션 (파이 차트)
├── 테이블 섹션 (상세 데이터)
└── 필터 옵션 (사이드바)
```

#### 마이그레이션 후 (Analytics 모듈)

```text
위젯 기반 구조:
├── 리포트 이름: "Tickets Report: Agent Performance Report"
├── 위젯 1: 차트 (파이 차트 위젯)
├── 위젯 2: 테이블 (테이블 위젯)
└── 공통 필터 (상단 도구모음)
```

### 2. 시각적 변화 예시

#### 레거시 리포트의 모습

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005444819/original/Cf-XMFaCKlG9sSQJUTtiFieu_9-qUL2Zsg.png?1652335565" alt="Legacy Report Example" width="624" height="353" />

**특징:**
- 전통적인 리포트 레이아웃
- 고정된 차트와 테이블 배치
- 제한적인 사용자 정의 옵션

#### Analytics 모듈의 마이그레이션된 리포트

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50005444817/original/4gfZrVajMgGSHSRkXDEO376ByZH5UMbqww.png?1652335564" alt="Analytics Migrated Report" width="624" height="296" />

**특징:**
- 모던한 대시보드 스타일
- 독립적인 위젯 구조
- 유연한 레이아웃 조정 가능

## 마이그레이션 규칙

### 1. 이름 변환 규칙

<div className="table-container">

| 원본 모듈 | 접두사 | 예시 |
|----------|--------|------|
| **Tickets** | "Tickets Report:" | "Agent Summary" → "Tickets Report: Agent Summary" |
| **Assets** | "Assets Report:" | "Hardware Report" → "Assets Report: Hardware Report" |
| **Changes** | "Changes Report:" | "Change Statistics" → "Changes Report: Change Statistics" |
| **Problems** | "Problems Report:" | "Problem Analysis" → "Problems Report: Problem Analysis" |

</div>

### 2. 위젯 분리 규칙

#### 차트와 테이블 분리

```text
레거시에서 한 리포트에 있던:
✓ 차트 + 테이블
↓
Analytics에서 두 개 위젯으로:
✓ 차트 위젯
✓ 테이블 위젯
```

#### 다중 뷰 처리

```text
레거시 리포트에 3개 뷰가 있었다면:
├── View 1: Summary Chart
├── View 2: Detailed Table  
└── View 3: Trend Analysis
↓
Analytics에서 3개 별도 리포트로:
├── "Tickets Report: Summary Chart"
├── "Tickets Report: Detailed Table"
└── "Tickets Report: Trend Analysis"
```

## 구체적인 마이그레이션 예시

### 예시 1: 티켓 담당자 성과 리포트

#### 마이그레이션 전

```text
리포트명: "Agent Performance Dashboard"

구성:
- 파이 차트: 담당자별 티켓 분포
- 바 차트: 담당자별 해결 시간
- 테이블: 상세 성과 지표
- 필터: 날짜 범위, 부서
```

#### 마이그레이션 후

```text
리포트명: "Tickets Report: Agent Performance Dashboard"

위젯 구성:
┌─────────────────┬─────────────────┐
│   위젯 1:       │   위젯 2:       │
│  담당자별 티켓   │  담당자별 해결   │
│   분포 (파이)    │   시간 (바)     │
├─────────────────┴─────────────────┤
│           위젯 3:                 │
│        상세 성과 지표 (테이블)     │
└───────────────────────────────────┘

공통 필터: 날짜 범위, 부서 (상단)
```

### 예시 2: 자산 관리 리포트

#### 마이그레이션 전

```text
리포트명: "Asset Utilization Report"

뷰 1: "Overview Chart" - 자산 유형별 분포
뷰 2: "Details Table" - 자산 상세 목록
뷰 3: "Trend Analysis" - 월별 자산 변화
```

#### 마이그레이션 후

```text
3개의 별도 리포트로 분리:

1. "Assets Report: Overview Chart"
   └── 자산 유형별 분포 위젯

2. "Assets Report: Details Table" 
   └── 자산 상세 목록 위젯

3. "Assets Report: Trend Analysis"
   └── 월별 자산 변화 위젯
```

## 향상된 기능

### 1. 위젯 기반 유연성

#### 크기 조정

```text
레거시: 고정된 레이아웃
Analytics: 위젯 크기 자유 조정
┌─────┬─────┐    ┌───────────┐
│  A  │  B  │ or │     A     │
├─────┴─────┤    ├─────┬─────┤
│     C     │    │  B  │  C  │
└───────────┘    └─────┴─────┘
```

#### 위치 변경

```text
드래그 앤 드롭으로 위젯 위치 자유 변경:
Before:  [A][B][C]
After:   [C][A][B]
```

### 2. 개별 위젯 설정

<div className="table-container">

| 기능 | 레거시 리포트 | Analytics 위젯 |
|-----|-------------|---------------|
| **차트 유형 변경** | 제한적 | 자유로운 변경 |
| **색상 설정** | 고정 | 커스터마이징 가능 |
| **필터 적용** | 전체 리포트 | 위젯별 개별 설정 |
| **데이터 범위** | 동일 범위 | 위젯별 다른 범위 |

</div>

### 3. 새로운 시각화 옵션

#### 사용 가능한 차트 유형

```text
레거시에서 제한적이었던 차트 유형이 확장:

기본 차트:
✓ 바 차트 (수직/수평)
✓ 파이 차트
✓ 라인 차트
✓ 테이블

새로 추가된 차트:
✓ 도넛 차트
✓ 히트맵
✓ 스택형 차트
✓ 게이지 차트
✓ KPI 위젯
```

## 데이터 정확성 및 차이점

### 1. 데이터 일치도

<div className="table-container">

| 데이터 유형 | 일치도 | 비고 |
|------------|--------|------|
| **기본 메트릭** | 99%+ | 거의 동일 |
| **집계 데이터** | 95%+ | 방법론 차이로 인한 소폭 차이 |
| **병합 티켓** | 0% | Analytics에서 제외 |
| **실시간 데이터** | 향상됨 | 30분마다 업데이트 |

</div>

### 2. 예상 차이점

```text
일반적으로 발생하는 데이터 차이:

1. 병합된 티켓 제외로 인한 카운트 차이
2. 더 빈번한 데이터 업데이트로 인한 최신성 차이
3. 개선된 필터링 로직으로 인한 정확도 향상
```

## 마이그레이션 후 권장 사항

### 1. 초기 검증

1. **데이터 비교**: 중요한 리포트의 데이터를 기존과 비교
2. **기능 테스트**: 필터, 드릴다운 등 주요 기능 확인
3. **성능 평가**: 로딩 속도 및 응답성 체험

### 2. 최적화 작업

1. **레이아웃 조정**: 새로운 유연성을 활용한 레이아웃 개선
2. **위젯 통합**: 필요시 관련 위젯들을 하나의 리포트로 통합
3. **새 기능 활용**: 향상된 시각화 및 필터링 옵션 적용

### 3. 교육 및 적응

1. **사용자 교육**: 새로운 인터페이스 사용법 숙지
2. **모범 사례 공유**: 팀 내 효과적인 활용 방법 공유
3. **지속적 개선**: 사용 경험을 바탕으로 리포트 지속 개선

마이그레이션된 리포트는 기존 기능을 보존하면서도 더욱 강력하고 유연한 분석 환경을 제공합니다.