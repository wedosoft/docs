---
sidebar_position: 19
---

# 표현식 빌더 노드의 함수

표현식 빌더 노드는 날짜, 문자열, 수학, 논리 연산을 수행할 수 있는 다양한 함수를 지원합니다. 이러한 함수들을 워크플로우 컨텍스트의 값들에 활용할 수 있습니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


## 날짜 함수

### 기본 날짜 조작
- **addDays(date, days)**: 지정된 날짜에 일수를 추가합니다
  - 예시: `addDays('2024-01-15', 10)` → '2024-01-25'
- **addHours(date, hours)**: 지정된 날짜에 시간을 추가합니다
  - 예시: `addHours('2024-01-15T10:00:00', 5)` → '2024-01-15T15:00:00'
- **addMinutes(date, minutes)**: 지정된 날짜에 분을 추가합니다
  - 예시: `addMinutes('2024-01-15T10:00:00', 30)` → '2024-01-15T10:30:00'
- **addMonths(date, months)**: 지정된 날짜에 월을 추가합니다
  - 예시: `addMonths('2024-01-15', 3)` → '2024-04-15'
- **addYears(date, years)**: 지정된 날짜에 년을 추가합니다
  - 예시: `addYears('2024-01-15', 2)` → '2026-01-15'

### 날짜 차이 계산
- **daysBetween(date1, date2)**: 두 날짜 사이의 일수를 계산합니다
  - 예시: `daysBetween('2024-01-15', '2024-01-20')` → 5
- **hoursBetween(date1, date2)**: 두 날짜 사이의 시간을 계산합니다
  - 예시: `hoursBetween('2024-01-15T10:00:00', '2024-01-15T15:00:00')` → 5

### 날짜 요소 추출
- **year(date)**: 날짜에서 년도를 추출합니다
  - 예시: `year('2024-01-15')` → 2024
- **month(date)**: 날짜에서 월을 추출합니다
  - 예시: `month('2024-01-15')` → 1
- **day(date)**: 날짜에서 일을 추출합니다
  - 예시: `day('2024-01-15')` → 15
- **dayOfWeek(date)**: 날짜의 요일을 숫자로 반환합니다 (1=일요일, 7=토요일)
  - 예시: `dayOfWeek('2024-01-15')` → 2 (월요일)

### 현재 날짜/시간
- **now()**: 현재 날짜와 시간을 반환합니다
  - 예시: `now()` → '2024-01-15T14:30:00'
- **today()**: 오늘 날짜를 반환합니다
  - 예시: `today()` → '2024-01-15'

## 문자열 함수

### 기본 문자열 조작
- **concat(str1, str2, ...)**: 여러 문자열을 연결합니다
  - 예시: `concat('Hello', ' ', 'World')` → 'Hello World'
- **upper(str)**: 문자열을 대문자로 변환합니다
  - 예시: `upper('hello')` → 'HELLO'
- **lower(str)**: 문자열을 소문자로 변환합니다
  - 예시: `lower('HELLO')` → 'hello'
- **trim(str)**: 문자열 앞뒤의 공백을 제거합니다
  - 예시: `trim(' hello ')` → 'hello'

### 문자열 검색 및 추출
- **substring(str, start, length)**: 문자열의 일부를 추출합니다
  - 예시: `substring('Freshservice', 0, 5)` → 'Fresh'
- **indexOf(str, searchStr)**: 특정 문자열의 위치를 찾습니다
  - 예시: `indexOf('Freshservice', 'service')` → 5
- **contains(str, searchStr)**: 문자열에 특정 문자열이 포함되어 있는지 확인합니다
  - 예시: `contains('Freshservice', 'service')` → true
- **startsWith(str, prefix)**: 문자열이 특정 접두사로 시작하는지 확인합니다
  - 예시: `startsWith('Freshservice', 'Fresh')` → true
- **endsWith(str, suffix)**: 문자열이 특정 접미사로 끝나는지 확인합니다
  - 예시: `endsWith('Freshservice', 'service')` → true

### 문자열 변환
- **replace(str, oldStr, newStr)**: 문자열의 일부를 다른 문자열로 교체합니다
  - 예시: `replace('Hello World', 'World', 'Universe')` → 'Hello Universe'
- **length(str)**: 문자열의 길이를 반환합니다
  - 예시: `length('Freshservice')` → 12

## 수학 함수

### 기본 수학 연산
- **abs(number)**: 절댓값을 반환합니다
  - 예시: `abs(-5)` → 5
- **round(number)**: 가장 가까운 정수로 반올림합니다
  - 예시: `round(3.7)` → 4
- **floor(number)**: 내림 처리합니다
  - 예시: `floor(3.9)` → 3
- **ceil(number)**: 올림 처리합니다
  - 예시: `ceil(3.1)` → 4

### 비교 함수
- **max(num1, num2, ...)**: 최댓값을 반환합니다
  - 예시: `max(5, 10, 3)` → 10
- **min(num1, num2, ...)**: 최솟값을 반환합니다
  - 예시: `min(5, 10, 3)` → 3

### 고급 수학 함수
- **sqrt(number)**: 제곱근을 계산합니다
  - 예시: `sqrt(16)` → 4
- **power(base, exponent)**: 거듭제곱을 계산합니다
  - 예시: `power(2, 3)` → 8

## 논리 함수

### 조건 함수
- **if(condition, trueValue, falseValue)**: 조건에 따라 값을 반환합니다
  - 예시: `if(age &gt; =  18, 'Adult', 'Minor')`
- **isNull(value)**: 값이 null인지 확인합니다
  - 예시: `isNull(description)` → true/false
- **isEmpty(str)**: 문자열이 비어있는지 확인합니다
  - 예시: `isEmpty('')` → true

## 배열 함수

### 배열 조작
- **size(array)**: 배열의 크기를 반환합니다
  - 예시: `size([1, 2, 3])` → 3
- **contains(array, value)**: 배열에 특정 값이 포함되어 있는지 확인합니다
  - 예시: `contains(['apple', 'banana'], 'apple')` → true

## 실제 사용 사례

### 사례 1: 직원 입사일 기반 티켓 마감일 설정
```
addDays('``{{ticket.ri_5_cf_start_date_iso}}``', 12)
```
직원의 입사일에 12일을 추가하여 온보딩 티켓의 마감일을 설정합니다.

### 사례 2: 요청자와 승인자 동일 여부 확인
```
'``{{ticket.actual_requester.reporting_manager.name}}``' == '``{{ticket.requester.name}}``'
```
보고 관리자와 요청자가 동일한지 확인하여 승인 프로세스를 건너뛸지 결정합니다.

### 사례 3: 우선순위 점수 계산
```
if(priority == 'High', 5, if(priority == 'Medium', 3, 1))
```
우선순위에 따라 숫자 점수를 할당합니다.

### 사례 4: 이메일 도메인 추출
```
substring(email, indexOf(email, '@') + 1, length(email))
```
이메일 주소에서 도메인 부분을 추출합니다.

### 사례 5: 근무일 계산 (주말 제외)
```
if(dayOfWeek(dueDate) == 1 || dayOfWeek(dueDate) == 7, 
   addDays(dueDate, 2), 
   dueDate)
```
마감일이 주말인 경우 월요일로 조정합니다.

### 사례 6: 문자열 형식 정리
```
trim(upper(department))
```
부서명의 공백을 제거하고 대문자로 변환합니다.

## 주의사항

1. **날짜 형식**: 날짜를 사용할 때는 ISO 형식('YYYY-MM-DD' 또는 'YYYY-MM-DDTHH:mm:ss')을 사용해야 합니다.

2. **문자열 인용부호**: 문자열과 날짜 값은 작은따옴표('')로 감싸야 합니다.
   - 예시: `'2024-01-15'`, `'Freshservice'`

3. **플레이스홀더 사용**: 워크플로우 컨텍스트의 값을 사용할 때는 플레이스홀더를 활용합니다.
   - 예시: `'``{{ticket.requester.name}}``'`

4. **함수 중첩**: 함수를 중첩하여 복잡한 계산을 수행할 수 있습니다.
   - 예시: `addDays(max(startDate, today()), 30)`

표현식 빌더 노드의 함수들을 효과적으로 활용하면 복잡한 비즈니스 로직을 워크플로우에 구현할 수 있습니다.