---
id: merging-requesters
title: 요청자 병합 가이드
sidebar_label: 요청자 병합 가이드
---

<div className="subtitle">
  이 문서는 Freshservice에서 중복된 요청자 계정을 하나로 통합하는 방법을 안내하는 문서입니다.
</div>

## 개요

사용자가 여러 이메일 주소로 요청을 보낼 때 Freshservice에서 중복된 요청자 항목이 생성될 수 있습니다. 이는 요청 추적을 어렵게 만들고 상담원의 업무 효율성을 떨어뜨릴 수 있습니다. 

Freshservice는 이러한 중복 요청자를 하나의 기본 항목으로 병합할 수 있는 기능을 제공합니다.

## 요청자 병합 단계

### 1단계: 요청자 관리 페이지 접속

**단일 워크스페이스 계정:**
- **Admin** > **User Management** > **Requesters**로 이동

**멀티 워크스페이스 계정:**
- **Admin** > **Global Settings** > **User Management** > **Requesters**로 이동

### 2단계: 기본 요청자 선택

1. 기본(primary) 요청자의 프로필을 클릭
2. 드롭다운 아이콘을 클릭
3. **Merge** 옵션 선택

### 3단계: 병합할 요청자 선택

1. 보조(secondary) 또는 중복 요청자를 검색
2. '+' 아이콘을 사용하여 병합할 요청자들을 선택

### 4단계: 병합 실행

1. **Proceed** 클릭
2. 모든 요청자를 선택한 후 **Continue and Merge** 클릭

![Freshservice 요청자 병합 과정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008082343/original/NCwO78o4BTLdPwF58hS9IcRNMli4ieGiqQ.gif?1681213336)

## 병합 후 변경사항

요청자 병합이 완료되면 다음과 같은 변경사항이 적용됩니다:

### 데이터 통합
- **티켓, 문제, 변경, 릴리스, 승인, 태그** 등 모든 관련 데이터가 기본 요청자로 이동

### 이메일 처리
- 보조 이메일 ID로 제출된 티켓의 경우, 상담원의 모든 답변은 해당 보조 이메일로 전송
- 티켓의 요청자는 기본 요청자로 표시

### 조직 정보 통합
- 보조 요청자의 **부서, 그룹, CAB** 정보가 기본 요청자에게 병합

### 기본 이메일 설정
- 가장 먼저 인증된 이메일 ID가 기본 이메일이 됨

### 데이터 보완
- 기본 요청자에게 누락된 필드가 있는 경우, 첫 번째 보조 요청자의 데이터로 자동 업데이트

:::info 고급 시나리오
더 복잡한 사용자 병합 시나리오에 대한 자세한 내용은 [고급 시나리오 가이드](https://support.freshservice.com/support/solutions/articles/50000010164-merging-users-in-freshservice-advanced-scenarios-)를 참고하세요.
:::

:::warning 주의사항
- 병합은 되돌릴 수 없는 작업입니다
- 병합 전에 데이터를 신중히 검토하세요
- 기본 요청자 선택 시 가장 완전한 정보를 가진 계정을 선택하는 것이 좋습니다
:::

## 관련 문서

- [요청자 관리 기본 가이드](../user-management)
- [사용자 계정 생성 및 관리](./creating-users)
- [사용자 역할 및 권한 설정](./user-roles-permissions)
