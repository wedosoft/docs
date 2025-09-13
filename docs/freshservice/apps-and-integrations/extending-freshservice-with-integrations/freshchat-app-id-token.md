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

