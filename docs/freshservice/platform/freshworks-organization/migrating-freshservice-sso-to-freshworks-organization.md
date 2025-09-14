---
sidebar_position: 2
---

# Freshservice SSO를 Freshworks Organization으로 마이그레이션

기존 Freshservice SSO 설정을 Freshworks Organization으로 마이그레이션하는 과정은 사용자 경험을 개선하고 보안을 강화하는 중요한 단계입니다. 이 문서는 원활한 마이그레이션을 위한 단계별 가이드를 제공합니다.

:::warning 마이그레이션 필수사항
마이그레이션 과정에서 사용자의 서비스 중단을 최소화하기 위해 사전 계획과 준비가 필요합니다.
:::

## 📋 마이그레이션 개요

### 주요 변경사항

- **통합 인증 시스템**: 개별 Freshservice SSO에서 Freshworks Organization 중앙 인증으로 전환
- **URL 변경**: 로그인 URL이 `domain.freshservice.com`에서 `organization.myfreshworks.com`으로 변경
- **정책 통합**: 여러 제품의 인증 정책이 하나의 중앙 정책으로 통합

### 지원되는 SSO 유형

1. **SAML 2.0**: Active Directory, Okta, OneLogin 등
2. **OAuth 2.0**: Google, Microsoft 365 등
3. **OpenID Connect (OIDC)**: 최신 표준 지원
4. **JWT**: 커스텀 토큰 기반 인증

## 🔄 마이그레이션 단계

### 1단계: 현재 SSO 설정 검토

#### 현재 설정 확인
1. **관리자 → 사용자 → 로그인 및 보안** 메뉴에서 현재 SSO 설정 확인
2. 인증서, 메타데이터, 엔드포인트 URL 등 현재 구성 정보 백업
3. 사용자 매핑 규칙 및 속성 매핑 정보 저장

#### 영향 분석
- 현재 SSO를 사용하는 사용자 수 파악
- 통합될 다른 Freshworks 제품 확인
- 다운타임 영향을 받을 업무 프로세스 식별

### 2단계: Freshworks Organization 설정

#### 조직 생성 및 구성
1. [Freshworks Organization](https://organization.freshworks.com) 접속
2. 조직 관리자 계정으로 로그인
3. **보안 → SSO 정책** 메뉴에서 새 정책 생성

#### SSO 정책 구성
```yaml
정책 이름: [조직명] 통합 SSO 정책
인증 방식: SAML 2.0 / OAuth 2.0 / OIDC
사용자 프로비저닝: 자동 / 수동
속성 매핑:
  - 이메일: email
  - 이름: given_name
  - 성: family_name
  - 부서: department
```

### 3단계: IdP(Identity Provider) 재구성

#### SAML 2.0 구성 예시 (Active Directory)

**새로운 ACS URL**:
```
https://organization.myfreshworks.com/auth/saml/callback
```

**Entity ID**:
```
https://organization.myfreshworks.com
```

**속성 매핑**:
- `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` → 이메일
- `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname` → 이름
- `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname` → 성

#### OAuth 2.0 구성 예시 (Google)

**리다이렉트 URI**:
```
https://organization.myfreshworks.com/auth/oauth/google/callback
```

**스코프**:
```
openid email profile
```

### 4단계: 테스트 및 검증

#### 테스트 계정 생성
1. 조직에 테스트 사용자 추가
2. SSO 로그인 프로세스 테스트
3. 제품별 액세스 권한 확인

#### 검증 체크리스트
- [ ] SSO 로그인 성공
- [ ] 사용자 속성 정확한 매핑
- [ ] Freshservice 접근 권한 유지
- [ ] 다른 Freshworks 제품 액세스 (해당하는 경우)

### 5단계: 프로덕션 마이그레이션

#### 순차적 마이그레이션
1. **소규모 그룹 우선**: IT 팀 등 우선 마이그레이션
2. **단계별 확장**: 부서별로 점진적 마이그레이션
3. **전체 적용**: 모든 사용자 대상 완료

#### 마이그레이션 체크리스트
- [ ] 사용자 사전 안내 완료
- [ ] DNS 설정 업데이트 (필요시)
- [ ] 모니터링 시스템 준비
- [ ] 롤백 계획 수립

## 🏢 실무 활용 예시

## ⚠️ 주의사항 및 문제 해결

### 일반적인 문제

#### 문제: 속성 매핑 오류
**원인**: IdP와 Freshworks Organization 간 속성명 불일치
**해결**:
1. IdP에서 전송되는 속성명 확인
2. Freshworks Organization에서 올바른 매핑 설정
3. 테스트 사용자로 매핑 검증

#### 문제: 사용자 중복 생성
**원인**: 이메일 주소 불일치로 인한 새 계정 생성
**해결**:
1. 기존 사용자 계정의 이메일 주소 정규화
2. IdP에서 일관된 이메일 형식 사용
3. 중복 계정 병합 프로세스 실행

#### 문제: 접근 권한 손실
**원인**: 마이그레이션 과정에서 역할/권한 정보 누락
**해결**:
1. 마이그레이션 전 모든 사용자 권한 백업
2. Freshworks Organization에서 역할 기반 액세스 제어 재설정
3. 사용자별 권한 검증 및 복원

### 모니터링 및 유지보수

#### 성능 모니터링
- SSO 로그인 성공률 추적
- 평균 인증 시간 모니터링
- 오류 로그 정기 검토

#### 정기 점검
- 인증서 만료일 관리
- IdP 연결 상태 확인
- 사용자 액세스 패턴 분석

:::success 마이그레이션 완료
SSO 마이그레이션이 성공적으로 완료되었습니다. 이제 중앙집중화된 인증 시스템의 이점을 활용할 수 있습니다.
:::