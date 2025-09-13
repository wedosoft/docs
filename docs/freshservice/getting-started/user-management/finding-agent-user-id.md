---
sidebar_position: 18
---

# 상담원 사용자 ID 찾기

:::info 문서 목적
이 문서는 상담원의 사용자 ID 또는 응답자 ID를 찾는 방법을 안내해요.
:::

## 개요

Freshservice에서 상담원의 **사용자 ID(User ID)** 또는 **응답자 ID(Responder ID)**를 찾는 방법을 안내해요. 이 ID는 API 연동, 자동화 스크립트, 고급 설정 등에서 필요한 고유 식별자입니다.

## 사용자 ID vs 상담원 ID

### 상담원 ID (Agent ID)
- Freshservice 내부에서 사용하는 상담원 식별 번호
- URL에서 확인 가능한 숫자 형태의 ID
- 상담원 프로필 페이지 URL에 표시됨

### 사용자 ID (User ID)
- API나 시스템 간 연동에서 사용하는 고유 식별자
- JSON 형태로 조회 가능
- 외부 시스템과의 데이터 연동 시 필요

## 상담원 사용자 ID 찾기 방법

### 1단계: 상담원 프로필 페이지 접근

1. **관리자 → 상담원**으로 이동해요.
2. ID를 찾으려는 **상담원의 이름**을 클릭해요.
3. 상담원 프로필 페이지가 열립니다.

### 2단계: 상담원 ID 확인

브라우저 주소창의 URL을 확인해요:
```
https://yourcompany.freshservice.com/admin/agents/12345678
```

여기서 `12345678`이 **상담원 ID**입니다.

![상담원 ID 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/21003944/original/Agent_ID.jpg?1417524045)

### 3단계: 사용자 ID 조회

1. URL 끝에 `.json`을 추가해요:
   ```
   https://yourcompany.freshservice.com/admin/agents/12345678.json
   ```

2. **Enter 키**를 눌러 페이지를 로드해요.

3. JSON 형태의 데이터에서 **사용자 ID**를 확인할 수 있어요.

![사용자 ID 조회](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/21003965/original/User_ID.jpg?1417524164)

## 단계별 상세 가이드

### URL 구조 이해하기

```
https://[도메인].freshservice.com/admin/agents/[상담원ID]
```

- **도메인**: 조직의 Freshservice 도메인
- **상담원ID**: 해당 상담원의 고유 번호

### JSON 응답 예시

```json
&#123;
  "agent": &#123;
    "id": 12345678,
    "user_id": 87654321,
    "email": "agent@company.com",
    "first_name": "김",
    "last_name": "상담원",
    ...
  &#125;
}
```

여기서 `user_id` 값이 **사용자 ID**입니다.

## 여러 상담원 ID 일괄 조회

### 방법 1: 상담원 목록 내보내기
1. **관리자 → 사용자 관리 → 상담원**으로 이동
2. **내보내기** 버튼 클릭
3. CSV 파일에서 상담원 정보 확인

### 방법 2: API 활용
```bash
curl -u email:password -H "Content-Type: application/json" \
https://yourcompany.freshservice.com/api/v2/agents
```

### 방법 3: 브라우저 개발자 도구
1. **F12** 키로 개발자 도구 열기
2. **Network** 탭 선택
3. 상담원 목록 페이지 새로고침
4. API 호출 결과에서 사용자 ID 확인

## 주의사항 및 팁

### 보안 고려사항

:::warning 접근 권한 확인
- 상담원 정보에 접근하려면 적절한 관리자 권한이 필요해요.
- 사용자 ID는 민감한 정보이므로 외부 노출을 주의하세요.
:::

### 데이터 정확성

:::tip ID 변경 불가
- 사용자 ID는 시스템에서 자동 생성되며 변경할 수 없어요.
- 상담원을 삭제 후 재생성하면 새로운 ID가 할당돼요.
:::

### API 사용 시 주의사항

:::warning API 제한사항
- API 호출 시 적절한 인증이 필요해요.
- 요청 제한(Rate Limit)을 준수해야 해요.
:::

## 문제 해결

### JSON 페이지가 로드되지 않는 경우
1. 로그인 상태를 확인하세요
2. 상담원 정보에 대한 접근 권한이 있는지 확인하세요
3. 브라우저 캐시를 삭제하고 다시 시도하세요

### 권한 오류가 발생하는 경우
1. 관리자 권한으로 로그인했는지 확인
2. 해당 상담원 정보에 대한 접근 권한이 있는지 확인
3. 계정 관리자에게 권한 부여 요청

### URL이 올바르지 않은 경우
1. 도메인이 정확한지 확인
2. 상담원 ID가 유효한 숫자인지 확인
3. URL 형식이 올바른지 재확인

