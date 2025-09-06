---
id: automatically-associating-contacts-companies
title: 연락처-회사 자동 연결 설정 가이드
sidebar_label: 연락처-회사 자동 연결 설정 가이드
---

<div className="subtitle">
  이 문서는 Freshservice에서 이메일 도메인을 기반으로 새로운 연락처(요청자)를 회사(부서)에 자동으로 연결하는 방법을 안내하는 문서입니다.
</div>

## 개요

새로운 연락처(또는 요청자)가 생성될 때, 이메일 주소의 도메인을 기반으로 회사(또는 부서)에 자동으로 연결할 수 있습니다.

### 예시
이메일 주소가 `cedric.diggory@hogwarts.edu`인 새로운 연락처 Cedric Diggory는 이메일 주소의 `hogwarts.edu` 도메인을 기반으로 Hogwarts 회사에 자동으로 연결될 수 있습니다.

## 자동 연결 설정 단계

### 1단계: 회사 관리 페이지 접속

**Admin** > **User Management** > **Companies**로 이동합니다.

![회사 관리 페이지](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965545/original/74fJSRdz8uUsRmbymeCaIV9XL_zkG2IIsg.png?1547785433)

### 2단계: 회사 편집

자동 연결을 설정할 회사 옆의 **편집 아이콘**을 클릭합니다.

![회사 편집 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965548/original/C5RYpAIUY7D1j4NanniXTp1M_hJY4z7anA.png?1547785455)

### 3단계: 도메인 추가

1. **"Domains"** 입력 필드까지 스크롤
2. 사용자를 해당 회사에 자동으로 연결할 **이메일 도메인** 입력
3. 도메인 입력 후 **스페이스** 또는 **엔터**를 눌러 필드에 항목으로 추가

![도메인 입력 필드](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/43191011/original/zGm7pJzRAhDthFlWY2Xonz1sSCmoD40hcQ.png?1548764644)

### 4단계: 변경사항 저장

위로 스크롤하여 **"Update"** 버튼을 클릭하여 변경사항을 확인합니다.

![업데이트 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/42965979/original/NXCY2Zvy4rQ9xqzwucc_Sdmn5nHaByjnpg.png?1547786855)

## 자동 연결 작동 방식

### 새로운 연락처

지정된 도메인이 포함된 이메일 주소로 생성되는 모든 새로운 연락처는 자동으로 해당 회사에 연결됩니다.

### 기존 연락처

기존 연락처에 해당 도메인의 추가 이메일 주소가 추가되는 경우에도 자동으로 회사에 연결됩니다.

## 중요 사항

:::warning 연결 해제 시 주의사항
회사에서 도메인을 연결 해제해도 해당 이메일 도메인을 가진 모든 사용자가 자동으로 회사에서 연결 해제되지는 않습니다.
:::

:::info 적용 범위
- **신규 연락처**: 설정 후 생성되는 연락처에만 적용
- **기존 연락처**: 기존 연락처의 새 이메일 추가 시에만 적용
- **소급 적용 없음**: 이미 존재하는 연락처는 자동으로 재연결되지 않음
:::

## 활용 사례

### 조직 관리

- **대기업**: 부서별 이메일 도메인 관리
- **교육기관**: 학과별 또는 캠퍼스별 자동 분류
- **병원**: 진료과별 또는 병원별 자동 연결

### 서비스 제공업체

- **MSP**: 고객사별 자동 분류
- **컨설팅**: 프로젝트별 또는 클라이언트별 관리
- **소프트웨어**: 고객사별 지원 요청 자동 분류

## 모범 사례

### 도메인 관리

- **정확한 도메인 입력**: 오타 방지를 위한 이중 확인
- **서브도메인 고려**: 필요 시 서브도메인별 설정
- **정기적 검토**: 도메인 목록의 정기적인 업데이트

### 조직 구조 반영

- **계층 구조**: 조직의 실제 계층 구조를 반영한 설정
- **권한 관리**: 각 회사별 적절한 권한 설정
- **명확한 분류**: 중복되지 않는 명확한 회사 분류

### 유지보수

- **변경 이력 관리**: 도메인 변경 이력 문서화
- **사용자 안내**: 자동 연결 정책에 대한 사용자 안내
- **예외 처리**: 자동 연결이 부적절한 경우의 수동 처리 방안

:::note 팁
- 여러 도메인을 한 번에 추가할 수 있습니다
- 도메인 설정 전에 조직의 이메일 도메인 구조를 미리 파악하세요
- 테스트 계정으로 설정이 올바르게 작동하는지 확인하세요
:::

## 관련 문서

- [회사 및 부서 관리](./managing-companies-departments)
- [요청자 관리 기본 가이드](./managing-requesters)
- [사용자 관리 모범 사례](./user-management-best-practices)
- [부서 커스텀 필드 추가](./adding-custom-fields-departments)
