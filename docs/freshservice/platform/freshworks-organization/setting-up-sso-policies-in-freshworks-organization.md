---
sidebar_position: 3
---

# Freshworks Organization SSO 정책 설정

Freshworks Organization에서 SSO(Single Sign-On) 정책을 설정하여 조직 전체의 인증을 중앙집중화하고 보안을 강화할 수 있습니다. 이 문서는 다양한 SSO 방식의 설정 방법을 상세히 안내합니다.

:::info 지원되는 SSO 방식
- SAML 2.0
- OAuth 2.0 (Google, Microsoft)
- OpenID Connect (OIDC)
- JWT (JSON Web Token)
:::

## 🔐 SSO 정책 개요

### SSO 정책이란?

SSO 정책은 조직 내 모든 Freshworks 제품에 대한 인증 방식을 정의하는 규칙입니다. 하나의 정책으로 여러 제품에 동일한 인증 경험을 제공할 수 있습니다.

### 주요 장점

- **중앙집중화된 관리**: 하나의 위치에서 모든 제품의 인증 관리
- **일관된 사용자 경험**: 모든 제품에서 동일한 로그인 프로세스
- **향상된 보안**: 통합된 보안 정책 적용
- **간편한 사용자 관리**: 자동 프로비저닝 및 디프로비저닝

## 🚀 SSO 정책 설정 방법

### 1단계: Freshworks Organization 접속

1. [https://organization.myfreshworks.com](https://organization.myfreshworks.com) 접속
2. 조직 관리자 계정으로 로그인
3. **보안** → **SSO 정책** 메뉴 선택

### 2단계: 새 SSO 정책 생성

1. **새 정책 생성** 버튼 클릭
2. 정책 이름 입력 (예: "회사명 통합 SSO")
3. 설명 추가 (선택사항)
4. 인증 방식 선택

## 🔧 인증 방식별 설정 가이드

### SAML 2.0 설정

#### 기본 정보 구성

| 필드 | 설명 | 예시 |
|------|------|------|
| IdP 엔티티 ID | Identity Provider의 고유 식별자 | `https://company.okta.com` |
| SSO URL | SAML 인증 요청을 받는 IdP 엔드포인트 | `https://company.okta.com/app/saml/sso` |
| X.509 인증서 | IdP에서 제공하는 공개 인증서 | 인증서 파일 업로드 |

#### 고급 설정

```xml
<!-- 속성 매핑 예시 -->
<saml:AttributeStatement>
  <saml:Attribute Name="email">
    <saml:AttributeValue>user@company.com</saml:AttributeValue>
  </saml:Attribute>
  <saml:Attribute Name="firstName">
    <saml:AttributeValue>홍길동</saml:AttributeValue>
  </saml:Attribute>
  <saml:Attribute Name="department">
    <saml:AttributeValue>개발팀</saml:AttributeValue>
  </saml:Attribute>
</saml:AttributeStatement>
```

### OAuth 2.0 설정 (Google)

#### 구성 매개변수

| 필드 | 값 |
|------|-----|
| 클라이언트 ID | Google Cloud Console에서 생성된 클라이언트 ID |
| 클라이언트 시크릿 | 해당 클라이언트의 시크릿 키 |
| 리다이렉트 URI | `https://organization.myfreshworks.com/auth/oauth/google/callback` |
| 스코프 | `openid email profile` |

#### Google Workspace 설정

1. Google Admin Console 접속
2. **보안** → **API 제어** → **도메인 소유 앱** 설정
3. Freshworks Organization 앱 신뢰할 수 있는 앱으로 추가

### OpenID Connect (OIDC) 설정

#### 필수 구성 요소

```json
{
  "issuer": "https://identity-provider.com",
  "authorization_endpoint": "https://identity-provider.com/oauth/authorize",
  "token_endpoint": "https://identity-provider.com/oauth/token",
  "userinfo_endpoint": "https://identity-provider.com/oauth/userinfo",
  "jwks_uri": "https://identity-provider.com/.well-known/jwks.json"
}
```

#### 클레임 매핑

| OIDC 클레임 | Freshworks 속성 |
|-------------|------------------|
| `sub` | 사용자 고유 ID |
| `email` | 이메일 주소 |
| `given_name` | 이름 |
| `family_name` | 성 |
| `preferred_username` | 사용자명 |

### JWT 설정

#### JWT 토큰 구조

```json
{
  "header": {
    "alg": "RS256",
    "typ": "JWT"
  },
  "payload": {
    "iss": "company-sso",
    "sub": "user123",
    "email": "user@company.com",
    "name": "홍길동",
    "exp": 1234567890
  }
}
```

#### 서명 키 설정

1. RSA 공개 키 업로드
2. 서명 알고리즘 선택 (RS256 권장)
3. 토큰 만료 시간 설정

## 🔄 사용자 프로비저닝 설정

### 자동 프로비저닝

#### JIT (Just-In-Time) 프로비저닝

```yaml
자동 계정 생성: 활성화
기본 역할: 요청자
속성 기반 역할 매핑:
  - department == "IT" → 상담원
  - department == "Admin" → 관리자
```

#### 속성 기반 그룹 할당

| 속성 | 조건 | 할당 그룹 |
|------|------|-----------|
| department | IT | IT 지원팀 |
| location | Seoul | 서울 지사 |
| job_title | Manager | 관리자 그룹 |

### 수동 프로비저닝

1. 관리자가 직접 사용자 계정 생성
2. SSO 로그인 시 기존 계정과 연결
3. 역할 및 권한 수동 할당

## 🏢 실무 활용 예시

### 상황 1: 삼성전자 SAML 통합
**목표**: Active Directory Federation Services를 통한 통합 인증

**구성**:
```xml
<!-- AD FS 클레임 규칙 -->
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
=> issue(Type = "email", Value = c.Value + "@samsung.com");

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
=> issue(Type = "firstName", Value = c.Value);
```

**결과**: 15,000명 직원의 원클릭 접근, IT 지원 요청 70% 감소

### 상황 2: LG화학 Google Workspace 연동
**목표**: Google 계정을 활용한 seamless 인증

**구성**:
- 도메인 제한: `@lgchem.com`
- 자동 그룹 매핑: Google Groups → Freshworks 그룹
- 2FA 강제 적용

**결과**: 신규 직원 온보딩 시간 80% 단축

### 상황 3: 현대자동차 하이브리드 환경
**목표**: 내부 직원(SAML) + 협력업체(OAuth) 동시 지원

**구성**:
```yaml
정책 1 - 내부 직원:
  방식: SAML 2.0
  도메인: "@hyundai.com"
  IdP: Hyundai AD FS

정책 2 - 협력업체:
  방식: Google OAuth
  도메인 제한: 없음
  승인 프로세스: 관리자 승인 필요
```

**결과**: 복합 사용자 환경에서 99.9% 인증 성공률 달성

## ⚠️ 보안 고려사항

### 인증서 관리

#### 인증서 로테이션
- 정기적인 인증서 갱신 (연 1회 권장)
- 만료 90일 전 알림 설정
- 백업 인증서 준비

#### 보안 강화 설정
```yaml
보안 옵션:
  강제 HTTPS: 활성화
  토큰 만료 시간: 8시간
  세션 타임아웃: 24시간
  다중 브라우저 로그인: 제한
```

### 액세스 제어

#### IP 제한
```yaml
허용 IP 범위:
  - 192.168.1.0/24    # 본사 네트워크
  - 10.0.0.0/16       # VPN 대역
  - 203.xxx.xxx.xxx   # 지사 고정 IP
```

#### 디바이스 제한
- 신뢰할 수 있는 디바이스만 허용
- 디바이스 등록 필수
- 정기적인 디바이스 감사

## 🔍 모니터링 및 문제 해결

### 로그 모니터링

#### 주요 모니터링 지표
- SSO 로그인 성공률
- 평균 인증 시간
- 실패한 로그인 시도
- 속성 매핑 오류

### 일반적인 문제

#### 문제: 속성 매핑 실패
**해결 방법**:
1. IdP에서 전송하는 속성 확인
2. 대소문자 정확히 매칭
3. 테스트 사용자로 검증

#### 문제: 인증서 오류
**해결 방법**:
1. 인증서 형식 확인 (PEM, X.509)
2. 인증서 체인 완전성 검사
3. 만료일 확인

:::tip 설정 완료 확인
모든 설정이 완료되면 테스트 사용자로 로그인을 시도하여 정상 작동을 확인하세요.
:::

:::success SSO 정책 설정 완료
SSO 정책이 성공적으로 설정되었습니다. 이제 조직 전체에서 통합된 인증 경험을 제공할 수 있습니다.
:::