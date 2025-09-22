---
sidebar_position: 5
---

# CSV 파일로 요청자 가져오기

:::info 문서 목적
이 문서는 CSV 파일을 사용해서 요청자를 일괄 가져오는 방법을 안내하는 문서입니다.
:::

## 개요

요청자를 수동으로 하나씩 추가하는 대신 기존 연락처 데이터를 CSV 파일을 통해 일괄 가져올 수 있어요. 이전 시스템이나 애플리케이션에서 연락처를 CSV 파일로 내보내 Freshservice에 업로드하면 돼요.

:::info 중요 사항
- CSV 형식만 지원 (다른 형식 지원 안 함)
- 기존 요청자 프로필의 대량 업데이트도 가능
- 이메일 주소를 기준으로 중복 확인 및 업데이트
:::

## CSV 파일 준비 요구사항

### 1단계: 파일 형식 확인

다음 요구사항을 충족하는 CSV 파일을 준비해야 해요:

1. **올바른 CSV 형식**: 쉼표로 구분된 값 형식이어야 해요.
2. **헤더 행 필수**: 첫 번째 행에는 필드명이 포함되어야 합니다 (Name, Email, Job Title, Description 등).

### 2단계: 필수 및 권장 필드

| 필드명 | 필수 여부 | 설명 | 예시 |
|--------|-----------|------|------|
| Name | 필수 | 요청자 전체 이름 | 김철수 |
| Email | 필수 | 고유한 이메일 주소 | kim@company.com |
| Job Title | 권장 | 직급 또는 직책 | 시니어 개발자 |
| Phone | 선택 | 업무용 전화번호 | 02-1234-5678 |
| Mobile | 선택 | 휴대폰 번호 | 010-1234-5678 |
| Department | 권장 | 소속 부서 | 개발팀 |
| Company | 선택 | 소속 회사 | 본사 |
| Location | 선택 | 근무 위치 | 서울 본사 |

## 요청자 가져오기 프로세스

### 1단계: 가져오기 페이지 접속

**단일 워크스페이스인 경우:**
**관리자 → 사용자 관리 → 요청자**로 이동해요.

**다중 워크스페이스인 경우:**
**관리자 → 글로벌 설정 → 사용자 관리 → 요청자**로 이동해요.

**가져오기** 링크를 클릭하고 **CSV에서 가져오기**를 선택해요.

![CSV 가져오기 옵션](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35631581/original/IF9o6-87YQpvnOQS-Wqzrr9prUNvrO9eBw.png?1509086975)

### 2단계: CSV 파일 업로드

1. **파일 선택** 버튼을 클릭해서 준비한 CSV 파일을 선택해요.
2. 페이지에 표시된 지침을 확인한 후 **가져오기** 버튼을 클릭해요.

![CSV 파일 선택 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35631584/original/UstfSgJfJgHtmxUvazmKiIbKKEEFjrmNGg.png?1509086984)

### 3단계: 필드 매핑

CSV 파일의 필드를 Freshservice의 해당 요청자 필드와 매핑해요. 시스템이 자동으로 유사한 필드를 매핑하지만, 수동으로 조정할 수 있어요.

![필드 매핑 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011179377/original/3esC6RF_Z3xOGMhm2fm-fLkFIoYqrIQIRQ.png?1710085545)

#### 중요한 필드 매핑 참고사항
- **'active' 필드**: 요청자 프로필의 활성화/비활성화 상태를 나타냅니다.
- **이메일 필드**: 중복 확인 및 업데이트의 기준이 돼요.

### 4단계: 가져오기 실행 및 확인

매핑이 완료되면 **가져오기** 버튼을 클릭해요.

![가져오기 결과 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/35631594/original/lY-0QSNSj0N3oZi4eszpAo_q5z44FgPpAQ.png?1509087018)

완료 후 **관리자 → 사용자 관리 → 요청자**에서 새로운 요청자들을 확인할 수 있어요. 가져온 요청자들은 티켓 생성 시에도 즉시 사용할 수 있어요.

## 특별 주의사항

### 보고 관리자 필드

:::warning 보고 관리자 설정 주의
**보고 관리자** 필드에는 반드시 이메일 주소를 사용해야 해요. 이름을 사용하면 해당 필드가 가져오기되지 않어요.

✅ 올바른 예: `manager@company.com`  
❌ 잘못된 예: `김 관리자`
:::

### 위치 정보 사전 설정

:::warning 위치 사전 생성 필요
가져오기 전에 **관리자 → 위치**에서 모든 위치를 미리 생성해야 해요. 존재하지 않는 위치는 빈 값으로 처리돼요.
:::

## CSV 파일 예시

### 기본 템플릿
```csv
Name,Email,Job Title,Phone,Department,Active
김철수,kim@company.com,시니어 개발자,02-1234-5678,개발팀,true
이영희,lee@company.com,마케팅 매니저,02-2345-6789,마케팅팀,true
박민수,park@company.com,영업 담당,02-3456-7890,영업팀,true
```

### 확장 필드 포함 템플릿
```csv
Name,Email,Job Title,Work Phone,Mobile,Department,Company,Location,Reporting Manager,Active,Description
김철수,kim@company.com,시니어 개발자,02-1234-5678,010-1234-5678,개발팀,본사,서울 본사,dev.manager@company.com,true,10년 경력 백엔드 개발자
이영희,lee@company.com,마케팅 매니저,02-2345-6789,010-2345-6789,마케팅팀,본사,서울 본사,marketing.manager@company.com,true,디지털 마케팅 전문가
```

## 대량 업데이트 활용

이 가져오기 기능은 기존 요청자 프로필의 대량 업데이트에도 사용할 수 있어요. 동일한 이메일 주소가 있는 경우 기존 데이터가 업데이트돼요.

### 업데이트 전용 템플릿
```csv
Email,Department,Location,Active
kim@company.com,신기술팀,판교 사무소,true
lee@company.com,브랜드팀,강남 사무소,true
park@company.com,기업영업팀,서울 본사,false
```

