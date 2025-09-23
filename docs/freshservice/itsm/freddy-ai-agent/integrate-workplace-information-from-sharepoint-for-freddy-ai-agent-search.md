---
sidebar_position: 16
---

# SharePoint 연동을 통한 Freddy AI Agent 검색 기능

SharePoint에서 회사 정보를 통합하여 Freddy AI Agent가 더 정확하고 포괄적인 답변을 제공할 수 있도록 설정하는 방법을 안내합니다.

:::info
SharePoint 연동을 통해 Freddy AI Agent는 회사 문서, 정책, 절차서까지 검색하여 보다 완전한 답변을 제공할 수 있습니다.
:::

## 연동 개요

### SharePoint 통합의 이점

**확장된 지식 범위:**
```bash
📚 검색 가능한 콘텐츠 확장
기존 지식베이스:
├── Freshservice 내부 KB 아티클
├── 해결된 티켓 히스토리
├── FAQ 및 표준 응답
└── 에이전트 작성 가이드

SharePoint 추가 후:
├── 회사 정책 문서
├── 절차서 및 매뉴얼
├── 제품 사양서
├── 교육 자료
├── 프로젝트 문서
└── 부서별 가이드라인
```

**정보 접근성 향상:**
- 실시간 문서 검색 및 참조
- 버전 관리된 최신 정보 제공
- 권한 기반 정보 접근 제어
- 다양한 파일 형식 지원 (Word, Excel, PDF, PowerPoint)

### 지원되는 SharePoint 환경

**SharePoint Online (Microsoft 365):**
- 완전 지원
- 실시간 동기화
- OAuth 2.0 인증
- 고급 검색 기능

**SharePoint Server (온프레미스):**
- SharePoint 2019 이상
- 제한적 동기화 옵션
- 추가 방화벽 설정 필요
- 하이브리드 환경 지원

## 설정 과정

### 1단계: SharePoint 앱 등록

**Microsoft Azure AD에서 앱 등록:**
```bash
1. Azure Portal (portal.azure.com) 접속
2. Azure Active Directory → App registrations
3. "New registration" 클릭
4. 앱 정보 입력:
   - Name: "Freshservice Freddy AI Agent"
   - Account types: "Single tenant"
   - Redirect URI: "https://your-domain.freshservice.com/auth/callback"
5. "Register" 클릭하여 완료
```

**API 권한 설정:**
```bash
Required API Permissions:
├── Microsoft Graph:
│   ├── Sites.Read.All (위임됨)
│   ├── Files.Read.All (위임됨)
│   ├── User.Read (위임됨)
│   └── Directory.Read.All (애플리케이션)
├── SharePoint:
│   ├── Sites.Search.All (위임됨)
│   ├── TermStore.Read.All (위임됨)
│   └── Sites.Read.All (애플리케이션)
```

### 2단계: Freshservice 연동 설정

**Admin 설정에서 연동 활성화:**
```bash
1. Admin → Integrations → SharePoint
2. "Enable SharePoint Integration" 토글 ON
3. Azure 앱 정보 입력:
   - Client ID: [Azure에서 복사한 Application ID]
   - Client Secret: [Azure에서 생성한 Secret]
   - Tenant ID: [Azure AD Tenant ID]
4. "Test Connection" 버튼으로 연결 확인
5. "Save Configuration" 클릭
```

**사이트 및 라이브러리 선택:**
```bash
연동할 SharePoint 사이트:
✅ 회사 정책 사이트 (policies.sharepoint.com)
✅ IT 문서 라이브러리 (itdocs.sharepoint.com)  
✅ 교육 자료 사이트 (training.sharepoint.com)
✅ 부서별 공유 라이브러리
❌ 개인 OneDrive (보안상 제외)
❌ 기밀 프로젝트 사이트 (접근 제한)
```

### 3단계: 검색 범위 및 권한 설정

**문서 유형별 우선순위:**
```bash
🔍 검색 우선순위 설정
높은 우선순위 (즉시 검색):
├── IT 정책 및 절차서 (.docx, .pdf)
├── 사용자 매뉴얼 (.pdf, .docx)
├── FAQ 문서 (.docx, .txt)
└── 공지사항 (.docx, .html)

중간 우선순위 (필요시 검색):
├── 교육 자료 (.pptx, .pdf)
├── 프로젝트 문서 (.docx, .xlsx)
├── 회의록 (.docx, .pdf)
└── 참고 자료 (.pdf, .docx)

낮은 우선순위 (수동 요청시):
├── 과거 프로젝트 자료
├── 아카이브된 문서
└── 초안 및 작업 중 문서
```

## 실무 활용 사례

### 정책 및 절차 문의

**시나리오 1: 재택근무 정책 문의**
```
사용자: "재택근무 시 VPN 사용 정책이 어떻게 되나요?"
↓
Freddy AI Agent 검색 과정:
1. 내부 KB 검색 → 기본 VPN 설정 가이드 발견
2. SharePoint 검색 → "재택근무 보안 정책 v2.1.pdf" 발견
3. 통합 응답 생성

Freddy 응답:
"재택근무 시 VPN 사용 정책을 안내해드리겠습니다.

📋 **회사 재택근무 보안 정책**(v2.1, 2024년 3월 업데이트):
- VPN 연결 필수: 모든 회사 시스템 접속 시
- 승인된 VPN 클라이언트만 사용 (Cisco AnyConnect)
- 공용 WiFi 사용 금지
- 업무 종료 시 VPN 연결 해제

🔗 **상세 정책 문서**: [재택근무_보안정책_v2.1.pdf]
📞 **추가 문의**: IT 보안팀 (ext. 2200)

VPN 설정에 도움이 필요하시면 말씀해주세요!"
```

### 소프트웨어 및 도구 관련 문의

**시나리오 2: 신규 소프트웨어 설치 절차**
```
사용자: "Adobe Creative Suite 설치 방법을 알려주세요"
↓
검색 결과 통합:
1. 내부 KB: 기본 설치 가이드
2. SharePoint: "소프트웨어_설치_매뉴얼_Adobe_v3.2.docx"
3. SharePoint: "라이선스_관리_정책.pdf"

Freddy 통합 응답:
"Adobe Creative Suite 설치를 도와드리겠습니다.

📦 **설치 전 필수 사항** (소프트웨어 설치 매뉴얼 v3.2):
1. 부서장 승인 완료 확인
2. 라이선스 할당 확인 (IT 자산팀)
3. 시스템 요구사항 체크:
   - Windows 10 이상 / macOS 10.15 이상
   - RAM 8GB 이상 권장
   - 여유 디스크 공간 20GB 이상

🔧 **설치 단계**:
1. IT 자산팀에 설치 요청 티켓 생성
2. 원격 설치 일정 조율 (1-2일 소요)
3. 설치 완료 후 활성화 확인
4. 교육 자료 제공 ([Adobe_교육자료.pdf])

📋 **관련 정책**: [소프트웨어_라이선스_정책.pdf]

설치 요청을 도와드릴까요?"
```

### 하드웨어 및 자산 관리

**시나리오 3: 장비 교체 절차 문의**
```
사용자: "노트북이 너무 느려서 교체하고 싶어요"
↓
SharePoint에서 발견된 문서:
- "IT_자산_관리_정책.docx"
- "하드웨어_교체_신청_절차.pdf"
- "장비_성능_기준_가이드.xlsx"

Freddy 응답:
"노트북 교체 절차를 안내해드리겠습니다.

📊 **교체 기준 확인** (하드웨어 교체 신청 절차):
✅ 사용 기간: 3년 이상 또는
✅ 성능 저하: 업무 효율성 50% 이하 또는  
✅ 고장/결함: 수리 비용 > 신품 가격의 60%

🔍 **현재 장비 진단**:
귀하의 노트북 정보를 확인해보겠습니다.
- 모델명과 구매일을 알려주시겠어요?
- 주요 느려짐 증상은 무엇인가요?

📝 **신청 절차** (IT 자산 관리 정책):
1. 장비 진단 요청 (IT 지원팀)
2. 교체 필요성 평가
3. 부서 예산 확인 및 승인
4. 신규 장비 주문 (1-2주 소요)
5. 데이터 이전 및 구 장비 회수

🔗 **신청 양식**: [하드웨어_교체_신청서.docx]

진단부터 시작해드릴까요?"
```

## 고급 설정 및 최적화

### 검색 정확도 향상

**메타데이터 활용:**
```bash
SharePoint 메타데이터 매핑:
├── 문서 유형 (Document Type)
│   ├── 정책 (Policy)
│   ├── 절차서 (Procedure)
│   ├── 매뉴얼 (Manual)
│   └── FAQ (FAQ)
├── 부서 (Department)
│   ├── IT (Information Technology)
│   ├── HR (Human Resources)
│   ├── 재무 (Finance)
│   └── 마케팅 (Marketing)
├── 중요도 (Priority)
│   ├── 높음 (High)
│   ├── 보통 (Medium)
│   └── 낮음 (Low)
└── 대상 사용자 (Target Audience)
    ├── 전직원 (All Staff)
    ├── IT팀 (IT Team)
    ├── 관리자 (Managers)
    └── 신규직원 (New Employees)
```

### 보안 및 권한 관리

**접근 권한 제어:**
```bash
🔐 권한 기반 검색 제한
임원진 전용 문서:
- Freddy AI는 검색하지 않음
- 별도 요청 시에만 안내

부서별 제한 문서:
- 사용자 부서 정보 기반 필터링
- 권한 없는 문서는 검색 결과에서 제외

기밀 문서:
- "기밀" 태그가 있는 문서 자동 제외
- 보안 분류 수준 확인

외부 공유 문서:
- 외부 파트너와 공유된 문서만 별도 표시
- 민감 정보 포함 여부 자동 체크
```

### 성능 모니터링

**검색 성능 지표:**
```bash
📊 SharePoint 연동 성능 대시보드
응답 시간:
├── 평균 검색 시간: 1.8초 (목표: <2초)
├── SharePoint 응답: 0.9초
├── 내용 분석: 0.6초
└── 답변 생성: 0.3초

검색 정확도:
├── 관련 문서 발견율: 87% (목표: 85%+)
├── 최신 문서 우선도: 92%
├── 권한 오류율: 0.3% (목표: <1%)
└── 사용자 만족도: 4.4/5.0

시스템 안정성:
├── SharePoint 연결 가용성: 99.7%
├── 동기화 실패율: 1.2% (목표: <2%)
├── 대용량 파일 처리: 94% 성공
└── 동시 검색 처리: 최대 50건
```

## 문제 해결

### 일반적인 연동 문제

**연결 실패 문제:**
```bash
증상: SharePoint 검색 결과가 나오지 않음
원인: API 권한 또는 네트워크 문제
해결:
1. Azure AD 앱 권한 재확인
2. SharePoint 사이트 접근 권한 검증
3. 방화벽 설정 확인 (포트 443 허용)
4. OAuth 토큰 갱신
```

**검색 품질 저하:**
```bash
증상: 관련 없는 문서가 검색됨
원인: 메타데이터 부족 또는 키워드 매칭 오류
해결:
1. SharePoint 문서 메타데이터 보완
2. 검색 키워드 매핑 테이블 업데이트
3. 불필요한 문서 검색 범위에서 제외
4. 사용자 피드백 기반 검색 알고리즘 조정
```

:::tip 효과적인 활용 팁
SharePoint 연동의 효과를 극대화하려면 문서 구조화와 메타데이터 관리가 핵심입니다. 정기적으로 문서를 정리하고 태그를 업데이트하세요.
:::

## 관련 문서

- [Freddy AI Agent 소개](/freshservice/itsm/freddy-ai-agent/introduction-to-freddy-ai-agent)
- [채널별 쿼리 응답 설정](/freshservice/itsm/freddy-ai-agent/how-to-use-freddy-ai-agent-to-enable-query-responses-on-channels)
- [Freddy AI Agent 성과 분석](/freshservice/itsm/freddy-ai-agent/analysing-freddy-ai-agent-performance-using-analytics)