---
sidebar_position: 4
---

# Microsoft Teams용 Freddy AI 에이전트 설정하기

Microsoft Teams와 함께 Freddy AI 에이전트를 사용하면 팀원들이 Teams 내에서 직접 IT 지원을 받을 수 있어 워크플로우가 간소화됩니다.

:::info
Freddy AI 에이전트는 Freshservice와 Microsoft Teams를 연결하여 사용자가 Teams 채널에서 직접 티켓을 생성하고 IT 지원을 받을 수 있게 해주는 스마트 봇입니다.
:::

## 전제 조건

- Microsoft Teams 관리자 권한
- Freshservice 관리자 계정 접근 권한
- 활성화된 Freddy AI 에이전트 라이선스

## 설정 단계

### 1단계: Freshservice에서 Microsoft Teams 통합 활성화

1. Freshservice 관리자로 로그인
2. **Admin > Apps > Microsoft Teams**로 이동
3. **Install App** 버튼 클릭
4. 필요한 권한 승인

### 2단계: Freddy AI 에이전트 구성

1. **Admin > Freddy > AI Agent**로 이동
2. **Microsoft Teams** 탭 선택
3. 봇 이름 및 환영 메시지 설정
4. 채널 액세스 권한 구성

## 실제 사용 예제

사용자가 Teams에서 다음과 같이 입력:

```
@Freddy 노트북이 부팅되지 않습니다. 도움이 필요해요.
```

Freddy가 자동으로 문제를 분석하고 해결책을 제안하거나 티켓을 생성합니다.

## 모범 사례

- 자주 묻는 질문을 지식베이스에 정기적으로 업데이트
- 복잡한 문제는 인간 에이전트에게 자동 에스컬레이션
- 사용자 피드백을 통한 지속적인 봇 성능 개선