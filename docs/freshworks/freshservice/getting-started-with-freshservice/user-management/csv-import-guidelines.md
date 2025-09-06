---
id: csv-import-guidelines
title: CSV 가져오기 가이드라인
sidebar_label: CSV 가져오기 가이드라인
---

<div class="subtitle">
  이 문서는 "CSV 파일을 통한 요청자 가져오기(CSV Import Guidelines)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 개요

CSV 파일을 통해 요청자 정보를 일괄 가져올 때 준수해야 할 가이드라인을 제공합니다. 올바른 형식을 따르면 대량의 요청자 데이터를 효율적으로 관리할 수 있습니다.

## 일반 가이드라인

### 기본 요구사항

- **첫 번째 행**에는 반드시 요청자 필드명이 포함되어야 합니다 (예: Name, Email 등)
- **기존 이메일 주소**가 있는 요청자의 경우, 현재 정보가 CSV 데이터로 덮어쓰여집니다

> **데이터 백업 권장**
> 가져오기 작업 전에 기존 요청자 데이터를 백업하는 것을 권장합니다.

## 필수 필드 요구사항

### 필수 조합 중 하나 선택

다음 조합 중 **하나 이상**을 반드시 포함해야 합니다:

1. **이메일 주소**
2. **이름 + 업무용 전화번호**
3. **이름 + 휴대폰 번호**

### 추가 필수 필드

요청자/연락처 필드에서 **"양식 제출 시 필수"**로 표시된 모든 속성도 가져오기 시 필수로 간주됩니다.

## 필드별 세부 가이드라인

### 보고 관리자 (Reporting Manager)

<table>
<thead>
<tr><th>상황</th><th>처리 방식</th></tr>
</thead>
<tbody>
<tr>
  <td>기존 관리자 지정</td>
  <td>정상적으로 연결됩니다</td>
</tr>
<tr>
  <td>존재하지 않는 관리자</td>
  <td>제공된 이메일 주소로 새 요청자/연락처가 생성됩니다<br/>
  다른 모든 필드(필수 필드 포함)는 NULL로 설정되며<br/>
  가져오기 완료 후 수동으로 업데이트해야 합니다</td>
</tr>
</tbody>
</table>

### 부서/회사 (Department/Company)

- **기존에 존재하는 부서/회사**만 지정할 수 있습니다
- 새로운 부서/회사는 미리 생성해야 합니다

### 위치 및 드롭다운 필드

- 서비스 데스크에서 해당 필드에 **미리 설정된 선택지**만 사용할 수 있습니다
- 잘못된 값은 가져오기 오류를 발생시킵니다

### 체크박스 필드

- **허용 값**: `true` 또는 `false`만 입력 가능
- 대소문자를 구분하므로 정확히 입력해야 합니다

### 이메일 필드

- **형식**: `john@freshservice.com`
- 유효한 이메일 형식을 준수해야 합니다

### URL 필드

- **형식**: `http://www.freshservice.com/` 또는 `https://www.example.com/`
- 프로토콜(http:// 또는 https://)을 반드시 포함해야 합니다

### 날짜 필드

- **형식**: `YYYY-MM-DD` (예: 2024-03-15)
- ISO 8601 표준 날짜 형식을 사용합니다

### 시간대 (Time Zone)

Freshservice에서 지원하는 시간대 목록에서 선택해야 합니다. 주요 시간대:

- `Asia/Seoul` - 한국 표준시
- `UTC` - 협정 세계시
- `America/New_York` - 동부 표준시
- `Europe/London` - 그리니치 표준시

### 언어 (Language)

Freshservice에서 지원하는 언어 목록에서 선택해야 합니다. 주요 언어:

- `ko` - 한국어
- `en` - 영어
- `ja` - 일본어
- `zh` - 중국어

## CSV 파일 작성 예시

### 기본 템플릿

```csv
Name,Email,Phone,Department,Location,Language,Time Zone
김철수,kim@company.com,02-1234-5678,개발팀,서울 본사,ko,Asia/Seoul
이영희,lee@company.com,02-2345-6789,마케팅팀,부산 지사,ko,Asia/Seoul
박민수,park@company.com,02-3456-7890,영업팀,서울 본사,ko,Asia/Seoul
```

### 고급 필드 포함 템플릿

```csv
Name,Email,Phone,Department,Company,Reporting Manager,Status,Join Date
김철수,kim@company.com,02-1234-5678,개발팀,본사,manager@company.com,true,2024-01-15
이영희,lee@company.com,02-2345-6789,마케팅팀,본사,director@company.com,true,2024-02-01
```

## 가져오기 전 체크리스트

### 파일 준비
- [ ] CSV 파일 인코딩이 UTF-8인지 확인
- [ ] 첫 번째 행에 필드명이 올바르게 입력되었는지 확인
- [ ] 필수 필드 조합이 모든 행에 포함되었는지 확인

### 데이터 검증
- [ ] 이메일 형식이 올바른지 확인
- [ ] 날짜 형식이 YYYY-MM-DD인지 확인
- [ ] 드롭다운 값이 시스템에 존재하는지 확인
- [ ] 부서/회사가 미리 생성되었는지 확인

### 백업 및 테스트
- [ ] 기존 데이터 백업 완료
- [ ] 소량 데이터로 테스트 가져오기 수행
- [ ] 오류 발생 시 롤백 계획 수립

## 문제 해결

### 일반적인 오류와 해결책

| 오류 메시지 | 원인 | 해결책 |
|------------|------|--------|
| "Invalid email format" | 잘못된 이메일 형식 | 이메일 형식을 다시 확인하고 수정 |
| "Department not found" | 존재하지 않는 부서 | 부서를 미리 생성하거나 기존 부서명 사용 |
| "Invalid date format" | 잘못된 날짜 형식 | YYYY-MM-DD 형식으로 수정 |
| "Required field missing" | 필수 필드 누락 | 필수 필드를 모든 행에 추가 |

## 관련 문서

- [CSV를 통한 요청자 가져오기](./importing-requesters-csv.md)
- [CSV를 통한 부서/회사 가져오기](./importing-departments-companies-csv.md)
- [요청자 관리](./managing-requesters.md)
- [사용자 맞춤 필드 추가](./adding-custom-fields-users.md)
