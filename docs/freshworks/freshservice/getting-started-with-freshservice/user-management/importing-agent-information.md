---
id: importing-agent-information
title: 상담원 정보 가져오기 가이드
sidebar_label: 상담원 정보 가져오기 가이드
---

<div className="subtitle">
  이 문서는 Freshservice에서 CSV 파일을 사용하여 상담원 정보를 일괄 가져오는 방법을 안내하는 문서입니다.
</div>

## 상담원 정보 가져오기 방법

### 1단계: 가져오기 페이지 접속

**단일 워크스페이스:**
- **Admin** → **User Management** → **Agents**로 이동한 후 **Import** 클릭

**멀티 워크스페이스:**
- **Admin** → **Global Settings** → **User Management** → **Agents**로 이동한 후 **Import** 클릭

![상담원 가져오기 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/38061766/original/wS35PbIZwEzuYAxYCqS7mLxoDrlM7nvKqw.png?1522912523)

### 2단계: CSV 파일 업로드

1. "Import Agents" 패널이 화면에 표시됩니다
2. CSV 파일을 선택하거나 파일 업로드 영역에 **드래그 앤 드롭**합니다
3. **Upload** 버튼을 클릭합니다

:::warning 파일 형식 제한
CSV 형식만 지원됩니다. 다른 형식은 지원되지 않습니다.
:::

![CSV 파일 업로드](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000691461/original/C51vmoeK_N8uC_xjr28NwhTaUL9ue9rWxQ.png?1581056647)

### 3단계: 필드 매핑

1. 상담원 속성을 CSV 파일의 컬럼 헤더에 매핑합니다
2. 매핑이 완료되면 **Import** 버튼을 클릭합니다

### 4단계: 가져오기 완료

가져오기 프로세스가 완료되면 결과 요약이 표시됩니다.

## 가져올 수 있는 필드

<table>
<thead>
<tr><th>필드</th><th>설명</th><th>가능한 값</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>Full Name</strong></td>
  <td>상담원 이름</td>
  <td>모든 텍스트</td>
</tr>
<tr>
  <td><strong>Email</strong></td>
  <td>기본 이메일 주소 (필수)</td>
  <td>username@domain.ext 형식의 유효한 이메일 주소</td>
</tr>
<tr>
  <td><strong>Occasional</strong></td>
  <td>임시 상담원 또는 정규 상담원 구분</td>
  <td>FALSE (정규 상담원)<br/>TRUE (임시 상담원)</td>
</tr>
<tr>
  <td><strong>Title</strong></td>
  <td>직함</td>
  <td>모든 텍스트</td>
</tr>
<tr>
  <td><strong>Work Phone</strong></td>
  <td>직장 전화번호</td>
  <td>모든 텍스트</td>
</tr>
<tr>
  <td><strong>Mobile Phone</strong></td>
  <td>휴대폰 번호</td>
  <td>모든 텍스트</td>
</tr>
<tr>
  <td><strong>Location</strong></td>
  <td>상담원 위치</td>
  <td>Admin → Asset Management → Locations의 위치명</td>
</tr>
<tr>
  <td><strong>Reporting Manager</strong></td>
  <td>보고 관리자의 기본 이메일 주소</td>
  <td>username@domain.ext 형식의 유효한 이메일 주소<br/><em>(존재하지 않는 경우 요청자/연락처로 생성됨)</em></td>
</tr>
<tr>
  <td><strong>Groups</strong></td>
  <td>상담원이 속할 그룹 (복수 값 지원)</td>
  <td>Admin → User Management → Groups → Agent Groups의 그룹명</td>
</tr>
<tr>
  <td><strong>Roles</strong></td>
  <td>상담원에게 할당할 기본 및 사용자 정의 역할 (복수 값 지원)</td>
  <td><a href="https://support.freshservice.com/en/support/solutions/articles/50000005577-understanding-roles-for-agents" target="_blank">상담원 역할 이해하기</a></td>
</tr>
<tr>
  <td><strong>Time Zone</strong><br/><em>(Growth, Pro, Enterprise 플랜)</em></td>
  <td>상담원이 근무하는 시간대</td>
  <td><a href="https://support.freshservice.com/support/solutions/articles/232302-list-of-time-zones-supported-in-freshservice" target="_blank">Freshservice 지원 시간대 목록</a></td>
</tr>
<tr>
  <td><strong>Language</strong><br/><em>(Growth, Pro, Enterprise 플랜)</em></td>
  <td>상담원에게 표시되는 Freshservice 인터페이스 언어</td>
  <td><a href="https://support.freshservice.com/support/solutions/articles/232303-list-of-languages-supported-in-freshservice" target="_blank">Freshservice 지원 언어 목록</a></td>
</tr>
<tr>
  <td><strong>Level</strong><br/><em>(리더보드 기능 활성화 시)</em></td>
  <td>Arcade 모듈에서 상담원이 달성한 레벨</td>
  <td>Beginner<br/>Intermediate<br/>Professional<br/>Expert<br/>Master<br/>Guru</td>
</tr>
</tbody>
</table>

## CSV 파일 준비 가이드

### 필수 요구사항

- **파일 형식**: CSV (.csv)
- **인코딩**: UTF-8 권장
- **필수 필드**: Email (이메일 주소)

### CSV 파일 예시

```csv
Full Name,Email,Occasional,Title,Work Phone,Mobile Phone,Location,Groups,Roles
홍길동,hong@company.com,FALSE,시니어 상담원,02-1234-5678,010-1234-5678,서울 사무소,IT Support,Agent
김영희,kim@company.com,TRUE,주니어 상담원,02-1234-5679,010-1234-5679,부산 사무소,HR Support,Agent
```

### 복수 값 처리

그룹이나 역할 같이 여러 값이 있는 경우 쉼표로 구분합니다:

```csv
Groups,Roles
"IT Support, Network Team","Agent, Supervisor"
```

## 가져오기 모범 사례

### 사전 준비

1. **데이터 검증**: 이메일 주소 형식 및 중복 확인
2. **참조 데이터 확인**: 그룹, 역할, 위치 등이 시스템에 존재하는지 확인
3. **백업**: 기존 데이터 백업 후 진행

### 오류 방지

- **중복 이메일**: 이미 존재하는 이메일 주소 확인
- **잘못된 참조**: 존재하지 않는 그룹이나 역할 참조 방지
- **형식 오류**: 각 필드의 올바른 형식 준수

### 대용량 처리

- **배치 처리**: 대량의 데이터는 여러 번에 나누어 처리
- **테스트 실행**: 소량의 테스트 데이터로 먼저 검증
- **단계적 적용**: 부서별 또는 팀별로 단계적 가져오기

:::info 유용한 팁
- 가져오기 전에 소량의 테스트 데이터로 먼저 시도해보세요
- 오류 발생 시 오류 메시지를 확인하여 문제를 해결하세요
- 정기적인 데이터 동기화를 위해 자동화 도구 사용을 고려하세요
:::

:::warning 주의사항
- 가져오기는 되돌릴 수 없으므로 신중하게 진행하세요
- 민감한 정보가 포함된 CSV 파일은 안전하게 보관하세요
- 가져오기 후 데이터 정확성을 반드시 확인하세요
:::

## 관련 문서

- [상담원 정보 내보내기](./exporting-agent-information)
- [상담원 역할 및 권한 설정](./setting-agent-roles-permissions)
- [상담원 그룹 생성 및 관리](./create-manage-agent-groups)
- [상담원 이해하기](./understanding-agents)
