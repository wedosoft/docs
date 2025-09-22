---
sidebar_position: 14
---

# 티켓 목록 뷰 개선 사항

티켓 뷰의 유연성과 견고성을 향상시키기 위해 티켓 목록 뷰에 몇 가지 새로운 기능을 도입하게 되어 기쁩니다.

## 정렬

이제 선호도에 따라 티켓 목록을 쉽게 정리할 수 있습니다. 헤드라인을 탭하기만 하면 오름차순과 내림차순 순서를 전환할 수 있습니다.

**참고:** 다음 필드는 제외되며 정렬할 수 없습니다: 상태, 할당 대상, 사용자 정의 텍스트 필드 및 다중 선택 드롭다운 필드.

## 페이지당 레코드 수 구성

이제 사용자는 모든 뷰에서 단일 페이지에 표시되는 레코드 수를 사용자 정의할 수 있습니다. 최소 30개에서 최대 100개 레코드 중에서 선택하여 효율적인 보기 경험을 제공합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011469964/original/eOrHH6AHfO0CItvw4zKSELd5ZinsX21jgw.png?1712561274" style={{width: '624px', height: '364px', maxWidth: '100%'}} />

## 고급 필터 도입

티켓 뷰를 더욱 세분화하기 위해 필터를 '기본' 및 '고급' 섹션으로 분류했습니다.

'고급 필터' 섹션에서 다음과 같은 개선 사항을 찾을 수 있습니다:

### 필드 유형에서 지원하는 추가 매개변수

필드 유형별 필터링은 이제 에이전트, 상태 등과 같은 특정 필드에 대해 '포함' 및 '제외' 옵션을 모두 제공하여 제외 목록을 만들 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011469963/original/HEMJ2ZW-ZNJRGaW-DcrS688NhmTynrj_0Q.png?1712561274" style={{width: '624px', height: '364px', maxWidth: '100%'}} />

- '단일 또는 다중 선택' 드롭다운 필드에 대한 포함 또는 제외
- '체크박스' 필드에 대해 선택된 값 '입니다'
- 날짜 필드에 대해 켜짐/사이/마지막/다음 내
- 숫자/소수 필드에 대해 같음/같지 않음/크거나 같음/작거나 같음
- 종속 필드에 대해 입니다/포함/제외

**참고:** "입니다" 매개변수를 선택하면 에이전트가 다음 수준의 필터를 추가할 수 있습니다.

### 모든 또는 모든 조건 일치

모든 필터 조건 중 '모든' 또는 '모든'을 선택하여 티켓 목록을 더 세밀하게 제어할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011469965/original/PXM9CCH6jDWbxwMRgHj4d3BVGlmkyNBhPQ.png?1712561274" style={{width: '624px', height: '364px', maxWidth: '100%'}} />

## 연관 기반 필터

연관을 기반으로 하는 필터를 도입하여 요청자, 연관된 자산, 서비스 항목 및 영향받는 서비스를 기반으로 티켓을 필터링할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011469966/original/cLkNJx6TX-4JNBnD_WCSYdnwzj54ENEAHA.png?1712561274" style={{width: '624px', height: '407px', maxWidth: '100%'}} />

### 지원되는 연관 필드 목록

- **서비스 항목**: 항목 이름, 항목 카테고리
- **요청자**: 부서, 위치, 그룹, VIP
- **연관된 자산**: 이름, 유형, 관리자, 관리자 그룹
- **영향받는 서비스**: 이름, 유형, 관리자, 관리자 그룹

:::warning 참고사항
1. '요청자'를 제외하고 나머지 연관 필드에 대해서는 한 번에 하나의 매개변수만 선택할 수 있습니다
2. 목록 뷰에 업데이트된 값이 반영되는 데 5-7초가 걸립니다
3. 목록 뷰는 최대 10,000개의 티켓으로 제한됩니다. 내보내기 중에는 각 파일이 다시 10,000개의 티켓 목록을 허용하고 여러 파일로 내보내집니다
:::