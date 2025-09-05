---
sidebar_position: 2
---

# 구성 세트 (Config Sets)

구성 세트를 사용하여 한 인스턴스에서 다른 인스턴스로 구성을 전송할 수 있습니다. 예를 들어, Sandbox 인스턴스에서 새로운 워크플로 자동화를 생성하고 테스트한 다음, 구성 세트를 사용하여 프로덕션으로 동기화할 수 있습니다.

:::info 중요 사항
- 구성 세트를 사용하여 **관리자 구성만** 동기화할 수 있습니다
- TCPR(티켓, 연락처, 문제, 릴리스) 레코드는 동기화할 수 없습니다
:::

:::note 새 Sandbox 정보
이 문서는 현재 Enterprise 요금제 고객에게 활성화된 새로운 Sandbox에 관한 내용입니다. Freshservice의 현재 Sandbox 버전에 대해서는 [여기](https://support.freshservice.com/en/support/solutions/articles/240613)를 클릭하세요. 단계적 폐지 계획에 대한 자세한 내용은 [여기](https://support.freshservice.com/en/support/solutions/articles/50000009922)를 참고하세요.
:::

## 구성 세트 관리 권한

### 글로벌 설정에서:
- **Play God 관리자만** 구성 세트를 사용하여 구성을 보기, 생성 및 동기화할 수 있습니다
- 글로벌 설정의 모듈 구성만 추가하고 동기화할 수 있습니다

### 워크스페이스 설정에서:
- **Play God 관리자와 워크스페이스 관리자 모두** 구성 세트를 사용하여 구성을 보기, 생성 및 동기화할 수 있습니다
- 워크스페이스 설정의 모듈 구성만 추가하고 동기화할 수 있습니다
- 글로벌 구성은 직접 추가할 수 없지만 종속성 확인의 일부로 추가할 수 있습니다
- 구성 세트에 종속성 확인의 일부로 추가된 글로벌 구성이 포함된 경우, **Play God 관리자만** 해당 구성 세트를 동기화할 수 있습니다

## 구성 세트를 사용한 변경사항 동기화

**아웃바운드 구성 세트**는 로그인한 Freshservice 인스턴스(예: Sandbox)에서 생성되어 다른 인스턴스(예: 프로덕션)로 동기화하려는 경우에 사용됩니다. 일반적으로 sandbox에서 생성하고 테스트한 구성을 프로덕션 인스턴스로 동기화할 때 사용됩니다.

:::warning 구성 세트 제한사항
구성 세트는 종속성을 포함하여 **최대 250개의 구성**을 포함할 수 있습니다. 동기화 요구사항이 250개를 초과하는 경우, 여러 구성 세트로 나누는 것이 좋습니다.
:::

## 구성 세트 생성 및 동기화 단계

### 1단계: 구성 세트 생성
소스 인스턴스(예: Sandbox)에서 대상 인스턴스로 변경사항을 동기화하려면:

1. 소스 인스턴스에서 **관리자 > Sandbox**로 이동

![Sandbox 메뉴](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869755/original/j_-wSaDcRXddUhXIEP1Rn1OujKGPDvOhhA.png?1715953407)

![Sandbox 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869757/original/G05-OAQwlJsniZYwQafYYSjKycStcdoVHA.png?1715953407)

### 2단계: 아웃바운드 동기화 설정
1. **'아웃바운드 동기화'** 탭으로 이동하여 **'구성 세트 생성'** 버튼 클릭
2. 필요한 세부 정보(이름, 설명, 소스, 대상) 입력 후 **'생성'** 클릭

![구성 세트 생성](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869760/original/S3BhHTEmy7lYScC1uH0wqKzipDMb80w3ow.png?1715953408)

![구성 세트 상세 정보](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869761/original/MGDjdvM7dTuIuyKmV3u2xFuBdav6_0u6Sw.png?1715953408)

### 3단계: 동기화할 모듈 선택
화면 왼쪽에서 동기화가 지원되는 모든 모듈을 확인할 수 있습니다.

![지원 모듈 목록](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869762/original/UaScSmkDlfejSKxRV7CkaccJVNfuOPvgyQ.png?1715953409)

### 4단계: 구성 선택 및 추가
1. 원하는 모듈로 이동하여 체크박스를 사용해 필요한 구성 선택
2. 필터를 사용하여 검색 범위 좁히기 가능
3. 선택한 구성을 목록에 추가하고 **'저장 후 계속'** 클릭

![구성 선택](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869758/original/5_bkxJ4_zAXIM3iCjouC-tQ94IGeGzflMA.png?1715953408)

### 5단계: 종속성 확인
시스템이 빠른 [종속성](https://support.freshservice.com/en/support/solutions/articles/50000009718) 확인을 실행하여 필요한 종속성을 추가하고 참조용으로 나열합니다.

![종속성 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869759/original/zeKSc_kcIaUwnZPEWmFGNikmgUW6f1mK8A.png?1715953408)

:::warning 종속성 추가 필수
모든 종속성을 검토하고 구성 세트에 추가해야 합니다. 계속 진행하려면 **모든 필수 종속성을 추가하는 것이 필수입니다**.
:::

### 6단계: 동기화 실행
1. 구성이 구성 세트에 추가되면 Freshservice에서 구성 목록 미리보기 제공
2. 구성 수준에서 동기화가 추가되는지 업데이트되는지 확인 가능
3. **"구성 동기화"** 클릭하여 동기화 시작

![동기화 미리보기](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869763/original/aM_6APOaiWOkJB9NW_1BmaxMtubvjUGppA.png?1715953409)

### 7단계: 동기화 완료 확인
- 구성의 수와 복잡성에 따라 동기화는 몇 초에서 몇 분이 소요될 수 있습니다
- 동기화 완료 시 이메일로 알림을 받게 됩니다
- 대상 인스턴스(예: 프로덕션)의 '[인바운드 동기화](https://support.freshservice.com/en/support/solutions/articles/50000009721)' 탭에서 동기화 상태를 추적할 수 있습니다

![동기화 완료](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869765/original/ieANM8ztKUMhSGgg6oJATwr2fBGyvY3Tvw.png?1715953413)

:::info 동기화 후 참고사항
동기화가 완료되면 구성 세트는 동기화 기록 역할을 합니다. **편집이나 삭제가 불가능합니다**.
:::

## 구성 세트에서 구성 추가/제거

더 많은 변경이 예상되는 경우 구성 세트를 초안 상태로 유지할 수 있습니다. 이러한 모든 구성 세트는 '동기화 상태' = '시작되지 않음'으로 '아웃바운드 동기화' 탭에서 찾을 수 있습니다.

### 구성 세트 편집 방법:
1. **'아웃바운드 동기화'** 탭에서 편집하려는 구성 세트 클릭

![구성 세트 편집](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869764/original/pOeopLzlqDkmWMnWY3dq5MWWTXuAA5GGZQ.png?1715953412)

2. 미리 선택된 구성 목록이 표시됩니다
3. 구성을 추가하거나 제거할 수 있습니다
4. 변경사항 적용 후 과정이 반복됩니다 ('구성 세트를 사용한 변경사항 동기화' 섹션 참조)

![구성 목록 편집](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011869766/original/QdEi8HyFTVOyruS9TYXr0vgrOjD_gyc2Rw.png?1715953413)
