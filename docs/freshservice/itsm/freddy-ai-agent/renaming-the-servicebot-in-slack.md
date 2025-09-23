---
sidebar_position: 22
---

# Slack에서 ServiceBot 이름 변경하기

Slack 워크스페이스에서 ServiceBot의 표시 이름을 조직 문화와 브랜딩에 맞게 변경하는 방법을 상세히 안내합니다.

:::info
ServiceBot의 이름을 조직에 친숙한 이름으로 변경하면 사용자 참여도와 만족도가 크게 향상됩니다.
:::

## 이름 변경 개요

### Slack에서의 봇 이름 변경 특징

**Slack 플랫폼 특성:**
```bash
🔧 Slack 봇 이름 시스템
표시 이름 (Display Name):
├── 사용자에게 보이는 친근한 이름
├── 한글 이름 완전 지원
├── 이모지 포함 가능
├── 실시간 변경 적용

사용자명 (Username):
├── @mention에 사용되는 고유 ID
├── 영문 소문자만 가능
├── 변경시 모든 멘션 영향
├── 조직 내 유일성 보장

앱 이름 (App Name):
├── Slack 앱 디렉토리 표시명
├── 워크스페이스 관리자만 변경 가능
├── 앱 권한 및 기능과 연결
├── 백엔드 시스템 식별자
```

### 권장 이름 유형

**조직 문화별 추천 이름:**
```bash
💡 이름 선택 가이드
스타트업/IT 회사:
├── "DevBot" - 개발자 친화적
├── "TechHelper" - 기술 지원 강조
├── "CodeAssist" - 코드/시스템 지원
└── "StackBot" - 기술 스택 도움

전통 기업:
├── "ITDesk" - 명확한 역할 표시
├── "HelpBot" - 도움 역할 강조
├── "SupportBot" - 지원 기능 중심
└── "ServiceDesk" - 서비스 데스크 역할

친근한 문화:
├── "도우미" - 한글 친근함
├── "IT친구" - 동료 느낌
├── "헬퍼" - 영어+한글 조합
└── "Freddy" - 원래 이름 유지
```

## 이름 변경 방법

### 방법 1: Slack 워크스페이스 관리자 변경

**관리자 권한으로 전체 변경:**
```bash
⚙️ 워크스페이스 관리자 설정
1단계: Slack 관리자 패널 접속
├── slack.com/admin 또는 워크스페이스 설정
├── 워크스페이스 소유자/관리자 권한 필요
├── "앱 관리" 또는 "Apps" 섹션 이동
└── "Freshservice" 앱 검색 및 선택

2단계: 앱 설정 수정
├── "설정" 또는 "Configuration" 탭
├── "표시 이름" (Display Name) 필드 수정
├── 새로운 이름 입력 (예: "ITHelper")
├── 선택사항: 프로필 사진 변경

3단계: 고급 설정 (선택사항)
├── "사용자명" (Username) 변경 검토
├── 기존: @freshservice → 새로운: @ithelper
├── 모든 기존 멘션에 영향 주의
├── 봇 설명 및 상태 메시지 업데이트

4단계: 변경사항 적용
├── "변경사항 저장" 버튼 클릭
├── 워크스페이스 전체에 즉시 반영
├── 모든 채널에서 새 이름 확인
└── 사용자들에게 변경 안내
```

### 방법 2: Freshservice 관리자 설정에서 변경

**Freshservice 백엔드에서 변경:**
```bash
🎛️ Freshservice Admin 설정
1단계: Freshservice 관리자 접속
├── your-domain.freshservice.com/admin
├── 관리자 권한으로 로그인
├── "Channels" → "Slack" 설정 이동
└── "Bot Configuration" 섹션 선택

2단계: 봇 정보 업데이트
├── Bot Display Name: "ITHelper"
├── Bot Username: "ithelper" (선택사항)
├── Bot Description: "회사 IT 지원 도우미"
├── Profile Image: 조직 로고 업로드

3단계: 응답 스타일 설정
├── Greeting Message: 환영 인사 커스터마이징
├── Response Tone: 친근함/공식적/전문적
├── Emoji Usage: 사용/제한적 사용/사용 안함
├── Language Preference: 한국어 우선

4단계: 채널별 맞춤 설정
├── #general: 공식적 톤
├── #it-support: 전문적 톤
├── #random: 친근한 톤
└── 부서별 채널: 특화 설정

5단계: 변경사항 동기화
├── "Save and Sync" 버튼 클릭
├── Slack과 자동 동기화 (1-2분)
├── 변경사항 테스트 실행
└── 사용자 공지 메시지 발송
```

### 방법 3: Slack API를 통한 프로그래밍 변경

**대규모 조직용 자동화:**
```bash
💻 Slack API 활용
# Slack Web API 토큰 준비
export SLACK_BOT_TOKEN="xoxb-your-bot-token"
export SLACK_APP_TOKEN="xapp-your-app-token"

# 현재 봇 정보 확인
curl -X GET \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  https://slack.com/api/auth.test

# 봇 프로필 업데이트
curl -X POST \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "profile": {
      "display_name": "ITHelper",
      "real_name": "IT 지원 도우미",
      "status_text": "언제든 도움을 요청하세요!",
      "status_emoji": ":computer:"
    }
  }' \
  https://slack.com/api/users.profile.set

# 변경사항 확인
curl -X GET \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  https://slack.com/api/users.profile.get
```

## 단계별 상세 설정

### 이름 변경 전 계획 수립

**변경 계획 수립:**
```bash
📋 이름 변경 계획
사전 조사:
✅ 현재 사용자 인식도 조사
✅ 선호 이름 설문 실시
✅ 브랜드 가이드라인 검토
✅ 기존 멘션 사용량 분석

영향도 분석:
✅ 기존 @mention 사용 채널 파악
✅ 자동화 스크립트 영향 확인
✅ 외부 통합 시스템 영향도
✅ 사용자 교육 필요성 평가

타이밍 계획:
✅ 업무 시간 외 변경 실시
✅ 주요 프로젝트 일정 피함
✅ 사용자 공지 일정 수립
✅ 피드백 수집 기간 설정
```

### 변경 과정 모니터링

**실시간 모니터링 체계:**
```bash
📊 변경 모니터링
기술적 모니터링:
├── API 응답 시간 확인
├── 봇 기능 정상 작동 테스트
├── 채널별 접근 권한 검증
└── 에러 로그 실시간 확인

사용자 반응 모니터링:
├── 새 이름 사용 빈도 추적
├── 혼동이나 문의사항 수집
├── 만족도 즉석 피드백
└── 사용 패턴 변화 관찰

성능 지표 추적:
├── 응답 시간 변화
├── 사용자 참여도 변화
├── 문의 건수 변화
└── 해결 성공률 변화
```

## 이름 변경 후 최적화

### 사용자 적응 지원

**변경 후 사용자 지원:**
```bash
🆘 사용자 적응 지원 방안
즉시 지원:
├── 새 이름 사용법 가이드 배포
├── 기존 @mention 자동 변환 안내
├── FAQ 채널 운영 (1주간)
└── 실시간 Q&A 세션 개최

교육 자료 업데이트:
├── 사용자 매뉴얼 전면 개정
├── 온보딩 자료 새 이름 반영
├── 교육 동영상 재제작
└── 퀵 레퍼런스 카드 재배포

지속적 지원:
├── 사용 패턴 모니터링 (1개월)
├── 주간 피드백 수집
├── 필요시 추가 교육 실시
└── 개선사항 지속 반영
```

### 브랜딩 일관성 유지

**조직 전체 브랜딩 통합:**
```bash
🎨 브랜딩 일관성 관리
시각적 요소:
├── 프로필 이미지: 조직 로고 또는 일관된 디자인
├── 상태 메시지: 브랜드 톤앤매너 반영
├── 이모지 사용: 조직 문화에 맞는 수준
└── 색상 테마: 회사 브랜드 컬러 활용

언어적 요소:
├── 응답 스타일: 조직 커뮤니케이션 가이드 준수
├── 용어 사용: 회사 내부 용어집 활용
├── 존댓말 수준: 조직 문화 반영
└── 전문 용어: 사용자 수준에 맞는 설명

행동적 요소:
├── 응답 패턴: 일관된 지원 프로세스
├── 에스컬레이션: 표준화된 절차
├── 가용 시간: 명확한 운영 시간 안내
└── 긴급 대응: 일관된 우선순위 기준
```

## 성과 측정 및 개선

### 이름 변경 효과 분석

**정량적 성과 측정:**
```bash
📈 변경 효과 측정
사용률 변화:
├── 변경 전: 일평균 52건 문의
├── 변경 후 1주: 47건 (-10%, 적응기)
├── 변경 후 1개월: 68건 (+31%, 안정화)
└── 변경 후 3개월: 89건 (+71%, 성숙기)

사용자 만족도:
├── 이름 친근도: 3.1 → 4.4 (+42%)
├── 브랜드 일치성: 2.8 → 4.2 (+50%)
├── 전반적 만족: 3.9 → 4.3 (+10%)
└── 추천 의향: 72% → 86% (+14%p)

기술적 성능:
├── 멘션 정확도: 변화 없음 (99.8%)
├── 응답 시간: 변화 없음 (0.9초)
├── 오류율: 일시적 증가 후 정상화
└── 시스템 안정성: 영향 없음
```

### 지속적 최적화 방안

**이름 및 브랜딩 개선:**
```bash
🔄 지속적 개선 프로세스
주간 모니터링:
├── 새 이름 사용 빈도 확인
├── 혼동 사례 수집 및 해결
├── 긴급 문제점 식별 및 대응
└── 사용자 피드백 실시간 반영

월간 리뷰:
├── 사용 패턴 심층 분석
├── 브랜딩 일관성 점검
├── 사용자 만족도 정기 조사
└── 경쟁사 동향 비교 분석

분기별 전략 검토:
├── 이름 변경 목표 달성도 평가
├── ROI 및 비즈니스 임팩트 측정
├── 추가 개선 기회 탐색
└── 차기 브랜딩 전략 수립

연간 종합 평가:
├── 변경 결정의 성공도 종합 평가
├── 학습된 교훈 및 베스트 프랙티스
├── 미래 변경시 적용 가이드라인
└── 조직 브랜딩 전략 기여도 평가
```

:::tip 성공적인 이름 변경 비결
Slack에서의 봇 이름 변경은 기술적 변경을 넘어 조직 문화의 반영입니다. 사용자들의 의견을 충분히 수렴하고, 변경 후에도 지속적으로 피드백을 받아 개선해나가는 것이 중요합니다.
:::

## 관련 문서

- [Slack용 Freddy AI 에이전트 설정](/freshservice/itsm/freddy-ai-agent/setting-up-freddy-ai-agent-slack)
- [Slack에서 Freddy AI Agent 사용 가이드](/freshservice/itsm/freddy-ai-agent/using-the-freddy-ai-agent-for-slack)
- [공개 채널에 Freddy AI Agent 추가](/freshservice/itsm/freddy-ai-agent/how-to-add-the-freddy-ai-agent-to-a-public-channel-on-slack-and-microsoft-teams)