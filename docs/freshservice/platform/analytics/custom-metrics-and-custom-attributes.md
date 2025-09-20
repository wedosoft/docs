---
sidebar_position: 13
---

# 사용자 정의 메트릭 및 사용자 정의 속성

Freshservice Analytics에서 조직의 특별한 요구사항에 맞는 사용자 정의 메트릭과 속성을 생성하고 활용하는 방법을 설명합니다.

:::info 맞춤형 분석 도구
표준 메트릭과 속성 외에도 조직의 고유한 비즈니스 요구사항을 충족하기 위해 사용자 정의 메트릭과 속성을 생성할 수 있습니다.
:::

## 개요

## 사용자 정의 메트릭

:::tip 메트릭 설계 원칙
효과적인 사용자 정의 메트릭은 측정 가능하고, 실행 가능하며, 비즈니스 목표와 직접 연결되어야 합니다.
:::

### 지원되는 메트릭 유형

#### 1. 계산된 메트릭

**정의**: 기존 메트릭을 조합하여 새로운 의미를 가지는 메트릭

**예시**:
```
예시 1: 에이전트 효율성
 = (해결된 티켓 수) / (할당된 티켓 수) × 100

예시 2: 평균 해결 비용
 = (총 운영 비용) / (해결된 티켓 수)

예시 3: 고객 만족 비율
 = (CSAT 4-5점 응답 수) / (총 CSAT 응답 수) × 100
```

#### 2. 조건부 메트릭

**정의**: 특정 조건을 만족하는 데이터만 계산하는 메트릭

**예시**:
```
예시 1: 긴급 티켓 해결 시간
 =  IF(우선순위  = "긴급", 해결 시간, NULL)

예시 2: VIP 고객 만족도
 =  IF(고객 유형  = "VIP", CSAT 점수, NULL)

예시 3: 업무 시간 외 티켓 수
 =  IF(생성 시간 NOT IN 업무시간, 1, 0)
```

#### 3. 시계열 메트릭

**정의**: 시간 경과에 따른 변화를 추적하는 메트릭

**예시**:
```
예시 1: 월별 증가율
 = (이번 달 티켓 수 - 지난 달 티켓 수) / 지난 달 티켓 수 × 100

예시 2: 누적 해결 티켓
 =  SUM(해결된 티켓 수) OVER (ORDER BY 날짜)

예시 3: 이동 평균 해결 시간
 =  AVG(해결 시간) OVER (ORDER BY 날짜 ROWS 6 PRECEDING)
```

### 사용자 정의 메트릭 생성 과정

#### 1단계: 비즈니스 요구사항 정의

<div className="procedure">
  <ol>
    <li><strong>목적 명확화</strong>: 메트릭으로 측정하고자 하는 것이 무엇인지 정의</li>
    <li><strong>계산 공식 설계</strong>: 필요한 데이터 요소와 계산 방법 결정</li>
    <li><strong>기준값 설정</strong>: 성과 평가를 위한 목표치나 기준값 정의</li>
</ol>
</div>

#### 2단계: 데이터 소스 확인

<div className="procedure">
  <ol>
    <li><strong>필요한 데이터 식별</strong>: 계산에 필요한 모든 데이터 요소 확인</li>
    <li><strong>데이터 품질 검증</strong>: 데이터의 정확성과 완전성 확인</li>
    <li><strong>데이터 가용성 확인</strong>: Analytics에서 해당 데이터에 접근 가능한지 확인</li>
</ol>
</div>

#### 3단계: 메트릭 구현

```javascript
// 예시: 사용자 정의 메트릭 생성 (JavaScript 기반)
const customMetrics  = &#123;
  // 에이전트 생산성 메트릭
  agentProductivity: function(resolvedTickets, assignedTickets) {
    return assignedTickets > 0 ? (resolvedTickets / assignedTickets) * 100 : 0;
  &#125;,
  
  // 고객 만족 지수
  customerSatisfactionIndex: function(csat5, csat4, totalResponses) {
    return totalResponses > 0 ? ((csat5 + csat4) / totalResponses) * 100 : 0;
  },
  
  // 비용 효율성
  costEfficiency: function(totalCost, resolvedTickets) {
    return resolvedTickets > 0 ? totalCost / resolvedTickets : 0;
  }
};
```

## 사용자 정의 속성

:::warning 속성 설계 주의사항
사용자 정의 속성은 시스템 성능에 영향을 줄 수 있으므로, 반드시 필요한 속성만 추가하고 데이터 타입을 신중하게 선택하세요.
:::

### 속성 카테고리

#### 1. 비즈니스 맥락 속성

**목적**: 비즈니스 프로세스나 조직 구조를 반영

**예시**:
- **비용 센터**: 부서별 비용 추적
- **프로젝트 코드**: 프로젝트별 지원 요청 분석
- **서비스 레벨**: 고객별 서비스 등급
- **지리적 위치**: 지역별 지원 분석

#### 2. 성과 측정 속성

**목적**: 성과 평가와 개선을 위한 추가 정보

**예시**:
- **복잡도 점수**: 티켓 처리 난이도
- **고객 중요도**: 고객의 비즈니스 영향도
- **긴급도 가중치**: 우선순위별 가중값
- **해결 유형**: 해결 방법 분류

#### 3. 운영 효율성 속성

**목적**: 운영 프로세스 최적화를 위한 데이터

**예시**:
- **자동화 사용 여부**: 자동화 도구 활용 추적
- **에스컬레이션 레벨**: 에스컬레이션 단계
- **재작업 여부**: 재처리가 필요한 티켓
- **지식베이스 참조**: KB 활용 여부

### 속성 생성 가이드

#### 텍스트 속성

```
이름: Customer_Segment
유형: 드롭다운 (단일 선택)
옵션: Enterprise, SMB, Startup, Non-Profit
용도: 고객 세그먼트별 분석
```

#### 숫자 속성

```
이름: Complexity_Score  
유형: 숫자 (1-10)
기본값: 5
용도: 티켓 복잡도 측정
```

#### 날짜 속성

```
이름: Target_Resolution_Date
유형: 날짜
용도: 목표 해결일 추적
```

#### 불린 속성

```
이름: Is_Automated_Resolution
유형: 체크박스
기본값: False
용도: 자동화 해결 여부 추적
```

## 활용 사례

### 1. 고급 성과 대시보드

**목표**: 경영진을 위한 종합적인 성과 지표

**사용자 정의 메트릭**:
- 고객 성공 지수 (Customer Success Index)
- 서비스 효율성 비율 (Service Efficiency Ratio)
- 비용 대비 효과 (Cost-Effectiveness)

**구현 예시**:
```
고객 성공 지수  = (CSAT 평균 점수 × 0.4) + 
  (재문의 비율 × -0.3) + 
  (해결 시간 준수율 × 0.3)
```

### 2. 부서별 맞춤 분석

**목표**: 각 부서의 특성에 맞는 분석

**IT 부서**:
- 시스템 가용성 메트릭
- 보안 인시던트 심각도
- 인프라 비용 효율성

**HR 부서**:
- 직원 만족도 지수
- 온보딩 프로세스 효율성
- 교육 프로그램 효과

### 3. 고객 세그먼트 분석

**목표**: 고객 유형별 차별화된 서비스

**사용자 정의 속성**:
- 고객 가치 등급 (Customer Value Tier)
- 서비스 복잡도 (Service Complexity)
- 계약 유형 (Contract Type)

## 구현 모범 사례

:::tip 성공적인 구현을 위한 핵심
데이터 설계 단계에서의 신중한 계획과 지속적인 모니터링이 사용자 정의 메트릭과 속성의 성공적인 활용을 보장합니다.
:::

### 1. 데이터 설계

**일관성 유지**:
- 표준화된 명명 규칙 사용
- 데이터 타입 일관성 확보
- 필드 의미 명확화

**확장성 고려**:
- 미래 요구사항 고려한 구조 설계
- 모듈화된 접근 방식
- 버전 관리 계획

### 2. 성능 최적화

**효율적인 계산**:
- 불필요한 복잡성 피하기
- 인덱싱 가능한 필드 활용
- 적절한 데이터 집계 수준 선택

**캐싱 전략**:
- 자주 사용되는 메트릭 사전 계산
- 실시간 vs 배치 처리 구분
- 적절한 새로고침 주기 설정

### 3. 품질 관리

**검증 절차**:
- 메트릭 정확성 정기 검증
- 데이터 무결성 확인
- 예상 범위 내 값 유지

**문서화**:
- 메트릭 정의 명확한 문서화
- 계산 공식 상세 기록
- 사용 예시 및 해석 가이드

## 고급 기능

### 1. 동적 메트릭

실시간으로 변화하는 비즈니스 조건에 따라 조정되는 메트릭:

```javascript
// 동적 가중치를 적용한 메트릭
function dynamicPriorityScore(ticket) {
  const timeWeight  =  getTimeBasedWeight(ticket.createdDate);
  const customerWeight  =  getCustomerTierWeight(ticket.customer);
  const impactWeight  =  getImpactWeight(ticket.impact);
  
  return (timeWeight + customerWeight + impactWeight) / 3;
}
```

### 2. 예측 메트릭

과거 데이터를 기반으로 미래 추세를 예측하는 메트릭:

```javascript
// 간단한 선형 회귀 기반 예측
function predictTicketVolume(historicalData, forecastPeriod) {
  const trend  =  calculateTrend(historicalData);
  const seasonality  =  calculateSeasonality(historicalData);
  
  return trend * forecastPeriod + seasonality;
}
```

### 3. 알림 기반 메트릭

임계값 초과 시 자동으로 알림을 발생시키는 메트릭:

```javascript
// 임계값 모니터링
const alertMetrics  = &#123;
  slaBreachRate: &#123;
    threshold: 5, // 5% 초과 시 알림
    condition: 'greater_than',
    notification: 'email'
  &#125;,
  
  avgResolutionTime: &#123;
    threshold: 24, // 24시간 초과 시 알림
    condition: 'greater_than',
    notification: 'slack'
  &#125;
&#125;;
```

## 제한사항 및 고려사항

:::warning 구현 시 주의사항
사용자 정의 메트릭과 속성 구현 시 기술적 제한사항과 비즈니스 요구사항을 균형 있게 고려하여 진행하세요.
:::

### 기술적 제한사항

- **계산 복잡도**: 과도하게 복잡한 메트릭은 성능 저하 야기
- **데이터 크기**: 대용량 데이터 처리 시 지연 발생 가능
- **실시간 처리**: 모든 메트릭이 실시간 계산되지 않음

### 비즈니스 고려사항

- **사용자 교육**: 새로운 메트릭의 의미와 해석 방법 교육 필요
- **변경 관리**: 메트릭 변경 시 기존 리포트에 미치는 영향 고려
- **거버넌스**: 메트릭 생성과 관리에 대한 승인 절차 필요

사용자 정의 메트릭과 속성을 효과적으로 활용하면 조직의 고유한 요구사항에 맞는 정확하고 의미 있는 분석을 수행할 수 있습니다.

:::success 맞춤형 분석 완성
사용자 정의 메트릭과 속성을 통해 조직만의 독특한 인사이트를 발굴하고, 데이터 기반 의사결정 역량을 한 단계 높여보세요.
:::