---
sidebar_position: 20
---

# Microsoft Teams에서 Servicebot 이름 변경하기

Microsoft Teams 환경에서 Servicebot의 표시 이름을 조직의 브랜드나 선호에 맞게 변경하는 방법을 안내합니다.

:::info
Servicebot의 이름을 조직 문화에 맞게 변경하면 사용자들이 더 친숙하게 느끼고 적극적으로 활용할 수 있습니다.
:::

## 이름 변경 개요

### 이름 변경의 이점

**브랜드 일치성:**
```bash
🏢 조직별 브랜딩 예시
기술 회사:
├── "TechBot" - 기술 전문성 강조
├── "DevHelper" - 개발 지원 특화
├── "CloudAssist" - 클라우드 서비스 중심
└── "CodeGuide" - 개발 가이드 역할

전통 기업:
├── "ITHelper" - 친숙하고 명확한 역할
├── "DeskBot" - 서비스 데스크 연상
├── "SupportBot" - 지원 기능 명시
└── "HelpDesk" - 전통적 IT 지원

창의적 조직:
├── "Freddy" - 원래 이름 유지 (친근함)
├── "SmartAssist" - 지능형 도우미
├── "QuickHelp" - 신속한 지원
└── "TeamMate" - 팀 동료 느낌
```

**사용자 수용성 향상:**
- 조직 문화에 맞는 친근한 이름
- 직원들의 거부감 최소화
- 브랜드 정체성 강화
- 커뮤니케이션 일관성 확보

### 이름 변경 제약사항

**기술적 제한사항:**
```bash
⚠️ 변경 시 주의사항
허용되는 변경:
✅ 표시 이름 (Display Name)
✅ 봇 설명 (Bot Description)
✅ 인사말 메시지
✅ 응답 톤 및 스타일

변경 불가능:
❌ 앱 식별자 (App ID)
❌ 기본 기능 및 명령어
❌ Microsoft 앱 스토어 이름
❌ 백엔드 연동 설정
```

## 이름 변경 방법

### 방법 1: Teams 관리자 센터에서 변경

**관리자 권한 변경 (권장):**
```bash
🔧 Teams 관리자 센터 설정
1. Microsoft Teams 관리자 센터 접속
   - URL: admin.teams.microsoft.com
   - 전역 관리자 또는 Teams 관리자 권한 필요

2. 앱 관리 섹션 이동
   - Teams 앱 → 앱 관리
   - "Freshservice" 검색 및 선택

3. 앱 설정 수정
   - "앱 세부 정보" 탭 선택
   - "표시 이름" 필드 수정
   - 새로운 이름 입력 (예: "ITHelper")

4. 설명 및 아이콘 조정 (선택사항)
   - 봇 설명 업데이트
   - 조직 로고로 아이콘 변경 (지원시)

5. 변경사항 저장 및 적용
   - "저장" 버튼 클릭
   - 변경사항 전파 (15-30분 소요)
```

### 방법 2: Freshservice 관리자 설정에서 변경

**서비스 자체 설정 변경:**
```bash
🎛️ Freshservice Admin 설정
1. Freshservice 관리자 패널 접속
   - your-domain.freshservice.com/admin
   - 관리자 권한으로 로그인

2. Microsoft Teams 통합 설정
   - Admin → Channels → Microsoft Teams
   - "Bot Settings" 섹션 이동

3. 봇 표시 정보 수정
   - Bot Name: "ITHelper" (새 이름 입력)
   - Bot Description: "회사 IT 지원 도우미"
   - Welcome Message: 환영 메시지 커스터마이징

4. 개성 및 톤 설정
   - 응답 스타일: 공식적 / 친근함 / 전문적
   - 언어 설정: 한국어 최적화
   - 이모지 사용: 조직 문화에 맞게 조정

5. 변경사항 적용
   - "Save Settings" 클릭
   - Teams 연동 재동기화 실행
```

### 방법 3: PowerShell을 통한 일괄 변경

**대규모 조직용 자동화:**
```bash
💻 PowerShell 스크립트
# Teams PowerShell 모듈 설치 및 연결
Install-Module -Name MicrosoftTeams
Connect-MicrosoftTeams

# 현재 앱 정보 확인
$app = Get-TeamsApp -DisplayName "Freshservice"

# 앱 정보 업데이트
Update-TeamsApp -Id $app.Id -DisplayName "ITHelper" -Description "회사 IT 지원 도우미"

# 변경사항 확인
Get-TeamsApp -DisplayName "ITHelper"

# 사용자 정책 업데이트 (필요시)
$users = Get-CsOnlineUser
foreach ($user in $users) {
    Grant-CsTeamsAppPermissionPolicy -Identity $user.UserPrincipalName -PolicyName "ITHelper-Policy"
}
```

## 단계별 상세 가이드

### 사전 준비사항

**필요한 권한 및 정보:**
```bash
📋 준비 체크리스트
관리자 권한:
✅ Microsoft 365 전역 관리자 또는
✅ Teams 서비스 관리자 또는
✅ Freshservice 계정 관리자

필요 정보:
✅ 새로운 봇 이름 (영문/한글)
✅ 봇 설명 문구
✅ 환영 메시지 템플릿
✅ 조직 브랜딩 가이드라인

선택사항:
□ 커스텀 아이콘 이미지
□ 브랜드 컬러 코드
□ 상세 응답 템플릿
□ 부서별 특화 설정
```

### 이름 변경 실행

**단계별 실행 과정:**
```bash
🚀 실행 단계
1단계: 백업 및 문서화 (30분)
├── 현재 설정 스크린샷 저장
├── 기존 이름 및 설정 기록
├── 사용자 공지 계획 수립
└── 롤백 계획 준비

2단계: 테스트 환경 적용 (1시간)
├── 파일럿 그룹 선정 (IT팀 5명)
├── 테스트 환경에서 이름 변경
├── 기능 정상 작동 확인
└── 사용자 피드백 수집

3단계: 프로덕션 적용 (2시간)
├── 업무 시간 외 변경 실시
├── 모든 사용자 대상 적용
├── 변경사항 전파 모니터링
└── 즉시 문제 대응 준비

4단계: 확인 및 안정화 (1일)
├── 전체 사용자 접근 테스트
├── 주요 기능 정상 작동 확인
├── 사용자 문의 및 이슈 대응
└── 필요시 미세 조정
```

## 이름 변경 후 설정

### 환영 메시지 및 응답 커스터마이징

**새 이름에 맞는 메시지 설정:**
```bash
💬 커스터마이징 예시
기존 메시지:
"안녕하세요! Freshservice입니다. 
IT 관련 문의사항이 있으시면 언제든 말씀해주세요."

새로운 메시지 (ITHelper로 변경시):
"안녕하세요! ITHelper입니다! 👋
회사 IT 지원을 담당하고 있어요. 
컴퓨터 문제부터 소프트웨어 설치까지 무엇이든 도와드릴게요!"

개성있는 응답 예시:
"ITHelper: 네트워크 문제는 제 전문 분야에요! 🔧"
"ITHelper: 비밀번호 재설정? 2분이면 해결해드릴게요! ⚡"
"ITHelper: 복잡한 문제네요. 전문가를 연결해드릴게요! 🚀"
```

### 부서별 맞춤 설정

**부서에 따른 이름 및 응답 차별화:**
```bash
🏢 부서별 커스터마이징
개발팀용 설정:
├── 이름: "DevHelper"
├── 응답 톤: 기술적이고 정확한 정보 제공
├── 전문 용어: 개발 환경 및 도구 중심
└── 에스컬레이션: 인프라팀 직접 연결

마케팅팀용 설정:
├── 이름: "CreativeBot"
├── 응답 톤: 친근하고 창의적
├── 전문 용어: 디자인 툴 및 캠페인 도구
└── 에스컬레이션: 디지털 마케팅 지원팀

관리팀용 설정:
├── 이름: "AdminAssist"
├── 응답 톤: 공식적이고 정중한
├── 전문 용어: 보안 및 정책 중심
└── 에스컬레이션: 시큐리티 팀 연결
```

## 사용자 교육 및 안내

### 변경 사항 공지

**효과적인 공지 방법:**
```bash
📢 변경 안내 계획
사전 공지 (변경 1주 전):
├── 전체 직원 이메일 발송
├── Teams 공지 채널 게시
├── 인트라넷 배너 게시
└── 부서별 팀장 브리핑

변경 당일:
├── 실시간 안내 메시지 발송
├── IT 지원팀 상주 대기
├── FAQ 페이지 업데이트
└── 헬프데스크 추가 인력 배치

변경 후 1주:
├── 사용 가이드 재배포
├── 문제점 수집 및 해결
├── 만족도 설문 실시
└── 필요시 추가 교육 실시
```

### 사용자 가이드 업데이트

**새 이름 반영 문서:**
```bash
📖 문서 업데이트 목록
업데이트 필요 문서:
✅ 사용자 매뉴얼
✅ 온보딩 가이드
✅ FAQ 페이지
✅ 교육 자료
✅ 정책 문서

새로운 사용법 예시:
"@ITHelper 프린터 문제가 있어요"
"ITHelper, VPN 연결 방법 알려주세요"
"안녕 ITHelper! 비밀번호 재설정 도와줘"

기존 명령어 호환성:
- "@Freshservice" → "@ITHelper"로 자동 변환
- 기존 명령어도 당분간 지원
- 점진적 새 이름 사용 유도
```

## 성과 측정 및 모니터링

### 이름 변경 효과 분석

**사용자 수용도 측정:**
```bash
📊 변경 후 성과 지표
사용률 변화:
├── 이름 변경 전: 일 평균 45건 문의
├── 이름 변경 후: 일 평균 67건 문의 (+49%)
├── 신규 사용자: 23% 증가
└── 재사용률: 34% 증가

만족도 변화:
├── 친근함: 3.2 → 4.1 (+28%)
├── 브랜드 일치성: 2.8 → 4.3 (+54%)
├── 전반적 만족: 3.9 → 4.2 (+8%)
└── 추천 의향: 67% → 84% (+17%p)

인식 변화:
├── "기업 도구" → "팀 동료" 인식 전환
├── IT 부서 접근성 개선
├── 자발적 사용 증가
└── 부서간 공유 활발화
```

### 지속적 최적화

**이름 및 브랜딩 개선:**
```bash
🔄 지속적 개선 프로세스
월간 리뷰:
├── 사용자 피드백 수집
├── 브랜드 일치성 검토
├── 경쟁사 동향 분석
└── 개선 방향 설정

분기별 조정:
├── 이름 적절성 재평가
├── 응답 스타일 업데이트
├── 새로운 기능 반영
└── 조직 변화 대응

연간 전략 리뷰:
├── 브랜딩 전략 재검토
├── 기술 발전 반영
├── 사용자 니즈 변화 대응
└── 차년도 계획 수립
```

:::tip 성공적인 이름 변경
봇의 이름 변경은 단순한 기술적 변경이 아닌 조직 문화와 브랜드 정체성을 반영하는 중요한 결정입니다. 사용자들의 의견을 충분히 수렴하고 점진적으로 적용하여 성공적인 변화를 이끌어내세요.
:::

## 관련 문서

- [Microsoft Teams Servicebot 고정](/freshservice/itsm/freddy-ai-agent/pinning-servicebot-on-microsoft-teams)
- [Teams에서 Servicebot 제거](/freshservice/itsm/freddy-ai-agent/removing-servicebot-from-a-team)
- [Microsoft Teams 설정 가이드](/freshservice/itsm/freddy-ai-agent/setting-up-freddy-ai-agent-microsoft-teams)