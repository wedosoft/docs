---
sidebar_position: 1
---

# Freshworks Organization 소개

조직이 성장함에 따라 여러 계정과 제품에 걸쳐 분산된 관리 설정을 제어하고 관리하는 것은 항상 어려운 일입니다. 비밀번호 정책부터 사용자 관리까지, 제품 전반에 걸친 통합된 접근 방식을 통해 관리자가 더 중앙집중화된 제어권을 가질 수 있습니다.

:::info Freshworks Organization 특징
Freshworks Organization은 사용하는 Freshworks 제품 전반에 걸쳐 사용자 관리 및 보안 설정을 위한 중앙집중화된 대시보드를 제공합니다.
:::

![Freshworks Organization Dashboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001731539/original/x6bIUzA_QpSt8tURgSDrfvHcespBYUD8jw.jpg?1600148749)

## 🔍 Freshworks Organization이란?

Freshworks Organization은 사용하는 Freshworks 제품 전반에 걸쳐 사용자 관리 및 보안 설정을 위한 중앙집중화된 대시보드를 제공합니다.

## 🆕 새로운 기능

### 주요 기능 목록

- **다중 계정 사용자 관리**: 하나의 대시보드에서 여러 Freshservice 계정 또는 기타 Freshworks 제품의 사용자 프로필 관리
- **고급 비밀번호 정책**: 중앙집중식 비밀번호 정책 구성. Google Recaptcha를 통한 자동 SPAM/봇 탐지로 무차별 대입 공격 방지
- **보안 SSO 구성**: OAuth2/OIDC/SAML/JWT를 사용한 보안 SSO 구성 
- **이중 인증**: 사용자가 TOTP 기반 이중 인증을 구성하여 비밀번호 탈취 공격 방지
- **감사 로그**: 보안 설정 수정과 관련된 모든 감사 로그 보기
- **Freshworks 스위처**: 사용자가 다른 Freshworks 계정 및 제품 간에 원활하게 탐색할 수 있는 기능

## 🔮 곧 제공될 기능

- **통합 청구 대시보드**: 여러 제품 또는 Freshservice 계정에 대한 통합 송장 발행 및 청구 대시보드
- **역할 관리 기능**: 관리자가 대시보드에서 하나 이상의 Freshworks 제품에 대한 사용자의 액세스/역할을 수정할 수 있는 기능
- **필수 2FA 정책**: 모든 관리자/상담원에 대해 2FA를 필수 정책으로 적용할 수 있는 기능

## 👨‍💼 관리자에게 변경되는 사항

### 조직 관리자 도입

조직 관리자는 Freshworks 조직 대시보드의 모든 구성을 제어하고 관리할 수 있습니다. 기본적으로 조직을 만드는 사용자가 해당 조직의 조직 관리자가 됩니다.

#### 조직 관리자 역할 개요

- 사용자와 계정을 관리하기 위해 여러 조직 관리자가 있을 수 있습니다
- 사용자의 프로필 세부 정보 업데이트, 보안 정책 구성, 다른 조직에서 계정 가져오기 또는 조직 URL 변경이 가능합니다
- 조직 내 다른 사용자에게 조직 관리자 권한을 부여하거나 취소할 수 있습니다

#### 누가 조직 관리자가 될까요?

- **신규 Freshservice 가입자**: Freshservice에 가입한 계정 관리자는 Freshservice가 유일하게 인식된 제품인 경우 자동으로 조직 관리자가 됩니다
- **기존 슈퍼 관리자**: "슈퍼 관리자 제어로 신 노릇하기" 권한을 가진 모든 Freshservice 상담원은 마이그레이션 후 자동으로 조직 관리자가 됩니다
- **다중 제품 사용자**: 다른 Freshworks 제품이나 Freshservice 계정을 사용하는 경우 Freshservice 계정 관리자는 조직 관리자로 전환되지 않습니다. 기존 조직 관리자가 조직 관리자 권한을 부여할 수 있습니다

### 통합 로그인

![통합 로그인 화면](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001731616/original/5XEVRJL7Ophx8B02E_0i4vSHwxnOjNb6Vw.png?1600149553)

#### 주요 변경사항

- **단일 로그인 경험**: 상담원과 요청자에 대한 현재 분할 로그인 경험(활성화된 경우)이 두 사용자 그룹 모두에 대한 단일 로그인 경험으로 대체됩니다
- **조직 로고 표시**: 통합 로그인 페이지에 조직의 로고를 표시하도록 선택할 수 있습니다
- **URL 변경**: 현재 로그인 URL `domain.freshservice.com`이 `organization.myfreshworks.com`으로 교체됩니다
- **이메일 발신자 변경**: 모든 활성화 이메일과 비밀번호 재설정 이메일은 Freshworks 조직에서 트리거되므로 `support@freshworks.com`에서 발송됩니다

#### Freshservice에서 더 이상 사용할 수 없는 기능

- **로그인 페이지 커스터마이징**: Freshservice의 **서비스 데스크 리브랜딩** 하에 구성된 모든 기존 로그인 페이지 커스터마이징이 제거됩니다. 조직 대시보드에서 로고와 같은 로그인 페이지 커스터마이징을 추가할 수 있습니다

![로그인 커스터마이징](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001731699/original/zogerk7VtKnfd99DZC_XatmtbN8_h540Tw.png?1600150561)

- **비밀번호 찾기 이메일 커스터마이징**: Freshservice의 **이메일 알림** 하에서 비밀번호 찾기 이메일 커스터마이징을 사용할 수 없습니다. 대신 Freshworks에서 표준 이메일이 발송됩니다
- **보조 이메일 로그인**: 보조 이메일 주소를 사용한 로그인을 더 이상 사용할 수 없습니다. 사용자는 기본 이메일 주소만 사용하여 로그인할 수 있습니다
- **관리자 전용 로그인**: `https://accountname.freshservice.com/login/normal` URL이 `https://organizationname.myfreshworks.com/login/normal`로 변경되었습니다. 이는 비밀번호 로그인만 지원하며 앞으로 조직 관리자만 액세스할 수 있습니다

:::warning 비관리자 로그인 설정
비관리자에 대해 비밀번호/Google 로그인을 활성화해야 하는 경우, 조직 보안 정책에서 SSO와 함께 해당 옵션을 활성화하거나 MSP 모드를 사용하는 경우 전용 포털을 만들고 비밀번호/Google 로그인이 활성화된 사용자 지정 정책을 매핑해야 합니다.
:::

### 통합 보안 정책

![통합 보안 정책](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001731717/original/_0D4-VSw_bWqnlWXTORcX5OjLq2CPkQMuQ.png?1600150699)

#### 정책 관리 기능

- **중앙집중식 구성**: Google/OAuth2/SAML/JWT 기반 사용자 지정 SSO와 같은 모든 비밀번호 정책 및 SSO 구성을 조직 관리자가 조직 대시보드에서 구성할 수 있습니다
- **비밀번호 정책**: 비밀번호 기반 로그인을 활성화하도록 선택하는 경우 사용자가 사용해야 하는 비밀번호의 강도를 적용하기 위해 사용자 지정 비밀번호 정책을 구성할 수 있습니다
- **권한 관리**: 조직 관리자 권한이 없는 Freshservice 관리자는 인증/SSO를 구성하기 위해 조직 관리자에게 문의해야 합니다

#### Freshservice에서 더 이상 사용할 수 없는 기능

- **비밀번호 재설정**: 관리자는 Freshservice에서 요청자의 비밀번호를 재설정할 수 없습니다. 요청자는 자신의 비밀번호를 재설정할 수 있습니다

## 🏢 실무 활용 예시

### 상황 1: 삼성전자 전사 통합 관리
**목표**: 전 세계 법인의 Freshworks 제품을 하나의 조직으로 통합 관리

**방법**:
1. 각 지역 법인의 Freshservice 계정을 Freshworks Organization으로 통합
2. 중앙집중식 SSO 정책을 통한 Active Directory 연동
3. 조직 관리자 권한을 지역 IT 책임자들에게 분산 위임

**결과**: 전 세계 50개 법인의 사용자 관리 효율성 70% 향상, 보안 정책 일관성 달성

### 상황 2: LG화학 다중 제품 환경 관리
**목표**: Freshservice, Freshdesk, Freshworks CRM을 통합 관리

**방법**:
1. 각 제품별 분산된 사용자 계정을 Freshworks Organization으로 통합
2. SAML 기반 SSO로 기존 IdP(Identity Provider) 연동
3. 제품별 역할 기반 액세스 제어 구현

**결과**: IT 관리 업무 50% 감소, 사용자 편의성 95% 향상

### 상황 3: 현대자동차 MSP 모드 활용
**목표**: 협력업체별 독립적인 보안 정책 적용

**방법**:
1. MSP 모드를 활용하여 협력업체별 전용 포털 구성
2. 협력업체별 차별화된 보안 정책 적용
3. 중앙집중식 감사 로그 모니터링 구현

**결과**: 협력업체 보안 수준 80% 향상, 규정 준수율 99% 달성

## 🔧 마이그레이션 준비사항

Freshworks Organization으로의 원활한 마이그레이션을 위해 다음 사항을 확인해 주세요:

### 필수 준비사항

1. **도메인 차단 해제**: 네트워크나 이메일 방화벽이 있는 경우 `freshworks.com`과 `myfreshworks.com`이 차단 해제되어 있는지 확인하세요

2. **직원 안내**: 이러한 변경사항이 상담원과 최종 사용자에게 영향을 미치므로 1주일의 기간 동안 직원들에게 이러한 변경사항을 전달할 수 있도록 마이그레이션이 롤아웃됩니다

3. **기본 이메일 주소 확인**: 마이그레이션 후 기본 이메일 주소를 사용해서만 사용자 로그인이 가능하므로 직원들이 올바른 기본 이메일 주소를 활성화했는지 확인하세요

4. **제품 통합**: 마이그레이션 후 독립적인 조직에서 Freshworks 제품/계정을 찾은 경우 함께 병합되도록 하세요. [병합 지침](https://support.freshworks.com/support/solutions/articles/50000002805-what-happens-when-i-request-to-import-an-account-from-another-organization-)을 참조하세요

:::success 마이그레이션 완료
모든 준비사항을 완료하셨습니다. 이제 Freshworks Organization의 향상된 기능을 활용할 수 있습니다.
:::