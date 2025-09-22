---
sidebar_position: 14
---

# 연락처-회사 자동 연결

:::info 문서 목적
이 문서는 이메일 도메인을 기반으로 연락처를 회사에 자동으로 연결하는 기능의 설정과 활용을 안내하는 문서입니다.
:::

새로운 연락처를 이메일 도메인을 기반으로 회사에 자동으로 연결하는 기능입니다. 요청자가 생성될 때 이메일 주소의 도메인을 확인해서 해당 회사로 자동 배정돼요.

## 기본 개념

연락처가 `cedric.diggory@hogwarts.edu` 이메일로 생성되면, `hogwarts.edu` 도메인을 기반으로 Hogwarts 회사에 자동으로 연결돼요.

:::info 적용 범위
- 새로 생성되는 연락처에만 적용
- 기존 연락처에 새 이메일 추가 시에도 적용
- 기존 연락처는 소급 적용되지 않음
:::

## 설정 방법

### 1단계: 회사 관리 페이지 접속

1. **Admin** → **User Management** → **Companies**로 이동
2. 자동 연결을 설정할 회사 찾기

![회사 관리 페이지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965545/original/74fJSRdz8uUsRmbymeCaIV9XL_zkG2IIsg.png?1547785433)

### 2단계: 회사 편집

회사 옆의 **편집 아이콘** 클릭

![회사 편집 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965548/original/C5RYpAIUY7D1j4NanniXTp1M_hJY4z7anA.png?1547785455)

### 3단계: 도메인 추가

1. **"Domains"** 입력 필드로 스크롤
2. 연결할 이메일 도메인 입력
3. **스페이스** 또는 **엔터**로 도메인 추가

![도메인 입력 필드](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/43191011/original/zGm7pJzRAhDthFlWY2Xonz1sSCmoD40hcQ.png?1548764644)

### 4단계: 저장

**"Update"** 버튼으로 변경사항 저장

![업데이트 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965979/original/NXCY2Zvy4rQ9xqzwucc_Sdmn5nHaByjnpg.png?1547786855)

## 작동 방식

| 상황 | 자동 연결 여부 |
|------|----------------|
| 새 연락처 생성 | ✅ 자동 연결 |
| 기존 연락처에 새 이메일 추가 | ✅ 자동 연결 |
| 기존 연락처 (설정 이전) | ❌ 연결 안됨 |

:::warning 연결 해제 주의사항
회사에서 도메인을 제거해도 이미 연결된 사용자는 자동으로 연결 해제되지 않어요.
:::

## 활용 사례

### 조직별 관리
- **대기업**: 부서별 이메일 도메인 분리
- **교육기관**: 학과별 자동 분류
- **병원**: 진료과별 자동 연결

### 고객사별 관리
- **MSP**: 고객사별 자동 분류
- **컨설팅**: 클라이언트별 자동 배정
- **소프트웨어**: 고객사별 지원 요청 분류

## 설정 팁

:::tip 효과적인 도메인 관리
- 여러 도메인을 한 번에 설정 가능
- 서브도메인도 별도 설정 필요
- 도메인 입력 시 오타 주의
- 테스트 계정으로 작동 확인
:::

### 도메인 예시

```
# 회사별 도메인 설정 예시
wedosoft.net → 위두소프트
example.com → 예시회사
university.edu → 대학교
```

### 관리 모범 사례

1. **정기적 검토**: 도메인 목록 주기적 업데이트
2. **명확한 분류**: 중복되지 않는 회사 구분
3. **문서화**: 도메인 변경 이력 기록
4. **예외 처리**: 수동 연결이 필요한 경우 대응 방안

:::success 설정 완료 확인
도메인 설정 후 새로운 연락처 생성 시 올바른 회사로 자동 연결되는지 확인하세요.
:::
