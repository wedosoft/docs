# SSO FAQ

Single Sign-On 구성에서 자주 발생하는 질문들과 실무에서 검증된 해결 방법을 정리했습니다. 기본 SSO 설정부터 고급 보안 구성 및 문제 해결까지 포괄적으로 다룹니다.

## 🔐 기본 SSO 이해

<details>
<summary><strong>SSO가 무엇인가요?</strong></summary>

**답변:** Single Sign-On(SSO)은 하나의 인증으로 여러 애플리케이션에 안전하게 접근할 수 있게 해주는 인증 시스템입니다. 사용자는 한 번만 로그인하면 Freshservice를 포함한 모든 연동된 시스템을 사용할 수 있습니다.

**핵심 구성 요소:**
- **Identity Provider (IdP)**: 인증 관리 시스템 (ADFS, Okta, Azure AD, Google Workspace)
- **Service Provider (SP)**: IdP를 신뢰하는 애플리케이션 (Freshservice)
- **SAML/OAuth**: 안전한 인증 정보 전달 프로토콜

**비즈니스 효과:**
- **보안 강화**: 중앙집중식 인증으로 보안 정책 일관성 확보
- **사용자 편의성**: 여러 패스워드 기억할 필요 없음
- **관리 효율성**: IT 관리자의 계정 관리 부담 대폭 감소
- **컴플라이언스**: 감사 추적 및 액세스 제어 강화

**실무 장점:** 직원들이 업무 시작 시 한 번만 로그인하면 하루 종일 모든 시스템을 원활하게 사용할 수 있습니다.

</details>

<details>
<summary><strong>지원하는 SSO 프로토콜은 무엇인가요?</strong></summary>

**주요 지원 프로토콜과 활용 시나리오:**

**🔒 SAML 2.0 (가장 널리 사용)**
- XML 기반의 안전한 인증 정보 교환
- 엔터프라이즈 환경에서 검증된 안정성
- **최적 사용**: 대기업, 보안이 중요한 조직
- **호환 IdP**: ADFS, Okta, OneLogin, Azure AD

**⚡ OAuth 2.0 (현대적 표준)**
- JSON 기반의 경량화된 토큰 교환
- API 접근 제어에 특화
- **최적 사용**: 클라우드 네이티브 환경, API 중심 조직
- **호환 IdP**: Google Workspace, Microsoft 365, Auth0

**🆔 OpenID Connect (하이브리드)**
- OAuth 2.0 기반의 ID 인증 레이어
- 사용자 프로필 정보 풍부한 교환
- **최적 사용**: 개인화가 중요한 서비스
- **호환 IdP**: Google, Microsoft, Facebook

**선택 가이드:**
- **기존 Active Directory 환경**: SAML 2.0 권장
- **클라우드 우선 환경**: OAuth 2.0/OpenID Connect 권장
- **하이브리드 환경**: 조직 정책에 따라 선택

</details>

<details>
<summary><strong>SSO 설정을 위한 사전 준비사항은 무엇인가요?</strong></summary>

**성공적인 SSO 구축을 위한 체크리스트:**

**🔧 기술적 요구사항**
- **활성 Identity Provider**: 라이선스가 있는 IdP 계정 (Azure AD, Okta 등)
- **Freshservice 관리자 권한**: Admin 레벨 접근 권한
- **SSL 인증서**: HTTPS 도메인 필수 (보안 통신용)
- **네트워크 접근**: IdP와 Freshservice 간 통신 가능

**📋 정보 수집 체크리스트**
- **IdP 메타데이터**: SSO URL, 인증서, Entity ID
- **사용자 속성 매핑**: 이메일, 이름, 부서 정보 필드명
- **그룹 정보**: 사용자 역할/권한과 연결할 그룹 구조
- **도메인 정보**: 사용자 이메일 도메인 목록

**👥 조직적 준비사항**
- **IT 팀 협업**: IdP 관리자와 Freshservice 관리자 간 협력
- **사용자 교육**: 변경되는 로그인 프로세스 안내
- **롤백 계획**: SSO 장애 시 임시 접근 방법 준비
- **테스트 계획**: 단계별 검증 및 사용자 그룹별 테스트

**⚠️ 주의사항:**
- 기존 사용자 계정과 IdP 사용자 정보 일치 여부 확인
- 관리자 계정 별도 백업 로그인 방법 확보
- 프로덕션 적용 전 충분한 테스트 환경 검증

**성공 팁:** SSO 구성 전에 IdP 관리자와 사전 미팅을 통해 필요한 정보와 권한을 미리 확보하세요.

</details>

**정보 수집:**
- IdP의 메타데이터 또는 설정 정보
- 사용자 속성 매핑 정의
- 인증서 파일 (필요시)

**조직적 요구사항:**
- IT 보안 정책 검토
- 사용자 교육 계획
- 백업 인증 방법 준비

사전 계획을 통해 원활한 SSO 도입이 가능합니다.
</details>

<details>
<summary>4. SAML SSO는 어떻게 설정하나요?</summary>

SAML SSO 설정은 다음 단계로 진행됩니다:

**1단계: Freshservice 설정**
- Admin > Security > SSO 메뉴 접근
- SAML 2.0 선택 및 기본 정보 입력
- Service Provider 메타데이터 다운로드

![SSO Settings Screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000801700/original/v3EVn0FGLDKOIvDVP85y86CoVKCzhzzLOg.png)

*Admin Security Settings에서 SSO 구성 진행*

**2단계: IdP 설정**
- IdP에서 새 애플리케이션 추가
- Freshservice 메타데이터 업로드
- 사용자 속성 매핑 구성

![Admin Security Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50007504089/original/xWuGQ2zcOimDLop_hgQ5KFNVqGUFwdtjvg.png?1675315951)

*Admin > Security Settings에서 보안 정책 및 인증 설정 관리*

**3단계: 연동 테스트**
- 테스트 사용자로 로그인 검증
- 속성 매핑 확인
- 오류 발생 시 로그 분석

**4단계: 프로덕션 배포**
- 모든 사용자에게 SSO 활성화
- 교육 및 지원 제공

체계적인 접근을 통해 안정적인 SSO 구현이 가능합니다.
</details>

<details>
<summary>5. OAuth 2.0 SSO는 어떻게 구성하나요?</summary>

OAuth 2.0 SSO 구성 절차:

**1단계: OAuth 애플리케이션 등록**
- IdP에서 OAuth 애플리케이션 생성
- 클라이언트 ID 및 시크릿 발급
- 리다이렉트 URI 설정

**2단계: Freshservice 연동**
- Admin > Security > SSO에서 OAuth 선택
- 클라이언트 정보 및 엔드포인트 설정
- 스코프 및 권한 구성

**3단계: 사용자 매핑**
- 사용자 정보 클레임 설정
- 그룹 매핑 구성 (필요시)
- 권한 레벨 정의

**4단계: 보안 강화**
- 토큰 만료 시간 설정
- 리프레시 토큰 정책 구성
- 로깅 및 모니터링 활성화

OAuth는 특히 API 기반 통합에서 강력한 보안을 제공합니다.
</details>

<details>
<summary>6. 사용자 속성 매핑은 어떻게 설정하나요?</summary>

사용자 속성 매핑 설정 방법:

**기본 속성:**
- Email (필수): emailaddress, email
- First Name: givenname, FirstName, username
- Last Name: surname, LastName
- Phone: phone
- Company: company, organization

**사용자 정의 속성:**
- Custom Field: custom_field_`<field_name>`
- 예시: Office Location → custom_field_office_location

**매핑 설정 단계:**
1. IdP에서 사용자 속성 정의
2. Freshservice에서 필드 매핑 구성
3. 테스트 사용자로 속성 전달 확인
4. 필요시 변환 규칙 적용

정확한 속성 매핑을 통해 사용자 정보의 자동 동기화가 가능합니다.
</details>

<details>
<summary>7. 커스텀 SSO 정책은 어떻게 생성하나요?</summary>

커스텀 SSO 정책 생성 절차:

**정책 유형:**
- 에이전트용 커스텀 정책 (계정당 1개)
- 고객용 커스텀 정책 (계정당 1개)
- 전체 조직당 최대 5개 정책

**설정 단계:**
1. Admin > Security > Custom Policies 메뉴 접근
2. 새 정책 생성 및 이름 지정
3. 인증 방법 선택 (SAML, OAuth 등)
4. 커스텀 로그인 URL 설정

**정책 적용:**
- 기본 정책과 별도로 운영
- 특정 사용자 그룹에만 적용 가능
- 로그인 페이지에서 정책 선택

커스텀 정책을 통해 다양한 인증 요구사항을 충족할 수 있습니다.
</details>

<details>
<summary>8. Multi-Factor Authentication (MFA)은 어떻게 설정하나요?</summary>

MFA 설정 및 관리:

**지원되는 MFA 방법:**
- SMS 기반 OTP
- 이메일 기반 OTP
- 앱 기반 TOTP (Google Authenticator, Authy)
- 하드웨어 토큰

**설정 절차:**
1. Admin > Security > Multi-Factor Authentication
2. MFA 정책 활성화
3. 허용할 인증 방법 선택
4. 사용자별 또는 그룹별 적용

![Neo Admin Center Dashboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002090171/original/RMt5HlTd1B6AOXxxMLuwGBabpkBlOJ8wEg.png?1606215812)

*Neo Admin Center에서 패스워드 정책 및 보안 설정 관리*

**사용자 등록:**
- 초기 로그인 시 MFA 설정 안내
- 백업 코드 생성 및 안전 보관
- 분실 시 관리자 리셋 절차

MFA를 통해 계정 보안을 크게 향상시킬 수 있습니다.
</details>

## 고급 SSO 구성

<details>
<summary>9. Just-In-Time (JIT) 프로비저닝은 어떻게 작동하나요?</summary>

JIT 프로비저닝 동작 원리:

**자동 사용자 생성:**
- SSO 로그인 시 자동으로 사용자 계정 생성
- IdP에서 전달받은 속성 정보로 프로필 설정
- 사전 등록 없이도 즉시 서비스 이용 가능

**설정 방법:**
1. Admin > Security > SSO에서 JIT 활성화
2. 사용자 속성 매핑 구성
3. 기본 역할 및 권한 설정
4. 승인 프로세스 정의 (필요시)

**보안 고려사항:**
- 신뢰할 수 있는 IdP에서만 활성화
- 최소 권한 원칙 적용
- 정기적인 사용자 검토

JIT를 통해 사용자 관리 overhead를 크게 줄일 수 있습니다.
</details>

<details>
<summary>10. SCIM (System for Cross-domain Identity Management)은 어떻게 구성하나요?</summary>

SCIM 프로비저닝 구성:

**SCIM의 이점:**
- 실시간 사용자 프로비저닝/디프로비저닝
- 조직 변경사항 자동 반영
- 규모 있는 사용자 관리

**설정 단계:**
1. Admin > Security > User Provisioning에서 SCIM 활성화
2. SCIM 엔드포인트 URL 확인
3. Bearer 토큰 생성
4. IdP에서 SCIM 커넥터 구성

**지원되는 작업:**
- 사용자 생성 (CREATE)
- 사용자 정보 업데이트 (UPDATE)
- 사용자 비활성화 (DELETE)
- 그룹 멤버십 관리

SCIM을 통해 엔터프라이즈급 사용자 관리가 가능합니다.
</details>

<details>
<summary>11. 조건부 접근 제어는 어떻게 설정하나요?</summary>

조건부 접근 제어 구성:

**조건 유형:**
- 위치 기반 (IP 주소, 지역)
- 디바이스 기반 (관리되는 디바이스)
- 시간 기반 (업무 시간)
- 위험 기반 (비정상 로그인 패턴)

**설정 방법:**
1. IdP에서 조건부 접근 정책 생성
2. Freshservice 애플리케이션에 정책 적용
3. 조건 불충족 시 액션 정의
4. 예외 사용자/그룹 설정

**액션 옵션:**
- 접근 차단
- 추가 인증 요구
- 제한된 권한으로 접근 허용
- 관리자 알림

조건부 접근을 통해 세밀한 보안 제어가 가능합니다.
</details>

<details>
<summary>12. 세션 관리 및 타임아웃은 어떻게 설정하나요?</summary>

세션 관리 구성:

**세션 타임아웃 설정:**
- 유휴 타임아웃: 활동 없을 시 자동 로그아웃
- 절대 타임아웃: 최대 세션 지속 시간
- 개별 세션 vs 전역 세션 정책

**설정 위치:**
1. Admin > Security > Session Management
2. 타임아웃 값 설정 (분/시간 단위)
3. 사용자 그룹별 차등 적용
4. 경고 메시지 설정

**보안 강화 옵션:**
- 동시 세션 제한
- 디바이스별 세션 추적
- 의심스러운 활동 감지
- 강제 로그아웃 기능

적절한 세션 관리를 통해 보안과 사용성의 균형을 맞출 수 있습니다.
</details>

## 특정 IdP 연동

<details>
<summary>13. Microsoft Azure AD (Entra ID)와의 연동은 어떻게 하나요?</summary>

Azure AD 연동 설정:

**Azure AD 설정:**
1. Azure Portal에서 Enterprise Applications 메뉴 접근
2. 새 애플리케이션 추가 → 사용자 지정 애플리케이션
3. SAML 기반 Sign-on 구성
4. Freshservice 메타데이터 업로드

**사용자 및 그룹 할당:**
- Azure AD 그룹을 Freshservice 역할에 매핑
- 조건부 접근 정책 적용
- 자동 프로비저닝 구성

**고급 기능:**
- Seamless SSO 활성화
- Multi-tenant 지원
- B2B 게스트 사용자 관리
- PIM (Privileged Identity Management) 연동

Azure AD의 풍부한 기능을 활용하여 엔터프라이즈급 인증을 구현할 수 있습니다.
</details>

<details>
<summary>14. Google Workspace SSO는 어떻게 설정하나요?</summary>

Google Workspace 연동 절차:

**Google Admin Console 설정:**
1. Apps > Web and mobile apps 메뉴 접근
2. 새 커스텀 SAML 앱 추가
3. Freshservice 세부정보 입력
4. 속성 매핑 구성

**Freshservice 연동:**
- Google의 SSO URL 및 인증서 정보 입력
- 사용자 속성 매핑 검증
- 도메인 검증 완료

**Google 특화 기능:**
- Gmail 통합 인증
- Google Groups 동기화
- Mobile Device Management 연동
- Chrome 브라우저 정책 적용

Google Workspace의 통합 환경을 최대한 활용할 수 있습니다.
</details>

<details>
<summary>15. Okta SSO는 어떻게 구성하나요?</summary>

Okta 연동 구성:

**Okta 애플리케이션 설정:**
1. Okta Admin Console에서 Applications 메뉴
2. Browse App Catalog에서 Freshservice 검색
3. 애플리케이션 추가 및 기본 설정
4. Sign On 옵션에서 SAML 2.0 구성

**고급 설정:**
- Attribute Statements 설정
- Group Attribute Statements 구성
- Provisioning 활성화 (SCIM)
- Lifecycle Management 설정

**Okta 특화 기능:**
- Universal Directory 연동
- Adaptive Multi-Factor Authentication
- Behavior Detection
- API Access Management

Okta의 강력한 IAM 기능을 모두 활용할 수 있습니다.
</details>

<details>
<summary>16. ADFS (Active Directory Federation Services)와의 연동은 어떻게 하나요?</summary>

ADFS 연동 설정:

**ADFS 서버 구성:**
1. ADFS Management Console 접근
2. Relying Party Trust 추가
3. Freshservice 메타데이터 임포트
4. Claim Rules 구성

**Claim Rules 설정:**
- UPN → Email address 매핑
- SAM-Account-Name → Username 매핑
- Group SID → Role 매핑
- 커스텀 속성 추가

**보안 강화:**
- 인증서 기반 인증
- Multi-Factor Authentication
- Extranet Lockout Protection
- Device Registration Service

온프레미스 Active Directory와의 완벽한 연동이 가능합니다.
</details>

## 보안 및 컴플라이언스

<details>
<summary>17. SSO 보안 모범 사례는 무엇인가요?</summary>

SSO 보안 모범 사례:

**인증서 관리:**
- 정기적인 인증서 갱신
- 강력한 암호화 알고리즘 사용
- 인증서 체인 검증
- 백업 인증서 준비

**보안 설정:**
- 강력한 암호화 수준 (SHA-256, RSA-2048)
- 짧은 어설션 유효 기간
- 안전한 바인딩 방법
- 로그아웃 URL 설정

**모니터링:**
- 인증 이벤트 로깅
- 실패한 로그인 추적
- 비정상적인 패턴 감지
- 정기적인 보안 검토

**백업 계획:**
- 대체 인증 방법 준비
- 응급 접근 절차 수립
- 복구 계정 관리
- 재해 복구 테스트

체계적인 보안 관리를 통해 안전한 SSO 환경을 유지할 수 있습니다.
</details>

<details>
<summary>18. 컴플라이언스 요구사항은 어떻게 충족하나요?</summary>

컴플라이언스 준수 방안:

**GDPR 준수:**
- 사용자 동의 관리
- 데이터 처리 목적 명시
- 개인정보 삭제 권리 보장
- 데이터 이동성 지원

**SOX 준수:**
- 접근 제어 문서화
- 정기적인 접근 권한 검토
- 감사 로그 보관
- 직무 분리 원칙 적용

**HIPAA 준수:**
- PHI 접근 제어
- 암호화된 데이터 전송
- 최소 권한 원칙
- 사용자 활동 추적

**ISO 27001 준수:**
- 정보보안 정책 수립
- 위험 평가 및 관리
- 인시던트 대응 절차
- 지속적인 개선

각 규정에 맞는 설정과 절차를 통해 컴플라이언스를 달성할 수 있습니다.
</details>

<details>
<summary>19. 감사 로그 및 모니터링은 어떻게 설정하나요?</summary>

감사 로그 및 모니터링 구성:

**로그 수집 범위:**
- 로그인/로그아웃 이벤트
- 인증 실패 및 성공
- 권한 변경 사항
- 세션 생성/종료

**로그 분석:**
1. Admin > Reports > Security Logs 접근
2. 필터 조건 설정 (시간, 사용자, 이벤트 유형)
3. 이상 패턴 식별
4. 정기적인 리포트 생성

**실시간 모니터링:**
- 실패한 로그인 시도 알림
- 비정상적인 접근 패턴 감지
- 권한 에스컬레이션 탐지
- 지역별 접근 이상 감지

**SIEM 연동:**
- Splunk, ELK Stack 등과 연동
- API를 통한 로그 스트리밍
- 자동화된 위협 탐지
- 사고 대응 워크플로우

체계적인 모니터링을 통해 보안 위협을 사전에 감지할 수 있습니다.
</details>

<details>
<summary>20. 데이터 암호화 및 전송 보안은 어떻게 보장하나요?</summary>

데이터 보안 보장 방법:

**전송 중 암호화:**
- TLS 1.2 이상 사용 강제
- HTTPS 리다이렉션 설정
- HSTS (HTTP Strict Transport Security) 적용
- 인증서 핀닝 구현

**저장 중 암호화:**
- AES-256 암호화
- 키 관리 시스템 (KMS) 연동
- 정기적인 키 로테이션
- 백업 데이터 암호화

**SAML 암호화:**
- 어설션 암호화
- 서명 검증
- 암호화 키 교환
- 메시지 무결성 보장

**API 보안:**
- OAuth 2.0 토큰
- API 키 관리
- Rate Limiting
- IP 화이트리스팅

다중 계층 보안을 통해 데이터를 완벽하게 보호할 수 있습니다.
</details>

## 문제 해결 및 최적화

<details>
<summary>21. 일반적인 SSO 로그인 오류는 어떻게 해결하나요?</summary>

일반적인 SSO 오류 해결:

**"SAML Response not found" 오류:**
- IdP 설정에서 POST 바인딩 확인
- 어설션 소비자 URL 검증
- 네트워크 방화벽 설정 점검

**"Invalid SAML Response" 오류:**
- 인증서 만료일 확인
- 시간 동기화 검증 (NTP)
- 어설션 유효 기간 설정 확인

**사용자 속성 매핑 오류:**
- IdP에서 전송되는 속성 확인
- Freshservice 필드 매핑 검증
- 대소문자 구분 확인

**권한 부족 오류:**
- 사용자 그룹 매핑 확인
- 기본 역할 설정 검토
- JIT 프로비저닝 설정 점검

체계적인 진단을 통해 대부분의 오류를 신속하게 해결할 수 있습니다.
</details>

<details>
<summary>22. SSO 성능 최적화는 어떻게 하나요?</summary>

SSO 성능 최적화 방법:

**어설션 캐싱:**
- IdP에서 어설션 캐시 시간 조정
- Freshservice 세션 타임아웃 최적화
- 중복 인증 요청 방지

**네트워크 최적화:**
- CDN을 통한 메타데이터 배포
- 지역별 IdP 엔드포인트 설정
- 압축 및 최적화된 프로토콜 사용

**데이터베이스 최적화:**
- 사용자 조회 쿼리 최적화
- 인덱스 최적화
- 커넥션 풀 설정

**모니터링 지표:**
- 평균 로그인 시간
- 인증 성공률
- 네트워크 지연 시간
- 서버 응답 시간

지속적인 모니터링과 튜닝을 통해 최적의 성능을 유지할 수 있습니다.
</details>

<details>
<summary>23. 멀티 도메인 환경에서의 SSO는 어떻게 관리하나요?</summary>

멀티 도메인 SSO 관리:

**도메인 설정:**
- 각 도메인별 SAML 엔드포인트 구성
- 도메인별 인증서 관리
- 서브도메인 정책 설정

**사용자 라우팅:**
- 이메일 도메인 기반 자동 라우팅
- 사용자 선택 기반 IdP 선택
- 기본 IdP 설정

**통합 관리:**
- 중앙집중식 정책 관리
- 도메인 간 사용자 이동
- 통합 감사 로그

**보안 고려사항:**
- 도메인별 보안 정책
- 크로스 도메인 세션 관리
- 도메인 격리 정책

복잡한 조직 구조에서도 효율적인 SSO 관리가 가능합니다.
</details>

<details>
<summary>24. 모바일 디바이스에서의 SSO는 어떻게 작동하나요?</summary>

모바일 SSO 구현:

**앱 기반 SSO:**
- 네이티브 앱에서 웹뷰를 통한 SSO
- Deep Link를 통한 자동 리다이렉션
- 생체 인증 연동 (지문, Face ID)

**브라우저 기반 SSO:**
- 모바일 브라우저에서 일반 SSO 플로우
- 쿠키 공유를 통한 자동 로그인
- Progressive Web App (PWA) 지원

**디바이스 관리:**
- MDM (Mobile Device Management) 연동
- 디바이스 인증서 기반 인증
- 앱 보호 정책 적용

**보안 강화:**
- 디바이스 등록 요구
- 위치 기반 접근 제어
- 원격 데이터 삭제 기능

모바일 환경에서도 안전하고 편리한 SSO 경험을 제공할 수 있습니다.
</details>

## 고급 통합 및 자동화

<details>
<summary>25. API를 통한 SSO 관리는 어떻게 하나요?</summary>

API 기반 SSO 관리:

**사용자 관리 API:**
- 프로그래매틱 사용자 생성/수정/삭제
- 대량 사용자 가져오기/내보내기
- 사용자 속성 동기화
- 그룹 멤버십 관리

**설정 관리 API:**
- SSO 구성 자동화
- 인증서 갱신 자동화
- 정책 템플릿 배포
- 백업 및 복원

**모니터링 API:**
- 실시간 인증 상태 확인
- 로그 데이터 스트리밍
- 메트릭 수집 및 분석
- 알림 및 경고 관리

**보안 고려사항:**
- API 키 관리 및 로테이션
- Rate Limiting 설정
- IP 제한 및 액세스 제어
- 감사 로그 관리

API를 통해 대규모 환경에서의 효율적인 SSO 관리가 가능합니다.
</details>

<details>
<summary>26. 하이브리드 클라우드 환경에서의 SSO는 어떻게 구현하나요?</summary>

하이브리드 클라우드 SSO 구현:

**아키텍처 설계:**
- 온프레미스 IdP와 클라우드 서비스 연동
- 네트워크 연결성 보장 (VPN, ExpressRoute)
- 페더레이션 신뢰 관계 설정

**ID 브릿지 구성:**
- Azure AD Connect 또는 유사 도구 사용
- 디렉토리 동기화 설정
- 패스워드 해시 동기화

**보안 경계 관리:**
- 클라우드와 온프레미스 간 보안 정책 일관성
- 네트워크 세그멘테이션
- 데이터 분류 및 보호

**재해 복구:**
- 다중 IdP 페일오버
- 백업 인증 경로
- 연결 중단 시 대응 절차

하이브리드 환경에서도 완벽한 SSO 통합이 가능합니다.
</details>

<details>
<summary>27. 자동화된 사용자 라이프사이클 관리는 어떻게 구현하나요?</summary>

자동화된 라이프사이클 관리:

**온보딩 자동화:**
- HR 시스템과 연동한 자동 계정 생성
- 역할 기반 자동 권한 할당
- 환영 이메일 및 교육 자료 자동 발송

**권한 관리:**
- 조직 변경 시 자동 권한 업데이트
- 정기적인 접근 권한 검토 자동화
- 임시 권한의 자동 만료

**오프보딩 자동화:**
- 퇴사자 계정 자동 비활성화
- 모든 세션 강제 종료
- 데이터 보관 정책 자동 적용

**컴플라이언스:**
- SOD (Segregation of Duties) 자동 검증
- 감사 보고서 자동 생성
- 규정 위반 자동 탐지

완전한 자동화를 통해 인적 오류를 최소화하고 효율성을 극대화할 수 있습니다.
</details>

<details>
<summary>28. 제로 트러스트 아키텍처에서의 SSO는 어떻게 구현하나요?</summary>

제로 트러스트 SSO 구현:

**핵심 원칙:**
- "신뢰하지 말고 검증하라"
- 모든 요청에 대한 지속적인 검증
- 최소 권한 원칙 적용
- 마이크로 세그멘테이션

**동적 인증:**
- 컨텍스트 기반 인증 결정
- 실시간 위험 평가
- 적응형 인증 요구
- 지속적인 세션 검증

**ID 확인:**
- 디바이스 신뢰도 검증
- 사용자 행동 분석
- 지리적 위치 검증
- 시간 기반 접근 제어

**통합 모니터링:**
- 모든 접근 시도 로깅
- 실시간 위협 탐지
- 자동화된 대응 조치
- 포렌식 분석 지원

제로 트러스트를 통해 최고 수준의 보안을 달성할 수 있습니다.
</details>

## 비즈니스 연속성 및 운영

<details>
<summary>29. SSO 재해 복구 계획은 어떻게 수립하나요?</summary>

SSO 재해 복구 계획:

**복구 시나리오:**
- 주 IdP 서비스 중단
- 네트워크 연결 장애
- 인증서 만료 또는 손상
- 대규모 보안 침해

**백업 인증 방법:**
- 로컬 관리자 계정 유지
- 백업 IdP 설정
- 임시 패스워드 시스템
- 오프라인 인증 방법

**복구 절차:**
1. 사고 감지 및 평가
2. 백업 시스템 활성화
3. 사용자 커뮤니케이션
4. 서비스 복원 및 검증
5. 사후 분석 및 개선

**테스트 및 훈련:**
- 정기적인 재해 복구 훈련
- 복구 시간 목표 (RTO) 설정
- 복구 지점 목표 (RPO) 정의
- 문서화 및 업데이트

완벽한 재해 복구 계획을 통해 비즈니스 연속성을 보장할 수 있습니다.
</details>

<details>
<summary>30. 대규모 조직에서의 SSO 거버넌스는 어떻게 관리하나요?</summary>

대규모 SSO 거버넌스:

**거버넌스 구조:**
- 중앙 ID 관리 팀
- 부서별 ID 관리자
- 보안 정책 위원회
- 감사 및 컴플라이언스 팀

![Organization Management](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002090235/original/5sYD1HlhVY3pUmJ794nqXE8LsirD5FW0YA.png?1606216437)

*Neo Admin Center를 통한 조직 전체 사용자 및 계정 관리*

**정책 관리:**
- 표준화된 ID 정책
- 역할 기반 접근 제어 매트릭스
- 권한 승인 워크플로우
- 정기적인 정책 검토

**위험 관리:**
- ID 관련 위험 평가
- 비즈니스 영향 분석
- 위험 완화 전략
- 인시던트 대응 계획

**성과 측정:**
- SSO 채택률 추적
- 보안 인시던트 분석
- 사용자 만족도 조사
- 비용 효익 분석

체계적인 거버넌스를 통해 대규모 조직에서도 효과적인 SSO 관리가 가능합니다.
</details>

