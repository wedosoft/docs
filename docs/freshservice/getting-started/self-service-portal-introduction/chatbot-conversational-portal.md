---
sidebar_position: 1
---

# 셀프 서비스 포털 챗봇 설정

:::info 문서 목적
이 문서는 "셀프 서비스 포털 챗봇 설정(Chatbot Conversational Portal)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
:::

## 개요

우수한 고객 경험을 만드는 요소는 무엇일까요? 셀프 서비스 포털의 챗봇을 통해 사용자와의 대화를 모방하는 인터페이스를 제공할 수 있어요.

Freddy 챗봇을 통해 문제를 보고하고, 서비스 카탈로그에서 항목을 요청하는 등 다양한 작업을 대화형으로 원활하게 수행할 수 있어요. 이는 동적 FAQ를 통해 상담원에게 불필요한 티켓을 줄이고, 고객 만족도를 향상시키며, 셀프 서비스 포털 사용률을 증가시킬 수 있어요.

:::warning 요금제 제한사항
**2020년 11월 2일 이전에 가입한 고객**의 Blossom, Garden, Estate & Forest 요금제에서 사용할 수 있어요.
:::

:::info MSP 계정 제한
대화형 포털은 MSP 계정에서는 사용할 수 없어요.
:::

## 대화형 포털 설정 방법

### 기본 설정

1. **챗봇 설정 페이지 이동**
   - `Admin > Channels > Chatbot`으로 이동해요

2. **챗봇 커스터마이징**
   - **이름**: 챗봇의 이름을 설정해요
   - **테마**: 포털에 맞는 색상 테마를 선택해요
   - **아바타**: 챗봇의 아바타 이미지를 설정해요

3. **셀프 서비스 활성화 옵션 선택**
   - **Enable Self-Service** 섹션에서 원하는 옵션을 선택해요
   - 예: 'Both conversational & Classic portal'을 선택해서 대화형 포털과 기존 포털 간 전환 가능

### Enable Self-Service 옵션

다음 세 가지 옵션 중 선택할 수 있습니다:

1. **Only Conversational**
   - 요청자가 Freddy가 포함된 대화형 셀프 서비스 포털에만 접근 가능

2. **Both Conversational & Requestor Portal**
   - 요청자가 대화형 포털(Freddy 포함)과 기존 포털 간 전환 가능

3. **Only Requester Portal**
   - 요청자가 기존 포털(Freddy 제외)에만 접근 가능

4. **실시간 미리보기**
   - **Preview on Portal**을 클릭하여 대화형 포털과 기존 포털의 모습을 우측에서 실시간으로 확인 가능

![챗봇 설정 인터페이스](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008601489/original/hOtQNu5U3Pa3PI7YieR3AyCyGZ8BwtfhQQ.png)

## 최종 사용자의 대화형 포털 사용법

관리자가 대화형 포털을 활성화하면, 최종 사용자는 지원 포털에 접속하여 우측 하단의 **"Ask Freddy"**를 클릭하여 챗봇과 대화할 수 있습니다.

## 대화형 포털용 서비스 항목 설정

### 서비스 항목 생성 및 설정

1. **서비스 카탈로그 페이지 이동**
   - `Admin > Service Management > Service Request Management > Service Catalog > Add New > Service Item`으로 이동합니다

2. **Bot Ready 기능 활성화**
   - **Custom Fields** 탭에서 **"Make it Bot Ready"** 토글을 활성화합니다

3. **사용자 지정 필드 구성**
   - 사용자 지정 필드(예: Date)를 드래그 앤 드롭합니다
   - 다음 속성을 입력합니다:
     - **Behavior**: 필드 동작 방식
     - **Field Name**: 필드 이름
     - **Drop-down values**: 드롭다운 값들

4. **Freddy 질문 설정**
   - **"What question should Freddy ask?"** 필드를 작성합니다
   - Freddy가 요청을 처리하기 위해 적절한 질문을 할 수 있도록 설정합니다
   - **Done** 버튼을 클릭하여 완료합니다

![서비스 항목 Bot Ready 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/46354843/original/wlxHqrgvasyciMCuBf8119adKhVHF111zQ.png)

### 대화형 미리보기

**Chat 아이콘**을 클릭하여 대화형 포털에서 필드들이 어떻게 표시되는지 미리 볼 수 있습니다.

![대화형 포털 미리보기](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008601542/original/7MI3MrfkGNzxskBoF4adDXpdP79WjTAl4Q.png)

## 주요 기능

:::tip 챗봇의 장점
- **사용자 경험 향상**: 자연스러운 대화형 인터페이스로 직관적인 지원 요청
- **티켓 감소**: 동적 FAQ를 통해 불필요한 티켓 생성 방지
- **셀프 서비스 증진**: 사용자가 스스로 문제를 해결할 수 있는 환경 제공
- **고객 만족도 향상**: 빠르고 편리한 서비스 요청 프로세스
:::

