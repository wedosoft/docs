---
sidebar_position: 9
---

# SPF 레코드 생성하기

SPF(Sender Policy Framework) 레코드는 지정된 도메인에서 전송된 이메일이 이메일 클라이언트에 의해 스팸으로 표시되지 않도록 보장합니다. 지원 이메일 설정 외에도 때로는 도메인 이름 등록업체와 함께 SPF 레코드를 생성하여 모든 이메일이 제대로 전달되도록 해야 합니다. DNS를 수정하여 몇 분 만에 빠르게 완료할 수 있습니다.

## SPF 레코드 생성 방법

### 1단계: 도메인 등록업체 웹사이트 접속

도메인 등록업체의 웹사이트로 이동합니다.

### 2단계: 도메인 제어판 로그인

도메인 제어판에 로그인합니다.

### 3단계: DNS 구성 설정 열기

DNS 구성 설정을 엽니다.

### 4단계: ZONE 파일 편집

ZONE 파일을 편집하고 TXT 또는 SPF 레코드를 찾습니다.

### 5단계: SPF 값 지정

다음 값을 지정합니다: **`v=spf1 include:email.freshservice.com ~all`**

### 6단계: 변경사항 저장

변경사항을 **저장**합니다.

## 기존 SPF 레코드가 있는 경우

기존 레코드와 같은 라인에 SPF를 포함할 수 있습니다:

```
v=spf1 include:spf1.domain.com include:spf2.domain2.com include:email.freshservice.com ~all
```

이제 어려움 없이 Freshservice 계정에서 이메일을 보내고 받을 수 있어야 합니다. SPF 설정에 문제가 있는 경우 각 제공업체별 구체적인 지침이 있습니다. 변경사항을 저장하기 전에 올바른 값을 사용해야 합니다.

## 주요 도메인 제공업체별 가이드

### GoDaddy
[DNS 관리 가이드](http://support.godaddy.com/help/article/680/managing-dns-for-your-domain-names)를 참조하여 SPF 레코드를 설정하세요.

### Namecheap
[SPF/TXT 레코드 추가 방법](https://www.namecheap.com/support/knowledgebase/article.aspx/317/78/how-do-i-add-spf-or-txt-records-for-my-domain)을 참조하세요.

### Hover
[DNS 레코드 편집 방법](https://help.hover.com/entries/21204757-how-to-edit-dns-records-a-cname-mx-txt-and-srv)을 확인하세요.

### Name.com
[SPF 설정 가이드](http://wiki.dreamhost.com/SPF)를 참조하세요.

## Pod별 SPF 레코드

Freshservice에서 제공하는 SPF 레코드에 포함된 조회가 너무 많은 경우 이 문제를 방지하기 위해 Pod별 SPF를 참조하세요.

### Pod US
[Sendgrid에서 Freshworks 이메일 서비스로 마이그레이션 (US)](https://support.freshservice.com/en/support/solutions/articles/50000002688-migrating-from-sendgrid-to-freshworks-email-service-us-)

### Pod EU  
[Sendgrid에서 Freshworks 이메일 서비스로 마이그레이션 (EU)](https://support.freshservice.com/en/support/solutions/articles/50000002689-migrating-from-sendgrid-to-freshworks-email-service-eu-)

### Pod AU
[Sendgrid에서 Freshworks 이메일 서비스로 마이그레이션 (AU)](https://support.freshservice.com/en/support/solutions/articles/50000002690-migrating-from-sendgrid-to-freshworks-email-service-au-)

### Pod IND
[Sendgrid에서 Freshworks 이메일 서비스로 마이그레이션 (IND)](https://support.freshservice.com/en/support/solutions/articles/50000002691-migrating-from-sendgrid-to-freshworks-email-service-ind-)

## SPF 레코드 검증

### 온라인 SPF 검사 도구

SPF 레코드가 올바르게 설정되었는지 확인하기 위해 온라인 검사 도구를 사용할 수 있습니다:

- MXToolbox SPF 검사
- SPF Record Checker
- DNS Checker

### 일반적인 SPF 오류

#### 1. 구문 오류
```
잘못된 예: v=spf1 include:email.freshservice.com all
올바른 예: v=spf1 include:email.freshservice.com ~all
```

#### 2. 조회 제한 초과
SPF 레코드는 최대 10개의 DNS 조회만 허용합니다. 너무 많은 include 문을 사용하면 오류가 발생할 수 있습니다.

#### 3. 중복 SPF 레코드
도메인당 하나의 SPF 레코드만 있어야 합니다. 여러 SPF 레코드가 있으면 모두 무효화됩니다.

## 고급 SPF 설정

### SPF 메커니즘

- **all**: 모든 IP 주소
- **include**: 다른 도메인의 SPF 레코드 포함
- **a**: 도메인의 A 레코드에 있는 IP 주소
- **mx**: 도메인의 MX 레코드에 있는 IP 주소
- **ip4**: 특정 IPv4 주소 또는 범위
- **ip6**: 특정 IPv6 주소 또는 범위

### SPF 한정자

- **+**: 통과 (기본값)
- **-**: 실패
- **~**: 소프트 실패
- **?**: 중립

### 복잡한 SPF 레코드 예시

```
v=spf1 ip4:192.0.2.0/24 include:_spf.google.com include:email.freshservice.com ~all
```

## 문제 해결

### SPF 레코드가 작동하지 않는 경우

1. **DNS 전파 확인**: 변경사항이 전파되는 데 최대 24시간이 걸릴 수 있습니다
2. **구문 검증**: SPF 레코드 구문이 올바른지 확인하세요
3. **조회 제한**: 10개 조회 제한을 초과하지 않았는지 확인하세요
4. **중복 레코드**: 중복 SPF 레코드가 없는지 확인하세요

### 이메일 전달 문제

SPF 레코드를 설정한 후에도 이메일 전달에 문제가 있는 경우:

1. **DKIM 설정**: 추가적인 이메일 인증을 위해 DKIM을 설정하세요
2. **DMARC 정책**: 이메일 보안을 강화하기 위해 DMARC를 구성하세요
3. **이메일 클라이언트 설정**: 이메일 클라이언트의 스팸 필터 설정을 확인하세요

:::warning 주의사항
- SPF 레코드 변경 시 기존 이메일 전달에 영향을 줄 수 있으므로 신중하게 진행하세요
- 변경 전에 현재 SPF 레코드를 백업해 두세요
- 테스트 이메일을 보내서 설정이 올바른지 확인하세요
:::