---
sidebar_position: 14
---

# Analytics 데이터 웨어하우스 및 ETL 프로세스

Freshservice Analytics의 강력한 분석 기능은 체계적인 데이터 웨어하우스 아키텍처와 효율적인 ETL(Extract, Transform, Load) 프로세스를 기반으로 합니다.

:::info 데이터 아키텍처 이해
이 문서는 Analytics 플랫폼의 데이터 처리 방식과 최적화 방법을 상세히 설명합니다.
:::

## 데이터 웨어하우스 아키텍처

:::tip 계층화 아키텍처의 장점
계층별 데이터 구조는 데이터 품질을 보장하고, 성능을 최적화하며, 유지보수를 용이하게 합니다.
:::

### 1. 계층별 데이터 구조

#### 운영 데이터 계층 (Operational Layer)
```
실시간 운영 데이터:
📊 Tickets: 실시간 티켓 정보
👥 Users: 사용자 및 상담원 데이터
🏢 Organizations: 조직 및 부서 정보
💼 Assets: IT 자산 관리 데이터
🔄 Changes: 변경 관리 기록
📋 Problems: 문제 관리 데이터
```

#### 스테이징 계층 (Staging Layer)
```
데이터 변환 중간 단계:
- 원본 데이터 임시 저장
- 데이터 품질 검증
- 형식 표준화
- 중복 제거
- 데이터 정합성 검사
```

#### 데이터 마트 계층 (Data Mart Layer)
```
분석용 최적화 데이터:
🎯 Service Desk Mart: 서비스 데스크 KPI
📈 Performance Mart: 성능 분석 데이터
👤 Customer Mart: 고객 중심 분석
🔧 Asset Mart: 자산 관리 분석
📊 Financial Mart: 비용 및 ROI 분석
```

### 2. 데이터 모델링

#### 차원 모델 (Dimensional Model)
```
팩트 테이블 (Fact Tables):
- FactTickets: 티켓 관련 측정값
- FactAssets: 자산 관련 메트릭
- FactSurveys: 만족도 조사 결과
- FactTimeTracking: 시간 추적 데이터

차원 테이블 (Dimension Tables):
- DimTime: 시간 차원 (일, 주, 월, 분기, 년)
- DimAgent: 상담원 차원
- DimCustomer: 고객 차원
- DimCategory: 카테고리 차원
- DimPriority: 우선순위 차원
```

## ETL 프로세스 상세

:::warning ETL 성능 주의사항
ETL 프로세스는 시스템 성능에 직접적인 영향을 미치므로, 적절한 배치 처리 시간과 리소스 관리가 필수입니다.
:::

### 1. 추출 (Extract) 단계

#### 실시간 데이터 캡처
```sql
-- 변경된 티켓 데이터 추출
SELECT 
    id,
    subject,
    description,
    status,
    priority,
    created_at,
    updated_at,
    assigned_to,
    requester_id
FROM tickets 
WHERE updated_at > :last_extract_time
```

#### 증분 추출 전략
```python
def extract_incremental_data(table_name, last_sync_time):
    """
    증분 데이터 추출 함수
    """
    query  =  f"""
    SELECT * FROM {table_name} 
    WHERE modified_date > '{last_sync_time}'
    OR created_date > '{last_sync_time}'
    """
    
    return execute_query(query)
```

### 2. 변환 (Transform) 단계

#### 데이터 정제 및 표준화
```python
def clean_ticket_data(raw_data):
    """
    티켓 데이터 정제 함수
    """
    cleaned_data  = []
    
    for record in raw_data:
        # NULL 값 처리
        record['priority'] =  record['priority'] or 'Medium'
        record['category'] =  record['category'] or 'General'
        
        # 데이터 형식 표준화
        record['created_at'] =  standardize_datetime(record['created_at'])
        
        # 데이터 검증
        if validate_record(record):
            cleaned_data.append(record)
    
    return cleaned_data
```

#### 비즈니스 규칙 적용
```python
def apply_business_rules(ticket_data):
    """
    비즈니스 규칙 적용
    """
    # SLA 계산
    ticket_data['sla_breached'] =  calculate_sla_breach(
        ticket_data['created_at'],
        ticket_data['resolved_at'],
        ticket_data['priority']
    )
    
    # 응답 시간 계산
    ticket_data['first_response_time'] =  calculate_first_response_time(
        ticket_data['created_at'],
        ticket_data['first_response_at']
    )
    
    # 고객 세그먼트 분류
    ticket_data['customer_segment'] =  classify_customer_segment(
        ticket_data['requester_id']
    )
    
    return ticket_data
```

#### 집계 및 요약 테이블 생성
```sql
-- 일별 티켓 요약 테이블
CREATE TABLE daily_ticket_summary AS
SELECT 
    DATE(created_at) as ticket_date,
    priority,
    category,
    COUNT(*) as ticket_count,
    AVG(CASE WHEN resolved_at IS NOT NULL 
        THEN TIMESTAMPDIFF(HOUR, created_at, resolved_at) 
        END) as avg_resolution_time,
    COUNT(CASE WHEN sla_breached  =  1 THEN 1 END) as sla_breach_count
FROM processed_tickets
GROUP BY DATE(created_at), priority, category;
```

### 3. 적재 (Load) 단계

#### 배치 로딩 전략
```python
def load_data_batch(data, table_name, batch_size=1000):
    """
    배치 단위 데이터 로딩
    """
    for i in range(0, len(data), batch_size):
        batch  =  data[i:i + batch_size]
        
        try:
            insert_batch(table_name, batch)
            log_success(f"Loaded batch {i//batch_size + 1}")
            
        except Exception as e:
            log_error(f"Failed to load batch {i//batch_size + 1}: {e}")
            # 실패한 배치는 별도 처리
            handle_failed_batch(batch, table_name)
```

#### 실시간 스트리밍 로드
```python
def stream_real_time_data():
    """
    실시간 데이터 스트리밍 처리
    """
    kafka_consumer  =  create_kafka_consumer('freshservice-events')
    
    for message in kafka_consumer:
        event_data  =  json.loads(message.value)
        
        # 실시간 변환
        transformed_data  =  transform_real_time_event(event_data)
        
        # 즉시 로드
        load_to_analytics_db(transformed_data)
        
        # 실시간 대시보드 업데이트
        update_real_time_metrics(transformed_data)
```

## 데이터 품질 관리

:::info 데이터 품질의 중요성
분석 결과의 신뢰성은 데이터 품질에 직접적으로 의존하므로, 체계적인 품질 관리 프로세스가 필수입니다.
:::

### 1. 데이터 검증 규칙

#### 필수 필드 검증
```python
def validate_required_fields(record, required_fields):
    """
    필수 필드 검증
    """
    for field in required_fields:
        if not record.get(field):
            raise ValidationError(f"Required field {field} is missing")
```

#### 데이터 타입 검증
```python
def validate_data_types(record, field_types):
    """
    데이터 타입 검증
    """
    for field, expected_type in field_types.items():
        if field in record:
            if not isinstance(record[field], expected_type):
                record[field] =  convert_type(record[field], expected_type)
```

#### 참조 무결성 검증
```sql
-- 외래 키 제약 조건 검사
SELECT t.id, t.assigned_to
FROM tickets t
LEFT JOIN agents a ON t.assigned_to  =  a.id
WHERE t.assigned_to IS NOT NULL 
AND a.id IS NULL;
```

### 2. 데이터 이상 탐지

#### 통계적 이상 탐지
```python
def detect_statistical_anomalies(data, column):
    """
    통계적 방법을 사용한 이상값 탐지
    """
    mean  =  np.mean(data[column])
    std  =  np.std(data[column])
    threshold  =  3 * std
    
    anomalies  =  data[
        (data[column] &lt;  mean - threshold) | 
        (data[column] > mean + threshold)
    ]
    
    return anomalies
```

#### 비즈니스 규칙 기반 탐지
```python
def detect_business_rule_violations(ticket_data):
    """
    비즈니스 규칙 위반 탐지
    """
    violations  = []
    
    # 해결 시간이 생성 시간보다 이른 경우
    if ticket_data['resolved_at'] &lt;  ticket_data['created_at']:
        violations.append("Invalid resolution time")
    
    # 우선순위와 해결 시간 불일치
    if (ticket_data['priority'] == 'Critical' and 
        ticket_data['resolution_time'] > 4):  # 4시간
        violations.append("SLA violation for critical ticket")
    
    return violations
```

## 성능 최적화

:::tip 성능 최적화 전략
데이터 웨어하우스의 성능은 인덱싱, 파티셔닝, 캐싱 전략을 통해 크게 향상시킬 수 있습니다.
:::

### 1. 인덱싱 전략

#### 시간 기반 파티셔닝
```sql
-- 월별 파티셔닝
CREATE TABLE tickets_partitioned (
    id INT,
    created_at DATETIME,
    -- 기타 필드들
) PARTITION BY RANGE (YEAR(created_at) * 100 + MONTH(created_at)) (
    PARTITION p202301 VALUES LESS THAN (202302),
    PARTITION p202302 VALUES LESS THAN (202303),
    PARTITION p202303 VALUES LESS THAN (202304)
);
```

#### 컬럼스토어 인덱스
```sql
-- 분석 쿼리 최적화를 위한 컬럼스토어 인덱스
CREATE COLUMNSTORE INDEX IX_tickets_analytics
ON tickets (created_at, priority, category, status, assigned_to);
```

### 2. 쿼리 최적화

#### 집계 테이블 사전 계산
```sql
-- 시간별 집계 테이블
CREATE MATERIALIZED VIEW hourly_ticket_stats AS
SELECT 
    DATE_FORMAT(created_at, '%Y-%m-%d %H:00:00') as hour_bucket,
    COUNT(*) as ticket_count,
    COUNT(CASE WHEN priority  = 'Critical' THEN 1 END) as critical_count,
    AVG(TIMESTAMPDIFF(MINUTE, created_at, first_response_at)) as avg_response_time
FROM tickets
GROUP BY DATE_FORMAT(created_at, '%Y-%m-%d %H:00:00');
```

#### 캐싱 전략
```python
class AnalyticsCache:
    def __init__(self):
        self.cache  = {}
        self.cache_ttl  = {}
    
    def get_cached_result(self, query_hash):
        """
        캐시된 쿼리 결과 조회
        """
        if query_hash in self.cache:
            if time.time() &lt;  self.cache_ttl[query_hash]:
                return self.cache[query_hash]
            else:
                # 만료된 캐시 제거
                del self.cache[query_hash]
                del self.cache_ttl[query_hash]
        
        return None
    
    def cache_result(self, query_hash, result, ttl_seconds=3600):
        """
        쿼리 결과 캐싱
        """
        self.cache[query_hash] =  result
        self.cache_ttl[query_hash] =  time.time() + ttl_seconds
```

## 실시간 스트리밍 처리

### 1. 이벤트 스트리밍 아키텍처

#### Apache Kafka 활용
```python
def setup_kafka_producer():
    """
    Kafka 프로듀서 설정
    """
    producer  =  KafkaProducer(
        bootstrap_servers=['kafka1:9092', 'kafka2:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        compression_type='gzip'
    )
    return producer

def publish_ticket_event(producer, event_type, ticket_data):
    """
    티켓 이벤트 발행
    """
    event  = {
        'event_type': event_type,
        'timestamp': datetime.utcnow().isoformat(),
        'data': ticket_data
    }
    
    producer.send('ticket-events', value=event)
```

### 2. 실시간 집계 처리

#### Apache Spark Streaming
```python
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

def process_real_time_analytics():
    """
    실시간 분석 처리
    """
    spark  =  SparkSession.builder.appName("FreshserviceAnalytics").getOrCreate()
    ssc  =  StreamingContext(spark.sparkContext, 10)  # 10초 배치
    
    # Kafka에서 스트림 생성
    kafka_stream  =  KafkaUtils.createDirectStream(
        ssc, 
        ['ticket-events'], 
        {"metadata.broker.list": "kafka1:9092,kafka2:9092"}
    )
    
    # 실시간 집계 처리
    ticket_counts  =  kafka_stream.map(lambda x: json.loads(x[1])) \
                               .map(lambda event: (event['data']['priority'], 1)) \
                               .reduceByKey(lambda a, b: a + b)
    
    ticket_counts.pprint()
    
    ssc.start()
    ssc.awaitTermination()
```

## 모니터링 및 알림

:::warning 프로덕션 모니터링 필수
ETL 프로세스의 안정적인 운영을 위해 포괄적인 모니터링과 즉시 알림 체계가 반드시 필요합니다.
:::

### 1. ETL 프로세스 모니터링

#### 처리 상태 추적
```python
class ETLMonitor:
    def __init__(self):
        self.metrics  = {
            'extract_count': 0,
            'transform_count': 0,
            'load_count': 0,
            'error_count': 0,
            'processing_time': 0
        }
    
    def log_stage_completion(self, stage, count, duration):
        """
        ETL 단계 완료 로깅
        """
        self.metrics[f'{stage}_count'] =  count
        self.metrics['processing_time'] + =  duration
        
        # 성능 임계값 체크
        if duration > self.get_threshold(stage):
            self.send_alert(f"{stage} stage took {duration}s")
```

### 2. 데이터 품질 알림

#### 자동 알림 시스템
```python
def check_data_quality_and_alert():
    """
    데이터 품질 체크 및 알림
    """
    # 데이터 완결성 체크
    missing_data_pct  =  calculate_missing_data_percentage()
    if missing_data_pct > 5:  # 5% 이상 누락
        send_alert(f"High missing data percentage: {missing_data_pct}%")
    
    # 데이터 지연 체크
    latest_data_time  =  get_latest_data_timestamp()
    current_time  =  datetime.utcnow()
    delay_minutes  = (current_time - latest_data_time).total_seconds() / 60
    
    if delay_minutes > 30:  # 30분 이상 지연
        send_alert(f"Data processing delayed by {delay_minutes} minutes")
```

이러한 체계적인 데이터 웨어하우스와 ETL 프로세스를 통해 Analytics 플랫폼의 안정성과 성능을 보장하고, 정확하고 신속한 분석 결과를 제공할 수 있습니다.

:::success 데이터 아키텍처 완성
강력한 데이터 웨어하우스와 최적화된 ETL 프로세스로 신뢰할 수 있는 분석 환경을 구축하여 비즈니스 인사이트를 극대화하세요.
:::