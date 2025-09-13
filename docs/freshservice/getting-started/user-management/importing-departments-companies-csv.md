---
sidebar_position: 20
---

# CSV를 통한 부서/회사 가져오기

:::info 문서 목적
이 문서는 CSV 파일을 통한 부서/회사 가져오기 방법을 안내합니다.
:::

## 개요

부서/회사를 수동으로 하나씩 추가하는 대신, **CSV 파일**을 사용하여 기존 시스템에서 데이터를 일괄 가져올 수 있습니다. 이전 설정이나 애플리케이션에서 데이터를 내보내어 CSV 파일 형태로 Freshservice에 업로드하면 됩니다.

## CSV 파일 요구사항

### 기본 요구사항

1. **CSV 형식**: 올바르게 형식화된 CSV 파일이어야 합니다 (다른 형식은 지원되지 않음)
2. **첫 번째 행**: 필드명이 포함되어야 합니다 (예: Department Name, Description)
3. **인코딩**: UTF-8 인코딩을 권장합니다

### 지원되는 필드 정보

<table>
<thead>
<tr><th>속성</th><th>타입</th><th>필수여부</th><th>설명</th><th>예시</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>부서/회사명</strong></td>
  <td>문자열</td>
  <td><span style={{ color: 'red' }}>✅ 필수</span></td>
  <td>부서 또는 회사의 이름</td>
  <td>인사팀</td>
</tr>
<tr>
  <td><strong>부서/회사 책임자</strong></td>
  <td>문자열</td>
  <td>선택</td>
  <td>부서 또는 회사의 책임자</td>
  <td>manager@company.com</td>
</tr>
<tr>
  <td><strong>주 사용자</strong></td>
  <td>문자열</td>
  <td>선택</td>
  <td>부서/회사의 주 사용자 이메일</td>
  <td>admin@company.com</td>
</tr>
<tr>
  <td><strong>설명</strong></td>
  <td>문자열</td>
  <td>선택</td>
  <td>부서 또는 회사에 대한 설명</td>
  <td>인적 자원 관리</td>
</tr>
<tr>
  <td><strong>도메인</strong></td>
  <td>문자열 배열</td>
  <td>선택</td>
  <td>부서/회사와 연결된 이메일 도메인</td>
  <td>company.com</td>
</tr>
</tbody>
</table>

## CSV 파일 작성 예시

### 기본 템플릿

```csv
Department Name,Description,Department Head,Prime User,Domains
인사팀,인적 자원 관리,hr.manager@company.com,hr.admin@company.com,company.com
개발팀,소프트웨어 개발,dev.manager@company.com,dev.admin@company.com,company.com
마케팅팀,마케팅 및 홍보,marketing.manager@company.com,marketing.admin@company.com,company.com
영업팀,고객 영업 및 관리,sales.manager@company.com,sales.admin@company.com,company.com
```

### 회사 정보 템플릿

```csv
Company Name,Description,Company Head,Prime User,Domains
본사,주식회사 본사,ceo@mainoffice.com,admin@mainoffice.com,mainoffice.com
지사,서울 지사,branch.manager@branch.com,branch.admin@branch.com,branch.com
```

### 복합 도메인 예시

```csv
Department Name,Description,Domains
IT부서,정보기술 관리,"company.com,tech.company.com"
고객서비스,고객 지원 서비스,"support.company.com,help.company.com"
```

## 부서/회사 가져오기 단계

### 1단계: 부서/회사 관리 페이지 접근

1. **관리자 → 사용자 관리 → 부서/회사**로 이동합니다.
2. 계정에 여러 워크스페이스가 있는 경우:
   - **관리자 → 전역 설정 → 사용자 관리 → 부서/회사**로 이동합니다.

### 2단계: CSV 파일 선택

1. **'CSV 파일 선택'** 버튼을 클릭합니다.
2. 준비된 CSV 파일을 선택하여 업로드합니다.

### 3단계: 필드 매핑

1. CSV 파일의 필드를 Freshservice의 해당 부서/회사 필드와 매핑합니다.
2. 매핑이 완료되면 **가져오기** 버튼을 클릭합니다.

### 4단계: 가져오기 결과 확인

1. **관리자 → 전역 설정 → 사용자 관리 → 부서/회사**로 이동합니다.
2. 새로 가져온 부서/회사가 목록에 표시되는지 확인합니다.

## 가져오기 전 체크리스트

### 데이터 준비
- [ ] CSV 파일 형식이 올바른지 확인
- [ ] 첫 번째 행에 필드명이 정확히 입력되었는지 확인
- [ ] 필수 필드(부서/회사명)가 모든 행에 포함되었는지 확인
- [ ] 이메일 주소 형식이 올바른지 확인

### 중복 확인
- [ ] 기존 부서/회사와 중복되는 이름이 없는지 확인
- [ ] 동일한 도메인을 여러 부서에서 사용하지 않는지 확인

### 백업 및 테스트
- [ ] 기존 부서/회사 설정 백업 완료
- [ ] 소량 데이터로 테스트 가져오기 수행

## 주의사항 및 팁

### 데이터 정확성

:::warning 필수 필드 확인
- 부서/회사명은 반드시 입력해야 하는 필수 필드입니다.
- 빈 값이나 중복된 이름은 가져오기 오류를 발생시킵니다.
:::

### 이메일 도메인 설정

:::tip 도메인 형식
- 여러 도메인을 지정할 때는 쉼표로 구분하여 입력합니다.
- 예: "company.com,subsidiary.company.com"
:::

### 기존 데이터와의 관계

:::warning 덮어쓰기 주의
- 동일한 이름의 부서/회사가 이미 존재하면 기존 데이터가 업데이트됩니다.
- 중요한 기존 설정이 손실될 수 있으므로 사전에 백업하세요.
:::

## 문제 해결

### 가져오기 실패 시 확인사항

| 오류 상황 | 원인 | 해결책 |
|-----------|------|--------|
| "Invalid CSV format" | 잘못된 CSV 형식 | 파일을 CSV 형식으로 다시 저장 |
| "Missing required field" | 필수 필드 누락 | 부서/회사명이 모든 행에 있는지 확인 |
| "Duplicate name" | 중복된 이름 | 기존 부서/회사와 다른 이름 사용 |
| "Invalid email format" | 잘못된 이메일 형식 | 이메일 주소 형식 재확인 |

### 부분적 가져오기 실패

- 일부 행만 실패한 경우, 오류 메시지를 확인하여 해당 행을 수정
- 성공한 행은 그대로 유지되므로 실패한 행만 별도로 처리
- 오류 로그를 참조하여 구체적인 문제점 파악

## 관련 문서

- [CSV 가져오기 가이드라인](./csv-import-guidelines.md)
- [CSV를 통한 요청자 가져오기](./importing-requesters-csv.md)
- [요청자 관리](./managing-requesters.md)
- [사용자 맞춤 필드 추가](./adding-custom-fields-users.md)
