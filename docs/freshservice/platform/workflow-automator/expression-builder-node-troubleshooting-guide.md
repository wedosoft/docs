---
sidebar_position: 18
---

# 표현식 빌더 노드 문제 해결 가이드

표현식 빌더 노드를 사용할 때 발생할 수 있는 다양한 오류와 해결 방법을 안내합니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


:::warning 표현식 빌더 사용 시 주의사항
- **구문 검증**: 표현식 작성 후 반드시 구문 유효성을 확인하세요
- **테스트 데이터 활용**: 실제 데이터로 테스트하기 전에 샘플 데이터로 검증하세요
- **오류 로그 확인**: 실행 실패 시 상세한 오류 코드를 확인하여 문제를 진단하세요
:::

## 오류 코드 및 해결 방법

### 구문 오류

#### 1501: 표현식이 비어있음
**오류 메시지**: Expression cannot be blank.  
**설명**: 표현식이 비어있을 때 발생합니다.  
**해결**: 유효한 표현식을 입력하세요.

#### 1507: 여는 괄호 누락
**오류 메시지**: Missing '('.  
**설명**: 표현식에서 여는 괄호가 누락되었을 때 발생합니다.  
**예시**: `equals'test','test')` → `equals('test','test')`

#### 1514: 닫는 괄호 누락
**오류 메시지**: Missing ')'.  
**설명**: 표현식에서 닫는 괄호가 누락되었을 때 발생합니다.  
**예시**: `asin(1` → `asin(1)`

#### 1516: 피연산자 간 연산자 누락
**오류 메시지**: Missing Operator between operands.  
**설명**: 두 피연산자 사이에 연산자가 없을 때 발생합니다.  
**예시**: `if(condition1, 'YES', 'NO')if(condition2, 'YES', 'NO')` → `if(condition1, 'YES', 'NO') && if(condition2, 'YES', 'NO')`

### 연산자 관련 오류

#### 1502: 잘못된 연산자
**오류 메시지**: Invalid operator '%s'.  
**설명**: 존재하지 않는 연산자를 사용했을 때 발생합니다.  
**해결**: 지원되는 연산자를 사용하세요.

#### 1504: 피연산자 누락
**오류 메시지**: Operator '%s' : An operand is missing.  
**설명**: 함수에 필요한 피연산자가 누락되었을 때 발생합니다.  
**예시**: `year()` → `year('2024-01-01')`

#### 1509: 예상보다 많은 피연산자
**오류 메시지**: Operator '%s' : Found more operands than expected.  
**설명**: 함수에 필요한 것보다 많은 피연산자를 제공했을 때 발생합니다.  
**예시**: `addDays('2024-01-01', 10, '2024-01-03')` → `addDays('2024-01-01', 10)`

#### 1511: 추가 구분자 발견
**오류 메시지**: Operator '%s' : Found an extra '%c'.  
**설명**: 표현식에 불필요한 구분자(쉼표 등)가 있을 때 발생합니다.  
**예시**: `max(5, 10,)` → `max(5, 10)`

### 피연산자 관련 오류

#### 1503: 잘못된 피연산자
**오류 메시지**: Invalid operand '%s'.  
**설명**: 잘못된 피연산자를 제공했을 때 발생합니다.  
**예시**: `dateTime` 함수에 6개의 피연산자와 시간대가 필요하지만 3개만 제공한 경우

#### 1505: 피연산자 중 하나가 잘못됨
**오류 메시지**: Operator '%s' : One of its operands is invalid.  
**설명**: 피연산자 중 하나의 데이터 타입이 잘못되었을 때 발생합니다.  
**예시**: `max('abc', 10)` → `max(5, 10)` (숫자끼리 비교)

#### 1508: 구분자 누락
**오류 메시지**: Operand '%s' : Missing '%s'.  
**설명**: 피연산자에서 닫는 구분자가 누락되었을 때 발생합니다.  
**예시**: `charAt(#{operand1}, #{operand2)` → `charAt(#{operand1}, #{operand2})`

#### 1510: 잘못된 데이터 타입
**오류 메시지**: Operand '%s' : Invalid data type.  
**설명**: 피연산자의 데이터 타입이 기대되는 타입과 다를 때 발생합니다.  
**예시**: 산술 연산에서 문자열과 숫자를 혼용한 경우

### 반환 타입 오류

#### 1512: 잘못된 반환 타입
**오류 메시지**: Invalid return type for expression.  
**설명**: 함수의 실제 반환 타입과 기대되는 반환 타입이 다를 때 발생합니다.  
**예시**: `abs` 함수는 숫자를 반환하지만 boolean 타입을 기대한 경우

### 수학 연산 오류

#### 1515: 무한대 결과
**오류 메시지**: Operator '%s' : Result of operator is infinitely large.  
**설명**: 연산 결과가 무한대로 큰 값일 때 발생합니다.  
**예시**: `pow(10,308)*pow(10,308)`

#### 1601: 0으로 나누기
**오류 메시지**: Operator '%s' : Second operand's value cannot be 0.  
**설명**: 나누기 연산에서 분모가 0일 때 발생합니다.  
**예시**: `4/0`

### 범위 관련 오류

#### 1641: 음수 인덱스
**오류 메시지**: Operator '%s' : Second operand's value must be &gt; =  0.  
**설명**: 문자열 인덱스가 음수일 때 발생합니다.  
**예시**: `substring('test', -1, 3)` → `substring('test', 0, 3)`

#### 1642: 인덱스 범위 초과
**오류 메시지**: Operator '%s' : Third operand's value must be &lt; =  first operand's length.  
**설명**: 문자열 길이를 초과하는 인덱스를 사용할 때 발생합니다.  
**예시**: `substring('test', 3, 7)` → `substring('test', 3, 4)`

#### 1643: 잘못된 인덱스 순서
**오류 메시지**: Operator '%s' : Third operand's value must be > second operand's value.  
**설명**: 종료 인덱스가 시작 인덱스보다 작을 때 발생합니다.  
**예시**: `substring('test', 2, 1)` → `substring('test', 1, 3)`

#### 1661: 문자 인덱스 범위 오류
**오류 메시지**: Operator '%s' : Second operand's value must be &gt; =  0 and &lt;  first operand's length.  
**설명**: 문자열에서 존재하지 않는 위치의 문자를 가져오려 할 때 발생합니다.  
**예시**: `charAt('test', 4)` → `charAt('test', 3)`

#### 1681: 삼각함수 범위 오류
**오류 메시지**: Operator '%s' : Operand's value must be &gt; = -1 and &lt; =  1.  
**설명**: 역삼각함수의 입력값이 유효 범위를 벗어날 때 발생합니다.  
**예시**: `asin(54.8)` → `asin(0.5)`

#### 1741: 길이 범위 오류
**오류 메시지**: Operator '%s' : Operand value must be &gt; =  1 and &lt;=18.  
**설명**: `randomNumberOfLength` 함수에서 유효하지 않은 길이를 지정할 때 발생합니다.  
**예시**: `randomNumberOfLength(19)` → `randomNumberOfLength(10)`

### 조건문 오류

#### 1701: Boolean 타입 필요
**오류 메시지**: Operator '%s' : First operand of the function must be of boolean type.  
**설명**: `if` 함수의 첫 번째 피연산자가 boolean이 아닐 때 발생합니다.  
**예시**: `if(5, 'abc', 'def')` → `if(5 > 3, 'abc', 'def')`

#### 1702: 타입 불일치
**오류 메시지**: Operator '%s' : Second and third operands value must be of same type.  
**설명**: `if` 함수의 두 번째와 세 번째 피연산자의 타입이 다를 때 발생합니다.  
**예시**: `if(true, false, 9.50)` → `if(true, 'yes', 'no')`

### 날짜/시간 오류

#### 1721: 잘못된 날짜
**오류 메시지**: Operator '%s' : %s  
**설명**: 존재하지 않는 날짜를 생성하려 할 때 발생합니다.  
**예시**: `dateTime(2019, 2, 30, 3, 3, 3, 'Australia/Sydney')` → `dateTime(2019, 2, 28, 3, 3, 3, 'Australia/Sydney')`

#### 1722: 잘못된 시간대
**오류 메시지**: Operator '%s' : Invalid timezone.  
**설명**: 유효하지 않은 시간대를 지정할 때 발생합니다.  
**해결**: 올바른 시간대 형식을 사용하세요 (예: 'Asia/Seoul', 'America/New_York')

### 캐스팅 오류

#### 1517: 지원되지 않는 캐스팅
**오류 메시지**: castOperandTypes meta does not support provided '%s' casting information  
**설명**: 지원되지 않는 데이터 타입 캐스팅을 시도할 때 발생합니다.  
**지원되는 캐스팅**:
- `"text":["boolean"]`
- `"text":["number"]` 
- `"text":["boolean", "number"]`

## 문제 해결 팁

### 1. 데이터 타입 확인
- 문자열은 작은따옴표로 감싸세요: `'Hello World'`
- 날짜는 ISO 형식을 사용하세요: `'2024-01-15'`
- Boolean 값은 `true` 또는 `false`를 사용하세요

### 2. 함수 매개변수 확인
- 각 함수가 요구하는 매개변수 개수와 타입을 확인하세요
- 필수 매개변수가 누락되지 않았는지 확인하세요

### 3. 괄호와 구분자 확인
- 모든 여는 괄호에 대응하는 닫는 괄호가 있는지 확인하세요
- 쉼표, 세미콜론 등의 구분자가 올바른 위치에 있는지 확인하세요

### 4. 범위 확인
- 배열이나 문자열의 인덱스가 유효한 범위 내에 있는지 확인하세요
- 수학 함수의 입력값이 허용 범위 내에 있는지 확인하세요

### 5. 테스트 표현식 활용
- 표현식 빌더의 "테스트 표현식" 기능을 사용하여 샘플 값으로 검증하세요
- 복잡한 표현식은 단계별로 나누어 테스트하세요

이 가이드를 참조하여 표현식 빌더 노드에서 발생하는 오류를 신속하게 해결할 수 있습니다.