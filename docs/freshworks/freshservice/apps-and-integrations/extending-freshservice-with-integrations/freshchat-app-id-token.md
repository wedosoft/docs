---
sidebar_position: 2
---

# Freshchat 앱 ID와 토큰 확인

Freshservice와 Freshchat 통합을 위해 필요한 앱 ID와 토큰을 확인하는 방법을 안내합니다.

:::info 통합 전 준비사항
Freshchat 계정과 Freshservice 계정에 모두 관리자 권한이 있어야 합니다.
:::

## 앱 ID 및 토큰 확인 방법

### 1단계: Freshchat 관리자 설정 접근
1. **Freshchat 계정**에 로그인
2. **Admin** 설정으로 이동
3. **Chat settings** → **Chat widget settings** 클릭

### 2단계: 계정 설정 메뉴 이동
1. **Setup** 섹션 하위의 **Account Settings** 클릭

![Freshchat 계정 설정 메뉴](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008303824/original/3hoahMp_QZ_R_lCt5zE-umvR2FR5X64uhw.png?1683599982)

### 3단계: 통합 설정에서 ID 및 토큰 확인
1. **Integration Settings** 메뉴로 이동
2. **App ID**와 **Web Messenger Token** 확인 및 복사

![Freshchat 앱 ID와 토큰 위치](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008303830/original/d2Teqm7HqSic0ounGE72RwL4XgHm-Qfs6w.png?1683600031)

:::tip 정보 보안
앱 ID와 토큰은 민감한 정보입니다. 안전한 곳에 보관하고 필요한 담당자에게만 공유하세요.
:::

## 실무 활용 예시

### 상황 1: 신규 Freshchat 통합 설정
**목표**: Freshservice와 Freshchat 간 채팅 연동 구축
**방법**: 
1. 위 단계를 통해 앱 ID와 토큰 확인
2. Freshservice 통합 설정에서 해당 정보 입력
3. 연동 테스트 실행

**결과**: 고객이 Freshchat으로 문의한 내용이 Freshservice 티켓으로 자동 생성

### 상황 2: 토큰 갱신이 필요한 경우
**목표**: 만료된 토큰으로 인한 연동 오류 해결
**방법**:
1. Integration Settings에서 새 토큰 생성
2. Freshservice 설정에서 토큰 업데이트
3. 연동 상태 확인

**결과**: 정상적인 채팅-티켓 연동 복구

## 문제 해결

### 자주 발생하는 문제

#### 문제: 앱 ID나 토큰이 보이지 않음
**원인**: Freshchat 관리자 권한 부족
**해결**: 
1. 계정 권한 확인 (Account Owner 또는 Admin 권한 필요)
2. 다른 관리자에게 권한 요청
3. Freshchat 고객지원팀 문의

#### 문제: 토큰이 유효하지 않다는 오류
**원인**: 토큰 만료 또는 복사 오류
**해결**:
1. Integration Settings에서 토큰 재생성
2. 복사 시 공백이나 특수문자 포함 여부 확인
3. 새로운 토큰으로 재설정

:::success 통합 준비 완료
앱 ID와 토큰을 성공적으로 확인했습니다. 이제 Freshservice에서 Freshchat 통합을 설정할 수 있습니다.
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [Freshchat 통합 설정 가이드](./freshchat-integration-setup)
- [채팅 위젯 설정](./chat-widget-configuration)
- [통합 문제 해결](./integration-troubleshooting)
-->
