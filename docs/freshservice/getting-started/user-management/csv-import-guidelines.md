---
sidebar_position: 17
---

# CSV 요청자 가져오기 가이드라인

:::info 문서 목적
이 문서는 CSV 파일을 통한 요청자 가져오기 작성 규칙과 주의사항을 안내합니다.
:::

## 개요

Freshservice에서 CSV 파일을 통해 요청자 정보를 성공적으로 가져오기 위한 필수 가이드라인입니다. 올바른 형식과 규칙을 준수하면 대량의 요청자 데이터를 오류 없이 효율적으로 관리할 수 있습니다.

## 기본 가이드라인

### 필수 요구사항

:::warning CSV 파일 기본 규칙
1. **첫 번째 행**은 반드시 요청자 필드명이어야 합니다 (예: Name, Email, Phone 등)
2. **기존 이메일 주소**를 가진 요청자는 CSV 데이터로 **덮어쓰기** 됩니다
3. **중복 확인 기준**은 이메일 주소입니다
:::

### 데이터 업데이트 동작

<table>
<thead>
<tr><th>상황</th><th>동작</th><th>주의사항</th></tr>
</thead>
<tbody>
<tr>
  <td>새로운 이메일</td>
  <td>새 요청자 생성</td>
  <td>모든 필수 필드가 포함되어야 함</td>
</tr>
<tr>
  <td>기존 이메일</td>
  <td>기존 정보 업데이트</td>
  <td>기존 데이터가 완전히 덮어쓰여짐</td>
</tr>
<tr>
  <td>빈 필드 값</td>
  <td>해당 필드를 NULL로 설정</td>
  <td>필수 필드는 비워둘 수 없음</td>
</tr>
</tbody>
</table>

## 필수 필드 요구사항

### 필수 조합 규칙

다음 조합 중 **최소 하나**는 반드시 포함되어야 합니다:

1. **이메일 주소** (Email)
2. **이름 + 업무용 전화번호** (Name + Work Phone)  
3. **이름 + 휴대폰 번호** (Name + Mobile Phone)

### 추가 필수 필드

- 요청자/연락처 필드에서 **"양식 제출 시 필수"**로 설정된 모든 커스텀 필드
- 조직의 정책에 따라 설정된 필수 입력 필드들

### 필수 필드 검증 예시

```csv
# ✅ 올바른 예시들
Name,Email,Department
김철수,kim@company.com,개발팀

Name,Work Phone,Department  
이영희,02-1234-5678,마케팅팀

Name,Mobile Phone,Department
박민수,010-9876-5432,영업팀

# ❌ 잘못된 예시들
Name,Department
김철수,개발팀                    # 연락처 정보 누락

Email
kim@company.com                  # 이름 정보 부족 (선택사항이지만 권장)
```

## 필드별 상세 가이드라인

### 보고 관리자 (Reporting Manager)

**입력 규칙:**
- 반드시 **이메일 주소**로 입력해야 합니다
- 이름으로는 입력할 수 없습니다

**처리 방식:**

<table>
<thead>
<tr><th>상황</th><th>시스템 동작</th><th>후속 작업</th></tr>
</thead>
<tbody>
<tr>
  <td>기존 사용자 이메일</td>
  <td>해당 사용자와 연결</td>
  <td>추가 작업 불필요</td>
</tr>
<tr>
  <td>존재하지 않는 이메일</td>
  <td>새 요청자/연락처 자동 생성<br/>모든 필드가 NULL로 설정</td>
  <td>가져오기 후 관리자 정보를<br/>수동으로 업데이트 필요</td>
</tr>
</tbody>
</table>

**예시:**
```csv
Name,Email,Reporting Manager
김철수,kim@company.com,manager@company.com    # ✅ 올바름
이영희,lee@company.com,김 부장                # ❌ 잘못됨 (이름 사용)
```

### 부서/회사 (Department/Company)

:::warning 사전 생성 필수
- **기존에 존재하는 부서/회사**만 지정할 수 있습니다
- 새로운 부서/회사는 가져오기 전에 **관리자 → 부서** 또는 **관리자 → 회사**에서 미리 생성해야 합니다
:::

**처리 결과:**
- 존재하는 부서/회사: 정상 연결
- 존재하지 않는 부서/회사: 해당 필드가 빈 값으로 처리됨

### 위치 및 드롭다운 필드

**입력 규칙:**
- 서비스 데스크에서 해당 필드에 **미리 설정된 선택지**만 사용 가능
- 대소문자 및 띄어쓰기가 정확히 일치해야 합니다

**설정 확인 방법:**
1. **관리자 → 사용자 관리 → 사용자 필드**로 이동
2. 해당 드롭다운 필드 선택
3. 설정된 옵션 목록 확인

### 체크박스 필드

**허용 값:**
- `true` (체크됨)
- `false` (체크 해제됨)

**주의사항:**
- 대소문자 구분: `True`, `FALSE`, `1`, `0` 등은 인식되지 않음
- 빈 값: `false`로 처리됨

### 이메일 필드

**형식 요구사항:**
```
올바른 형식: john@company.com
잘못된 형식: john@company, @company.com, john.company.com
```

**검증 규칙:**
- @ 기호 포함 필수
- 도메인 부분 필수
- 특수문자 제한 준수

### URL 필드

**형식 요구사항:**
```
올바른 형식: 
- http://www.company.com
- https://company.com/profile
- https://github.com/username

잘못된 형식:
- www.company.com (프로토콜 누락)
- company.com (프로토콜 누락)
```

### 날짜 필드

**표준 형식:** `YYYY-MM-DD` (ISO 8601)

**예시:**
```csv
Join Date,Birthday,Last Login
2024-03-15,1990-12-25,2024-01-30   # ✅ 올바름
15/03/2024,25-12-90,30-Jan-24      # ❌ 잘못됨
2024-3-15,1990/12/25,2024.01.30    # ❌ 잘못됨
```

### 전화번호 필드

**권장 형식:**
```csv
Work Phone,Mobile Phone
02-1234-5678,010-9876-5432        # ✅ 한국 형식
+82-2-1234-5678,+82-10-9876-5432  # ✅ 국제 형식
+1-555-123-4567,+1-555-987-6543   # ✅ 미국 형식
```

### 시간대 (Time Zone)

**주요 지원 시간대:**

<table>
<thead>
<tr><th>지역</th><th>시간대 값</th><th>설명</th></tr>
</thead>
<tbody>
<tr><td>한국</td><td><code>Asia/Seoul</code></td><td>한국 표준시 (KST)</td></tr>
<tr><td>일본</td><td><code>Asia/Tokyo</code></td><td>일본 표준시 (JST)</td></tr>
<tr><td>중국</td><td><code>Asia/Shanghai</code></td><td>중국 표준시 (CST)</td></tr>
<tr><td>미국 동부</td><td><code>America/New_York</code></td><td>동부 표준시 (EST)</td></tr>
<tr><td>미국 서부</td><td><code>America/Los_Angeles</code></td><td>태평양 표준시 (PST)</td></tr>
<tr><td>영국</td><td><code>Europe/London</code></td><td>그리니치 표준시 (GMT)</td></tr>
<tr><td>협정세계시</td><td><code>UTC</code></td><td>UTC 표준시</td></tr>
</tbody>
</table>

### 언어 (Language)

**주요 지원 언어:**

<table>
<thead>
<tr><th>언어</th><th>언어 코드</th><th>표시명</th></tr>
</thead>
<tbody>
<tr><td>한국어</td><td><code>ko</code></td><td>한국어</td></tr>
<tr><td>영어</td><td><code>en</code></td><td>English</td></tr>
<tr><td>일본어</td><td><code>ja</code></td><td>日本語</td></tr>
<tr><td>중국어(간체)</td><td><code>zh-CN</code></td><td>简体中文</td></tr>
<tr><td>중국어(번체)</td><td><code>zh-TW</code></td><td>繁體中文</td></tr>
<tr><td>스페인어</td><td><code>es</code></td><td>Español</td></tr>
<tr><td>프랑스어</td><td><code>fr</code></td><td>Français</td></tr>
<tr><td>독일어</td><td><code>de</code></td><td>Deutsch</td></tr>
</tbody>
</table>

## CSV 파일 작성 템플릿

### 기본 템플릿

```csv
Name,Email,Work Phone,Department,Company,Location,Language,Time Zone
김철수,kim@company.com,02-1234-5678,개발팀,본사,서울 본사,ko,Asia/Seoul
이영희,lee@company.com,02-2345-6789,마케팅팀,본사,부산 지사,ko,Asia/Seoul
박민수,park@company.com,02-3456-7890,영업팀,본사,서울 본사,ko,Asia/Seoul
```

### 최소 필수 필드 템플릿

```csv
Name,Email
김철수,kim@company.com
이영희,lee@company.com
박민수,park@company.com
```

### 전화번호 기반 템플릿

```csv
Name,Work Phone,Department
김철수,02-1234-5678,개발팀
이영희,02-2345-6789,마케팅팀
박민수,02-3456-7890,영업팀
```

### 고급 필드 포함 템플릿

```csv
Name,Email,Work Phone,Mobile,Department,Company,Location,Reporting Manager,Join Date,Active,Description
김철수,kim@company.com,02-1234-5678,010-1111-2222,개발팀,본사,서울 본사,manager@company.com,2024-01-15,true,시니어 백엔드 개발자
이영희,lee@company.com,02-2345-6789,010-3333-4444,마케팅팀,본사,부산 지사,director@company.com,2024-02-01,true,디지털 마케팅 전문가
박민수,park@company.com,02-3456-7890,010-5555-6666,영업팀,본사,서울 본사,sales.manager@company.com,2024-03-01,true,기업 영업 담당
```

### 국제 사용자 템플릿

```csv
Name,Email,Work Phone,Department,Language,Time Zone,Location
John Smith,john@company.com,+1-555-123-4567,Engineering,en,America/New_York,New York Office
田中太郎,tanaka@company.com,+81-3-1234-5678,開発部,ja,Asia/Tokyo,Tokyo Office
王小明,wang@company.com,+86-10-8765-4321,工程部,zh-CN,Asia/Shanghai,Beijing Office
```

## 가져오기 전 준비 체크리스트

### 1단계: 파일 준비

#### 파일 형식 검증
- [ ] **파일 형식**: .csv 확장자 사용
- [ ] **인코딩**: UTF-8 또는 UTF-8 BOM 설정
- [ ] **구분자**: 쉼표(,) 사용
- [ ] **텍스트 한정자**: 큰따옴표(") 사용 (필요시)

#### 헤더 검증
- [ ] **첫 번째 행**: 필드명만 포함 (데이터 없음)
- [ ] **필드명 정확성**: Freshservice 표준 필드명 사용
- [ ] **특수문자 제거**: 필드명에 특수문자나 공백 최소화

### 2단계: 데이터 품질 검증

#### 필수 필드 확인
- [ ] **필수 조합**: 이메일 또는 이름+전화번호 조합 확인
- [ ] **빈 값 검증**: 필수 필드에 빈 값이 없는지 확인
- [ ] **커스텀 필수 필드**: 조직에서 설정한 필수 필드 포함

#### 형식 검증
- [ ] **이메일 형식**: `user@domain.com` 형식 준수
- [ ] **날짜 형식**: `YYYY-MM-DD` 형식 통일
- [ ] **전화번호**: 일관된 형식 사용
- [ ] **체크박스**: `true` 또는 `false`만 사용

### 3단계: 참조 데이터 사전 설정

#### 기준 데이터 생성
- [ ] **부서**: 모든 부서를 **관리자 → 부서**에서 미리 생성
- [ ] **회사**: 모든 회사를 **관리자 → 회사**에서 미리 생성  
- [ ] **위치**: 모든 위치를 **관리자 → 위치**에서 미리 생성
- [ ] **드롭다운 옵션**: 커스텀 필드의 모든 선택지 설정

#### 사용자 계정 확인
- [ ] **보고 관리자**: 관리자 이메일이 시스템에 존재하는지 확인
- [ ] **기존 사용자**: 업데이트될 기존 사용자 목록 확인

### 4단계: 백업 및 테스트

#### 데이터 백업
- [ ] **기존 요청자 데이터**: 전체 요청자 목록 내보내기
- [ ] **시스템 설정**: 현재 사용자 필드 설정 스크린샷
- [ ] **권한 설정**: 현재 권한 구조 문서화

#### 테스트 가져오기
- [ ] **소량 테스트**: 5-10개 레코드로 테스트 실행
- [ ] **오류 확인**: 발생한 오류 메시지 분석
- [ ] **결과 검증**: 가져온 데이터 정확성 확인

## 실무 시나리오별 가이드

### 신규 시스템 도입

**상황**: 기존 시스템에서 Freshservice로 완전 이전

**준비 단계:**
1. 기존 시스템에서 모든 사용자 데이터 추출
2. Freshservice 표준 필드에 맞게 데이터 매핑
3. 부서/회사/위치 등 기준 데이터 먼저 생성
4. 단계적 가져오기 (관리자 → 일반 사용자)

**권장 순서:**
```
1. 관리자 계정 먼저 가져오기
2. 부서장/팀장 계정 가져오기  
3. 일반 직원 계정 가져오기
4. 외부 협력업체 계정 가져오기
```

### 조직 개편 반영

**상황**: 부서 통폐합이나 조직 구조 변경

**준비 단계:**
1. 새로운 조직 구조에 맞는 부서/팀 생성
2. 보고 체계 변경사항 반영
3. 기존 사용자 데이터에 새 조직 정보 매핑
4. 권한 구조 재검토

**주의사항:**
- 기존 티켓 이력은 유지됨
- 워크플로 규칙도 함께 업데이트 필요
- 알림 규칙 재확인 필요

### 대량 신입사원 등록

**상황**: 대규모 채용으로 인한 신규 직원 등록

**효율적인 처리 방법:**
1. 인사팀에서 표준 템플릿 제공
2. 입사일 기준으로 배치 처리
3. 임시 비밀번호 일괄 설정
4. 온보딩 프로세스와 연계

**자동화 고려사항:**
- Active 필드를 false로 설정 후 입사일에 활성화
- 환영 이메일 자동 발송 규칙 설정
- 초기 교육 티켓 자동 생성

### 외부 고객사 등록

**상황**: 새로운 고객사와의 계약으로 외부 사용자 등록

**보안 고려사항:**
1. 회사 필드로 내부/외부 구분
2. 제한된 권한으로 계정 생성
3. 특정 서비스만 접근 가능하도록 설정
4. 계약 만료일 추가 (커스텀 필드)

## 오류 해결 가이드

### 파일 관련 오류

<table>
<thead>
<tr><th>오류 메시지</th><th>원인</th><th>해결책</th></tr>
</thead>
<tbody>
<tr>
  <td>"File format not supported"</td>
  <td>CSV가 아닌 다른 형식</td>
  <td>파일을 .csv 형식으로 저장</td>
</tr>
<tr>
  <td>"Encoding error"</td>
  <td>파일 인코딩 문제</td>
  <td>UTF-8 인코딩으로 다시 저장</td>
</tr>
<tr>
  <td>"Header row missing"</td>
  <td>첫 번째 행에 필드명 없음</td>
  <td>첫 번째 행에 정확한 필드명 추가</td>
</tr>
</tbody>
</table>

### 데이터 유효성 오류

<table>
<thead>
<tr><th>오류 메시지</th><th>원인</th><th>해결책</th></tr>
</thead>
<tbody>
<tr>
  <td>"Invalid email format"</td>
  <td>잘못된 이메일 형식</td>
  <td>user@domain.com 형식으로 수정</td>
</tr>
<tr>
  <td>"Required field missing"</td>
  <td>필수 필드 값 누락</td>
  <td>모든 필수 필드에 값 입력</td>
</tr>
<tr>
  <td>"Date format invalid"</td>
  <td>날짜 형식 오류</td>
  <td>YYYY-MM-DD 형식으로 변경</td>
</tr>
<tr>
  <td>"Department not found"</td>
  <td>존재하지 않는 부서</td>
  <td>부서를 먼저 생성하거나 기존 부서명 사용</td>
</tr>
<tr>
  <td>"Invalid dropdown value"</td>
  <td>허용되지 않은 드롭다운 값</td>
  <td>설정된 옵션 중에서 선택</td>
</tr>
</tbody>
</table>

### 권한 관련 오류

<table>
<thead>
<tr><th>오류 메시지</th><th>원인</th><th>해결책</th></tr>
</thead>
<tbody>
<tr>
  <td>"Access denied"</td>
  <td>가져오기 권한 없음</td>
  <td>관리자 권한으로 로그인</td>
</tr>
<tr>
  <td>"Workspace permission required"</td>
  <td>워크스페이스 권한 부족</td>
  <td>해당 워크스페이스 관리자에게 권한 요청</td>
</tr>
</tbody>
</table>

## 성능 최적화 팁

### 대용량 파일 처리

**파일 크기 제한:**
- 권장 크기: 10MB 이하, 10,000행 이하
- 대용량 파일은 여러 개로 분할하여 처리

**분할 전략:**
```
전체 20,000명의 사용자가 있는 경우:
- 파일 1: 1-5,000번 사용자
- 파일 2: 5,001-10,000번 사용자  
- 파일 3: 10,001-15,000번 사용자
- 파일 4: 15,001-20,000번 사용자
```

### 처리 시간 단축

**우선순위 처리:**
1. **관리자 계정**: 먼저 가져오기
2. **핵심 부서**: 우선 처리
3. **일반 사용자**: 마지막 처리

**배치 처리 스케줄:**
- 업무 시간 외 처리 (야간 또는 주말)
- 시스템 부하가 적은 시간대 활용
- 단계별 검증 후 다음 배치 진행

## 품질 관리 체크포인트

### 가져오기 후 검증

#### 데이터 정확성 확인
- [ ] **총 레코드 수**: 예상 개수와 일치하는지 확인
- [ ] **필수 필드**: 모든 필수 필드가 올바르게 입력되었는지 확인
- [ ] **관계 설정**: 보고 관리자, 부서 연결이 정확한지 확인
- [ ] **권한 할당**: 각 사용자의 권한이 올바르게 설정되었는지 확인

#### 기능 테스트
- [ ] **로그인 테스트**: 샘플 사용자로 로그인 가능한지 확인
- [ ] **티켓 생성**: 새 사용자가 티켓을 생성할 수 있는지 확인
- [ ] **알림 발송**: 알림 규칙이 정상 작동하는지 확인
- [ ] **워크플로**: 자동화 규칙이 올바르게 적용되는지 확인

### 롤백 계획

**문제 발생 시 대응:**
1. **즉시 중단**: 추가 가져오기 중단
2. **문제 분석**: 오류 원인 파악
3. **데이터 복구**: 백업 데이터로 복원
4. **재시도 준비**: 수정된 데이터로 재가져오기

## 관련 참고 문서

- [CSV를 통한 요청자 가져오기](./importing-requesters-csv)
- [사용자 맞춤 필드 추가](./adding-custom-fields-users)
- [부서별 커스텀 필드 추가](./adding-custom-fields-departments)
- [요청자 관리 가이드](./managing-requesters)
- [Freshservice 지원 시간대 목록](https://support.freshservice.com/support/solutions/articles/232302-list-of-time-zones-supported-in-freshservice)
- [Freshservice 지원 언어 목록](https://support.freshservice.com/support/solutions/articles/232303-list-of-languages-supported-in-freshservice)
